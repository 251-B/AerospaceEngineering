---
title: "Problem Set - Topic 6: Rigid Body Kinematics and Inertia"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Problem Statements"
language: "English"
tags:
  - problems
  - topic-6
  - rigid-body-kinematics
---

# 📝 Topic 6: Rigid Body Kinematics and Inertia - Problem Statements

Problem statements of the rigid body section (section 2) of `Problems.pdf`, copied word for word; typing errors of the PDF are kept and marked "[sic]". Numbers are those of that section, written RB-NN. Course material: Lectures 7 and 8; Notes.pdf, chapters 9 and 10.

> [!NOTE]
> **Status:** statements transcribed from `Problems.pdf` (PDF page index in every figure caption). Official answers, where the PDF prints one: [[Problem Set - Rigid Body Official Key]]. Subject index: [[Engineering Mechanics MOC]].

- **Group A:** Rigid body kinematics, Euler angles and the instantaneous axis of rotation.
- **Group B:** Mass geometry, Steiner's theorem and principal axes.

| Problem | Group | Key (PDF page) | Title |
| :---: | :---: | :---: | :--- |
| RB-01 | A | p. 77 | Kinematics (3 points) |
| RB-02 | A | p. 77 | Kinematics (3 conditions) |
| RB-03 | A | p. 77 | Flywheel kinematics (Euler angles) |
| RB-11 | A | p. 79 | Rolling disk (3D pure rolling kinematics) |
| RB-34 | A | none | Velocity field of a rigid body 1 |
| RB-35 | A | none | Velocity field of a rigid body 2 (Spaceship) |
| RB-04 | B | p. 77 | Moments of inertia (planar shapes: T, I, C) |
| RB-05 | B | pp. 77-78 | Moments of inertia (3D shapes a-j) |

---

## 📌 Problem RB-01: Kinematics (3 points)

A rigid body moves with respect to a reference frame $Oxyz$. At a given instant, the velocity of the point $A(a, 0, 0)$ is $v_0\mathbf{j}$, the velocity of a point $B(0, a, 0)$ of the rigid body is $v_0(\mathbf{j} + \mathbf{k})$ and the velocity of a third point of the rigid body, $C(0, 0, a)$, is $v_0(\mathbf{i} + \mathbf{j} + \mathbf{k})$. Where is the instantaneous axis of rotation? Does the body have a slip velocity at this instant? Compute also the angular velocity of the rigid body at this instant. Find the minimum velocity of all points of the rigid body.

---

## 📌 Problem RB-02: Kinematics (3 conditions)

A rigid body (body reference frame $Px_By_Bz_B$) is moving with respect [sic] a reference frame $Oxyz$ in a way such that:

- the point $P$ of the solid is located along $Oy$
- the axis $Px_B$ passes through $A(a, 0, 0)$ (coordinates with respect to $Oxyz$)
- the angle $\theta$ between $Py_B$ and the plane $Oxy$ is equal to the angle between $Ox$ and $Px_B$

Determine the angular velocity of the body ($\boldsymbol{\omega}$) and the velocity of $P$ ($\mathbf{v}_0^P$) as a function of $\theta$ and $\dot{\theta}$.

---

## 📌 Problem RB-03: Flywheel kinematics (Euler angles)

A free gyroscope consists of a flywheel that rotates relative to the inner gimbal at the constant angular speed of $\omega_\theta$, and the rotation of the inner gimbal relative to the outer gimbal is $\gamma = A\sin(\omega_\gamma t)$. The rotation of the outer gimbal is $\beta = B\sin(\omega_\beta t)$. Determine the angular velocity and angular acceleration of the flywheel. Express the results in terms of components relative to the body-fixed reference frame $S_b$ ($xyz$) and with respect to the external reference frame $S_0$ ($XYZ$), where the $x$ axis was directed from bearing $D$ to bearing $C$ at $t = 0$.

![[attachments/EM/T6-RB03-figure.png]]
*Figure: free gyroscope with the flywheel, the inner and outer gimbals, the bearings $A$ to $F$, the axes $x, y, z$ and $X, Y, Z$, and the angles $\gamma$ and $\beta$ Source: Problems.pdf, p. 37.*

---

## 📌 Problem RB-11: Rolling disk (3D pure rolling kinematics)

A disc with radius $R$ is rolling (without slipping) on the plane $Oxy$ of a reference frame $S_0$ : $\{O, B_0\}$ with $B_0 : \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$. The center of the disc describes a circumference with radius $R$, in the counterclockwise direction seen from $Oz$ and with constant velocity $\omega R$. This circumference is contained in the plane $z = R$, with the center being at $(0, 0, R)$. The disc always remains perpendicular to plane $Oxy$. The perpendicular axis of the disc always intersects $Oz$. Determine:

* **(a)** Angular velocity and acceleration of the disc with respect to $S_0$.
* **(b)** Acceleration of the point of the disc that is in contact with $Oxy$.
* **(c)** Instantaneous axis of rotation.

---

## 📌 Problem RB-34: Velocity field of a rigid body 1

At a given instant of time a rigid body $b$ is in pure rotation. A point $A$ and a point $B$ of the rigid body have position and velocity vectors $\mathbf{r}_0^A = \mathbf{0}$, $\mathbf{r}_0^B = \mathbf{i}$, $\mathbf{v}_0^A = \mathbf{i} + 2\mathbf{k}$ and $\mathbf{v}_0^B = c\,\mathbf{i} + \mathbf{j}$, where $c$ is an unknown value. Determine $c$, the angular velocity $\boldsymbol{\omega}_{b0}$ of the body, and the position vector of a point in its instantaneous axis of rotation.

---

## 📌 Problem RB-35: Velocity field of a rigid body 2 (Spaceship)

Of a spaceship floating in space we known [sic] that its center of mass $G$, located at $\mathbf{r}_0^G = \mathbf{0}$, has a velocity $\mathbf{v}_0^G = 8\mathbf{i} + 4\mathbf{j}$. A point $A$ on its solar array has $\mathbf{r}_0^A = -2\mathbf{i} + 4\mathbf{j}$ and $\mathbf{v}_0^A = 4\mathbf{i} + 2\mathbf{j} + 6\mathbf{k}$. Point $C$ on the rear side has $\mathbf{r}_0^C = -8\mathbf{i} + 2\mathbf{k}$ and $\mathbf{v}_0^C = 10\mathbf{i} - 6\mathbf{j} + 8\mathbf{k}$.

* **(a)** Is the data compatible with the rigid body constraint?
* **(b)** What is the minimal velocity that any point of the spacecraft has at that instant?

---

## 📌 Problem RB-04: Moments of inertia (planar shapes: T, I, C)

Consider the following planar shapes (T,I,C shapes). Assuming the figures have uniform surface density $\sigma$, calculate:

![[attachments/EM/T6-RB04-figure.png]]
*Figure: the three planar shapes T, I and C, with the dimensions $w$, $h$ and $t$ Source: Problems.pdf, p. 38.*

* **(a)** the area of each figure and the position of the center of mass $G$. Once you have found it, define axes $x, y$ with origin on $G$.
* **(b)** the moment of inertia relative to the $x$ axis, $I_{Gx}$.
* **(c)** the moment of inertia relative to the $y$ axis, $I_{Gy}$.

What is the value of the product of inertia in $P_{xz,yz}$? Can you infer its value from the geometrical properties of the shapes?

---

## 📌 Problem RB-05: Moments of inertia (3D shapes a-j)

Compute the full three dimensional inertia tensor of the following homogeneous rigid bodies with respect to their center of mass:

* **(a)** Slender bar
* **(b)** Cylinder
* **(c)** Rectangular parallelepiped
* **(d)** Sphere
* **(e)** Hemisphere
* **(f)** Right angular cone
* **(g)** Thin disk ($h \ll R$)
* **(h)** Semicircular plate ($h \ll R$)
* **(i)** Semicircular wire arc
* **(j)** A flat sheet of length $L$ and width $w$, with respect [sic] a vertex $A$ and with respect to the center of mass $G$ (use the Steiner theorem)

![[attachments/EM/T6-RB05-figure.png]]
*Figure: slender bar with cross-sectional area $A$, cylinder with radius $R$, rectangular parallelepiped with sides $a$, $b$, $c$ and sphere with radius $R$, each with its center of mass $G$ and the axes $x, y, z$ Source: Problems.pdf, p. 38.*

![[attachments/EM/T6-RB05-figure-b.png]]
*Figure: hemisphere with radius $R$ and dimension $3R/8$, right angular cone with radius $R$ and length $L$, thin disk with radius $R$ and thickness $h$, semicircular plate with radius $R$ and thickness $h$, and semicircular wire arc with radius $R$ and cross-sectional area $A$, each with its center of mass $G$ and the axes $x, y, z$ Source: Problems.pdf, p. 39.*

---
