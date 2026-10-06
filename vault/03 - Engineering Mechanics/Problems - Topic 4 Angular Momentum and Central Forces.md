---
title: "Problems - Topic 4: Angular Momentum and Central Forces"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/03-engineering-mechanics/problemas/Problems.pdf"
type: "Verbatim Problem Statements"
language: "English"
---

# 📝 Topic 4: Angular Momentum and Central Forces - Problem Statements

Official problem statements from the UC3M Aerospace Engineering problem collection (`Problems.pdf`, Chapter 1). These problems test angular momentum, central force fields, torque about fixed and moving points, effective potential diagrams, two-body gravitational dynamics, Kepler's laws, the Binet equation, and the Vis-Viva energy relation.

> [!NOTE]
> **Status:** Verbatim problem statements transcribed faithfully from official department exams and problem sets.
> 
> [!SUCCESS] Complete Analytical Solutions Ready
> All problems have full, step-by-step pedagogical solutions developed in: [[Solutions - Topic 4 Angular Momentum and Central Forces]].

---

## 📌 Problem 17: Linear Central Force under Gravity

A force attracts a heavy particle $M$ of mass $m$ to a point $O$. The attractive force is proportional to the mass of the particle and to the distance $OM$. The proportionality coefficient is $k^2$. The coordinate system $Oxyz$ has the origin at the centre of attraction $O$ and the axis $Oz$ is vertically oriented. Initially, the coordinates of $M$ are:
$$ (x_0, y_0, z_0) = \left(\frac{\sqrt{3}g}{k^2}, 0, 0\right) $$
and its initial velocity is:
$$ (\dot{x}_0, \dot{y}_0, \dot{z}_0) = \left(0, \frac{2g}{k}, 0\right) $$

* **(a)** Describe the motion of $M$, specifying clearly the shape of the path.
* **(b)** What is the velocity of the particle as a function of $t$?

*(Note: This problem is directly featured as the foundational benchmark example on Slide 6 of `04_-_Angular_momentum.pdf`).*

---

## 📌 Problem 39: Particle on a String with a Plate

A heavy point particle $P$ with mass $m$ is connected with point $O$ on the upper surface of a thin square plate by a massless, inextensible string of length $\ell$. The distance between $O$ and the edge of the plate is $d$. The string hangs over the edge of the plate and can slide without friction. You can assume that the string remains tense and in contact with the plate at all times.

We denote the geometric point where the string is in contact with the plate edge as $Q$. We define the inertial reference frame $S_0 : \{O, \mathcal{B}_0\}$, with $\mathcal{B}_0 = \{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ as shown in the figure. We define the angle $\theta$ between the $Ox_0$ axis and the string segment $OQ$, and the angle $\phi$ between a vertical plane containing the plate edge and the line perpendicular to the plate edge that passes through $P$.

Initially at time $t = 0$, $\theta(0) = \phi(0) = \pi/3\text{ rad}$, and the modulus of the velocity of $P$ is $v_0^P(0) = \sqrt{\ell g}$, where $g$ is the magnitude of the acceleration due to gravity.

*Hint: Note that under the conditions of the problem, the two angles marked with dashed lines are equal.*

* **(a)** How many degrees of freedom does the system have?
* **(b)** Obtain the general expression of a unit vector in the direction from $Q$ to $P$ as a function of $\theta$ and $\phi$.
* **(c)** Obtain the general expression for the position, velocity, and acceleration vectors of $Q$ and $P$.
* **(d)** Formulate the equations of motion of the system and discuss the conservation of angular momentum and mechanical energy.

---

## 📌 Problem 42: Particle Attracted to the Origin (Advanced General Power Law)

*(Advanced problem:)* A point particle $P$ of mass $m$ is attracted by the origin of coordinates $O$ of the inertial reference frame $S_0$ by a force with magnitude:
$$ F = \frac{m\mu}{r^\alpha} $$
where $r$ is the distance between $O$ and $P$, and $\mu, \alpha$ are known positive constants.

* **(a)** Show that the angular momentum vector and the mechanical energy of $P$ are conserved quantities of motion, and that the motion of $P$ occurs in a plane.
* **(b)** Using polar coordinates $(r, \theta)$ in the plane of motion, find a second-order differential equation to solve for $u \equiv 1/r$ as a function of $\theta$ (i.e., $u = u(\theta)$).
* **(c)** Find a first integral of this equation and discuss the limits of motion of $u$ as a function of $\mu/h^2$, $\alpha$, and the values of $u$ and $u' \equiv du/d\theta$ at $t = 0$, where $h$ is the magnitude of the angular momentum vector about the origin per unit mass. For $\alpha = 1, 2, 3,$ and $4$, determine under which conditions:
  * **i.** The particle escapes to infinity ($u \to 0$).
  * **ii.** The particle reaches $r = 0$ ($u \to \infty$).
  * **iii.** The particle oscillates between two values of $u$.

*(Hint: try to solve first the problem with $\alpha = 2$, and then try the other values).*

---

## 📌 Problem 43: Two Connected Particles, Plane with Hole

We consider a smooth horizontal plane with a small hole in it. One of the ends of a massless cord of length $2a$ is passed through the hole and then, two point particles, $P_1$ and $P_2$, each with the same mass $m$, are attached to the ends of the cord. Therefore, $P_1$ is constrained to move on the plane and $P_2$ moves along a vertical line below the hole.

Initially, half of the cord lies under the plane and half of the cord is on the plane (so $r(0) = a$). At that instant, $P_1$ is pushed with a speed $v_0$ perpendicular to the cord, counterclockwise as seen from above. Assume that the cord is always in tension.

* **(a)** What is the value of $v_0$ if $P_1$ describes a circumference?
* **(b)** In that case, what is the value of the tension in the cord?
* **(c)** If $v_0 = \sqrt{8ag/3}$, reduce the problem to integrals (i.e., quadratures).
* **(d)** Show that for this value of $v_0$, $P_1$ oscillates between $r = a$ and $r = 2a$.
* **(e)** Apply Newton's law to $P_2$ and show that the tension of the cord is:
  $$ T = mg\left(\frac{1}{2} + \frac{4a^3}{3r^3}\right) $$
* **(f)** Write down the new equations of motion if the plane on which $P_1$ moves is rough, with a friction coefficient $\mu$.

*(Hint: the roots of the polynomial $-3x^3 + 7x^2 - 4$ are $x_1 = 1$, $x_2 = 2$, and $x_3 = -2/3$).*

---

## 📌 Problem 44: The Little Prince Throwing Seeds

The little Prince is on his spherical asteroid, which has radius $R$ and mass $M$, and does not rotate. While he sits at the equator, he throws a baobab seed with an initial velocity of magnitude $v_0$ and angle $\beta = 60^\circ$ with respect to the local horizontal. Knowing that it reaches an apocenter of:
$$ r_a = 3R $$
before falling back, determine $v_0$ as a function of the parameters of the problem and the universal gravitational constant $G$.
