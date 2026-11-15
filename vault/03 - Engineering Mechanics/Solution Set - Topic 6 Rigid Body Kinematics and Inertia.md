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

---

## Problem RB-02: Kinematics (3 conditions)

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** one rigid body whose position and attitude are tied to a single angle $\theta$ by the three geometric conditions of the statement.
* **Fixed frame:** $S_0\{O; \mathcal B_0\}$ is the frame $Oxyz$ of the statement, with right-handed basis $\{\mathbf i, \mathbf j, \mathbf k\}$.
* **Body frame:** $S_B\{P; \mathcal B_B\}$ is the frame $Px_By_Bz_B$ of the statement, with origin at the body point $P$ and right-handed basis $\{\mathbf i_B, \mathbf j_B, \mathbf k_B\}$ along the axes $Px_B$, $Py_B$, $Pz_B$.
* **Intermediate basis:** $\mathcal B_1\{\mathbf i_1, \mathbf j_1, \mathbf k_1\}$, obtained from $\mathcal B_0$ by the first elementary rotation, about $\mathbf k$; the body basis is obtained from $\mathcal B_1$ by the second one, about $\mathbf i_1$.
* **How each condition is read:**
  1. *The point $P$ is located along $Oy$.* Its first and third coordinates are zero, so $P$ lies in the plane $Oxy$ at a distance from $O$ that changes with time.
  2. *The axis $Px_B$ passes through $A(a, 0, 0)$.* Both $P$ and $A$ lie in the plane $Oxy$, so the whole line $Px_B$ lies in that plane: $\mathbf i_B$ is horizontal. Its sense is read as pointing from $P$ towards $A$.
  3. *The angle between $Py_B$ and the plane $Oxy$ equals the angle between $Ox$ and $Px_B$, and both are $\theta$.* The first angle fixes how far $\mathbf j_B$ is lifted out of the plane $Oxy$; since $\mathbf i_B$ stays in that plane, the lift is a rotation about $\mathbf i_B$ itself. The second angle fixes the direction of the horizontal line $Px_B$.
* **Senses chosen (reading of the statement, which gives only the size of the angles):** for positive $\theta$ the point $P$ is on the positive half of $Oy$, so the axis $Px_B$, going from $P$ down to $A$, is turned clockwise from $Ox$ when seen from the positive end of $Oz$; and $\mathbf j_B$ is lifted towards positive $z$. The official key confirms both choices (see Answers and Checks).
* **Degrees of freedom:** a free rigid body has six (Notes.pdf, Sec. 9.3). Condition 1 removes two (two coordinates of $P$), condition 2 removes two (the direction of $Px_B$ is that of the segment from $P$ to $A$), and condition 3 removes one (the rotation about $Px_B$ is tied to the direction of $Px_B$). One degree of freedom is left, the angle $\theta$.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Position of the fixed point $A$ | $(a, 0, 0)$ | m |
| Coordinate of the body | $\theta(t)$ | rad |
| Its rate | $\dot\theta(t)$ | rad/s |

* **Unknowns:** the angular velocity of the body and the velocity of $P$, as functions of $\theta$ and its rate.
* **Plan:** the position of $P$ comes from the right triangle $OPA$; the body basis comes from two elementary rotations, each drawn looking down its axis; the angular velocity is the sum of the angular velocities of the two rotations (additivity, Notes.pdf, Eq. 3.14); the velocity of $P$ is the time derivative of its position vector.

### Change of Basis, Position Vectors and Constraint Kinematics

#### Position of the point P

![[attachments/EM-SOL/rb02-triangle-opa.svg]]

> [!derivation] Position of P from the right triangle OPA
> **Law:** right-triangle trigonometry in the plane $Oxy$ (conditions 1, 2 and the second half of condition 3)
> **Source:** Problems.pdf, p. 37; Notes.pdf, Sec. 9.3
>
> The triangle $OPA$ has its right angle at $O$, because $A$ is on $Ox$ and $P$ is on $Oy$. The line $AP$ is the axis $Px_B$, so the interior angle at $A$, between $Ox$ and $Px_B$, is $\theta$. With respect to that angle the leg $OA$ is adjacent, the leg $OP$ is opposite and $PA$ is the hypotenuse.
>
> $$\begin{aligned}
> \lvert OA\rvert &= a \quad &\text{(adjacent leg: $A$ is on $Ox$ at the distance $a$ from $O$)} \\
> \lvert OP\rvert &= y_P \quad &\text{(opposite leg: $P$ is on $Oy$, at the coordinate $y_P$)} \\
> \tan\theta &= \frac{\lvert OP\rvert}{\lvert OA\rvert} = \frac{y_P}{a} \quad &\text{(tangent: opposite leg over adjacent leg)} \\
> y_P &= a\tan\theta \quad &\text{(solve for $y_P$)} \\
> \lvert PA\rvert &= \frac{\lvert OA\rvert}{\cos\theta} = \frac{a}{\cos\theta} \quad &\text{(cosine: adjacent leg over hypotenuse, solved for the hypotenuse)} \\
> \mathbf r_0^P &= y_P\,\mathbf j = a\tan\theta\,\mathbf j \quad &\text{(condition 1: only the second coordinate is non-zero)} \\
> \mathbf{PA} &= \mathbf r_0^A - \mathbf r_0^P = a\,\mathbf i - a\tan\theta\,\mathbf j \quad &\text{(head minus tail)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = a\tan\theta\,\mathbf j, \qquad \mathbf{PA} = a\,\mathbf i - a\tan\theta\,\mathbf j, \qquad \lvert PA\rvert = \frac{a}{\cos\theta}}$$
>
> **Units:** $[\mathrm L]$ in every term; $\tan\theta$ and $\cos\theta$ are dimensionless
> **Meaning:** as the angle grows from zero towards a right angle, $P$ slides along $Oy$ from $O$ to infinity, so that the line from $P$ to the fixed point $A$ turns away from $Ox$.

#### First elementary rotation: about k

![[attachments/EM-SOL/rb02-rotation-k.svg]]

> [!derivation] First rotation: about k by the angle minus theta
> **Law:** simple rotation about the third axis; the rotated first axis is the unit vector of the segment from $P$ to $A$
> **Source:** Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; [Lecture 7, Slide 12]
>
> View with $\mathbf k$ out of the paper (⊙), $\mathbf i$ to the right and $\mathbf j$ up. The unit vector $\mathbf i_1$ points from $P$ to $A$; it is turned by $\theta$ clockwise from $\mathbf i$, which is the negative sense of the right-hand rule about $\mathbf k$ (thumb out of the paper, fingers counterclockwise). The rotation angle is therefore minus $\theta$.
>
> $$\begin{aligned}
> \mathbf i_1 &= \frac{\mathbf{PA}}{\lvert PA\rvert} = \frac{\cos\theta}{a}\,(a\,\mathbf i - a\tan\theta\,\mathbf j) \quad &\text{(unit vector: divide by the hypotenuse of the previous box)} \\
> &= \cos\theta\,\mathbf i - \sin\theta\,\mathbf j \quad &\text{(right triangle of hypotenuse 1: adjacent leg along $\mathbf i$, opposite leg along $-\mathbf j$ because the turn is clockwise)} \\
> \mathbf k_1 &= \mathbf k \quad &\text{(the rotation axis does not move)} \\
> \mathbf j_1 &= \mathbf k_1\times\mathbf i_1 = \cos\theta\,(\mathbf k\times\mathbf i) - \sin\theta\,(\mathbf k\times\mathbf j) \quad &\text{(right-handed basis; distribute the product)} \\
> &= \sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{($\mathbf k\times\mathbf i = \mathbf j$ and $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> [{}_0R_1] &= \begin{bmatrix} \cos\theta & \sin\theta & 0 \cr -\sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot(\cos\theta\cos\theta - \sin\theta\,(-\sin\theta)) = \cos^2\theta + \sin^2\theta = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\theta + \sin^2\theta & -\cos\theta\sin\theta + \sin\theta\cos\theta & 0 \cr -\sin\theta\cos\theta + \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = [{}_0R_1(z, -\theta)] = \begin{bmatrix} \cos\theta & \sin\theta & 0 \cr -\sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** this is Eq. 1.20 with the angle minus $\theta$: the minus sign of the sine moves to the first column, because the rotated first axis leans towards $-\mathbf j$ in a clockwise turn. The axis $\mathbf i_1$ already has the final direction of $Px_B$.

#### Second elementary rotation: about i1

![[attachments/EM-SOL/rb02-rotation-i1.svg]]

> [!derivation] Second rotation: about i1 by the angle theta
> **Law:** simple rotation about the first axis; angle between a line and a plane
> **Source:** Notes.pdf, Eq. 1.18; Notes.pdf, Eq. 1.15; [Lecture 7, Slide 12]
>
> View with $\mathbf i_1$ out of the paper (⊙), $\mathbf j_1$ to the right and $\mathbf k_1$ up (since $\mathbf j_1\times\mathbf k_1 = \mathbf i_1$); the trace of the plane $Oxy$ is the horizontal line along $\mathbf j_1$. Turning about $\mathbf i_1$ keeps $\mathbf i_B$ horizontal, as condition 2 requires; a counterclockwise turn (positive by the right-hand rule) lifts $\mathbf j_B$ towards positive $z$.
>
> $$\begin{aligned}
> \mathbf i_B &= \mathbf i_1 \quad &\text{(the rotation axis does not move)} \\
> \mathbf j_B &= \cos\theta\,\mathbf j_1 + \sin\theta\,\mathbf k_1 \quad &\text{(hypotenuse 1: adjacent leg along $\mathbf j_1$, opposite leg along $\mathbf k_1$)} \\
> \mathbf k_B &= -\sin\theta\,\mathbf j_1 + \cos\theta\,\mathbf k_1 \quad &\text{($\mathbf k_1$ turned counterclockwise leans towards $-\mathbf j_1$: opposite leg $\sin\theta$ along $-\mathbf j_1$)} \\
> \mathbf j_B\cdot\mathbf k &= \sin\theta \quad &\text{(component of $\mathbf j_B$ along the normal $\mathbf k = \mathbf k_1$ of the plane $Oxy$)} \\
> \widehat{(Py_B,\,Oxy)} &= \arcsin\lvert\mathbf j_B\cdot\mathbf k\rvert = \theta \quad &\text{(the angle between a line and a plane is the complement of the angle with the normal: condition 3 holds)} \\
> [{}_1R_B] &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos\theta & -\sin\theta \cr 0 & \sin\theta & \cos\theta \end{bmatrix} \quad &\text{(columns: $\mathbf i_B$, $\mathbf j_B$, $\mathbf k_B$ in $\mathcal B_1$)} \\
> \det[{}_1R_B] &= 1\cdot(\cos^2\theta + \sin^2\theta) = 1 \quad &\text{(expand along the first row)} \\
> [{}_1R_B][{}_1R_B]^T &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos^2\theta + \sin^2\theta & \cos\theta\sin\theta - \sin\theta\cos\theta \cr 0 & \sin\theta\cos\theta - \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta \end{bmatrix} = [U] \quad &\text{(row by row products)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_B] = [{}_1R_B(x, \theta)] = \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos\theta & -\sin\theta \cr 0 & \sin\theta & \cos\theta \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** the same angle appears in both rotations because condition 3 makes the lift of $Py_B$ equal to the turn of $Px_B$; the body attitude is a one-parameter family.

> [!derivation] Composed matrix and check of condition 3
> **Law:** composition of changes of basis; matrix product row by column
> **Source:** Notes.pdf, Eq. 1.16; Notes.pdf, Eq. 1.15
>
> Abbreviations: $c$ and $s$ stand for the cosine and sine of $\theta$.
>
> $$\begin{aligned}
> [{}_0R_B] &= [{}_0R_1][{}_1R_B] \quad &\text{(Eq. 1.16: first rotation on the left)} \\
> [\mathbf i_B]_0 &= \text{column 1 of } [{}_0R_1] = (c,\ -s,\ 0) \quad &\text{(first column of $[{}_1R_B]$ is $(1, 0, 0)$)} \\
> [\mathbf j_B]_0 &= c\,(s,\ c,\ 0) + s\,(0,\ 0,\ 1) = (cs,\ c^2,\ s) \quad &\text{($c$ times column 2 plus $s$ times column 3 of $[{}_0R_1]$)} \\
> [\mathbf k_B]_0 &= -s\,(s,\ c,\ 0) + c\,(0,\ 0,\ 1) = (-s^2,\ -sc,\ c) \quad &\text{($-s$ times column 2 plus $c$ times column 3)} \\
> \det[{}_0R_B] &= \det[{}_0R_1]\,\det[{}_1R_B] = 1\cdot 1 = 1 \quad &\text{(determinant of a product)} \\
> \mathbf i_B\cdot\mathbf i &= c \quad &\text{(first component of $\mathbf i_B$: the angle between $Ox$ and $Px_B$ is $\theta$)} \\
> \mathbf i_B\cdot\mathbf k &= 0 \quad &\text{(third component: $Px_B$ stays in the plane $Oxy$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_B] = \begin{bmatrix} \cos\theta & \sin\theta\cos\theta & -\sin^2\theta \cr -\sin\theta & \cos^2\theta & -\sin\theta\cos\theta \cr 0 & \sin\theta & \cos\theta \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** the three columns satisfy the three conditions of the statement at every instant, so the basis built is the body basis of the problem.

#### Angular velocity by additivity

> [!derivation] Angular velocity of the first rotation, checked with the derivative of i1
> **Law:** a simple rotation has the angular velocity of the rate of its angle along its axis; Poisson formula
> **Source:** Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 9.16; [Lecture 7, Slide 12]
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \frac{d(-\theta)}{dt}\,\mathbf k = -\dot\theta\,\mathbf k \quad &\text{(rotation angle minus $\theta$ about $\mathbf k$)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \frac{d}{dt}(\cos\theta\,\mathbf i - \sin\theta\,\mathbf j) \quad &\text{(the vectors $\mathbf i$, $\mathbf j$ are fixed in $S_0$)} \\
> &= -\sin\theta\,\dot\theta\,\mathbf i - \cos\theta\,\dot\theta\,\mathbf j \quad &\text{(chain rule: derivative with respect to $\theta$ times $\dot\theta$)} \\
> &= -\dot\theta\,\mathbf j_1 \quad &\text{(compare with $\mathbf j_1$ of the first rotation)} \\
> \boldsymbol\omega_{10}\times\mathbf i_1 &= -\dot\theta\,\mathbf k_1\times\mathbf i_1 = -\dot\theta\,\mathbf j_1 \quad &\text{($\mathbf k = \mathbf k_1$; right-handed $\mathcal B_1$: $\mathbf k_1\times\mathbf i_1 = \mathbf j_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = -\dot\theta\,\mathbf k, \qquad \boldsymbol\omega_{B1} = \dot\theta\,\mathbf i_1}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** the Poisson formula holds with this vector. In the same way the second rotation, by $\theta$ about $\mathbf i_1$, contributes $\dot\theta$ along its own axis.

> [!derivation] Angular velocity of the body in both bases
> **Law:** additivity of angular velocities; change of basis
> **Source:** Notes.pdf, Eq. 3.14; Notes.pdf, Eq. 1.14; [Lecture 7, Slide 12]
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0} &= \boldsymbol\omega_{B1} + \boldsymbol\omega_{10} \quad &\text{(Eq. 3.14 with the intermediate basis $\mathcal B_1$)} \\
> &= \dot\theta\,\mathbf i_1 - \dot\theta\,\mathbf k \quad &\text{(previous box)} \\
> &= \dot\theta\,(\cos\theta\,\mathbf i - \sin\theta\,\mathbf j) - \dot\theta\,\mathbf k \quad &\text{(substitute $\mathbf i_1$ in $\mathcal B_0$)} \\
> \mathbf k &= \mathbf k_1 = \sin\theta\,\mathbf j_B + \cos\theta\,\mathbf k_B \quad &\text{(third row of $[{}_1R_B]$: inverse of the second rotation, Eq. 1.14)} \\
> \boldsymbol\omega_{B0} &= \dot\theta\,\mathbf i_B - \dot\theta\,(\sin\theta\,\mathbf j_B + \cos\theta\,\mathbf k_B) \quad &\text{(substitute $\mathbf i_1 = \mathbf i_B$ and $\mathbf k$)} \\
> [\boldsymbol\omega_{B0}]_B &= [{}_0R_B]^T[\boldsymbol\omega_{B0}]_0 \quad &\text{(cross-check with the composed matrix)} \\
> \omega_{x_B} &= \cos\theta\,(\dot\theta\cos\theta) + (-\sin\theta)(-\dot\theta\sin\theta) + 0\cdot(-\dot\theta) = \dot\theta \quad &\text{(first column of $[{}_0R_B]$ times the fixed components)} \\
> \omega_{y_B} &= \sin\theta\cos\theta\,(\dot\theta\cos\theta) + \cos^2\theta\,(-\dot\theta\sin\theta) + \sin\theta\,(-\dot\theta) = -\dot\theta\sin\theta \quad &\text{(second column)} \\
> \omega_{z_B} &= -\sin^2\theta\,(\dot\theta\cos\theta) + (-\sin\theta\cos\theta)(-\dot\theta\sin\theta) + \cos\theta\,(-\dot\theta) = -\dot\theta\cos\theta \quad &\text{(third column)} \\
> \lvert\boldsymbol\omega_{B0}\rvert^2 &= \dot\theta^2(\cos^2\theta + \sin^2\theta + 1) = \dot\theta^2(1 + \sin^2\theta + \cos^2\theta) = 2\dot\theta^2 \quad &\text{(same modulus in both bases)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{B0} = \dot\theta\,(\cos\theta\,\mathbf i - \sin\theta\,\mathbf j - \mathbf k) = \dot\theta\,(\mathbf i_B - \sin\theta\,\mathbf j_B - \cos\theta\,\mathbf k_B)}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ in every term
> **Meaning:** the body turns at $\sqrt2\,\lvert\dot\theta\rvert$ about a direction that is the sum of the horizontal axis $Px_B$ and the downward vertical; the vertical part is the turn of $Px_B$ in the plane $Oxy$, the horizontal part is the lift of $Py_B$.

#### Velocity of P

> [!derivation] Velocity of P from its position vector
> **Law:** time derivative of the position vector in $S_0$; chain rule; quotient rule
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 1.14
>
> $$\begin{aligned}
> \mathbf v_0^P &= \left.\frac{d\mathbf r_0^P}{dt}\right|_0 = \frac{d}{dt}(a\tan\theta)\,\mathbf j \quad &\text{($\mathbf j$ is fixed in $S_0$ and $a$ is constant)} \\
> \frac{d}{dt}\tan\theta &= \frac{d\tan\theta}{d\theta}\,\dot\theta \quad &\text{(chain rule)} \\
> \frac{d\tan\theta}{d\theta} &= \frac{d}{d\theta}\frac{\sin\theta}{\cos\theta} = \frac{\cos\theta\cos\theta - \sin\theta\,(-\sin\theta)}{\cos^2\theta} \quad &\text{(quotient rule)} \\
> &= \frac{1}{\cos^2\theta} \quad &\text{($\cos^2\theta + \sin^2\theta = 1$)} \\
> \mathbf v_0^P &= \frac{a\dot\theta}{\cos^2\theta}\,\mathbf j \quad &\text{(substitute)} \\
> [\mathbf j]_B &= (-\sin\theta,\ \cos^2\theta,\ -\sin\theta\cos\theta) \quad &\text{(second row of $[{}_0R_B]$, Eq. 1.14)} \\
> \mathbf v_0^P &= \frac{a\dot\theta}{\cos^2\theta}\,(-\sin\theta\,\mathbf i_B + \cos^2\theta\,\mathbf j_B - \sin\theta\cos\theta\,\mathbf k_B) \quad &\text{(substitute $\mathbf j$ in $\mathcal B_B$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \frac{a\dot\theta}{\cos^2\theta}\,\mathbf j = a\dot\theta\left(-\frac{\sin\theta}{\cos^2\theta}\,\mathbf i_B + \mathbf j_B - \tan\theta\,\mathbf k_B\right)}$$
>
> **Units:** $[\mathrm L][\mathrm{T^{-1}}] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** $P$ slides along $Oy$, slowly near zero angle and ever faster as the axis $Px_B$ approaches the direction of $Oy$, where no point of $Oy$ can see $A$ along it.

### Center of Mass and Inertia Tensor

This section does not apply: the problem is purely kinematic, and no mass property enters the angular velocity or the velocity of a point.

### Linear Momentum, Angular Momentum and Kinetic Energy

This section does not apply: no momentum or energy is asked for.

### Free-Body Diagram and Equations of Motion

This section does not apply: the motion is described by the geometric conditions alone and no force is asked for.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| Angular velocity, fixed basis | $\boldsymbol\omega_{B0} = \dot\theta\,(\cos\theta\,\mathbf i - \sin\theta\,\mathbf j - \mathbf k)$ |
| Angular velocity, body basis | $\boldsymbol\omega_{B0} = \dot\theta\,(\mathbf i_B - \sin\theta\,\mathbf j_B - \cos\theta\,\mathbf k_B)$ |
| Velocity of $P$ | $\mathbf v_0^P = \dfrac{a\dot\theta}{\cos^2\theta}\,\mathbf j$ |

**Check against the official key:** the key (Problems.pdf, p. 77) prints the angular velocity as the rate times $\mathbf i_B$ minus sine times $\mathbf j_B$ minus cosine times $\mathbf k_B$, equal to the rate times $\mathbf i$ cosine minus $\mathbf j$ sine minus $\mathbf k$, and the velocity of $P$ as $a$ times the rate over the squared cosine along $\mathbf j$. The two bases and the velocity coincide term by term with the results above, which also confirms the senses read from the statement ($P$ on the positive half of $Oy$, $Py_B$ lifted towards positive $z$).

> [!derivation] Check: the body point at A slides along the axis Px_B
> **Law:** velocity field of a rigid body from $P$ to the body point $A(B)$ that coincides with the fixed point $A$
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 9.14; Notes.pdf, Eq. 9.15
>
> Condition 2 holds at every instant, so the body line $Px_B$ always passes through the fixed point $A$: the body point that is at $A$ may only move along that line. Its velocity must then be parallel to $\mathbf i_B$.
>
> $$\begin{aligned}
> \mathbf v_0^{A(B)} &= \mathbf v_0^P + \boldsymbol\omega_{B0}\times\mathbf{PA} \quad &\text{(Eq. 9.3 between two body points)} \\
> \boldsymbol\omega_{B0}\times\mathbf{PA} &= (\dot\theta\,\mathbf i_1 - \dot\theta\,\mathbf k_1)\times\frac{a}{\cos\theta}\,\mathbf i_1 \quad &\text{($\mathbf{PA}$ is the hypotenuse along $\mathbf i_1$)} \\
> &= -\frac{a\dot\theta}{\cos\theta}\,\mathbf k_1\times\mathbf i_1 = -\frac{a\dot\theta}{\cos\theta}\,\mathbf j_1 \quad &\text{($\mathbf i_1\times\mathbf i_1 = \mathbf 0$; $\mathbf k_1\times\mathbf i_1 = \mathbf j_1$)} \\
> &= -a\dot\theta\tan\theta\,\mathbf i - a\dot\theta\,\mathbf j \quad &\text{(substitute $\mathbf j_1 = \sin\theta\,\mathbf i + \cos\theta\,\mathbf j$)} \\
> \mathbf v_0^{A(B)} &= -a\dot\theta\tan\theta\,\mathbf i + a\dot\theta\left(\frac{1}{\cos^2\theta} - 1\right)\mathbf j \quad &\text{(add the velocity of $P$)} \\
> &= -a\dot\theta\tan\theta\,\mathbf i + a\dot\theta\tan^2\theta\,\mathbf j \quad &\text{($1/\cos^2\theta - 1 = \tan^2\theta$)} \\
> &= -\frac{a\dot\theta\tan\theta}{\cos\theta}\,(\cos\theta\,\mathbf i - \sin\theta\,\mathbf j) \quad &\text{(take out the common factor)} \\
> &= -\frac{a\dot\theta\sin\theta}{\cos^2\theta}\,\mathbf i_B \quad &\text{($\cos\theta\,\mathbf i - \sin\theta\,\mathbf j = \mathbf i_1 = \mathbf i_B$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^{A(B)} = -\frac{a\dot\theta\sin\theta}{\cos^2\theta}\,\mathbf i_B \parallel \mathbf i_B}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the body slides through the fixed point $A$ along its own axis $Px_B$ and never leaves it, so the angular velocity found is consistent with condition 2. The distance from $P$ to $A$ grows at the rate $a\dot\theta\sin\theta/\cos^2\theta$, the time derivative of the hypotenuse.

**Limiting cases and consistency:**

* **Zero angle.** $P$ is at $O$, the body basis coincides with the fixed basis, the speed of $P$ is $a$ times the rate, along $\mathbf j$ (the leg $OA$ swinging about $A$), and the angular velocity is the rate times the difference of $\mathbf i$ and $\mathbf k$.
* **Angle approaching a right angle.** The squared cosine in the denominator makes the speed of $P$ grow without bound: $P$ must run to infinity along $Oy$ to keep the line to $A$ nearly parallel to $Oy$.
* **Slip velocity.** The scalar product of the velocity of $P$ with the angular velocity is minus $a$ times the squared rate times the sine over the squared cosine, which is not zero for a non-zero angle: the instantaneous motion is a screw motion, not a pure rotation.
* **Dimensions.** The angular velocity has the dimensions of the rate, $[\mathrm{T^{-1}}]$; the velocity of $P$ is a length times a rate.

---

## Problem RB-03: Flywheel kinematics (Euler angles)

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a free gyroscope made of three rigid bodies in a chain: the outer gimbal, turning in the fixed bearings $A$ and $B$; the inner gimbal, turning in the bearings $C$ and $D$ of the outer gimbal; and the flywheel, turning in the bearings $E$ and $F$ of the inner gimbal. Only the motion of the flywheel is asked for.
* **Fixed frame:** $S_0\{O; \mathcal B_0\}$, the frame $XYZ$ of the figure, with right-handed basis $\{\mathbf i, \mathbf j, \mathbf k\}$ along $X$, $Y$, $Z$. Read from the figure: the three bearing axes meet at the centre of the flywheel, which is fixed and is taken as the origin $O$; the bearing axis $AB$ is the fixed axis $Y$.
* **Outer gimbal frame:** $S_1\{O; \mathcal B_1\}$, attached to the outer gimbal. It turns about $AB$, so its second unit vector is the fixed one, $\mathbf j_1$ equal to $\mathbf j$; its first unit vector $\mathbf i_1$ lies along the bearing axis $CD$, from $D$ to $C$. The angle from $X$ to $\mathbf i_1$ is $\beta$.
* **Inner gimbal frame:** $S_2\{O; \mathcal B_2\}$, attached to the inner gimbal. It turns about $CD$, so $\mathbf i_2$ equals $\mathbf i_1$; its second unit vector $\mathbf j_2$ lies along the flywheel axle $EF$. The angle between the two gimbals, marked at $C$ in the figure, is $\gamma$.
* **Body frame of the flywheel:** $S_b\{O; \mathcal B_B\}$, the frame $xyz$ of the statement, with basis $\{\mathbf i_B, \mathbf j_B, \mathbf k_B\}$. It turns about the axle $EF$, so $\mathbf j_B$ equals $\mathbf j_2$ (the axis $y$ of the figure); the spin angle is $\theta$, with constant rate $\omega_\theta$.
* **Senses and origin of the angles (reading):** the figure is a perspective sketch, so the positive senses of $\beta$, $\gamma$ and $\theta$ are taken by the right-hand rule about $\mathbf j$, $\mathbf i_1$ and $\mathbf j_2$; the key uses the same convention (see Answers and Checks). At the initial instant the given laws make $\beta$ and $\gamma$ zero, and the spin angle is counted from the position in which $x$ points from $D$ to $C$, so $\theta$ is zero too: the four bases coincide at the initial instant and $X$ also points from $D$ to $C$, as the statement requires.
* **Degrees of freedom:** each gimbal joint is a revolute joint about a fixed line of the previous body, so the flywheel has three rotational degrees of freedom about its fixed centre, the three angles of a 2-1-2 Euler sequence. All three are given functions of time, so no coordinate is left free: the problem is pure kinematics.

| Datum | Law | SI unit |
| :--- | :--- | :--- |
| Spin of the flywheel relative to the inner gimbal | $\theta = \omega_\theta t$, rate $\omega_\theta$ constant | rad, rad/s |
| Inner gimbal relative to the outer gimbal | $\gamma = A\sin(\omega_\gamma t)$ | rad ($A$ in rad, $\omega_\gamma$ in rad/s) |
| Outer gimbal relative to the fixed frame | $\beta = B\sin(\omega_\beta t)$ | rad ($B$ in rad, $\omega_\beta$ in rad/s) |

* **Unknowns:** the angular velocity and the angular acceleration of the flywheel, each in the body basis and in the fixed basis.
* **Plan:** one view per elementary rotation gives its matrix; the angular velocity is the sum of the three elementary angular velocities (Notes.pdf, Eq. 3.14); the angular acceleration is the derivative in $S_0$ of that sum, with the moving unit vectors differentiated by the Poisson formula (Notes.pdf, Eq. 3.3).

![[attachments/EM-SOL/rb03-gimbal-chain.svg]]

### Change of Basis, Position Vectors and Constraint Kinematics

No position vector is needed: the centre $O$ is fixed and only the attitude of the flywheel is asked for.

#### Three elementary rotations

![[attachments/EM-SOL/rb03-rotation-beta.svg]]

> [!derivation] Outer gimbal: rotation about j by the angle beta
> **Law:** simple rotation about the second axis, positive by the right-hand rule
> **Source:** Notes.pdf, Eq. 1.19; Notes.pdf, Eq. 1.15; [Lecture 7, Slide 12]
>
> View with $\mathbf j$ out of the paper (⊙), $\mathbf k$ to the right and $\mathbf i$ up, since $\mathbf k\times\mathbf i = \mathbf j$. Positive $\beta$ is counterclockwise in this view.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\beta\,\mathbf i - \sin\beta\,\mathbf k \quad &\text{(hypotenuse 1: adjacent leg along $\mathbf i$; $\mathbf i$ turned counterclockwise from up leans to the left, opposite leg along $-\mathbf k$)} \\
> \mathbf j_1 &= \mathbf j \quad &\text{(the rotation axis does not move)} \\
> \mathbf k_1 &= \sin\beta\,\mathbf i + \cos\beta\,\mathbf k \quad &\text{($\mathbf k$ turned counterclockwise from the right leans upwards: opposite leg along $+\mathbf i$)} \\
> [{}_0R_1] &= \begin{bmatrix} \cos\beta & 0 & \sin\beta \cr 0 & 1 & 0 \cr -\sin\beta & 0 & \cos\beta \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot(\cos\beta\cos\beta - \sin\beta\,(-\sin\beta)) = 1 \quad &\text{(expand along the second row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\beta + \sin^2\beta & 0 & -\cos\beta\sin\beta + \sin\beta\cos\beta \cr 0 & 1 & 0 \cr -\sin\beta\cos\beta + \cos\beta\sin\beta & 0 & \sin^2\beta + \cos^2\beta \end{bmatrix} = [U] \quad &\text{(row by row products)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = [{}_0R_1(y, \beta)] = \begin{bmatrix} \cos\beta & 0 & \sin\beta \cr 0 & 1 & 0 \cr -\sin\beta & 0 & \cos\beta \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** for a rotation about the second axis the minus sign sits below the diagonal, in the third row: the cyclic order is $\mathbf k$, $\mathbf i$, $\mathbf j$, so it is the first axis that leans towards the negative third one.

![[attachments/EM-SOL/rb03-rotation-gamma.svg]]

> [!derivation] Inner gimbal: rotation about i1 by the angle gamma
> **Law:** simple rotation about the first axis, positive by the right-hand rule
> **Source:** Notes.pdf, Eq. 1.18; Notes.pdf, Eq. 1.15; [Lecture 7, Slide 12]
>
> View with $\mathbf i_1$ out of the paper (⊙), $\mathbf j_1$ to the right and $\mathbf k_1$ up, since $\mathbf j_1\times\mathbf k_1 = \mathbf i_1$. Positive $\gamma$ is counterclockwise.
>
> $$\begin{aligned}
> \mathbf i_2 &= \mathbf i_1 \quad &\text{(the rotation axis $CD$ does not move)} \\
> \mathbf j_2 &= \cos\gamma\,\mathbf j_1 + \sin\gamma\,\mathbf k_1 \quad &\text{(hypotenuse 1: adjacent leg along $\mathbf j_1$, opposite leg along $\mathbf k_1$)} \\
> \mathbf k_2 &= -\sin\gamma\,\mathbf j_1 + \cos\gamma\,\mathbf k_1 \quad &\text{($\mathbf k_1$ turned counterclockwise leans towards $-\mathbf j_1$)} \\
> [{}_1R_2] &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos\gamma & -\sin\gamma \cr 0 & \sin\gamma & \cos\gamma \end{bmatrix} \quad &\text{(columns: $\mathbf i_2$, $\mathbf j_2$, $\mathbf k_2$ in $\mathcal B_1$)} \\
> \det[{}_1R_2] &= 1\cdot(\cos^2\gamma + \sin^2\gamma) = 1 \quad &\text{(expand along the first row)} \\
> [{}_1R_2][{}_1R_2]^T &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos^2\gamma + \sin^2\gamma & \cos\gamma\sin\gamma - \sin\gamma\cos\gamma \cr 0 & \sin\gamma\cos\gamma - \cos\gamma\sin\gamma & \sin^2\gamma + \cos^2\gamma \end{bmatrix} = [U] \quad &\text{(row by row products)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_2] = [{}_1R_2(x, \gamma)] = \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos\gamma & -\sin\gamma \cr 0 & \sin\gamma & \cos\gamma \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** the inner gimbal tilts the flywheel axle $\mathbf j_2$ away from the fixed axis $AB$ by the angle $\gamma$.

![[attachments/EM-SOL/rb03-rotation-theta.svg]]

> [!derivation] Flywheel: rotation about j2 by the angle theta
> **Law:** simple rotation about the second axis, positive by the right-hand rule
> **Source:** Notes.pdf, Eq. 1.19; Notes.pdf, Eq. 1.15; [Lecture 7, Slide 12]
>
> View with $\mathbf j_2$ out of the paper (⊙), $\mathbf k_2$ to the right and $\mathbf i_2$ up, since $\mathbf k_2\times\mathbf i_2 = \mathbf j_2$. Positive $\theta$ is counterclockwise.
>
> $$\begin{aligned}
> \mathbf i_B &= \cos\theta\,\mathbf i_2 - \sin\theta\,\mathbf k_2 \quad &\text{(hypotenuse 1: adjacent leg along $\mathbf i_2$; turned counterclockwise from up it leans towards $-\mathbf k_2$)} \\
> \mathbf j_B &= \mathbf j_2 \quad &\text{(the axle $EF$ does not move)} \\
> \mathbf k_B &= \sin\theta\,\mathbf i_2 + \cos\theta\,\mathbf k_2 \quad &\text{($\mathbf k_2$ turned counterclockwise from the right leans upwards, towards $+\mathbf i_2$)} \\
> [{}_2R_B] &= \begin{bmatrix} \cos\theta & 0 & \sin\theta \cr 0 & 1 & 0 \cr -\sin\theta & 0 & \cos\theta \end{bmatrix} \quad &\text{(columns: $\mathbf i_B$, $\mathbf j_B$, $\mathbf k_B$ in $\mathcal B_2$)} \\
> \det[{}_2R_B] &= 1\cdot(\cos^2\theta + \sin^2\theta) = 1 \quad &\text{(expand along the second row)} \\
> [{}_2R_B][{}_2R_B]^T &= [U] \quad &\text{(same products as for $[{}_0R_1]$ with $\theta$ in place of $\beta$)}
> \end{aligned}$$
>
> $$\boxed{[{}_2R_B] = [{}_2R_B(y, \theta)] = \begin{bmatrix} \cos\theta & 0 & \sin\theta \cr 0 & 1 & 0 \cr -\sin\theta & 0 & \cos\theta \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** the spin turns the flywheel about its own axle; the attitude is the 2-1-2 sequence $[{}_0R_B] = [{}_0R_1][{}_1R_2][{}_2R_B]$, whose determinant is the product of three ones.

> [!derivation] Unit vectors needed in the fixed basis and in the body basis
> **Law:** change of basis and its inverse (the transpose)
> **Source:** Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.16
>
> $$\begin{aligned}
> \mathbf j_2 &= \cos\gamma\,\mathbf j_1 + \sin\gamma\,\mathbf k_1 = \cos\gamma\,\mathbf j + \sin\gamma\,(\sin\beta\,\mathbf i + \cos\beta\,\mathbf k) \quad &\text{(second rotation, then $\mathbf j_1$ and $\mathbf k_1$ of the first)} \\
> &= \sin\gamma\sin\beta\,\mathbf i + \cos\gamma\,\mathbf j + \sin\gamma\cos\beta\,\mathbf k \quad &\text{(collect the components)} \\
> \mathbf i_2 &= \cos\theta\,\mathbf i_B + \sin\theta\,\mathbf k_B, \quad \mathbf k_2 = -\sin\theta\,\mathbf i_B + \cos\theta\,\mathbf k_B \quad &\text{(rows of $[{}_2R_B]$: the inverse change, Eq. 1.14)} \\
> \mathbf j_1 &= \cos\gamma\,\mathbf j_2 - \sin\gamma\,\mathbf k_2, \quad \mathbf k_1 = \sin\gamma\,\mathbf j_2 + \cos\gamma\,\mathbf k_2 \quad &\text{(rows of $[{}_1R_2]$)} \\
> \mathbf i_1 &= \mathbf i_2 = \cos\theta\,\mathbf i_B + \sin\theta\,\mathbf k_B \quad &\text{($\mathbf i_2 = \mathbf i_1$)} \\
> \mathbf j_1 &= \sin\gamma\sin\theta\,\mathbf i_B + \cos\gamma\,\mathbf j_B - \sin\gamma\cos\theta\,\mathbf k_B \quad &\text{(substitute $\mathbf j_2 = \mathbf j_B$ and $\mathbf k_2$)} \\
> \mathbf k_1 &= -\cos\gamma\sin\theta\,\mathbf i_B + \sin\gamma\,\mathbf j_B + \cos\gamma\cos\theta\,\mathbf k_B \quad &\text{(substitute $\mathbf j_2 = \mathbf j_B$ and $\mathbf k_2$)}
> \end{aligned}$$
>
> $$\boxed{\begin{aligned} \mathbf j_2 &= \sin\gamma\sin\beta\,\mathbf i + \cos\gamma\,\mathbf j + \sin\gamma\cos\beta\,\mathbf k \quad &\text{(axle in $\mathcal B_0$)} \\ [\mathbf i_1]_B &= (\cos\theta,\ 0,\ \sin\theta),\ [\mathbf j_1]_B = (\sin\gamma\sin\theta,\ \cos\gamma,\ -\sin\gamma\cos\theta),\ [\mathbf k_1]_B = (-\cos\gamma\sin\theta,\ \sin\gamma,\ \cos\gamma\cos\theta) \quad &\text{(basis 1 in $\mathcal B_B$)} \end{aligned}}$$
>
> **Units:** dimensionless
> **Meaning:** each of the three triads is orthonormal (sum of squares of every row equal to one), which is a quick check of the substitutions.

#### Angular velocity by additivity

> [!derivation] Angular velocities of the elementary rotations
> **Law:** a simple rotation has the angular velocity of the rate of its angle along its axis; Poisson formula
> **Source:** Notes.pdf, Eq. 3.3; [Lecture 7, Slide 12]
>
> Check for the outer gimbal with the derivative of one of its unit vectors.
>
> $$\begin{aligned}
> \left.\frac{d\mathbf k_1}{dt}\right|_0 &= \frac{d}{dt}(\sin\beta\,\mathbf i + \cos\beta\,\mathbf k) = \cos\beta\,\dot\beta\,\mathbf i - \sin\beta\,\dot\beta\,\mathbf k \quad &\text{(chain rule; $\mathbf i$, $\mathbf k$ fixed)} \\
> &= \dot\beta\,\mathbf i_1 \quad &\text{(compare with $\mathbf i_1$)} \\
> \dot\beta\,\mathbf j\times\mathbf k_1 &= \dot\beta\,\mathbf j_1\times\mathbf k_1 = \dot\beta\,\mathbf i_1 \quad &\text{($\mathbf j = \mathbf j_1$; right-handed $\mathcal B_1$)} \\
> \boldsymbol\omega_{10} &= \dot\beta\,\mathbf j \quad &\text{(the Poisson formula holds with this vector)} \\
> \boldsymbol\omega_{21} &= \dot\gamma\,\mathbf i_1, \quad \boldsymbol\omega_{B2} = \dot\theta\,\mathbf j_2 \quad &\text{(same argument for the other two rotations)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \dot\beta\,\mathbf j, \qquad \boldsymbol\omega_{21} = \dot\gamma\,\mathbf i_1, \qquad \boldsymbol\omega_{B2} = \dot\theta\,\mathbf j_2}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** each gimbal adds the rate of its own angle along its own bearing axis.

> [!derivation] Angular velocity of the flywheel in the fixed basis
> **Law:** additivity of angular velocities
> **Source:** Notes.pdf, Eq. 3.14; Notes.pdf, Eq. 9.21; [Lecture 7, Slide 12]
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0} &= \boldsymbol\omega_{B2} + \boldsymbol\omega_{20} = \boldsymbol\omega_{B2} + \boldsymbol\omega_{21} + \boldsymbol\omega_{10} \quad &\text{(Eq. 3.14 twice, with the intermediate frames $S_2$ and $S_1$)} \\
> &= \dot\theta\,\mathbf j_2 + \dot\gamma\,\mathbf i_1 + \dot\beta\,\mathbf j \quad &\text{(previous box)} \\
> &= \dot\theta\,(\sin\gamma\sin\beta\,\mathbf i + \cos\gamma\,\mathbf j + \sin\gamma\cos\beta\,\mathbf k) + \dot\gamma\,(\cos\beta\,\mathbf i - \sin\beta\,\mathbf k) + \dot\beta\,\mathbf j \quad &\text{(substitute $\mathbf j_2$ and $\mathbf i_1$ in $\mathcal B_0$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{B0} = (\dot\theta\sin\gamma\sin\beta + \dot\gamma\cos\beta)\,\mathbf i + (\dot\theta\cos\gamma + \dot\beta)\,\mathbf j + (\dot\theta\sin\gamma\cos\beta - \dot\gamma\sin\beta)\,\mathbf k}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ in every term
> **Meaning:** the spin, the largest rate in a gyroscope, is spread over the three fixed axes by the tilt of the axle; the gimbal rates add along their bearing axes.

> [!derivation] Angular velocity of the flywheel in the body basis
> **Law:** additivity of angular velocities; inverse change of basis
> **Source:** Notes.pdf, Eq. 3.14; Notes.pdf, Eq. 1.14
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0} &= \dot\theta\,\mathbf j_B + \dot\gamma\,\mathbf i_1 + \dot\beta\,\mathbf j_1 \quad &\text{($\mathbf j_2 = \mathbf j_B$ and $\mathbf j = \mathbf j_1$)} \\
> &= \dot\theta\,\mathbf j_B + \dot\gamma\,(\cos\theta\,\mathbf i_B + \sin\theta\,\mathbf k_B) + \dot\beta\,(\sin\gamma\sin\theta\,\mathbf i_B + \cos\gamma\,\mathbf j_B - \sin\gamma\cos\theta\,\mathbf k_B) \quad &\text{(substitute $\mathbf i_1$ and $\mathbf j_1$ in $\mathcal B_B$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{B0} = (\dot\gamma\cos\theta + \dot\beta\sin\theta\sin\gamma)\,\mathbf i_B + (\dot\theta + \dot\beta\cos\gamma)\,\mathbf j_B + (\dot\gamma\sin\theta - \dot\beta\sin\gamma\cos\theta)\,\mathbf k_B}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ in every term
> **Meaning:** these are the rates a three-axis gyrometer fixed on the flywheel would read. The squares of the two forms add up to the same value, the squared gimbal rates plus the squared spin plus twice the spin times the outer rate times the cosine of the inner angle.

#### Angular acceleration from the derivative in the fixed frame

> [!derivation] Derivatives of the moving unit vectors
> **Law:** Poisson formula: a unit vector fixed in a frame changes with the angular velocity of that frame
> **Source:** Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.14; Notes.pdf, Eq. 1.42
>
> The vector $\mathbf i_1$ is fixed in $S_1$; the vector $\mathbf j_2$ is fixed in $S_2$, whose angular velocity is the sum of the first two elementary ones.
>
> $$\begin{aligned}
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \boldsymbol\omega_{10}\times\mathbf i_1 = \dot\beta\,\mathbf j_1\times\mathbf i_1 \quad &\text{(Poisson formula in $S_1$)} \\
> &= -\dot\beta\,\mathbf k_1 \quad &\text{(right-handed $\mathcal B_1$: $\mathbf j_1\times\mathbf i_1 = -\mathbf k_1$)} \\
> \boldsymbol\omega_{20} &= \boldsymbol\omega_{21} + \boldsymbol\omega_{10} = \dot\gamma\,\mathbf i_1 + \dot\beta\,\mathbf j_1 \quad &\text{(Eq. 3.14)} \\
> \left.\frac{d\mathbf j_2}{dt}\right|_0 &= \boldsymbol\omega_{20}\times\mathbf j_2 = \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr \dot\gamma & \dot\beta & 0 \cr 0 & \cos\gamma & \sin\gamma \end{vmatrix} \quad &\text{(Poisson formula in $S_2$; components in $\mathcal B_1$)} \\
> &= \mathbf i_1\,(\dot\beta\sin\gamma - 0\cdot\cos\gamma) - \mathbf j_1\,(\dot\gamma\sin\gamma - 0\cdot 0) + \mathbf k_1\,(\dot\gamma\cos\gamma - \dot\beta\cdot 0) \quad &\text{(expand along the first row)} \\
> &= \dot\beta\sin\gamma\,\mathbf i_1 - \dot\gamma\sin\gamma\,\mathbf j_1 + \dot\gamma\cos\gamma\,\mathbf k_1 \quad &\text{(carry out the products)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf i_1}{dt}\right|_0 = -\dot\beta\,\mathbf k_1, \qquad \left.\frac{d\mathbf j_2}{dt}\right|_0 = \dot\beta\sin\gamma\,\mathbf i_1 - \dot\gamma\sin\gamma\,\mathbf j_1 + \dot\gamma\cos\gamma\,\mathbf k_1}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** the bearing axis $CD$ swings with the outer gimbal only; the axle $EF$ swings with both gimbals. Using the angular velocity of $S_2$ for the first vector would give the same result, because the extra term is along $\mathbf i_1$ itself.

> [!derivation] Angular acceleration in the basis of the outer gimbal
> **Law:** definition of angular acceleration as the derivative in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 3.9; Notes.pdf, Eq. 3.3
>
> $$\begin{aligned}
> \boldsymbol\alpha_{B0} &= \left.\frac{d\boldsymbol\omega_{B0}}{dt}\right|_0 = \frac{d}{dt}(\dot\beta\,\mathbf j + \dot\gamma\,\mathbf i_1 + \dot\theta\,\mathbf j_2) \quad &\text{(definition; additive form of the angular velocity)} \\
> &= \ddot\beta\,\mathbf j + \ddot\gamma\,\mathbf i_1 + \dot\gamma\left.\frac{d\mathbf i_1}{dt}\right|_0 + \ddot\theta\,\mathbf j_2 + \dot\theta\left.\frac{d\mathbf j_2}{dt}\right|_0 \quad &\text{(product rule; $\mathbf j$ is fixed in $S_0$)} \\
> \ddot\theta &= 0 \quad &\text{(the spin rate $\omega_\theta$ is constant)} \\
> \boldsymbol\alpha_{B0} &= \ddot\beta\,\mathbf j_1 + \ddot\gamma\,\mathbf i_1 - \dot\gamma\dot\beta\,\mathbf k_1 + \dot\theta\,(\dot\beta\sin\gamma\,\mathbf i_1 - \dot\gamma\sin\gamma\,\mathbf j_1 + \dot\gamma\cos\gamma\,\mathbf k_1) \quad &\text{(previous box; $\mathbf j = \mathbf j_1$)} \\
> &= (\ddot\gamma + \dot\theta\dot\beta\sin\gamma)\,\mathbf i_1 + (\ddot\beta - \dot\theta\dot\gamma\sin\gamma)\,\mathbf j_1 + (\dot\theta\dot\gamma\cos\gamma - \dot\gamma\dot\beta)\,\mathbf k_1 \quad &\text{(collect along $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\alpha_{B0} = (\ddot\gamma + \dot\theta\dot\beta\sin\gamma)\,\mathbf i_1 + (\ddot\beta - \dot\theta\dot\gamma\sin\gamma)\,\mathbf j_1 + (\dot\theta\dot\gamma\cos\gamma - \dot\gamma\dot\beta)\,\mathbf k_1}$$
>
> **Units:** $[\mathrm{T^{-2}}]$ in every term
> **Meaning:** besides the angular accelerations of the gimbals, the products of rates appear because the axes of the gimbal rates and of the spin turn; the basis $\mathcal B_1$ is the shortest place to collect them before passing to the two requested bases.

> [!derivation] Angular acceleration in the fixed basis
> **Law:** change of basis from $\mathcal B_1$ to $\mathcal B_0$
> **Source:** Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.19
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\beta\,\mathbf i - \sin\beta\,\mathbf k, \quad \mathbf j_1 = \mathbf j, \quad \mathbf k_1 = \sin\beta\,\mathbf i + \cos\beta\,\mathbf k \quad &\text{(columns of $[{}_0R_1]$)} \\
> \alpha_X &= (\ddot\gamma + \dot\theta\dot\beta\sin\gamma)\cos\beta + (\dot\theta\dot\gamma\cos\gamma - \dot\gamma\dot\beta)\sin\beta \quad &\text{(components along $\mathbf i$ of $\mathbf i_1$ and $\mathbf k_1$)} \\
> &= \dot\theta\,(\dot\gamma\cos\gamma\sin\beta + \dot\beta\cos\beta\sin\gamma) + \ddot\gamma\cos\beta - \dot\gamma\dot\beta\sin\beta \quad &\text{(group the terms in the spin rate)} \\
> \alpha_Y &= \ddot\beta - \dot\theta\dot\gamma\sin\gamma \quad &\text{(only $\mathbf j_1$ has a component along $\mathbf j$)} \\
> \alpha_Z &= -(\ddot\gamma + \dot\theta\dot\beta\sin\gamma)\sin\beta + (\dot\theta\dot\gamma\cos\gamma - \dot\gamma\dot\beta)\cos\beta \quad &\text{(components along $\mathbf k$ of $\mathbf i_1$ and $\mathbf k_1$)} \\
> &= \dot\theta\,(\dot\gamma\cos\gamma\cos\beta - \dot\beta\sin\beta\sin\gamma) - \ddot\gamma\sin\beta - \dot\gamma\dot\beta\cos\beta \quad &\text{(group the terms in the spin rate)}
> \end{aligned}$$
>
> $$\boxed{\begin{aligned} \boldsymbol\alpha_{B0} &= \left[\dot\theta\,(\dot\gamma\cos\gamma\sin\beta + \dot\beta\cos\beta\sin\gamma) + \ddot\gamma\cos\beta - \dot\gamma\dot\beta\sin\beta\right]\mathbf i + \left[\ddot\beta - \dot\theta\dot\gamma\sin\gamma\right]\mathbf j \quad &\text{(first two)} \\ &\quad + \left[\dot\theta\,(\dot\gamma\cos\gamma\cos\beta - \dot\beta\sin\beta\sin\gamma) - \ddot\gamma\sin\beta - \dot\gamma\dot\beta\cos\beta\right]\mathbf k \quad &\text{(third)} \end{aligned}}$$
>
> **Units:** $[\mathrm{T^{-2}}]$
> **Meaning:** the same result follows by differentiating the three fixed components of the angular velocity one by one, because the fixed unit vectors do not change; that route is used below as a check.

> [!derivation] Angular acceleration in the body basis
> **Law:** change of basis from $\mathcal B_1$ to $\mathcal B_B$
> **Source:** Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.16
>
> Write the components of the previous box in $\mathcal B_1$ as $\alpha_1$, $\alpha_2$, $\alpha_3$ and use the body components of $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$.
>
> $$\begin{aligned}
> \alpha_{x_B} &= \alpha_1\cos\theta + \alpha_2\sin\gamma\sin\theta - \alpha_3\cos\gamma\sin\theta \quad &\text{(first body components of $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$)} \\
> &= \ddot\gamma\cos\theta + \dot\theta\dot\beta\sin\gamma\cos\theta + \ddot\beta\sin\gamma\sin\theta - \dot\theta\dot\gamma\sin^2\gamma\sin\theta - \dot\theta\dot\gamma\cos^2\gamma\sin\theta + \dot\gamma\dot\beta\cos\gamma\sin\theta \quad &\text{(expand the three products)} \\
> &= \dot\beta\,(\dot\theta\cos\theta\sin\gamma + \dot\gamma\cos\gamma\sin\theta) + \ddot\gamma\cos\theta - \dot\gamma\dot\theta\sin\theta + \ddot\beta\sin\theta\sin\gamma \quad &\text{($\sin^2\gamma + \cos^2\gamma = 1$, then group)} \\
> \alpha_{y_B} &= \alpha_2\cos\gamma + \alpha_3\sin\gamma \quad &\text{(second body components; that of $\mathbf i_1$ is zero)} \\
> &= \ddot\beta\cos\gamma - \dot\theta\dot\gamma\sin\gamma\cos\gamma + \dot\theta\dot\gamma\cos\gamma\sin\gamma - \dot\gamma\dot\beta\sin\gamma \quad &\text{(expand)} \\
> &= \ddot\beta\cos\gamma - \dot\gamma\dot\beta\sin\gamma \quad &\text{(the terms in the spin rate cancel)} \\
> \alpha_{z_B} &= \alpha_1\sin\theta - \alpha_2\sin\gamma\cos\theta + \alpha_3\cos\gamma\cos\theta \quad &\text{(third body components)} \\
> &= \ddot\gamma\sin\theta + \dot\theta\dot\beta\sin\gamma\sin\theta - \ddot\beta\sin\gamma\cos\theta + \dot\theta\dot\gamma\sin^2\gamma\cos\theta + \dot\theta\dot\gamma\cos^2\gamma\cos\theta - \dot\gamma\dot\beta\cos\gamma\cos\theta \quad &\text{(expand)} \\
> &= \ddot\gamma\sin\theta + \dot\theta\dot\gamma\cos\theta - \ddot\beta\sin\gamma\cos\theta - \dot\beta\,(\dot\gamma\cos\gamma\cos\theta - \dot\theta\sin\theta\sin\gamma) \quad &\text{($\sin^2\gamma + \cos^2\gamma = 1$, then group)}
> \end{aligned}$$
>
> $$\boxed{\begin{aligned} \boldsymbol\alpha_{B0} &= \left[\dot\beta\,(\dot\theta\cos\theta\sin\gamma + \dot\gamma\cos\gamma\sin\theta) + \ddot\gamma\cos\theta - \dot\gamma\dot\theta\sin\theta + \ddot\beta\sin\theta\sin\gamma\right]\mathbf i_B \quad &\text{(first)} \\ &\quad + \left[\ddot\beta\cos\gamma - \dot\gamma\dot\beta\sin\gamma\right]\mathbf j_B \quad &\text{(second)} \\ &\quad + \left[\ddot\gamma\sin\theta + \dot\theta\dot\gamma\cos\theta - \ddot\beta\sin\gamma\cos\theta - \dot\beta\,(\dot\gamma\cos\gamma\cos\theta - \dot\theta\sin\theta\sin\gamma)\right]\mathbf k_B \quad &\text{(third)} \end{aligned}}$$
>
> **Units:** $[\mathrm{T^{-2}}]$
> **Meaning:** the component along the axle has no term in the spin rate: with a constant spin, the axle component of the angular acceleration comes only from the outer gimbal rate projected on the axle and its change.

> [!derivation] Rates and accelerations of the three angles
> **Law:** time derivatives of the given laws; chain rule
> **Source:** Problems.pdf, p. 37
>
> $$\begin{aligned}
> \dot\theta &= \omega_\theta, \quad \ddot\theta = 0 \quad &\text{(constant spin rate; $\theta = \omega_\theta t$ with zero initial angle)} \\
> \dot\gamma &= \frac{d}{dt}\,A\sin(\omega_\gamma t) = A\cos(\omega_\gamma t)\,\omega_\gamma \quad &\text{(chain rule: outer derivative times $d(\omega_\gamma t)/dt = \omega_\gamma$)} \\
> \ddot\gamma &= \frac{d}{dt}\,A\omega_\gamma\cos(\omega_\gamma t) = -A\omega_\gamma^2\sin(\omega_\gamma t) \quad &\text{(chain rule again)} \\
> \dot\beta &= B\omega_\beta\cos(\omega_\beta t) \quad &\text{(chain rule)} \\
> \ddot\beta &= -B\omega_\beta^2\sin(\omega_\beta t) \quad &\text{(chain rule again)}
> \end{aligned}$$
>
> $$\boxed{\dot\theta = \omega_\theta,\quad \dot\gamma = A\omega_\gamma\cos(\omega_\gamma t),\quad \ddot\gamma = -A\omega_\gamma^2\sin(\omega_\gamma t),\quad \dot\beta = B\omega_\beta\cos(\omega_\beta t),\quad \ddot\beta = -B\omega_\beta^2\sin(\omega_\beta t)}$$
>
> **Units:** rates in $[\mathrm{T^{-1}}]$ and accelerations in $[\mathrm{T^{-2}}]$, since the amplitudes are angles in rad
> **Meaning:** substituting these laws and the angles themselves in the boxed components gives the angular velocity and acceleration as explicit functions of time.

### Center of Mass and Inertia Tensor

This section does not apply: only the angular velocity and acceleration of the flywheel are asked for, and they do not depend on its mass distribution.

### Linear Momentum, Angular Momentum and Kinetic Energy

This section does not apply: no momentum or energy is asked for.

### Free-Body Diagram and Equations of Motion

This section does not apply: the three angles are prescribed functions of time and no torque is asked for.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| Angular velocity, body basis | $(\dot\gamma\cos\theta + \dot\beta\sin\theta\sin\gamma)\,\mathbf i_B + (\dot\theta + \dot\beta\cos\gamma)\,\mathbf j_B + (\dot\gamma\sin\theta - \dot\beta\sin\gamma\cos\theta)\,\mathbf k_B$ |
| Angular velocity, fixed basis | $(\dot\theta\sin\gamma\sin\beta + \dot\gamma\cos\beta)\,\mathbf i + (\dot\theta\cos\gamma + \dot\beta)\,\mathbf j + (\dot\theta\sin\gamma\cos\beta - \dot\gamma\sin\beta)\,\mathbf k$ |
| Angular acceleration, body basis | $[\dot\beta(\dot\theta\cos\theta\sin\gamma + \dot\gamma\cos\gamma\sin\theta) + \ddot\gamma\cos\theta - \dot\gamma\dot\theta\sin\theta + \ddot\beta\sin\theta\sin\gamma]\,\mathbf i_B + [\ddot\beta\cos\gamma - \dot\gamma\dot\beta\sin\gamma]\,\mathbf j_B + [\ddot\gamma\sin\theta + \dot\theta\dot\gamma\cos\theta - \ddot\beta\sin\gamma\cos\theta - \dot\beta(\dot\gamma\cos\gamma\cos\theta - \dot\theta\sin\theta\sin\gamma)]\,\mathbf k_B$ |
| Angular acceleration, fixed basis | $[\dot\theta(\dot\gamma\cos\gamma\sin\beta + \dot\beta\cos\beta\sin\gamma) + \ddot\gamma\cos\beta - \dot\gamma\dot\beta\sin\beta]\,\mathbf i + [\ddot\beta - \dot\theta\dot\gamma\sin\gamma]\,\mathbf j + [\dot\theta(\dot\gamma\cos\gamma\cos\beta - \dot\beta\sin\beta\sin\gamma) - \ddot\gamma\sin\beta - \dot\gamma\dot\beta\cos\beta]\,\mathbf k$ |
| Time laws to substitute | $\theta = \omega_\theta t$, $\dot\theta = \omega_\theta$; $\gamma = A\sin\omega_\gamma t$, $\dot\gamma = A\omega_\gamma\cos\omega_\gamma t$, $\ddot\gamma = -A\omega_\gamma^2\sin\omega_\gamma t$; $\beta = B\sin\omega_\beta t$, $\dot\beta = B\omega_\beta\cos\omega_\beta t$, $\ddot\beta = -B\omega_\beta^2\sin\omega_\beta t$ |

**Check against the official key:** the key (Problems.pdf, p. 77) prints "some partial results": the angular velocity and the angular acceleration in the fixed basis and in the body basis, written with the rates and accelerations of the three angles and no second derivative of the spin. Compared term by term, the twelve printed components (three per basis for each of the two vectors) coincide with the four boxed results above. The convention is the same: the outer gimbal turns about $Y$ by $\beta$, the inner gimbal about the axis $CD$ by $\gamma$, the flywheel about its axle (the axis $y$) by $\theta$, all positive by the right-hand rule. No discrepancy is found.

> [!derivation] Check: body components of the angular acceleration by direct differentiation
> **Law:** the angular acceleration of a frame is the same derivative in $S_0$ and in that frame, so the body components of the angular velocity may be differentiated directly
> **Source:** Notes.pdf, Eq. 3.8; Notes.pdf, Eq. 3.9; Notes.pdf, Sec. 9.2
>
> $$\begin{aligned}
> \left.\frac{d\boldsymbol\omega_{B0}}{dt}\right|_0 &= \left.\frac{d\boldsymbol\omega_{B0}}{dt}\right|_B + \boldsymbol\omega_{B0}\times\boldsymbol\omega_{B0} = \left.\frac{d\boldsymbol\omega_{B0}}{dt}\right|_B \quad &\text{(Coriolis theorem, Eq. 3.8; the vector product of a vector with itself vanishes)} \\
> \frac{d}{dt}(\dot\gamma\cos\theta + \dot\beta\sin\theta\sin\gamma) &= \ddot\gamma\cos\theta - \dot\gamma\dot\theta\sin\theta + \ddot\beta\sin\theta\sin\gamma + \dot\beta\dot\theta\cos\theta\sin\gamma + \dot\beta\dot\gamma\sin\theta\cos\gamma \quad &\text{(product rule; chain rule on each sine and cosine)} \\
> \frac{d}{dt}(\dot\theta + \dot\beta\cos\gamma) &= 0 + \ddot\beta\cos\gamma - \dot\beta\dot\gamma\sin\gamma \quad &\text{(constant spin rate; product and chain rules)} \\
> \frac{d}{dt}(\dot\gamma\sin\theta - \dot\beta\sin\gamma\cos\theta) &= \ddot\gamma\sin\theta + \dot\gamma\dot\theta\cos\theta - \ddot\beta\sin\gamma\cos\theta - \dot\beta\dot\gamma\cos\gamma\cos\theta + \dot\beta\dot\theta\sin\gamma\sin\theta \quad &\text{(product and chain rules)}
> \end{aligned}$$
>
> $$\boxed{\dot\omega_{x_B} = \alpha_{x_B}, \qquad \dot\omega_{y_B} = \alpha_{y_B}, \qquad \dot\omega_{z_B} = \alpha_{z_B}}$$
>
> **Units:** $[\mathrm{T^{-2}}]$ in every term
> **Meaning:** the three derivatives are, term by term, the body components obtained through the basis of the outer gimbal; the two routes agree.

**Limiting cases and consistency:**

* **Gimbals locked.** With both gimbal angles held at zero, the angular velocity reduces to the spin rate along the axle, which is then the fixed axis $Y$, and the angular acceleration vanishes: a wheel spinning at a constant rate about a fixed axle.
* **Spin stopped.** With a zero spin rate the flywheel moves with the inner gimbal, and the angular acceleration in the outer gimbal basis keeps only the gimbal accelerations and the product of the two gimbal rates along the third axis, the term that appears because the inner bearing axis turns with the outer gimbal.
* **Gyroscopic terms.** Every product of the spin rate with a gimbal rate comes from the turning of the axle, the derivative of its unit vector; these are the terms that make a fast flywheel resist the motion of its gimbals.
* **Dimensions.** Every term of the angular velocity is a rate and every term of the angular acceleration is a product of two rates or a second derivative of an angle.

---

## Problem RB-11: Rolling disk (3D pure rolling kinematics)

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a disc $B$ of radius $R$ rolling without slipping on the fixed plane $Oxy$. Points used: the centre $G$ of the disc, the geometric contact point $C$ on the plane, and the point $O_1$, the centre $(0, 0, R)$ of the circle described by $G$.
* **Fixed frame:** $S_0\{O; \mathcal B_0\}$ with $\mathcal B_0\{\mathbf i, \mathbf j, \mathbf k\}$, as in the statement.
* **Intermediate frame:** $S_1\{O; \mathcal B_1\}$, the basis of the official key: $\mathbf k_1$ along $\mathbf k$; $\mathbf i_1$ horizontal, along the perpendicular axis of the disc, from $Oz$ towards the disc; $\mathbf j_1$ completing a right-handed basis, $\mathbf k_1$ times $\mathbf i_1$. It turns about $Oz$ by the angle $\varphi$ measured from $\mathbf i$ to $\mathbf i_1$.
* **Body frame:** $S_B\{G; \mathcal B_B\}$ attached to the disc, with $\mathbf i_B$ equal to $\mathbf i_1$ (the axis of the disc) and $\mathbf j_B$, $\mathbf k_B$ in the plane of the disc, turned by the spin angle $\psi$ about $\mathbf i_1$.
* **How the conditions are read:**
  1. *The disc remains perpendicular to the plane $Oxy$:* its plane is vertical, so its perpendicular axis is horizontal.
  2. *The perpendicular axis always intersects $Oz$:* the axis passes through $G$, at height $R$, and is horizontal, so it meets $Oz$ at the point at height $R$, which is $O_1$. The axis is the line $O_1G$, along $\mathbf i_1$, and $O_1G$ is the radius $R$ of the circle described by $G$.
  3. *Contact with $Oxy$:* the plane of the disc is vertical and contains $\mathbf k$, so the point of the rim nearest to the plane $Oxy$ is directly below $G$, at the distance $R$; it is at height zero, which is the contact point $C$.
* **Degrees of freedom:** a free rigid body has six (Notes.pdf, Sec. 9.3). The position of $G$ (three coordinates) is prescribed by the statement; conditions 1 and 2 fix the direction of the axis of the disc (two attitude angles). One coordinate is left, the spin angle $\psi$, and the no-slip condition fixes its rate.
* **Assumption for the fixed-basis components only:** at the initial instant $G$ is above the positive half of $Ox$, so $\varphi$ starts from zero.

| Datum | Value | SI unit |
| :--- | :--- | :--- |
| Radius of the disc | $R$ | m |
| Circle of the centre | radius $R$, centre $O_1(0, 0, R)$, in the plane $z = R$ | m |
| Speed of the centre | $\omega R$, constant, counterclockwise seen from $Oz$ | m/s |
| Coordinates | $\varphi(t)$ (prescribed), $\psi(t)$ (fixed by rolling) | rad |

* **Unknowns:** (a) the angular velocity and acceleration of the disc in $S_0$; (b) the acceleration of the point of the disc in contact with $Oxy$; (c) the instantaneous axis of rotation.

![[attachments/EM-SOL/rb11-overview.svg]]

### Change of Basis, Position Vectors and Constraint Kinematics

#### Elementary rotations

![[attachments/EM-SOL/rb11-rotation-phi.svg]]

> [!derivation] First rotation: about k by the angle phi
> **Law:** simple rotation about the third axis, positive by the right-hand rule
> **Source:** Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 1.15; [Lecture 7, Slide 12]
>
> View with $\mathbf k$ out of the paper (⊙), $\mathbf i$ to the right and $\mathbf j$ up. Counterclockwise in this view is the sense of motion of $G$ seen from $Oz$, and the positive sense of $\varphi$.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\varphi\,\mathbf i + \sin\varphi\,\mathbf j \quad &\text{(hypotenuse 1: adjacent leg along $\mathbf i$, opposite leg along $\mathbf j$)} \\
> \mathbf j_1 &= -\sin\varphi\,\mathbf i + \cos\varphi\,\mathbf j \quad &\text{($\mathbf j$ turned counterclockwise leans towards $-\mathbf i$: opposite leg along $-\mathbf i$)} \\
> \mathbf k_1 &= \mathbf k \quad &\text{(the rotation axis does not move)} \\
> \mathbf k_1\times\mathbf i_1 &= \cos\varphi\,(\mathbf k\times\mathbf i) + \sin\varphi\,(\mathbf k\times\mathbf j) = \cos\varphi\,\mathbf j - \sin\varphi\,\mathbf i = \mathbf j_1 \quad &\text{(the key's definition of $\mathbf j_1$ is met)} \\
> [{}_0R_1] &= \begin{bmatrix} \cos\varphi & -\sin\varphi & 0 \cr \sin\varphi & \cos\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot(\cos^2\varphi + \sin^2\varphi) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\varphi + \sin^2\varphi & \cos\varphi\sin\varphi - \sin\varphi\cos\varphi & 0 \cr \sin\varphi\cos\varphi - \cos\varphi\sin\varphi & \sin^2\varphi + \cos^2\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = [{}_0R_1(z, \varphi)] = \begin{bmatrix} \cos\varphi & -\sin\varphi & 0 \cr \sin\varphi & \cos\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix}, \qquad \boldsymbol\omega_{10} = \dot\varphi\,\mathbf k}$$
>
> **Units:** dimensionless; the angular velocity in $[\mathrm{T^{-1}}]$
> **Meaning:** $\mathbf i_1$ points from $Oz$ towards the disc, $\mathbf j_1$ is the horizontal tangent to the circle of $G$ in the sense of motion; the frame $S_1$ turns with the rate of $\varphi$ about the fixed vertical.

![[attachments/EM-SOL/rb11-rotation-psi.svg]]

> [!derivation] Second rotation: spin about i1 by the angle psi
> **Law:** simple rotation about the first axis, positive by the right-hand rule
> **Source:** Notes.pdf, Eq. 1.18; Notes.pdf, Eq. 1.15; [Lecture 7, Slide 12]
>
> View with $\mathbf i_1$ out of the paper (⊙): the observer is outside the circle of $G$, looking at the face of the disc towards $Oz$; $\mathbf j_1$ points to the right and $\mathbf k_1$ up, since $\mathbf j_1\times\mathbf k_1 = \mathbf i_1$. Positive $\psi$ is counterclockwise.
>
> $$\begin{aligned}
> \mathbf i_B &= \mathbf i_1 \quad &\text{(the axis of the disc does not move in this rotation)} \\
> \mathbf j_B &= \cos\psi\,\mathbf j_1 + \sin\psi\,\mathbf k_1 \quad &\text{(hypotenuse 1: adjacent leg along $\mathbf j_1$, opposite leg along $\mathbf k_1$)} \\
> \mathbf k_B &= -\sin\psi\,\mathbf j_1 + \cos\psi\,\mathbf k_1 \quad &\text{($\mathbf k_1$ turned counterclockwise leans towards $-\mathbf j_1$)} \\
> [{}_1R_B] &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos\psi & -\sin\psi \cr 0 & \sin\psi & \cos\psi \end{bmatrix} \quad &\text{(columns: $\mathbf i_B$, $\mathbf j_B$, $\mathbf k_B$ in $\mathcal B_1$)} \\
> \det[{}_1R_B] &= 1\cdot(\cos^2\psi + \sin^2\psi) = 1 \quad &\text{(expand along the first row)} \\
> [{}_1R_B][{}_1R_B]^T &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos^2\psi + \sin^2\psi & \cos\psi\sin\psi - \sin\psi\cos\psi \cr 0 & \sin\psi\cos\psi - \cos\psi\sin\psi & \sin^2\psi + \cos^2\psi \end{bmatrix} = [U] \quad &\text{(row by row products)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_B] = [{}_1R_B(x, \psi)] = \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos\psi & -\sin\psi \cr 0 & \sin\psi & \cos\psi \end{bmatrix}, \qquad \boldsymbol\omega_{B1} = \dot\psi\,\mathbf i_1}$$
>
> **Units:** dimensionless; the angular velocity in $[\mathrm{T^{-1}}]$
> **Meaning:** the spin is the only rotation of the disc relative to $S_1$; its rate is still unknown and will be fixed by the no-slip condition.

> [!derivation] Angular velocity of the disc with the spin rate unknown
> **Law:** additivity of angular velocities
> **Source:** Notes.pdf, Eq. 3.14; [Lecture 7, Slide 12]
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0} &= \boldsymbol\omega_{B1} + \boldsymbol\omega_{10} \quad &\text{(Eq. 3.14 with the intermediate frame $S_1$)} \\
> &= \dot\psi\,\mathbf i_1 + \dot\varphi\,\mathbf k_1 \quad &\text{(the two previous boxes; $\mathbf k = \mathbf k_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{B0} = \dot\psi\,\mathbf i_1 + \dot\varphi\,\mathbf k_1}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ in both terms
> **Meaning:** the disc turns about its own axis and, with the frame $S_1$, about the vertical.

#### Position and velocity of the centre

![[attachments/EM-SOL/rb11-meridian.svg]]

> [!derivation] Position and velocity of G; the rate of phi
> **Law:** position vector built point to point; time derivative in $S_0$ with the Poisson formula
> **Source:** Notes.pdf, Eq. 3.3; Problems.pdf, p. 44
>
> In the vertical plane of $\mathbf i_1$ and $\mathbf k_1$ (the meridian plane through $G$), $O_1$ is at the height $R$ on $Oz$, $G$ is at the horizontal distance $R$ from $O_1$, and $C$ is at the vertical distance $R$ below $G$.
>
> $$\begin{aligned}
> \mathbf r_0^G &= \overrightarrow{OO_1} + \overrightarrow{O_1G} = R\,\mathbf k_1 + R\,\mathbf i_1 \quad &\text{(up $Oz$ to $O_1$, then along the axis of the disc to $G$)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \frac{d}{dt}(\cos\varphi\,\mathbf i + \sin\varphi\,\mathbf j) = \dot\varphi\,(-\sin\varphi\,\mathbf i + \cos\varphi\,\mathbf j) = \dot\varphi\,\mathbf j_1 \quad &\text{(chain rule; $\mathbf i$, $\mathbf j$ fixed)} \\
> \mathbf v_0^G &= R\left.\frac{d\mathbf i_1}{dt}\right|_0 + R\left.\frac{d\mathbf k_1}{dt}\right|_0 = R\dot\varphi\,\mathbf j_1 + \mathbf 0 \quad &\text{(derivative of the position; $R$ constant and $\mathbf k_1$ fixed)} \\
> \lvert\mathbf v_0^G\rvert &= R\dot\varphi = \omega R \quad &\text{(the speed of $G$ is given; counterclockwise from $Oz$ means a positive rate)} \\
> \dot\varphi &= \omega, \qquad \varphi = \omega t \quad &\text{(constant rate; initial angle zero by the assumption above)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G = R\,(\mathbf i_1 + \mathbf k_1), \qquad \mathbf v_0^G = \omega R\,\mathbf j_1, \qquad \dot\varphi = \omega, \qquad \overrightarrow{GC} = -R\,\mathbf k_1}$$
>
> **Units:** positions in $[\mathrm L]$, velocity in $[\mathrm{T^{-1}}][\mathrm L] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the frame $S_1$ turns about $Oz$ at the constant rate $\omega$; in it, $G$, $C$ and $O_1$ are fixed points of the meridian plane.

#### No-slip condition at the contact point

> [!derivation] Spin rate from the no-slip condition
> **Law:** rolling without slipping: the body point of the disc at the contact has the velocity of the body point of the plane at the contact, which is zero because the plane is fixed; velocity field of the disc from $G$ to the body point $C(B)$
> **Source:** Notes.pdf, Eq. 13.2; Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 9.14; Notes.pdf, Eq. 9.15
>
> The geometric point $C$ moves along the circle of radius $R$ on the plane, but the body point $C(B)$ of the disc that is at $C$ at this instant must have zero velocity. Its velocity follows from the velocity field (Eq. 9.3), not from the derivative of the position of $C$.
>
> $$\begin{aligned}
> \mathbf v_0^{C(B)} &= \mathbf v_0^G + \boldsymbol\omega_{B0}\times\overrightarrow{GC} \quad &\text{(Eq. 9.3 between two body points)} \\
> \boldsymbol\omega_{B0}\times\overrightarrow{GC} &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr \dot\psi & 0 & \omega \cr 0 & 0 & -R \end{vmatrix} \quad &\text{(determinant form in $\mathcal B_1$, with the rate of $\varphi$ equal to $\omega$)} \\
> &= \mathbf i_1\,(0\cdot(-R) - \omega\cdot 0) - \mathbf j_1\,(\dot\psi\,(-R) - \omega\cdot 0) + \mathbf k_1\,(\dot\psi\cdot 0 - 0\cdot 0) \quad &\text{(expand along the first row)} \\
> &= R\dot\psi\,\mathbf j_1 \quad &\text{(carry out the products)} \\
> \mathbf v_0^{C(B)} &= (\omega R + R\dot\psi)\,\mathbf j_1 \quad &\text{(add the velocity of $G$)} \\
> \mathbf 0 &= (\omega R + R\dot\psi)\,\mathbf j_1 \quad &\text{(no slip on the fixed plane, Eq. 13.2)} \\
> \dot\psi &= -\omega, \qquad \psi = \psi_0 - \omega t \quad &\text{(solve; integrate with the initial spin angle)}
> \end{aligned}$$
>
> $$\boxed{\dot\psi = -\omega, \qquad \mathbf v_0^{C(B)} = \mathbf 0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ in the velocity condition; the spin rate in $[\mathrm{T^{-1}}]$
> **Meaning:** seen from outside the circle (axis of the disc out of the paper), the disc moves to the right and turns clockwise, the negative sense, like a wheel rolling forward. Only the component along $\mathbf j_1$ gave a condition: the other two components of the contact velocity vanish for any spin rate.

#### Part (a): angular velocity and angular acceleration

> [!derivation] Angular velocity of the disc
> **Law:** additivity of angular velocities with the rates found
> **Source:** Notes.pdf, Eq. 3.14; Notes.pdf, Eq. 1.20
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0} &= \dot\psi\,\mathbf i_1 + \dot\varphi\,\mathbf k_1 = -\omega\,\mathbf i_1 + \omega\,\mathbf k_1 \quad &\text{(substitute both rates)} \\
> &= -\omega\,(\cos\omega t\,\mathbf i + \sin\omega t\,\mathbf j) + \omega\,\mathbf k \quad &\text{(substitute $\mathbf i_1$ in $\mathcal B_0$ with the angle $\omega t$)} \\
> \lvert\boldsymbol\omega_{B0}\rvert &= \sqrt{\omega^2 + \omega^2} = \sqrt2\,\omega \quad &\text{(two perpendicular legs of length $\omega$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{B0} = \omega\,(-\mathbf i_1 + \mathbf k_1) = -\omega\cos\omega t\,\mathbf i - \omega\sin\omega t\,\mathbf j + \omega\,\mathbf k}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** the angular velocity has constant modulus and makes 45 degrees with the horizontal, pointing inwards and upwards; it turns about $Oz$ with the frame $S_1$.

> [!derivation] Angular acceleration of the disc
> **Law:** derivative in $S_0$ with the Poisson formula; checked with the composition of angular accelerations
> **Source:** Notes.pdf, Eq. 3.9; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.15
>
> $$\begin{aligned}
> \boldsymbol\alpha_{B0} &= \left.\frac{d\boldsymbol\omega_{B0}}{dt}\right|_0 = -\omega\left.\frac{d\mathbf i_1}{dt}\right|_0 + \omega\left.\frac{d\mathbf k_1}{dt}\right|_0 \quad &\text{(product rule with the constant $\omega$)} \\
> &= -\omega\,(\omega\,\mathbf j_1) + \omega\,\mathbf 0 \quad &\text{(derivative of $\mathbf i_1$ found above; $\mathbf k_1$ is fixed)} \\
> &= -\omega^2\,\mathbf j_1 \quad &\text{(multiply)} \\
> \boldsymbol\alpha_{B0} &= \boldsymbol\alpha_{B1} + \boldsymbol\omega_{10}\times\boldsymbol\omega_{B1} + \boldsymbol\alpha_{10} \quad &\text{(check with Eq. 3.15)} \\
> &= \mathbf 0 + \omega\,\mathbf k_1\times(-\omega\,\mathbf i_1) + \mathbf 0 \quad &\text{(constant spin rate about the axis $\mathbf i_1$ fixed in $S_1$; constant $\omega$ about the fixed $\mathbf k$)} \\
> &= -\omega^2\,\mathbf j_1 \quad &\text{($\mathbf k_1\times\mathbf i_1 = \mathbf j_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\alpha_{B0} = -\omega^2\,\mathbf j_1 = \omega^2\sin\omega t\,\mathbf i - \omega^2\cos\omega t\,\mathbf j}$$
>
> **Units:** $[\mathrm{T^{-2}}]$
> **Meaning:** both rates are constant, yet the angular acceleration is not zero: the spin axis is carried round the vertical, so the angular velocity vector turns; its tip moves horizontally, backwards with respect to the motion of $G$.

#### Part (b): acceleration of the contact point of the disc

> [!derivation] Acceleration of G
> **Law:** derivative in $S_0$ of the velocity of $G$, with the Poisson formula
> **Source:** Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 1.20
>
> $$\begin{aligned}
> \left.\frac{d\mathbf j_1}{dt}\right|_0 &= \boldsymbol\omega_{10}\times\mathbf j_1 = \omega\,\mathbf k_1\times\mathbf j_1 = -\omega\,\mathbf i_1 \quad &\text{(Poisson formula in $S_1$; $\mathbf k_1\times\mathbf j_1 = -\mathbf i_1$)} \\
> \mathbf a_0^G &= \left.\frac{d}{dt}(\omega R\,\mathbf j_1)\right|_0 = \omega R\left.\frac{d\mathbf j_1}{dt}\right|_0 \quad &\text{(constant speed $\omega R$)} \\
> &= -\omega^2 R\,\mathbf i_1 \quad &\text{(substitute)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^G = -\omega^2 R\,\mathbf i_1}$$
>
> **Units:** $[\mathrm{T^{-2}}][\mathrm L] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** $G$ moves uniformly on its circle, so its acceleration points towards $O_1$, the centre of that circle.

> [!derivation] Acceleration of the body point C(B)
> **Law:** acceleration field of a rigid body from $G$ to $C(B)$, each vector product by its determinant
> **Source:** Notes.pdf, Eq. 9.4; Notes.pdf, Eq. 9.15; Notes.pdf, Eq. 1.42
>
> $$\begin{aligned}
> \mathbf a_0^{C(B)} &= \mathbf a_0^G + \boldsymbol\alpha_{B0}\times\overrightarrow{GC} + \boldsymbol\omega_{B0}\times(\boldsymbol\omega_{B0}\times\overrightarrow{GC}) \quad &\text{(Eq. 9.4 between two body points)} \\
> \boldsymbol\alpha_{B0}\times\overrightarrow{GC} &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr 0 & -\omega^2 & 0 \cr 0 & 0 & -R \end{vmatrix} = \mathbf i_1\,((-\omega^2)(-R) - 0\cdot 0) - \mathbf j_1\,(0\cdot(-R) - 0\cdot 0) + \mathbf k_1\,(0\cdot 0 - (-\omega^2)\cdot 0) \quad &\text{(expand along the first row)} \\
> &= \omega^2 R\,\mathbf i_1 \quad &\text{(carry out the products)} \\
> \boldsymbol\omega_{B0}\times\overrightarrow{GC} &= R\dot\psi\,\mathbf j_1 = -\omega R\,\mathbf j_1 \quad &\text{(determinant of the no-slip box with the spin rate found)} \\
> \boldsymbol\omega_{B0}\times(\boldsymbol\omega_{B0}\times\overrightarrow{GC}) &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr -\omega & 0 & \omega \cr 0 & -\omega R & 0 \end{vmatrix} \quad &\text{(determinant form)} \\
> &= \mathbf i_1\,(0\cdot 0 - \omega\,(-\omega R)) - \mathbf j_1\,((-\omega)\cdot 0 - \omega\cdot 0) + \mathbf k_1\,((-\omega)(-\omega R) - 0\cdot 0) \quad &\text{(expand along the first row)} \\
> &= \omega^2 R\,\mathbf i_1 + \omega^2 R\,\mathbf k_1 \quad &\text{(carry out the products)} \\
> \mathbf a_0^{C(B)} &= -\omega^2 R\,\mathbf i_1 + \omega^2 R\,\mathbf i_1 + \omega^2 R\,(\mathbf i_1 + \mathbf k_1) \quad &\text{(add the three terms)} \\
> &= \omega^2 R\,(\mathbf i_1 + \mathbf k_1) \quad &\text{(the first two cancel)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^{C(B)} = \omega^2 R\,(\mathbf i_1 + \mathbf k_1), \qquad \lvert\mathbf a_0^{C(B)}\rvert = \sqrt2\,\omega^2 R}$$
>
> **Units:** $[\mathrm{T^{-2}}][\mathrm L] = [\mathrm{L\,T^{-2}}]$ in every term
> **Meaning:** the body point at the contact is at rest but not unaccelerated: it leaves the plane upwards, with the acceleration $\omega^2 R$ that any rolling wheel point has at the contact, and it is also pushed outwards, away from $Oz$, by the turning of the plane of the disc.

#### Part (c): instantaneous axis of rotation

> [!derivation] Instantaneous axis through the contact point
> **Law:** the axis is the set of points with the minimum velocity, parallel to the angular velocity; the slip velocity is common to all body points
> **Source:** Notes.pdf, Eq. 9.5; Notes.pdf, Eq. 9.8; Notes.pdf, Eq. 9.11; [Lecture 7, Slide 9]
>
> $$\begin{aligned}
> v_{0\parallel} &= \mathbf v_0^{C(B)}\cdot\frac{\boldsymbol\omega_{B0}}{\lvert\boldsymbol\omega_{B0}\rvert} = 0 \quad &\text{(Eq. 9.5 evaluated at the body point with zero velocity)} \\
> \mathbf r_0^I &= \mathbf r_0^C + \lambda\,\boldsymbol\omega_{B0} \quad &\text{(Eq. 9.8: the axis is the line through a point of zero velocity, parallel to the angular velocity)} \\
> \mathbf r_0^C &= \mathbf r_0^G + \overrightarrow{GC} = R\,\mathbf i_1 \quad &\text{(the contact point is below $G$, at the foot of the meridian triangle)} \\
> \mathbf r_0^I &= R\,\mathbf i_1 + \lambda\omega\,(-\mathbf i_1 + \mathbf k_1) \quad &\text{(substitute)} \\
> \mathbf r_0^I &= R\,\mathbf k_1 = \overrightarrow{OO_1} \quad &\text{(for the value $\lambda\omega = R$ the line reaches $O_1$ on $Oz$)} \\
> \mathbf v_0^{O_1(B)} &= \mathbf v_0^G + \boldsymbol\omega_{B0}\times\overrightarrow{GO_1} = \omega R\,\mathbf j_1 + \omega\,(-\mathbf i_1 + \mathbf k_1)\times(-R\,\mathbf i_1) \quad &\text{(check with Eq. 9.3; $\overrightarrow{GO_1} = -R\,\mathbf i_1$)} \\
> &= \omega R\,\mathbf j_1 - \omega R\,(\mathbf k_1\times\mathbf i_1) = \omega R\,\mathbf j_1 - \omega R\,\mathbf j_1 = \mathbf 0 \quad &\text{($\mathbf i_1\times\mathbf i_1 = \mathbf 0$, $\mathbf k_1\times\mathbf i_1 = \mathbf j_1$)}
> \end{aligned}$$
>
> $$\boxed{\text{axis: } \mathbf r = R\,\mathbf i_1 + \mu\,(-\mathbf i_1 + \mathbf k_1), \text{ the line through } C \text{ and } O_1(0, 0, R)}$$
>
> **Units:** $\mu$ is a length, $[\mathrm L]$, so every term of the line is a length
> **Meaning:** the motion is a pure rotation (zero slip velocity) about the line joining the contact point to $O_1$; in the meridian triangle $O_1GC$, with legs $R$ and $R$ and hypotenuse $R\sqrt2$, the axis is the hypotenuse, inclined 45 degrees to the plane. Since $O_1$ has zero velocity at every instant, the disc in fact moves about the fixed point $O_1$, and the axis sweeps a cone of vertex $O_1$ as the disc goes round.

### Center of Mass and Inertia Tensor

This section does not apply: the problem is purely kinematic, and the mass distribution of the disc does not enter.

### Linear Momentum, Angular Momentum and Kinetic Energy

This section does not apply: no momentum or energy is asked for.

### Free-Body Diagram and Equations of Motion

This section does not apply: the motion of the centre is prescribed and no force is asked for.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Angular velocity | $\boldsymbol\omega_{B0} = \omega(-\mathbf i_1 + \mathbf k_1) = -\omega\cos\omega t\,\mathbf i - \omega\sin\omega t\,\mathbf j + \omega\,\mathbf k$ |
| (a) Angular acceleration | $\boldsymbol\alpha_{B0} = -\omega^2\,\mathbf j_1 = \omega^2\sin\omega t\,\mathbf i - \omega^2\cos\omega t\,\mathbf j$ |
| (b) Acceleration of the contact point of the disc | $\mathbf a_0^{C(B)} = \omega^2 R(\mathbf i_1 + \mathbf k_1)$ |
| (c) Instantaneous axis | Axis of pure rotation through the contact point and $O_1(0, 0, R)$, direction $-\mathbf i_1 + \mathbf k_1$ |

**Check against the official key:** the key (Problems.pdf, p. 79) defines the same basis (third vector along $\mathbf k$, first vector along the axis of the disc from $Oz$ towards the disc, second the vector product of the third and the first) and prints the angular velocity $\omega$ times the difference of $\mathbf k_1$ and $\mathbf i_1$, the angular acceleration minus the squared rate along $\mathbf j_1$, and the acceleration of the contact point of the disc $\omega^2 R$ times the sum of $\mathbf i_1$ and $\mathbf k_1$. All three coincide with the results above. The key prints nothing for part (c).

**Limiting cases and consistency:**

* **Rolling on a straight line.** If the circle of the centre were very large, the turning of the plane of the disc would be negligible: the angular velocity would reduce to the spin and the contact point acceleration to the upward $\omega^2 R$ of a wheel rolling on a straight line. The outward part along $\mathbf i_1$ is the effect of the finite radius of the path.
* **Speeds against distances to the axis.** $G$ is at the distance $R/\sqrt2$ from the axis (half the diagonal of the square of side $R$ built on the meridian triangle), and its speed $\omega R$ equals the modulus $\sqrt2\,\omega$ of the angular velocity times that distance.
* **Contact velocity versus the geometric point.** The geometric contact point moves on the plane with speed $\omega R$ along $\mathbf j_1$, while the body point that occupies it is at rest: the two velocities differ, as Eq. 9.15 warns.
* **Dimensions.** Angular velocity in rad/s, angular acceleration in rad/s², accelerations in m/s².

---

## Problem RB-04: Moments of inertia (planar shapes: T, I, C)

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** three homogeneous plates of negligible thickness shaped as the letters T, I and C, with uniform surface density $\sigma$ (mass per unit area, kg/m²).
* **Dimensions (read from the figure):** every horizontal bar has length $w$, every letter has overall height $h$, and every bar, horizontal or vertical, has thickness $t$. The figure dimensions $h$ only on the T and $t$ only on the I (stem and lower bar) and on the C (upper bar); the three letters are drawn with equal heights and equal bar thicknesses, so the same $h$ and $t$ are used for all of them. The official key makes the same reading for the T.
* **Basis:** for every shape the plate lies in the plane of the paper; $\mathbf i$ is horizontal to the right, $\mathbf j$ vertical upwards and $\mathbf k$ normal to the plate, out of the paper, so that $\{\mathbf i, \mathbf j, \mathbf k\}$ is right-handed. All the frames of one shape share this basis.
* **Frames of the T:** the auxiliary frame $S_O$ has its origin $O$ at the midpoint of the lower edge of the top bar (the frame of the official key); $S_G$ is parallel to it with origin at the centre of mass $G$.
* **Frame of the I:** the letter has two symmetry lines, so the frame $S_G$ is placed directly at their intersection.
* **Frames of the C:** the auxiliary frame $S_{O'}$ has its origin $O'$ at the midpoint of the outer vertical edge (the back of the C, on the left; read from the figure: the C opens to the right); $S_G$ is parallel to it at the centre of mass.
* **Degrees of freedom:** each plate is a rigid body with six degrees of freedom, but no motion is involved: only its mass geometry is asked.
* **Mass element:** dm equals $\sigma$ times dA, with dA the product dx dy in Cartesian coordinates (jacobian 1); every point of a plate has zero third coordinate.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Length of the horizontal bars | $w$ | m |
| Overall height | $h$ | m |
| Thickness of every bar | $t$ | m |
| Surface density (uniform) | $\sigma$ | kg/m² |

* **Unknowns:** for each shape (a) the area and the centre of mass $G$; (b) the moment of inertia $I_{Gx}$ about the axis $Gx$; (c) the moment of inertia $I_{Gy}$ about the axis $Gy$; and the product of inertia $P_{xz,yz}$ with respect to the planes $Gxz$ and $Gyz$.

### Change of Basis, Position Vectors and Constraint Kinematics

No rotation of the basis is needed: every frame of a shape has the basis $\{\mathbf i, \mathbf j, \mathbf k\}$. The only operation between frames is a translation of the origin from an auxiliary point to $G$, handled with Steiner's theorem, written once here in components for a translation in the plane of the plate.

> [!derivation] Steiner's theorem for a translation in the plane of the plate
> **Law:** Steiner's theorem; components of the tensor of inertia
> **Source:** Notes.pdf, Eq. 10.48; Notes.pdf, Eq. 10.36; Notes.pdf, Eq. 10.37; Notes.pdf, Eq. 10.38
>
> Let the centre of mass have the position vector $\mathbf r_O^G$ with components $x_G$, $y_G$ and zero along $\mathbf k$ in the frame with origin $O$.
>
> $$\begin{aligned}
> \bar{\bar I}_O &= \bar{\bar I}_G + m\left[(\mathbf r_O^G)^2\,U - \mathbf r_O^G\otimes\mathbf r_O^G\right] \quad &\text{(Steiner's theorem, Eq. 10.48; both tensors in the same basis)} \\
> (\mathbf r_O^G)^2\,U &= \begin{bmatrix} x_G^2+y_G^2 & 0 & 0 \cr 0 & x_G^2+y_G^2 & 0 \cr 0 & 0 & x_G^2+y_G^2 \end{bmatrix} \quad &\text{(squared modulus times the unit tensor, Eq. 10.36, third component zero)} \\
> \mathbf r_O^G\otimes\mathbf r_O^G &= \begin{bmatrix} x_G^2 & x_G y_G & 0 \cr x_G y_G & y_G^2 & 0 \cr 0 & 0 & 0 \end{bmatrix} \quad &\text{(dyad, Eq. 10.37, third component zero)} \\
> (\mathbf r_O^G)^2\,U - \mathbf r_O^G\otimes\mathbf r_O^G &= \begin{bmatrix} y_G^2 & -x_G y_G & 0 \cr -x_G y_G & x_G^2 & 0 \cr 0 & 0 & x_G^2+y_G^2 \end{bmatrix} \quad &\text{(subtract element by element)} \\
> I_{Ox} &= I_{Gx} + m\,y_G^2 \quad &\text{(element 11; Eq. 10.38 puts $I_x$ there)} \\
> I_{Oy} &= I_{Gy} + m\,x_G^2 \quad &\text{(element 22)} \\
> -P^O_{xz,yz} &= -P^G_{xz,yz} - m\,x_G\,y_G \quad &\text{(element 12; Eq. 10.38 puts minus the product there)} \\
> P^O_{xz,yz} &= P^G_{xz,yz} + m\,x_G\,y_G \quad &\text{(change the sign of both sides)}
> \end{aligned}$$
>
> $$\boxed{I_{Gx} = I_{Ox} - m\,y_G^2, \qquad I_{Gy} = I_{Oy} - m\,x_G^2, \qquad P^G_{xz,yz} = P^O_{xz,yz} - m\,x_G\,y_G}$$
>
> **Units:** every term in $[\mathrm M][\mathrm L^2]$, kg·m²
> **Meaning:** the moment about an axis through $O$ exceeds the moment about the parallel axis through $G$ by the mass times the squared distance between the two axes: $y_G$ for the axes parallel to $\mathbf i$, $x_G$ for the axes parallel to $\mathbf j$. The moment about a central axis is therefore the smallest of its family.

### Center of Mass and Inertia Tensor

#### Shape T

The T is the union of two rectangles in $S_O$: the top bar, with abscissa between minus and plus half of $w$ and ordinate between 0 and $t$; and the stem, with abscissa between minus and plus half of $t$ and ordinate between minus $(h-t)$ and 0.

![[attachments/EM-SOL/rb04-t-shape.svg]]

> [!derivation] Area and centre of mass of the T
> **Law:** total mass and centre of mass as zeroth and first moments of the mass distribution; the centre of mass lies on a plane of symmetry
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.7; Notes.pdf, Eq. 10.8; Notes.pdf, Sec. 10.3; Problems.pdf, p. 38
>
> $$\begin{aligned}
> A_T &= \int_{-w/2}^{w/2}\!\int_0^{t} dy\,dx + \int_{-t/2}^{t/2}\!\int_{-(h-t)}^{0} dy\,dx \quad &\text{(area of the two rectangles, $dA = dx\,dy$)} \\
> &= \big[x\big]_{-w/2}^{w/2}\big[y\big]_0^{t} + \big[x\big]_{-t/2}^{t/2}\big[y\big]_{-(h-t)}^{0} \quad &\text{(constant limits: the double integrals split; antiderivative of 1)} \\
> &= \Big(\tfrac w2 + \tfrac w2\Big)(t - 0) + \Big(\tfrac t2 + \tfrac t2\Big)\big(0 + (h-t)\big) \quad &\text{(Barrow's rule, both limits)} \\
> &= t\,(w + h - t) \quad &\text{(multiply and take the common factor $t$)} \\
> m &= \sigma\,t\,(w + h - t) \quad &\text{(Eq. 10.6 with $dm = \sigma\,dA$ and constant $\sigma$)} \\
> x_G &= 0 \quad &\text{(the plane $Oyz$ is a plane of symmetry of the T: $G$ lies on it, Sec. 10.3)} \\
> m\,y_G &= \sigma\int_{-w/2}^{w/2}\!\int_0^{t} y\,dy\,dx + \sigma\int_{-t/2}^{t/2}\!\int_{-(h-t)}^{0} y\,dy\,dx \quad &\text{(first moment, second component of Eq. 10.7)} \\
> &= \sigma\,w\Big[\tfrac{y^2}{2}\Big]_0^{t} + \sigma\,t\Big[\tfrac{y^2}{2}\Big]_{-(h-t)}^{0} \quad &\text{(the $x$ integrals give $w$ and $t$ as above; antiderivative of $y$)} \\
> &= \sigma\,w\Big(\tfrac{t^2}{2} - 0\Big) + \sigma\,t\Big(0 - \tfrac{(h-t)^2}{2}\Big) \quad &\text{(Barrow's rule, both limits)} \\
> &= \tfrac{\sigma\,t}{2}\big[w\,t - (h-t)^2\big] \quad &\text{(common factor)} \\
> y_G &= \frac{w\,t - (h-t)^2}{2\,(w + h - t)} \quad &\text{(divide by the mass; $\sigma\,t$ cancels)}
> \end{aligned}$$
>
> $$\boxed{A_T = t\,(w+h-t), \qquad m = \sigma\,t\,(w+h-t), \qquad \mathbf r_O^G = \frac{w\,t - (h-t)^2}{2\,(w+h-t)}\,\mathbf j}$$
>
> **Units:** area $[\mathrm L^2]$; $y_G$ is $[\mathrm L^2]/[\mathrm L] = [\mathrm L]$
> **Meaning:** $G$ is on the vertical symmetry line. It lies above the lower edge of the top bar when the first moment of the bar, proportional to $w\,t$, beats that of the stem, proportional to the square of $h-t$, and below it otherwise.

> [!derivation] Moment of inertia of the T about the axis Gx
> **Law:** moment of inertia about a coordinate axis; Steiner's theorem for the parallel axis
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.48; Notes.pdf, Sec. 10.8
>
> $$\begin{aligned}
> I_{Ox} &= \int (y^2 + z^2)\,dm \quad &\text{(Eq. 10.11, axis $Ox$)} \\
> &= \sigma\int_{-w/2}^{w/2}\!\int_0^{t} y^2\,dy\,dx + \sigma\int_{-t/2}^{t/2}\!\int_{-(h-t)}^{0} y^2\,dy\,dx \quad &\text{(the plate has zero third coordinate; two rectangles)} \\
> &= \sigma\,w\Big[\tfrac{y^3}{3}\Big]_0^{t} + \sigma\,t\Big[\tfrac{y^3}{3}\Big]_{-(h-t)}^{0} \quad &\text{(the $x$ integrals give $w$ and $t$; antiderivative of $y^2$)} \\
> &= \sigma\,w\Big(\tfrac{t^3}{3} - 0\Big) + \sigma\,t\Big(0 - \tfrac{-(h-t)^3}{3}\Big) \quad &\text{(Barrow's rule; the cube of a negative number is negative)} \\
> &= \tfrac{\sigma}{3}\big[w\,t^3 + t\,(h-t)^3\big] \quad &\text{(common factor)} \\
> I_{Gx} &= I_{Ox} - m\,y_G^2 \quad &\text{(Steiner: the axes $Ox$ and $Gx$ are parallel, at the distance $y_G$)} \\
> &= \tfrac{\sigma}{3}\big[w\,t^3 + t\,(h-t)^3\big] - \sigma\,t\,(w+h-t)\,\frac{\big[w\,t - (h-t)^2\big]^2}{4\,(w+h-t)^2} \quad &\text{(substitute the mass and the ordinate of $G$)} \\
> &= \sigma\,t\,\frac{4\,(w+h-t)\big[w\,t^2 + (h-t)^3\big] - 3\big[w\,t - (h-t)^2\big]^2}{12\,(w+h-t)} \quad &\text{(common denominator)} \\
> &= \sigma\,t\,\frac{(h-t)^4 + 4w(h-t)^3 + 6wt(h-t)^2 + 4wt^2(h-t) + w^2t^2}{12\,(w+h-t)} \quad &\text{(expand: the terms in $w^2t^2$ and $(h-t)^4$ partly cancel)}
> \end{aligned}$$
>
> $$\boxed{I_{Gx}^{T} = \frac{\sigma}{3}\big[w\,t^3 + t\,(h-t)^3\big] - m\,y_G^2 = \frac{\sigma\,t\,\big[(h-t)^4 + 4w(h-t)^3 + 6wt(h-t)^2 + 4wt^2(h-t) + w^2t^2\big]}{12\,(w+h-t)}}$$
>
> **Units:** $[\mathrm M\,\mathrm L^{-2}][\mathrm L^4] = [\mathrm M\,\mathrm L^2]$ in every term
> **Meaning:** the bar and the stem first contribute their second moments about the line $Ox$; moving the axis to $G$ removes the mass times the squared distance, which makes the result the smallest moment about a horizontal axis.

> [!derivation] Moment of inertia of the T about the axis Gy
> **Law:** moment of inertia about a coordinate axis
> **Source:** Notes.pdf, Eq. 10.11
>
> The abscissa of $G$ is zero, so the axis $Gy$ is the same line as $Oy$ and no translation is needed.
>
> $$\begin{aligned}
> I_{Gy} &= \int (x^2 + z^2)\,dm \quad &\text{(Eq. 10.11, axis $Gy$)} \\
> &= \sigma\int_0^{t}\!\int_{-w/2}^{w/2} x^2\,dx\,dy + \sigma\int_{-(h-t)}^{0}\!\int_{-t/2}^{t/2} x^2\,dx\,dy \quad &\text{(zero third coordinate; two rectangles)} \\
> &= \sigma\,t\Big[\tfrac{x^3}{3}\Big]_{-w/2}^{w/2} + \sigma\,(h-t)\Big[\tfrac{x^3}{3}\Big]_{-t/2}^{t/2} \quad &\text{(the $y$ integrals give $t$ and $h-t$; antiderivative of $x^2$)} \\
> &= \sigma\,t\Big(\tfrac{w^3}{24} + \tfrac{w^3}{24}\Big) + \sigma\,(h-t)\Big(\tfrac{t^3}{24} + \tfrac{t^3}{24}\Big) \quad &\text{(Barrow's rule, both limits)} \\
> &= \tfrac{\sigma\,t}{12}\big[w^3 + (h-t)\,t^2\big] \quad &\text{(add and take the common factor)}
> \end{aligned}$$
>
> $$\boxed{I_{Gy}^{T} = \frac{\sigma\,t}{12}\big[w^3 + (h-t)\,t^2\big]}$$
>
> **Units:** $[\mathrm M\,\mathrm L^{-2}][\mathrm L^4] = [\mathrm M\,\mathrm L^2]$
> **Meaning:** the wide top bar dominates: its contribution grows with the cube of $w$, while the narrow stem adds only the cube of $t$ times its length.

> [!derivation] Products of inertia of the T
> **Law:** definition of the products of inertia; a product of inertia vanishes when one of its planes is a plane of symmetry
> **Source:** Notes.pdf, Eq. 10.15; Notes.pdf, Sec. 10.4; Notes.pdf, Eq. 10.38
>
> In $S_G$ the ordinate of a point is its ordinate in $S_O$ minus $y_G$.
>
> $$\begin{aligned}
> P^G_{xy,xz} &= \int z\,(y - y_G)\,dm \quad &\text{(Eq. 10.15)} \\
> &= 0 \quad &\text{(every point of the plate has zero third coordinate)} \\
> P^G_{xy,yz} &= \int z\,x\,dm = 0 \quad &\text{(same reason)} \\
> P^G_{xz,yz} &= \sigma\int_0^{t}\!(y-y_G)\,dy\int_{-w/2}^{w/2} x\,dx + \sigma\int_{-(h-t)}^{0}\!(y-y_G)\,dy\int_{-t/2}^{t/2} x\,dx \quad &\text{(Eq. 10.15; the double integrals split)} \\
> \int_{-w/2}^{w/2} x\,dx &= \Big[\tfrac{x^2}{2}\Big]_{-w/2}^{w/2} = \tfrac{w^2}{8} - \tfrac{w^2}{8} = 0 \quad &\text{(antiderivative and Barrow's rule; likewise for the stem)} \\
> P^G_{xz,yz} &= 0 \quad &\text{(both terms carry a vanishing factor)} \\
> I_{Gz} &= \int \big[x^2 + (y-y_G)^2\big]\,dm = I_{Gy} + I_{Gx} \quad &\text{(Eq. 10.11 about $Gz$ with zero third coordinate)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G^{T} = \begin{bmatrix} I_{Gx}^{T} & 0 & 0 \cr 0 & I_{Gy}^{T} & 0 \cr 0 & 0 & I_{Gx}^{T} + I_{Gy}^{T} \end{bmatrix}, \qquad P^G_{xz,yz} = 0}$$
>
> **Units:** every element in $[\mathrm M\,\mathrm L^2]$
> **Meaning:** the plane $Gyz$ is a plane of symmetry of the T (each point with abscissa $x$ has a twin with abscissa $-x$ and the same ordinate), so the products that involve it vanish, as Sec. 10.4 states; the products that involve the plane $Gxy$ vanish because the plate lies in it. The axes $Gx$, $Gy$, $Gz$ are principal axes.

#### Shape I

The I is the union of three rectangles in $S_G$: the top bar (abscissa between minus and plus half of $w$, ordinate between half of $h$ minus $t$ and half of $h$), the bottom bar (its mirror image in the plane $Gxz$) and the stem (abscissa between minus and plus half of $t$, ordinate between minus and plus the quantity half of $h$ minus $t$).

![[attachments/EM-SOL/rb04-i-shape.svg]]

> [!derivation] Area and centre of mass of the I
> **Law:** total mass; the centre of mass lies on every plane of symmetry
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Sec. 10.3; Problems.pdf, p. 38
>
> $$\begin{aligned}
> A_I &= 2\int_{-w/2}^{w/2}\!\int_{h/2-t}^{h/2} dy\,dx + \int_{-t/2}^{t/2}\!\int_{-(h/2-t)}^{h/2-t} dy\,dx \quad &\text{(two equal bars and the stem, $dA = dx\,dy$)} \\
> &= 2\,\big[x\big]_{-w/2}^{w/2}\big[y\big]_{h/2-t}^{h/2} + \big[x\big]_{-t/2}^{t/2}\big[y\big]_{-(h/2-t)}^{h/2-t} \quad &\text{(antiderivative of 1)} \\
> &= 2\,w\,t + t\,(h - 2t) \quad &\text{(Barrow's rule, both limits)} \\
> m &= \sigma\,t\,(2w + h - 2t) \quad &\text{(Eq. 10.6 with constant $\sigma$)} \\
> x_G &= 0 \quad &\text{(the plane $Gyz$ is a plane of symmetry, Sec. 10.3)} \\
> y_G &= 0 \quad &\text{(the plane $Gxz$ is a plane of symmetry, Sec. 10.3)}
> \end{aligned}$$
>
> $$\boxed{A_I = 2\,w\,t + t\,(h-2t), \qquad m = \sigma\,t\,(2w + h - 2t), \qquad G \text{ at the centre of the letter}}$$
>
> **Units:** $[\mathrm L^2]$ for the area, $[\mathrm M]$ for the mass
> **Meaning:** the two symmetry lines of the letter meet at its geometric centre, which is therefore $G$; no integral of first moments is needed.

> [!derivation] Moments of inertia of the I about Gx and Gy
> **Law:** moment of inertia about a coordinate axis
> **Source:** Notes.pdf, Eq. 10.11
>
> $$\begin{aligned}
> I_{Gx} &= \sigma\int y^2\,dA \quad &\text{(Eq. 10.11 with zero third coordinate)} \\
> &= \sigma\,w\Big[\tfrac{y^3}{3}\Big]_{h/2-t}^{h/2} + \sigma\,w\Big[\tfrac{y^3}{3}\Big]_{-h/2}^{-(h/2-t)} + \sigma\,t\Big[\tfrac{y^3}{3}\Big]_{-(h/2-t)}^{h/2-t} \quad &\text{(top bar, bottom bar, stem; the $x$ integrals give $w$, $w$, $t$)} \\
> &= \tfrac{\sigma w}{3}\Big[\tfrac{h^3}{8} - \big(\tfrac h2 - t\big)^3\Big] + \tfrac{\sigma w}{3}\Big[-\big(\tfrac h2 - t\big)^3 + \tfrac{h^3}{8}\Big] + \tfrac{\sigma t}{3}\,2\big(\tfrac h2 - t\big)^3 \quad &\text{(Barrow's rule, both limits each time)} \\
> &= \tfrac{\sigma}{3}\Big[\tfrac{w\,h^3}{4} - 2\,(w - t)\big(\tfrac h2 - t\big)^3\Big] \quad &\text{(collect the terms)} \\
> &= \tfrac{\sigma}{12}\big[w\,h^3 - (w - t)(h - 2t)^3\big] \quad &\text{(the cube of half of $h-2t$ is the cube of $h-2t$ over 8)} \\
> I_{Gy} &= \sigma\int x^2\,dA \quad &\text{(Eq. 10.11 with zero third coordinate)} \\
> &= 2\,\sigma\,t\Big[\tfrac{x^3}{3}\Big]_{-w/2}^{w/2} + \sigma\,(h-2t)\Big[\tfrac{x^3}{3}\Big]_{-t/2}^{t/2} \quad &\text{(the $y$ integrals give $t$, $t$ and $h-2t$)} \\
> &= 2\,\sigma\,t\,\tfrac{w^3}{12} + \sigma\,(h-2t)\,\tfrac{t^3}{12} \quad &\text{(Barrow's rule: each bracket is twice the cube of the half width over 3)} \\
> &= \tfrac{\sigma}{12}\big[2\,t\,w^3 + (h-2t)\,t^3\big] \quad &\text{(common factor)}
> \end{aligned}$$
>
> $$\boxed{I_{Gx}^{I} = \frac{\sigma}{12}\big[w\,h^3 - (w-t)(h-2t)^3\big], \qquad I_{Gy}^{I} = \frac{\sigma}{12}\big[2\,t\,w^3 + (h-2t)\,t^3\big]}$$
>
> **Units:** $[\mathrm M\,\mathrm L^{-2}][\mathrm L^4] = [\mathrm M\,\mathrm L^2]$
> **Meaning:** about $Gx$ the I behaves as the full rectangle $w$ by $h$ minus the two empty rectangles beside the stem, of total width $w-t$ and height $h-2t$; the bars, far from the axis, carry most of the moment, which is why I-beams resist bending so well.

> [!derivation] Products of inertia of the I
> **Law:** a product of inertia vanishes when one of its planes is a plane of symmetry
> **Source:** Notes.pdf, Eq. 10.15; Notes.pdf, Sec. 10.4
>
> $$\begin{aligned}
> P^G_{xy,xz} &= \int z\,y\,dm = 0 \quad &\text{(zero third coordinate)} \\
> P^G_{xy,yz} &= \int z\,x\,dm = 0 \quad &\text{(zero third coordinate)} \\
> P^G_{xz,yz} &= \sigma\int x\,y\,dA = 0 \quad &\text{(each rectangle is symmetric in $x$: $\int x\,dx$ between opposite limits is zero)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G^{I} = \begin{bmatrix} I_{Gx}^{I} & 0 & 0 \cr 0 & I_{Gy}^{I} & 0 \cr 0 & 0 & I_{Gx}^{I} + I_{Gy}^{I} \end{bmatrix}, \qquad P^G_{xz,yz} = 0}$$
>
> **Units:** every element in $[\mathrm M\,\mathrm L^2]$
> **Meaning:** both planes $Gxz$ and $Gyz$ are planes of symmetry of the I; either of them alone is enough to cancel the product $P_{xz,yz}$.

#### Shape C

The C is the union of three rectangles in $S_{O'}$: the top bar (abscissa between 0 and $w$, ordinate between half of $h$ minus $t$ and half of $h$), the bottom bar (its mirror image in the plane $O'xz$) and the back (abscissa between 0 and $t$, ordinate between minus and plus the quantity half of $h$ minus $t$).

![[attachments/EM-SOL/rb04-c-shape.svg]]

> [!derivation] Area and centre of mass of the C
> **Law:** total mass and first moment of the mass distribution; the centre of mass lies on a plane of symmetry
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.7; Notes.pdf, Eq. 10.8; Notes.pdf, Sec. 10.3; Problems.pdf, p. 38
>
> $$\begin{aligned}
> A_C &= 2\,\big[x\big]_0^{w}\big[y\big]_{h/2-t}^{h/2} + \big[x\big]_0^{t}\big[y\big]_{-(h/2-t)}^{h/2-t} \quad &\text{(two bars and the back; antiderivative of 1)} \\
> &= 2\,w\,t + t\,(h-2t) \quad &\text{(Barrow's rule, both limits)} \\
> m &= \sigma\,t\,(2w + h - 2t) \quad &\text{(Eq. 10.6 with constant $\sigma$)} \\
> y_G &= 0 \quad &\text{(the plane $O'xz$ is a plane of symmetry of the C, Sec. 10.3)} \\
> m\,x_G &= 2\,\sigma\,t\int_0^{w} x\,dx + \sigma\,(h-2t)\int_0^{t} x\,dx \quad &\text{(first moment, Eq. 10.7; the $y$ integrals give $t$, $t$ and $h-2t$)} \\
> &= 2\,\sigma\,t\Big[\tfrac{x^2}{2}\Big]_0^{w} + \sigma\,(h-2t)\Big[\tfrac{x^2}{2}\Big]_0^{t} \quad &\text{(antiderivative of $x$)} \\
> &= \sigma\,t\,w^2 + \sigma\,(h-2t)\,\tfrac{t^2}{2} \quad &\text{(Barrow's rule, lower limit zero)} \\
> x_G &= \frac{2\,w^2 + t\,(h-2t)}{2\,(2w + h - 2t)} \quad &\text{(divide by the mass; $\sigma\,t$ cancels)}
> \end{aligned}$$
>
> $$\boxed{A_C = 2\,w\,t + t\,(h-2t), \qquad m = \sigma\,t\,(2w+h-2t), \qquad \mathbf r_{O'}^G = \frac{2\,w^2 + t\,(h-2t)}{2\,(2w+h-2t)}\,\mathbf i}$$
>
> **Units:** $x_G$ is $[\mathrm L^2]/[\mathrm L] = [\mathrm L]$
> **Meaning:** $G$ is on the horizontal symmetry line, between the back and the middle of the bars; it does not lie on the plate when the bars are thin and long.

> [!derivation] Moments of inertia of the C about Gx and Gy
> **Law:** moment of inertia about a coordinate axis; Steiner's theorem for the parallel axis
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.48; Notes.pdf, Sec. 10.8
>
> The ordinate of $G$ is zero, so the axis $Gx$ is the same line as $O'x$.
>
> $$\begin{aligned}
> I_{Gx} &= \sigma\,w\Big[\tfrac{y^3}{3}\Big]_{h/2-t}^{h/2} + \sigma\,w\Big[\tfrac{y^3}{3}\Big]_{-h/2}^{-(h/2-t)} + \sigma\,t\Big[\tfrac{y^3}{3}\Big]_{-(h/2-t)}^{h/2-t} \quad &\text{(Eq. 10.11; the $x$ integrals give $w$, $w$, $t$)} \\
> &= \tfrac{\sigma}{12}\big[w\,h^3 - (w-t)(h-2t)^3\big] \quad &\text{(Barrow's rule and the same collection of terms as for the I)} \\
> I_{O'y} &= 2\,\sigma\,t\Big[\tfrac{x^3}{3}\Big]_0^{w} + \sigma\,(h-2t)\Big[\tfrac{x^3}{3}\Big]_0^{t} \quad &\text{(Eq. 10.11 about $O'y$; the $y$ integrals give $t$, $t$, $h-2t$)} \\
> &= \tfrac{\sigma}{3}\big[2\,t\,w^3 + (h-2t)\,t^3\big] \quad &\text{(Barrow's rule, lower limit zero)} \\
> I_{Gy} &= I_{O'y} - m\,x_G^2 \quad &\text{(Steiner: the axes $O'y$ and $Gy$ are parallel, at the distance $x_G$)} \\
> &= \tfrac{\sigma t}{3}\big[2\,w^3 + (h-2t)\,t^2\big] - \sigma\,t\,(2w+h-2t)\,\frac{\big[2w^2 + t(h-2t)\big]^2}{4\,(2w+h-2t)^2} \quad &\text{(substitute the mass and the abscissa of $G$)} \\
> &= \sigma\,t\,\frac{4\,(2w+h-2t)\big[2w^3 + (h-2t)t^2\big] - 3\big[2w^2 + t(h-2t)\big]^2}{12\,(2w+h-2t)} \quad &\text{(common denominator)} \\
> &= \sigma\,t\,\frac{4w^4 + 8(h-2t)w^3 - 12(h-2t)w^2t + 8(h-2t)wt^2 + (h-2t)^2t^2}{12\,(2w+h-2t)} \quad &\text{(expand and collect)}
> \end{aligned}$$
>
> $$\boxed{I_{Gx}^{C} = \frac{\sigma}{12}\big[w\,h^3 - (w-t)(h-2t)^3\big], \qquad I_{Gy}^{C} = \frac{\sigma}{3}\big[2\,t\,w^3 + (h-2t)\,t^3\big] - m\,x_G^2}$$
>
> **Units:** $[\mathrm M\,\mathrm L^2]$ in every term
> **Meaning:** about the horizontal axis the C equals the I: sliding a bar sideways does not change any ordinate, and $I_{Gx}$ depends only on the ordinates. About the vertical axis the C is less compact than the I, because its bars sit on one side of the back instead of being centred on it.

> [!derivation] Products of inertia of the C
> **Law:** a product of inertia vanishes when one of its planes is a plane of symmetry; Steiner's theorem for products
> **Source:** Notes.pdf, Eq. 10.15; Notes.pdf, Sec. 10.4; Notes.pdf, Eq. 10.48
>
> $$\begin{aligned}
> P^G_{xy,xz} &= \int z\,y\,dm = 0 \quad &\text{(zero third coordinate)} \\
> P^G_{xy,yz} &= \int z\,(x - x_G)\,dm = 0 \quad &\text{(zero third coordinate)} \\
> P^G_{xz,yz} &= \sigma\int (x - x_G)\,y\,dA \quad &\text{(Eq. 10.15 in $S_G$)} \\
> \int_{h/2-t}^{h/2} y\,dy + \int_{-h/2}^{-(h/2-t)} y\,dy &= \Big[\tfrac{y^2}{2}\Big]_{h/2-t}^{h/2} + \Big[\tfrac{y^2}{2}\Big]_{-h/2}^{-(h/2-t)} = 0 \quad &\text{(Barrow: the two brackets are opposite; the bars share the same $x$ integral)} \\
> \int_{-(h/2-t)}^{h/2-t} y\,dy &= 0 \quad &\text{(back: symmetric limits)} \\
> P^G_{xz,yz} &= 0 \quad &\text{(sum of the three rectangles)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G^{C} = \begin{bmatrix} I_{Gx}^{C} & 0 & 0 \cr 0 & I_{Gy}^{C} & 0 \cr 0 & 0 & I_{Gx}^{C} + I_{Gy}^{C} \end{bmatrix}, \qquad P^G_{xz,yz} = 0}$$
>
> **Units:** every element in $[\mathrm M\,\mathrm L^2]$
> **Meaning:** for the C the plane of symmetry is $Gxz$ (each point at ordinate $y$ has a twin at $-y$), not $Gyz$; one plane of symmetry is enough to cancel $P_{xz,yz}$. The product with respect to $O'$ is also zero, because the Steiner correction is the mass times the product of the two coordinates of $G$ and the ordinate of $G$ is zero.

### Linear Momentum, Angular Momentum and Kinetic Energy

This section does not apply: the plates are not moving, and only their mass geometry is asked.

### Free-Body Diagram and Equations of Motion

This section does not apply: no force acts in the statement and no equation of motion is written.

### Answers and Checks

| Asked | T | I | C |
| :--- | :--- | :--- | :--- |
| Area | $t(w+h-t)$ | $2wt + t(h-2t)$ | $2wt + t(h-2t)$ |
| Centre of mass | on the symmetry line, at $\frac{wt-(h-t)^2}{2(w+h-t)}$ above the lower edge of the top bar | centre of the letter | on the symmetry line, at $\frac{2w^2+t(h-2t)}{2(2w+h-2t)}$ from the back |
| $I_{Gx}$ | $\frac{\sigma}{3}[wt^3+t(h-t)^3] - m y_G^2$ | $\frac{\sigma}{12}[wh^3-(w-t)(h-2t)^3]$ | $\frac{\sigma}{12}[wh^3-(w-t)(h-2t)^3]$ |
| $I_{Gy}$ | $\frac{\sigma t}{12}[w^3+(h-t)t^2]$ | $\frac{\sigma}{12}[2tw^3+(h-2t)t^3]$ | $\frac{\sigma}{3}[2tw^3+(h-2t)t^3] - m x_G^2$ |
| $P_{xz,yz}$ | 0 (plane $Gyz$ of symmetry) | 0 (planes $Gxz$ and $Gyz$ of symmetry) | 0 (plane $Gxz$ of symmetry) |

The masses are $\sigma$ times the areas; the moments about $Gz$ are the sums of the moments about $Gx$ and $Gy$, and all the products of inertia vanish, so $Gx$, $Gy$, $Gz$ are principal axes of each plate. The product of inertia can be inferred from the geometry without any integral: each letter has a symmetry line in its plane, and the plane through that line normal to the plate is one of the two planes of $P_{xz,yz}$.

**Check against the official key:** the key (Problems.pdf, p. 77) uses the same auxiliary frame for the T (vertical axis on the symmetry line, horizontal axis on the lower edge of the top bar). It prints the same position of $G$, the moment about $Gx$ as one third of $\sigma$ times the bracket with $w\,t^3$ and $(h-t)^3\,t$ minus $m\,r^2$, with $r$ the opposite of the ordinate of $G$ (the square removes the sign, so this is the Steiner line of the box above), the same moment about $Gy$, and a zero product of inertia. All four coincide with the results above. The key prints nothing for the I and the C, which are checked below.

**Limiting cases and consistency:**

> [!derivation] Check: the letters collapse into one rectangle, and thin walls
> **Law:** moments of inertia of the limiting shapes, from the results above
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.24; Notes.pdf, Eq. 10.25
>
> With bars as long as they are thick, each letter becomes one rectangle of width $t$ and height $h$, centred at its middle.
>
> $$\begin{aligned}
> y_G^{T}\big|_{w=t} &= \frac{t^2 - (h-t)^2}{2h} = t - \tfrac h2 \quad &\text{(difference of squares; this is the middle of the rectangle from $-(h-t)$ to $t$)} \\
> I_{Gx}^{T}\big|_{w=t} &= \frac{\sigma\,t\,\big[(h-t) + t\big]^4}{12\,h} = \frac{\sigma\,t\,h^3}{12} \quad &\text{(the numerator becomes the binomial expansion of the fourth power)} \\
> I_{Gx}^{I}\big|_{w=t} &= I_{Gx}^{C}\big|_{w=t} = \frac{\sigma\,t\,h^3}{12} \quad &\text{(the bracket with $w-t$ vanishes)} \\
> I_{Gy}^{T}\big|_{w=t} &= I_{Gy}^{I}\big|_{w=t} = \frac{\sigma\,h\,t^3}{12} \quad &\text{(substitute and add)} \\
> x_G^{C}\big|_{w=t} &= \frac{2t^2 + th - 2t^2}{2h} = \frac t2, \qquad I_{Gy}^{C}\big|_{w=t} = \frac{\sigma\,t\,t^2h^2}{12\,h} = \frac{\sigma\,h\,t^3}{12} \quad &\text{(the numerator becomes the square of $t(2t + h - 2t)$)} \\
> I_{Gx}^{I} &\approx \frac{\sigma\,t\,h^3}{12} + 2\,(\sigma\,w\,t)\Big(\frac h2\Big)^2 \quad &\text{(thin walls: keep the terms linear in $t$; stem plus two bars at the distance half of $h$)}
> \end{aligned}$$
>
> $$\boxed{\text{all three letters give } \frac{\sigma\,t\,h^3}{12} \text{ and } \frac{\sigma\,h\,t^3}{12} \text{ when } w \to t}$$
>
> **Units:** $[\mathrm M\,\mathrm L^2]$
> **Meaning:** the limits are the central moments of a rectangle (the form of Eqs. 10.25 and 10.26 of the notes, with mass $\sigma t h$), so the three general results are consistent; in the thin-walled I the bars act as two point masses at the distance half of $h$ from the axis, plus the stem as a slender bar.

* **Equal moments about the horizontal axis.** The I and the C have the same moment about $Gx$, as they must: they differ only by a horizontal shift of the bars.
* **Ordering about the vertical axis.** The moment of the C about $Gy$ is larger than that of the I with the same dimensions, because its mass is spread on one side of the back. Subtracting the two closed forms (checked with a computer algebra system) leaves $\sigma$ times $t\,w\,(h-2t)(w-t)^2$ over twice $(2w+h-2t)$, which is positive and vanishes for bars as long as they are thick, where both letters become the same rectangle.
* **Dimensions.** Areas in m², positions in m, moments of inertia in kg·m² (surface density times the fourth power of a length).

---

## Problem RB-05: Moments of inertia (3D shapes a-j)

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** ten homogeneous rigid bodies. Bodies with volume have uniform density $\rho$ (kg/m³); the thin disk, the semicircular plate and the flat sheet are modelled as plates of uniform surface density $\sigma$ (kg/m²), the slender bar and the wire as lines of uniform linear density $\lambda$ (kg/m). Each density is replaced by the mass at the end of its calculation.
* **Frames:** each body has its central frame $S_G$, with origin at its centre of mass $G$ and the right-handed basis $\{\mathbf i, \mathbf j, \mathbf k\}$ along the axes $x$, $y$, $z$ of the statement figures, so that the tensors are written in the same axes as the official key. Where $G$ is not the natural origin of the integral, an auxiliary frame $S_O$ (or $S_V$, $S_A$) parallel to $S_G$ is used and the result is translated to $G$ with Steiner's theorem.
* **Degrees of freedom:** each body is a rigid body with six degrees of freedom, but no motion is involved: only mass properties are asked.
* **Coordinates and volume elements:** Cartesian, cylindrical or the spherical coordinates of the notes (radius $r$, longitude $\theta$ measured in a coordinate plane, latitude $\varphi$ measured from that plane), with the jacobians of Eq. 10.5 of the notes.

| Part | Body | Axes (read from the figures) | Auxiliary origin |
| :--- | :--- | :--- | :--- |
| (a) | slender bar, length $L$, cross-section $A$ negligible | $x$ along the bar | none |
| (b) | cylinder, radius $R$, length $L$ | $z$ along the axis of the cylinder; $x$, $y$ in the middle cross-section | none |
| (c) | rectangular parallelepiped, edges $a$, $b$, $c$ | edge $a$ parallel to $x$, $b$ parallel to $y$, $c$ parallel to $z$ | none |
| (d) | sphere, radius $R$ | any three orthogonal axes through the centre | none |
| (e) | hemisphere, radius $R$ | flat face horizontal; $z$ normal to it, pointing from the face into the body (downwards in the figure) | $O$: centre of the flat face, $G$ at $3R/8$ from it |
| (f) | right circular cone, base radius $R$, height $L$ | $x$ along the axis, pointing from the apex towards the base | $V$: the apex, $G$ at $3L/4$ from it |
| (g) | thin disk, radius $R$, thickness $h \ll R$ | $z$ along the axis; $x$, $y$ in the mid-plane | none |
| (h) | semicircular plate, radius $R$, thickness $h \ll R$ | $z$ normal to the plate; diameter parallel to $y$; $x$ along the symmetry axis, pointing from the diameter towards the arc | $O$: centre of the diameter, $G$ at $4R/(3\pi)$ from it |
| (i) | semicircular wire, radius $R$, cross-section $A$ negligible | $z$ normal to the plane of the arc; $x$ parallel to the diameter through the two ends; $y$ along the symmetry axis, towards the arc | $O$: centre of the circle, $G$ at $2R/\pi$ from it |
| (j) | flat sheet, length $L$, width $w$ (no figure) | $x$ along the edge of length $L$, $y$ along the edge of width $w$, $z$ normal to the sheet | $A$: the vertex where those two edges meet |

* **Unknowns:** the tensor of inertia $\bar{\bar I}_G$ of each body in its central frame (Eq. 10.38 of the notes: moments on the diagonal, minus the products off the diagonal); for (j) also the tensor $\bar{\bar I}_A$ at the vertex.

### Change of Basis, Position Vectors and Constraint Kinematics

No rotation of the basis is needed: each auxiliary frame is parallel to the central frame of its body. The only operation between frames is a translation of the origin by the position vector of $G$, handled with Steiner's theorem, written once here in components.

> [!derivation] Steiner's theorem in components for a translation of the origin
> **Law:** Steiner's theorem; components of the tensor of inertia
> **Source:** Notes.pdf, Eq. 10.48; Notes.pdf, Eq. 10.36; Notes.pdf, Eq. 10.37; Notes.pdf, Eq. 10.38
>
> Let the centre of mass have the position vector $\mathbf r_O^G$ with components $x_G$, $y_G$, $z_G$ in the auxiliary frame with origin $O$.
>
> $$\begin{aligned}
> \bar{\bar I}_O &= \bar{\bar I}_G + m\left[(\mathbf r_O^G)^2\,U - \mathbf r_O^G\otimes\mathbf r_O^G\right] \quad &\text{(Steiner's theorem, Eq. 10.48; both tensors in the same basis)} \\
> (\mathbf r_O^G)^2\,U &= (x_G^2 + y_G^2 + z_G^2)\begin{bmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(squared modulus times the unit tensor, Eq. 10.36)} \\
> \mathbf r_O^G\otimes\mathbf r_O^G &= \begin{bmatrix} x_G^2 & x_Gy_G & x_Gz_G \cr x_Gy_G & y_G^2 & y_Gz_G \cr x_Gz_G & y_Gz_G & z_G^2 \end{bmatrix} \quad &\text{(dyad, Eq. 10.37)} \\
> (\mathbf r_O^G)^2\,U - \mathbf r_O^G\otimes\mathbf r_O^G &= \begin{bmatrix} y_G^2+z_G^2 & -x_Gy_G & -x_Gz_G \cr -x_Gy_G & x_G^2+z_G^2 & -y_Gz_G \cr -x_Gz_G & -y_Gz_G & x_G^2+y_G^2 \end{bmatrix} \quad &\text{(subtract element by element)} \\
> I_{Ox} &= I_{Gx} + m\,(y_G^2 + z_G^2) \quad &\text{(element 11, and likewise 22 and 33 with the other two coordinates)} \\
> P^O_{xz,yz} &= P^G_{xz,yz} + m\,x_G\,y_G \quad &\text{(element 12 is minus the product; likewise for the other pairs)}
> \end{aligned}$$
>
> $$\boxed{I_{Gx} = I_{Ox} - m\,(y_G^2 + z_G^2), \quad I_{Gy} = I_{Oy} - m\,(x_G^2 + z_G^2), \quad I_{Gz} = I_{Oz} - m\,(x_G^2 + y_G^2), \quad P^G_{xz,yz} = P^O_{xz,yz} - m\,x_G\,y_G}$$
>
> **Units:** every term in $[\mathrm M\,\mathrm L^2]$, kg·m²
> **Meaning:** each moment changes by the mass times the squared distance between the two parallel axes (the distance from $G$ to the axis through $O$); an axis that contains both $O$ and $G$ keeps its moment. When $G$ lies on one coordinate axis of the auxiliary frame, every Steiner correction of the products vanishes.

### Center of Mass and Inertia Tensor

For every body, the products of inertia are found from the planes of symmetry: by Sec. 10.4 of the notes, a product of inertia vanishes whenever one of its two planes is a plane of symmetry of the body. The three products are $P_{xy,xz}$, $P_{xy,yz}$ and $P_{xz,yz}$ (Eq. 10.15).

#### Part (a): slender bar

![[attachments/EM-SOL/rb05-a-bar.svg]]

> [!derivation] Inertia tensor of the slender bar
> **Law:** total mass, moments of inertia about the coordinate axes, line density
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.15; Notes.pdf, Sec. 10.4; Problems.pdf, p. 38
>
> The bar occupies the segment of the axis $x$ between minus and plus half of $L$; its section is negligible, so every point has zero $y$ and $z$ and the mass element is $\lambda\,dx$, with $\lambda$ equal to $\rho A$.
>
> $$\begin{aligned}
> m &= \int_{-L/2}^{L/2} \lambda\,dx = \lambda\big[x\big]_{-L/2}^{L/2} = \lambda\Big(\tfrac L2 + \tfrac L2\Big) = \lambda\,L \quad &\text{(Eq. 10.6, antiderivative of 1 and Barrow's rule)} \\
> \lambda &= \frac mL \quad &\text{(solve for the density)} \\
> x_G &= 0 \quad &\text{(the plane $x$ equal to zero bisects the bar and is a plane of symmetry, Sec. 10.3)} \\
> I_{Gx} &= \int (y^2 + z^2)\,dm = 0 \quad &\text{(Eq. 10.11; every point of the bar has zero $y$ and $z$)} \\
> I_{Gy} &= \int (x^2 + z^2)\,dm = \lambda\int_{-L/2}^{L/2} x^2\,dx \quad &\text{(Eq. 10.11 with zero $z$)} \\
> &= \lambda\Big[\tfrac{x^3}{3}\Big]_{-L/2}^{L/2} \quad &\text{(antiderivative of $x^2$)} \\
> &= \lambda\Big(\tfrac{L^3}{24} + \tfrac{L^3}{24}\Big) = \frac{\lambda\,L^3}{12} \quad &\text{(Barrow's rule, both limits)} \\
> &= \frac{m\,L^2}{12} \quad &\text{(substitute the density)} \\
> I_{Gz} &= \int (x^2 + y^2)\,dm = \frac{m\,L^2}{12} \quad &\text{(same integral, since $y$ is zero as $z$ was)} \\
> P_{xy,xz} &= \int z\,y\,dm = 0, \quad P_{xy,yz} = \int z\,x\,dm = 0, \quad P_{xz,yz} = \int y\,x\,dm = 0 \quad &\text{(Eq. 10.15: each integrand has the factor $y$ or $z$)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = \frac{m\,L^2}{12}\begin{bmatrix} 0 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{bmatrix}}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** all the mass is on the axis $x$, so it has no moment about that axis; about any transverse axis through $G$ the bar has the same moment, one twelfth of the mass times the squared length.

#### Part (b): cylinder

![[attachments/EM-SOL/rb05-b-cylinder.svg]]

> [!derivation] Mass and moment of the cylinder about its axis
> **Law:** total mass and moment of inertia in cylindrical coordinates
> **Source:** Notes.pdf, Eq. 10.5; Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.11; Problems.pdf, p. 38
>
> Cylindrical coordinates about $z$: the abscissa is $r\cos\theta$ and the ordinate $r\sin\theta$, with $r$ from 0 to $R$, $\theta$ from 0 to $2\pi$ and $z$ from minus to plus half of $L$; the volume element is $r\,dr\,d\theta\,dz$ (jacobian $r$, Eq. 10.5). The limits are constant, so each triple integral is the product of three simple integrals.
>
> $$\begin{aligned}
> m &= \rho\int_{-L/2}^{L/2}\!\int_0^{2\pi}\!\int_0^{R} r\,dr\,d\theta\,dz \quad &\text{(Eq. 10.6 with $dm = \rho\,dV$)} \\
> &= \rho\Big[\tfrac{r^2}{2}\Big]_0^{R}\big[\theta\big]_0^{2\pi}\big[z\big]_{-L/2}^{L/2} \quad &\text{(antiderivatives)} \\
> &= \rho\,\tfrac{R^2}{2}\,(2\pi)\,L = \rho\,\pi\,R^2L \quad &\text{(Barrow's rule, both limits each time)} \\
> I_{Gz} &= \rho\int (x^2 + y^2)\,r\,dr\,d\theta\,dz = \rho\int_{-L/2}^{L/2}\!\int_0^{2\pi}\!\int_0^{R} r^3\,dr\,d\theta\,dz \quad &\text{(Eq. 10.11; $x^2 + y^2$ equals $r^2(\cos^2\theta + \sin^2\theta) = r^2$)} \\
> &= \rho\Big[\tfrac{r^4}{4}\Big]_0^{R}(2\pi)\,L = \frac{\rho\,\pi\,R^4L}{2} \quad &\text{(antiderivative of $r^3$ and Barrow's rule)} \\
> &= \frac{m\,R^2}{2} \quad &\text{(divide by the mass and multiply by it)}
> \end{aligned}$$
>
> $$\boxed{m = \rho\,\pi\,R^2L, \qquad I_{Gz} = \frac{m\,R^2}{2}}$$
>
> **Units:** $[\mathrm M\,\mathrm L^{-3}][\mathrm L^5] = [\mathrm M\,\mathrm L^2]$
> **Meaning:** the moment about the axis depends only on the distances to the axis, so it does not depend on the length; it is half that of a thin ring of the same mass and radius, since much of the mass is close to the axis.

> [!derivation] Transverse moments and products of the cylinder
> **Law:** moments of inertia about the coordinate axes; vanishing products for planes of symmetry
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.15; Notes.pdf, Sec. 10.4
>
> $$\begin{aligned}
> \int y^2\,dm &= \rho\int_{-L/2}^{L/2}\!\int_0^{2\pi}\!\int_0^{R} r^3\sin^2\theta\,dr\,d\theta\,dz \quad &\text{(ordinate $r\sin\theta$, element $r\,dr\,d\theta\,dz$)} \\
> \int_0^{2\pi}\sin^2\theta\,d\theta &= \Big[\tfrac{\theta}{2} - \tfrac{\sin 2\theta}{4}\Big]_0^{2\pi} = \pi - 0 = \pi \quad &\text{(identity $\sin^2\theta = (1 - \cos 2\theta)/2$, antiderivative and Barrow)} \\
> \int y^2\,dm &= \rho\,\tfrac{R^4}{4}\,\pi\,L = \frac{m\,R^2}{4} \quad &\text{(the $r$ and $z$ integrals give $R^4/4$ and $L$; substitute the mass)} \\
> \int x^2\,dm &= \rho\,\tfrac{R^4}{4}\Big[\tfrac{\theta}{2} + \tfrac{\sin 2\theta}{4}\Big]_0^{2\pi} L = \frac{m\,R^2}{4} \quad &\text{(same with $\cos^2\theta = (1 + \cos 2\theta)/2$; the bracket is again $\pi$)} \\
> \int z^2\,dm &= \rho\Big[\tfrac{r^2}{2}\Big]_0^{R}(2\pi)\Big[\tfrac{z^3}{3}\Big]_{-L/2}^{L/2} \quad &\text{(antiderivatives)} \\
> &= \rho\,\tfrac{R^2}{2}\,(2\pi)\Big(\tfrac{L^3}{24} + \tfrac{L^3}{24}\Big) = \frac{\rho\,\pi\,R^2L^3}{12} = \frac{m\,L^2}{12} \quad &\text{(Barrow's rule and the mass)} \\
> I_{Gx} &= \int y^2\,dm + \int z^2\,dm = \frac{m}{12}\,(3R^2 + L^2) \quad &\text{(Eq. 10.11)} \\
> I_{Gy} &= \int x^2\,dm + \int z^2\,dm = \frac{m}{12}\,(3R^2 + L^2) \quad &\text{(Eq. 10.11)} \\
> P_{xy,xz} &= P_{xy,yz} = P_{xz,yz} = 0 \quad &\text{(the planes $Gxy$, $Gxz$, $Gyz$ are planes of symmetry, Sec. 10.4)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = \frac{m}{12}\begin{bmatrix} 3R^2 + L^2 & 0 & 0 \cr 0 & 3R^2 + L^2 & 0 \cr 0 & 0 & 6R^2 \end{bmatrix}}$$
>
> **Units:** $[\mathrm M\,\mathrm L^2]$ in every element
> **Meaning:** a transverse moment adds the spread across the axis (a quarter of the mass times the squared radius) and the spread along it (one twelfth of the mass times the squared length). Each plane through $G$ normal to an axis maps the cylinder onto itself, so every product contains a plane of symmetry.

#### Part (c): rectangular parallelepiped

![[attachments/EM-SOL/rb05-c-box.svg]]

> [!derivation] Inertia tensor of the rectangular parallelepiped
> **Law:** moments of inertia with respect to the coordinate planes and axes; vanishing products for planes of symmetry
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.12; Notes.pdf, Sec. 10.4; Problems.pdf, p. 38
>
> Cartesian coordinates with volume element $dx\,dy\,dz$ (jacobian 1) and limits plus and minus half of $a$, $b$, $c$ for $x$, $y$, $z$. The moments with respect to the coordinate planes (Eq. 10.12) are found first.
>
> $$\begin{aligned}
> m &= \rho\big[x\big]_{-a/2}^{a/2}\big[y\big]_{-b/2}^{b/2}\big[z\big]_{-c/2}^{c/2} = \rho\,a\,b\,c \quad &\text{(Eq. 10.6, antiderivative of 1 and Barrow's rule)} \\
> \int x^2\,dm &= \rho\Big[\tfrac{x^3}{3}\Big]_{-a/2}^{a/2}\,b\,c = \rho\Big(\tfrac{a^3}{24} + \tfrac{a^3}{24}\Big)b\,c \quad &\text{(the $y$ and $z$ integrals give $b$ and $c$; Barrow's rule)} \\
> &= \frac{\rho\,a^3\,b\,c}{12} = \frac{m\,a^2}{12} \quad &\text{(add and substitute the mass)} \\
> \int y^2\,dm &= \frac{m\,b^2}{12}, \qquad \int z^2\,dm = \frac{m\,c^2}{12} \quad &\text{(same integral with $b$ or $c$ in place of $a$)} \\
> I_{Gx} &= \int (y^2 + z^2)\,dm = \frac{m}{12}\,(b^2 + c^2) \quad &\text{(Eq. 10.11)} \\
> I_{Gy} &= \int (x^2 + z^2)\,dm = \frac{m}{12}\,(a^2 + c^2) \quad &\text{(Eq. 10.11)} \\
> I_{Gz} &= \int (x^2 + y^2)\,dm = \frac{m}{12}\,(a^2 + b^2) \quad &\text{(Eq. 10.11)} \\
> P_{xy,xz} &= P_{xy,yz} = P_{xz,yz} = 0 \quad &\text{(the three coordinate planes through $G$ are planes of symmetry, Sec. 10.4)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = \frac{m}{12}\begin{bmatrix} b^2 + c^2 & 0 & 0 \cr 0 & a^2 + c^2 & 0 \cr 0 & 0 & a^2 + b^2 \end{bmatrix}}$$
>
> **Units:** $[\mathrm M\,\mathrm L^2]$
> **Meaning:** the moment about each axis involves only the two edges perpendicular to it; the edge along the axis does not matter.

#### Part (d): sphere

![[attachments/EM-SOL/rb05-d-sphere.svg]]

> [!derivation] Inertia tensor of the sphere
> **Law:** total mass and moments of inertia in spherical coordinates; polar moment and Eq. 10.13 as a check
> **Source:** Notes.pdf, Eq. 10.5; Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.10; Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.13; Notes.pdf, Sec. 10.4; Problems.pdf, p. 38
>
> Spherical coordinates of the notes: the coordinates of a point are $r\cos\varphi\cos\theta$, $r\cos\varphi\sin\theta$ and $r\sin\varphi$, with $r$ from 0 to $R$, longitude $\theta$ from 0 to $2\pi$ and latitude $\varphi$ from minus to plus half of $\pi$; the volume element is $r^2\cos\varphi\,dr\,d\theta\,d\varphi$ (Eq. 10.5). The latitude integrals use the substitution $u$ equal to $\sin\varphi$, with $du$ equal to $\cos\varphi\,d\varphi$, which carries the limits to minus 1 and plus 1.
>
> $$\begin{aligned}
> m &= \rho\Big[\tfrac{r^3}{3}\Big]_0^{R}\big[\theta\big]_0^{2\pi}\big[\sin\varphi\big]_{-\pi/2}^{\pi/2} = \rho\,\tfrac{R^3}{3}\,(2\pi)\,(1+1) = \tfrac43\,\rho\,\pi\,R^3 \quad &\text{(Eq. 10.6; antiderivatives and Barrow's rule)} \\
> I_{Gz} &= \rho\int (x^2 + y^2)\,r^2\cos\varphi\,dr\,d\theta\,d\varphi = \rho\int_0^{R} r^4\,dr\int_0^{2\pi} d\theta\int_{-\pi/2}^{\pi/2}\cos^3\varphi\,d\varphi \quad &\text{(Eq. 10.11; $x^2+y^2$ equals $r^2\cos^2\varphi$)} \\
> \int_{-\pi/2}^{\pi/2}\cos^3\varphi\,d\varphi &= \int_{-1}^{1}(1 - u^2)\,du = \Big[u - \tfrac{u^3}{3}\Big]_{-1}^{1} = \tfrac23 + \tfrac23 = \tfrac43 \quad &\text{(substitution: $\cos^2\varphi = 1 - u^2$; Barrow's rule)} \\
> I_{Gz} &= \rho\,\tfrac{R^5}{5}\,(2\pi)\,\tfrac43 = \tfrac{8}{15}\,\rho\,\pi\,R^5 = \tfrac25\,m\,R^2 \quad &\text{(antiderivative of $r^4$, Barrow's rule, substitute the mass)} \\
> I_{Gx} &= I_{Gy} = \tfrac25\,m\,R^2 \quad &\text{(a rotation that carries $z$ onto $x$ or $y$ maps the sphere onto itself)} \\
> I_G &= \rho\int r^2\,r^2\cos\varphi\,dr\,d\theta\,d\varphi = \rho\,\tfrac{R^5}{5}\,(2\pi)\,(2) = \tfrac35\,m\,R^2 \quad &\text{(check: polar moment, Eq. 10.10)} \\
> I_{Gx} + I_{Gy} + I_{Gz} &= \tfrac65\,m\,R^2 = 2\,I_G \quad &\text{(Eq. 10.13 holds)} \\
> P_{xy,xz} &= P_{xy,yz} = P_{xz,yz} = 0 \quad &\text{(every plane through $G$ is a plane of symmetry, Sec. 10.4)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = \frac{2\,m\,R^2}{5}\begin{bmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{bmatrix}}$$
>
> **Units:** $[\mathrm M\,\mathrm L^{-3}][\mathrm L^5] = [\mathrm M\,\mathrm L^2]$
> **Meaning:** the tensor is spherical: every axis through the centre is a principal axis with the same moment, two fifths of the mass times the squared radius.

#### Part (e): hemisphere

![[attachments/EM-SOL/rb05-e-hemisphere.svg]]

> [!derivation] Mass and centre of mass of the hemisphere
> **Law:** total mass and first moment in spherical coordinates; the centre of mass lies on the planes of symmetry
> **Source:** Notes.pdf, Eq. 10.5; Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.7; Notes.pdf, Eq. 10.8; Notes.pdf, Sec. 10.3; Problems.pdf, p. 39
>
> In the auxiliary frame $S_O$, at the centre of the flat face and parallel to $S_G$, the body is the half of the ball on the side of positive $z$ (the side of the dome, below the face in the figure). In the spherical coordinates of the notes this is the latitude $\varphi$ from 0 to half of $\pi$, with $r$ from 0 to $R$ and $\theta$ from 0 to $2\pi$; the third coordinate is $r\sin\varphi$.
>
> $$\begin{aligned}
> m &= \rho\Big[\tfrac{r^3}{3}\Big]_0^{R}\big[\theta\big]_0^{2\pi}\big[\sin\varphi\big]_0^{\pi/2} = \rho\,\tfrac{R^3}{3}\,(2\pi)\,(1 - 0) = \tfrac23\,\rho\,\pi\,R^3 \quad &\text{(Eq. 10.6; antiderivatives and Barrow's rule)} \\
> x_G &= y_G = 0 \quad &\text{(the planes $Oxz$ and $Oyz$ are planes of symmetry, Sec. 10.3)} \\
> m\,z_G &= \rho\int_0^{R} r^3\,dr\int_0^{2\pi} d\theta\int_0^{\pi/2}\sin\varphi\cos\varphi\,d\varphi \quad &\text{(Eq. 10.7: $z\,dV$ is $r\sin\varphi\;r^2\cos\varphi\,dr\,d\theta\,d\varphi$)} \\
> \int_0^{\pi/2}\sin\varphi\cos\varphi\,d\varphi &= \int_0^{1} u\,du = \Big[\tfrac{u^2}{2}\Big]_0^{1} = \tfrac12 \quad &\text{(substitution $u = \sin\varphi$, $du = \cos\varphi\,d\varphi$, limits 0 and 1)} \\
> m\,z_G &= \rho\,\tfrac{R^4}{4}\,(2\pi)\,\tfrac12 = \tfrac14\,\rho\,\pi\,R^4 \quad &\text{(antiderivative of $r^3$ and Barrow's rule)} \\
> z_G &= \frac{\rho\,\pi\,R^4/4}{2\rho\,\pi\,R^3/3} = \frac{3R}{8} \quad &\text{(divide by the mass)}
> \end{aligned}$$
>
> $$\boxed{m = \tfrac23\,\rho\,\pi\,R^3, \qquad \mathbf r_O^G = \frac{3R}{8}\,\mathbf k}$$
>
> **Units:** $z_G$ in $[\mathrm M\,\mathrm L][\mathrm M^{-1}] = [\mathrm L]$
> **Meaning:** $G$ is on the symmetry axis, at three eighths of the radius from the flat face towards the dome, as the figure of the statement shows.

> [!derivation] Inertia tensor of the hemisphere at O and at G
> **Law:** moments of inertia in spherical coordinates; Steiner's theorem; vanishing products for planes of symmetry
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.12; Notes.pdf, Eq. 10.48; Notes.pdf, Sec. 10.4
>
> The latitude integrals use the substitution $u$ equal to $\sin\varphi$ (limits 0 and 1); the longitude integrals of the squared cosine and sine over a full turn are $\pi$, from the identities that write them as one half plus or minus half of the cosine of $2\theta$.
>
> $$\begin{aligned}
> \int z^2\,dm &= \rho\int_0^{R} r^4\,dr\int_0^{2\pi}d\theta\int_0^{\pi/2}\sin^2\varphi\cos\varphi\,d\varphi \quad &\text{(Eq. 10.12: $z^2\,dV$ is $r^2\sin^2\varphi\;r^2\cos\varphi\,dr\,d\theta\,d\varphi$)} \\
> &= \rho\,\tfrac{R^5}{5}\,(2\pi)\Big[\tfrac{u^3}{3}\Big]_0^{1} = \tfrac{2}{15}\,\rho\,\pi\,R^5 = \tfrac15\,m\,R^2 \quad &\text{(antiderivatives, Barrow's rule, substitute the mass)} \\
> \int x^2\,dm &= \rho\int_0^{R} r^4\,dr\int_0^{2\pi}\cos^2\theta\,d\theta\int_0^{\pi/2}\cos^3\varphi\,d\varphi \quad &\text{(Eq. 10.12: $x^2$ is $r^2\cos^2\varphi\cos^2\theta$)} \\
> &= \rho\,\tfrac{R^5}{5}\,\pi\Big[u - \tfrac{u^3}{3}\Big]_0^{1} = \rho\,\tfrac{R^5}{5}\,\pi\,\tfrac23 = \tfrac15\,m\,R^2 \quad &\text{(the longitude integral is $\pi$; Barrow's rule)} \\
> \int y^2\,dm &= \tfrac15\,m\,R^2 \quad &\text{(same with $\sin^2\theta$, whose integral over a turn is also $\pi$)} \\
> I_{Ox} &= \int (y^2 + z^2)\,dm = \tfrac25\,m\,R^2, \quad I_{Oy} = \int (x^2 + z^2)\,dm = \tfrac25\,m\,R^2 \quad &\text{(Eq. 10.11)} \\
> I_{Oz} &= \int (x^2 + y^2)\,dm = \tfrac25\,m\,R^2 \quad &\text{(Eq. 10.11)} \\
> I_{Gx} &= I_{Ox} - m\,(y_G^2 + z_G^2) = \tfrac25\,m\,R^2 - m\Big(\tfrac{3R}{8}\Big)^2 \quad &\text{(Steiner: $Ox$ and $Gx$ are parallel, at the distance $z_G$)} \\
> &= \Big(\tfrac25 - \tfrac{9}{64}\Big)m\,R^2 = \tfrac{83}{320}\,m\,R^2 \quad &\text{(common denominator 320)} \\
> I_{Gy} &= I_{Oy} - m\,(x_G^2 + z_G^2) = \Big(\tfrac25 - \tfrac{9}{64}\Big)m\,R^2 \quad &\text{(Steiner, same distance)} \\
> I_{Gz} &= I_{Oz} - m\,(x_G^2 + y_G^2) = \tfrac25\,m\,R^2 \quad &\text{(Steiner: $Oz$ and $Gz$ are the same line)} \\
> P_{xy,xz} &= P_{xy,yz} = P_{xz,yz} = 0 \quad &\text{(each involves $Gxz$ or $Gyz$, planes of symmetry, Sec. 10.4)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = m\,R^2\begin{bmatrix} \tfrac25 - \tfrac{9}{64} & 0 & 0 \cr 0 & \tfrac25 - \tfrac{9}{64} & 0 \cr 0 & 0 & \tfrac25 \end{bmatrix} = m\,R^2\begin{bmatrix} \tfrac{83}{320} & 0 & 0 \cr 0 & \tfrac{83}{320} & 0 \cr 0 & 0 & \tfrac25 \end{bmatrix}}$$
>
> **Units:** $[\mathrm M\,\mathrm L^2]$
> **Meaning:** at the centre of the flat face every axis has the moment of the full sphere per unit mass, because the missing half would be the mirror image of this one. Moving to $G$ reduces only the two transverse moments; the plane $Gxy$ is not a plane of symmetry, but no product needs it.

#### Part (f): right circular cone

![[attachments/EM-SOL/rb05-f-cone.svg]]

> [!derivation] Mass and centre of mass of the cone
> **Law:** total mass and first moment in cylindrical coordinates about the axis of the cone; similar triangles for the radius of a section
> **Source:** Notes.pdf, Eq. 10.5; Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.7; Notes.pdf, Eq. 10.8; Notes.pdf, Sec. 10.3; Problems.pdf, p. 39
>
> In the auxiliary frame $S_V$, at the apex and parallel to $S_G$, a point has the coordinates $s$ (distance from the apex along the axis, towards the base), $r\cos\theta$ and $r\sin\theta$; the volume element is $r\,dr\,d\theta\,ds$ (cylindrical coordinates about the axis, Eq. 10.5). The meridian section is a right triangle with the axis $L$ as one leg, the base radius $R$ as the other leg and the slant side as hypotenuse; the section at the distance $s$ cuts a smaller similar triangle with legs $s$ and $R_s$, so the ratio of the legs is the same.
>
> $$\begin{aligned}
> \frac{R_s}{s} &= \frac RL \quad &\text{(similar right triangles: opposite leg over adjacent leg at the apex angle)} \\
> R_s &= \frac{R\,s}{L} \quad &\text{(upper limit of $r$ at the distance $s$)} \\
> m &= \rho\int_0^{L}\!\int_0^{2\pi}\!\int_0^{Rs/L} r\,dr\,d\theta\,ds \quad &\text{(Eq. 10.6 with $dm = \rho\,dV$; $r$ runs from the axis to $R_s$)} \\
> &= \rho\int_0^{L} 2\pi\Big[\tfrac{r^2}{2}\Big]_0^{Rs/L} ds = \rho\,\frac{\pi R^2}{L^2}\int_0^{L} s^2\,ds \quad &\text{(inner integrals: antiderivatives and Barrow's rule)} \\
> &= \rho\,\frac{\pi R^2}{L^2}\Big[\tfrac{s^3}{3}\Big]_0^{L} = \tfrac13\,\rho\,\pi\,R^2L \quad &\text{(antiderivative of $s^2$ and Barrow's rule)} \\
> y_G &= z_G = 0 \quad &\text{(the planes $Vxy$ and $Vxz$ contain the axis and are planes of symmetry, Sec. 10.3)} \\
> m\,s_G &= \rho\int_0^{L} s\,2\pi\Big[\tfrac{r^2}{2}\Big]_0^{Rs/L} ds = \rho\,\frac{\pi R^2}{L^2}\Big[\tfrac{s^4}{4}\Big]_0^{L} = \tfrac14\,\rho\,\pi\,R^2L^2 \quad &\text{(Eq. 10.7, first component; same inner integrals)} \\
> s_G &= \frac{\rho\,\pi\,R^2L^2/4}{\rho\,\pi\,R^2L/3} = \frac{3L}{4} \quad &\text{(divide by the mass)}
> \end{aligned}$$
>
> $$\boxed{m = \tfrac13\,\rho\,\pi\,R^2L, \qquad \mathbf r_V^G = \frac{3L}{4}\,\mathbf i}$$
>
> **Units:** $[\mathrm M\,\mathrm L^{-3}][\mathrm L^3] = [\mathrm M]$; $s_G$ in $[\mathrm L]$
> **Meaning:** most of the volume is near the base, so $G$ is at three quarters of the height from the apex, a quarter from the base, as the figure shows.

> [!derivation] Inertia tensor of the cone at the apex and at G
> **Law:** moments of inertia about the coordinate axes; Steiner's theorem; vanishing products for planes of symmetry
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.12; Notes.pdf, Eq. 10.48; Notes.pdf, Sec. 10.4
>
> $$\begin{aligned}
> I_{Gx} &= I_{Vx} = \rho\int_0^{L}\!\int_0^{2\pi}\!\int_0^{Rs/L} r^2\,r\,dr\,d\theta\,ds \quad &\text{(Eq. 10.11; the axis $Vx$ contains $G$, so no translation; $y^2+z^2$ is $r^2$)} \\
> &= \rho\int_0^{L} 2\pi\Big[\tfrac{r^4}{4}\Big]_0^{Rs/L} ds = \rho\,\frac{\pi R^4}{2L^4}\Big[\tfrac{s^5}{5}\Big]_0^{L} \quad &\text{(antiderivatives and Barrow's rule)} \\
> &= \tfrac{1}{10}\,\rho\,\pi\,R^4L = \tfrac{3}{10}\,m\,R^2 \quad &\text{(substitute the mass)} \\
> \int s^2\,dm &= \rho\int_0^{L} s^2\,2\pi\Big[\tfrac{r^2}{2}\Big]_0^{Rs/L} ds = \rho\,\frac{\pi R^2}{L^2}\Big[\tfrac{s^5}{5}\Big]_0^{L} = \tfrac15\,\rho\,\pi\,R^2L^3 = \tfrac35\,m\,L^2 \quad &\text{(Eq. 10.12 with respect to the plane through $V$ normal to the axis)} \\
> \int z^2\,dm &= \rho\int_0^{L}\Big[\tfrac{r^4}{4}\Big]_0^{Rs/L}ds\int_0^{2\pi}\sin^2\theta\,d\theta \quad &\text{(Eq. 10.12: $z^2$ is $r^2\sin^2\theta$)} \\
> &= \rho\,\frac{R^4}{4L^4}\,\frac{L^5}{5}\Big[\tfrac\theta2 - \tfrac{\sin 2\theta}{4}\Big]_0^{2\pi} = \rho\,\frac{R^4L}{20}\,\pi = \tfrac{3}{20}\,m\,R^2 \quad &\text{(Barrow's rule: the bracket is $\pi$; substitute the mass)} \\
> \int y^2\,dm &= \tfrac{3}{20}\,m\,R^2 \quad &\text{(same with $\cos^2\theta$; the bracket is again $\pi$)} \\
> I_{Vy} &= \int (s^2 + z^2)\,dm = \tfrac35\,m\,L^2 + \tfrac{3}{20}\,m\,R^2 \quad &\text{(Eq. 10.11 about the axis through $V$ parallel to $y$)} \\
> I_{Gy} &= I_{Vy} - m\,(x_G^2 + z_G^2) = \tfrac35\,m\,L^2 + \tfrac{3}{20}\,m\,R^2 - m\Big(\tfrac{3L}{4}\Big)^2 \quad &\text{(Steiner: the axes are parallel, at the distance $3L/4$)} \\
> &= \Big(\tfrac{48}{80} - \tfrac{45}{80}\Big)m\,L^2 + \tfrac{12}{80}\,m\,R^2 = \tfrac{3m}{80}\,(4R^2 + L^2) \quad &\text{(common denominator 80)} \\
> I_{Gz} &= I_{Vz} - m\,(x_G^2 + y_G^2) = \tfrac{3m}{80}\,(4R^2 + L^2) \quad &\text{(same steps with $\int y^2\,dm$ in place of $\int z^2\,dm$)} \\
> P_{xy,xz} &= P_{xy,yz} = P_{xz,yz} = 0 \quad &\text{(each involves $Gxy$ or $Gxz$, which contain the axis and are planes of symmetry, Sec. 10.4)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = \frac{3m}{80}\begin{bmatrix} 8R^2 & 0 & 0 \cr 0 & 4R^2 + L^2 & 0 \cr 0 & 0 & 4R^2 + L^2 \end{bmatrix}}$$
>
> **Units:** $[\mathrm M\,\mathrm L^2]$
> **Meaning:** about its axis the cone has less inertia than a cylinder of the same mass and radius (three tenths against one half), because its mass gathers near the axis at the apex end. The transverse moment at $G$ is much smaller than at the apex: the large term in the squared height is almost cancelled by Steiner.

#### Part (g): thin disk

![[attachments/EM-SOL/rb05-g-disk.svg]]

> [!derivation] Inertia tensor of the thin disk
> **Law:** plate model with surface density; moments of inertia in polar coordinates; vanishing products
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.29; Notes.pdf, Sec. 10.4; Problems.pdf, p. 39
>
> Since the thickness is much smaller than the radius, the disk is modelled as a plate in the plane $Gxy$ with surface density $\sigma$ equal to $\rho h$; the third coordinate of its points is neglected. Polar coordinates: the abscissa is $r\cos\theta$, the ordinate $r\sin\theta$, $r$ from 0 to $R$, $\theta$ from 0 to $2\pi$, and the area element is $r\,dr\,d\theta$ (jacobian $r$, Eq. 10.29).
>
> $$\begin{aligned}
> m &= \sigma\Big[\tfrac{r^2}{2}\Big]_0^{R}\big[\theta\big]_0^{2\pi} = \sigma\,\pi\,R^2 \quad &\text{(Eq. 10.6; antiderivatives and Barrow's rule)} \\
> \int y^2\,dm &= \sigma\int_0^{R} r^3\,dr\int_0^{2\pi}\sin^2\theta\,d\theta = \sigma\,\tfrac{R^4}{4}\Big[\tfrac\theta2 - \tfrac{\sin2\theta}{4}\Big]_0^{2\pi} = \sigma\,\tfrac{\pi R^4}{4} = \tfrac14\,m\,R^2 \quad &\text{(ordinate squared times $r\,dr\,d\theta$; Barrow's rule)} \\
> \int x^2\,dm &= \sigma\,\tfrac{R^4}{4}\Big[\tfrac\theta2 + \tfrac{\sin2\theta}{4}\Big]_0^{2\pi} = \tfrac14\,m\,R^2 \quad &\text{(same with $\cos^2\theta$)} \\
> I_{Gx} &= \int (y^2 + z^2)\,dm = \tfrac14\,m\,R^2 \quad &\text{(Eq. 10.11 with the third coordinate neglected)} \\
> I_{Gy} &= \int (x^2 + z^2)\,dm = \tfrac14\,m\,R^2 \quad &\text{(Eq. 10.11)} \\
> I_{Gz} &= \int (x^2 + y^2)\,dm = \tfrac12\,m\,R^2 \quad &\text{(Eq. 10.11: sum of the two integrals)} \\
> P_{xy,xz} &= P_{xy,yz} = 0, \quad P_{xz,yz} = 0 \quad &\text{(the plate lies in $Gxy$; and $Gxz$, $Gyz$ are planes of symmetry, Sec. 10.4)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = \frac{m\,R^2}{4}\begin{bmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 2 \end{bmatrix}}$$
>
> **Units:** $[\mathrm M\,\mathrm L^{-2}][\mathrm L^4] = [\mathrm M\,\mathrm L^2]$
> **Meaning:** for a flat body the moment about the normal axis is the sum of the two in-plane moments, and the disk's rotational symmetry splits it equally between $Gx$ and $Gy$.

#### Part (h): semicircular plate

![[attachments/EM-SOL/rb05-h-half-plate.svg]]

> [!derivation] Mass and centre of mass of the semicircular plate
> **Law:** plate model; total mass and first moment in polar coordinates; the centre of mass lies on the plane of symmetry
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.7; Notes.pdf, Eq. 10.8; Notes.pdf, Eq. 10.29; Notes.pdf, Sec. 10.3; Problems.pdf, p. 39
>
> Plate of surface density $\sigma$ equal to $\rho h$ in the plane $Oxy$ of the auxiliary frame $S_O$, with $O$ at the centre of the diameter. The half disk on the side of positive $x$ (towards the arc) is described by $r$ from 0 to $R$ and the polar angle $\theta$, measured from $x$, from minus to plus half of $\pi$; abscissa $r\cos\theta$, ordinate $r\sin\theta$, area element $r\,dr\,d\theta$.
>
> $$\begin{aligned}
> m &= \sigma\Big[\tfrac{r^2}{2}\Big]_0^{R}\big[\theta\big]_{-\pi/2}^{\pi/2} = \sigma\,\tfrac{R^2}{2}\,\pi = \tfrac12\,\sigma\,\pi\,R^2 \quad &\text{(Eq. 10.6; antiderivatives and Barrow's rule)} \\
> y_G &= 0 \quad &\text{(the plane $Oxz$ is a plane of symmetry, Sec. 10.3)} \\
> m\,x_G &= \sigma\int_0^{R} r^2\,dr\int_{-\pi/2}^{\pi/2}\cos\theta\,d\theta = \sigma\Big[\tfrac{r^3}{3}\Big]_0^{R}\big[\sin\theta\big]_{-\pi/2}^{\pi/2} \quad &\text{(Eq. 10.7: abscissa $r\cos\theta$ times $r\,dr\,d\theta$)} \\
> &= \sigma\,\tfrac{R^3}{3}\,\big(1 - (-1)\big) = \tfrac23\,\sigma\,R^3 \quad &\text{(Barrow's rule, both limits)} \\
> x_G &= \frac{2\sigma R^3/3}{\sigma\pi R^2/2} = \frac{4R}{3\pi} \quad &\text{(divide by the mass)}
> \end{aligned}$$
>
> $$\boxed{m = \tfrac12\,\sigma\,\pi\,R^2, \qquad \mathbf r_O^G = \frac{4R}{3\pi}\,\mathbf i}$$
>
> **Units:** $x_G$ in $[\mathrm L]$
> **Meaning:** $G$ is on the symmetry axis at about 0.424 of the radius from the diameter, as Eq. 10.31 of the notes also finds for the half disk with other axes.

> [!derivation] Inertia tensor of the semicircular plate at O and at G
> **Law:** moments of inertia in polar coordinates; Steiner's theorem; vanishing products
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.12; Notes.pdf, Eq. 10.48; Notes.pdf, Sec. 10.4
>
> $$\begin{aligned}
> \int y^2\,dm &= \sigma\int_0^{R} r^3\,dr\int_{-\pi/2}^{\pi/2}\sin^2\theta\,d\theta = \sigma\,\tfrac{R^4}{4}\Big[\tfrac\theta2 - \tfrac{\sin2\theta}{4}\Big]_{-\pi/2}^{\pi/2} \quad &\text{(Eq. 10.12; identity for $\sin^2\theta$)} \\
> &= \sigma\,\tfrac{R^4}{4}\Big[\Big(\tfrac\pi4 - 0\Big) - \Big(-\tfrac\pi4 - 0\Big)\Big] = \sigma\,\tfrac{\pi R^4}{8} = \tfrac14\,m\,R^2 \quad &\text{(Barrow's rule: $\sin(\pm\pi)$ is zero; substitute the mass)} \\
> \int x^2\,dm &= \sigma\,\tfrac{R^4}{4}\Big[\tfrac\theta2 + \tfrac{\sin2\theta}{4}\Big]_{-\pi/2}^{\pi/2} = \sigma\,\tfrac{\pi R^4}{8} = \tfrac14\,m\,R^2 \quad &\text{(same with $\cos^2\theta$)} \\
> I_{Ox} &= \tfrac14\,m\,R^2, \quad I_{Oy} = \tfrac14\,m\,R^2, \quad I_{Oz} = \tfrac12\,m\,R^2 \quad &\text{(Eq. 10.11 with the third coordinate neglected)} \\
> I_{Gx} &= I_{Ox} - m\,(y_G^2 + z_G^2) = \tfrac14\,m\,R^2 \quad &\text{(Steiner: $Ox$ and $Gx$ are the same line)} \\
> I_{Gy} &= I_{Oy} - m\,(x_G^2 + z_G^2) = \tfrac14\,m\,R^2 - m\,\frac{16R^2}{9\pi^2} \quad &\text{(Steiner: parallel axes at the distance $x_G$)} \\
> I_{Gz} &= I_{Oz} - m\,(x_G^2 + y_G^2) = \tfrac12\,m\,R^2 - m\,\frac{16R^2}{9\pi^2} \quad &\text{(Steiner: parallel axes at the distance $x_G$)} \\
> P_{xy,xz} &= P_{xy,yz} = 0, \quad P_{xz,yz} = 0 \quad &\text{(the plate lies in $Gxy$; $Gxz$ is a plane of symmetry, Sec. 10.4)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = m\,R^2\begin{bmatrix} \tfrac14 & 0 & 0 \cr 0 & \tfrac14 - \tfrac{16}{9\pi^2} & 0 \cr 0 & 0 & \tfrac12 - \tfrac{16}{9\pi^2} \end{bmatrix} \approx m\,R^2\begin{bmatrix} 0.2500 & 0 & 0 \cr 0 & 0.0699 & 0 \cr 0 & 0 & 0.3199 \end{bmatrix}}$$
>
> **Units:** $[\mathrm M\,\mathrm L^2]$
> **Meaning:** at the centre of the diameter each moment equals that of the full disk per unit mass (the missing half is a mirror image). At $G$ only the axes parallel to the diameter and normal to the plate shrink, because $G$ moved along $x$.

#### Part (i): semicircular wire arc

![[attachments/EM-SOL/rb05-i-wire.svg]]

> [!derivation] Mass and centre of mass of the semicircular wire
> **Law:** line density; total mass and first moment with the arc parametrised by its angle
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.7; Notes.pdf, Eq. 10.17; Notes.pdf, Sec. 10.3; Problems.pdf, p. 39
>
> The cross-section is negligible, so the wire is a line of density $\lambda$ equal to $\rho A$. In the auxiliary frame $S_O$ at the centre of the circle, its points are $R\cos\theta$, $R\sin\theta$, 0 with $\theta$ from 0 to $\pi$ (from the end on the positive $x$ side, through the top of the arc on the $y$ axis, to the other end). The arc length element is $R\,d\theta$ (radius times the angle), so the mass element is $\lambda R\,d\theta$.
>
> $$\begin{aligned}
> m &= \int_0^{\pi}\lambda\,R\,d\theta = \lambda\,R\big[\theta\big]_0^{\pi} = \pi\,\lambda\,R \quad &\text{(Eq. 10.6; Barrow's rule)} \\
> x_G &= 0 \quad &\text{(the plane $Oyz$ is a plane of symmetry, Sec. 10.3)} \\
> m\,y_G &= \lambda\,R^2\int_0^{\pi}\sin\theta\,d\theta = \lambda\,R^2\big[-\cos\theta\big]_0^{\pi} \quad &\text{(Eq. 10.7: ordinate $R\sin\theta$ times $\lambda R\,d\theta$)} \\
> &= \lambda\,R^2\big(1 - (-1)\big) = 2\,\lambda\,R^2 \quad &\text{(Barrow's rule: $-\cos\pi = 1$, $-\cos 0 = -1$)} \\
> y_G &= \frac{2\lambda R^2}{\pi\lambda R} = \frac{2R}{\pi} \quad &\text{(divide by the mass)}
> \end{aligned}$$
>
> $$\boxed{m = \pi\,\lambda\,R, \qquad \mathbf r_O^G = \frac{2R}{\pi}\,\mathbf j}$$
>
> **Units:** $y_G$ in $[\mathrm L]$
> **Meaning:** $G$ is on the symmetry axis at about 0.637 of the radius from the centre, off the wire, between the diameter and the arc.

> [!derivation] Inertia tensor of the semicircular wire at O and at G
> **Law:** moments of inertia along the arc; Steiner's theorem; vanishing products
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.12; Notes.pdf, Eq. 10.48; Notes.pdf, Sec. 10.4
>
> $$\begin{aligned}
> \int x^2\,dm &= \lambda\,R^3\int_0^{\pi}\cos^2\theta\,d\theta = \lambda\,R^3\Big[\tfrac\theta2 + \tfrac{\sin2\theta}{4}\Big]_0^{\pi} = \tfrac{\pi}{2}\,\lambda\,R^3 = \tfrac12\,m\,R^2 \quad &\text{(Eq. 10.12; identity for $\cos^2\theta$, Barrow's rule)} \\
> \int y^2\,dm &= \lambda\,R^3\Big[\tfrac\theta2 - \tfrac{\sin2\theta}{4}\Big]_0^{\pi} = \tfrac{\pi}{2}\,\lambda\,R^3 = \tfrac12\,m\,R^2 \quad &\text{(same with $\sin^2\theta$)} \\
> \int z^2\,dm &= 0 \quad &\text{(the wire lies in the plane $Oxy$)} \\
> I_{Ox} &= \tfrac12\,m\,R^2, \quad I_{Oy} = \tfrac12\,m\,R^2, \quad I_{Oz} = m\,R^2 \quad &\text{(Eq. 10.11: sums of two of the integrals above)} \\
> I_{Gx} &= I_{Ox} - m\,(y_G^2 + z_G^2) = \tfrac12\,m\,R^2 - m\,\frac{4R^2}{\pi^2} \quad &\text{(Steiner: parallel axes at the distance $y_G$)} \\
> I_{Gy} &= I_{Oy} - m\,(x_G^2 + z_G^2) = \tfrac12\,m\,R^2 \quad &\text{(Steiner: $Oy$ and $Gy$ are the same line)} \\
> I_{Gz} &= I_{Oz} - m\,(x_G^2 + y_G^2) = m\,R^2 - m\,\frac{4R^2}{\pi^2} \quad &\text{(Steiner: parallel axes at the distance $y_G$)} \\
> P_{xy,xz} &= 0, \quad P_{xy,yz} = P_{xz,yz} = 0 \quad &\text{(the wire lies in $Gxy$; $Gyz$ is a plane of symmetry, Sec. 10.4)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = m\,R^2\begin{bmatrix} \tfrac12 - \tfrac{4}{\pi^2} & 0 & 0 \cr 0 & \tfrac12 & 0 \cr 0 & 0 & 1 - \tfrac{4}{\pi^2} \end{bmatrix} \approx m\,R^2\begin{bmatrix} 0.0947 & 0 & 0 \cr 0 & 0.5 & 0 \cr 0 & 0 & 0.5947 \end{bmatrix}}$$
>
> **Units:** $[\mathrm M\,\mathrm L^2]$
> **Meaning:** at the centre of the circle every point of the wire is at the distance $R$ from the normal axis, which gives the full moment of a point mass at that distance; at $G$ the axes normal to the symmetry line lose the Steiner term.

#### Part (j): flat sheet, at a vertex and at the centre of mass

![[attachments/EM-SOL/rb05-j-sheet.svg]]

> [!derivation] Inertia tensor of the flat sheet at the vertex A
> **Law:** plate model; moments and products of inertia in Cartesian coordinates
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.15; Notes.pdf, Eq. 10.38; Problems.pdf, p. 38
>
> The statement has no figure for this part: the frame $S_A$ is chosen with origin at the vertex $A$, $x$ along the edge of length $L$, $y$ along the edge of width $w$ and $z$ normal to the sheet, which occupies the rectangle with $x$ from 0 to $L$ and $y$ from 0 to $w$. Area element $dx\,dy$, surface density $\sigma$, third coordinate zero.
>
> $$\begin{aligned}
> m &= \sigma\big[x\big]_0^{L}\big[y\big]_0^{w} = \sigma\,L\,w \quad &\text{(Eq. 10.6; Barrow's rule)} \\
> \int x^2\,dm &= \sigma\Big[\tfrac{x^3}{3}\Big]_0^{L}\big[y\big]_0^{w} = \sigma\,\tfrac{L^3}{3}\,w = \tfrac13\,m\,L^2 \quad &\text{(antiderivatives and Barrow's rule; substitute the mass)} \\
> \int y^2\,dm &= \sigma\,L\Big[\tfrac{y^3}{3}\Big]_0^{w} = \tfrac13\,m\,w^2 \quad &\text{(same steps)} \\
> P^A_{xz,yz} &= \int x\,y\,dm = \sigma\Big[\tfrac{x^2}{2}\Big]_0^{L}\Big[\tfrac{y^2}{2}\Big]_0^{w} = \sigma\,\tfrac{L^2w^2}{4} = \tfrac14\,m\,L\,w \quad &\text{(Eq. 10.15; constant limits split the integral)} \\
> P^A_{xy,xz} &= P^A_{xy,yz} = 0 \quad &\text{(Eq. 10.15: the integrands contain the zero third coordinate)} \\
> I_{Ax} &= \tfrac13\,m\,w^2, \quad I_{Ay} = \tfrac13\,m\,L^2, \quad I_{Az} = \tfrac13\,m\,(L^2 + w^2) \quad &\text{(Eq. 10.11)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_A = m\begin{bmatrix} \tfrac{w^2}{3} & -\tfrac{Lw}{4} & 0 \cr -\tfrac{Lw}{4} & \tfrac{L^2}{3} & 0 \cr 0 & 0 & \tfrac{L^2 + w^2}{3} \end{bmatrix}}$$
>
> **Units:** $[\mathrm M\,\mathrm L^2]$
> **Meaning:** at the vertex the sheet lies entirely in the first quadrant, so the product $P_{xz,yz}$ is positive and the axes along the edges are not principal axes (Eq. 10.38 puts minus the product off the diagonal).

> [!derivation] Inertia tensor of the flat sheet at G by Steiner's theorem
> **Law:** centre of mass on the planes of symmetry; Steiner's theorem in components
> **Source:** Notes.pdf, Eq. 10.7; Notes.pdf, Eq. 10.48; Notes.pdf, Sec. 10.3; Notes.pdf, Sec. 10.4
>
> $$\begin{aligned}
> m\,x_G &= \sigma\Big[\tfrac{x^2}{2}\Big]_0^{L}\big[y\big]_0^{w} = \sigma\,\tfrac{L^2}{2}\,w \quad &\text{(Eq. 10.7; Barrow's rule)} \\
> x_G &= \frac L2, \qquad y_G = \frac w2, \qquad z_G = 0 \quad &\text{(divide by the mass; same steps for $y_G$; the sheet lies in $Axy$)} \\
> (\mathbf r_A^G)^2\,U - \mathbf r_A^G\otimes\mathbf r_A^G &= \begin{bmatrix} \tfrac{w^2}{4} & -\tfrac{Lw}{4} & 0 \cr -\tfrac{Lw}{4} & \tfrac{L^2}{4} & 0 \cr 0 & 0 & \tfrac{L^2 + w^2}{4} \end{bmatrix} \quad &\text{(Steiner matrix of the previous section with the coordinates of $G$)} \\
> \bar{\bar I}_G &= \bar{\bar I}_A - m\left[(\mathbf r_A^G)^2\,U - \mathbf r_A^G\otimes\mathbf r_A^G\right] \quad &\text{(Eq. 10.48 solved for the central tensor)} \\
> I_{Gx} &= \tfrac13\,m\,w^2 - \tfrac14\,m\,w^2 = \tfrac{1}{12}\,m\,w^2 \quad &\text{(element 11)} \\
> I_{Gy} &= \tfrac13\,m\,L^2 - \tfrac14\,m\,L^2 = \tfrac{1}{12}\,m\,L^2 \quad &\text{(element 22)} \\
> I_{Gz} &= \tfrac13\,m\,(L^2 + w^2) - \tfrac14\,m\,(L^2 + w^2) = \tfrac{1}{12}\,m\,(L^2 + w^2) \quad &\text{(element 33)} \\
> -P^G_{xz,yz} &= -\tfrac14\,m\,L\,w - \Big(-\tfrac14\,m\,L\,w\Big) = 0 \quad &\text{(element 12: the product at the vertex is exactly the Steiner term)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = \frac{m}{12}\begin{bmatrix} w^2 & 0 & 0 \cr 0 & L^2 & 0 \cr 0 & 0 & L^2 + w^2 \end{bmatrix}}$$
>
> **Units:** $[\mathrm M\,\mathrm L^2]$
> **Meaning:** the product of inertia vanishes at $G$ as it must, because the planes $Gxz$ and $Gyz$ are planes of symmetry of the sheet (Sec. 10.4); this confirms both tensors. Each central moment is a quarter of the one at the vertex.

### Linear Momentum, Angular Momentum and Kinetic Energy

This section does not apply: the bodies are not moving, and only their mass geometry is asked.

### Free-Body Diagram and Equations of Motion

This section does not apply: no force acts in the statement and no equation of motion is written.

### Answers and Checks

| Part | Body | $\bar{\bar I}_G$ in the axes of the figure (diagonal; all products zero unless stated) |
| :--- | :--- | :--- |
| (a) | slender bar | $\frac{mL^2}{12}\,\mathrm{diag}(0, 1, 1)$ |
| (b) | cylinder | $\frac{m}{12}\,\mathrm{diag}(3R^2+L^2,\ 3R^2+L^2,\ 6R^2)$ |
| (c) | parallelepiped | $\frac{m}{12}\,\mathrm{diag}(b^2+c^2,\ a^2+c^2,\ a^2+b^2)$ |
| (d) | sphere | $\frac{2mR^2}{5}\,\mathrm{diag}(1, 1, 1)$ |
| (e) | hemisphere | $mR^2\,\mathrm{diag}(\frac25-\frac{9}{64},\ \frac25-\frac{9}{64},\ \frac25)$, that is $\frac{83}{320}$, $\frac{83}{320}$, $\frac25$; $G$ at $3R/8$ from the flat face |
| (f) | cone | $\frac{3m}{80}\,\mathrm{diag}(8R^2,\ 4R^2+L^2,\ 4R^2+L^2)$; $G$ at $3L/4$ from the apex |
| (g) | thin disk | $\frac{mR^2}{4}\,\mathrm{diag}(1, 1, 2)$ |
| (h) | semicircular plate | $mR^2\,\mathrm{diag}(\frac14,\ \frac14-\frac{16}{9\pi^2},\ \frac12-\frac{16}{9\pi^2})$; $G$ at $4R/(3\pi)$ from the diameter |
| (i) | semicircular wire | $mR^2\,\mathrm{diag}(\frac12-\frac{4}{\pi^2},\ \frac12,\ 1-\frac{4}{\pi^2})$; $G$ at $2R/\pi$ from the centre |
| (j) | flat sheet | at $A$: moments $\frac{mw^2}{3}$, $\frac{mL^2}{3}$, $\frac{m(L^2+w^2)}{3}$ and $P_{xz,yz} = \frac{mLw}{4}$; at $G$: $\frac{m}{12}\,\mathrm{diag}(w^2,\ L^2,\ L^2+w^2)$ |

**Check against the official key:** the key (Problems.pdf, pp. 77-78) prints parts (a) to (g), in the axes of the statement figures used here. It gives the slender bar with zero moment about its axis and one twelfth of the mass times the squared length about the other two, the cylinder with the third diagonal element 6R² over 12, the parallelepiped with b² + c², a² + c² and a² + b², the sphere with two fifths, the hemisphere with two fifths minus nine sixty-fourths on the two transverse axes and two fifths on the axis, the cone with 3m/80 times 8R², 4R² + L² and 4R² + L², and the thin disk with one quarter, one quarter and one half of the mass times the squared radius; all products are zero. All seven tensors coincide with the results above. The key prints nothing for (h), (i) and (j), which are checked below.

**Limiting cases and consistency:**

> [!derivation] Check: flat bodies, mirror halves and a thin cylinder
> **Law:** Eq. 10.13 for a plate with zero thickness; the results above in limiting cases
> **Source:** Notes.pdf, Eq. 10.13; Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.21
>
> $$\begin{aligned}
> I_{Gz} &= I_{Gx} + I_{Gy} \quad &\text{(flat body in the plane $Gxy$: $x^2 + y^2$ is the sum of the two integrands of Eq. 10.11)} \\
> \text{(g)}: \ \tfrac12 &= \tfrac14 + \tfrac14 \quad &\text{(holds)} \\
> \text{(h)}: \ \tfrac12 - \tfrac{16}{9\pi^2} &= \tfrac14 + \Big(\tfrac14 - \tfrac{16}{9\pi^2}\Big) \quad &\text{(holds)} \\
> \text{(i)}: \ 1 - \tfrac{4}{\pi^2} &= \Big(\tfrac12 - \tfrac{4}{\pi^2}\Big) + \tfrac12 \quad &\text{(holds; the wire is also flat)} \\
> \text{(j)}: \ \tfrac{L^2 + w^2}{12} &= \tfrac{w^2}{12} + \tfrac{L^2}{12} \quad &\text{(holds at $G$, and with thirds at $A$)} \\
> \text{(b) with } L \to h \ll R: \ \tfrac{m}{12}\,(3R^2 + h^2) &\to \tfrac14\,m\,R^2 \quad &\text{(the thick disk tends to the plate of part (g))} \\
> \text{(e) at } O: \ 2\cdot\tfrac25\,\tfrac m2\,R^2 &= \tfrac25\,m\,R^2 \quad &\text{(two hemispheres of mass $m/2$ make the sphere of part (d))} \\
> \text{(h) at } O: \ 2\cdot\tfrac14\,\tfrac m2\,R^2 &= \tfrac14\,m\,R^2 \quad &\text{(two half plates make the disk of part (g))} \\
> \text{(i) at } O: \ I_{Ox} &= \tfrac12\,m\,R^2 \quad &\text{(same value as Eq. 10.21 of the notes for this wire)}
> \end{aligned}$$
>
> $$\boxed{\text{every flat body satisfies } I_{Gz} = I_{Gx} + I_{Gy}, \text{ and every half body matches its whole body at the centre}}$$
>
> **Units:** dimensionless coefficients of $m\,R^2$ or $m\,L^2$
> **Meaning:** the moments of the half bodies (e), (h) and (i) about axes through the centre of the full body are those of the full body per unit mass, which checks the integrals before Steiner; the perpendicular-axis relation checks the plates and the wire after Steiner.

* **Positive moments after Steiner.** The smallest central coefficients, 0.0699 for the semicircular plate and 0.0947 for the wire, are positive, as every moment of inertia must be (Sec. 10.4); a wrong distance in Steiner would easily make them negative.
* **Triangle inequality.** In every tensor each moment is not larger than the sum of the other two, with equality only for the flat bodies and the slender bar.
* **Dimensions.** Every element is a mass times a squared length, kg·m².
