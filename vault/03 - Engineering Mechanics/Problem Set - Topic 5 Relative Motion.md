---
title: "Problem Set - Topic 5: Relative Motion"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Problem Statements"
language: "English"
tags:
  - problems
  - topic-5
  - relative-motion
---

# 📝 Topic 5: Relative Motion - Problem Statements

Problem statements from the UC3M Aerospace Engineering problem collection (`Problems.pdf`, "Particle exercises and problems") that require a moving reference frame: relative kinematics (Coriolis theorem, Notes Eq. 3.27) or dynamics in a non-inertial frame with inertia forces (Notes Eq. 4.63). Problems 7, 9, 41 (Topic 1), 21 (Topic 2) and 20, 26 (Topic 3) were already worked in earlier topics with other tools; here they are solved again with the method of this topic.

> [!NOTE]
> **Status:** The statements below follow `Problems.pdf` (version 2026). Worked solutions: [[Solution Set - Topic 5 Relative Motion]]. Theory: [[Topic 5 - Relative Motion]].

| Problem | Problems.pdf page | Key page | Topic of the problem |
| :---: | :---: | :---: | :--- |
| 7 | 8 | 72 | Skater Towed by a Vehicle on a Circumference (Rotating Frame) |
| 9 | 8 | none | Artificial Gravity in a Rotating Cylinder (2001: A Space Odyssey) |
| 20 | 10 | none | Heavy Particle on a Rotating Circumference |
| 21 | 10 | none | Apparent Weight on a Spinning Planet |
| 25 | 13 | 72-73 | Ijon Tichy's Space Walk |
| 26 | 14 | none | Heavy Particle on a Rotating Half-Circumference (Moving-Frame Method) |
| 27 | 15 | 73 | Bead on a Rotating Sine-Shaped Wire with a Spring |
| 28 | 16 | none | Spherical Pendulum with a Vertically Oscillating Suspension Point |
| 30 | 18 | none | Particle on a Rotating Quarter Circumference with a Spring |
| 33 | 21 | 74 | Two Repelling Particles on a Rotating Parabola |
| 34 | 22 | 74 | Particle on a Circular Wire in an Oscillating Vertical Plane |
| 36 | 24 | 74 | Pendulum String Dragged by a Rotating Bar |
| 37 | 25 | 74 | Particle on a Spinning Elliptic Cone |
| 40 | 28 | 75 | Spring-Coupled Particles on a Vertical Axis and a Revolving Ring |
| 41 | 29 | 75 | Satellite Solar Panel (Composition of Rotations) |
| 47 | 32 | 75 | Two Repelling Particles on Concentric Wires in a Rotating Plane |
| 49 | 34 | none | Particle on a Rotating Sphere Attracted to a Point |
| 51 | 36 | none | Particle inside a Hollow Sphere in a Rotating Frame |

---

## 📌 Problem 07: Skater Towed by a Vehicle on a Circumference (Rotating Frame)

A skater $B$ is being towed by a vehicle $A$ on a perfectly smooth horizontal plane, where we define an inertial reference frame $Oxy$. The vehicle is moving along a circumference of radius $a$ and center at $O$ with constant angular velocity $\omega$. The skater is attached to the vehicle by a bar without mass and constant length $l = a$. Initially, the vehicle is located at $(a, 0)$ and the skater is at rest at $(2a, 0)$. Defining a rotating reference frame $Ox_1y_1$ with origin at $O$ and axis $Ox_1$ along $OA$, and calling $\psi$ the angle between the axis $Ox_1$ and the bar $AB$, determine:

![[attachments/EM/T5-P07-figure.png]]
*Figure: Inertial axes Oxy, rotating axes Ox1y1 turned by ωt, vehicle A on the circle of radius a, bar AB at angle ψ from Ox1, skater B Source: Problems.pdf, p. 8.*

* **(a)** The relative acceleration of the skater with respect to $Ox_1y_1$ as a function of $\psi$ and its time derivatives.
* **(b)** The centripetal and Coriolis acceleration terms also as a function of $\psi$ and its time derivatives.
* **(c)** Reduce the evolution of $\psi$ to integrals of the form $\int [\ldots]\,d\psi = \int [\ldots]\,dt$ (consider that $\dot{\psi}^2 = \int 2\dot{\psi}\ddot{\psi}\,dt$).
* **(d)** Determine the tension on the bar.
* **(e)** If the rigid bar is substituted by a string which cannot bear compression, determine if/when the string will become loose.

---

## 📌 Problem 08: Kinematics, Two Trains on Tracks

Two trains, $A$ and $B$, are moving along parallel tracks. The separation between the tracks is $a$. The absolute velocity of each train is $v_A$ and $v_B$, respectively. What is the relative velocity of each train with respect to the other?

Solve the same problem considering that train $B$ is now moving along a circular track of radius $R$. The minimum distance between the circular track and the straight track of $A$ is $a$.

---

## 📌 Problem 09: Artificial Gravity in a Rotating Cylinder (2001: A Space Odyssey)

In "2001: A Space Odyssey" an idea to obtain artificial gravity in a spaceship was presented. It consists of a cylinder rotating at constant angular velocity around its axis. The astronauts would live in the inner surface of the cylinder and the centrifugal force would act as artificial gravity.

* **(a)** If the cylinder has radius $R$, determine the angular velocity $\omega$ required to obtain a given level of artificial gravity $g$. Consider $R = 10$ m and $g = 9.81$ m/s$^2$ for a particular case.
* **(b)** An astronaut runs inside the surface of the cylinder with a constant speed $u$ with respect to the cylinder. Determine the artificial gravity that she feels (neglect the height of the astronaut $h$ with respect to the radius of the cylinder $R$, $h \ll R$).
* **(c)** What is the condition for her to feel no artificial gravity at all?

---

## 📌 Problem 20: Heavy Particle on a Rotating Circumference

A heavy particle is moving along a smooth circumference of radius $R$ and center $O$. One of the diameters of the circumference is along the local vertical, and the circumference is rotating with constant angular velocity $\omega$ about it. The position of the particle with respect to the circumference is described by the angle $\theta$ between the particle and the lowest point of the circumference.

* **(a)** Discuss the conservation of mechanical energy in the moving reference frame and compute its value.
* **(b)** Compute the reaction of the circumference in the direction normal to its plane, as a function of $\theta$.

---

## 📌 Problem 21: Apparent Weight on a Spinning Planet

On a spinning spherical planet of radius $R$ and gravitational acceleration $g_p$, the bodies weigh twice as much on the poles as on the equator. Determine the duration of the day on that planet.

---

## 📌 Problem 22: Particle on a Curve

A heavy point particle $P$ of mass $m$ is constrained to move without friction along the curve:

$$ y = a\left(1 - \cos\frac{x}{a}\right) \tag{4} $$

in the range $-\pi a \le x \le \pi a$, where $a$ is a positive constant. Initially, the particle is located at $x = 0$ with velocity $v_0$ along the positive $x$ axis.

![[attachments/EM/T5-P22-figure.png]]
*Figure: Heavy particle m on the curve y = a(1 - cos(x/a)) between x = -pi a and x = pi a, gravity g downward Source: Problems.pdf, p. 10.*

* **(a)** Reduce the problem to integrals.
* **(b)** If $v_0 = \sqrt{ga}$, determine the minimum and maximum value of $x$ along the motion.
* **(c)** What should be the minimum value of $v_0$ in order to reach $x = \pi a$?

**Extended Section (Moving Reference Frame):**<br> Let's assume now that the curve containing the point particle rotates around the $OY$ axis with constant angular velocity $\boldsymbol{\omega} = \Omega\mathbf{j}$.

* **(d)** Define a convenient moving reference frame with origin in $O$, $OX_1Y_1Z_1$. Determine the inertia force that acts on the particle in this moving reference frame as a function of $m, \Omega, x_1$ and $\dot{x}_1$, where $x_1$ represents the position coordinate of $P$ along $OX_1$.
* **(e)** Reduce the problem to quadratures and determine the value of the reaction force.
* **(f)** Find out a transcendental equation whose solutions are the equilibrium positions of the point particle in $OX_1Y_1Z_1$.
* **(g)** If $\Omega$ were a function of time, would it be possible to use the energy equation in the same way as before? Justify your answer.

---

## 📌 Problem 25: Ijon Tichy's Space Walk

A spacecraft $S$ is orbiting a celestial body $F$. The trajectory of the spacecraft with respect to an inertial reference frame $Fxy$ is given by

$$ r = \frac{p}{1 + e\cos\nu}, $$

where $p$ and $e$ are known constants and $\nu(t)$ is a known function of time. The space explorer Ijon Tichy needs to perform some extra-vehicular activities during his Seventh Voyage (from *The Star Diaries* by Stanislaw Lem). He attaches himself with a massless cord of length $L$ to the spacecraft and goes for a space walk. The cord remains in tension at all times. The astronaut is very light compared to the spacecraft, so his motion does not perturb the motion of the spacecraft. Furthermore, we assume that we can consider him as a point particle of mass $m$. We define a moving reference frame $Sx_1y_1$ as depicted in the figure.

![[attachments/EM/T5-P25-figure.png]]
*Figure: Spacecraft S on its orbit around F, true anomaly ν, moving axes Sx1 (radial) and Sy1, astronaut on a cord of length L at angle θ from Sx1 Source: Problems.pdf, p. 13.*

* **(a)** Determine the acceleration of the spacecraft with respect to $Fxy$ as a function of time.
* **(b)** Determine the tangent vector to the trajectory of $S$ as a function of time.
* **(c)** Determine the relative velocity and relative acceleration of Ijon Tichy with respect to $Sx_1y_1$ as a function of $\theta$ and its time derivatives.
* **(d)** Determine the fictitious forces acting on Ijon Tichy if we analyze the problem with respect to the frame $Sx_1y_1$.

The length $L$ is very small compared to the distance between $F$ and $S$. This allows us to take an approximation: in the following, assume that the gravitational acceleration on the astronaut and on the spacecraft are exactly the same vector (magnitude and direction) as a function of time. (In actual problems the small differences in gravity at the position of the astronaut and the spacecraft can give rise to small but important effects, and this approximation is usually not taken for that reason.)

* **(e)** Write down one ordinary differential equation that once solved (with given initial conditions) would yield the angle $\theta$ as a function of time (you do not need to solve it).
* **(f)** Assuming that you solved the previous equation, and therefore knew $\theta(t)$, determine the value of the tension on the cord as a function of time.

---

## 📌 Problem 26: Heavy Particle on a Rotating Half-Circumference (Moving-Frame Method)

A heavy point particle $P$ of mass $m$ is constrained to move without friction along the half-circumference wire of radius $a$ shown in the figure. The wire containing the point particle rotates around the $OY$ axis with constant angular velocity $\boldsymbol{\omega} = \Omega\mathbf{j}$. Initially, the particle is located at $x = 0$ with velocity $v_0$ along the positive $x$ axis.

![[attachments/EM/T5-P26-figure.png]]
*Figure: Half-circumference wire of radius a with lowest point O, ends at x = ±a, rotating about the vertical axis OY; particle of mass m on the wire Source: Problems.pdf, p. 14.*

* **(a)** Determine the number of degrees of freedom of the problem.
* **(b)** Define a convenient moving reference frame with origin in $O$, $OX_1Y_1Z_1$. Express the inertia force that acts on the particle in this moving reference frame.
* **(c)** Express also the components of the weight of the particle with respect to $OX_1Y_1Z_1$.
* **(d)** Determine if there are any equilibrium points.
* **(e)** Reduce the problem to integrals (i.e. quadratures) and determine the value of the reaction force.
* **(f)** Is it possible to use the energy equation? If $\Omega$ were a function of time, would it be possible to use the energy equation? Justify your answer.

---

## 📌 Problem 27: Bead on a Rotating Sine-Shaped Wire with a Spring

A heavy bead $P$ of mass $m$ slides without friction along a thin wire with shape given by the following equation:

$$ y_1(x_1) = \sin x_1. $$

Moreover, the bead is joined to a straight rail located at $y_1 = 2$ by a spring of stiffness $k$. The connection of the spring with the rail can move freely along the rail, so that the spring is always vertical. The whole setup rotates with respect to the $y_1$ axis with a constant angular velocity $\omega$. A sketch of the setup and the definition of the right-handed, rotating $Ox_1y_1z_1$ reference frame is given below.

![[attachments/EM/T5-P27-figure.png]]
*Figure: Sine-shaped wire y1 = sin x1 rotating about the vertical axis Oy1 with angular velocity ω; bead P joined by a vertical spring k to the rail y1 = 2 Source: Problems.pdf, p. 15.*

* **(a)** Write down the general expression for the components of the relative velocity and acceleration of $P$ in the reference frame $Ox_1y_1z_1$ as functions of the axial position of the bead, $x_1$, and its time derivatives $\dot x_1$ and $\ddot x_1$.
* **(b)** Identify all forces acting on the bead and then write down the three components of Newton's second law in the $Ox_1y_1z_1$ reference frame. From these equations, obtain an explicit expression of the components of the reaction force on the wire as a function of $x_1$, $\dot x_1$ and the parameters of the problem only, and a second order differential equation for $x_1$ that does not depend on the reaction force.
* **(c)** Is it possible to use the equation of conservation of mechanical energy of the relative motion of $P$? If so, write it down in terms of $x_1$, $\dot x_1$ and the parameters of the problem. What is the relation of this equation with the differential equation for $x_1$ in the previous point?
* **(d)** For $\omega = 0$ and $x_1 \in [0, 2\pi]$, discuss the existence of equilibrium positions as a function of the parameter $\lambda = mg/k$. Are these equilibrium positions stable?
* **(e)** Consider now that $\omega \neq 0$, and $k = 0$. We drop the bead $P$ at $x_1 = \pi$ with no initial velocity. Sketch the shape of the potential and discuss qualitatively the motion of $P$ if the parameter $\beta = \omega^2/g$ is small or large. Write down the system of equations that would allow to solve for the critical value of $\beta$ that divides between the two behaviors.

---

## 📌 Problem 28: Spherical Pendulum with a Vertically Oscillating Suspension Point

A point particle $P$ of mass $m$ is attached with a massless cord of length $L$ to the point $A$, as shown in the figure. The point $A$ is oscillating vertically with respect to the fixed reference frame $Oxyz$ according to the law $z = a\sin\omega t$, where $a$ and $\omega$ are known constants. The position of the particle $P$ with respect to the moving reference frame $Ax'y'z'$ is completely specified by the angles $\varphi$ and $\theta$ shown in the figure.

![[attachments/EM/T5-P28-figure.png]]
*Figure: Point A oscillating vertically as a sin(ωt) above O; translating axes Ax'y'z'; particle P on a cord from A, located by the angle φ from Az' and the azimuth θ Source: Problems.pdf, p. 16.*

At $t = 0$ the relative position and relative velocity of the particle are defined by the values

$$ \theta_0 = 0, \qquad \varphi_0 = 30^\circ, \qquad \dot\theta_0 = \sqrt{\frac{2g}{\sqrt{3}L}}, \qquad \dot\varphi_0 = 0, $$

where $g$ is the gravitational acceleration. We define the following unit vectors that define a spherical coordinate system

$$ \mathbf{e}_r = \sin\varphi\cos\theta\,\mathbf{i} + \sin\varphi\sin\theta\,\mathbf{j} + \cos\varphi\,\mathbf{k}, \qquad \mathbf{e}_\varphi = \cos\varphi\cos\theta\,\mathbf{i} + \cos\varphi\sin\theta\,\mathbf{j} - \sin\varphi\,\mathbf{k}, \qquad \mathbf{e}_\theta = -\sin\theta\,\mathbf{i} + \cos\theta\,\mathbf{j}. $$

The partial derivatives of these vectors with respect to $\varphi$ and $\theta$ are

$$ \frac{\partial\mathbf{e}_r}{\partial\varphi} = \mathbf{e}_\varphi, \quad \frac{\partial\mathbf{e}_\varphi}{\partial\varphi} = -\mathbf{e}_r, \quad \frac{\partial\mathbf{e}_\theta}{\partial\varphi} = \mathbf{0}, \quad \frac{\partial\mathbf{e}_r}{\partial\theta} = \sin\varphi\,\mathbf{e}_\theta, \quad \frac{\partial\mathbf{e}_\varphi}{\partial\theta} = \cos\varphi\,\mathbf{e}_\theta, \quad \frac{\partial\mathbf{e}_\theta}{\partial\theta} = -\sin\varphi\,\mathbf{e}_r - \cos\varphi\,\mathbf{e}_\varphi. $$

* **(a)** Show that the relative acceleration of $P$ with respect to $Ax'y'z'$ can be expressed as $\mathbf{a}'_P = -L\left(\dot\varphi^2 + \dot\theta^2\sin^2\varphi\right)\mathbf{e}_r + L\left(\ddot\varphi - \dot\theta^2\sin\varphi\cos\varphi\right)\mathbf{e}_\varphi + L\left(\ddot\theta\sin\varphi + 2\dot\theta\dot\varphi\cos\varphi\right)\mathbf{e}_\theta$.
* **(b)** Write down a system of three ordinary differential equations that once solved would yield the angles $\theta$ and $\varphi$, and the tension on the cord as a function of time (you do not need to solve it).
* **(c)** At $t = 0$, determine the relative acceleration of $P$ with respect to $Ax'y'z'$.
* **(d)** At $t = 0$, determine the value of the tension on the cord.

---

## 📌 Problem 30: Particle on a Rotating Quarter Circumference with a Spring

A point particle $P$ of mass $m$ is constrained to move on a smooth quarter of circumference as shown in the figure below. We define a moving reference frame $OX_1Y_1Z_1$ that rotates with respect to an inertial reference frame $OXYZ$. The rotation of the moving reference frame is performed along a vertical axis defined as $x_1 = -R$ and $y_1 = 0$; the angular velocity is $\boldsymbol{\omega} = \omega\mathbf{k} = \omega\mathbf{k}_1$. The particle is attached to a linear spring with the other end attached to the point $B$ of the reference frame $OX_1Y_1Z_1$ with coordinates $(-2R, 0, 0)$. The constant of the spring is $K = \alpha m\omega^2$. The angle between $\overline{OP}$ and the negative side of the $z_1$ axis, $\phi$, is used to define the position of the particle. Neglect the action of gravity on the particle.

Initially the particle is located at $\phi = 0$ and it is set to motion with a relative velocity $-\beta\omega R\,\mathbf{i}_1$. Both $\alpha$ and $\beta$ are positive nondimensional parameters.

![[attachments/EM/T5-P30-figure.png]]
*Figure: Quarter circumference of radius R centred at O in the plane X1Z1, rotation axis x1 = −R (dashed), spring of constant K from B = (−2R, 0, 0) to P, angle φ measured from the negative z1 axis Source: Problems.pdf, p. 18.*

* **(a)** Compute the relative velocity and the relative acceleration of the particle in the path variable reference frame $\{\mathbf{e}_t, \mathbf{e}_n, \mathbf{e}_b\}$ as functions of the coordinate $\phi$ and their derivatives.
* **(b)** Write down the three components of Newton's second law expressed in the path variables reference frame $\{\mathbf{e}_t, \mathbf{e}_n, \mathbf{e}_b\}$.
* **(c)** Express the energy conservation equation in the relative reference frame. Discuss if this equation is equivalent to one of the above ones.

Let us now consider a different problem. Depending on the values of the parameters, we may find the equilibrium of the forces at different positions.

* **(d)** Obtain the value of $\alpha$ to have an equilibrium position when the particle is positioned at $\phi$ equal to $\pi/6$.

For this value of $\alpha$, the particle is again located at $\phi = 0$ and is set to motion with the relative velocity defined before.

* **(e)** Describe the possible types of motion for the different values of $\beta$. In particular, obtain the critical value of $\beta$ that makes the particle reach the position $\phi = \pi/2$ and the reaction force of the curve to the particle at that instant.
* **(f)** For a value of $\beta$ higher than the critical one, the particle leaves the arc of circumference and its motion is not anymore constrained. Under these conditions compute the maximum height reached by the particle, $z_{max}$, as a function of $\beta$. Note that the particle is still under the action of the spring.

---

## 📌 Problem 33: Two Repelling Particles on a Rotating Parabola

Two heavy point particles, $P_1$ and $P_2$, of mass $m$ each, slide without friction along a rigid wire parabola given by the equation $z = x^2/(2L)$, where $L$ is a known length. The wire rotates about its axis with a fixed, known angular velocity $\omega$. The two particles repel each other electrically with a force of magnitude $F_E = k/d^2$, where $k$ is a known constant and $d$ is the distance between the particles. We define the rotating reference frame $Oxyz$ attached to the parabola as shown in the figure below.

![[attachments/EM/T5-P33-figure.png]]
*Figure: Parabola z = x²/(2L) in the plane Oxz rotating with angular velocity ω about Oz, particles P1 (left branch) and P2 (right branch) with the repulsive forces F_E along the line P1P2, gravity g downward Source: Problems.pdf, p. 21.*

* **(a)** Write down the position, velocity, and acceleration vectors of each particle relative to $Oxyz$ in a generic instant of time, as a function of $x_1$, $x_2$ (the position of $P_1$ and $P_2$ along the $Ox$ axis) and their derivatives.
* **(b)** Write down Newton's second law for each particle in the $Oxyz$ reference frame.
* **(c)** If the rotation of the wire is maintained by a motor, how much torque must it produce in the $Oz$ direction to keep $\omega$ constant as a function of the variables of the problem and their derivatives?
* **(d)** Find out the equilibrium configurations of the system in the reference frame $Oxyz$ as a function of the parameters $\gamma = g/(\omega^2L)$ and $\kappa = k/(m\omega^2L^3)$.

Consider now that $P_1$ and $P_2$ are constrained to move symmetrically on each branch of the parabola, and that $\gamma = \kappa = 2$. Initially, $x_1(0) = L$ and $v_1(0) = L\omega$ (with $\dot x_1(0) \gt 0$).

* **(e)** Write down the equation that gives the minimum and maximum values of $x_1$ occurring in this case. *Hint: this equation is a third-order polynomial in $x_1$.*

---

## 📌 Problem 34: Particle on a Circular Wire in an Oscillating Vertical Plane

A heavy point particle $P$ of mass $m$ slides without friction on a circular wire of center $C$ and radius $R$. The wire is located on a vertical plane $Oxy$ that rotates about the vertical axis $Oy$ with a prescribed angular frequency $\boldsymbol{\Omega}(t) = A\omega\sin(\omega t)\,\mathbf{j}$, where $A$ and $\omega$ are known positive constants, as shown in the figure. The angle that the vector $\overrightarrow{CP}$ makes with the $Ox$ axis is denoted $\varphi$.

![[attachments/EM/T5-P34-figure.png]]
*Figure: Circular wire of centre C and radius R in the vertical plane Oxy, passing through O, with C on the Ox axis; P on the wire at angle φ from Ox; the plane rotates about the vertical axis Oy with Ω(t); gravity g downward Source: Problems.pdf, p. 22.*

Answer the following questions in a reasoned way:

* **(a)** Write down the position, velocity and acceleration vectors of $P$ relative to the reference frame $Oxyz$, as a function of $\varphi$ and its derivatives.
* **(b)** Identify the forces that act on $P$, and write down their mathematical expression for a generic instant of time $t$.
* **(c)** Is the mechanical energy of $P$ conserved as seen from the $Oxy$ reference frame? Why?
* **(d)** Write down a single second order differential equation to calculate $\varphi$ as a function of time. Note that you do not need to solve this equation.
* **(e)** Compute the reaction of the wire on the particle $P$ as a function of $\varphi$, $\dot\varphi$ and $t$.
* **(f)** Assume now that $A^2 \ll g/(R\omega^2)$ and that the motion of $P$ is such that $\varphi = \delta - \pi/2$ with $\delta \ll 1$. Around what value of $\delta$ does the particle oscillate? Are there any values of $\omega$ for which the approximation $\delta \ll 1$ will not hold?

---

## 📌 Problem 36: Pendulum String Dragged by a Rotating Bar

A heavy point particle $P$ with mass $m$ hangs from a fixed point $A$ on the ceiling with a massless string of constant length $L$. The particle is initially at rest. A bar $b$ rotates about its center $O$ in a horizontal plane at a distance $h$ from the ceiling, with a known, constant angular velocity $\omega$. The horizontal distance between $O$ and $A$ is $R$. At time $t = 0$, the bar collides with the string and drags it along its motion. The string slides over the bar without friction. We call $C$ the instantaneous point of contact of the string with the bar. We define a reference frame $S_1$ that rotates with the bar as shown in the figure. We call $\xi$ the distance between $O$ and $C$; $\ell$ the length of the string segment between $C$ and $P$; $\theta$ the angle between the vertical plane $Ox_1z_1$ and the plane defined by the bar and $P$; and $\varphi$ the angle formed between the string segment $CP$ and the bar. You are asked to study only the part of the motion in which the string remains tense and in contact with the bar.

![[attachments/EM/T5-P36-figure.png]]
*Figure: Left, before the impact (t negative): bar b rotating with ω about O in the horizontal plane x1y1, ceiling point A at height h above that plane and horizontal distance R from O, P hanging below A. Right, after the impact (t positive): frame S1 = Ox1y1z1 attached to the bar, contact point C at distance ξ from O, string A–C–P with segment CP of length ℓ at angle φ from the bar, θ the angle of the plane bar–P from the vertical; gravity g downward Source: Problems.pdf, p. 24.*

* **(a)** Write down the position and velocity of point $A$ in $S_1$ as a function of time.
* **(b)** Obtain a general expression for the position, velocity, and acceleration of $P$ in $S_1$ as a function of $\xi$, $\ell$, $\theta$, $\varphi$, their derivatives, and time.
* **(c)** Express $AC$, $\ell$, and $\varphi$ as a function of $\xi$ and time.
* **(d)** Identify and express all the forces acting on $P$.
* **(e)** Write down a set of second order differential equations for the evolution of the unknowns of the problem.
* **(f)** Compute the initial conditions for the previous equations at $t = 0$.
* **(g)** Is the mechanical energy of the particle conserved in time? Justify your answer.
* **(h)** If/when the string separates from the bar, express the geometric condition as a relation between $\theta$ and time.

---

## 📌 Problem 37: Particle on a Spinning Elliptic Cone

A heavy point particle $P$ with mass $m$ moves without friction on a cone of elliptic cross-section as shown in the figure. We define an auxiliary reference frame $S_1 : \{O; \mathcal{B}_1\}$ attached to the cone. The cone is defined in terms of two parameters $\zeta$, $\beta$ as

$$ \text{Elliptic cone:} \quad \begin{cases} x_1 = \zeta\cos\beta \\ y_1 = 2\zeta\sin\beta \\ z_1 = \zeta \end{cases} \qquad (5) $$

The cone spins about its $Oz_1$ axis at a constant angular rate $\Omega$ with respect to the inertial reference frame $S_0 : \{O; \mathcal{B}_0\}$. At time $t = 0$, the reference frame $S_1$ coincides with $S_0$, the particle $P$ is located at $\mathbf{r}^P_{1,0} = 2\mathbf{j}_1 + \mathbf{k}_1$, and has a velocity $\mathbf{v}^P_{1,0} = \mathbf{i}_1$.

![[attachments/EM/T5-P37-figure.png]]
*Figure: Elliptic cone with vertex O and vertical axis z0 = z1, frame S1 rotated by the angle Omega t about z0, particle P on the cone, gravity g downward Source: Problems.pdf, p. 25.*

* **(a)** How many degrees of freedom does the particle motion have?
* **(b)** Obtain the general expression for the position, velocity, and acceleration of $P$ **in reference frame $S_1$** as a function of $\zeta$, $\beta$ and their derivatives. Remember to define any unit vectors that you use in terms of the vectors of $\mathcal{B}_0$.
* **(c)** Identify and express mathematically all the forces acting on $P$ as seen from $S_1$.
* **(d)** Obtain two second-order differential equations for the evolution of $\zeta$, $\beta$ in time, which do not depend on any other unknowns in the problem.
* **(e)** Find, justify, and write down one conservation law in this problem, including the value of any constants there might be.
* **(f)** Find the equilibrium positions for $P$ in $S_1$ for $\zeta \gt 0$ as a function of the constants of the problem.

---

## 📌 Problem 40: Spring-Coupled Particles on a Vertical Axis and a Revolving Ring

Two heavy particles $P$ and $Q$, each of mass $m$, are connected with a spring of stiffness $k$ as shown in the figure. An inertial reference frame $S_0$ is defined with origin $O$ and vector basis $\mathcal{B}_0 = \{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$. Particle $P$ slides without friction along the vertical axis, while particle $Q$ slides without friction on a ring of radius $R$ contained in the horizontal plane defined by $O$, $\mathbf{i}_0$ and $\mathbf{j}_0$. The center $D$ of this ring is located a distance $\ell$ from $O$ and rotates around the vertical axis of $S_0$ with a known constant angular rate $\Omega$. A rotating reference frame $S_1$ is defined so that the $\mathbf{j}_1$ vector follows the position of $D$. We define the generalized coordinates $\zeta$ (vertical position of $P$) and $\phi$ (angle of $Q$ on the circle from $\mathbf{j}_1$) as shown.

![[attachments/EM/T5-P40-figure.png]]
*Figure: Particle P on the vertical axis k0 = k1, particle Q on a horizontal ring of centre D on the j1 axis, spring k between P and Q, frame S1 rotated by Omega t about k0 Source: Problems.pdf, p. 28.*

* **(a)** How many degrees of freedom does the system have? Define the vectors $\mathbf{i}_1$, $\mathbf{j}_1$ and $\mathbf{k}_1$ in terms of the vectors of $\mathcal{B}_0$.
* **(b)** Write down the general expression of the position, velocity, and acceleration of $P$ and $Q$ with respect to $S_1$ in terms of $\zeta$, $\phi$ and their derivatives.
* **(c)** Identify and write down the general expression of all the forces acting on $P$ and $Q$.
* **(d)** Using $S_1$ for your analysis, write down the scalar equations of motion of $P$ and $Q$.
* **(e)** Starting from these equations, write down a system of two differential equations for $\zeta$ and $\phi$, that do not depend on any other unknowns of the problem.
* **(f)** Find one conservation law of the problem (i.e., a first integral of motion) in reference frame $S_1$.

---

## 📌 Problem 41: Satellite Solar Panel (Composition of Rotations)

The angle $\theta$ describing the rotation of the solar panels of a reconnaissance satellite about the body-fixed axis $x$ is an arbitrary function of time. The satellite spins about the $z$ axis at the constant angular rate $\omega$. Derive expressions for the absolute velocity and acceleration of point $B$ in the figure relative to an inertial reference frame centered in $A$.

(Taken from Ginsberg, "Engineering Dynamics", Cambridge University Press, 2008.)

![[attachments/EM/T5-P41-figure.png]]
*Figure: Satellite body spinning about z with a solar panel rotated by the angle θ about the body-fixed x axis, points A and B, dimensions H and W Source: Problems.pdf, p. 29.*

---

## 📌 Problem 47: Two Repelling Particles on Concentric Wires in a Rotating Plane

We consider a system of two heavy particles of equal mass $m$. The first particle $P$ is constrained to move without friction along a circular wire of radius $a$. The second particle $Q$ is constrained to move without friction along a circular wire of radius $2a$. Both wires are contained in a plane $Ox_1y_1$ that rotates at a constant, known angular rate $\Omega$ about the axis $Oy_1 \equiv Oy_0$ with respect to a fixed reference frame $S_0$ with axes $Ox_0y_0z_0$ (not shown in the figure). We also define a moving reference frame $S_1$ with axes $Ox_1y_1z_1$. The two particles repel each other with a force that is proportional to their distance, with constant of proportionality, $k$.

![[attachments/EM/T5-P47-figure.png]]
*Figure: Concentric circular wires of radii a and 2a centred at O in the plane Ox1y1, particle P at angle varphi and particle Q at angle theta from x1, the plane spins with rate Omega about the vertical axis y0 = y1, gravity g downward Source: Problems.pdf, p. 32.*

* **(a)** How many configuration degrees of freedom has this system?
* **(b)** How many independent components of the reaction forces on the particles need to be considered? Write down the reaction force on each particle.
* **(c)** Write down the relative accelerations of $P$ and $Q$ with respect to $S_1$ as a function of the coordinates of the problem and their derivatives.
* **(d)** Express the applied forces on the particles as a function of the coordinates of the problem.
* **(e)** Express the fictitious forces of inertia on the particles as seen from $S_1$, as a function of the coordinates of the problem and their derivatives.
* **(f)** Write down a system of ordinary differential equations to determine the evolution of the coordinates of the problem as a function of time, free of any other unknowns. You do not need to solve this system (since no initial conditions have been provided) but we assume that we know how to solve it, so that from this point we know the coordinates as a function of time.
* **(g)** Determine the values of the reaction forces from the wires as a function of time.
* **(h)** Is the mechanical energy of this system conserved in $S_1$? If so, write down the corresponding equation.
* **(i)** Determine the values of $\alpha = \dfrac{ka}{mg}$ and $\beta = \dfrac{a\Omega^2}{g}$ so that $\varphi = 30^\circ$, $\theta = -60^\circ$ is an equilibrium position of the system in the relative motion.

---

## 📌 Problem 49: Particle on a Rotating Sphere Attracted to a Point

A point particle $P$ of mass $m$ slides without friction on a sphere of radius $a$ centered at the origin of the inertial reference frame $S_0$ as shown in the figure. The particle is attracted by a point $A$ in the equatorial plane, located a distance $a$ from the surface of the sphere as shown. The force of attraction is linearly proportional to the distance between this point and $P$, with known constant of proportionality $k \gt 0$. The sphere and the point $A$ rotate rigidly about the vertical with a known angular velocity $\Omega\mathbf{k}_0$. We define the auxiliary reference frame $S_1$ that rotates with the sphere and point $A$, with $\mathbf{k}_1 = \mathbf{k}_0$ and $\mathbf{i}_1$ pointing in the direction of $A$. We introduce the angles $\phi$ and $\theta$ as shown to locate $P$ on the sphere. Note that there is no gravity in this problem.

![[attachments/EM/T5-P49-figure.png]]
*Figure: Sphere of radius a centred at O, point A on the i1 axis outside the sphere in the equatorial plane, particle P located by the angles phi and theta, frame S1 rotated by Omega t about k0 = k1 Source: Problems.pdf, p. 34.*

* **(a)** Express the position, velocity, and acceleration of $P$ with respect to $S_1$ in terms of $\phi$, $\theta$ and their derivatives. Remember to define any unit vectors that you want to use in terms of $\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0$ first.
* **(b)** Write down the (vector) equation of motion of $P$ in $S_1$, and derive from there a set of two scalar second-order differential equations for $\phi$, $\theta$ that do not depend on any other unknowns. To do so, first identify and write down all the forces needed in your analysis.
* **(c)** Is the mechanical energy of $P$ conserved in $S_1$? Explain. If so, write down the corresponding conservation law.
* **(d)** Identify all equilibrium configurations of the system, and discuss them as a function of the ratio $m\Omega^2/k$.
* **(e)** Assuming the functions of time $\phi(t)$ and $\theta(t)$ are known, write down the expression of the reaction of the sphere on $P$.

---

## 📌 Problem 51: Particle inside a Hollow Sphere in a Rotating Frame

A heavy point particle $P$ of mass $m$ is constrained to move inside the surface of a hollow sphere of radius $R$ and center $C$ located at $\mathbf{r}_1^C = R(\mathbf{j}_1 + \mathbf{k}_1)$. The surface of the sphere is smooth. The reference frame $S_1$ shown in the figure is a non-inertial reference frame, because it rotates with a known angular velocity $\boldsymbol{\omega}_{10} = \Omega(t)\,\mathbf{k}_1$ with respect to inertial space. We introduce the two coordinates $\theta$ and $\phi$ as shown in the figure, in order to characterize the configuration of $P$.

![[attachments/EM/T5-P51-figure.png]]
*Figure: Rotating frame S1 with axes i1, j1, k1, hollow sphere of centre C at R(j1+k1), particle P located by the angles theta and phi, angular velocity Omega(t) about k1 Source: Problems.pdf, p. 36.*

* **(a)** Give the expressions for the position, velocity, and acceleration vectors of $P$ with respect to $S_1$, as functions of $\theta$, $\phi$ and their derivatives. Remember that you may use any unit vectors in your solution, provided that you define them first.
* **(b)** Identify and write down all forces (actual and fictitious) on $P$ as seen from $S_1$.
* **(c)** Write down two differential equations for $\theta$ and $\phi$, free of any other unknowns.
* **(d)** Write down an expression for the reaction unknown. This expression may depend on $\theta, \dot{\theta}, \phi, \dot{\phi}$ and the known parameters of the problem. What is the mathematical condition for the particle to separate from the surface?
* **(e)** In the case that $\Omega = \text{const}$, determine and discuss the value of $\theta$, $\phi$ and the reaction unknown for the equilibrium configurations of $P$.
