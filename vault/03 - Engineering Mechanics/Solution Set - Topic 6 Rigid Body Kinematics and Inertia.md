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
