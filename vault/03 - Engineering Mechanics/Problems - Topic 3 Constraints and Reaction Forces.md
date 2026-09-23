---
title: "Problems - Topic 3: Constraints and Reaction Forces"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/03-engineering-mechanics/problemas/Problems.pdf"
type: "Verbatim Problem Statements"
language: "English"
---

# 📝 Topic 3: Constraints and Reaction Forces - Problem Statements

Official problem statements from the UC3M Aerospace Engineering problem collection (`Problems.pdf`, Chapter 1). These problems test configuration degrees of freedom (CDOFs), geometric surfaces and curves, normal and tangent subspaces ($V_N, V_T$), constraint reactions, dynamical decoupling, zero work theorem, multi-particle systems connected by inextensible cables, and Coulomb dry friction.

> [!NOTE]
> **Status:** Verbatim problem statements transcribed faithfully from official department exams and problem sets.
> 
> [!SUCCESS] Complete Analytical Solutions Ready
> All 15 problems have full, step-by-step pedagogical solutions developed in: [[Solutions - Topic 3 Constraints and Reaction Forces]].

---

## 📌 Problem 18: Heavy Particle on a Cone

A heavy particle of mass $m$ is moving without friction on a cone which is described as:
$$ z^2 = x^2 + y^2 $$
The frame of reference $Oxyz$ is inertial and $Oz$ is the ascending vertical. The initial coordinates of the particle are $(a, 0, a)$ and its velocity is $\sqrt{ag}\,\mathbf{j}$. Reduce the problem to integral equations and determine the maximum and minimum value of $z$ along the motion.

---

## 📌 Problem 19: Heavy Particle on a Paraboloid

A heavy particle of mass $m$ is moving without friction on the paraboloid which is described as:
$$ az = r^2 $$
where $a$ is a positive constant and $r$ is the distance to the $Oz$ vertical axis. If $r = a$ initially, and the particle is released with a velocity $v_0$ tangent to the local parallel, reduce the problem to integrals of the form $\int [...] dr = \int [...] dt$. Determine the maximum and minimum of $r$ along the motion.

---

## 📌 Problem 20: Heavy Particle on a Rotating Circumference

A heavy particle is moving along a smooth circumference of radius $R$ and center $O$. One of the diameters of the circumference is along the local vertical, and the circumference is rotating with constant angular velocity $\omega$ about it. The position of the particle with respect to the circumference is described by the angle $\theta$ between the particle and the lowest point of the circumference.

* **(a)** Discuss the conservation of mechanical energy in the moving reference frame and compute its value.
* **(b)** Compute the reaction of the circumference in the direction normal to its plane, as a function of $\theta$.

---

## 📌 Problem 22: Particle on a Curve

A heavy point particle $P$ of mass $m$ is constrained to move without friction along the curve:
$$ y = a\left(1 - \cos\frac{x}{a}\right) \tag{4} $$
in the range $-\pi a \le x \le \pi a$, where $a$ is a positive constant. Initially, the particle is located at $x = 0$ with velocity $v_0$ along the positive $x$ axis.

* **(a)** Reduce the problem to integrals.
* **(b)** If $v_0 = \sqrt{ga}$, determine the minimum and maximum value of $x$ along the motion.
* **(c)** What should be the minimum value of $v_0$ in order to reach $x = \pi a$?

*Extended Exam Section (Moving Frame):*
Let's assume now that the curve containing the point particle rotates around the $OY$ axis with constant angular velocity $\boldsymbol{\omega} = \Omega\mathbf{j}$.
* **(d)** Define a convenient moving reference frame with origin in $O$, $OX_1Y_1Z_1$. Determine the inertia force that acts on the particle in this moving reference frame as a function of $m, \Omega, x_1$ and $\dot{x}_1$, where $x_1$ represents the position coordinate of $P$ along $OX_1$.
* **(e)** Reduce the problem to quadratures and determine the value of the reaction force.
* **(f)** Find out a transcendental equation whose solutions are the equilibrium positions of the point particle in $OX_1Y_1Z_1$.
* **(g)** If $\Omega$ were a function of time, would it be possible to use the energy equation in the same way as before? Justify your answer.

---

## 📌 Problem 24: Particle on a Circumference with a Spring

A heavy particle $P$ is constrained to move along a circumference and it is attached to a spring as shown in the figure. The mass of the particle is $m$, and the radius of the circumference is $a$. The other end of the spring is attached to a point of the $y$ axis with coordinates $(0, \beta a)$ and the constant of the spring is equal to $k$.

* **(a)** Compute the potential of the forces acting on the particle as a function of the angle $\theta$ (shown in the figure).
* **(b)** Identify the equilibrium positions.

The particle departs from the point $(a, 0)$ of the circumference with an initial velocity $\mathbf{v}_0 = v_0\mathbf{j}$.
* **(c)** Reduce the motion to integrals (i.e., quadratures).
* **(d)** If $\beta = \frac{mg}{ka}$, obtain the position of the particle as a function of time.

*Viscous Damping Case:*
Consider now the situation in which an additional force acts on the particle. The force is proportional to, and in the same direction as, the instantaneous velocity. The constant of proportionality is $2m\mu$. The initial conditions are the same as before.
* **(e)** Obtain the position of the particle as a function of time.
* **(f)** Obtain the reaction of the circumference.

---

## 📌 Problem 26: Heavy Particle on a Rotating Half-Circumference

A heavy point particle $P$ of mass $m$ is constrained to move without friction along the half-circumference wire of radius $a$ shown in the figure. The wire containing the point particle rotates around the $OY$ axis with constant angular velocity $\omega = \Omega\mathbf{j}$. Initially, the particle is located at $x = 0$ with velocity $v_0$ along the positive $x$ axis.

* **(a)** Determine the number of degrees of freedom of the problem.
* **(b)** Define a convenient moving reference frame with origin in $O$, $OX_1Y_1Z_1$. Express the inertia force that acts on the particle in this moving reference frame.
* **(c)** Express also the components of the weight of the particle with respect to $OX_1Y_1Z_1$.
* **(d)** Determine if there are any equilibrium points.
* **(e)** Reduce the problem to integrals (i.e. quadratures) and determine the value of the reaction force.
* **(f)** Is it possible to use the energy equation? If $\Omega$ were a function of time, would it be possible to use the energy equation? Justify your answer.

---

## 📌 Problem 29: Heavy Particle on a Tilted Cylinder

A heavy particle of mass $m$ is constrained to move without friction along the surface of an infinitely-long, circular cylinder of radius $R$. The cylinder axis ($Oz$) forms an angle $\alpha$ with the vertical direction ($Oz_1$). The position of the particle is completely specified by providing the coordinate $z$ along the axis $Oz$ and the angle $\theta$. Initially, the particle is located at $z = 0, \theta = \pi/2$ and the time derivatives are $\dot{z} = v_0$ and $\dot{\theta} = \omega_0$.

* **(a)** Determine the value of $z$ as a function of time, $z(t)$.
* **(b)** Reduce the determination of the angle $\theta(t)$ to integrals of the form $\int [...] d\theta = \int [...] dt$.
* **(c)** Determine the reaction from the cylinder as a function of $\theta$.
* **(d)** For the particular case $\omega_0^2 = \frac{g\sin\alpha}{R}$, describe qualitatively the motion of the particle.
* **(e)** For the particular case $\omega_0^2 = \frac{4g\sin\alpha}{R}$, describe qualitatively the motion of the particle.

---

## 📌 Problem 31: Two Particles on Cone with String

Two heavy point particles $P_1$ and $P_2$ of mass $m$ each are connected by an inextensible, massless string of total length $\ell$. Particle $P_1$ is constrained to move without friction over the surface of a cone of semiangle $\alpha$ (the particle cannot leave the surface of the cone). The string passes through an aperture at the cone vertex $O$, and it can slide through it without friction. Particle $P_2$ hangs along the cone axis, and is constrained to move along it. We define an inertial reference frame $S_0$. We call $\xi$ the length of the fraction of string between $O$ and $P_1$, and $\theta$ the angle formed between the $Ox$ axis and the projection onto the $Oxy$ plane of the $\mathbf{OP}_1$ vector. In the following, assume that the string is always tense and that the particles do not reach point $O$ during motion.

* **(a)** Write down the general expression of the position, velocity, and acceleration vectors of $P_1$ and $P_2$ as a function of $\theta, \xi$ and the parameters of the problem.
* **(b)** Write down the expression of all forces that act on $P_1$ and $P_2$.
* **(c)** Write down the differential equations that, if solved, would yield the time evolution of $\theta, \xi$, the tension on the string, and any other reaction force in the problem.
* **(d)** What is the mathematical condition that the function $\xi(t)$ must satisfy for the string to remain tense all the time?
* **(e)** How fast should $P_1$ rotate in the $\theta$ direction to have a circular trajectory over a cone parallel? What is the value of the string tension and any other reaction force in the problem in that case? Give your answer as a function of $\xi$ and the parameters of the problem.
* **(f)** Taking these equations as the starting point (or based on the physical considerations of the problem) write down two first-integrals of the problem that do not depend on the string tension or any other reaction force in the problem.

---

## 📌 Problem 32: Particle with String on Spool

A heavy particle $P$ of mass $m$ is connected by a string of total length $l = 4\pi a$ to a cylindrical spool of radius $a$ and center at $O$. The spool rotates at a known constant angular rate $\omega$ counterclockwise. The string is massless, inelastic, thin, and remains always in tension during the motion of the particle. We define the inertial reference frame $Oxy$. The other end of the string is attached to the spool at a point $A$ of its perimeter, and we shall call $B$ the instantaneous point of tangency between the straight segment of the string (the segment $BP$) and the spool. We will denote the angle between the local horizontal (axis $Ox$) and the radius $OB$ as $\phi$. Initially, $\mathbf{OA} = -a\mathbf{i}$, and $B$ never reaches $A$.

* **(a)** Discuss the number of degrees of freedom of the motion of the particle.
* **(b)** Write down the position, velocity, and acceleration vectors of $P$ with respect to $Oxy$ as a function of the constants of the problem, time, the angle $\phi$, and its derivatives.
* **(c)** Write down the mathematical expression of the forces acting on $P$.
* **(d)** Is the mechanical energy of $P$ conserved? If so, write down the equation of conservation of mechanical energy; otherwise, explain why it is not conserved.
* **(e)** Write down a closed set of equations that, if solved, would yield $\phi$ (and the other unknowns of the problem, if any) as a function of time. Note that you do not need to solve the equations.
* **(f)** Consider now that $\omega = 0$. Can you write down a first integral of motion that only involves $\phi$ and $\dot{\phi}$ (but not $\ddot{\phi}$) in this case? You may want to rethink your previous answers for this particular case.

---

## 📌 Problem 35: String with Two Particles on a Cylinder

Two heavy particles $P$ and $Q$ of mass $m$ each are connected by an inextensible massless string of constant length $L$. Part of this string rests on top of a cylinder of radius $R$ and center at $O$. The string can slide over the cylinder without friction, and remains tense at all times. Furthermore, $P$ and $Q$ are also connected by a spring of zero natural length and stiffness $k$. We define the inertial reference frame $S_0$. We denote as $A$ and $B$ the points of tangency of the string with the cylinder.

* **(a)** How many degrees of freedom does this system have? Define your own generalized coordinates to parametrize the configuration of the system. You will use them in the rest of the problem.
* **(b)** Write down the general expression of the position, velocity, and acceleration vectors of $P$ and $Q$ relative to the $S_0$ reference frame as a function of your chosen coordinates and their time derivatives.
* **(c)** Write down the expression of all forces acting on $P$ and $Q$.
* **(d)** Discuss whether the mechanical energy of $P$ is conserved; if so, write down the expression of the corresponding potential energy.
* **(e)** Consider now that we restrict the motion of the system to symmetric configurations about the $Oy$ axis only. What is the number of degrees of freedom now? Find the mathematical relations that exist between your previously-defined coordinates in this case.
* **(f)** Find the approximate value of your coordinates when the system is in equilibrium and the configuration is symmetric about the $Oy$ axis. To do so, assume that the deviation from the vertical of the $AP$ and $BQ$ segments is small, and linearize the equations of motion. Find the angular frequency of the oscillations around this equilibrium configuration.

---

## 📌 Problem 38: Particle on Torus

A heavy point particle $P$ with mass $m_P = 1$ moves without friction on a vertically-standing torus. The particle cannot separate from the surface of this torus. The torus is defined in the Cartesian coordinates of the inertial reference frame $S_0$ by the following expressions:
$$ \begin{cases} x_0 = (2 + \cos\phi)\sin\theta \\ y_0 = \sin\phi \\ z_0 = 4 + (2 + \cos\phi)\cos\theta \end{cases} $$
A second particle $Q$ with mass $m_Q = 2$ is constrained to move on the $Ox_0y_0$ plane without friction. The two particles $P$ and $Q$ attract each other with a force that is proportional to the distance between them. The proportionality constant of this force is $k = 2$. Initially, particle $P$ is located at $\mathbf{r}_0^P(t_0) = 2\mathbf{i}_0 + \mathbf{j}_0 + 4\mathbf{k}_0$ with $\mathbf{v}_0^P(t_0) = -\mathbf{k}_0$ and particle $Q$ is located at $\mathbf{r}_0^Q(t_0) = 3\mathbf{i}_0 + \mathbf{j}_0$ with $\mathbf{v}_0^Q(t_0) = -\mathbf{i}_0 + \mathbf{j}_0$.

* **(a)** Pick a minimal, valid set of coordinates to describe the configuration of the system. Indicate what is the geometrical meaning of the chosen coordinates.
* **(b)** Obtain a general expression for the position, velocity, and acceleration vectors of $P$ and $Q$ in $S_0$ using the chosen coordinates and their derivatives.
* **(c)** Obtain two independent tangent vectors and one normal vector to the torus as a function of the chosen coordinates.
* **(d)** Identify and express mathematically all the forces acting on $P$ and $Q$.
* **(e)** Find down a set of second order differential equations to determine the evolution of the chosen coordinates in time, free of any other unknowns.
* **(f)** Obtain a scalar conservation law.
* **(g)** Attending to this conservation law alone, can $P$ ever reach the highest point of the torus?

---

## 📌 Problem 39: Particle on a String with a Plate

A heavy point particle $P$ with mass $m$ is connected with point $O$ on the upper surface of a thin square plate by a massless, inextensible string of length $\ell$. The distance between $O$ and the edge of the plate is $d$. The string hangs over the edge of the plate and can slide without friction. You can assume that the string remains tense and in contact with the plate at all times. We denote the geometric point where the string is in contact with the plate edge as $Q$. We define the inertial reference frame $S_0 : \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$. We define the angle $\theta$ between the $Ox_0$ axis and the string segment $OQ$, and the angle $\phi$ between a vertical plane containing the plate edge and the line perpendicular to the plate edge that passes through $P$. Initially at time $t = 0$, $\theta(0) = \phi(0) = \pi/3\text{ rad}$, and the modulus of the velocity of $P$ is $v_0^P(0) = \sqrt{\ell g}$, where $g$ is the magnitude of the acceleration due to gravity.

*(Hint: Note that under the conditions of the problem, the two angles marked with dashed lines are equal)*.

* **(a)** How many degrees of freedom does the system have?
* **(b)** Obtain the general expression of a unit vector in the direction from $Q$ to $P$ as a function of $\theta$ and $\phi$.
* **(c)** Obtain the general expression for the position, velocity, and acceleration vectors of $Q$ and $P$ in $S_0$ as a function of $\theta, \phi$, their derivatives, and the parameters of the problem.
* **(d)** Identify and express mathematically all the forces acting on $P$.
* **(e)** Find a set of second order differential equations to determine the evolution of $\theta$ and $\phi$ in time, free of any other unknowns.
* **(f)** Does the tension force exert work on $P$? Provide proof of your answer.
* **(g)** Derive the general expression of the mechanical energy of $P$ in $S_0$ and compute its value initially. Is this a conserved quantity of motion? Justify your answer.

---

## 📌 Problem 43: Two Connected Particles, Plane with Hole

We consider a smooth horizontal plane with a small hole in it. One of the ends of a massless cord of length $2a$ is passed through the hole and then, two point particles, $P_1$ and $P_2$, each with the same mass $m$, are attached to the ends of the cord. Therefore, $P_1$ is constrained to move on the plane and $P_2$ moves along a vertical line below the hole. Initially, half of the cord lies under the plane and half of the cord is on the plane. At that instant, $P_1$ is pushed with a speed $v_0$ perpendicular to the cord, counterclockwise as seen from above. Assume that the cord is always in tension.

* **(a)** What is the value of $v_0$ if $P_1$ describes a circumference?
* **(b)** In that case, what is the value of the tension in the cord?
* **(c)** If $v_0 = \sqrt{8ag/3}$, reduce the problem to integrals (i.e., quadratures).
* **(d)** Show that for this value of $v_0$, $P_1$ oscillates between $r = a$ and $r = 2a$.
* **(e)** Apply Newton's law to $P_2$ and show that the tension of the cord is $T = mg\left(\frac{1}{2} + \frac{4a^3}{3r^3}\right)$.
* **(f)** Write down the new equations of motion if the plane on which $P_1$ moves is rough, with a friction coefficient $\mu$.

*(Hint: the roots of the polynomial $-3x^3 + 7x^2 - 4$ are $x_1 = 1, x_2 = 2$ and $x_3 = -2/3$)*.

---

## 📌 Problem 48: Two Connected Particles, One on Paraboloid

Two heavy particles $P$ and $Q$, each of mass $m$, are connected with an inextensible, massless string of length $\ell$. Particle $P$ is constrained to stay on a paraboloid, given implicitly by equation $z = cR^2$, where $c$ is a known constant and we have introduced the usual cylindrical coordinates $\{R, \theta, z\}$. The string passes through a small hole at the origin $O$, and particle $Q$ is restricted to hang along the vertical axis. The reference frame $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ is inertial. There is no friction in this problem. Assume that the string is long enough so that $Q$ never reaches $O$ and that it is always tense.

* **(a)** How many effective degrees of freedom does the system have? Justify your answer.
* **(b)** Give the expressions for the position, velocity, and acceleration of $P$ and $Q$ with respect to $S_0$ as a function of $R, \theta$ and their derivatives. If you use any vector basis other than $\{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ to write your solution, define it first.
* **(c)** Find a normal vector and two linearly independent tangent vectors to the paraboloid as a function of $R, \theta$. They do not need to be unitary.
* **(d)** Identify and write down the general expression of all the forces acting on $P$ and $Q$, introducing new unknowns as needed.
* **(e)** Find the condition that the solution $R(t)$ must satisfy so that the string is indeed always in tension.
* **(f)** Using $S_0$ for your analysis, write down two second-order differential equations for $R$ and $\theta$, that do not depend on any other unknowns.
* **(g)** Find two scalar conservation laws (i.e., first integrals).
* **(h)** Assuming that initially $R = 1/c, \theta = 0, \dot{R} = 0, \dot{\theta} = d$, where $d \neq 0$ is a given value, write down an equation in the form $f(R) = 0$ whose roots determine the minimum and maximum values of $R$ in the subsequent motion. You do not need to solve this equation.

---

## 📌 Problem 50: Double Pendulum

A double pendulum consists of two heavy point masses $P$ and $Q$, each of mass $m$, connected to the origin $O$ and to each other by two rigid, massless bars of length $\ell$. We define the inertial frame $S_0$ with origin $O$ and vector basis $\mathcal{B}_0$. We define the two angles $\theta$ and $\phi$ to describe the configuration of the system.

* **(a)** Write down the general expressions of the position, velocity, and acceleration vectors of $P$ and $Q$, using $\theta, \phi$ and their derivatives.
* **(b)** Write down all forces acting on $P$ and $Q$, introducing new unknowns as needed.
* **(c)** Write down the equations of motion for $\theta$ and $\phi$, free of other unknowns.
* **(d)** Find and write down one conservation law of this problem.
* **(e)** If the initial conditions are $\theta = \phi = \pi/4, \dot{\theta} = \dot{\phi} = 0$, will $Q$ ever cross the $Ox$ axis? Justify your answer.
* **(f)** Consider now that we impose the additional constraint $\phi = 2\theta$. Compute the natural frequency of oscillation of the system under the assumption of small angles.

*(Hint: The mechanical energy of an ideal harmonic oscillator of natural frequency $\omega_0$ and mass $m$ can be written as $\frac{1}{2}m(\dot{x}^2 + \omega_0^2 x^2)$)*.
