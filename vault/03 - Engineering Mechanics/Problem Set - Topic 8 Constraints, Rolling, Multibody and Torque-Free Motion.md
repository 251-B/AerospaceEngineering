---
title: "Problem Set - Topic 8: Constraints, Rolling, Multibody and Torque-Free Motion"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Problem Statements"
language: "English"
tags:
  - problems
  - topic-8
  - rolling-multibody
---

# 📝 Topic 8: Constraints, Rolling, Multibody and Torque-Free Motion - Problem Statements

Problem statements of the rigid body section (section 2) of `Problems.pdf`, copied word for word; typing errors of the PDF are kept and marked "[sic]". Numbers are those of that section, written RB-NN. Course material: Notes.pdf, chapters 13, 14 and 15.

> [!NOTE]
> **Status:** statements transcribed from `Problems.pdf` (PDF page index in every figure caption). Official answers, where the PDF prints one: [[Problem Set - Rigid Body Official Key]]. Subject index: [[Engineering Mechanics MOC]].

- **Group E:** Rolling with and without slip, unilateral constraints and lift-off.
- **Group F:** Multibody systems and exploded views.
- **Group G:** Torque-free motion, Poinsot's construction and gyroscopes.

| Problem | Group | Key (PDF page) | Title |
| :---: | :---: | :---: | :--- |
| RB-12 | E | none | Box rolling on cylinder |
| RB-13 | E | p. 79 | Rolling disk with cavity |
| RB-14 | E | none | Rocking semicircumference |
| RB-15 | E | none | Rocking hollow hemisphere |
| RB-16 | E | none | Sphere on inclined plane with central attraction |
| RB-18 | E | p. 79 | Bowling ball (Jesús Quintana) |
| RB-19 | E | none | Sphere on the floor with spring |
| RB-22 | E | none | Ball with bar on inclined plane |
| RB-23 | E | none | Rectangle with a hole on knob |
| RB-28 | E | none | Euler's disk |
| RB-33 | E | p. 81 | Axle with two wheels |
| RB-37 | E | none | Disk rolling without slip over a bigger cylinder |
| RB-39 | E | none | Yo-yo |
| RB-40 | E | none | Disk on parabolic groove |
| RB-41 | E | none | Sail sledge |
| RB-17 | F | p. 79 | Constrained pizza cutter (Fork and disc) |
| RB-20 | F | p. 80 | Pioneer III spacecraft (Yo-yo de-spin) |
| RB-21 | F | none | Reaction wheel spacecraft attitude control |
| RB-26 | F | pp. 80-81 | Unbalanced planetary bearings |
| RB-27 | F | p. 81 | Rectangle with weight, pulleys, and string |
| RB-29 | F | none | Disk-bar train |
| RB-31 | F | none | Ball bearing between cylinder and cone |
| RB-36 | F | p. 81 | Mars rolling rover |
| RB-42 | F | none | Gyro on inclined plane |
| RB-30 | G | p. 81 | Free spinning asteroid (Poinsot's construction) |
| RB-32 | G | none | Rate gyro on aircraft |

---

## 📌 Problem RB-12: Box rolling on cylinder

The homogeneous box, whose mass is $m$, is placed horizontally on the semicylindrical surface, such that contact is below the centroid $G$. Assuming that the box does not slip, derive the differential equation of motion governing the angle $\varphi$ by which the box rotates away from horizontal.

![[attachments/EM/T8-RB12-figure.png]]
*Figure: Box of width $b$ and height $h$ resting on a semicylindrical surface of radius $R$, with the centroid $G$ inside the box Source: Problems.pdf, p. 44.*

---

## 📌 Problem RB-13: Rolling disk with cavity

A heavy homogeneous sheet is in the form of a disc that has a circular hole with diameter equal to the disc radius $R$, as shown in the figure. The mass of the sheet is $m$. The sheet is in contact with a horizontal rough straight line with friction coefficient $\mu$. Initially, the vector from the disk geometrical center $O$ to the center of the hole is in the horizontal direction, as shown in the figure. The initial angular velocity of the sheet is $\omega$ and the initial velocity of $O$ is $\omega R$. In the subsequent motion, the sheet can roll with or without slip or even can lose contact with the line (assuming unilateral constraint).

* **(a)** Determine the position of the center of mass.
* **(b)** Determine the moment of inertia about $O$.
* **(c)** Determine the moment of inertia about the center of mass.
* **(d)** Determine the initial velocity of the disk point that is in contact with the line.
* **(e)** Reduce the motion to quadratures (i.e., integrals) for $\mu = 0$.
* **(f)** Reduce the motion to quadratures for $\mu \to \infty$.

![[attachments/EM/T8-RB13-figure.png]]
*Figure: Circular sheet of radius $R$ with a circular hole of diameter $R$ in contact with a horizontal line; the arrow marks the initial velocity $\omega R$ of $O$ Source: Problems.pdf, p. 45.*

(From Prieto's book)

---

## 📌 Problem RB-14: Rocking semicircumference

A thin 2D semi-circular arc of mass $M$ and radius $R_0$ rests on a flat plane. It is displaced through an angle $\theta_0$ and held at rest. It maintains rolling contact with the plane. (i.e. it rolls without slipping.). The location of the center of mass for the arc is $R_G = 2R_0/\pi$.

* What is the moment of inertia of the semicircular arc about its center, $I_C$ ?
* Using the parallel axis theorem, find the moment of inertia about the center of mass, $I_G$.
* What is the displacement of the point of contact, $X_C$? As it rolls, the center of mass displaces in both the horizontal and vertical directions.
* What is the vertical displacement of the center of mass, $y_{CM}$ ?
* What is the horizontal displacement of the center of mass $x_{CM}$ ?
* What is the potential energy in the displaced $\theta = \theta_0$ position with the arc at rest? Now the arc is released and returns to and past $\theta = 0$ in an oscillatory motion.
* What is the total kinetic energy in both translation and rotation as the arc passes through $\theta = 0$.

![[attachments/EM/T8-RB14-figure.png]]
*Figure: Semi-circular arc $M$ of radius $R_0$ rolling on a flat plane, with the centre $C$, the centre of mass $G$ at distance $R_G$ from $C$, the angle $\theta_0$ and the displacement $X_C$ of the contact point Source: Problems.pdf, p. 45.*

---

## 📌 Problem RB-15: Rocking hollow hemisphere

An empty homegeneous [sic] semi-sphere of mass $m$, radius $a$ and negligible thickness is moving on a smooth horizontal plane. An auxiliar [sic] reference frame $Gxyz$ can be defined in the following way: the $Gz$ axis is the axis of revolution of the semi-sphere and is oriented towards the edge of the semi-sphere; the $Gx$ is always parallel to the plane $O_1x_1y_1$ and perpendicular to $Gz$; and finally $Gy$ is orthogonal to $Gz$ and $Gx$, contituting [sic] a right-handed reference system. The position of the sphere is determined by five parameters: the coordinates $\xi$, $\eta$ of the projection of $G$ on the plane $O_1x_1y_1$; the angle $\psi$ between $Gx$ and $O_1x_1$; the angle $\theta$ between $Gz$ and $O_1z_1$; and the angle $\varphi$ of the rotation of the semi-sphere about the $Gz$ axis.

* **(a)** Compute the inertia tensor of the semi-sphere with respect to its center $O$ and a set of axis parallel to $Gxyz$. It can be deduced from symmetry considerations, knowing that the moment of inertia of a spherical shell of radius $R$ and mass $M$ with respect an axis that passes through its center is $I = 2MR^2/3$.
* **(b)** Determine the position of the center of mass of the semi-sphere.
* **(c)** Determine the inertia tensor at $G$
* **(d)** Determine the angular velocity of the semi-sphere expressed as a function of $\psi,\theta,\varphi$ and its time derivatives.
* **(e)** Determine the kinetic energy of the semi-sphere as a function of the parameters that determine its position and their time derivatives.
* **(f)** Write down and integrate the linear momentum equation (a) with respect to the axis $O_1x_1$ and $O_1y_1$
* **(g)** Write down and compute the first integral (b) of the angular momentum equation with respect to the $Gz$ axis.
* **(h)** Write down and compute the first integral (c) of the angular momentum equation with respect to the vertical along $G$.
* **(i)** Write down and get a first integral (d) from the energy equation.

![[attachments/EM/T8-RB15-figure.png]]
*Figure: Semi-sphere with the auxiliary frame $Gxyz$ and the fixed frame $O_1x_1y_1z_1$, with the centre $O$ and the centre of mass $G$ Source: Problems.pdf, p. 46.*

---

## 📌 Problem RB-16: Sphere on inclined plane with central attraction

A homogeneous sphere of mass $m$ and radius $R$, rolls without slipping on a fixed plane. The angle between this plane and the horizontal plane is equal to $\alpha$. The sphere is subject to the action of gravity and an attraction which is directed towards a point of the plane $O$, and it is proportional to the mass of the sphere and the distance to $O$. Analyze the motion of the sphere and compute the reactions on the plane.

---

## 📌 Problem RB-18: Bowling ball (Jesús Quintana)

A bowling player, Jesús Quintana, is obsessed with the bowling league semifinals. In order to do the best possible throw, he decides to analyze the motion of the bowling ball along the lane. The bowling ball is modeled as a heavy sphere of mass $M$ and radius $a$. The inertial frame $S_0 : \{O, B_0\}$ with $B_0 : \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ is defined as $Oxyz$ in the figure. The lane contains in the plane $Oxy$, with width $W$, length $l$, and friction coefficient $\mu$. The projection of the center of mass $G$ on $Oxy$ plane is given by the coordinates $x_G$ and $y_G$. The orientation of the ball is given by three Euler angles $\psi$, $\theta$, and $\phi$, with the order of rotation being $3-2-3$. After the second simple rotation, the $Gz_2$ axis of $S_2 : \{G, B_2\}$ is in the direction from $G$ to $A$ ($A$ is a point on the surface of the ball at which one of the holes is drilled, as shown in the figure).

![[attachments/EM/T8-RB18-figure.png]]
*Figure: Sphere with the axes $x_2$, $y_2$, $z_2$ at $G$, the point $A$ and the inertial axes $x$, $y$, $z$ at $O$, and the lane seen from above with the holes of the ball. Source: Problems.pdf, p. 48.*

* **(a)** For the condition of rolling with slip: determine the degree of freedom and the number of constraints; identify the necessary variables of the problem.
* **(b)** For the condition of rolling without slip: determine the degree of freedom and the number of constraints; identify the necessary variables of the problem.
* **(c)** Express the angular momentum of the ball about $G$, with respect to $S_0$, as function of the variables of the problem.
* **(d)** Express force and torque as function of the variables of the problem.
* **(e)** For rolling with slip, obtain the set of ordinary differential equations and algebraic equations to solve the motion.
* **(f)** For rolling without slip, reduce the problem to quadratures (i.e., integrals). What is the shape of the trajectory of $G$?
* **(g)** If Jesús Quintana throws the ball with the following initial conditions:

$$x_G(t = 0) = y_G(t = 0) = 0 ,$$

$$\dot x_G(t = 0) = \dot x_{G0} ,$$

$$\dot y_G(t = 0) = 0 ,$$

$$\psi(t = 0) = \theta(t = 0) = \phi(t = 0) = 0 ,$$

$$\dot\psi(t = 0) = \dot\phi(t = 0) = 0 ,$$

$$\dot\theta(t = 0) = \frac{\dot x_{G0}}{4a} ,$$

solve the whole motion of the ball along the lane and determine: 1) when and where the ball starts to slip; 2) for $l = \dot x_{G0}^2/(10\mu g)$, what are the velocity and angular velocity of the ball when it hits the pocket.

---

## 📌 Problem RB-19: Sphere on the floor with spring

The motion of a heavy sphere of mass $M$ and radius $a$ is to be analyzed. The sphere rests on a horizontal plane $Oxy$. Moreover, a point $A$ on its surface is attached to a point $C$ on the vertical axis $Oz$ by means of a spring with zero natural length and constant $k$. The distance $|OC|$ is equal to $2a$. An intermediate reference frame is defined in the following way: axis $Gz_2$ is the direction of the line connecting the center of mass of the sphere, $G$, and $A$; axis $Gy_2$ perpendicular to both $Gz_2$ and $Oz$ and, therefore, parallel to the horizontal plane $Oxy$; and $Gx_2$ forming a right-handed reference frame. The position of the sphere is given by $\xi, \eta$, coordinates of the projection of $G$ on the horizontal plane $Oxy$, angle $\psi$ between $Gy_2$ and $Oy$, angle $\theta$ between $Gz_2$ and $Oz$, and angle $\varphi$ corresponding to the rotation of the sphere about the $Gz_2$ axis. Note that the difference between the $Gx_2y_2z_2$ reference frame and a truly body-fixed reference frame is a rotation $\varphi$ about the $Gz_2$ axis.

![[attachments/EM/T8-RB19-figure.png]]
*Figure: Sphere on the plane $Oxy$, with the spring from point $A$ on its surface to point $C$ on the axis $Oz$ at height $2a$, and the axes $x_2$, $y_2$, $z_2$ at $G$. Source: Problems.pdf, p. 49.*

* **(a)** Considering the horizontal plane a smooth surface:
  * **i.** express the angular momentum of the sphere with respect to $G$ as a function of the variables of the problem,
  * **ii.** express force and torque of the spring as a function of the variables of the problem,
  * **iii.** obtain the set of five ordinary differential equations to solve the motion,
  * **iv.** compute also the reaction as a function of the above-mentioned coordinates.
* **(b)** If the horizontal plane is rough, and assuming that the sphere rolls without slipping, indicate the changes on the set of required equations to solve the motion and the reactions.

---

## 📌 Problem RB-22: Ball with bar on inclined plane

A heavy, solid, homogeneous sphere of mass $M$ and radius $R$ moves on top of an inclined plane that forms an angle $\gamma$ with the horizontal. The sphere is always in contact with the plane. A stiff rod of negligible mass traverses the sphere through a small diametral perforation. The sphere can slide along and rotate about the rod freely, without any friction. The interaction between the rod and the sphere can be reduced to a resultant force and a resultant torque with respect to the center of mass of the sphere, $G$. These are unknown reactions until the problem is solved. One end of the rod is fixed at point $O$ of the inclined plane. The rod is free to turn in any direction but it does not rotate along its longitudinal axis.

To study the motion of the sphere, we define the inertial reference frame $S\{Oxyz\}$ with origin at $O$, the $x$ axis pointing downward along the maximum slope line of the plane, and the $z$ axis pointing upward perpendicular to the plane. We also define an auxiliary rotating reference frame $S_2\{Ox_2y_2z_2\}$, where $x_2$ always contains the point $P$ of contact of the sphere with the plane, and $z_2 \equiv z$. In order to describe the state of the system, we will use the angle $\theta$ between $x$ and $x_2$, the distance $d = |\overline{OP}|$, and the rotation angle $\phi$ of the sphere about the rod. For convenience, we also define the angle $\beta$ between the plane and the rod. Note that $\tan \beta = R/d$.

![[attachments/EM/T8-RB22-figure.png]]
*Figure: Heavy sphere on the inclined plane with the rod through its diametral perforation, the axes $x$, $y$, $z$ at $O$, the auxiliary axes $x_2$, $y_2$, the point $P$ of contact, the distance $d$, the angles $\theta$, $\beta$, $\phi$, the inclination $\gamma$ and the gravity $g$. Source: Problems.pdf, p. 52.*

You are asked to:

* **(a)** Choose the minimum number of variables (linear or angular coordinates) in order to fully determine the position and orientation of the sphere.
* **(b)** Write the general expression for the angular velocity and angular acceleration of the sphere ($\boldsymbol\omega$ and $\boldsymbol\alpha$), and the velocity and acceleration of $G$ ($\mathbf v_G$ and $\mathbf a_G$), as a function of $\theta$, $d$, $\phi$ and their derivatives.

Consider first that the friction of the sphere with the inclined plane is infinite, so that it cannot slip with respect to the plane.

* **(c)** Relate the velocity of the center of mass $G$ and the velocity of $P$, and use this to express the time derivatives $\dot d$ and $\dot\phi$ in terms of $\dot\theta$ and the angle $\beta$ formed by the rod with the plane.
* **(d)** Identify all the components of reaction forces and reaction torques acting on the rod alone. Using the balance of forces and torques on the rod, express all reaction forces and torques as a function of only two force components.
* **(e)** Identify all the components of forces and torques acting on the sphere, and reduce them to a sum of forces and a sum of torques on $G$ in terms of the unit vectors of $S_2$.
* **(f)** Obtain a closed set of six differential equations that would provide the evolution of $\theta$ and the 5 unknowns mentioned in the previous question. Note that you do not need to solve any of these equations.
* **(g)** If the system is in equilibrium when $\theta = 0$, then compute the reaction force between the rod and the sphere. Compute also the normal reaction and the friction force between the sphere and the inclined plane.
* **(h)** Linearize the equation obtained in the previous question and study the small oscillations about this equilibrium position when the system is released with zero initial velocity and a small nonzero value of $\theta \ll 1$. What is the frequency of these oscillations as a function of the parameters of the problem?

Consider now that the inclined plane is frictionless instead:

* **(i)** What changes in this case? Adapt the differential equations to the new case.
* **(j)** If the center of the sphere is initially located at $\mathbf r_{G0} = 2R\mathbf i + 3R\mathbf j + R\mathbf k$ and has an initial velocity $\mathbf v_{G0} = -\sqrt{Rg}(\mathbf i + \mathbf j)$, derive the initial conditions that are necessary to integrate the differential equations.

---

## 📌 Problem RB-23: Rectangle with a hole on knob

A heavy rectangular piece of wood of mass $m$ with a circular hole of radius $a_2$ is positioned on a fixed cylindrical knob of radius $a_1$ as shown below. We want to study the motion of the piece as a rigid body with respect to the inertial reference frame $Ox_1y_1z_1$ of the figure, assuming that the internal surface of the hole is always in contact with the knob at one point $I$ and that the piece rolls without slip over the knob. We call $\theta$ the angle between the longitudinal symmetry axis of the piece and the vertical, and we call $\phi$ the angle between the vector $OI$ and the vertical. Note that the two angles, $\theta$ and $\phi$, do not need to coincide in general. The dimensions of the problem satisfy $h = 2w$, $a_2 = w/\sqrt{2\pi}$, $a_1 = a_2/3$.

![[attachments/EM/T8-RB23-figure.png]]
*Figure: Front view of the rectangular piece of width $h$ and height $w$, with the circular hole of radius $a_2$ centred at $G$, and the axes $x_B$ and $y_B$. Source: Problems.pdf, p. 53.*

![[attachments/EM/T8-RB23-figure-b.png]]
*Figure: Piece on the knob of radius $a_1$ with the centre $O$, the contact point $I$, the inertial axes $x_1$, $y_1$, the body axes $x_B$, $y_B$, the centre $G$, the angles $\phi$ and $\theta$, and the gravity $g$. Source: Problems.pdf, p. 53.*

* **(a)** Compute $I_z$, the moment of inertia of the piece along $z_1$ at $G$, as a function of $m$ and $w$.
* **(b)** Write down the expressions of the velocity and acceleration of point $G$ as a function of $\phi$, $\theta$ and their time derivatives.
* **(c)** Find the relation between $\dot\phi$ and $\dot\theta$ imposing the no-slip condition at $I$.
* **(d)** Write down the equations of motion that yield $\phi$ and the reaction forces as functions of time. Note that you do not need to solve these equations.
* **(e)** From these equations, find the second-order differential equation for the evolution of $\phi$ that does not depend on the reaction forces.
* **(f)** If initially the wood piece is placed such that $G$ and $O$ are along the same vertical with $\theta_0 = 0$, the speed of $G$ is $|\mathbf v_{G0}| = 2wA/3$ [sic] and the piece is rotating counterclockwise, find the initial conditions that should be imposed to integrate the equation from the previous question for $\phi$.

---

## 📌 Problem RB-28: Euler's disk

A heavy, homogeneous coin b [sic] of mass $m$, radius $R$ and negligible thickness rolls on a horizontal plane at rest. The coin never takes off from the plane. We call $C$ the instantaneous contact point between the coin and the plane, and $G$ the center of mass of the coin. An inertial reference frame $S_0 = \{O; B_0\}$, with $O$ a point of the plane and $B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, is given. We define $r$ and $\psi$, which are the polar coordinates of $C$ in the $Ox_0y_0$ plane, and we call $S_1 = \{C; B_1\}$ the local reference frame associated to these polar coordinates. Lastly, we define $\beta$, $\theta$, $\delta$, which are a set of Euler angles of the coin with respect to $S_1$, positive in the direction shown in the figure (the coin is contained in the $Cy_2z_3$ plane).

![[attachments/EM/T8-RB28-figure.png]]
*Figure: Coin of radius $R$ rolling on the horizontal plane, with the inertial frame $O x_0 y_0 z_0$, the polar coordinates $r$ and $\psi$ of the contact point $C$, the local frame $S_1$ with axes $x_1$, $y_1$, $z_1$, the axes $x_2$, $y_2$, $z_3$, the Euler angles $\beta$, $\theta$, $\delta$, and gravity $\mathbf g$ Source: Problems.pdf, p. 58.*

* **(a)** How many degrees of freedom does the motion of the coin have, when the coin can roll and slip, and when the coin can roll but not slip?
* **(b)** Assuming that the coin can slip, obtain the general expression of $\boldsymbol\omega_{B0}$, $\boldsymbol\alpha_{B0}$, $\mathbf r_0^G$, $\mathbf v_0^G$, and $\mathbf a_0^G$ as a function of the coordinates of the problem and their time derivatives.

From this point on, consider that the friction coefficient between the coin and the plane is $\mu = \infty$, so the coin can roll but not slip:

* **(c)** Derive the scalar constraint equation(s) between the time derivatives of the coordinates of the problem that result from the no-slipping condition.
* **(d)** Identify and express all the external forces acting on the coin and the torque that they produce about $G$, introducing any necessary additional unknowns.
* **(e)** Write down the equations of motion of the coin in scalar form. Discuss whether any simple conservation law exists in the problem and justify your answer.
* **(f)** Finally, consider the particular case in which the coin moves with $\beta = 0$ and $\mathbf r_0^G = h\mathbf k_0$, where $h < R$ is constant. Give the value of $r$, $\theta$, and the reaction forces in this case. What is the relation between $h$ and $\dot\psi$? Comment on this result.

NOTE: The moment of inertia of a disk of mass $m$ and radius $R$ about its axis of rotational symmetry is $mR^2/2$.

---

## 📌 Problem RB-33: Axle with two wheels

Two thin, heavy, homogeneous wheels, of center $C_1$ and $C_2$ and radius $a$ and $2a$ respectively, are connected to each other with a massless, perpendicular axle of length $\sqrt{3}\,a$ forming a single rigid body $b$ as shown in the figure. The surface density of the wheel material is $\sigma$. We label the points of the rigid body that are in contact with the ground at each instant as $P$ and $Q$. The friction coefficient $\mu$ between the wheels and the ground is sufficiently large to ensure that the wheels always roll without slipping. We define the inertial reference frame $S_0$ and the auxiliary, rotating reference frame $S_1$ as shown. We also define other auxiliary vectors in the figure, $\mathbf i_2, \mathbf j_2, \mathbf i_3, \mathbf j_3$. The axis $Oy_1$ follows points $P$ and $Q$ as they move. The angle $\psi$ is measured between the axes $Ox_0$ and $Ox_1$. The angle $\phi$ is the angle that the wheels have rotated about the axle since the initial instant of time. Initially, $\psi = 0$, $\phi = 0$, and vector $\mathbf i_3$ points in the direction of $\mathbf{C_2Q}$.

Hint: Observe that the points $O$, $C_1$, and $C_2$ are always aligned. Remember to define all the vector bases that you use as a function of the vectors $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$, or other, already defined vectors.

![[attachments/EM/T8-RB33-figure.png]]
*Figure: Two wheels of radii $a$ and $2a$ with centres $C_1$ and $C_2$ joined by the axle, with the inertial basis $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0 \equiv \mathbf k_1$, the auxiliary vectors $\mathbf i_2 \equiv \mathbf i_1$, $\mathbf j_2 \equiv \mathbf j_3$, $\mathbf i_3$, $\mathbf j_1$, the contact points $P$ and $Q$, the angles $\psi$ and $\phi$, and gravity $\mathbf g$ Source: Problems.pdf, p. 63.*

* **(a)** Compute the total mass $m$, the distance between point $C_1$ on the axle and the center of mass $G$, and the tensor of inertia about $G$ of the object.

    **Hint**: the tensor of inertia of a thin, homogeneous disk of mass $M$ and radius $L$ about its center $C$, expressed in a vector basis **with the second unit vector perpendicular to the disk**, is given by:

    $$\mathcal I_C = \frac{ML^2}{4}\begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

    In the rest of the problem, you can name the resulting inertia tensor components with letters $A$, $B$, etc. and use them instead of their numerical expressions.

* **(b)** Write down the position, velocity, and acceleration of $G$, and the angular velocity and acceleration of the rigid body $b$, with respect to $S_0$.
* **(c)** Find out the kinematic relation between $\psi$ and $\phi$.
* **(d)** Identify and write down the general expression of all the forces acting on the rigid body, and reduce them to the resultant force and resultant moment of force about $G$.
* **(e)** Write down the equations of motion for the rigid body in the form of 6 scalar differential equations.
* **(f)** Find out the maximum value of $\dot\psi$ for which both wheels remain in contact with the ground.
* **(g)** Discuss whether the mechanical energy of the rigid body in $S_0$ is conserved in this problem. Note that you do not need to write down the equation of mechanical energy.
* **(h)** Is the system of equations of question (e) closed? Why, or why not?

---

## 📌 Problem RB-37: Disk rolling without slip over a bigger cylinder

A homogeneous, heavy disk b of mass $m$, radius $R$, and center $G$ rolls without slip on a stationary cylinder of radius $3R$ and center $O$. We call $C$ the instantaneous point of contact between the two. We assume that the friction coefficient $\mu$ between the disk and the cylinder is infinite. To study the motion of the disk, we define an inertial reference frame $S_0$ and a body-fixed reference frame $S_b$, and we introduce the angles $\psi$ and $\phi$, as shown in the figure. The body point $P$ on the disk, with position $\mathbf{r}_b^P = R\,\mathbf{i}_b$, feels a repulsive force from point $A$, located at $\mathbf{r}_0^A = -6R\,\mathbf{j}_0$, whose magnitude is equal to a known constant $k$ times the distance between $A$ and $P$. Initially, $\psi_0 = \phi_0 = 0$ and the disk is at rest.

**Data**: the moment of inertia of the disk about a line perpendicular to the drawing passing through $G$ is $I = mR^2/2$.

![[attachments/EM/T8-RB37-figure.png]]
*Figure: Disk b of radius $R$ rolling on the outside of a fixed cylinder of radius $3R$ centred at $O$ (as drawn), with the angles $\psi$ and $\phi$, the contact point $C$, the body point $P$, the force $\mathbf{F}_P$, the point $A$ and the frames $S_0$ and $S_b$ Source: Problems.pdf, p. 66.*

Assuming that the disk and the cylinder are always in contact:

* **(a)** How many effective degrees of freedom does the system have? Define $\mathbf{i}_b$, $\mathbf{j}_b$, and any other unit vectors that you want to use to solve the problem, in terms of $\{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$.
* **(b)** Give the general expressions for the position, velocity, and acceleration of $G$ and the angular velocity and acceleration of b with respect to $S_0$, as a function of $\psi$, $\phi$ and their derivatives.
* **(c)** Find the mathematical relation that exists between $\phi$ and $\psi$. Rewrite the expressions of the last question in terms of $\psi$ and its derivatives only.
* **(d)** Identify and give the mathematical expression of all forces on the disk, stating clearly their points of application, and introducing new unknowns as necessary. Then, reduce the system of forces to a resultant force $\mathbf{F}$ and a resultant torque $\mathbf{M}_G$ about $G$.
* **(e)** Write down a first-order differential equation for $\psi$, free of any other unknowns in the problem, and give the initial conditions for its integration.

Assuming now that the disk may separate from the cylinder:

* **(f)** Find the condition for which the disk detaches from the cylinder in terms of $\psi$ only (i.e., no $\dot{\psi}$ can appear in the solution).

---

## 📌 Problem RB-39: Yo-yo

The rigid body yo-yo in the figure consists of two heavy, homogeneous disks of radius $R$ and an inner cylinder of radius $a$, about which an ideally thin, infinitely long, massless, inextensible string winds up and down. The mass of the yo-yo is $m$, and its moment of inertia about its spin axis is $mR^2/2$. We denote the yo-yo with symbol $b$, and its center point as $C$. The other end of the string is attached to a fixed point on the ceiling, and we know that the string remains taut at all times. We introduce the generalized coordinates $\xi$, $\theta$ to determine the configuration of the system.

![[attachments/EM/T8-RB39-figure.png]]
*Figure: Yo-yo with the outer disks of radius $R$, the inner cylinder of radius $a$, the string attached to the ceiling at $O$, the generalized coordinates $\xi$ and $\theta$, the centre $C$, the gravity $\mathbf{g}$ and the axes $\mathbf{i}$, $\mathbf{j}$ Source: Problems.pdf, p. 68.*

* **(a)** Determine the position, velocity, and acceleration of the center point $C$ of the yo-yo, and its angular velocity and angular acceleration, as a function of the generalized coordinates and their time derivatives.
* **(b)** Identify all the forces/torques acting on the yo-yo $b$ and reduce them to a single resultant force and a single resultant torque at $C$.
* **(c)** Write down a system of (differential) equations that allows solving for the time evolution of all unknowns in the problem.
* **(d)** Find a first integral of motion (i.e., an equation that do not depend on second derivatives). Justify your procedure.

In the following, assume tat [sic] the yo-yo is further constrained to stay with $\theta = 0$:

* **(e)** If the yo-yo is initially at rest, determine the initial value of $\ddot{\xi}_0$. Sketch the graph of $\ddot{\xi}_0$ as a function of the ratio $R/a \in [1, \infty[$.
* **(f)** If initially $\xi_0 = 2R$, find the minimum value of $\Omega_0$, the magnitude of the initial angular velocity of the yo-yo, for it to be able to reach the origin (i.e., for $\xi$ to become equal to $0$ at a later instant of time). Assuming $a \ll R$, sketch the graph of $\Omega$ as a function of $R$.

---

## 📌 Problem RB-40: Disk on parabolic groove

A homogeneous, heavy disk $b$ of mass $m$, radius $R$, and center $G$ rolls without slip on the surface of a cavity with parabolic shape, whose geometry is given by

$$y = \frac{x^2}{4R},$$

and has a maximum depth of $3R$. The moment of inertia of the disk about $G$ is $I = mR^2/2$. To study the motion of the disk, we define an inertial reference frame $S_0$ and a body-fixed reference frame $S_b$ as shown below. We call $P$ the instantaneous point of contact between the disk and the parabola. We introduce the variables $x_P$ and $\phi$. An external, constant torque $Q\mathbf{k}_0$ is applied on the disk through an axle passing through $G$. Assume that the friction coefficient between the disk and the parabola $\mu$ is infinite, and that the disk and the parabola are always in contact. Initially, the disk is at rest with $x_P = 0$ and $\phi = 0$.

![[attachments/EM/T8-RB40-figure.png]]
*Figure: Disk b in the parabolic cavity with the torque $Q$, the frames $S_0$ (O, $\mathbf{i}_0$, $\mathbf{j}_0$) and $S_b$ (G, $\mathbf{i}_b$, $\mathbf{j}_b$), the contact point $P$, the angle $\phi$ and the coordinate $x_P$ Source: Problems.pdf, p. 69.*

* **(a)** How many degrees of freedom does the system have after taking into account all constraints? Write down the general expression of a tangent unit vector $\mathbf{e}_t$ and a normal unit vector $\mathbf{e}_n$ to the parabola at $P$ as a function of $x_P$, in terms of $\{\mathbf{i}_0, \mathbf{j}_0\}$.
* **(b)** Give the general expressions for the position and velocity of $G$, and the angular velocity of the disk $b$ with respect to $S_0$, as a function of $x_P$, $\phi$ and their derivatives.
* **(c)** Identify and give the mathematical expression of all forces and torques on the disk, introducing new unknowns as necessary. For each force, state clearly the point of application. Then, reduce the system to a resultant force $\mathbf{F}$ and a resultant torque $\mathbf{M}_G$ about $G$.
* **(d)** Express $\phi$ as a function of $x_P$.

  **Hint:** one of the resulting integrals is immediate; the other can be solved as

  $$\int \frac{\sqrt{u^2 + 4a^2}}{2a^2}\,\mathrm{d}u = \frac{u\sqrt{u^2 + 4a^2}}{4a^2} + \ln\left(\sqrt{u^2 + 4a^2} + u\right) + \text{const}$$

From this point on, assume the function $\phi(x_P)$ is known, even if you did not reach the correct result above.

* **(e)** Noting that the power of the constant torque is $Q\dot{\phi}$, write down a first-order differential equation for $x_P$, free of any other unknowns in the problem .
* **(f)** Determine the condition on the value of $Q$ to ensure that the disk gets out of the cavity.

---

## 📌 Problem RB-41: Sail sledge

A sail sledge is a special vehicle designed to slide over ice on blades, equipped with a vertical sail to catch the wind and propel itself. The sledge is moving on a horizontal plane of ice. We model it as a heavy rigid body $b$ of mass $m$ and moment of inertia $I$ about its center of mass $G$, which is located at a negligible height with respect to the ice. The contact points? [sic] of the blades with the ice are points $A$, $B$ and $C$, which form an equilateral triangle of side $\sqrt{3}\,\ell$ and center below $G$ as shown. The configuration of the sledge is defined by the $x$ and $y$ coordinates of its center of mass in $S_0$, and the attitude angle $\psi$. The blades at $A$ and $B$ are oriented parallel to $\mathbf{i}_b$, while the blade at $C$ forms an angle $\theta$ with this direction. Each blade may slide along the direction parallel to it without friction, but it cannot slip in the direction perpendicular to it.

The (horizontal) aerodynamic forces on the sail are a lift force $\mathbf{L}$ and a drag force $\mathbf{D}$, respectively perpendicular and parallel to the upstream wind velocity $\mathbf{u}_b^w$ relative to $S_b$. The point of application of these forces is the center of pressure $P$ of the sail, which is found at a distance $\ell$ above $G$, and their magnitudes are:

$$L = b_L\left(u_b^w\right)^2; \qquad D = b_D\left(u_b^w\right)^2;$$

where $b_L$ and $b_D$ are two known constants (we can assume the sail is automatically readjusted to keep them constant under all conditions). Wind blows in the direction of the arrow with a groundspeed $u_0^w = U_\infty$ relative to $S_0$.

![[attachments/EM/T8-RB41-figure.png]]
*Figure: Photograph of a sail sledge on ice (left) and schematic of the sledge with the blades $A$, $B$ and $C$, the centre of mass $G$, the frames $S_0$ and $S_b$, the angles $\psi$ and $\theta$, the centre of pressure $P$ and the wind $U_\infty$ (right) Source: Problems.pdf, p. 70.*

* **(a)** Find the general expression for the position, velocity, and acceleration of $G$, and the angular velocity and acceleration of the body $b$, with respect to $S_0$, in terms of $x$, $y$, $\psi$, and their derivatives.
* **(b)** Find the position $\mathbf{r}_b^I$ of the instantaneous center of rotation $I$ of $b$ as a function of $\theta$.
* **(c)** Express $\dot{x}$ and $\dot{y}$ as a function of $\dot{\psi}$ and $\theta$, assuming $\theta \neq 0$.
* **(d)** Write down all the forces acting on $b$ and specify their point of application. Introduce new unknowns in the problem as needed. Assume that the reaction forces on $A$ and $B$ in the $\mathbf{j}_b$ direction are equal in magnitude.

In the rest of the problem, consider that $\psi = \theta = 0$.

* **(e)** If the sledge is at rest and $b_D = 0$, $\mathbf{L} \cdot \mathbf{i}_b \geq 0$, what is the maximum value of $U_\infty$ that the vehicle can withstand without tipping over at that instant?
* **(f)** Assuming that the sledge does not tip over, what is the maximum speed it can continuously travel at, as a function of $b_L$, $b_D$, and $U_\infty$?

---

## 📌 Problem RB-17: Constrained pizza cutter (Fork and disc)

The system of the figure comprises a fork and a disc. The fork can turn around the horizontal axis $AB$. The disc turns around the axis $CD$ mounted on the fork perpendicularly to $AB$. Thus, the disc always contains the horizontal $AB$. The mass of the fork is $M$, $a$ is the distance from the center of mass of the fork $G$ to the axis $AB$, $m$ is the mass of the disc, $b$ the minimum distance between the axis $AB$ and $CD$, $R$ the radius of the disc. The tensor of inertia of the fork in $O_1$ has the following form:

$$\bar{\bar{\mathcal{I}}}^{F}_{O_1} = \begin{bmatrix} I_1 & 0 & 0 \\ 0 & I_2 & 0 \\ 0 & 0 & I_3 \end{bmatrix}_{22}$$

Assuming that the thickness of the disc is negligible and that gravity $\mathbf{g} = g\,\mathbf{k}_1$,

* **(a)** Compute the kinetic energy of the system fork-disc with respect to frame $S_1 : \{O_1; B_1\}$.
* **(b)** Compute the angular momentum of the disc about $O$ with respect to $S_1$. Express its components using the vector basis $B_2 : \{\mathbf{i}_2, \mathbf{j}_2, \mathbf{k}_2\}$.
* **(c)** Compute the angular momentum of the fork-disc about $O_1$ with respect to $S_1$. Express its components using the vector basis $B_1 : \{\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$.
* **(d)** Formulate the equations of motion of the system and reduce them to quadratures (i.e., integrals).
* **(e)** Determine the resultant force and torque that the axis $AB$ applies on the fork-disc system at $O_1$.
* **(f)** Determine the resultant force and torque that the axis $CD$ applies on the disc at $O$.

![[attachments/EM/T8-RB17-figure.png]]
*Figure: Fork turning about the horizontal axis $AB$, with the disc turning about the axis $CD$ on the fork; the angles $\theta$ and $\varphi$ and the frames $x_0y_0z_0$, $x_1y_1z_1$ and $x_2y_2z_2$ are marked Source: Problems.pdf, p. 47.*

---

## 📌 Problem RB-20: Pioneer III spacecraft (Yo-yo de-spin)

The Pioneer III lunar probe is an axisymmetric space vehicle, as shown in the figure. The mass of the probe is $m$, radius is $R$, and moment of inertia with respect to the axis of symmetry is $I$. It is launched with an initial constant spin rate $\omega_0$. By using a yo-yo with two weights of mass $m/2$ each, it is desired to reduce the spin rate to $\omega_f$. Each mass is connected to the spacecraft by a cord, as shown in the figure for one of the mass [sic]. The cords are attached to the spacecraft at $H$ and $H'$. Both masses are released simultaneously by explosive bolts, so that the cords unwrap in the manner shown in the figure. In doing so, the points of tangency, $T$ and $T'$, move around the circumference towards $H$ and $H'$ (respectively). When $T$ and $T'$ reach the hinges $H$ and $H'$, the cords are automatically released from the spacecraft. The gravitational interaction with all celestial bodies (Sun, Earth, etc.) may be considered negligible.

![[attachments/EM/T8-RB20-figure.png]]
*Figure: Photograph of the Pioneer III probe, a cone-shaped axisymmetric body with a ring of yo-yo masses below it. Source: Problems.pdf, p. 50.*

![[attachments/EM/T8-RB20-figure-b.png]]
*Figure: Top view of the probe with its centre $G$, the cords at $H$ and $H'$, the points of tangency $T$, the yo-yo masses $m/2$ at $A$ and $A'$, the point $P$ with position $\mathbf r$ and velocity $\mathbf v$, the radius $R$, the angle $\phi$ and the spin $\omega$. Source: Problems.pdf, p. 50.*

* **(a)** Analyze the motion after the release of the yo-yo masses and compute the evolution of the probe's angular velocity as function of time.
* **(b)** In order to obtain the desired final angular velocity, what is the required length of the cord that joins the yo-yo masses and the probe?
* **(c)** Compute the evolution of the tension in the cord as function of time.

---

## 📌 Problem RB-21: Reaction wheel spacecraft attitude control

A reaction wheel is a type of flywheel used for attitude control of spacecraft. Consider a spacecraft $b$, modeled as a homogeneous rigid rod of mass $m^b = 6M$, and length $L$, and negligible diameter. Two reaction wheels $w_1$ and $w_2$ with radius $R$ and mass $m^{w_1} = m^{w_2} = M$ are located at the ends of the spacecraft. We define an inertial reference frame $S_0 = \{O; B_0\}$ (not shown in the figure), and a parallel reference frame $S_G = \{G; B_0\}$ that translates but does not rotate with the spacecraft. Observe that $G$ is the center of mass of of $b$ [sic] and also the center of mass of the whole assembly. Furthermore, we define a spacecraft-fixed reference frame $S_b = \{G; B_b\}$. This reference frame is defined with the axis $Gx_b$ along the spacecraft in the direction from wheel 2 to wheel 1. The direction of $Gx_b$ is defined with the angles $\theta$ and $\varphi$ as in spherical coordinates, as shown in the figure. The reaction wheels can rotate with respect to the spacecraft $b$ about the $Gx_b$ axis, with unknown angular rates $\dot\phi_1$ and $\dot\phi_2$ that may vary in time, respectively. The (degenerate) tensor of inertia of the spacecraft body $b$ alone (without the wheels) about its center of mass $G$, and the tensor of inertia of one wheel $w_i$ about its center of mass $G_i$, expressed in basis $B_b$, are:

$$\overline{\overline{I}}{}^{\,b}_{G} = \frac{1}{12} m^b L^2 \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}_b , \qquad \overline{\overline{I}}{}^{\,w_i}_{G_i} = \frac{1}{4} m^{w_i} R^2 \begin{bmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}_b , \qquad i = 1, 2$$

We assume that the system is in deep space, so all the external forces and torques are negligible. Lastly, consider the following initial conditions ($\Omega$ is a known constant):

$$\mathbf r_0^G(t = 0) = \mathbf 0 , \qquad \mathbf v_0^G(t = 0) = \mathbf 0$$

$$\theta(t = 0) = 0 , \qquad \varphi(t = 0) = \pi/4$$

$$\phi_1(t = 0) = 0 , \qquad \phi_2(t = 0) = 0$$

$$\boldsymbol\omega_{b0}(t = 0) = \frac{\Omega}{\sqrt{2}} \left[ \frac{1}{\sqrt{2}}\mathbf i_B + \mathbf j_B + \frac{1}{\sqrt{2}}\mathbf k_B \right] , \qquad \dot\phi_1 = \dot\phi_2 = \frac{\Omega}{2}$$

![[attachments/EM/T8-RB21-figure.png]]
*Figure: Spacecraft with its two reaction wheels $D_1$ and $D_2$ at the ends, the axes $x_B$, $y_B$, $z_B$ at $G$, and the angles $\theta$ and $\varphi$. Source: Problems.pdf, p. 51.*

* **(a)** Express the angular velocities of the spacecraft and reaction wheels $\boldsymbol\omega_{b0}$, $\boldsymbol\omega_{10}$, and $\boldsymbol\omega_{20}$ as a function of $\theta$, $\varphi$, $\dot\theta$, $\dot\varphi$, $\dot\phi_1$, $\dot\phi_2$.
* **(b)** Express the absolute velocities of $G_1$ and $G_2$ as a function of the absolute velocity of $G$, $\theta$, $\varphi$, $\dot\theta$ and $\dot\varphi$.
* **(c)** Compute the angular momentum of each of the reaction wheels about their respective center of mass ($G_1$ and $G_2$).
* **(d)** Compute the angular momentum of the whole system about the center of mass of the whole system.
* **(e)** Compute the kinetic energy, $T$, of the whole assembly.
* **(f)** Pose the set of ordinary differential equations for the position of $G$ and for $\theta$, $\varphi$, $\phi_1$, $\phi_2$.
* **(g)** Write down the reaction forces and torques at the joints between the rod and the reaction wheels.

---

## 📌 Problem RB-26: Unbalanced planetary bearings

A heavy disk of radius $d$ and mass $2m$ is allowed to rotate inside a circular cavity thanks to three heavy cylindrical bearings with center at $A$, $B$, and $C$, each with a radius $d/4$ and mass $m$, as shown in the figure. The disk-bearing contacts and bearing-cavity contacts allow rolling but no slipping. We define the inertial reference frame $Oxy$ fixed to the cavity. We denote $\theta$ the angular position of $A$ with respect to $Ox$. Initially, $\theta_0 = 0$ and all points of the system have zero velocity.

![[attachments/EM/T8-RB26-figure.png]]
*Figure: Disk of radius $d$ inside a circular cavity, with three bearings $A$, $B$ and $C$ of radius $d/4$, the angle $\theta$ of $A$ from $Ox$, the two $45^\circ$ angles and the gravity $\boldsymbol g$ Source: Problems.pdf, p. 56.*

* **(a)** Discuss the number of degrees of freedom of the system and choose a set of independent parameter(s) to specify its state at any instant of time.
* **(b)** Express the linear velocity of the center of each bearing, and the angular velocity of the disk and the bearings, as a function of your chosen set of parameter(s) and its/their derivatives in a generic instant of time.
* **(c)** Write down the position of the center of mass of the system as a function of your chosen set of parameter(s) in a generic instant of time.
* **(d)** Compute the kinetic energy of each body in the system in a generic instant of time.
* **(e)** Reduce the motion of the system to quadratures (i.e.,integrals) [sic].
* **(f)** Find the equilibrium positions of the system and discuss their stability.
* **(g)** If there are any stable equilibrium positions, compute the angular frequency of the oscillations of the system about it/them, if only very small deviations from equilibrium are allowed.

---

## 📌 Problem RB-27: Rectangle with weight, pulleys, and string

A heavy homogeneous rectangular block of mass $2m$ has height $L$ and width $2L$. The middle point $A$ of one of the short edges of the block is connected to a fixed point $B$, located at a distance $2L$ to the right of $O$, with a spring of stiffness $k$ and zero length in the absence of forces. The center $G$ of the block is connected to a point weight $P$ of mass $m$ with a string of constant length $6L$ and negligible mass. The string passes by two frictionless pulleys of negligible radius at $O$ and $C$ and is always tense. The distance between the two pulleys is $2L$. The weight $P$ is constrained to move along the vertical that passes by $C$. We define the right-handed inertial reference frame $Oxyz$ and the right-handed body-fixed reference frame $Gx_By_Bz_B$ attached to the block as shown in the figure. The block moves only in the $Oxy$ plane. The length $\xi$ and the angles $\theta$, $\phi$ are also defined there.

![[attachments/EM/T8-RB27-figure.png]]
*Figure: Rectangular block of mass $2m$ hanging from the spring $k$ fixed at $B$, with the string from $G$ over the pulleys at $O$ and $C$ to the weight $P$, the length $\xi$, the angles $\theta$ and $\phi$, and the frames $Oxyz$ and $Gx_By_Bz_B$ Source: Problems.pdf, p. 57.*

Answer the following questions in a reasoned way:

* **(a)** How many degrees of freedom does the system have?. [sic]
* **(b)** Express the position, velocity and acceleration of $G$ and the angular velocity and angular acceleration of the block with respect to $Oxy$, as a function of $\xi$, $\theta$, $\phi$ and their derivatives.
* **(c)** Write down the expression of all forces acting on the weight $P$ and the block.
* **(d)** Write down three second order differential equations for the evolution of $\xi$, $\theta$, $\phi$ with time. Note that you do not need to solve them.
* **(e)** Can you apply the law of conservation of mechanical energy to this problem? if so [sic], write down the corresponding equation.

---

## 📌 Problem RB-29: Disk-bar train

A homogeneous disk $D$ of radius $R$ and mass $m$ can rotate freely about its center $O$, which is fixed to the wall. We define the inertial reference frame $S_0$ as shown in the figure. A homogeneous, heavy bar $B$ of mass $2m$ and length $L$ has a longitudinal groove that allows it to slide without friction over a small knob $K$ fixed to the wall and located at a height $h$ above $O$. One of the end points of the bar is connected to perimeter [sic] of the disk at point $C$ as shown. This connection allows the bar to rotate freely about $C$ with respect to the disk. The other end point $A$ of the bar is attracted to the $Oy$ axis by a force $\mathbf F_A$ that is proportional to its distance to $Oy$. The proportionality constant of this force is $k$.

![[attachments/EM/T8-RB29-figure.png]]
*Figure: Disk $D$ of radius $R$ centred at $O$ on the wall, bar $B$ with its groove over the knob $K$ at height $h$, end $C$ on the disk perimeter, end $A$ pulled towards the $Oy$ axis by $\mathbf F_A$, the frame $S_0$ with axes $x_0$, $y_0$, and the angles $\theta$ and $\phi$ Source: Problems.pdf, p. 59.*

* **(a)** How many degrees of freedom does this planar problem have? Justify your answer.
* **(b)** Find the geometric relation between $\theta$ and $\phi$. Compute $\dot\phi$ and $\ddot\phi$.
* **(c)** Express the general position, velocity, and acceleration of point $A$ and the center of mass of the bar $G$ as a function of $\theta$, $\phi$ and their time derivatives.
* **(d)** Write down the general expression of all forces acting on the bar and on the disk, be they applied or otherwise.
* **(e)** Compute the general expression of the kinetic energy of the bar and the kinetic energy of the disk.
* **(f)** If $\theta_0 = 0$, $\dot\theta_0 = 0$ initially, obtain one equation on $\theta$, $\phi$, $\dot\theta$, $\dot\phi$ to describe the motion of the system that does not depend on any additional unknowns.

---

## 📌 Problem RB-31: Ball bearing between cylinder and cone

A rigid, homogeneous, heavy ball $b$ of mass $m$ and radius $R$ is always in contact with a rigid, homogeneous, heavy cone $c$ of half-angle $\beta$, radius at the base $2R$, and mass $2m$. The ball is also always in contact with a rigid cylindrical frame $d$ of inner radius $3R$ that has a base at the bottom and the same axis of symmetry as the cone. We call the instantaneous contact points between the bodies $I$, $P$ and $Q$, as shown in the figure. We call the center of mass of the ball and cone $A$ and $G$, respectively. The cylinder is at rest in the inertial reference frame $S_0$. The cone can rotate about its axis, which is constrained to coincide with $Oz_0$ at all times. We define the auxiliary reference frame $S_1$ that initially coincides with $S_0$ and rotates with respect to $\mathbf k_0$, such that $Ox_1$ follows the center of the ball in its motion. The angle between $Ox_0$ and $Ox_1$ is called $\theta$, and the angle of rotation of the cone with respect to $S_0$ is called $\phi$. Both angles are positive in the counterclockwise direction as seen from $Oz_0$. The friction coefficient of the ball with the other bodies is $\mu$. The ball can pivot freely at each contact point with the cone and the cylinder.

![[attachments/EM/T8-RB31-figure.png]]
*Figure: Cone $c$ with half-angle $\beta$ on the symmetry axis $Oz_1 \equiv Oz_0$, ball $b$ with centre $A$ between the cone and the cylindrical frame $d$, contact points $I$, $P$ and $Q$, the centre of mass $G$ of the cone, the axis $Ox_1$ and gravity $\boldsymbol g$ Source: Problems.pdf, p. 61.*

* **(a)** How many degrees of freedom does the system have in the limit $\mu = 0$? And in the limit $\mu = \infty$?
* **(b)** Write down the general expression of the position, velocity and acceleration of $A$ with respect to $S_0$ as a function of $\theta$ and its derivatives.

Assuming first that no slipping occurs between the ball and the other objects:

* **(c)** Locate the instantaneous axis of rotation (IAR) of the ball in $S_0$. Write down the general expression of the angular velocity and acceleration of the ball with respect to $S_0$ as a function of $\theta$ and its derivatives.
* **(d)** Find the relation between $\dot\theta$ and $\dot\phi$.
* **(e)** Identify and express all forces acting on the ball, and clearly state their point of application.
* **(f)** Obtain the equations of motion of the system and prove that the problem is undetermined (i.e., more unknowns than equations).

Considering now that the cone is rotating at a constant angular velocity, and assuming that the component in the $Ox_1z_1$ plane of the friction forces at points $P$ and $I$ are zero:

* **(g)** What is the maximum value of $\dot\theta$ for which the no-slipping condition holds?

Note: The moment of inertia of the sphere about any axis that passes through its center is $2mR^2/5$. The moment of inertia of the cone about its axis is $12mR^2/5$.

---

## 📌 Problem RB-36: Mars rolling rover

To prevent the effect of martian dust on internal mechanisms, a new concept of a hermetically-sealed rolling robot for the exploration of Mars is proposed, which consists of a homogeneous, heavy, rigid cylinder $b$ of mass $M$, radius $R$, and center of mass at its geometric center $C$. The moment of inertia of the cylinder about an axis through $C$ perpendicular to the plane of motion is $I_z$. The cylinder has an internal diametrical slot in it of total length $2\ell < 2R$ as shown in the figure. Inside this slot there is a heavy point particle $P$ of mass $m$, whose position $x_1^P$ in the slot is varied in time according to a prescribed law $x_1^P = x_1^P(t)$. The motion of $P$ is imposed by an internal motor (not shown) of negligible mass that is mounted on the cylinder $b$. We determine the configuration of the cylinder with the position $x_0^C$ of its center $C$ and its rotation angle $\varphi$. The angle of the ground is denoted $\gamma$, the instantaneous contact point of the robot with the ground is denoted $A$, and the friction coefficient is denoted $\mu$. The reference frame $S_0$ is inertial and the reference frame $S_1$ is fixed to the cylinder.

![[attachments/EM/T8-RB36-figure.png]]
*Figure: Rolling robot: cylinder $b$ with its diametrical slot, particle $P$, frames $S_0$ (axes $\mathbf{i}_0$, $\mathbf{j}_0$) and $S_1$ (axes $\mathbf{i}_1$, $\mathbf{j}_1$), angle $\varphi$, slope angle $\gamma$ and contact point $A$ Source: Problems.pdf, p. 65.*

* **(a)** Find the general expression for the position, velocity, and acceleration vectors of $P$ with respect to $S_0$ as a function of $x_0^C$, $\varphi$, $x_1^P$, and their derivatives.
* **(b)** Give the expression of the force $\mathbf{F}$ on the cylinder $b$ caused by the particle $P$ and its motion.

  **NOTE**: observe that as the motor pushes on $P$, an equal and opposite force appears on the cylinder along the same line of action.
* **(c)** Reduce the system of all forces and torques on the cylinder to a single resultant force and a single resultant torque about its geometric center $C$.
* **(d)** Consider now that we want keep the robot at rest, i.e., in equilibrium, on the slope. What is the maximum value of $\gamma$ that allows this condition if we have $\varphi = \gamma$ and $x_1^P$ can be set within the range $[-\ell, \ell]$?

In the following, assume that $\mu$ is sufficiently large to prevent slipping, that $\gamma = 0$, and that the control law $x_1^P(t) = \ell \sin(\Omega t)$ for the position of $P$ is prescribed, where $\Omega$ is a known constant and $\ell = R/2$.

* **(e)** Write down a closed system of equations for all unknowns in the problem, and identify which initial conditions would be needed to integrate it. Explain in what order you would solve this system.
* **(f)** Consider finally that at a particular instant of time $\dot{\varphi} = 0$ and $\ddot{\varphi} = 0$. What is the maximum value of $\Omega$ that we can have and still ensure that the robot never takes off the ground?

---

## 📌 Problem RB-42: Gyro on inclined plane

A heavy, thin, homogeneous, hollow sphere $s$ of radius $R$ and mass $m$ contains a heavy, homogeneous disk $d$ of mass $2m$. The disk is supported by a massless axle that is rigidly connected to the sphere at two polar opposite points $A$ and $B$, so that the centers of mass of the sphere and disk coincide, $G_s \equiv G_d \equiv G$. The disk can spin freely about the axle. The sphere rolls without slipping over an inclined plane that forms a known, fixed angle $\gamma$ with the horizontal. We call $C$ the instantaneous contact point of the sphere with the plane, and we assume that the sphere cannot separate from the plane. We define the inertial reference frame $S_0$, the sphere-fixed reference frame $S_s$, and the disk-fixed reference frame $S_d$ (see figure). The attitude of $S_s$ with respect to $S_0$ is given by the 3-1-3 Euler angles $\psi$, $\theta$, $\phi$. The attitude of $S_d$ with respect to $S_s$ is given by angle $\beta$, knowing that when $\beta = 0$, $S_d$ coincides with $S_s$. The position of the contact point on the plane is described with coordinates $\xi$, $\eta$. The tensors of inertia of the sphere and the disk about $G$, expressed in the basis $B_s$ of $S_s$, are:

$$\overline{\overline{I}}{}^{\,s}_G = 2\,\dfrac{mR^2}{3}\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}_s ; \qquad \overline{\overline{I}}{}^{\,d}_G = \dfrac{mR^2}{6}\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{bmatrix}_s .$$

![[attachments/EM/T8-RB42-figure.png]]
*Figure: Hollow sphere s with the disk d on the axle AB, the inertial frame $S_0$ (O, $\mathbf{i}_0$, $\mathbf{j}_0$, $\mathbf{k}_0$), the frames $S_s$ and $S_d$ with $\mathbf{k}_s \equiv \mathbf{k}_d$, the contact point $C$ on the inclined plane with coordinates $\xi$ and $\eta$, the angle $\gamma$ and the gravity $\mathbf{g}$ Source: Problems.pdf, p. 71.*

* **(a)** Starting from the vector basis $B_0$ of $S_0$, write down the expressions for the change-of-basis associated to the Euler angles, which define the intermediate vector bases $(B_1, B_2)$ and the vector basis $B_s$ of $S_s$.
* **(b)** Give the general expressions for $\mathbf{r}_0^G$, $\boldsymbol{\omega}_{s0}$, and $\boldsymbol{\omega}_{ds}$ as a function of the coordinates of the problem and their derivatives.
* **(c)** Write down the equations of the rolling without slipping constraint between the sphere and the plane, in terms of the coordinates of the problem and their derivatives. Classify this constraint according to [integrable / non-integrable], [stationary / non-stationary].
* **(d)** Draw an exploded view diagram of the disk, the sphere (including the axle as part of it), and the plane, and correctly represent all reactions on each body.
* **(e)** Express all forces and torques on the sphere mathematically, using the unit vectors you have defined before and introducing new unknowns as needed. Reduce this system of forces and torques to a resultant force and a resultant torque at $G$.
* **(f)** Write down the total angular momentum about $G$ and the total kinetic energy of the system, as seen from $S_0$.
* **(g)** Find two first integrals of motion.

---

## 📌 Problem RB-30: Free spinning asteroid (Poinsot's construction)

An irregularly-shaped, rigid asteroid $b$ with center of mass $G$ is floating freely in space. We define an inertial reference frame $S_0 : \{G; B_0\}$, and a body-fixed reference frame $S_b : \{G; B_b\}$ as shown in the figure, where $B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$ and $B_b = \{\mathbf i_b, \mathbf j_b, \mathbf k_b\}$. One can reach $B_b$ from $B_0$ by a sequence of Euler rotations 1-2-3, with angles that we shall call $\psi$, $\theta$, and $\phi$ (in that order). The asteroid has mass $m$ and a tensor of inertia at $G$ that expressed in the vector basis $B_b$ is

$$\overline{\overline{\mathcal I}}_G = m\ell^2 \begin{bmatrix} 2 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 8 \end{bmatrix}_b ,$$

where $\ell$ is a characteristic length of the asteroid. Initially, $(\psi_0, \theta_0, \phi_0) = (\pi/3, 0, \pi/2)$ and $(\dot\psi_0, \dot\theta_0, \dot\phi_0) = (-2, 0, 1)/\tau$, where $\tau$ is a characteristic time.

![[attachments/EM/T8-RB30-figure.png]]
*Figure: Asteroid $b$ with centre $G$, the inertial basis $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$ (blue) and the body-fixed basis $\mathbf e_1$, $\mathbf e_2$, $\mathbf e_3 \equiv \mathbf k_2$ (red) Source: Problems.pdf, p. 60.*

* **(a)** Express the vectors $\mathbf i_b$, $\mathbf j_b$, $\mathbf k_b$ in the vector basis $B_0$ as a function of $\psi$, $\theta$, and $\phi$.
* **(b)** Write down the angular velocity vector of the asteroid, $\boldsymbol\omega_{b0}$, in basis $B_b$ as a function of $\psi$, $\theta$, $\phi$ and their derivatives.

In the following, we shall denote the components of $\boldsymbol\omega_{b0}$ in $B_b$ as $\omega_{xb}$, $\omega_{yb}$, $\omega_{zb}$, and define a point $P$ with position vector $\mathbf r_b^P = x_b\mathbf i_b + y_b\mathbf j_b + z_b\mathbf k_b = \tau\ell(\omega_{xb}\mathbf i_b + \omega_{yb}\mathbf j_b + \omega_{zb}\mathbf k_b)$.

* **(c)** Compute the kinetic energy $T_0^b$ of the asteroid. Demonstrate that $P$ must remain on the surface of a body-fixed ellipsoid at all times. What are the sizes of the semi-axes of this ellipsoid?
* **(d)** Compute the angular momentum vector $\mathbf H^b_{G0}$ of the asteroid. Demonstrate that the component of $\boldsymbol\omega_{b0}$ in the direction of $\mathbf H^b_{G0}$ is constant. Show that $P$ must remain on an invariant plane of $S_0$ at all times, and compute the distance to this plane from $G$.

Since the ellipsoid is body-fixed, it rotates with the same angular velocity vector as the asteroid, and we can study the motion of the asteroid with the ellipsoid only.

* **(e)** Show that the ellipsoid and the plane are tangent at $P$ at all times.
* **(f)** Using the results of previous questions, describe qualitatively the motion of the ellipsoid with respect to the plane.

HINT: An ellipsoid can be expressed as $x^2/a + y^2/b + z^2/c = d$ with $a, b, c, d > 0$.

---

## 📌 Problem RB-32: Rate gyro on aircraft

An aircraft $a$ is equipped with a rate gyroscope, which consists of a spinning disk $d$ mounted on a single gimbal $b$, which is in turn attached to the aircraft chassis as shown in the figure. Each of these elements can be considered to be a rigid body. The principal moments of inertia of the disk about its center of mass $G$ are $2I$ along its axis of spin, and $I$ along the perpendicular directions. The gimbal has negligible mass and moments of inertia. The figure defines the nutation angle $\theta$ and the spin angle $\phi$. Moreover, it defines the aircraft-fixed $S_a$, the gimbal-fixed $S_b$ (simple rotation of angle $\theta$ with respect to $S_a$), and the disk-fixed $S_d$ reference frames (simple rotation of angle $\phi$ with respect to $S_b$). We shall denote an arbitrary inertial reference frame as $S_0$ (not shown). There is a torsional spring which exerts a restoring torque on the gimbal proportional to angle $\theta$, with constant of proportionality $k$. Additionally, there is a a [sic] torsional damper which exerts a damping torque on the gimbal proportional to $\dot\theta$, with constant of proportionality $\lambda$. The aircraft performs a known yaw maneuver with angular velocity $\boldsymbol\omega_{a0} = \Omega(t)\mathbf k_a$.

![[attachments/EM/T8-RB32-figure.png]]
*Figure: Rate gyroscope: disk $d$ with centre $G$ mounted on the gimbal $b$, whose axis is the horizontal bar along $\mathbf i_b$ (the spin axle is drawn along $\mathbf j_b$), the nutation angle $\theta$, the spin angle $\phi$, the torsional spring and damper $k$, $\lambda$ at the gimbal axis, the aircraft basis $\mathbf i_a$, $\mathbf j_a$, $\mathbf k_a$ and the yaw rate $\Omega(t)$ Source: Problems.pdf, p. 62.*

* **(a)** Express the vectors of the bases of $S_b$ and $S_d$ as a function of the vectors of the basis of $S_a$ and the angles $\theta$, $\phi$.
* **(b)** Obtain the general expressions for the angular velocity and angular acceleration of $S_b$ and $S_d$ with respect to the inertial reference frame, $S_0$.
* **(c)** Identify all the torques acting on the rigid bodies of the problem and provide their general mathematical expression.
* **(d)** Derive the equations of motion for $\theta$ and $\phi$ as a function of the parameters of the problem. No other unknowns shall appear in the equations.
* **(e)** Prove that the component of the angular momentum of the disk about its spin axis is a constant of motion.

In the following, assume that $\Omega \ll \dot\phi$ and that $k, \lambda$ are chosen so that $\theta$ remains small ($\theta \ll 1$) during the maneuver.

* **(f)** Linearize the equation of motion of $\theta$ under these assumptions. What is the relation between $\Omega$ and $\theta$ when $\Omega$ is constant?
* **(g)** Using the linearized equation of motion, find out the value of $\lambda$ for the system to be critically damped, as a function of the rest of parameters of the problem.

---
