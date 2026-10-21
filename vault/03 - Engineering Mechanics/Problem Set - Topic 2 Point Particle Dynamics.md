---
title: "Problem Set - Topic 2: Point Particle Dynamics"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Verbatim Problem Statements"
language: "English"
tags:
  - problem-statements
  - point-particle-dynamics
---

# 📝 Topic 2: Point Particle Dynamics - Problem Statements

Official problem statements from the UC3M Aerospace Engineering problem collection (`Problems.pdf`, Chapter 1). These problems test Newton's second law, linear momentum, kinetic energy, work, conservative forces, potential energy, 1D energy landscapes, aerodynamic drag, and the simple pendulum.

> [!NOTE]
> **Status:** Verbatim problem statements transcribed faithfully from official department exams and problem sets.
> 
> [!SUCCESS] Complete Analytical Solutions Ready
> All 10 problems have full, step-by-step pedagogical solutions developed in: [[Solution Set - Topic 2 Point Particle Dynamics]].

---

## 📌 Problem 10: Conservative Force and Potential I

A particle of mass $m$ moves under a force $\mathbf{F} = -c x^3\mathbf{i}$, where $c$ is a positive constant. Find the potential energy function. If the particle starts from rest at $x = -a$, what is its velocity when it reaches $x = 0$? In the subsequent motion, where does it stop again?

---

## 📌 Problem 11: Conservative Force and Potential II

The potential energy function of a particle of mass $m$ is:

$$ V(x) = -\frac{c}{2}(x^2 - a^2)^2 $$

where $c$ and $a$ are positive constants. Sketch this function, and describe the possible types of motion in the three cases:

* **(a)** $E > 0$
* **(b)** $E < -\frac{ca^4}{2}$
* **(c)** $-\frac{ca^4}{2} < E < 0$

---

## 📌 Problem 12: Conservative Force and Potential III

A particle moving under a conservative force oscillates between $x_1$ and $x_2$. Show that the period of oscillation is:

$$ \tau = 2\int_{x_1}^{x_2} \sqrt{\frac{m}{2[V(x_2) - V(x)]}}\,dx $$

where $V(x)$ is the potential energy function. In particular, if $V(x) = \frac{1}{2}m\omega_0^2(x^2 - bx^4)$, show that the period for oscillations of amplitude $a$ is:

$$ \tau = \frac{2}{\omega_0}\int_{-a}^a \frac{dx}{\sqrt{a^2 - x^2}\sqrt{1 - b(a^2 + x^2)}} $$

---

## 📌 Problem 13: Conservative Force and Potential IV

A particle of mass $m$ moves along the $Ox$ axis under the potential:

$$ V(x) = mgx\left[\left(\frac{x}{a}\right)^2 - 3\right] $$

Compute the evolution of the particle as a function of time, when it is released from $x_0 = a$ with an initial velocity $v_0 = \sqrt{8ga}$ directed along the positive $Ox$ axis.

*(Tip: $\int \frac{dx}{(x+1)\sqrt{2-x}} = -\frac{2}{\sqrt{3}}\text{arctanh}\left(\sqrt{\frac{2-x}{3}}\right)$)*.

---

## 📌 Problem 14: Conservative Force and Potential V

A particle of mass $m$ is moving along the $Ox$ axis under the force $\mathbf{F}(x) = mK x e^{x/a}\mathbf{i}$, where $K$ and $a$ are known positive constants. The initial position of the particle is $x = a$ and the initial velocity is $\mathbf{v} = -v_0\mathbf{i}$. Describe the possible types of motion of the particle as a function of $v_0$.

---

## 📌 Problem 15: Stokes Drag and Terminal Velocity

The Stokes' law states that the magnitude of the drag force acting on a sphere of radius $r$ and velocity $v$ moving on a fluid at rest of dynamic viscosity $\mu$ is: $F(v) = 6\pi\mu rv$. Assuming the density of a vertically-falling sphere is twice the density of the fluid ($\rho_0$), and considering drag, the weight, and the buoyancy of the sphere, compute:

* **(a)** The terminal velocity of the sphere.
* **(b)** The evolution of the position as a function of time, if the sphere starts from rest.

Remember that the kinematic viscosity is defined as $\nu = \mu / \rho_0$.

---

## 📌 Problem 16: Drag on Falling Football

A football has frontal surface area $S$, mass $m$, and a drag coefficient $C_D$. It falls vertically through the air of density $\rho$. It is assumed that the forces acting on the ball are only gravity and drag. The drag can be modeled as: $D = \frac{1}{2}\rho v^2 S C_D$, with $v$ the speed of the ball. Compute its terminal speed and its position as a function of time.

You may find the following integrals useful:

$$ \int \frac{dx}{x_0^2 - x^2} = \frac{1}{x_0}\text{atanh}\left(\frac{x}{x_0}\right); \qquad \int \tanh x\,dx = \ln\cosh x $$

---

## 📌 Problem 17: Linear Central Force

A force attracts a heavy particle $M$ of mass $m$ to a point $O$. The attractive force is proportional to the mass of the particle and to the distance $OM$. The proportionality coefficient is $k^2$. The coordinate system $Oxyz$ has the origin at the centre of attraction $O$ and the axis $Oz$ is vertically oriented. Initially, the coordinates of $M$ are:

$$ (x_0, y_0, z_0) = \left(\frac{\sqrt{3}g}{k^2}, 0, 0\right) $$

and its initial velocity is:

$$ (\dot{x}_0, \dot{y}_0, \dot{z}_0) = \left(0, \frac{2g}{k}, 0\right) $$

* **(a)** Describe the motion of $M$, specifying clearly the shape of the path.
* **(b)** What is the velocity of the particle as a function of $t$?

---

## 📌 Problem 45: Vibrating Rotor (Unbalanced Turbojet)

To understand the vibrations that occur in a turbojet when the mass distribution of the rotor is slightly unbalanced, we can consider the turbojet as a rigid disk of mass $m$ that rotates at a fixed angular velocity $\omega$, with the center of mass $G$ being separated from the geometric center $C$ by a fixed distance [called $\ell$ in the figure]. An elastic restoring force (with constant $k$) tries to keep $C$ at its design position $O$. We call $x_0^G, y_0^G$ the Cartesian coordinates of $G$, and $x_0^C, y_0^C$ the Cartesian coordinates of $C$. Considering the weight of the disk negligible, write down the equation of the dynamics of $G$. Assuming that the homogeneous solution is damped over time and only the particular solution remains, write down the expression of $x_0^G(t)$ and $x_0^C(t)$. Can we affirm that $|\boldsymbol{OC}| > |\boldsymbol{OG}|$ if $\omega > \sqrt{k/m}$?

![[attachments/EM/T2-P45-figure.png]]
*Figure: Rotating disk of centre C with the centre of mass G at distance l, angle omega t from the x direction, spring k from O to C, axes Oxy Source: Problems.pdf, p. 31.*

---

## 📌 Problem 46: Bumpy Taxiway

An airplane is taxiing over a bumpy runway of vertical profile $y_1 = \sin(x)$ with a horizontal velocity $c$. The vertical motion of the airplane can be modeled as that of a heavy particle $P$ of mass $m$ supported on a landing gear of nominal length $L$ when unloaded. Consider that the landing gear has stiffness constant $k$ and negligible damping.

![[attachments/EM/T2-P46-figure.png]]
*Figure: Mass m on a spring k whose lower end follows the bumpy runway profile y1 = sin x Source: Problems.pdf, p. 31.*

* **(a)** At what taxiing speed is the system in resonance with the bumpy road?
* **(b)** Find the expression of the amplitude of the airplane oscillations when the taxiing velocity $c$ is very high. Hint: the expression depends on $c$.
* **(c)** Consider now that the landing gear has damping constant $\lambda$. How does the results above change? Consider the underdamped, critical, and overdamped cases. What value of $\lambda$ would you choose for this application and why? If the mass of the aircraft changes (e.g. more or less payload), does this affect your conclusion?
