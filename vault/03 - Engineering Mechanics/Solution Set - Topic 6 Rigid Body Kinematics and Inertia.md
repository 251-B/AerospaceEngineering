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
