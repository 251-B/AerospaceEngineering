---
title: "Problem Set - Topic 7: Rigid Body Momentum, Energy and Dynamics"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Problem Statements"
language: "English"
tags:
  - problems
  - topic-7
  - rigid-body-dynamics
---

# 📝 Topic 7: Rigid Body Momentum, Energy and Dynamics - Problem Statements

Problem statements of the rigid body section (section 2) of `Problems.pdf`, copied word for word; typing errors of the PDF are kept and marked "[sic]". Numbers are those of that section, written RB-NN. Course material: Lectures 9, 10 and 6; Notes.pdf, chapters 5, 11 and 12.

> [!NOTE]
> **Status:** statements transcribed from `Problems.pdf` (PDF page index in every figure caption). Official answers, where the PDF prints one: [[Problem Set - Rigid Body Official Key]]. Subject index: [[Engineering Mechanics MOC]].

- **Group C:** Linear momentum, angular momentum and kinetic energy.
- **Group D:** Planar and 3D rigid body dynamics, equilibrium and linearized oscillations.

| Problem | Group | Key (PDF page) | Title |
| :---: | :---: | :---: | :--- |
| RB-06 | C | p. 78 | Blade Runner (Spinner) |
| RB-07 | C | p. 78 | One problem to rule them all (One Ring) |
| RB-08 | D | p. 78 | Triangle with spring and vertical constraint |
| RB-09 | D | none | Rectangle with spring hanging from a corner |
| RB-10 | D | p. 79 | Firedoor motion |
| RB-24 | D | none | Lagrange's top (Heavy axisymmetric pegtop) |
| RB-25 | D | p. 80 | Cylinder hanging from the ceiling by two strings |
| RB-38 | D | none | Disk on hanging axle |

---

## 📌 Problem RB-06: Blade Runner (Spinner)

Los Angeles 2019. Deckard is a special policeman (a blade runner) specialized in “retiring” Nexus 6 replicants. He goes around in a spinner, his flying car. We want to analyze the flying motion of the spinner with respect to an inertial reference frame $S_0 : \{O; B_0\}$ with $B_0 : \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ as shown in the figure. We are going to consider the spinner as a rigid body. A body-fixed reference frame $S_B : \{G; B_B\}$ with $B_B : \{\mathbf{i}_B, \mathbf{j}_B, \mathbf{k}_B\}$ is also defined. In the instant considered,

* the center of mass $G$ and the axes $Gx_B$ and $Gy_B$ are contained in the plane $Oxy$,
* the distance between $G$ and $O$ is $3L/2$, where $L$ is the length of the spinner as indicated in the figure,
* the angle between the axis $Ox$ and $Gx_B$ is $45^\circ$
* the velocity of $G$ is $\boldsymbol{v}_0^G = 3\sqrt{2}\Omega L(-\boldsymbol{i} + \boldsymbol{j})/4$,
* the velocity of point $A$ of the body is $\boldsymbol{v}_0^A = \Omega L(\boldsymbol{i}_B - 8\boldsymbol{j}_B + \sqrt{2}\boldsymbol{k}_B)/4$, where the position vector of $A$ is given by $\boldsymbol{r}_B^A = (2\boldsymbol{i}_B + \boldsymbol{j}_B)L/4$,
* we also know that $\boldsymbol{v}_0^G \cdot \boldsymbol{\omega}_{B0} = 0$, where $\boldsymbol{\omega}_{B0}$ is the angular velocity of the spinner.

The mass of the spinner is $M$. The inertia tensor about $G$ is

$$ \overline{\overline{I}}_G = ML^2 \begin{bmatrix} B & 0 & E \\ 0 & C & F \\ E & F & D \end{bmatrix}_b , $$

where $B$, $C$, $D$, $E$ and $F$ are known constants. Compute

* **(a)** The instantaneous axis of rotation with respect to $S_0$.
* **(b)** The kinetic energy of the spinner with respect to $S_0$.
* **(c)** The angular momentum of the spinner about $G$ with respect to $S_0$.
* **(d)** The angular momentum of the spinner about $A$ with respect to $S_0$.

![[attachments/EM/T7-RB06-figure.png]]
*Figure: Spinner with the inertial frame $S_0$ (axes $x$, $y$, $z$, origin $O$) and the body frame $S_B$ (axes $x_B$, $y_B$, $z_B$, origin $G$) in an oblique view, and its top and side views with the points $G$ and $A$ and the dimensions $L$ and $L/2$. Source: Problems.pdf, p. 40.*

---

## 📌 Problem RB-07: One problem to rule them all (One Ring)

We want to analyze the motion of the ring with respect to an inertial reference frame $S_0 : \{O; B_0\}$ (with unit vectors $\boldsymbol{i}$, $\boldsymbol{j}$ and $\boldsymbol{k}$) as shown in the figure. We are going to consider the ring as a rigid body, with a body-fixed reference frame $S_B : \{G; B_B\}$ (with unit vectors $\boldsymbol{i}_B$, $\boldsymbol{j}_B$ and $\boldsymbol{k}_B$) attached to it. In the instant considered,

* the ring is rolling without slipping.
* the centre of mass $G$ and the axes $Gx_B$ and $Gz_B$ are contained in the plane $Oxz$
* the angle between the axis $Ox$ and $Gx_B$ is $45^\circ$
* the contact point of the ring with the plane $Oxy$ is $C$. The coordinates of $C$ in the body-fixed reference frame are $R(-1, 0, -19)/20$.
* the velocity of $G$ is $\boldsymbol{v}_G = \Omega R \left(-\boldsymbol{i} + \frac{\sqrt{5}}{2}\boldsymbol{j} - \frac{9}{10}\boldsymbol{k}\right)$
* the angular velocity fulfills the condition $\boldsymbol{\omega} \cdot \boldsymbol{i}_B = \boldsymbol{\omega} \cdot \boldsymbol{k}_B$

The mass of the ring is $M$ and the inertia tensor with respect to the reference frame $S_B$ is approximately given by

$$ \overline{\overline{I}}_G = MR^2 \begin{bmatrix} B & 0 & 0 \\ 0 & D & 0 \\ 0 & 0 & D \end{bmatrix} $$

where $B$, and $D$ are considered as constants.

* **(a)** Compute the instantaneous axis of rotation
* **(b)** Compute the kinetic energy of the ring and the angular momentum of the ring with respect to $G$ as seen from $S_0$
* **(c)** Assume Mordor is located at the origin and attracts the ring with a force. The force applied at each differential mass is proportional to the differential mass and the distance, with proportionality constant being $\beta$. Compute the force and the moment with respect to $G$ due to the presence of Mordor.
* **(d)** If we know that $B = 2D$ and the moment of inertia with respect to $G$ is $I_G = MR^2$, solve for $B$ and $D$.

*...One Ring to rule them all*

![[attachments/EM/T7-RB07-figure.png]]
*Figure: Ring with the inertial frame $S_0$ (axes $x$, $y$, $z$) and the body frame $S_B$ (axes $x_B$, $y_B$, $z_B$, centre $G$), with the contact point $C$, shown in an oblique view and in side and top views. Source: Problems.pdf, p. 41.*

---

## 📌 Problem RB-08: Triangle with spring and vertical constraint

The planar equilateral triangle has side length $a$ and uniform mass $m$. It moves in the vertical plane $Oxy$ of the inertial frame $S_0 : \{O, B_0\}$ with $B_0 : \{\boldsymbol{i}, \boldsymbol{j}, \boldsymbol{k}\}$. The vertex $A$ of the triangle is connect [sic] to $O$ by a spring with constant $k$ and zero nominal length. The center of mass $G$ of the triangle is constrained to move along the vertical line $x = 2a$ without friction.

* **(a)** Determine the position of $G$ with respect to the coordinate system $x_1y_1$.
* **(b)** Determine the moment of inertia with respect to point $G$.
* **(c)** Write down the equations of motion for the triangle.
* **(d)** At time $t = 0$, the side $BC$ of the triangle coincides with the axis $Ox$, the vertex $A$ is on the line $x = 2a$ with $y > 0$, and the velocity of $A$ is $\boldsymbol{v}_0^A = u_0\boldsymbol{i} + v_0\boldsymbol{j}$.
  * **i.** Obtain the required initial conditions for the equations of the motion.
  * **ii.** Determine also the instantaneous axis of rotation at $t = 0$.
* **(e)** Now, we consider a different situation. The triangle is in the equilibrium position and at rest, with the orientation $\theta = \pi/4$. Determine the value of the spring constant $k$, the position of $G$, and the reaction force.
* **(f)** In the equilibrium position computed before, we now fix the position of $G$ and apply a small perturbation to the orientation of the triangle, such that $\theta = \pi/4 + \phi$ and $\phi \ll 1$. Determine the oscillation frequency of the triangle with respect to the equilibrium position.

![[attachments/EM/T7-RB08-figure.png]]
*Figure: Equilateral triangle with vertices $A$, $B$, $C$ and centre $G$ in its body frame and with the frame $x_1y_1$ (left), and the triangle in the vertical plane with the spring $k$ from $O$, the vertical line $x = 2a$, the angle $\theta$ and the gravity $g$ (right). Source: Problems.pdf, p. 42.*

---

## 📌 Problem RB-09: Rectangle with spring hanging from a corner

We consider the planar motion in a vertical plane $OXY$ of a heavy homogeneous rectangle of mass $m$, length $a$ and width $b = \sqrt{3}a$. The motion of the rectangle is influenced by the spring of constant $k$ which connects the origin of the inertial reference frame $O_1X_1Y_1$ to the vertex $A$ of the rectangle, as shown in the figure. In addition, the vertex $C$ of the rectangle is constrained to move along the horizontal line $y = 5a/4$.

* **(a)** Determine the moment of inertia with respect to the center of mass of the rectangle $G$.
* **(b)** If at time $t = 0$, the side $BC$ of the rectangle is located on the axis $O_1Y_1$, the vertex $A$ has a positive $x_1$ component and the velocity of the vertex $A$ is $\boldsymbol{v}_A = u_0\boldsymbol{i}_1 + v_0\boldsymbol{j}_1$ (where $\boldsymbol{i}_1,\boldsymbol{j}_1$ are the unit vectors along the axes $O_1X_1$ and $O_1Y_1$).
  * Write down the equations of motion for the rectangle.
  * Specify the initial conditions that need to be imposed on the previous equations in order to completely specify the problem. Determine also the instantaneous axis of rotation at $t = 0$.
* **(c)** If at time $t = 0$, the rectangle is at rest, the value of the angle is $\theta = \pi/3$ and we know that the body is in equilibrium. Determine the position of the centre of mass and the reaction force.
* **(d)** In the equilibrium position computed before, we now do the following actions:
  * **i.** fix the position of $G$
  * **ii.** release the vertex $C$ from the constraint
  * **iii.** apply a small perturbation to the orientation of the rectangle. Such that $\theta = \pi/3 + \phi$ and $\phi \ll 1$.

Determine the frequency of oscillation of the rectangle with respect to the equilibrium position.

![[attachments/EM/T7-RB09-figure.png]]
*Figure: Rectangle $ABCD$ with its centre $G$ and the body axes $x_B$, $y_B$ (left), and the rectangle in the inertial frame $O_1X_1Y_1$ with the spring from $O_1$ to $A$, the vertex $C$ on the horizontal line $y = 5a/4$, the angle $\theta$ and the gravity $g$ (right). Source: Problems.pdf, p. 43.*

---

## 📌 Problem RB-10: Firedoor motion

A heavy fire door is a rectangular plate with mass $m$. The door is suspended from the ceiling by two rigid links with negligible mass. The door is also tied to the wall by a cable. In case of an emergency, this cable is severed and the door swings under the restraint of the rigid links. Derive the first-order differential equation of motion that governs the angle of inclination $\theta$ of the rigid links. Also derive the expressions for the forces exerted by the links on the plate.

![[attachments/EM/T7-RB10-figure.png]]
*Figure: Fire door of height $h$ and width $b$ hung from the ceiling by two rigid links of length $L$ at the points $A$ and $B$, with the angle $\theta$ measured from the vertical, and the cable to the wall at the right. Source: Problems.pdf, p. 44.*

---

## 📌 Problem RB-24: Lagrange's top (Heavy axisymmetric pegtop)

In this problem, we are going to study the motion of a heavy, axisymmetric pegtop of mass $m$. We will assume that during the precession, nutation and spin of the pegtop, the vertex $O$ of the pegtop remains fixed at the origin of the inertial reference frame $Oxyz$. The distance $\ell$ between $O$ and the center of mass of the pegtop $G$ is known. Also the moment of inertia tensor with respect to the principal axes of inertia $Gx_By_Bz_B$ is known, and given by

$$ \overline{\overline{I}}_G = m\ell^2 \begin{bmatrix} A & 0 & 0 \\ 0 & A & 0 \\ 0 & 0 & B \end{bmatrix} . $$

The orientation of the body fixed reference frame $Gx_By_Bz_B$ with respect to the inertial reference frame $Oxyz$ is given by three sequential rotations. First, a rotation $\psi$ with respect to the axis $Oz$, (leading to an intermediate reference frame $Ox_1y_1z_1$). Second, a rotation $\theta$ with respect to the axis $Ox_1$, (leading to an intermediate reference frame $Ox_2y_2z_2$). And finally a rotation $\varphi$ with respect to the axis $Gz_2$, leading to $Gx_By_Bz_B$. The initial condition is $\psi = 0$, $\theta = \pi/6$, $\varphi = 0$, $\dot{\psi} = 0$, $\dot{\theta} = \Omega_1$, $\dot{\varphi} = \Omega_2$, where $\Omega_1$ and $\Omega_2$ are known constants.

* **(a)** Compute the inertia tensor, $\overline{\overline{I}}_O$ with respect to a reference frame, parallel to $Gx_By_Bz_B$ with origin in $O$, i.e. $Ox_By_Bz_B$.
* **(b)** Compute the angular momentum of the peg-top with respect to $O$ as a function of the variables of the problem at an arbitrary instant of time.
* **(c)** Compute the kinetic energy of the peg-top as a function of the variables of the problem.
* **(d)** Is the mechanical energy of the system conserved? Why?
* **(e)** Is there any conserved component of the angular momentum with respect to $O$? Why?
* **(f)** Obtain three **first order** ordinary differential equations that would allow to obtain the values of $\psi$, $\theta$ and $\varphi$ as a function of time.
* **(g)** Assuming that $\psi(t)$, $\theta(t)$ and $\varphi(t)$ are known, explain how you would obtain the value of the reaction at $O$. You do not need to obtain the final result, but the procedure needs to be sufficiently clear.

![[attachments/EM/T7-RB24-figure.png]]
*Figure: Heavy axisymmetric pegtop with fixed point $O$ and centre of mass $G$ on the symmetry axis $Gz_2 \equiv Gz_B$, the Euler angles $\psi$ (about $Oz \equiv Oz_1$) and $\theta$ (between $z$ and $z_2$), the frames $Oxyz$, $Ox_1y_1z_1$ and $Ox_2y_2z_2$, and the gravity $g$. Source: Problems.pdf, p. 54.*

---

## 📌 Problem RB-25: Cylinder hanging from the ceiling by two strings

A heavy, homogeneous cylinder of mass $m$, length $2l$, and radius $l/3$ is hanging from the ceiling from points $A$ and $B$, supported by two massless strings of length $l$ each. The distance between $A$ and $B$ is $3l$. The strings are always straight and connected to the cylinder at points $C$ and $D$ as shown in the figure. We call $G$ the center of mass of the cylinder. In order to describe the motion of the cylinder, we define the inertial reference frame $S_0 : \{A, B_0\}$ with $B_0 : \{\boldsymbol{i}, \boldsymbol{j}, \boldsymbol{k}\}$, as $Axyz$ in the figure. The body-fixed reference frame $S_B : \{G, B_B\}$ with $B_B : \{\boldsymbol{i}_B, \boldsymbol{j}_B, \boldsymbol{k}_B\}$ is defined as $Gx_By_Bz_B$ in the figure. We denote the position of the center of mass of the cylinder $G$ as $\boldsymbol{r}_0^G = x_G\boldsymbol{i} + y_G\boldsymbol{j} + z_G\boldsymbol{k}$. We define $\beta$, $\theta$, and $\phi$, which are 3-2-1 Euler angles of the cylinder with respect to $S_0$, positive in the direction shown in the figure ($Gx_0$ is parallel to $Ax$). Observe that, for clarity, the figure only displays part of the auxiliary axes of these rotations. Lastly, the tensor of inertia of the cylinder about $G$ is given in terms of two known constants ($\lambda$, $\mu$) :

$$ \overline{\overline{I}}_G = ml^2 \begin{bmatrix} \lambda & 0 & 0 \\ 0 & \mu & 0 \\ 0 & 0 & \mu \end{bmatrix}_{BB} $$

* **(a)** What is the degree of freedom of this problem? What is the total number of *unknowns* in the problem? How many equations are needed to solve the problem?
* **(b)** Write down the position vectors of $C$ and $D$ as a function of the variables of the problem.
* **(c)** Calculate the angular velocity and angular acceleration of the body as a function of the variables of the problem and their derivatives.
* **(d)** Write down the equation of the constraints imposed by the strings.
* **(e)** Write down the expressions of all forces and moments of forces at $G$ acting on the cylinder.
* **(f)** Write down the equations of motion of the cylinder (plus any other necessary equations) that if integrated, would yield the evolution in time of these unknowns. Note that you do not need to integrate them.
* **(g)** Is the mechanical energy of the cylinder conserved in this problem? If so, write down its equation of conservation of energy. Is this an independent equation with respect to the set of equations of the previous question?

![[attachments/EM/T7-RB25-figure.png]]
*Figure: Cylinder hanging from $A$ and $B$ by two strings attached at $C$ and $D$, with the inertial frame $Axyz$, the body frame $Gx_By_Bz_B$, the Euler angles $\beta$, $\theta$, $\phi$ and the gravity $g$. Source: Problems.pdf, p. 55.*

---

## 📌 Problem RB-38: Disk on hanging axle

We consider a heavy, homogeneous, axisymmetric rigid body b of mass $m$. The body point A hangs from a fixed point O on the ceiling with a massless, inextensible string of length $\ell$, as shown in the figure. We know that the string always remains tense. The center of mass G of b is located a distance $\ell$ from A, and is constrained to move along the vertical that passes through O. We define the inertial reference frame $S_0$ with center on O. We introduce the angle $\psi$ between the OAG plane and the $Oy_0z_0$ plane. We define the the [sic] auxiliary reference frame $S_1$ as shown in the figure, so that the segment AG is contained in the $Gy_1z_1$ plane. We introduce the angle $\theta$ between the string OA and the axis of the body AG, and we define the auxiliary reference frame $S_2$ so that $\boldsymbol{j}_2$ points in the AG direction. Finally, we define the body-fixed reference frame $S_b$ and the angle $\varphi$, which represents the spin of the rigid body about the $\boldsymbol{j}_2$ vector, such that when $\varphi = 0$, $S_b$ coincides with $S_2$. The tensor of inertia of the rigid body about G expressed in the basis of $S_b$ is:

$$ \overline{\overline{I}}_G = \begin{bmatrix} A & 0 & 0 \\ 0 & B & 0 \\ 0 & 0 & A \end{bmatrix}_b , $$

where $A = 3B = 6m\ell^2$.

* **(a)** How many configuration degrees of freedom does this system have? Justify your answer.
* **(b)** Give the expressions of the unit vectors of $S_1$ in terms of those of $S_0$, the unit vectors of $S_2$ in terms of those of $S_1$, and the unit vectors of $S_b$ in terms of those of $S_2$.
* **(c)** Find the general expression for the position, velocity, and acceleration of G, and the angular velocity and acceleration of b, with respect to $S_0$, in terms of $\psi$, $\theta$ and their derivatives.
* **(d)** Identify all the forces/torques acting on b and reduce them to a single resultant force and a single resultant torque at G.
* **(e)** Write down a system of (differential) equations that allows solving for the time evolution of all unknowns in the problem.
* **(f)** What is the condition that $\dot{\psi}$ and $\dot{\varphi}$ must satisfy for the nutation angle $\theta$ to be constant in time?
* **(g)** Find three first integrals of motion (i.e., equations that do not depend on second derivatives). Justify your procedure.

![[attachments/EM/T7-RB38-figure.png]]
*Figure: Axisymmetric body b hanging from $O$ by the string $OA$ of length $\ell$, with the centre of mass $G$ on the vertical through $O$, the frames $S_0$ ($\boldsymbol{i}_0$, $\boldsymbol{j}_0$, $\boldsymbol{k}_0$), $S_1$, $S_2$ and $S_b$, the gravity $\boldsymbol{g}$ and the angles $\psi$, $\theta$ and $\varphi$. Source: Problems.pdf, p. 67.*

---
