---
title: "Problems - Topic 1: Fundamentals and Particle Kinematics"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/03-engineering-mechanics/problemas/Problems.pdf"
type: "Verbatim Problem Statements"
language: "English"
---

# 📝 Topic 1: Fundamentals and Particle Kinematics - Problem Statements

Official problem statements from the UC3M Aerospace Engineering problem collection (`Problems.pdf`, Chapter 1). These problems test kinematics in Cartesian, Cylindrical, and Frenet-Serret intrinsic bases, curvature, and relative motion between points.

> [!NOTE]
> **Status:** Verbatim problem statements transcribed faithfully from official department exams and problem sets.
> 
> [!SUCCESS] Complete Analytical Solutions Ready
> All 10 problems have full, step-by-step pedagogical solutions developed in: [[Solutions - Topic 1 Particle Kinematics]].

---

## 📌 Problem 01: Rocket Helical Trajectory (MIT OCW)

An out-of-control rocket traces an upward helical trajectory described in Cartesian coordinates for $t \ge 0$ by:
$$ x = a \cos(\omega t) \tag{1} $$
$$ y = a \sin(\omega t) \tag{2} $$
$$ z = v_z t \tag{3} $$
where $a$, $v_z$, and $\omega$ are constants.

* **(a)** Express the position, velocity, and acceleration vectors in the Cartesian $x, y, z$ system using unit vectors $\mathbf{i}, \mathbf{j}, \mathbf{k}$.
* **(b)** Express the position, velocity, and acceleration vectors in the cylindrical coordinate system using unit vectors $\mathbf{e}_R, \mathbf{e}_\theta, \mathbf{e}_z$.
* **(c)** Express the velocity and acceleration vectors using $s, \rho$ and the vector basis $\mathbf{e}_t, \mathbf{e}_n, \mathbf{e}_b$.
* **(d)** Compute the modulus of the velocity vector.
* **(e)** Express the evolution of the arc-length coordinate as a function of time.
* **(f)** Write down the trajectory as a function of the arc-length coordinate.
* **(g)** Where is the center of curvature for this curve when the particle is located at $(x, y, z) = (a, 0, 0)$?

*(Taken from MIT OCW)*

---

## 📌 Problem 02: Kinematics, Spiral

A planar spiral is given by the equation $r = \alpha e^{\beta\theta}$, where $\alpha$ and $\beta$ are constants, $r$ is the radial coordinate, and $\theta$ is the angular coordinate. If a particle moves along the spiral according to the equation $\theta = \delta t^n$ (where $\delta$ is a constant), determine:

* **(a)** The radial and transverse components of the velocity.
* **(b)** The radial and transverse components of the acceleration.
* **(c)** The tangential and normal components of the velocity.
* **(d)** The tangential and normal components of the acceleration.
* **(e)** The radius of curvature of the spiral.

---

## 📌 Problem 03: Kinematics, Astroid

A point particle describes the astroid:
$$ x = a \cos^3\phi $$
$$ y = a \sin^3\phi $$
with a motion whose tangential acceleration is constant, $a_t = k$. If the point is initially at rest at $\phi = 0$, compute the evolution of the position as a function of time while the particle is in one of the smooth segments of the astroid.

*(Hint: $ds = \sqrt{dx^2 + dy^2}$)*.

---

## 📌 Problem 04: Plane at Constant Altitude

An aircraft moves at constant altitude $y_0$ with velocity $v_0$ in the $x$ direction. At time $t = 0$ it is located at $x = 0$, and it begins to accelerate in the $x$ direction at a constant rate $a_x$. Describe the position, velocity, and acceleration in polar coordinates $r, \theta$, and answer the following questions:

* **(a)** Show that: $\dot{r} = \frac{v(t) x(t)}{r(t)}$
* **(b)** Show that: $\dot{\theta} = -\frac{v(t) y_0}{r^2(t)}$
* **(c)** Show that: $\ddot{r} = \frac{v^2(t) y_0^2 + a_x x(t) r^2(t)}{r^3(t)}$
* **(d)** Show that: $\ddot{\theta} = y_0 \frac{2v^2(t) x(t) - a_x r^2(t)}{r^4(t)}$

From these expressions form the acceleration vector $\mathbf{a} = a_r\mathbf{e}_r + a_\theta\mathbf{e}_\theta$. Repeat the problem using Cartesian coordinates.

---

## 📌 Problem 05: Plane and Glider

An airplane $A$ is flying horizontally with a constant speed $v_A$, and is towing a glider $B$. The glider is gaining altitude. The tow cable has a length $r$, and the angle $\theta$ formed between the tow cable and the horizontal is increasing at a constant rate of $\dot{\theta}$. We want to determine the magnitude of the velocity, $v_B$, and the acceleration, $a_B$, of the glider as a function of $\theta$ and its derivatives.

---

## 📌 Problem 06: Particle on Sinusoidal Curve

A point particle $P$ travels along a curve given by:
$$ y = \sin x $$
with a velocity along $x$ given by $\dot{x} = 1$.

* **(a)** Find the intrinsic, unitary vector basis associated to the curve.
* **(b)** Express $x$ as a function of an arc length parameter, $s$. You can leave your solution as a function of an integral.
* **(c)** Find the tangent and normal acceleration components of $P$ as a function of $x$.
* **(d)** Write the radius of curvature of the trajectory as a function of $x$.

---

## 📌 Problem 07: Skater Pulled by Vehicle on a Circumference

A skater $B$ is being towed by a vehicle $A$ on a perfectly smooth horizontal plane, where we define an inertial reference frame $Oxy$. The vehicle is moving along a circumference of radius $a$ and center at $O$ with constant angular velocity $\omega$. The skater is attached to the vehicle by a bar without mass and constant length $l = a$. Initially, the vehicle is located at $(a, 0)$ and the skater is at rest at $(2a, 0)$. Defining a rotating reference frame $Ox_1y_1$ with origin at $O$ and axis $Ox_1$ along $OA$, and calling $\psi$ the angle between the axis $Ox_1$ and the bar $AB$, determine:

* **(a)** The relative acceleration of the skater with respect to $Ox_1y_1$ as a function of $\psi$ and its time derivatives.
* **(b)** The centripetal and Coriolis acceleration terms also as a function of $\psi$ and its time derivatives.
* **(c)** Reduce the evolution of $\psi$ to integrals of the form $\int [...] d\psi = \int [...] dt$ (consider that $\dot{\psi}^2 = \int 2\dot{\psi}\ddot{\psi}\,dt$).
* **(d)** Determine the tension on the bar.
* **(e)** If the rigid bar is substituted by a string which cannot bear compression, determine if/when the string will become loose.

---

## 📌 Problem 08: Kinematics, Two Trains on Tracks

Two trains, $A$ and $B$, are moving along parallel tracks. The separation between the tracks is $a$. The absolute velocity of each train is $v_A$ and $v_B$, respectively. What is the relative velocity of each train with respect to the other?

Solve the same problem considering that train $B$ is now moving along a circular track of radius $R$. The minimum distance between the circular track and the straight track of $A$ is $a$.

---

## 📌 Problem 09: 2001: A Space Odyssey (Artificial Gravity)

In *2001: A Space Odyssey* an idea to obtain artificial gravity in a spaceship was presented. It consists of a cylinder rotating at constant angular velocity around its axis. The astronauts would live in the inner surface of the cylinder and the centrifugal force would act as artificial gravity.

* **(a)** If the cylinder has radius $R$, determine the angular velocity $\omega$ required to obtain a given level of artificial gravity $g$. Consider $R = 10\text{ m}$ and $g = 9.81\text{ m/s}^2$ for a particular case.
* **(b)** An astronaut runs inside the surface of the cylinder with a constant speed $u$ with respect to the cylinder. Determine the artificial gravity that she feels (neglect the height of the astronaut $h$ with respect to the radius of the cylinder $R$, $h \ll R$).
* **(c)** What is the condition for her to feel no artificial gravity at all?

---

## 📌 Problem 41: Simple Rotations, Satellite Solar Panels

The angle $\theta$ describing the rotation of the solar panels of a reconnaissance satellite about the body-fixed axis $x$ is an arbitrary function of time. The satellite spins about the $z$ axis at the constant angular rate $\omega$. Derive expressions for the absolute velocity and acceleration of point $B$ relative to an inertial reference frame centered in $A$.

*(Taken from Ginsberg, "Engineering Dynamics", Cambridge University Press, 2008)*
