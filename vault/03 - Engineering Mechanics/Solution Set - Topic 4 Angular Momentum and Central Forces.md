---
title: "Solution Set - Topic 4: Angular Momentum and Central Forces"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full Analytical Solutions (course order, Notes chapter 7)"
language: "English"
tags:
  - solutions
  - topic-4
  - central-forces
---

# Topic 4: Angular Momentum and Central Forces - Full Analytical Solutions

Step-by-step analytical solutions for the official problems of Topic 4 (**Angular Momentum, Central Forces, and Kepler's Problem**) of *Mechanics Applied to Aerospace Engineering* (UC3M). Every solution follows the Engineering Mechanics order of the problem-solving standard and the Newtonian approach of `Notes.pdf`, chapter 7: reference frames, bases and coordinates; change of basis and position vector; kinematics; forces and equations of motion; answers and checks. Angular momentum, central forces, Binet's equation and Kepler's problem are derived in each solution from the position vector and Newton's second law, in the order of `Notes.pdf`, chapters 4 and 8, and every development (derivatives with the product and chain rules, integrals with Barrow's rule) is written out in a derivation box.

---

## Problem 42: Particle Attracted to the Origin (Advanced General Power Law)

### Reference Frames, Bases and Coordinates

A point particle $P$ of mass $m$ is attracted by the origin $O$ of the inertial frame $S_0$ by a force of magnitude $m\mu/r^\alpha$, where $r$ is the distance from $O$ to $P$ (Problems.pdf, p. 29; the official text calls the strength $\alpha$ and the exponent $\beta$, see the notation note of the Problem Set). The statement asks to prove that the angular momentum and the mechanical energy are conserved and that the motion is planar, to find the second-order equation of $u$ as a function of $\theta$, and to discuss with a first integral when the particle escapes, reaches $O$ or oscillates, for the exponents 1, 2, 3 and 4. The solution follows the Newtonian approach of Notes.pdf, Sec. 7.1 to Sec. 7.7, and the derivation of the central force problem of Notes.pdf, Sec. 4.8.1 and Notes.pdf, Sec. 8.3, with the general exponent in place of the inverse square.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, origin at the attracting centre (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$, right-handed; $\mathbf k$ is taken along the angular momentum $\mathbf H_{O,0}$, which part (a) proves to be constant, so that the plane of the motion is the plane $Oxy$ (Notes.pdf, Sec. 8.2) |
| Polar basis | $\mathcal B_1 = \{\mathbf e_r, \mathbf e_\theta, \mathbf k\}$, $\mathcal B_0$ turned by $\theta$ about $\mathbf k$; $\mathbf e_r$ points from $O$ towards $P$ (Notes.pdf, Eq. 8.2) |
| Coordinates | $r$, the distance $OP$; $\theta$, the polar angle of $P$ measured from $\mathbf i$, counterclockwise about $\mathbf k$; $u = 1/r$ and $u' = du/d\theta$ (statement) |
| Hypotheses | $S_0$ inertial; $\mu \gt 0$ (attraction) and the exponent $\alpha$ constant, discussed for $\alpha = 1, 2, 3, 4$; no other force acts; $h \ne 0$ in parts (b) and (c) (with zero angular momentum the motion is radial: last limiting case) |
| Constraints | none: $P$ is a free particle ([Lecture 3, Slide 4]) |
| Degrees of freedom | 3 in space; 2 in the plane of the motion ($r$, $\theta$) once part (a) has proved that the motion is planar |
| Data | $m$ [kg], $\mu$ [m$^{\alpha+1}$ s$^{-2}$], $\alpha$ [1]; initial values $u_0 = u(0)$ [m$^{-1}$] and $u_0' = u'(0)$ [m$^{-1}$] |
| Derived constants | $h = \lvert\mathbf r_0^P\times\mathbf v_0^P\rvert$, angular momentum about $O$ per unit mass [m$^2$ s$^{-1}$]; $K = \mu/h^2$ [m$^{\alpha-3}$], the parameter of the discussion (the "$\mu/h^2$" of the statement) |
| Applied force | the attraction $\mathbf F = -\dfrac{m\mu}{r^\alpha}\,\mathbf e_r$, from $P$ towards $O$ |
| Constraint and inertia forces | none: no constraint, and $S_0$ is inertial |

![[attachments/EM-SOL/p42-plane.svg]]

### Change of Basis and Position Vector

![[attachments/EM-SOL/p42-rotation-k.svg]]

> [!derivation] Polar basis: rotation about k
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 8.2
>
> View along $\mathbf k$, which points out of the paper (⊙) because it is the cross product of $\mathbf i$ (to the right) and $\mathbf j$ (up): a positive rotation about $\mathbf k$ is counterclockwise, as $\theta$ in the figure. $\mathbf e_r$ is $\mathbf i$ turned by $\theta$: in its right triangle the hypotenuse is 1, the adjacent leg $\cos\theta$ lies along $\mathbf i$ and the opposite leg $\sin\theta$ along $\mathbf j$. $\mathbf e_\theta$ is $\mathbf j$ turned by $\theta$: the adjacent leg $\cos\theta$ lies along $\mathbf j$ and the opposite leg $\sin\theta$ along minus $\mathbf i$, because the upward vector turned counterclockwise leans to the left (the minus sign).
>
> $$\begin{aligned}
> \mathbf e_r &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j \quad &\text{(right triangle of $\mathbf e_r$: adjacent leg on $\mathbf i$, opposite leg on $\mathbf j$)} \\
> \mathbf e_\theta &= -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(right triangle of $\mathbf e_\theta$: opposite leg on $-\mathbf i$, adjacent leg on $\mathbf j$)} \\
> \mathbf e_r\times\mathbf e_\theta &= \cos^2\theta\,\mathbf i\times\mathbf j - \sin^2\theta\,\mathbf j\times\mathbf i \quad &\text{(distributive law; $\mathbf i\times\mathbf i = \mathbf j\times\mathbf j = \mathbf 0$)} \\
> &= \left(\cos^2\theta + \sin^2\theta\right)\mathbf k = \mathbf k \quad &\text{(right-handed: $\mathbf j\times\mathbf i = -\mathbf k$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos\theta\cdot\cos\theta - \left(-\sin\theta\right)\sin\theta\right) = 1 \quad &\text{(expansion along the third row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\theta + \sin^2\theta = 1 \quad &\text{(row 1 times row 1)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{12} &= \cos\theta\sin\theta - \sin\theta\cos\theta = 0 \quad &\text{(row 1 times row 2; row 3 is the unit row of $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** dimensionless direction cosines: $[1]$
> **Meaning:** the columns of the matrix are $\mathbf e_r$, $\mathbf e_\theta$ and $\mathbf k$ written in $\mathcal B_0$; $\mathbf e_r$ follows the particle and $\mathbf e_\theta$ is perpendicular to it in the plane of the motion.

> [!derivation] Position vector of the particle
> **Law:** position vector of a point particle; polar coordinates in the plane of the motion
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 8.3
>
> In the plane of the motion the segment $OP$ is the hypotenuse $r$ of the right triangle whose leg along $\mathbf i$ is $r\cos\theta$ (adjacent to $\theta$) and whose leg along $\mathbf j$ is $r\sin\theta$ (opposite to $\theta$).
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OP} \quad &\text{(definition, Eq. 2.2)} \\
> &= r\,\mathbf e_r \quad &\text{($\mathbf e_r$ is the unit vector from $O$ towards $P$)} \\
> &= r\cos\theta\,\mathbf i + r\sin\theta\,\mathbf j \quad &\text{($\mathbf e_r$ in $\mathcal B_0$)} \\
> \mathbf r_0^P\cdot\mathbf r_0^P &= r^2\cos^2\theta + r^2\sin^2\theta \quad &\text{(components squared and added)} \\
> &= r^2 \quad &\text{($\cos^2\theta + \sin^2\theta = 1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = r\,\mathbf e_r = r\cos\theta\,\mathbf i + r\sin\theta\,\mathbf j, \qquad \lvert\mathbf r_0^P\rvert = r}$$
>
> **Units:** $[r] = [\mathrm{L}]$
> **Meaning:** the position has only a radial component; the attraction acts along minus $\mathbf e_r$, that is along the line $PO$: it is a central force.

### Kinematics

> [!derivation] Derivatives of the polar unit vectors
> **Law:** derivative of a unit vector turning about a fixed axis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \dot\theta\,\mathbf k \quad &\text{($\mathcal B_1$ turns about the fixed $\mathbf k$ with the angle $\theta$)} \\
> \mathbf k\times\mathbf e_r &= \cos\theta\,\mathbf j - \sin\theta\,\mathbf i = \mathbf e_\theta \quad &\text{($\mathbf k\times\mathbf i = \mathbf j$, $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> \mathbf k\times\mathbf e_\theta &= -\sin\theta\,\mathbf j - \cos\theta\,\mathbf i = -\mathbf e_r \quad &\text{(same products)} \\
> \dot{\mathbf e}_r &= \boldsymbol\omega_{10}\times\mathbf e_r = \dot\theta\,\mathbf e_\theta \quad &\text{(Eq. 1.62)} \\
> \dot{\mathbf e}_\theta &= \boldsymbol\omega_{10}\times\mathbf e_\theta = -\dot\theta\,\mathbf e_r \quad &\text{(Eq. 1.62)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf e}_r = \dot\theta\,\mathbf e_\theta, \qquad \dot{\mathbf e}_\theta = -\dot\theta\,\mathbf e_r}$$
>
> **Units:** $[\dot\theta] = [\mathrm{T^{-1}}]$
> **Meaning:** both unit vectors turn with the particle at the rate $\dot\theta$; $\mathbf k$ is fixed.

> [!derivation] Velocity and acceleration of the particle
> **Law:** time derivatives of the position vector in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Notes.pdf, Eq. 8.3
>
> $$\begin{aligned}
> \mathbf v_0^P &= \frac{d}{dt}\left(r\,\mathbf e_r\right) \quad &\text{(definition, Eq. 2.3)} \\
> &= \dot r\,\mathbf e_r + r\,\dot{\mathbf e}_r \quad &\text{(product rule)} \\
> &= \dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta \quad &\text{($\dot{\mathbf e}_r = \dot\theta\,\mathbf e_\theta$)} \\
> \mathbf a_0^P &= \ddot r\,\mathbf e_r + \dot r\,\dot{\mathbf e}_r + \dot r\dot\theta\,\mathbf e_\theta + r\ddot\theta\,\mathbf e_\theta + r\dot\theta\,\dot{\mathbf e}_\theta \quad &\text{(Eq. 2.4; product rule on each term)} \\
> &= \ddot r\,\mathbf e_r + \dot r\dot\theta\,\mathbf e_\theta + \dot r\dot\theta\,\mathbf e_\theta + r\ddot\theta\,\mathbf e_\theta - r\dot\theta^2\,\mathbf e_r \quad &\text{(derivatives of the unit vectors substituted)} \\
> &= \left(\ddot r - r\dot\theta^2\right)\mathbf e_r + \left(r\ddot\theta + 2\dot r\dot\theta\right)\mathbf e_\theta \quad &\text{(grouped along $\mathbf e_r$ and $\mathbf e_\theta$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta, \qquad \mathbf a_0^P = \left(\ddot r - r\dot\theta^2\right)\mathbf e_r + \left(r\ddot\theta + 2\dot r\dot\theta\right)\mathbf e_\theta}$$
>
> **Units:** $[\dot r] = [r\dot\theta] = [\mathrm{L\,T^{-1}}]$; $[\ddot r] = [r\dot\theta^2] = [\dot r\dot\theta] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** $\dot r$ is the rate at which $P$ moves away from $O$ and $r\dot\theta$ the speed at which it turns round $O$; these are the expressions of Notes.pdf, Eq. 8.3.

> [!derivation] Angular momentum per unit mass in polar form
> **Law:** angular momentum about a point, per unit mass; cross products of the polar basis
> **Source:** Notes.pdf, Eq. 4.48; Notes.pdf, Eq. 8.7
>
> $$\begin{aligned}
> \mathbf h &= \mathbf r_0^P\times\mathbf v_0^P \quad &\text{(Eq. 4.48 about $O$, divided by $m$)} \\
> &= r\,\mathbf e_r\times\left(\dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta\right) \quad &\text{(position and velocity substituted)} \\
> &= r\dot r\,\mathbf e_r\times\mathbf e_r + r^2\dot\theta\,\mathbf e_r\times\mathbf e_\theta \quad &\text{(distributive law)} \\
> &= r^2\dot\theta\,\mathbf k \quad &\text{($\mathbf e_r\times\mathbf e_r = \mathbf 0$, $\mathbf e_r\times\mathbf e_\theta = \mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf h = \frac{\mathbf H_{O,0}}{m} = r^2\dot\theta\,\mathbf k, \qquad h = r^2\dot\theta}$$
>
> **Units:** $[r^2\dot\theta] = [\mathrm{L^2\,T^{-1}}]$
> **Meaning:** with $\mathbf k$ along $\mathbf H_{O,0}$ the rate $\dot\theta$ is positive: the particle turns counterclockwise about $\mathbf k$, never backwards.

### Forces and Equations of Motion

The free-body diagram of $P$ shows a single force, the attraction towards $O$. $S_0$ is inertial, so no inertia force acts, and there is no constraint.

![[attachments/EM-SOL/p42-fbd.svg]]

> [!derivation] (a) Torque about O and conservation of the angular momentum
> **Law:** theorem of the angular momentum about a fixed point; moment of a central force
> **Source:** Notes.pdf, Eq. 4.48; Notes.pdf, Eq. 4.53; Notes.pdf, Eq. 4.57; Notes.pdf, Eq. 4.58; [Lecture 4, Slide 5]
>
> The proof uses vectors of $S_0$ in any basis, not the polar coordinates, so it does not assume that the motion is planar. $O$ is fixed, so its velocity is zero.
>
> $$\begin{aligned}
> \mathbf H_{O,0} &= \mathbf r_0^P\times m\,\mathbf v_0^P \quad &\text{(definition, Eq. 4.48)} \\
> \left.\frac{d\mathbf H_{O,0}}{dt}\right|_0 &= \mathbf v_0^P\times m\,\mathbf v_0^P + \mathbf r_0^P\times m\,\mathbf a_0^P \quad &\text{(product rule for the cross product; $O$ fixed)} \\
> &= \mathbf r_0^P\times m\,\mathbf a_0^P \quad &\text{($\mathbf v_0^P\times\mathbf v_0^P = \mathbf 0$)} \\
> &= \mathbf r_0^P\times\mathbf F \quad &\text{(Newton's second law, Notes.pdf, Eq. 4.4)} \\
> &= r\,\mathbf e_r\times\left(-\frac{m\mu}{r^\alpha}\,\mathbf e_r\right) \quad &\text{(position vector and force)} \\
> &= -m\mu\,r^{1-\alpha}\left(\mathbf e_r\times\mathbf e_r\right) \quad &\text{(scalars taken out of the product)} \\
> &= \mathbf 0 \quad &\text{($\mathbf e_r\times\mathbf e_r = \mathbf 0$)} \\
> \left[\mathbf H_{O,0}\right]_0^t &= \int_0^t\mathbf 0\,dt' = \mathbf 0 \quad &\text{(Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M_O = \mathbf r_0^P\times\mathbf F = \mathbf 0, \qquad \mathbf H_{O,0} = m\,\mathbf r_0^P\times\mathbf v_0^P = \mathbf H_{O,0}(0) = \text{const}}$$
>
> **Units:** $[\mathbf H_{O,0}] = [\mathrm{M\,L^2\,T^{-1}}]$; $[\mathbf M_O] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the line of action of the attraction always passes through $O$, so it has no moment about $O$: the three components of the angular momentum are conserved (three scalar laws), for any exponent.

> [!derivation] (a) The motion is planar
> **Law:** the angular momentum is perpendicular to the position vector; scalar triple product
> **Source:** Notes.pdf, Sec. 4.8.1; [Lecture 4, Slide 7]
>
> $$\begin{aligned}
> \mathbf r_0^P\cdot\mathbf H_{O,0} &= \mathbf r_0^P\cdot\left(\mathbf r_0^P\times m\,\mathbf v_0^P\right) \quad &\text{(definition of $\mathbf H_{O,0}$)} \\
> &= m\,\mathbf v_0^P\cdot\left(\mathbf r_0^P\times\mathbf r_0^P\right) \quad &\text{(cyclic permutation of the triple product)} \\
> &= 0 \quad &\text{($\mathbf r_0^P\times\mathbf r_0^P = \mathbf 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P(t)\cdot\mathbf H_{O,0} = 0 \ \text{for all } t, \ \text{with } \mathbf H_{O,0} \ \text{constant}: \ P \ \text{moves in the fixed plane through } O \ \text{perpendicular to } \mathbf H_{O,0}}$$
>
> **Units:** $[\mathrm{L}][\mathrm{M\,L^2\,T^{-1}}]$ on both sides of the zero
> **Meaning:** the vector $\mathbf H_{O,0}$ is fixed by the previous box, and the position stays perpendicular to it: this is the plane $Oxy$ of the table, with $\mathbf k$ along $\mathbf H_{O,0}$. If $\mathbf H_{O,0}$ is zero the velocity is parallel to the position and the particle moves on a fixed line through $O$ (last limiting case).

> [!derivation] (a) Elementary work of the attraction: an exact differential
> **Law:** elementary work of a force; potential energy exists when the work is an exact differential
> **Source:** Notes.pdf, Eq. 4.13; Notes.pdf, Eq. 4.14; Notes.pdf, Sec. 4.4
>
> $$\begin{aligned}
> d\mathbf r_0^P &= dr\,\mathbf e_r + r\,d\mathbf e_r \quad &\text{(differential of $r\,\mathbf e_r$, product rule)} \\
> \mathbf e_r\cdot d\mathbf e_r &= \tfrac12\,d\left(\mathbf e_r\cdot\mathbf e_r\right) \quad &\text{(product rule on the dot product)} \\
> &= \tfrac12\,d(1) = 0 \quad &\text{($\mathbf e_r$ is a unit vector)} \\
> \delta W_0 &= \mathbf F\cdot d\mathbf r_0^P \quad &\text{(Eq. 4.13)} \\
> &= -\frac{m\mu}{r^\alpha}\,\mathbf e_r\cdot\left(dr\,\mathbf e_r + r\,d\mathbf e_r\right) \quad &\text{(force and displacement substituted)} \\
> &= -\frac{m\mu}{r^\alpha}\,dr \quad &\text{($\mathbf e_r\cdot\mathbf e_r = 1$, $\mathbf e_r\cdot d\mathbf e_r = 0$)}
> \end{aligned}$$
>
> $$\boxed{\delta W_0 = -m\mu\,r^{-\alpha}\,dr: \ \text{a function of } r \text{ alone times } dr, \ \text{an exact differential}}$$
>
> **Units:** $[m\mu\,r^{-\alpha}\,dr] = [\mathrm{M}][\mathrm{L^{\alpha+1}\,T^{-2}}][\mathrm{L^{-\alpha}}][\mathrm{L}] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** only the change of the distance to $O$ costs work; the work between two positions depends only on their distances to $O$, not on the path, so the attraction is conservative.

> [!derivation] (a) Potential energy of the attraction
> **Law:** potential energy as minus the work from a reference position; antiderivative and Barrow's rule
> **Source:** Notes.pdf, Eq. 4.14
>
> The work of the previous box is integrated from a reference radius $r_*$, where the potential energy is zero, to the radius $r$; $s$ is the integration variable.
>
> $$\begin{aligned}
> V_0(r) &= -\int_{r_*}^{r}\left(-m\mu\,s^{-\alpha}\right)ds \quad &\text{(Eq. 4.14 with the work of the previous box)} \\
> &= m\mu\int_{r_*}^{r}s^{-\alpha}\,ds \quad &\text{(the two minus signs cancel)} \\
> \alpha \ne 1:\quad V_0(r) &= m\mu\left[\frac{s^{1-\alpha}}{1-\alpha}\right]_{r_*}^{r} \quad &\text{(antiderivative of $s^{-\alpha}$)} \\
> &= m\mu\,\frac{r^{1-\alpha} - r_*^{1-\alpha}}{1-\alpha} \quad &\text{(Barrow's rule)} \\
> \alpha \gt 1,\ r_*\to\infty:\quad V_0(r) &= \frac{m\mu\,r^{1-\alpha}}{1-\alpha} \quad &\text{($r_*^{1-\alpha}\to 0$ because $1-\alpha \lt 0$)} \\
> &= -\frac{m\mu}{(\alpha-1)\,r^{\alpha-1}} \quad &\text{(sign moved to the denominator)} \\
> \alpha = 1:\quad V_0(r) &= m\mu\left[\ln s\right]_{r_*}^{r} \quad &\text{(antiderivative of $s^{-1}$)} \\
> &= m\mu\ln\frac{r}{r_*} \quad &\text{(Barrow's rule; difference of logarithms)} \\
> \alpha \gt 1:\quad \frac{dV_0}{dr} &= -\frac{m\mu}{\alpha-1}\left(1-\alpha\right)r^{-\alpha} \quad &\text{(derivative of the power $r^{1-\alpha}$)} \\
> &= m\mu\,r^{-\alpha} \quad &\text{($(1-\alpha)/(\alpha-1) = -1$)} \\
> \alpha = 1:\quad \frac{dV_0}{dr} &= \frac{m\mu}{r} \quad &\text{(derivative of the logarithm)}
> \end{aligned}$$
>
> $$\boxed{V_0(r) = -\frac{m\mu}{(\alpha-1)\,r^{\alpha-1}} \ (\alpha = 2, 3, 4), \qquad V_0(r) = m\mu\ln\frac{r}{r_*} \ (\alpha = 1), \qquad \frac{dV_0}{dr} = m\mu\,r^{-\alpha}}$$
>
> **Units:** $[m\mu\,r^{1-\alpha}] = [\mathrm{M}][\mathrm{L^{\alpha+1}\,T^{-2}}][\mathrm{L^{1-\alpha}}] = [\mathrm{M\,L^2\,T^{-2}}]$; the logarithm is of a ratio of lengths
> **Meaning:** minus the derivative of the potential is the radial component of the force, as it must be. For the exponents above 1 the potential tends to zero far away; for the exponent 1 it grows without bound with $r$, which will forbid the escape.

> [!derivation] (a) Conservation of the mechanical energy
> **Law:** theorem of the kinetic energy; the attraction derives from the potential of the previous box; Barrow's rule
> **Source:** Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31
>
> $$\begin{aligned}
> \frac{d}{dt}\left(\tfrac12 m\,\mathbf v_0^P\cdot\mathbf v_0^P\right) &= m\,\mathbf a_0^P\cdot\mathbf v_0^P \quad &\text{(product rule on the dot product)} \\
> &= \mathbf F\cdot\mathbf v_0^P \quad &\text{(Newton's second law, Eq. 4.11)} \\
> &= -\frac{m\mu}{r^\alpha}\,\mathbf e_r\cdot\mathbf v_0^P \quad &\text{(force substituted)} \\
> \mathbf r_0^P\cdot\mathbf v_0^P &= \tfrac12\,\frac{d}{dt}\left(\mathbf r_0^P\cdot\mathbf r_0^P\right) \quad &\text{(product rule on the dot product)} \\
> &= \tfrac12\,\frac{d}{dt}\left(r^2\right) \quad &\text{($\mathbf r_0^P\cdot\mathbf r_0^P = r^2$)} \\
> &= r\dot r \quad &\text{(chain rule)} \\
> \mathbf e_r\cdot\mathbf v_0^P &= \dot r \quad &\text{(divided by $r$; $\mathbf e_r$ is $\mathbf r_0^P/r$)} \\
> \frac{d}{dt}\left(\tfrac12 m\,\mathbf v_0^P\cdot\mathbf v_0^P\right) &= -m\mu\,r^{-\alpha}\,\dot r \quad &\text{(substituted)} \\
> &= -\frac{dV_0}{dr}\,\dot r \quad &\text{(derivative of the potential, previous box)} \\
> &= -\frac{d}{dt}V_0\big(r(t)\big) \quad &\text{(chain rule)} \\
> \frac{d}{dt}\left(\tfrac12 m\,\mathbf v_0^P\cdot\mathbf v_0^P + V_0\right) &= 0 \quad &\text{(both terms on the left)} \\
> \left[\tfrac12 m\,\mathbf v_0^P\cdot\mathbf v_0^P + V_0\right]_0^t &= 0 \quad &\text{(Barrow's rule between $0$ and $t$)}
> \end{aligned}$$
>
> $$\boxed{E_0 = \tfrac12 m\,\mathbf v_0^P\cdot\mathbf v_0^P + V_0(r) = \text{const}}$$
>
> **Units:** $[\tfrac12 m v^2] = [V_0] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the only force does work that depends on the distance to $O$ alone, so the kinetic energy gained when $P$ falls towards $O$ is exactly the potential energy lost: the mechanical energy is a second conserved quantity. This completes part (a).

> [!derivation] Newton's second law in the plane of the motion
> **Law:** Newton's second law in an inertial frame, projected on the polar basis
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 8.4; Notes.pdf, Eq. 8.5; Notes.pdf, Eq. 8.6
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= -\frac{m\mu}{r^\alpha}\,\mathbf e_r \quad &\text{(the only force; Eq. 4.4)} \\
> \mathbf e_r:\ m\left(\ddot r - r\dot\theta^2\right) &= -\frac{m\mu}{r^\alpha} \quad &\text{(dot product with $\mathbf e_r$)} \\
> \mathbf e_\theta:\ m\left(r\ddot\theta + 2\dot r\dot\theta\right) &= 0 \quad &\text{(dot product with $\mathbf e_\theta$)} \\
> \mathbf k:\ 0 &= 0 \quad &\text{(planar motion: no component along $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\ddot r - r\dot\theta^2 = -\frac{\mu}{r^\alpha}, \qquad r\ddot\theta + 2\dot r\dot\theta = 0}$$
>
> **Units:** $[\ddot r] = [r\dot\theta^2] = [\mu\,r^{-\alpha}] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** two equations for the two unknown functions $r(t)$ and $\theta(t)$; with the exponent 2 they are Notes.pdf, Eq. 8.5 and Eq. 8.6.

> [!derivation] Areal integral: the angular momentum per unit mass is constant
> **Law:** the transverse equation times r is an exact derivative; Barrow's rule
> **Source:** Notes.pdf, Eq. 8.6; Notes.pdf, Eq. 8.7; [Lecture 4, Slide 12]
>
> $$\begin{aligned}
> \frac{d}{dt}\left(r^2\dot\theta\right) &= 2r\dot r\dot\theta + r^2\ddot\theta \quad &\text{(product rule; chain rule on $r^2$)} \\
> &= r\left(r\ddot\theta + 2\dot r\dot\theta\right) \quad &\text{(common factor $r$)} \\
> &= 0 \quad &\text{(transverse equation)} \\
> \left[r^2\dot\theta\right]_0^t &= 0 \quad &\text{(Barrow's rule)} \\
> \dot\theta &= \frac{h}{r^2} = h\,u^2 \quad &\text{(the constant is $h$, kinematics box; $u = 1/r$)}
> \end{aligned}$$
>
> $$\boxed{r^2\dot\theta = h = \text{const}, \qquad \dot\theta = h\,u^2}$$
>
> **Units:** $[h] = [\mathrm{L^2\,T^{-1}}]$; $[h\,u^2] = [\mathrm{L^2\,T^{-1}}][\mathrm{L^{-2}}] = [\mathrm{T^{-1}}]$
> **Meaning:** the $\mathbf k$ component of the conserved angular momentum of part (a), per unit mass; the angular rate grows as the particle approaches $O$.

> [!derivation] (b) Second-order equation for u as a function of theta
> **Law:** change of independent variable from t to theta (chain rule); radial equation of motion
> **Source:** Notes.pdf, Eq. 8.9; Notes.pdf, Eq. 8.10; Notes.pdf, Eq. 8.11; Notes.pdf, Eq. 8.12; [Lecture 4, Slide 13]
>
> With $h$ nonzero the rate $\dot\theta = hu^2$ never vanishes, so $\theta$ grows monotonically with $t$ and can replace it as the independent variable: $u = u(\theta(t))$, and primes are derivatives with respect to $\theta$.
>
> $$\begin{aligned}
> \dot r &= \frac{d}{dt}\left(u^{-1}\right) = -u^{-2}\,\dot u \quad &\text{(chain rule on $r = u^{-1}$)} \\
> \dot u &= u'\,\dot\theta \quad &\text{(chain rule on $u(\theta(t))$)} \\
> \dot r &= -u^{-2}\,u'\,h\,u^2 \quad &\text{($\dot\theta = hu^2$ substituted)} \\
> &= -h\,u' \quad &\text{($u^{-2}u^2 = 1$)} \\
> \ddot r &= -h\,\frac{d}{dt}\left(u'\right) \quad &\text{($h$ constant)} \\
> &= -h\,u''\,\dot\theta \quad &\text{(chain rule on $u'(\theta(t))$)} \\
> &= -h^2u^2\,u'' \quad &\text{($\dot\theta = hu^2$)} \\
> r\dot\theta^2 &= u^{-1}\left(h\,u^2\right)^2 \quad &\text{($r = u^{-1}$, $\dot\theta = hu^2$)} \\
> &= h^2u^3 \quad &\text{(powers of $u$ collected)} \\
> -h^2u^2\,u'' - h^2u^3 &= -\mu\,u^\alpha \quad &\text{(radial equation; $r^{-\alpha} = u^\alpha$)} \\
> u'' + u &= \frac{\mu}{h^2}\,u^{\alpha-2} \quad &\text{(divided by $-h^2u^2$)}
> \end{aligned}$$
>
> $$\boxed{u'' + u = K\,u^{\alpha-2}, \qquad K = \frac{\mu}{h^2}}$$
>
> **Units:** $[u''] = [u] = [\mathrm{L^{-1}}]$ ($\theta$ is dimensionless); $[K\,u^{\alpha-2}] = [\mathrm{L^{\alpha+1}\,T^{-2}}][\mathrm{L^{-4}\,T^{2}}][\mathrm{L^{2-\alpha}}] = [\mathrm{L^{-1}}]$
> **Meaning:** the equation of the orbit, free of time. For the exponent 2 it is the linear equation of a forced harmonic oscillator, Notes.pdf, Eq. 8.12; for 3 it is linear and homogeneous; for 1 and 4 it is nonlinear.

### Answers and Checks

#### (c) First integral and limits of the motion

> [!derivation] First integral of the equation of u
> **Law:** the equation multiplied by 2u' is an exact derivative (chain rule); Barrow's rule between 0 and theta
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 8.12
>
> Write $\Phi(u)$ for an antiderivative of $u^{\alpha-2}$: $\Phi(u) = u^{\alpha-1}/(\alpha-1)$ for $\alpha \ne 1$ and $\Phi(u) = \ln(u/u_0)$ for $\alpha = 1$; in both cases its derivative is $u^{\alpha-2}$.
>
> $$\begin{aligned}
> 2u'u'' + 2u\,u' &= 2K\,u^{\alpha-2}\,u' \quad &\text{(equation of part (b) times $2u'$)} \\
> \frac{d}{d\theta}\left(u'^2\right) &= 2u'u'' \quad &\text{(chain rule)} \\
> \frac{d}{d\theta}\left(u^2\right) &= 2u\,u' \quad &\text{(chain rule)} \\
> \frac{d}{d\theta}\,\Phi(u) &= u^{\alpha-2}\,u' \quad &\text{(chain rule; $\Phi'(u) = u^{\alpha-2}$)} \\
> \frac{d}{d\theta}\left[u'^2 + u^2 - 2K\,\Phi(u)\right] &= 0 \quad &\text{(the first row is this sum of derivatives)} \\
> \left[u'^2 + u^2 - 2K\,\Phi(u)\right]_0^\theta &= 0 \quad &\text{(Barrow's rule)} \\
> u'^2 + W(u) &= u_0'^2 + W(u_0) \quad &\text{(with $W(u) \equiv u^2 - 2K\,\Phi(u)$)}
> \end{aligned}$$
>
> $$\boxed{u'^2 + W(u) = E^*, \qquad W(u) = u^2 - 2K\,\Phi(u), \qquad E^* = u_0'^2 + W(u_0)}$$
>
> **Units:** $[u'^2] = [u^2] = [\mathrm{L^{-2}}]$; $[K\,\Phi] = [\mathrm{L^{\alpha-3}}][\mathrm{L^{1-\alpha}}] = [\mathrm{L^{-2}}]$ (for the exponent 1, $K$ is in $\mathrm{L^{-2}}$ and $\Phi$ is dimensionless)
> **Meaning:** a first-order equation for $u(\theta)$: $u'$ is known from $u$ alone, and the constant $E^*$ is fixed by the values $u_0$ and $u_0'$ at the initial instant, as the statement asks.

> [!derivation] The first integral is the mechanical energy (check, exponents 2, 3, 4)
> **Law:** energy of part (a) written with the change of variable of part (b)
> **Source:** Notes.pdf, Eq. 4.31; Notes.pdf, Eq. 8.10; Notes.pdf, Eq. 8.19
>
> $$\begin{aligned}
> \dot r &= -h\,u' \quad &\text{(box of part (b))} \\
> r\dot\theta &= u^{-1}\,h\,u^2 \quad &\text{($r = u^{-1}$, $\dot\theta = hu^2$)} \\
> &= h\,u \quad &\text{(powers of $u$ collected)} \\
> \mathbf v_0^P\cdot\mathbf v_0^P &= \dot r^2 + \left(r\dot\theta\right)^2 \quad &\text{($\mathcal B_1$ orthonormal)} \\
> &= h^2\left(u'^2 + u^2\right) \quad &\text{(the two rates substituted)} \\
> \frac{E_0}{m} &= \tfrac12 h^2\left(u'^2 + u^2\right) - \frac{\mu\,u^{\alpha-1}}{\alpha-1} \quad &\text{(energy of part (a); $r^{1-\alpha} = u^{\alpha-1}$)} \\
> \frac{2E_0}{m h^2} &= u'^2 + u^2 - \frac{2K\,u^{\alpha-1}}{\alpha-1} \quad &\text{(times $2/h^2$; $K = \mu/h^2$)} \\
> &= u'^2 + W(u) \quad &\text{(definition of $W$, $\alpha \ne 1$)}
> \end{aligned}$$
>
> $$\boxed{E^* = \frac{2E_0}{m h^2} \quad (\alpha = 2, 3, 4)}$$
>
> **Units:** $[E_0/(m h^2)] = [\mathrm{L^2\,T^{-2}}][\mathrm{L^{-4}\,T^2}] = [\mathrm{L^{-2}}]$
> **Meaning:** the first integral is the energy of part (a) per unit of $m h^2/2$, and $W$ is the effective potential: the centrifugal term $u^2$ (it comes from the kinetic energy of the turning) minus the attraction. For the exponent 1 the constant differs only by the reference of the logarithm.

> [!derivation] Allowed values of u and turning points
> **Law:** a square cannot be negative; derivative of the first integral
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28
>
> $$\begin{aligned}
> u'^2 &= E^* - W(u) \ge 0 \quad &\text{(first integral; square of a real number)} \\
> 2u'u'' + W'(u)\,u' &= 0 \quad &\text{(derivative of the first integral with respect to $\theta$; chain rule)} \\
> u'' &= -\tfrac12\,W'(u) \quad &\text{(divided by $2u'$ where $u' \ne 0$)} \\
> W'(u) &= 2u - 2K\,u^{\alpha-2} \quad &\text{(derivative of $W$; $\Phi'(u) = u^{\alpha-2}$)} \\
> u'' &= -u + K\,u^{\alpha-2} \quad &\text{(substituted: the equation of part (b) is recovered)}
> \end{aligned}$$
>
> $$\boxed{W(u) \le E^* \ \text{along the motion}; \ \text{at a root } u_t \text{ of } W(u_t) = E^* \text{ with } W'(u_t) \ne 0, \ u' = 0 \text{ and } u'' = -\tfrac12 W'(u_t) \ne 0}$$
>
> **Units:** $[W] = [E^*] = [\mathrm{L^{-2}}]$; $[W'] = [u''] = [\mathrm{L^{-1}}]$
> **Meaning:** $u$ can only take the values where the curve $W$ lies below the level $E^*$; at a simple root $u'$ vanishes and $u''$ pushes $u$ back into the allowed region (a turning point, Notes.pdf, Eq. 4.28). Since $\dot\theta = hu^2$ is positive, $u'$ has the sign of $\dot u$: a growing $u$ means $P$ approaching $O$. Hence (i) escape ($u \to 0$) needs the allowed region to reach $u = 0$; (ii) reaching $O$ ($u \to \infty$) needs it to be unbounded above; (iii) oscillation needs $u_0$ inside a bounded interval of positive values limited by two simple roots.

![[attachments/EM-SOL/p42-weff.svg]]

#### Exponent 2: inverse square

> [!derivation] Exponent 2: conic orbits
> **Law:** first integral with the general solution of the linear equation of the orbit
> **Source:** Notes.pdf, Eq. 8.12; Notes.pdf, Eq. 8.13; Notes.pdf, Eq. 8.14; [Lecture 4, Slide 14]
>
> $$\begin{aligned}
> W(u) &= u^2 - 2K\,u \quad &\text{($\Phi(u) = u$)} \\
> &= \left(u - K\right)^2 - K^2 \quad &\text{(square completed)} \\
> E^* &= u_0'^2 + u_0^2 - 2K\,u_0 \quad &\text{(initial data)} \\
> u &= K + A\cos\left(\theta - \theta_p\right) \quad &\text{(general solution of $u'' + u = K$, Eq. 8.13; $A \ge 0$)} \\
> u' &= -A\sin\left(\theta - \theta_p\right) \quad &\text{(derivative)} \\
> A^2\sin^2\left(\theta - \theta_p\right) + A^2\cos^2\left(\theta - \theta_p\right) &= E^* + K^2 \quad &\text{(substituted in $u'^2 + (u - K)^2 = E^* + K^2$)} \\
> A^2 &= E^* + K^2 \quad &\text{($\cos^2 + \sin^2 = 1$)} \\
> e &= \frac{A}{K} \quad &\text{(eccentricity of Eq. 8.13, where $A = Ke$)} \\
> &= \sqrt{1 + \frac{E^*}{K^2}} \quad &\text{($A$ of the previous row)} \\
> u_{\min} &= K\left(1 - e\right), \quad u_{\max} = K\left(1 + e\right) \quad &\text{(cosine at $-1$ and $+1$)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} u = K\left[1 + e\cos\left(\theta - \theta_p\right)\right], \quad e = \sqrt{1 + E^*/K^2}, \quad E^* = u_0'^2 + u_0^2 - 2Ku_0 \cr \text{(i) escape} \iff E^* \ge 0 \ (e \ge 1); \quad \text{(ii) never}; \cr \text{(iii) oscillation between } K(1-e) \text{ and } K(1+e) \iff -K^2 \lt E^* \lt 0; \ \text{circle } u = K \text{ for } E^* = -K^2 \end{array}}$$
>
> **Units:** $[K] = [\mathrm{L^{-1}}]$ for the exponent 2; $e$ is dimensionless
> **Meaning:** $u$ reaches zero only if the cosine can reach $-1/e$, that is if $e \ge 1$ (parabola or hyperbola): the particle escapes, even if it first moves inward and passes the pericentre. $u$ never exceeds $K(1 + e)$, so $O$ is never reached. For $e$ below 1 (negative energy) $u$ oscillates between the pericentre and the apocentre of an ellipse, Kepler's first law.

#### Exponent 1

> [!derivation] Exponent 1: every orbit is bounded
> **Law:** first integral; shape of the effective potential (derivatives and limits)
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28
>
> $$\begin{aligned}
> W(u) &= u^2 - 2K\ln\frac{u}{u_0} \quad &\text{($\Phi(u) = \ln(u/u_0)$)} \\
> E^* &= u_0'^2 + u_0^2 \quad &\text{($\ln 1 = 0$)} \\
> W'(u) &= 2u - \frac{2K}{u} \quad &\text{(derivative)} \\
> 2u_c - \frac{2K}{u_c} &= 0 \quad &\text{(stationary point)} \\
> u_c &= \sqrt{K} \quad &\text{(times $u_c/2$; positive root)} \\
> W''(u) &= 2 + \frac{2K}{u^2} \gt 0 \quad &\text{(second derivative: $W$ is strictly convex)} \\
> \lim_{u\to 0^+}W(u) &= +\infty \quad &\text{($-\ln(u/u_0) \to +\infty$)} \\
> \lim_{u\to\infty}W(u) &= +\infty \quad &\text{($u^2$ grows faster than the logarithm)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} W \text{ has a single minimum at } u_c = \sqrt{K} = \sqrt{\mu}/h \text{ and tends to } +\infty \text{ at both ends} \cr \text{(i) never}; \quad \text{(ii) never}; \quad \text{(iii) always, between the two roots } u_1 \lt u_c \lt u_2 \text{ of } W = E^*; \cr \text{circle } r = h/\sqrt{\mu} \text{ when } u_0 = \sqrt{K} \text{ and } u_0' = 0 \end{array}}$$
>
> **Units:** $[K] = [\mathrm{L^{-2}}]$ for the exponent 1, so $[\sqrt K] = [\mathrm{L^{-1}}]$
> **Meaning:** the potential well is infinitely deep on both sides: the logarithmic potential grows without bound far away and the centrifugal term near $O$. Any level above the minimum cuts the convex curve exactly twice, so every motion with nonzero angular momentum oscillates between two radii.

#### Exponent 3

> [!derivation] Exponent 3: the orbit equation
> **Law:** first integral and equation of part (b) with the exponent 3
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 8.9; Notes.pdf, Eq. 8.11
>
> $$\begin{aligned}
> W(u) &= u^2 - K\,u^2 \quad &\text{($\Phi(u) = u^2/2$)} \\
> &= \left(1 - K\right)u^2 \quad &\text{(common factor $u^2$)} \\
> u'' + \left(1 - K\right)u &= 0 \quad &\text{(equation of part (b): $u^{\alpha-2} = u$)} \\
> E^* &= u_0'^2 + \left(1 - K\right)u_0^2 \quad &\text{(initial data)}
> \end{aligned}$$
>
> $$\boxed{u'' + \left(1 - K\right)u = 0, \qquad u'^2 + \left(1 - K\right)u^2 = E^*, \qquad K = \frac{\mu}{h^2} \ \text{dimensionless}}$$
>
> **Units:** $[K] = [\mathrm{L^{4}\,T^{-2}}]/[\mathrm{L^4\,T^{-2}}] = [1]$ for the exponent 3
> **Meaning:** the attraction and the centrifugal term both vary as $u^3$ in the radial equation, so the sign of $1 - K$ alone decides the type of motion; the three cases follow.

> [!derivation] Exponent 3 with K below 1: the particle always escapes
> **Law:** harmonic solution of the linear equation; initial conditions
> **Source:** Notes.pdf, Eq. 5.6; Notes.pdf, Eq. 5.10
>
> Write $\lambda = \sqrt{1 - K}$, positive.
>
> $$\begin{aligned}
> u &= A\cos\left(\lambda\theta + \delta\right) \quad &\text{(general solution of $u'' + \lambda^2u = 0$; $A \ge 0$)} \\
> u_0 &= A\cos\delta \quad &\text{(value at $\theta = 0$)} \\
> u_0' &= -\lambda A\sin\delta \quad &\text{(derivative at $\theta = 0$)} \\
> A^2\cos^2\delta + A^2\sin^2\delta &= u_0^2 + \frac{u_0'^2}{\lambda^2} \quad &\text{(the two rows squared and added)} \\
> A^2 &= u_0^2 + \frac{u_0'^2}{\lambda^2} \quad &\text{($\cos^2 + \sin^2 = 1$)} \\
> u &= 0 \ \text{at} \ \lambda\theta_e + \delta = \frac{\pi}{2} \quad &\text{(first zero of the cosine after $\theta = 0$)}
> \end{aligned}$$
>
> $$\boxed{K \lt 1: \ u \le A = \sqrt{u_0^2 + u_0'^2/(1 - K)}, \ u \text{ reaches } 0 \text{ at a finite angle}: \ \text{(i) always; (ii) never; (iii) never}}$$
>
> **Units:** $[A] = [u_0] = [u_0'] = [\mathrm{L^{-1}}]$; $\lambda$ dimensionless
> **Meaning:** the centrifugal term wins: $W$ is an upward parabola with its minimum at $u = 0$, so the particle reaches infinity along an asymptote; if it starts moving inward it is first reflected at the closest distance $1/A$.

> [!derivation] Exponent 3 with K above 1: escape or fall, decided by the initial data
> **Law:** exponential solution of the linear equation (characteristic equation with two real roots); initial conditions
> **Source:** Notes.pdf, Eq. 5.21; Notes.pdf, Sec. 5.3.2; Notes.pdf, Eq. 5.30
>
> Write $\lambda = \sqrt{K - 1}$, positive.
>
> $$\begin{aligned}
> u'' - \lambda^2 u &= 0 \quad &\text{(equation with $1 - K = -\lambda^2$)} \\
> p^2e^{p\theta} - \lambda^2e^{p\theta} &= 0 \quad &\text{(trial solution $u = e^{p\theta}$ substituted, as in Eq. 5.21)} \\
> p^2 - \lambda^2 &= 0 \quad &\text{(divided by $e^{p\theta} \ne 0$: characteristic equation)} \\
> p &= \pm\lambda \quad &\text{(two real roots)} \\
> u &= C_1e^{\lambda\theta} + C_2e^{-\lambda\theta} \quad &\text{(superposition of the two real exponentials, as in Eq. 5.30)} \\
> u_0 &= C_1 + C_2 \quad &\text{(value at $\theta = 0$)} \\
> u_0' &= \lambda\left(C_1 - C_2\right) \quad &\text{(derivative at $\theta = 0$)} \\
> C_1 &= \tfrac12\left(u_0 + \frac{u_0'}{\lambda}\right), \quad C_2 = \tfrac12\left(u_0 - \frac{u_0'}{\lambda}\right) \quad &\text{(sum and difference of the two rows)} \\
> E^* &= u_0'^2 - \lambda^2u_0^2 \quad &\text{(first integral with $1 - K = -\lambda^2$)} \\
> &= -\lambda^2\left(u_0 + \frac{u_0'}{\lambda}\right)\left(u_0 - \frac{u_0'}{\lambda}\right) \quad &\text{(difference of squares)} \\
> &= -4\lambda^2C_1C_2 \quad &\text{($C_1$ and $C_2$ substituted)} \\
> C_1 \lt 0:\quad e^{2\lambda\theta_e} &= \frac{C_2}{-C_1} \quad &\text{(zero of $u$; $C_2 = u_0 - C_1 \gt -C_1 \gt 0$)} \\
> \theta_e &= \frac{1}{2\lambda}\ln\frac{C_2}{-C_1} \gt 0 \quad &\text{(logarithm; the ratio exceeds 1)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} K \gt 1: \ \text{(ii) } u \to \infty \iff C_1 \gt 0 \iff u_0' \gt -\sqrt{K - 1}\,u_0; \cr \text{(i) escape at } \theta_e \iff C_1 \lt 0 \iff u_0' \lt -\sqrt{K - 1}\,u_0; \ \text{limit } C_1 = 0: \ u = u_0e^{-\lambda\theta} \to 0 \text{ as } \theta \to \infty; \ \text{(iii) never} \end{array}}$$
>
> **Units:** $[C_1] = [C_2] = [\mathrm{L^{-1}}]$; $\lambda\theta$ dimensionless
> **Meaning:** the attraction wins over the centrifugal term: with $C_1$ positive the growing exponential dominates and $P$ spirals into $O$ (when $C_2$ is negative, $u$ starts at $u_0$ with a positive slope and keeps growing); with $C_1$ negative $u$ falls to zero at the finite angle $\theta_e$. The energy row agrees with the shape of $W$, a downward parabola with its top at $u = 0$: a negative $E^*$ means $C_1$ and $C_2$ of the same sign, both positive, and a fall into $O$.

> [!derivation] Exponent 3 with K above 1: boundary case C1 equal to zero
> **Law:** general solution of the previous box with the growing term removed; areal integral for the time; Barrow's rule
> **Source:** Notes.pdf, Eq. 5.30; Notes.pdf, Eq. 8.7
>
> $$\begin{aligned}
> \tfrac12\left(u_0 + \frac{u_0'}{\lambda}\right) &= 0 \quad &\text{(the coefficient $C_1$ of the previous box set to zero)} \\
> u_0' &= -\lambda\,u_0 = -\sqrt{K - 1}\,u_0 \quad &\text{(solved for $u_0'$)} \\
> C_2 &= u_0 \quad &\text{($C_2 = u_0 - C_1$)} \\
> u &= u_0\,e^{-\lambda\theta} \quad &\text{(general solution with $C_1 = 0$)} \\
> E^* &= 0 \quad &\text{($E^* = -4\lambda^2C_1C_2$, previous box)} \\
> dt &= \frac{d\theta}{h\,u^2} \quad &\text{(areal integral: $\dot\theta = h/r^2 = h\,u^2$)} \\
> &= \frac{e^{2\lambda\theta}}{h\,u_0^2}\,d\theta \quad &\text{($u$ substituted)} \\
> t(\theta) &= \left[\frac{e^{2\lambda\bar\theta}}{2\lambda\,h\,u_0^2}\right]_0^\theta \quad &\text{(antiderivative of $e^{2\lambda\bar\theta}$; Barrow's rule from $0$ to $\theta$)} \\
> &= \frac{e^{2\lambda\theta} - 1}{2\lambda\,h\,u_0^2} \quad &\text{(limits substituted)}
> \end{aligned}$$
>
> $$\boxed{u_0' = -\sqrt{K - 1}\,u_0: \ u = u_0\,e^{-\lambda\theta} \to 0 \ \text{and} \ t \to \infty \ \text{as} \ \theta \to \infty: \ \text{outward spiral that reaches infinity only asymptotically}}$$
>
> **Units:** $[\lambda\,h\,u_0^2] = [\mathrm{L^2\,T^{-1}}][\mathrm{L^{-2}}] = [\mathrm{T^{-1}}]$, so $[t] = [\mathrm{T}]$
> **Meaning:** on the boundary between fall and escape the particle sits on top of the flat-topped barrier of zero level: it spirals outwards with infinitely many turns and never arrives at a finite angle or a finite time; it neither falls nor oscillates.

> [!derivation] Exponent 3 with K equal to 1: reciprocal spiral
> **Law:** equation of part (b) with the linear term cancelled; Barrow's rule twice
> **Source:** Notes.pdf, Eq. 8.9; Notes.pdf, Eq. 8.11
>
> $$\begin{aligned}
> u'' &= 0 \quad &\text{(equation with $1 - K = 0$)} \\
> u' &= u_0' \quad &\text{(Barrow's rule from $0$ to $\theta$)} \\
> u &= u_0 + u_0'\,\theta \quad &\text{(Barrow's rule again)}
> \end{aligned}$$
>
> $$\boxed{K = 1: \ u = u_0 + u_0'\theta; \ u_0' \gt 0: \text{(ii)}; \ u_0' \lt 0: \text{(i) at } \theta_e = u_0/\lvert u_0'\rvert; \ u_0' = 0: \text{circle}; \ \text{(iii) never}}$$
>
> **Units:** $[u_0'\theta] = [\mathrm{L^{-1}}]$
> **Meaning:** the attraction exactly balances the centrifugal term for every radius: the circle exists for any radius but any radial push makes the particle spiral in or out.

#### Exponent 4

> [!derivation] Exponent 4: shape of the effective potential
> **Law:** derivatives, stationary points and limits of W
> **Source:** Notes.pdf, Eq. 4.28
>
> $$\begin{aligned}
> W(u) &= u^2 - \tfrac23 K\,u^3 \quad &\text{($\Phi(u) = u^3/3$)} \\
> W'(u) &= 2u - 2K\,u^2 \quad &\text{(derivative)} \\
> &= 2u\left(1 - K\,u\right) \quad &\text{(common factor $2u$)} \\
> W'(u) &\gt 0 \ \text{for} \ 0 \lt u \lt \tfrac1K, \quad W'(u) \lt 0 \ \text{for} \ u \gt \tfrac1K \quad &\text{(sign of $1 - Ku$)} \\
> W\left(\tfrac1K\right) &= \frac{1}{K^2} - \frac{2}{3K^2} \quad &\text{(value at the maximum $u_b = 1/K$)} \\
> &= \frac{1}{3K^2} \quad &\text{(fractions added)} \\
> u_z^2\left(1 - \tfrac23 K\,u_z\right) &= 0 \quad &\text{(zeros of $W$)} \\
> u_z &= \frac{3}{2K} \quad &\text{(the nonzero root)} \\
> \lim_{u\to\infty}W(u) &= -\infty \quad &\text{(the cubic term dominates)}
> \end{aligned}$$
>
> $$\boxed{W: 0 \text{ at } u = 0, \ \text{increasing to } W_{\max} = \frac{1}{3K^2} \text{ at } u_b = \frac1K, \ \text{then decreasing through } 0 \text{ at } u_z = \frac{3}{2K} \text{ to } -\infty}$$
>
> **Units:** $[K] = [\mathrm{L}]$ for the exponent 4; $[u_b] = [u_z] = [\mathrm{L^{-1}}]$, $[W_{\max}] = [\mathrm{L^{-2}}]$
> **Meaning:** a barrier, not a well: there is no minimum at a positive $u$, only the unstable circular orbit $u = u_b$ on top of the barrier.

> [!derivation] Exponent 4: motion for each level of the first integral
> **Law:** allowed region below the level E* (previous boxes); W is monotonic on each side of the barrier
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28
>
> $E^*$ is fixed by the data, $E^* = u_0'^2 + u_0^2 - \tfrac23 K u_0^3$, and $u_0$ lies in the allowed region.
>
> $$\begin{aligned}
> E^* \gt W_{\max}:\quad W(u) &\lt E^* \ \text{for all} \ u \gt 0 \quad &\text{($W \le W_{\max}$): no turning point; the sign of $u_0'$ decides} \\
> E^* = W_{\max}:\quad W(u) &= E^* \ \text{only at} \ u_b \quad &\text{(double root): unstable circle, or asymptotic approach to $u_b$} \\
> 0 \lt E^* \lt W_{\max}:\quad W(u_1) &= W(u_2) = E^*, \ 0 \lt u_1 \lt u_b \lt u_2 \lt u_z \quad &\text{(one root on each monotonic branch)} \\
> 0 \lt E^* \lt W_{\max}:\quad u &\in \left(0, u_1\right] \ \text{or} \ u \in \left[u_2, \infty\right) \quad &\text{(the barrier between $u_1$ and $u_2$ is forbidden)} \\
> E^* = 0:\quad u &\in \{0\}\cup\left[u_z, \infty\right) \quad &\text{(roots $0$, double, and $u_z$)} \\
> E^* \lt 0:\quad u &\in \left[u_2, \infty\right), \ u_2 \gt u_z \quad &\text{(single root on the decreasing branch)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \text{(i) escape: } 0 \lt E^* \lt W_{\max},\ u_0 \lt u_b; \ \text{or } E^* = W_{\max},\ u_0 \lt u_b,\ u_0' \lt 0; \ \text{or } E^* \gt W_{\max},\ u_0' \lt 0 \cr \text{(ii) reaches } O\text{: } E^* \le 0; \ \text{or } 0 \lt E^* \lt W_{\max},\ u_0 \gt u_b; \ \text{or } E^* = W_{\max},\ u_0 \gt u_b,\ u_0' \gt 0; \ \text{or } E^* \gt W_{\max},\ u_0' \gt 0 \cr \text{(iii) never: } W \text{ has no minimum at positive } u; \ \text{only the unstable circle } u_0 = u_b = h^2/\mu,\ u_0' = 0 \end{array}}$$
>
> **Units:** $[E^*] = [W_{\max}] = [\mathrm{L^{-2}}]$
> **Meaning:** a particle below the barrier stays on its side: outside it escapes (after a reflection at $u_1$ if it was moving in), inside it falls to $O$ (after a reflection at $u_2$ if it was moving out). Above the barrier nothing reflects it, so it escapes if it moves outward and falls if it moves inward. On the separatrix $E^* = W_{\max}$ the cases moving towards $u_b$ approach the unstable circle without reaching it.

> [!derivation] Exponent 4 on the separatrix: asymptotic approach to the unstable circle
> **Law:** first integral with the level of the top of the barrier; factorisation of the double root; Barrow's rule
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28; Notes.pdf, Eq. 8.7
>
> $$\begin{aligned}
> u'^2 &= W_{\max} - W(u) \quad &\text{(first integral with $E^* = W_{\max}$)} \\
> &= \frac{1}{3K^2} - u^2 + \tfrac23 K\,u^3 \quad &\text{($W_{\max}$ and $W$ of the shape box)} \\
> &= \tfrac23 K\left(u^3 - \frac{3}{2K}\,u^2 + \frac{1}{2K^3}\right) \quad &\text{(common factor $\tfrac23 K$)} \\
> \left(u - u_b\right)^2\left(u + \tfrac12 u_b\right) &= u^3 - \tfrac32 u_b\,u^2 + \tfrac12 u_b^3 \quad &\text{(product expanded)} \\
> u'^2 &= \tfrac23 K\left(u - u_b\right)^2\left(u + \tfrac12 u_b\right) \quad &\text{(the bracket is this product with $u_b = 1/K$: a double root at $u_b$)} \\
> u' &= -\left(u - u_b\right)\sqrt{\tfrac23 K\left(u + \tfrac12 u_b\right)} \quad &\text{(branches moving towards $u_b$: $u' \gt 0$ below $u_b$, $u' \lt 0$ above it)} \\
> \tfrac23 K\left(u_b + \tfrac12 u_b\right) &= K\,u_b = 1 \quad &\text{(the root at $u = u_b$)} \\
> \theta - \theta_* &= -\int_{u_*}^{u}\frac{d\bar u}{\left(\bar u - u_b\right)\sqrt{\tfrac23 K\left(\bar u + \tfrac12 u_b\right)}} \quad &\text{(separation of variables; Barrow's rule from a point $u_*$ of the branch)} \\
> \theta - \theta_* &\approx -\left[\ln\left|\bar u - u_b\right|\right]_{u_*}^{u} \to +\infty \ \text{as} \ u \to u_b \quad &\text{(near $u_b$ the square root tends to 1: logarithmic divergence)} \\
> dt &= \frac{d\theta}{h\,u^2} \ge \frac{d\theta}{h\,\max\left(u_0, u_b\right)^2} \quad &\text{(areal integral; $u$ stays between $u_0$ and $u_b$)}
> \end{aligned}$$
>
> $$\boxed{E^* = W_{\max}, \ \left(u_0 \lt u_b,\ u_0' \gt 0\right) \text{ or } \left(u_0 \gt u_b,\ u_0' \lt 0\right): \ u \to u_b = \frac{h^2}{\mu} \ \text{as} \ \theta \to \infty \ \text{and} \ t \to \infty; \ \text{none of (i), (ii), (iii)}}$$
>
> **Units:** $[K\,u^3] = [\mathrm{L}][\mathrm{L^{-3}}] = [\mathrm{L^{-2}}] = [u'^2]$; $[K\,u_b] = [1]$
> **Meaning:** on the separatrix the particle climbs to the top of the barrier and approaches the unstable circular orbit of radius $\mu/h^2$ with infinitely many turns, never reaching it in a finite time: it neither escapes, nor falls, nor oscillates.

#### Answers

| Part of the statement | Answer |
| :--- | :--- |
| (a) Conserved quantities, planar motion | $\mathbf M_O = \mathbf r_0^P\times\mathbf F = \mathbf 0$, so $\mathbf H_{O,0} = m\,\mathbf r_0^P\times\mathbf v_0^P$ is constant; $\delta W_0 = -m\mu r^{-\alpha}dr$ is exact, $V_0 = -m\mu/[(\alpha - 1)r^{\alpha-1}]$ ($\alpha \ne 1$), $V_0 = m\mu\ln(r/r_*)$ ($\alpha = 1$), and $E_0 = \frac12 m v^2 + V_0$ is constant; $\mathbf r_0^P\cdot\mathbf H_{O,0} = 0$, so $P$ moves in the fixed plane through $O$ perpendicular to $\mathbf H_{O,0}$ |
| (b) Equation for $u(\theta)$ | $u'' + u = \dfrac{\mu}{h^2}\,u^{\alpha-2}$, with $h = r^2\dot\theta$ constant |
| (c) First integral | $u'^2 + W(u) = E^*$, $W(u) = u^2 - \dfrac{2\mu}{h^2}\Phi(u)$, $\Phi = \dfrac{u^{\alpha-1}}{\alpha - 1}$ ($\alpha \ne 1$) or $\ln(u/u_0)$ ($\alpha = 1$), $E^* = u_0'^2 + W(u_0)$ ($= 2E_0/(mh^2)$ for $\alpha = 2, 3, 4$); motion only where $W(u) \le E^*$, turning points at $W(u) = E^*$ |
| (c) $\alpha = 1$ | (i) never; (ii) never; (iii) always, between the two roots of $u^2 - \frac{2\mu}{h^2}\ln(u/u_0) = u_0'^2 + u_0^2$ (circle $r = h/\sqrt\mu$ if $u_0 = \sqrt\mu/h$, $u_0' = 0$) |
| (c) $\alpha = 2$ | $u = \frac{\mu}{h^2}[1 + e\cos(\theta - \theta_p)]$, $e = \sqrt{1 + E^*h^4/\mu^2}$, $E^* = u_0'^2 + u_0^2 - 2\frac{\mu}{h^2}u_0$: (i) iff $E^* \ge 0$; (ii) never; (iii) iff $-\mu^2/h^4 \lt E^* \lt 0$, between $\frac{\mu}{h^2}(1 \mp e)$; circle $u = \mu/h^2$ iff $E^* = -\mu^2/h^4$ |
| (c) $\alpha = 3$ | $\mu/h^2 \lt 1$: (i) always. $\mu/h^2 \gt 1$: (ii) iff $u_0' \gt -\sqrt{\mu/h^2 - 1}\,u_0$, (i) iff $u_0' \lt -\sqrt{\mu/h^2 - 1}\,u_0$; boundary $u_0' = -\sqrt{\mu/h^2 - 1}\,u_0$: $u = u_0e^{-\sqrt{\mu/h^2 - 1}\,\theta}$, outward spiral reaching infinity only as $\theta \to \infty$ (infinite time). $\mu/h^2 = 1$: (ii) if $u_0' \gt 0$, (i) if $u_0' \lt 0$, circle if $u_0' = 0$. (iii) never |
| (c) $\alpha = 4$ | with $E^* = u_0'^2 + u_0^2 - \frac{2\mu}{3h^2}u_0^3$, $W_{\max} = \frac{h^4}{3\mu^2}$, $u_b = \frac{h^2}{\mu}$: (i) if $0 \lt E^* \lt W_{\max}$ and $u_0 \lt u_b$, or $E^* \ge W_{\max}$ and $u_0' \lt 0$ (with $u_0 \lt u_b$ when $E^* = W_{\max}$); (ii) if $E^* \le 0$, or $0 \lt E^* \lt W_{\max}$ and $u_0 \gt u_b$, or $E^* \ge W_{\max}$ and $u_0' \gt 0$ (with $u_0 \gt u_b$ when $E^* = W_{\max}$); separatrix $E^* = W_{\max}$ with $u_0 \lt u_b$, $u_0' \gt 0$ or $u_0 \gt u_b$, $u_0' \lt 0$: asymptotic approach to the unstable circle $u = u_b$ (none of the three); circle if $u_0 = u_b$, $u_0' = 0$; (iii) never |

**Check against the official key:** Problems.pdf, p. 76 lists item 42 with no answer, so there is no key to compare with. Independent checks: the first integral was obtained from the equation of part (b) itself and agrees with the energy of part (a) (check box above); the classification is confirmed by integrating the equation of part (b) numerically (fourth-order Runge-Kutta, step $10^{-4}$ rad, the ratio $\mu/h^2$ set to 1 unless stated, "blow-up" meaning $u$ above $10^6$):

| Exponent | Data $(u_0, u_0')$ | Predicted | Numerical result |
| :---: | :--- | :--- | :--- |
| 2 | $(1.5, 0)$, $E^* = -0.75$ | (iii) between $0.5$ and $1.5$ | $u \in [0.5000, 1.5000]$ over 60 rad |
| 2 | $(0.5, -0.9)$, $E^* = 0.06$ | (i) | $u = 0$ at $\theta = 0.824$ |
| 1 | $(0.5, 0.3)$, $E^* = 0.34$ | (iii) | $u \in [0.4714, 1.6526]$ over 100 rad |
| 3, $\mu/h^2 = 1/2$ | $(1, 0)$ | (i) at $\theta_e = \pi/(2\sqrt{1/2}) = 2.2214$ | $u = 0$ at $\theta = 2.2214$ |
| 3, $\mu/h^2 = 2$ | $(1, -1.5)$, $C_1 = -0.25$ | (i) at $\theta_e = \frac12\ln 5 = 0.8047$ | $u = 0$ at $\theta = 0.8047$ |
| 3, $\mu/h^2 = 1$ | $(1, -0.1)$ | (i) at $\theta_e = 10$ | $u = 0$ at $\theta = 10.000$ |
| 4 | $(0.5, 0)$, $E^* = 1/6 \lt 1/3$, $u_0 \lt u_b = 1$ | (i) | $u = 0$ at $\theta = 2.078$ |
| 4 | $(1.2, 0)$, $E^* = 0.288 \lt 1/3$, $u_0 \gt u_b$ | (ii) | blow-up near $\theta = 4.06$ |
| 4 | $(0.5, \pm 0.9)$, $E^* = 0.977 \gt 1/3$ | (ii) for $+$, (i) for $-$ | blow-up near $\theta = 3.60$; $u = 0$ at $\theta = 0.524$ |

> [!derivation] Limiting case: circular orbits and their stability
> **Law:** a circular orbit is a stationary point of W; a minimum is stable, a maximum unstable
> **Source:** Notes.pdf, Sec. 4.6; Notes.pdf, Eq. 4.28
>
> $$\begin{aligned}
> W'(u_c) &= 2u_c - 2K\,u_c^{\alpha-2} = 0 \quad &\text{(circular orbit: $u$ constant, so $u'' = 0$)} \\
> K\,u_c^{\alpha-3} &= 1 \quad &\text{(divided by $2u_c$)} \\
> W''(u) &= 2 - 2K\left(\alpha - 2\right)u^{\alpha-3} \quad &\text{(derivative of $W'$)} \\
> W''(u_c) &= 2 - 2\left(\alpha - 2\right) \quad &\text{(the previous condition substituted)} \\
> &= 2\left(3 - \alpha\right) \quad &\text{(simplified)}
> \end{aligned}$$
>
> $$\boxed{u_c = K^{1/(3-\alpha)} \ (\alpha \ne 3), \qquad W''(u_c) = 2\left(3 - \alpha\right): \ \text{minimum (stable) for } \alpha \lt 3, \ \text{maximum (unstable) for } \alpha \gt 3}$$
>
> **Units:** $[K\,u_c^{\alpha-3}] = [\mathrm{L^{\alpha-3}}][\mathrm{L^{3-\alpha}}] = [1]$; $W''$ is dimensionless
> **Meaning:** the three cases worked above agree: $u_c = \sqrt K$ for the exponent 1 and $u_c = K$ for 2 are minima, with bounded oscillations around them; $u_b = 1/K$ for 4 is the top of the barrier; for 3 the curvature is zero and circles exist only when $K$ equals 1.

> [!derivation] Limiting case: zero angular momentum (radial motion)
> **Law:** equations of motion and energy with h equal to zero
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Sec. 4.8.1
>
> $$\begin{aligned}
> \dot\theta &= \frac{h}{r^2} = 0 \quad &\text{(areal integral with $h = 0$: fixed direction)} \\
> \ddot r &= -\mu\,r^{-\alpha} \lt 0 \quad &\text{(radial equation with $\dot\theta = 0$)} \\
> \tfrac12\dot r^2 + \frac{V_0(r)}{m} &= \frac{E_0}{m} \quad &\text{(energy with $\mathbf v_0^P = \dot r\,\mathbf e_r$)}
> \end{aligned}$$
>
> $$\boxed{h = 0: \ \text{motion on a fixed line through } O; \ \text{(i) only if } \alpha \gt 1,\ \dot r_0 \gt 0,\ E_0 \ge 0; \ \text{otherwise (ii)}; \ \text{(iii) never}}$$
>
> **Units:** $[\ddot r] = [\mu\,r^{-\alpha}] = [\mathrm{L\,T^{-2}}]$; $[\dot r^2] = [V_0/m] = [\mathrm{L^2\,T^{-2}}]$
> **Meaning:** without angular momentum there is no centrifugal barrier: the acceleration always points to $O$. Moving inward, the particle reaches $O$; moving outward, it escapes only if its energy reaches the value zero of the potential at infinity (impossible for the exponent 1, whose potential is unbounded), and otherwise it stops and falls back to $O$, because the radial acceleration of the second row is negative at every distance.

> [!warning] Erratum to Notes.pdf, Sec. 4.8.1, property 5
> Property 5 of the list of properties of central force motion in Notes.pdf, Sec. 4.8.1 states that the particle $P$ can never reach $O$ unless the angular momentum $\mathbf H_{O,0}$ is zero. The list is written for any central force, but the property holds only under an extra hypothesis: the effective potential $W$ must grow without bound as $u$ grows, that is, the centrifugal barrier must dominate the attraction near $O$. For the power law of this problem that is the case for every exponent below 3 (gravity, the exponent 2 of Notes.pdf, Ch. 8, included) and for the exponent 3 with $K$ below 1. With nonzero angular momentum the particle does reach $O$, in a finite time, for the exponent 3 with $K$ of at least 1 and for the exponent 4 (boxes of part (c) and the box below). Zero angular momentum is not sufficient either: the radial motion of the previous box escapes for some data.

> [!derivation] Property 5 tested on the power law
> **Law:** first integral of part (c); behaviour of W for large u; time along the orbit from the areal integral; Barrow's rule
> **Source:** Notes.pdf, Sec. 4.8.1; Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 8.7
>
> $$\begin{aligned}
> u'^2 &= E^* - W(u), \quad W(u) = u^2 - 2K\,\Phi(u) \quad &\text{(first integral of part (c))} \\
> \alpha \lt 3:\quad \lim_{u\to\infty}W(u) &= +\infty \quad &\text{($u^2$ grows faster than $u^{\alpha-1}$, and than $\ln u$ for $\alpha = 1$)} \\
> \alpha = 3:\quad W(u) &= \left(1 - K\right)u^2 \quad &\text{(box of the exponent 3)} \\
> \alpha = 3,\ K \lt 1:\quad \lim_{u\to\infty}W(u) &= +\infty \quad &\text{(positive coefficient)} \\
> \alpha \gt 3:\quad \lim_{u\to\infty}W(u) &= \lim_{u\to\infty}\left(-\frac{2K\,u^{\alpha-1}}{\alpha - 1}\right) = -\infty \quad &\text{(the highest power dominates)} \\
> \alpha = 3,\ K = 1,\ u_0' \gt 0:\quad u &= u_0 + u_0'\,\theta \quad &\text{(box of $K$ equal to 1)} \\
> dt &= \frac{d\theta}{h\,u^2} \quad &\text{(areal integral: $\dot\theta = h\,u^2$)} \\
> t_O &= \int_0^\infty\frac{d\theta}{h\left(u_0 + u_0'\theta\right)^2} \quad &\text{(time to reach $u \to \infty$)} \\
> &= \left[-\frac{1}{h\,u_0'\left(u_0 + u_0'\theta\right)}\right]_0^\infty \quad &\text{(antiderivative, with $d(u_0 + u_0'\theta) = u_0'\,d\theta$; Barrow's rule)} \\
> &= \frac{1}{h\,u_0\,u_0'} \quad &\text{(limits substituted)} \\
> \alpha = 3,\ K \gt 1,\ C_1 \gt 0:\quad \frac{1}{h\,u^2} &\le \frac{4\,e^{-2\lambda\theta}}{h\,C_1^2} \ \text{for large } \theta \quad &\text{($u \ge \tfrac12 C_1e^{\lambda\theta}$ once $C_2e^{-\lambda\theta}$ is small: the integral of $dt$ converges)} \\
> \alpha = 4,\ \text{cases (ii)}:\quad \int^{\infty}\frac{du}{u'} &\approx \int^{\infty}\frac{du}{\sqrt{\tfrac23 K}\,u^{3/2}} \lt \infty \quad &\text{($u'^2 \approx \tfrac23 K u^3$ for large $u$: $u \to \infty$ at a finite angle, so in a finite time)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \text{property 5 holds when } W \to +\infty \text{ as } u \to \infty: \ \alpha \lt 3, \text{ or } \alpha = 3 \text{ with } K \lt 1; \cr h \ne 0 \text{ and } P \text{ reaches } O \text{ in a finite time: } \alpha = 3,\ K \ge 1,\ u_0' \gt -\sqrt{K - 1}\,u_0; \ \alpha = 4 \text{ in the cases (ii) of its box} \end{array}}$$
>
> **Units:** $[t_O] = [h\,u_0\,u_0']^{-1} = \left([\mathrm{L^2\,T^{-1}}][\mathrm{L^{-1}}][\mathrm{L^{-1}}]\right)^{-1} = [\mathrm{T}]$
> **Meaning:** the angular momentum protects $O$ only if the centrifugal term, which grows as the square of $u$ in $W$, beats the attraction; an attraction as strong as the inverse cube with $K$ of at least 1, or stronger, overcomes it and the particle spirals into $O$ in a finite time, as for $K$ equal to 1, where the time is finite even though the angle grows without bound.

---

## Problem 43: Two Connected Particles, Plane with Hole

### Reference Frames, Bases and Coordinates

Two point particles $P_1$ and $P_2$ of mass $m$ are tied to the ends of a massless cord of length $2a$ that passes through a small hole $O$ of a smooth horizontal plane: $P_1$ moves on the plane and $P_2$ hangs on the vertical line below the hole (Problems.pdf, p. 30; in-class problem of Session 8). At the start half of the cord is on the plane and $P_1$ is pushed with the speed $v_0$ perpendicular to the cord, counterclockwise seen from above; the cord is always tense. The statement asks for the speed and the tension of a circular motion, the reduction to quadratures and the band of radii for the speed $\sqrt{8ag/3}$, the tension from Newton's law for $P_2$, and the equations of motion on a rough plane. The solution follows the Newtonian approach of Notes.pdf, Sec. 7.1 to Sec. 7.7.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, origin at the hole (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$: $\mathbf i$ and $\mathbf j$ horizontal on the plane, $\mathbf i$ along the initial position of $P_1$; $\mathbf k$ vertical **upward**, so that seen from above it points towards the observer and counterclockwise is the positive sense about $\mathbf k$ |
| Polar basis | $\mathcal B_1 = \{\mathbf e_r, \mathbf e_\theta, \mathbf k\}$, $\mathcal B_0$ turned by $\theta$ about $\mathbf k$; $\mathbf e_r$ horizontal, from $O$ towards $P_1$ (Notes.pdf, Eq. 2.24) |
| Coordinates | $r$, the distance $OP_1$ (the length of cord on the plane); $\theta$, the polar angle of $P_1$ from $\mathbf i$, counterclockwise seen from above |
| Hypotheses | smooth plane in parts (a) to (e) (rough with the coefficient $\mu$ in part (f)); small smooth hole, so the cord slides through it without friction; massless, inextensible cord, always tense (statement); $P_2$ stays below the hole, so the hanging length is not negative |
| Constraints | $P_1$ on the plane, $z_1 = 0$ (1 equation, holonomic, stationary, smooth); $P_2$ on the vertical through $O$, $x_2 = y_2 = 0$ (2 equations, holonomic, stationary, smooth); cord, $\lvert OP_1\rvert + \lvert OP_2\rvert = 2a$ (1 equation joining the particles, holonomic, stationary, **unilateral**) ([Lecture 3, Slide 17]; [Lecture 3, Slide 21]) |
| Degrees of freedom | 6 coordinates of two particles minus 4 constraint equations: 2, the functions $r(t)$ and $\theta(t)$ ([Lecture 3, Slide 4]) |
| Data | $m$ [kg], $a$ [m], $g$ [m s$^{-2}$], $v_0$ [m s$^{-1}$] (unknown in (a), $\sqrt{8ag/3}$ in (c) to (e)), $\mu$ [1] in (f) |
| Initial state | $r(0) = a$ (half of the cord on the plane), $\theta(0) = 0$, initial velocity of $P_1$ of magnitude $v_0$ perpendicular to the cord, counterclockwise seen from above |
| Applied forces | weights $-mg\,\mathbf k$ on each particle; in (f), the friction of the plane on $P_1$ |
| Constraint forces | on $P_1$: normal reaction of the plane along $\mathbf k$ and tension towards the hole; on $P_2$: tension upwards and reaction of the vertical guide, normal to it; the same tension $T$ at both ends (massless cord, smooth hole, [Lecture 3, Slide 17]) |

![[attachments/EM-SOL/p43-elevation.svg]]

### Change of Basis and Position Vector

![[attachments/EM-SOL/p43-rotation-k.svg]]

> [!derivation] Polar basis of P1: rotation about k
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.24
>
> View from above along $\mathbf k$, which points out of the paper (⊙, upward towards the observer) with $\mathbf i$ to the right and $\mathbf j$ up the page: a positive rotation about $\mathbf k$ is counterclockwise, the sense of the push. $\mathbf e_r$ is $\mathbf i$ turned by $\theta$: hypotenuse 1, adjacent leg $\cos\theta$ along $\mathbf i$, opposite leg $\sin\theta$ along $\mathbf j$. $\mathbf e_\theta$ is $\mathbf j$ turned by $\theta$: adjacent leg $\cos\theta$ along $\mathbf j$, opposite leg $\sin\theta$ along minus $\mathbf i$ (the vector $\mathbf j$ turned counterclockwise leans to the left: the minus sign).
>
> $$\begin{aligned}
> \mathbf e_r &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j \quad &\text{(right triangle of $\mathbf e_r$)} \\
> \mathbf e_\theta &= -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(right triangle of $\mathbf e_\theta$: opposite leg on $-\mathbf i$)} \\
> \mathbf e_r\times\mathbf e_\theta &= \cos^2\theta\,\mathbf i\times\mathbf j - \sin^2\theta\,\mathbf j\times\mathbf i \quad &\text{(distributive law; $\mathbf i\times\mathbf i = \mathbf j\times\mathbf j = \mathbf 0$)} \\
> &= \left(\cos^2\theta + \sin^2\theta\right)\mathbf k = \mathbf k \quad &\text{(right-handed; $\mathbf i\times\mathbf j = \mathbf k$, $\mathbf j\times\mathbf i = -\mathbf k$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expansion along the third row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\theta + \sin^2\theta = 1 \quad &\text{(row 1 times row 1)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{12} &= \cos\theta\sin\theta - \sin\theta\cos\theta = 0 \quad &\text{(row 1 times row 2; row 3 is the unit row of $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** dimensionless direction cosines: $[1]$
> **Meaning:** $\mathbf e_r$ points along the cord on the plane, from the hole to $P_1$, and $\mathbf e_\theta$ is the horizontal direction of the push at the initial instant.

> [!derivation] Position vectors and the length of cord on each side
> **Law:** position vectors with the constraints substituted; inextensible cord
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.28; [Lecture 3, Slide 17]
>
> The cord runs straight on the plane from $P_1$ to the hole, with the length $r$, and then straight down to $P_2$; the hanging length is the rest of the cord.
>
> $$\begin{aligned}
> \mathbf r_0^{P_1} &= r\,\mathbf e_r \quad &\text{(cylindrical position, Eq. 2.28, with $z_1 = 0$)} \\
> \lvert OP_2\rvert &= 2a - r \quad &\text{(inextensible cord of length $2a$)} \\
> \mathbf r_0^{P_2} &= -\left(2a - r\right)\mathbf k \quad &\text{(on the vertical through $O$, below the hole)} \\
> &= \left(r - 2a\right)\mathbf k \quad &\text{(sign distributed)} \\
> 2a - r &\ge 0 \quad &\text{($P_2$ cannot rise above the hole)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^{P_1} = r\,\mathbf e_r, \qquad \mathbf r_0^{P_2} = \left(r - 2a\right)\mathbf k, \qquad 0 \lt r \le 2a}$$
>
> **Units:** $[r] = [a] = [\mathrm{L}]$
> **Meaning:** both particles are described by the two coordinates; when $P_1$ moves away from the hole, $P_2$ rises by the same amount. At the start, with $r$ equal to $a$, the hanging length is also $a$: half of the cord on each side.

![[attachments/EM-SOL/p43-top.svg]]

### Kinematics

> [!derivation] Derivatives of the polar unit vectors
> **Law:** derivative of a unit vector turning about a fixed axis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \dot\theta\,\mathbf k \quad &\text{($\mathcal B_1$ turns about the fixed $\mathbf k$ with the angle $\theta$)} \\
> \mathbf k\times\mathbf e_r &= \cos\theta\,\mathbf j - \sin\theta\,\mathbf i = \mathbf e_\theta \quad &\text{($\mathbf k\times\mathbf i = \mathbf j$, $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> \mathbf k\times\mathbf e_\theta &= -\sin\theta\,\mathbf j - \cos\theta\,\mathbf i = -\mathbf e_r \quad &\text{(same products)} \\
> \dot{\mathbf e}_r &= \boldsymbol\omega_{10}\times\mathbf e_r = \dot\theta\,\mathbf e_\theta \quad &\text{(Eq. 1.62)} \\
> \dot{\mathbf e}_\theta &= \boldsymbol\omega_{10}\times\mathbf e_\theta = -\dot\theta\,\mathbf e_r \quad &\text{(Eq. 1.62)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf e}_r = \dot\theta\,\mathbf e_\theta, \qquad \dot{\mathbf e}_\theta = -\dot\theta\,\mathbf e_r}$$
>
> **Units:** $[\dot\theta] = [\mathrm{T^{-1}}]$
> **Meaning:** the polar basis follows $P_1$ round the hole; $\mathbf k$ is fixed.

> [!derivation] Velocity and acceleration of both particles
> **Law:** time derivatives of the position vectors in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Notes.pdf, Sec. 7.4
>
> $$\begin{aligned}
> \mathbf v_0^{P_1} &= \dot r\,\mathbf e_r + r\,\dot{\mathbf e}_r \quad &\text{(Eq. 2.3; product rule)} \\
> &= \dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta \quad &\text{($\dot{\mathbf e}_r = \dot\theta\,\mathbf e_\theta$)} \\
> \mathbf a_0^{P_1} &= \ddot r\,\mathbf e_r + \dot r\,\dot{\mathbf e}_r + \dot r\dot\theta\,\mathbf e_\theta + r\ddot\theta\,\mathbf e_\theta + r\dot\theta\,\dot{\mathbf e}_\theta \quad &\text{(Eq. 2.4; product rule on each term)} \\
> &= \ddot r\,\mathbf e_r + \dot r\dot\theta\,\mathbf e_\theta + \dot r\dot\theta\,\mathbf e_\theta + r\ddot\theta\,\mathbf e_\theta - r\dot\theta^2\,\mathbf e_r \quad &\text{(derivatives of the unit vectors substituted)} \\
> &= \left(\ddot r - r\dot\theta^2\right)\mathbf e_r + \left(r\ddot\theta + 2\dot r\dot\theta\right)\mathbf e_\theta \quad &\text{(grouped)} \\
> \mathbf v_0^{P_2} &= \frac{d}{dt}\left[\left(r - 2a\right)\mathbf k\right] = \dot r\,\mathbf k \quad &\text{($a$ constant, $\mathbf k$ fixed)} \\
> \mathbf a_0^{P_2} &= \ddot r\,\mathbf k \quad &\text{(derivative again)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \mathbf v_0^{P_1} = \dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta, \quad \mathbf a_0^{P_1} = \left(\ddot r - r\dot\theta^2\right)\mathbf e_r + \left(r\ddot\theta + 2\dot r\dot\theta\right)\mathbf e_\theta \cr \mathbf v_0^{P_2} = \dot r\,\mathbf k, \quad \mathbf a_0^{P_2} = \ddot r\,\mathbf k \end{array}}$$
>
> **Units:** $[\dot r] = [r\dot\theta] = [\mathrm{L\,T^{-1}}]$; $[\ddot r] = [r\dot\theta^2] = [\dot r\dot\theta] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** $P_2$ moves only vertically, with the radial rate of $P_1$: the cord transmits the radial motion through the hole.

> [!derivation] Initial state
> **Law:** initial velocity of P1 decomposed in the polar basis
> **Source:** Notes.pdf, Sec. 7.7; Problems.pdf, p. 30
>
> The push is perpendicular to the cord, which lies along $\mathbf e_r$, and counterclockwise seen from above, the sense of positive $\theta$: the initial velocity is $v_0\,\mathbf e_\theta$.
>
> $$\begin{aligned}
> \mathbf v_0^{P_1}(0) &= \dot r(0)\,\mathbf e_r + a\,\dot\theta(0)\,\mathbf e_\theta \quad &\text{(velocity at $t = 0$, with $r(0) = a$)} \\
> &= v_0\,\mathbf e_\theta \quad &\text{(push perpendicular to the cord, counterclockwise)} \\
> \dot r(0) &= 0, \quad \dot\theta(0) = \frac{v_0}{a} \quad &\text{(components along $\mathbf e_r$ and $\mathbf e_\theta$ compared)} \\
> \mathbf v_0^{P_2}(0) &= \dot r(0)\,\mathbf k = \mathbf 0 \quad &\text{($P_2$ starts at rest)}
> \end{aligned}$$
>
> $$\boxed{r(0) = a, \quad \dot r(0) = 0, \quad \theta(0) = 0, \quad \dot\theta(0) = \frac{v_0}{a}}$$
>
> **Units:** $[v_0/a] = [\mathrm{T^{-1}}]$
> **Meaning:** $P_1$ starts moving round the hole without approaching or leaving it, and $P_2$ starts at rest at the depth $a$.

### Forces and Equations of Motion

The free-body diagrams show on $P_1$ its weight, the normal reaction of the plane and the tension towards the hole (and, in part (f), the friction opposite to the velocity); on $P_2$ its weight, the tension upwards and the reaction of the vertical guide. $S_0$ is inertial, so no inertia force acts.

![[attachments/EM-SOL/p43-fbd.svg]]

> [!derivation] Forces on both particles (smooth plane)
> **Law:** weight; tension of a massless cord through a small smooth hole; reactions in the normal subspaces
> **Source:** Notes.pdf, Sec. 6.4; Notes.pdf, Sec. 7.5; [Lecture 3, Slide 13]; [Lecture 3, Slide 17]
>
> $$\begin{aligned}
> -\frac{\mathbf r_0^{P_1}}{r} &= -\mathbf e_r \quad &\text{(unit vector from $P_1$ towards the hole, along the cord)} \\
> \mathbf F^{P_1} &= -mg\,\mathbf k + N_1\,\mathbf k - T\,\mathbf e_r \quad &\text{(weight, normal reaction of the smooth plane, tension $T \ge 0$)} \\
> \mathbf F^{P_2} &= -mg\,\mathbf k + T\,\mathbf k + R_x\,\mathbf i + R_y\,\mathbf j \quad &\text{(weight, tension towards the hole, guide reaction normal to the vertical)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F^{P_1} = -T\,\mathbf e_r + \left(N_1 - mg\right)\mathbf k, \qquad \mathbf F^{P_2} = \left(T - mg\right)\mathbf k + R_x\,\mathbf i + R_y\,\mathbf j}$$
>
> **Units:** every force $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** four unknown reactions, $T$, $N_1$, $R_x$, $R_y$; no force on $P_1$ has a component along $\mathbf e_\theta$, and the tension on $P_1$ passes through the hole.

> [!derivation] Newton's second law for each particle
> **Law:** Newton's second law in an inertial frame, projected on the polar basis (P1) and on the fixed basis (P2)
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Sec. 7.6; [Lecture 3, Slide 14]
>
> $$\begin{aligned}
> P_1,\ \mathbf e_r:\ m\left(\ddot r - r\dot\theta^2\right) &= -T \quad &\text{(dot product with $\mathbf e_r$)} \\
> P_1,\ \mathbf e_\theta:\ m\left(r\ddot\theta + 2\dot r\dot\theta\right) &= 0 \quad &\text{(no force along $\mathbf e_\theta$)} \\
> P_1,\ \mathbf k:\ 0 &= N_1 - mg \quad &\text{($P_1$ stays on the plane: no vertical acceleration)} \\
> P_2,\ \mathbf k:\ m\ddot r &= T - mg \quad &\text{(along the vertical)} \\
> P_2,\ \mathbf i,\ \mathbf j:\ 0 &= R_x, \quad 0 = R_y \quad &\text{($\mathbf a_0^{P_2}$ has no horizontal part)}
> \end{aligned}$$
>
> $$\boxed{N_1 = mg, \qquad R_x = R_y = 0, \qquad T = m\left(g + \ddot r\right)}$$
>
> **Units:** every term $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** six scalar equations for the six unknowns $r$, $\theta$, $T$, $N_1$, $R_x$, $R_y$. The plane carries the weight of $P_1$ (the cord is horizontal on it), the guide exerts no force, and the tension is the weight of $P_2$ corrected by its vertical acceleration.

> [!derivation] Equations of motion free of the tension
> **Law:** elimination of the tension between the equations of P1 and P2
> **Source:** Notes.pdf, Sec. 7.6
>
> $$\begin{aligned}
> m\left(\ddot r - r\dot\theta^2\right) + m\ddot r &= -T + T - mg \quad &\text{(equation of $P_1$ along $\mathbf e_r$ plus equation of $P_2$)} \\
> 2\ddot r - r\dot\theta^2 + g &= 0 \quad &\text{(divided by $m$; all terms on the left)}
> \end{aligned}$$
>
> $$\boxed{2\ddot r - r\dot\theta^2 + g = 0, \qquad r\ddot\theta + 2\dot r\dot\theta = 0}$$
>
> **Units:** $[\ddot r] = [r\dot\theta^2] = [g] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** two equations for $r$ and $\theta$ only. The factor 2 is the inertia of both particles, which move with the same radial rate; the only driving terms are the centrifugal term of $P_1$ and the weight of $P_2$.

> [!derivation] Two first integrals: angular momentum and energy
> **Law:** exact derivatives (product and chain rules); Barrow's rule
> **Source:** Notes.pdf, Eq. 4.58; Notes.pdf, Eq. 4.31; Notes.pdf, Eq. 8.7; [Lecture 3, Slide 17]; [Lecture 4, Slide 7]
>
> $$\begin{aligned}
> \frac{d}{dt}\left(r^2\dot\theta\right) &= 2r\dot r\dot\theta + r^2\ddot\theta \quad &\text{(product rule; chain rule on $r^2$)} \\
> &= r\left(r\ddot\theta + 2\dot r\dot\theta\right) \quad &\text{(common factor $r$)} \\
> &= 0 \quad &\text{(transverse equation)} \\
> r^2\dot\theta &= r(0)^2\,\dot\theta(0) \quad &\text{(Barrow's rule between $0$ and $t$)} \\
> &= a^2\,\frac{v_0}{a} = a\,v_0 \equiv h \quad &\text{(initial state)} \\
> 2\ddot r - \frac{h^2}{r^3} + g &= 0 \quad &\text{(radial equation; $r\dot\theta^2 = h^2/r^3$)} \\
> 2\dot r\ddot r - \frac{h^2}{r^3}\,\dot r + g\,\dot r &= 0 \quad &\text{(times $\dot r$)} \\
> \frac{d}{dt}\left(\dot r^2\right) &= 2\dot r\ddot r \quad &\text{(chain rule)} \\
> \frac{d}{dt}\left(\frac{h^2}{2r^2}\right) &= -\frac{h^2}{r^3}\,\dot r \quad &\text{(chain rule; $h$ constant)} \\
> \frac{d}{dt}\left(g\,r\right) &= g\,\dot r \quad &\text{($g$ constant)} \\
> \frac{d}{dt}\left[\dot r^2 + \frac{h^2}{2r^2} + g\,r\right] &= 0 \quad &\text{(the previous equation is this sum of derivatives)} \\
> \left[\dot r^2 + \frac{h^2}{2r^2} + g\,r\right]_0^t &= 0 \quad &\text{(Barrow's rule)} \\
> m\dot r^2 + \frac{m h^2}{2r^2} + mg\left(r - 2a\right) &= E = \text{const} \quad &\text{(times $m$, minus the constant $2mga$)} \\
> \tfrac12 m\,\mathbf v_0^{P_1}\cdot\mathbf v_0^{P_1} + \tfrac12 m\,\mathbf v_0^{P_2}\cdot\mathbf v_0^{P_2} + mg\,z_2 &= E \quad &\text{(the same: $\dot r^2 + h^2/r^2$, $\dot r^2$ and $z_2 = r - 2a$)}
> \end{aligned}$$
>
> $$\boxed{r^2\dot\theta = h = a\,v_0, \qquad E = m\dot r^2 + \frac{m h^2}{2r^2} + mg\left(r - 2a\right) = \text{const}}$$
>
> **Units:** $[h] = [\mathrm{L^2\,T^{-1}}]$; every term of $E$ $[\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the first is the angular momentum of $P_1$ about the vertical through the hole per unit mass, constant because the tension passes through the hole; the second is the mechanical energy of the pair: the tension does the power $-T\dot r$ on $P_1$ and $+T\dot r$ on $P_2$, which cancel, and the smooth stationary constraints do no work.

### Answers and Checks

#### (a) and (b) Circular motion

> [!derivation] Speed and tension for a circular motion of P1
> **Law:** equations of motion with a constant radius
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Sec. 7.7
>
> A circumference of $P_1$ about the hole has a constant radius, equal to its initial value $a$.
>
> $$\begin{aligned}
> r &\equiv a, \quad \dot r = \ddot r = 0 \quad &\text{(constant radius)} \\
> m\cdot 0 &= T - mg \quad &\text{(equation of $P_2$)} \\
> T &= mg \quad &\text{(solved)} \\
> \dot\theta &= \frac{h}{a^2} \quad &\text{(areal integral with $r = a$)} \\
> &= \frac{v_0}{a} \quad &\text{($h = a v_0$)} \\
> m\left(0 - a\dot\theta^2\right) &= -T \quad &\text{(equation of $P_1$ along $\mathbf e_r$)} \\
> T &= m a\dot\theta^2 \quad &\text{(solved)} \\
> &= \frac{m v_0^2}{a} \quad &\text{($\dot\theta = v_0/a$)} \\
> \frac{m v_0^2}{a} &= mg \quad &\text{(the two values of $T$)} \\
> v_0 &= \sqrt{a g} \quad &\text{(positive root)}
> \end{aligned}$$
>
> $$\boxed{\text{(a)}\ v_0 = \sqrt{a g}, \qquad \text{(b)}\ T = mg}$$
>
> **Units:** $[\sqrt{ag}] = [\mathrm{L\,T^{-1}}]$; $[mg] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** $P_2$ hangs at rest, so the cord carries its weight; that weight is exactly the centripetal force that keeps $P_1$ on the circle of radius $a$.

#### (c) Reduction to quadratures for the speed of the statement

> [!derivation] First integrals evaluated with the initial state
> **Law:** the first integrals with the initial data; energy integral solved for the radial rate
> **Source:** Notes.pdf, Eq. 4.27; Problems.pdf, p. 30
>
> $$\begin{aligned}
> v_0^2 &= \frac{8ag}{3} \quad &\text{(statement)} \\
> h^2 &= a^2v_0^2 = \frac{8a^3g}{3} \quad &\text{($h = a v_0$)} \\
> \frac{E}{m} &= \dot r(0)^2 + \frac{h^2}{2a^2} + g\left(a - 2a\right) \quad &\text{(energy at $t = 0$)} \\
> &= 0 + \frac{4ag}{3} - g a \quad &\text{($\dot r(0) = 0$; $h^2/(2a^2) = 4ag/3$)} \\
> &= \frac{g a}{3} \quad &\text{(added)} \\
> \dot r^2 &= \frac{E}{m} - \frac{h^2}{2r^2} - g\left(r - 2a\right) \quad &\text{(energy integral solved for $\dot r^2$)} \\
> &= \frac{g a}{3} - \frac{4a^3g}{3r^2} - g r + 2g a \quad &\text{(values substituted)} \\
> &= \frac{7g a}{3} - g r - \frac{4a^3g}{3r^2} \quad &\text{(constant terms added)} \\
> &= \frac{g\left(7a r^2 - 3r^3 - 4a^3\right)}{3r^2} \quad &\text{(common denominator $3r^2$)}
> \end{aligned}$$
>
> $$\boxed{h^2 = \frac{8a^3g}{3}, \qquad \dot r^2 = \frac{g\,P(r)}{3r^2}, \qquad P(r) = -3r^3 + 7a r^2 - 4a^3}$$
>
> **Units:** $[g\,P/r^2] = [\mathrm{L\,T^{-2}}][\mathrm{L^3}][\mathrm{L^{-2}}] = [\mathrm{L^2\,T^{-2}}] = [\dot r^2]$
> **Meaning:** the radial motion obeys a one-dimensional energy equation: the radial rate is known from the radius alone.

> [!derivation] Quadrature for the time
> **Law:** separation of variables in the energy integral; Barrow's rule
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.44
>
> The sign of the radial rate is fixed by the radial acceleration at the start, where the rate is zero.
>
> $$\begin{aligned}
> \ddot r(0) &= \tfrac12\left(-g + \frac{h^2}{a^3}\right) \quad &\text{(equation of motion free of $T$ with $r\dot\theta^2 = h^2/r^3$, at $r = a$)} \\
> &= \tfrac12\left(-g + \frac{8g}{3}\right) \quad &\text{($h^2 = 8a^3g/3$)} \\
> &= \frac{5g}{6} \gt 0 \quad &\text{(added: $r$ starts to grow)} \\
> \frac{dr}{dt} &= +\sqrt{\frac{g}{3}}\,\frac{\sqrt{P(r)}}{r} \quad &\text{(positive root while $r$ grows)} \\
> \frac{r\,dr}{\sqrt{P(r)}} &= \sqrt{\frac{g}{3}}\,dt \quad &\text{(separation of variables)} \\
> \int_a^r\frac{r'\,dr'}{\sqrt{P(r')}} &= \sqrt{\frac{g}{3}}\int_0^t dt' \quad &\text{(integrated from the initial state)} \\
> &= \sqrt{\frac{g}{3}}\;t \quad &\text{(Barrow's rule on the right side)}
> \end{aligned}$$
>
> $$\boxed{t = \sqrt{\frac{3}{g}}\int_a^r\frac{r'\,dr'}{\sqrt{P(r')}} \ \ (r \text{ growing}), \qquad t = \frac{\tau_r}{2} + \sqrt{\frac{3}{g}}\int_r^{2a}\frac{r'\,dr'}{\sqrt{P(r')}} \ \ (r \text{ decreasing from } 2a)}$$
>
> **Units:** $[\sqrt{3/g}\;r\,dr/\sqrt{P}] = [\mathrm{T\,L^{-1/2}}][\mathrm{L^2}][\mathrm{L^{-3/2}}] = [\mathrm{T}]$
> **Meaning:** the integrand is improper at the turning radii, where $P$ has simple roots (next part), but it is integrable; after the outer turning point the root changes sign and the motion repeats with the radial period $\tau_r$, twice the time from $a$ to $2a$.

> [!derivation] Quadrature for the angle
> **Law:** areal integral with the time element of the previous box; Barrow's rule
> **Source:** Notes.pdf, Eq. 8.7
>
> $$\begin{aligned}
> d\theta &= \frac{h}{r^2}\,dt \quad &\text{(areal integral, $\dot\theta = h/r^2$)} \\
> &= \frac{h}{r^2}\,\sqrt{\frac{3}{g}}\,\frac{r\,dr}{\sqrt{P(r)}} \quad &\text{($dt$ of the previous box)} \\
> &= h\sqrt{\frac{3}{g}}\,\frac{dr}{r\sqrt{P(r)}} \quad &\text{(one power of $r$ cancelled)} \\
> h\sqrt{\frac{3}{g}} &= \sqrt{\frac{8a^3g}{3}\cdot\frac{3}{g}} \quad &\text{(product of the square roots)} \\
> &= \sqrt{8a^3} = 2\sqrt2\,a^{3/2} \quad &\text{($g$ and 3 cancel)} \\
> \theta - 0 &= 2\sqrt2\,a^{3/2}\int_a^r\frac{dr'}{r'\sqrt{P(r')}} \quad &\text{(Barrow's rule from $\theta(0) = 0$)}
> \end{aligned}$$
>
> $$\boxed{\theta(r) = 2\sqrt2\,a^{3/2}\int_a^r\frac{dr'}{r'\sqrt{P(r')}} \ \ (r \text{ growing}), \qquad \theta(t) = \int_0^t\frac{h}{r(t')^2}\,dt' \ \ (\text{all } t)}$$
>
> **Units:** $[a^{3/2}\,dr/(r\sqrt P)] = [\mathrm{L^{3/2}}][\mathrm{L}][\mathrm{L^{-1}}][\mathrm{L^{-3/2}}] = [1]$
> **Meaning:** the angle grows monotonically, since the angular rate is always positive; together with the quadrature for the time it gives the orbit of $P_1$ and, through the cord, the height of $P_2$.

#### (d) Oscillation between a and 2a

![[attachments/EM-SOL/p43-band.svg]]

> [!derivation] Band of radii and turning points
> **Law:** the square of the radial rate cannot be negative; radial acceleration at the turning points
> **Source:** Notes.pdf, Eq. 4.28; Problems.pdf, p. 30
>
> With $x = r/a$ the polynomial is factored with the roots of the hint.
>
> $$\begin{aligned}
> P(r) &= a^3\left(-3x^3 + 7x^2 - 4\right) \quad &\text{($r = a x$; $a^3$ factored out)} \\
> \left(x - 1\right)\left(x - 2\right) &= x^2 - 3x + 2 \quad &\text{(product)} \\
> \left(x^2 - 3x + 2\right)\left(3x + 2\right) &= 3x^3 - 7x^2 + 4 \quad &\text{(product)} \\
> -3x^3 + 7x^2 - 4 &= -\left(x - 1\right)\left(x - 2\right)\left(3x + 2\right) \quad &\text{(minus the previous row: roots $1$, $2$, $-2/3$)} \\
> P \ge 0 &\iff \left(x - 1\right)\left(x - 2\right) \le 0 \quad &\text{($\dot r^2 \ge 0$; $3x + 2 \gt 0$ for $x \gt 0$)} \\
> &\iff 1 \le x \le 2 \quad &\text{(a product of two factors is not positive between their roots)} \\
> \ddot r &= -\frac{g}{2} + \frac{h^2}{2r^3} \quad &\text{(equation of motion free of $T$, $r\dot\theta^2 = h^2/r^3$, divided by 2)} \\
> &= -\frac{g}{2} + \frac{4a^3g}{3r^3} \quad &\text{($h^2 = 8a^3g/3$)} \\
> \ddot r\big|_{r = a} &= -\frac{g}{2} + \frac{4g}{3} \quad &\text{(inner turning point)} \\
> &= \frac{5g}{6} \gt 0 \quad &\text{(added)} \\
> \ddot r\big|_{r = 2a} &= -\frac{g}{2} + \frac{g}{6} \quad &\text{(outer turning point: $4a^3/(3\cdot 8a^3) = 1/6$)} \\
> &= -\frac{g}{3} \lt 0 \quad &\text{(added)}
> \end{aligned}$$
>
> $$\boxed{a \le r(t) \le 2a; \ \text{the radial rate vanishes at } r = a \ (\ddot r = 5g/6 \gt 0) \text{ and at } r = 2a \ (\ddot r = -g/3 \lt 0): \ P_1 \text{ oscillates between them}}$$
>
> **Units:** $x$ dimensionless; $[\ddot r] = [g] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** at both ends of the band the radial rate vanishes and the radial acceleration points back into the band, so $r$ reverses in a finite time at each end. At the outer end the hanging length $2a - r$ is zero: $P_2$ arrives at the hole with zero velocity, exactly at the limit allowed by the cord, and goes down again.

#### (e) Tension of the cord

> [!derivation] Tension from Newton's law for P2
> **Law:** equation of P2 along the vertical; radial acceleration from the equation free of the tension
> **Source:** Notes.pdf, Eq. 4.4; Problems.pdf, p. 30
>
> $$\begin{aligned}
> T &= m\left(g + \ddot r\right) \quad &\text{(equation of $P_2$ along $\mathbf k$)} \\
> \ddot r &= -\frac{g}{2} + \frac{4a^3g}{3r^3} \quad &\text{(previous box)} \\
> T &= m\left(g - \frac{g}{2} + \frac{4a^3g}{3r^3}\right) \quad &\text{(substituted)} \\
> &= mg\left(\frac12 + \frac{4a^3}{3r^3}\right) \quad &\text{(common factor $mg$)} \\
> T(a) &= mg\left(\frac12 + \frac43\right) \quad &\text{(inner end of the band)} \\
> &= \frac{11}{6}\,mg \quad &\text{(added)} \\
> T(2a) &= mg\left(\frac12 + \frac{4}{24}\right) \quad &\text{(outer end of the band)} \\
> &= \frac23\,mg \quad &\text{(added)}
> \end{aligned}$$
>
> $$\boxed{T = mg\left(\frac12 + \frac{4a^3}{3r^3}\right), \qquad \frac23\,mg \le T \le \frac{11}{6}\,mg}$$
>
> **Units:** $[mg] = [\mathrm{M\,L\,T^{-2}}]$; $a^3/r^3$ dimensionless
> **Meaning:** the expression of the statement. The tension decreases with $r$ and is smallest at the outer end, where it is still positive: the cord stays tense during the whole motion, as assumed.

#### (f) Rough plane

> [!derivation] Friction force on P1
> **Law:** Coulomb friction of a sliding particle, opposite to its velocity relative to the (fixed) plane
> **Source:** Notes.pdf, Eq. 6.20; Notes.pdf, Eq. 6.21; [Lecture 3, Slide 18]
>
> The friction lies in the plane, so the vertical equation of $P_1$ is unchanged and the normal reaction is still the weight. The plane is at rest in $S_0$, so the relative velocity is the velocity of $P_1$.
>
> $$\begin{aligned}
> N_1 &= mg \quad &\text{(equation of $P_1$ along $\mathbf k$)} \\
> \lvert\mathbf v_0^{P_1}\rvert &= \sqrt{\dot r^2 + r^2\dot\theta^2} \quad &\text{(orthonormal polar basis)} \\
> \mathbf R &= -\mu N_1\,\frac{\mathbf v_0^{P_1}}{\lvert\mathbf v_0^{P_1}\rvert} \quad &\text{(Eq. 6.21, $P_1$ sliding)} \\
> &= -\mu mg\,\frac{\dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta}{\sqrt{\dot r^2 + r^2\dot\theta^2}} \quad &\text{($N_1$ and the velocity substituted)}
> \end{aligned}$$
>
> $$\boxed{\mathbf R = -\mu mg\,\frac{\dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta}{\sqrt{\dot r^2 + r^2\dot\theta^2}}}$$
>
> **Units:** $[\mu mg] = [\mathrm{M\,L\,T^{-2}}]$; the fraction is dimensionless
> **Meaning:** a force of constant magnitude opposite to the velocity of $P_1$; it adds no unknown while $P_1$ slides.

> [!derivation] Equations of motion on the rough plane
> **Law:** Newton's second law with the friction added; elimination of the tension
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Sec. 6.6; [Lecture 3, Slide 18]
>
> $$\begin{aligned}
> P_1,\ \mathbf e_r:\ m\left(\ddot r - r\dot\theta^2\right) &= -T - \mu mg\,\frac{\dot r}{\sqrt{\dot r^2 + r^2\dot\theta^2}} \quad &\text{(dot product with $\mathbf e_r$)} \\
> P_1,\ \mathbf e_\theta:\ m\left(r\ddot\theta + 2\dot r\dot\theta\right) &= -\mu mg\,\frac{r\dot\theta}{\sqrt{\dot r^2 + r^2\dot\theta^2}} \quad &\text{(dot product with $\mathbf e_\theta$)} \\
> P_2,\ \mathbf k:\ m\ddot r &= T - mg \quad &\text{(unchanged)} \\
> 2\ddot r - r\dot\theta^2 + g + \mu g\,\frac{\dot r}{\sqrt{\dot r^2 + r^2\dot\theta^2}} &= 0 \quad &\text{(first plus third, divided by $m$)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} 2\ddot r - r\dot\theta^2 + g + \mu g\,\dfrac{\dot r}{\sqrt{\dot r^2 + r^2\dot\theta^2}} = 0 \cr r\ddot\theta + 2\dot r\dot\theta + \mu g\,\dfrac{r\dot\theta}{\sqrt{\dot r^2 + r^2\dot\theta^2}} = 0 \cr T = m\left(g + \ddot r\right), \quad N_1 = mg \end{array}}$$
>
> **Units:** every term of the first two equations $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the two equations for $r$ and $\theta$ hold while $P_1$ slides and the cord is tense; the tension and the normal reaction follow afterwards.

> [!derivation] Angular momentum and energy on the rough plane
> **Law:** transverse equation times r; theorem of the kinetic energy for both particles (power of the forces)
> **Source:** Notes.pdf, Eq. 4.11; Notes.pdf, Sec. 6.6; [Lecture 3, Slide 17]
>
> $$\begin{aligned}
> \frac{d}{dt}\left(r^2\dot\theta\right) &= 2r\dot r\dot\theta + r^2\ddot\theta \quad &\text{(product rule; chain rule on $r^2$)} \\
> &= r\left(r\ddot\theta + 2\dot r\dot\theta\right) \quad &\text{(common factor $r$)} \\
> &= -\mu g\,\frac{r^2\dot\theta}{\sqrt{\dot r^2 + r^2\dot\theta^2}} \quad &\text{(transverse equation of the previous box)} \\
> \frac{dE}{dt} &= -T\,\mathbf e_r\cdot\mathbf v_0^{P_1} + T\,\mathbf k\cdot\mathbf v_0^{P_2} + \mathbf R\cdot\mathbf v_0^{P_1} \quad &\text{(power of the forces not in $E$; $N_1$ and the guide are normal to the velocities)} \\
> &= -T\dot r + T\dot r + \mathbf R\cdot\mathbf v_0^{P_1} \quad &\text{($\mathbf e_r\cdot\mathbf v_0^{P_1} = \dot r$, $\mathbf k\cdot\mathbf v_0^{P_2} = \dot r$)} \\
> &= -\mu mg\,\frac{\mathbf v_0^{P_1}\cdot\mathbf v_0^{P_1}}{\lvert\mathbf v_0^{P_1}\rvert} \quad &\text{(friction of the previous box)} \\
> &= -\mu mg\,\lvert\mathbf v_0^{P_1}\rvert \quad &\text{(square of the magnitude over the magnitude)}
> \end{aligned}$$
>
> $$\boxed{\frac{d}{dt}\left(r^2\dot\theta\right) = -\mu g\,\frac{r^2\dot\theta}{\lvert\mathbf v_0^{P_1}\rvert} \lt 0, \qquad \frac{dE}{dt} = -\mu mg\,\lvert\mathbf v_0^{P_1}\rvert \lt 0}$$
>
> **Units:** $[\mu g\,r^2\dot\theta/v] = [\mathrm{L^2\,T^{-2}}]$; $[\mu mg\,v] = [\mathrm{M\,L^2\,T^{-3}}]$, a power
> **Meaning:** the friction has a moment about the hole and dissipates energy, so neither first integral survives and the problem no longer reduces to the quadratures of part (c): the turning of $P_1$ slows down and the pair loses energy at the rate of the friction power.

#### Answers

| Part of the statement | Answer |
| :--- | :--- |
| (a) Circular motion | $v_0 = \sqrt{ag}$ (circle of radius $a$, $\dot\theta = \sqrt{g/a}$) |
| (b) Tension in that case | $T = mg$ |
| (c) Quadratures, $v_0 = \sqrt{8ag/3}$ | $r^2\dot\theta = h$, $h^2 = 8a^3g/3$; $\dot r^2 = g(-3r^3 + 7ar^2 - 4a^3)/(3r^2)$; $t = \sqrt{3/g}\int_a^r r'\,dr'/\sqrt{-3r'^3 + 7ar'^2 - 4a^3}$ while $r$ grows (from $2a$ downwards on the way back); $\theta = 2\sqrt2\,a^{3/2}\int_a^r dr'/(r'\sqrt{-3r'^3 + 7ar'^2 - 4a^3})$ |
| (d) Band of radii | $\dot r^2 = -g(r - a)(r - 2a)(3r + 2a)/(3r^2) \ge 0$ gives $a \le r \le 2a$; turning points $r = a$ ($\ddot r = 5g/6$) and $r = 2a$ ($\ddot r = -g/3$) |
| (e) Tension | $T = m(g + \ddot r) = mg\left(\frac12 + \frac{4a^3}{3r^3}\right)$, between $\frac23 mg$ and $\frac{11}{6}mg$ |
| (f) Rough plane | $2\ddot r - r\dot\theta^2 + g + \mu g\,\dot r/\sqrt{\dot r^2 + r^2\dot\theta^2} = 0$; $r\ddot\theta + 2\dot r\dot\theta + \mu g\,r\dot\theta/\sqrt{\dot r^2 + r^2\dot\theta^2} = 0$; $T = m(g + \ddot r)$, $N_1 = mg$ |

**Check against the official key:** Problems.pdf, p. 76 lists item 43 with no answer, so there is no key to compare with. The statement itself prints the tension of part (e) and the roots of the polynomial of part (d): the box of part (e) reproduces that tension and the box of part (d) the factorisation with those roots (**match** with the statement). Independent checks: the quadratures were evaluated numerically with unit data ($a$ of 1 m, $g$ of 1 m s$^{-2}$; substitution of $x$ by 3/2 minus one half of the cosine of a new variable $s$, which removes the endpoint singularities, and the midpoint rule with 200000 points) and compared with a direct fourth-order Runge-Kutta integration of the equations of motion free of the tension (step $10^{-5}$ s):

| Quantity | Quadrature of part (c) | Direct integration |
| :--- | :--- | :--- |
| time from $r = a$ to $r = 1.5a$ | $1.36154\sqrt{a/g}$ | $1.36154\sqrt{a/g}$ |
| angle turned from $r = a$ to $r = 1.5a$ | $1.63506$ rad | $1.63507$ rad |
| radial period $\tau_r$ | $6.34243\sqrt{a/g}$ | (not integrated) |
| angle turned in one radial period | $5.0813$ rad ($291.1^\circ$) | (not integrated) |

> [!derivation] Limiting case: the circle of part (a) as a radial equilibrium
> **Law:** equilibrium and linearisation of the radial equation of motion
> **Source:** Notes.pdf, Sec. 4.6; Notes.pdf, Eq. 5.6
>
> With the speed of part (a) the angular momentum is $a\sqrt{ag}$. A small radial perturbation $\rho$ about $r = a$ is kept to first order.
>
> $$\begin{aligned}
> h^2 &= a^2\cdot a g = a^3g \quad &\text{($h = a v_0$, $v_0^2 = ag$)} \\
> \ddot r &= -\frac{g}{2} + \frac{a^3g}{2r^3} \quad &\text{(equation of motion free of $T$ with this $h$)} \\
> \ddot r\big|_{r = a} &= -\frac{g}{2} + \frac{g}{2} = 0 \quad &\text{($r = a$ is an equilibrium of the radial motion)} \\
> \frac{a^3}{\left(a + \rho\right)^3} &\simeq 1 - \frac{3\rho}{a} \quad &\text{(first-order expansion, $\lvert\rho\rvert \ll a$)} \\
> \ddot\rho &= -\frac{g}{2} + \frac{g}{2}\left(1 - \frac{3\rho}{a}\right) \quad &\text{($r = a + \rho$ substituted)} \\
> \ddot\rho + \frac{3g}{2a}\,\rho &= 0 \quad &\text{(simplified: the form of Eq. 5.6)}
> \end{aligned}$$
>
> $$\boxed{v_0 = \sqrt{ag}: \ r = a \ \text{is a stable radial equilibrium}, \qquad \omega_r = \sqrt{\frac{3g}{2a}}}$$
>
> **Units:** $[g/a] = [\mathrm{T^{-2}}]$, so $[\omega_r] = [\mathrm{T^{-1}}]$
> **Meaning:** consistent with parts (a) and (b): with the speed $\sqrt{ag}$ the radial acceleration vanishes at $r = a$, and a slightly different push makes $r$ oscillate harmonically about $a$, as the speed $\sqrt{8ag/3}$ does with a large amplitude between $a$ and $2a$.

---

## Problem 44: The Little Prince Throwing Seeds

### Reference Frames, Bases and Coordinates

The little Prince throws a baobab seed from the equator of his spherical asteroid, of radius $R$ and mass $M$, which does not rotate; the initial velocity has the magnitude $v_0$ and makes the angle $\gamma$ of 60 degrees with the local horizontal, and the seed reaches the apocentre $3R$ before falling back (Problems.pdf, p. 31). The statement asks for $v_0$ in terms of the data and the gravitational constant $G$. The solution follows the Newtonian approach of Notes.pdf, Sec. 7.1 to Sec. 7.7, applied to Kepler's problem as in Notes.pdf, Sec. 8.2 to Sec. 8.5.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, origin at the centre $O$ of the asteroid (Notes.pdf, Eq. 2.1; Notes.pdf, Sec. 8.2) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$: $\mathbf i$ from $O$ through the launch point; $\mathbf j$ along the horizontal part of the launch velocity; $\mathbf k = \mathbf i\times\mathbf j$, perpendicular to the plane of the motion |
| Polar basis | $\mathcal B_1 = \{\mathbf e_r, \mathbf e_\theta, \mathbf k\}$, $\mathcal B_0$ turned by $\theta$ about $\mathbf k$; $\mathbf e_r$ from $O$ towards the seed $P$ (Notes.pdf, Eq. 8.2) |
| Coordinates | $r$, the distance $OP$; $\theta$, the polar angle of $P$ from $\mathbf i$, positive about $\mathbf k$ |
| Hypotheses | modelling hypothesis: the asteroid is modelled as a point mass $M$ at $O$ for every distance $r$ not smaller than $R$, as the Earth is modelled as a point particle in Notes.pdf, Ch. 8 (Fig. 8.1); seed mass $m \ll M$, so the acceleration of $O$ is neglected and $S_0$ is inertial; the asteroid does not rotate, so the launch velocity measured by the Prince is the velocity in $S_0$; no atmosphere; between launch and landing the seed moves outside the asteroid (checked below) |
| Constraints | none in flight: the seed is a free particle; the central force keeps it in the plane of $\mathbf i$ and $\mathbf j$ (Notes.pdf, Sec. 4.8.1) |
| Degrees of freedom | 3 in space; 2 in the plane of the motion ($r$, $\theta$) |
| Data | $R$ [m], $M$ [kg], $G$ [m$^3$ kg$^{-1}$ s$^{-2}$], $\gamma$ of 60 degrees, apocentre $r_a$ equal to $3R$; gravitational parameter $\mu = GM$ [m$^3$ s$^{-2}$] |
| Unknown | the launch speed $v_0$ [m s$^{-1}$] |
| Initial state | $r(0) = R$, $\theta(0) = 0$; velocity $v_0$ at $\gamma$ above the local horizontal, the plane perpendicular to $\mathbf e_r$ at the launch point |
| Applied force | the gravitational attraction of the asteroid, towards $O$ |
| Constraint and inertia forces | none in flight; $S_0$ inertial |

![[attachments/EM-SOL/p44-launch.svg]]

### Change of Basis and Position Vector

![[attachments/EM-SOL/p44-rotation-k.svg]]

> [!derivation] Polar basis: rotation about k
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 8.2
>
> View along $\mathbf k$, which points out of the paper (⊙) because it is the cross product of $\mathbf i$ (to the right) and $\mathbf j$ (up): a positive rotation about $\mathbf k$ is counterclockwise, the sense in which the seed moves away from the launch point. $\mathbf e_r$ is $\mathbf i$ turned by $\theta$: hypotenuse 1, adjacent leg $\cos\theta$ along $\mathbf i$, opposite leg $\sin\theta$ along $\mathbf j$. $\mathbf e_\theta$ is $\mathbf j$ turned by $\theta$: adjacent leg $\cos\theta$ along $\mathbf j$, opposite leg $\sin\theta$ along minus $\mathbf i$ (the upward vector turned counterclockwise leans to the left: the minus sign).
>
> $$\begin{aligned}
> \mathbf e_r &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j \quad &\text{(right triangle of $\mathbf e_r$)} \\
> \mathbf e_\theta &= -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(right triangle of $\mathbf e_\theta$: opposite leg on $-\mathbf i$)} \\
> \mathbf e_r\times\mathbf e_\theta &= \cos^2\theta\,\mathbf i\times\mathbf j - \sin^2\theta\,\mathbf j\times\mathbf i \quad &\text{(distributive law; $\mathbf i\times\mathbf i = \mathbf j\times\mathbf j = \mathbf 0$)} \\
> &= \left(\cos^2\theta + \sin^2\theta\right)\mathbf k = \mathbf k \quad &\text{(right-handed; $\mathbf i\times\mathbf j = \mathbf k$, $\mathbf j\times\mathbf i = -\mathbf k$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expansion along the third row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\theta + \sin^2\theta = 1 \quad &\text{(row 1 times row 1)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{12} &= \cos\theta\sin\theta - \sin\theta\cos\theta = 0 \quad &\text{(row 1 times row 2; row 3 is the unit row of $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** dimensionless direction cosines: $[1]$
> **Meaning:** at the launch point ($\theta = 0$) the basis $\mathcal B_1$ coincides with $\mathcal B_0$: $\mathbf e_r$ is the local vertical and $\mathbf e_\theta$ the local horizontal in the plane of the throw.

> [!derivation] Position vector of the seed
> **Law:** position vector of a point particle; polar coordinates in the plane of the motion
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 8.3
>
> In the plane of the motion the segment $OP$ is the hypotenuse $r$ of the right triangle with the leg $r\cos\theta$ along $\mathbf i$ (adjacent to $\theta$) and the leg $r\sin\theta$ along $\mathbf j$ (opposite).
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OP} = r\,\mathbf e_r \quad &\text{(definition; $\mathbf e_r$ from $O$ towards $P$)} \\
> &= r\cos\theta\,\mathbf i + r\sin\theta\,\mathbf j \quad &\text{($\mathbf e_r$ in $\mathcal B_0$)} \\
> \mathbf r_0^P(0) &= R\,\mathbf i \quad &\text{(launch point on the surface, $\theta(0) = 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = r\,\mathbf e_r = r\cos\theta\,\mathbf i + r\sin\theta\,\mathbf j, \qquad \mathbf r_0^P(0) = R\,\mathbf i}$$
>
> **Units:** $[r] = [R] = [\mathrm{L}]$
> **Meaning:** the outward normal of the sphere at the launch point is $\mathbf e_r$, so "local vertical" means $\mathbf e_r$ and "local horizontal" the plane perpendicular to it.

### Kinematics

> [!derivation] Derivatives of the polar unit vectors
> **Law:** derivative of a unit vector turning about a fixed axis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \dot\theta\,\mathbf k \quad &\text{($\mathcal B_1$ turns about the fixed $\mathbf k$ with the angle $\theta$)} \\
> \mathbf k\times\mathbf e_r &= \cos\theta\,\mathbf j - \sin\theta\,\mathbf i = \mathbf e_\theta \quad &\text{($\mathbf k\times\mathbf i = \mathbf j$, $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> \mathbf k\times\mathbf e_\theta &= -\sin\theta\,\mathbf j - \cos\theta\,\mathbf i = -\mathbf e_r \quad &\text{(same products)} \\
> \dot{\mathbf e}_r &= \boldsymbol\omega_{10}\times\mathbf e_r = \dot\theta\,\mathbf e_\theta \quad &\text{(Eq. 1.62)} \\
> \dot{\mathbf e}_\theta &= \boldsymbol\omega_{10}\times\mathbf e_\theta = -\dot\theta\,\mathbf e_r \quad &\text{(Eq. 1.62)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf e}_r = \dot\theta\,\mathbf e_\theta, \qquad \dot{\mathbf e}_\theta = -\dot\theta\,\mathbf e_r}$$
>
> **Units:** $[\dot\theta] = [\mathrm{T^{-1}}]$
> **Meaning:** the polar basis turns with the seed round the centre of the asteroid.

> [!derivation] Velocity and acceleration of the seed
> **Law:** time derivatives of the position vector in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Notes.pdf, Eq. 8.3
>
> $$\begin{aligned}
> \mathbf v_0^P &= \dot r\,\mathbf e_r + r\,\dot{\mathbf e}_r \quad &\text{(Eq. 2.3; product rule)} \\
> &= \dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta \quad &\text{($\dot{\mathbf e}_r = \dot\theta\,\mathbf e_\theta$)} \\
> \mathbf a_0^P &= \ddot r\,\mathbf e_r + \dot r\,\dot{\mathbf e}_r + \dot r\dot\theta\,\mathbf e_\theta + r\ddot\theta\,\mathbf e_\theta + r\dot\theta\,\dot{\mathbf e}_\theta \quad &\text{(Eq. 2.4; product rule on each term)} \\
> &= \ddot r\,\mathbf e_r + \dot r\dot\theta\,\mathbf e_\theta + \dot r\dot\theta\,\mathbf e_\theta + r\ddot\theta\,\mathbf e_\theta - r\dot\theta^2\,\mathbf e_r \quad &\text{(derivatives of the unit vectors substituted)} \\
> &= \left(\ddot r - r\dot\theta^2\right)\mathbf e_r + \left(r\ddot\theta + 2\dot r\dot\theta\right)\mathbf e_\theta \quad &\text{(grouped)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta, \qquad \mathbf a_0^P = \left(\ddot r - r\dot\theta^2\right)\mathbf e_r + \left(r\ddot\theta + 2\dot r\dot\theta\right)\mathbf e_\theta}$$
>
> **Units:** $[\dot r] = [r\dot\theta] = [\mathrm{L\,T^{-1}}]$; every acceleration term $[\mathrm{L\,T^{-2}}]$
> **Meaning:** $\dot r$ is the vertical (radial) part of the velocity and $r\dot\theta$ its horizontal (transverse) part, at every point of the flight.

> [!derivation] Launch velocity and the velocity at the apocentre
> **Law:** components of the launch velocity from its right triangle; a maximum of r has zero rate
> **Source:** Notes.pdf, Eq. 8.3; Notes.pdf, Sec. 8.4; Problems.pdf, p. 31
>
> In the right triangle of the launch velocity the hypotenuse is $v_0$, the leg along the local horizontal $\mathbf e_\theta$ is adjacent to $\gamma$ and the leg along the local vertical $\mathbf e_r$ is opposite to it. The apocentre is the largest distance reached, an interior maximum of the differentiable function $r(t)$.
>
> $$\begin{aligned}
> \mathbf v_0^P(0) &= v_0\sin\gamma\,\mathbf e_r + v_0\cos\gamma\,\mathbf e_\theta \quad &\text{(opposite leg vertical, adjacent leg horizontal)} \\
> \dot r(0) &= v_0\sin\gamma \quad &\text{(component along $\mathbf e_r$ compared with the velocity box at $r = R$)} \\
> &= \frac{\sqrt3}{2}\,v_0 \quad &\text{($\sin 60^\circ = \sqrt3/2$)} \\
> R\,\dot\theta(0) &= v_0\cos\gamma \quad &\text{(component along $\mathbf e_\theta$)} \\
> &= \frac12\,v_0 \quad &\text{($\cos 60^\circ = 1/2$)} \\
> \dot r(t_a) &= 0 \quad &\text{(zero derivative at the maximum of $r$)} \\
> \mathbf v_0^P(t_a) &= r_a\dot\theta(t_a)\,\mathbf e_\theta \quad &\text{(velocity box with $\dot r = 0$)}
> \end{aligned}$$
>
> $$\boxed{\dot r(0) = \frac{\sqrt3}{2}\,v_0, \quad R\,\dot\theta(0) = \frac12\,v_0; \qquad \text{at the apocentre } \dot r = 0, \ v_a = r_a\dot\theta_a}$$
>
> **Units:** $[v_0] = [R\dot\theta] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the seed leaves the surface climbing; at the highest point its velocity is purely horizontal (transverse).

### Forces and Equations of Motion

The free-body diagram of the seed in flight shows only the attraction of the asteroid, directed to its centre. $S_0$ is inertial, so no inertia force acts, and in flight there is no constraint.

![[attachments/EM-SOL/p44-fbd.svg]]

> [!derivation] Gravitational force on the seed
> **Law:** Newton's law of universal gravitation for a spherical body, outside it
> **Source:** Notes.pdf, Eq. 8.1; [Lecture 4, Slide 9]
>
> $$\begin{aligned}
> \mathbf F &= -\frac{G M m}{r^2}\,\mathbf e_r \quad &\text{(attraction towards $O$, Eq. 8.1 with the asteroid as the central body)} \\
> \mu &= G M \quad &\text{(gravitational parameter of the asteroid)} \\
> \mathbf F &= -\frac{\mu m}{r^2}\,\mathbf e_r \quad &\text{(substituted)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F = -\frac{\mu m}{r^2}\,\mathbf e_r, \qquad \mu = G M}$$
>
> **Units:** $[\mu] = [G][M] = [\mathrm{L^3\,M^{-1}\,T^{-2}}][\mathrm{M}] = [\mathrm{L^3\,T^{-2}}]$; $[\mu m/r^2] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** a central force (its line of action passes through $O$) of the inverse-square type: the seed solves Kepler's problem about the asteroid.

> [!derivation] Newton's second law projected on the polar basis
> **Law:** Newton's second law in an inertial frame
> **Source:** Notes.pdf, Eq. 8.4; Notes.pdf, Eq. 8.5; Notes.pdf, Eq. 8.6
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= -\frac{\mu m}{r^2}\,\mathbf e_r \quad &\text{(the only force)} \\
> \mathbf e_r:\ \ddot r - r\dot\theta^2 &= -\frac{\mu}{r^2} \quad &\text{(dot product with $\mathbf e_r$, divided by $m$)} \\
> \mathbf e_\theta:\ r\ddot\theta + 2\dot r\dot\theta &= 0 \quad &\text{(dot product with $\mathbf e_\theta$, divided by $m$)}
> \end{aligned}$$
>
> $$\boxed{\ddot r - r\dot\theta^2 = -\frac{\mu}{r^2}, \qquad r\ddot\theta + 2\dot r\dot\theta = 0}$$
>
> **Units:** $[\ddot r] = [r\dot\theta^2] = [\mu/r^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the mass of the seed drops out: its flight does not depend on how heavy it is.

> [!derivation] Areal integral: constant angular momentum per unit mass
> **Law:** the transverse equation times r is an exact derivative; Barrow's rule
> **Source:** Notes.pdf, Eq. 8.7; [Lecture 4, Slide 12]
>
> $$\begin{aligned}
> \frac{d}{dt}\left(r^2\dot\theta\right) &= 2r\dot r\dot\theta + r^2\ddot\theta \quad &\text{(product rule; chain rule on $r^2$)} \\
> &= r\left(r\ddot\theta + 2\dot r\dot\theta\right) \quad &\text{(common factor $r$)} \\
> &= 0 \quad &\text{(transverse equation)} \\
> \left[r^2\dot\theta\right]_0^t &= 0 \quad &\text{(Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{h = r^2\dot\theta = r\left(r\dot\theta\right) = \text{const}}$$
>
> **Units:** $[h] = [\mathrm{L^2\,T^{-1}}]$
> **Meaning:** the distance to the centre times the horizontal part of the velocity is the same at every point of the flight (Kepler's second law, Notes.pdf, Eq. 8.8).

> [!derivation] Energy integral (vis-viva equation)
> **Law:** the radial equation times the radial rate is an exact derivative (chain rule); Barrow's rule
> **Source:** Notes.pdf, Eq. 8.5; Notes.pdf, Eq. 8.19; Notes.pdf, Eq. 4.31
>
> $$\begin{aligned}
> \ddot r - \frac{h^2}{r^3} + \frac{\mu}{r^2} &= 0 \quad &\text{(radial equation; $r\dot\theta^2 = h^2/r^3$)} \\
> \dot r\ddot r - \frac{h^2}{r^3}\,\dot r + \frac{\mu}{r^2}\,\dot r &= 0 \quad &\text{(times $\dot r$)} \\
> \frac{d}{dt}\left(\tfrac12\dot r^2\right) &= \dot r\ddot r \quad &\text{(chain rule)} \\
> \frac{d}{dt}\left(\frac{h^2}{2r^2}\right) &= -\frac{h^2}{r^3}\,\dot r \quad &\text{(chain rule; $h$ constant)} \\
> \frac{d}{dt}\left(-\frac{\mu}{r}\right) &= \frac{\mu}{r^2}\,\dot r \quad &\text{(chain rule)} \\
> \frac{d}{dt}\left[\tfrac12\dot r^2 + \frac{h^2}{2r^2} - \frac{\mu}{r}\right] &= 0 \quad &\text{(the second row is this sum of derivatives)} \\
> \left[\tfrac12\dot r^2 + \frac{h^2}{2r^2} - \frac{\mu}{r}\right]_0^t &= 0 \quad &\text{(Barrow's rule)} \\
> \tfrac12\left(\dot r^2 + r^2\dot\theta^2\right) - \frac{\mu}{r} &= \xi \quad &\text{($h^2/r^2 = r^2\dot\theta^2$; $\xi$ the constant)}
> \end{aligned}$$
>
> $$\boxed{\xi = \tfrac12\,\mathbf v_0^P\cdot\mathbf v_0^P - \frac{\mu}{r} = \text{const}}$$
>
> **Units:** $[v^2] = [\mu/r] = [\mathrm{L^2\,T^{-2}}]$
> **Meaning:** the mechanical energy per unit mass, kinetic plus the potential $-\mu/r$ of the attraction with zero at infinity (Notes.pdf, Eq. 8.19): the seed slows down as it climbs.

### Answers and Checks

#### Launch speed

> [!derivation] Angular momentum at launch and at the apocentre
> **Law:** areal integral evaluated at two points of the flight
> **Source:** Notes.pdf, Eq. 8.7; Problems.pdf, p. 31
>
> $$\begin{aligned}
> h &= R\left(R\dot\theta(0)\right) \quad &\text{(launch: $r = R$)} \\
> &= R\,v_0\cos\gamma \quad &\text{(horizontal part of the launch velocity)} \\
> &= \tfrac12\,R\,v_0 \quad &\text{($\cos 60^\circ = 1/2$)} \\
> h &= r_a\left(r_a\dot\theta_a\right) = 3R\,v_a \quad &\text{(apocentre: $r_a = 3R$, $v_a = r_a\dot\theta_a$)} \\
> v_a &= \frac{h}{3R} \quad &\text{(solved)} \\
> &= \frac{R\,v_0/2}{3R} \quad &\text{($h$ at launch)} \\
> &= \frac{v_0}{6} \quad &\text{($R$ cancelled)}
> \end{aligned}$$
>
> $$\boxed{h = \tfrac12\,R\,v_0, \qquad v_a = \frac{v_0}{6}}$$
>
> **Units:** $[R\,v_0] = [\mathrm{L^2\,T^{-1}}]$; $[v_a] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** at three times the distance the horizontal speed is one third of the initial horizontal part, which is itself one half of the launch speed.

> [!derivation] Launch speed from the energy integral
> **Law:** vis-viva equation evaluated at launch and at the apocentre
> **Source:** Notes.pdf, Eq. 8.19; Problems.pdf, p. 31
>
> $$\begin{aligned}
> \tfrac12\,v_0^2 - \frac{\mu}{R} &= \tfrac12\,v_a^2 - \frac{\mu}{3R} \quad &\text{(same $\xi$ at launch and at the apocentre)} \\
> \tfrac12\,v_0^2 - \frac{\mu}{R} &= \frac{v_0^2}{72} - \frac{\mu}{3R} \quad &\text{($v_a = v_0/6$)} \\
> \left(\frac12 - \frac{1}{72}\right)v_0^2 &= \left(1 - \frac13\right)\frac{\mu}{R} \quad &\text{(terms collected)} \\
> \frac{35}{72}\,v_0^2 &= \frac23\,\frac{\mu}{R} \quad &\text{(fractions)} \\
> v_0^2 &= \frac23\cdot\frac{72}{35}\,\frac{\mu}{R} \quad &\text{(times $72/35$)} \\
> &= \frac{48}{35}\,\frac{\mu}{R} \quad &\text{(product)} \\
> v_0 &= \sqrt{\frac{48}{35}\,\frac{G M}{R}} \quad &\text{(positive root; $\mu = GM$)}
> \end{aligned}$$
>
> $$\boxed{v_0 = \sqrt{\frac{48\,G M}{35\,R}} = 4\sqrt{\frac{3\,G M}{35\,R}} \simeq 1.1711\sqrt{\frac{G M}{R}}}$$
>
> **Units:** $[G M/R] = [\mathrm{L^3\,M^{-1}\,T^{-2}}][\mathrm{M}][\mathrm{L^{-1}}] = [\mathrm{L^2\,T^{-2}}]$, so $[v_0] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** a little more than the circular speed at the surface (factor 1.17) and less than the escape speed (factor 1.41, Notes.pdf, Eq. 8.21): the seed is on a closed orbit and comes back.

> [!derivation] Check: 3R is the larger turning radius and the seed falls back
> **Law:** turning radii are the roots of the vis-viva equation with zero radial rate
> **Source:** Notes.pdf, Eq. 4.28; Notes.pdf, Eq. 8.19
>
> $$\begin{aligned}
> \xi &= \tfrac12\cdot\frac{48\,\mu}{35\,R} - \frac{\mu}{R} \quad &\text{(energy at launch)} \\
> &= -\frac{11\,\mu}{35\,R} \lt 0 \quad &\text{(fractions)} \\
> \frac{h^2}{2} &= \frac{R^2v_0^2}{8} \quad &\text{($h = Rv_0/2$)} \\
> &= \frac{6\,\mu R}{35} \quad &\text{($v_0^2 = 48\mu/(35R)$)} \\
> \frac{6\,\mu R}{35\,r^2} - \frac{\mu}{r} &= -\frac{11\,\mu}{35\,R} \quad &\text{(energy integral with $\dot r = 0$)} \\
> 11\,r^2 - 35\,R\,r + 6\,R^2 &= 0 \quad &\text{(times $35Rr^2/\mu$; terms moved to the left)} \\
> r &= \frac{35 \pm \sqrt{35^2 - 4\cdot 11\cdot 6}}{22}\,R \quad &\text{(quadratic formula)} \\
> &= \frac{35 \pm 31}{22}\,R \quad &\text{($1225 - 264 = 961 = 31^2$)} \\
> r_a &= 3R, \quad r_p = \frac{2}{11}\,R \quad &\text{(the two roots)}
> \end{aligned}$$
>
> $$\boxed{\xi = -\frac{11\,\mu}{35\,R} \lt 0, \qquad r_p = \frac{2}{11}\,R \lt R \lt r_a = 3R}$$
>
> **Units:** $[\xi] = [\mu/R] = [\mathrm{L^2\,T^{-2}}]$; $r_p$ and $r_a$ in $[\mathrm{L}]$
> **Meaning:** the energy is negative, so the orbit is an ellipse; $3R$ is its larger turning radius, the apocentre, consistent with the data. The pericentre lies inside the asteroid: after the apocentre the seed comes down and hits the surface before reaching it.

![[attachments/EM-SOL/p44-orbit.svg]]

| Part of the statement | Answer |
| :--- | :--- |
| Launch speed | $v_0 = \sqrt{\dfrac{48\,GM}{35\,R}} \simeq 1.1711\sqrt{GM/R}$ |
| Intermediate results | $h = \frac12 Rv_0$; speed at the apocentre $v_a = v_0/6$; $\xi = -\frac{11}{35}\,GM/R$; pericentre of the full ellipse $\frac{2}{11}R$ (inside the asteroid); eccentricity $\frac{31}{35}$ |

**Check against the official key:** Problems.pdf, p. 76 lists item 44 with no answer, so there is no key to compare with. Independent checks: the orbit equation of Notes.pdf, Eq. 8.13, fitted to the launch data alone, gives back the apocentre $3R$ (box below); the semi-major axis gives back the energy through Notes.pdf, Eq. 8.19 (box below); and a direct fourth-order Runge-Kutta integration of the equations of motion (unit values $\mu$ and $R$ of 1, step $10^{-5}$) from the launch data with the speed found reaches the largest distance $3.0000R$ with the speed $0.16667v_0$, at $42.1^\circ$ from the launch point, and lands after $11.27\sqrt{R^3/(GM)}$.

> [!derivation] Independent check with the conic of Kepler's problem
> **Law:** orbit equation of Kepler's problem and its first integral; launch data as initial conditions
> **Source:** Notes.pdf, Eq. 8.10; Notes.pdf, Eq. 8.13; Notes.pdf, Eq. 8.14
>
> $$\begin{aligned}
> u &= \frac{\mu}{h^2}\left[1 + e\cos\left(\theta + \psi\right)\right], \quad u' = -\frac{\mu e}{h^2}\sin\left(\theta + \psi\right) \quad &\text{(Eq. 8.13 and its derivative; $u = 1/r$)} \\
> \left(u - \frac{\mu}{h^2}\right)^2 + u'^2 &= \left(\frac{\mu e}{h^2}\right)^2 \quad &\text{(squared and added; $\cos^2 + \sin^2 = 1$)} \\
> u_0 &= \frac1R \quad &\text{(launch point)} \\
> u_0' &= -\frac{\dot r(0)}{h} \quad &\text{($\dot r = -h\,u'$, Eq. 8.10)} \\
> &= -\frac{\sqrt3\,v_0/2}{R\,v_0/2} = -\frac{\sqrt3}{R} \quad &\text{(launch data; $v_0/2$ cancelled)} \\
> \frac{\mu}{h^2} &= \frac{\mu}{12\,\mu R/35} \quad &\text{($h^2 = 12\,\mu R/35$, previous box)} \\
> &= \frac{35}{12\,R} \quad &\text{($\mu$ cancelled)} \\
> \left(\frac{\mu e}{h^2}\right)^2 &= \left(\frac{1}{R} - \frac{35}{12R}\right)^2 + \frac{3}{R^2} \quad &\text{(second row with the launch data)} \\
> &= \frac{529 + 432}{144\,R^2} = \frac{961}{144\,R^2} \quad &\text{(common denominator $144R^2$)} \\
> \frac{\mu e}{h^2} &= \frac{31}{12\,R} \quad &\text{(positive square root)} \\
> e &= \frac{31}{12R}\cdot\frac{12R}{35} = \frac{31}{35} \quad &\text{(divided by $\mu/h^2$)} \\
> r_a &= \frac{h^2/\mu}{1 - e} \quad &\text{(Eq. 8.14 at the apocentre, cosine equal to $-1$)} \\
> &= \frac{12R/35}{4/35} = 3R \quad &\text{($h^2/\mu = 12R/35$, $1 - e = 4/35$)}
> \end{aligned}$$
>
> $$\boxed{e = \frac{31}{35}, \qquad p = \frac{h^2}{\mu} = \frac{12}{35}\,R, \qquad r_a = \frac{p}{1 - e} = 3R}$$
>
> **Units:** $[u] = [u'] = [\mu/h^2] = [\mathrm{L^{-1}}]$; $e$ dimensionless
> **Meaning:** the conic through the launch point with the launch velocity has exactly the apocentre of the statement: a second derivation, independent of the energy balance, confirms the speed found.

> [!derivation] Independent check with the semi-major axis
> **Law:** semi-major axis from the apsides; constant of the vis-viva equation
> **Source:** Notes.pdf, Eq. 8.15; Notes.pdf, Eq. 8.19
>
> $$\begin{aligned}
> 2a_o &= r_p + r_a \quad &\text{(Eq. 8.15, $a_o$ the semi-major axis)} \\
> &= \frac{2}{11}\,R + 3R = \frac{35}{11}\,R \quad &\text{(apsides of the turning-radius box)} \\
> -\frac{\mu}{2a_o} &= -\frac{11\,\mu}{35\,R} \quad &\text{(constant of Eq. 8.19)}
> \end{aligned}$$
>
> $$\boxed{-\frac{\mu}{2a_o} = -\frac{11\,\mu}{35\,R} = \xi}$$
>
> **Units:** $[\mu/a_o] = [\mathrm{L^2\,T^{-2}}]$
> **Meaning:** the energy computed from the launch data equals the energy that Kepler's problem assigns to an ellipse with these apsides.

> [!derivation] Check: position of the apocentre and of the landing point
> **Law:** orbit equation of Kepler's problem at the launch point; symmetry of the conic about its apse line
> **Source:** Notes.pdf, Eq. 8.10; Notes.pdf, Eq. 8.13; Notes.pdf, Eq. 8.14
>
> Write $\nu = \theta + \psi$ for the angle measured from the pericentre, so that $\nu_0 = \psi$ at the launch point.
>
> $$\begin{aligned}
> \frac1R &= \frac{1}{p}\left(1 + e\cos\nu_0\right) \quad &\text{(Eq. 8.13 at launch, $p = h^2/\mu$)} \\
> \cos\nu_0 &= \frac{p/R - 1}{e} \quad &\text{(solved for the cosine)} \\
> &= \frac{12/35 - 1}{31/35} = -\frac{23}{31} \quad &\text{($p = 12R/35$, $e = 31/35$)} \\
> \dot r(0) &= h\,\frac{e}{p}\sin\nu_0 \quad &\text{($\dot r = -h\,u'$, Eq. 8.10, with $u'$ of the conic check box)} \\
> \sin\nu_0 &\gt 0 \quad &\text{(the seed climbs at launch: $\dot r(0) = v_0\sin\gamma \gt 0$)} \\
> \sin\nu_0 &= \sqrt{1 - \frac{529}{961}} = \frac{\sqrt{432}}{31} = \frac{12\sqrt3}{31} \quad &\text{(positive root)} \\
> \nu_0 &= \arccos\left(-\frac{23}{31}\right) = 137.9^\circ \quad &\text{(second quadrant: negative cosine, positive sine)} \\
> \theta_a &= 180^\circ - \nu_0 = 42.1^\circ \quad &\text{(apocentre at $\nu = 180^\circ$)} \\
> \nu_L &= 360^\circ - \nu_0 \quad &\text{(second root of $r = R$: the conic is symmetric about its apse line)} \\
> \theta_L &= \nu_L - \nu_0 = 2\,\theta_a = 84.2^\circ \quad &\text{(angle swept from launch to landing)}
> \end{aligned}$$
>
> $$\boxed{\cos\nu_0 = -\frac{23}{31}, \quad \nu_0 = 137.9^\circ, \quad \text{apocentre at } \theta_a = 42.1^\circ, \quad \text{landing at } \theta_L = 84.2^\circ}$$
>
> **Units:** $p/R$ and $e$ dimensionless; angles in degrees
> **Meaning:** the seed reaches its largest distance after turning $42.1^\circ$ about the centre (the value found by the numerical integration) and lands, by symmetry, $84.2^\circ$ away from the Prince; the sine of the launch anomaly agrees with the radial rate of the conic check box, whose $u_0'$ gives the same $12\sqrt3/31$.

> [!derivation] Limiting cases of the general launch speed
> **Law:** the same two first integrals with the apocentre and the launch angle kept as symbols
> **Source:** Notes.pdf, Eq. 8.7; Notes.pdf, Eq. 8.19; Notes.pdf, Eq. 8.20; Notes.pdf, Eq. 8.21
>
> $$\begin{aligned}
> v_a &= \frac{R}{r_a}\,v_0\cos\gamma \quad &\text{(areal integral: $R\,v_0\cos\gamma = r_a v_a$)} \\
> \tfrac12\,v_0^2\left(1 - \frac{R^2}{r_a^2}\cos^2\gamma\right) &= \mu\left(\frac1R - \frac{1}{r_a}\right) \quad &\text{(vis-viva at both points, terms collected)} \\
> v_0^2 &= \frac{2\mu\left(1/R - 1/r_a\right)}{1 - \left(R/r_a\right)^2\cos^2\gamma} \quad &\text{(solved)} \\
> r_a \to \infty:\quad v_0^2 &\to \frac{2\mu}{R} \quad &\text{(escape speed, Eq. 8.21)} \\
> \gamma = 90^\circ:\quad v_0^2 &= 2\mu\left(\frac1R - \frac{1}{r_a}\right) \quad &\text{(vertical throw: $\cos\gamma = 0$)} \\
> \gamma = 0:\quad v_0^2 &= \frac{2\mu\left(r_a - R\right)}{R\,r_a}\cdot\frac{r_a^2}{\left(r_a - R\right)\left(r_a + R\right)} \quad &\text{(common denominators; difference of squares)} \\
> &= \frac{2\mu\,r_a}{R\left(r_a + R\right)} \quad &\text{(common factors cancelled)} \\
> \gamma = 0,\ r_a \to R:\quad v_0^2 &\to \frac{\mu}{R} \quad &\text{(circular speed, Eq. 8.20)} \\
> r_a = 3R,\ \gamma = 60^\circ:\quad v_0^2 &= \frac{2\mu\cdot\frac{2}{3R}}{1 - \frac19\cdot\frac14} \quad &\text{(the case of the statement)} \\
> &= \frac{4\mu/(3R)}{35/36} = \frac{48\,\mu}{35\,R} \quad &\text{(fractions)}
> \end{aligned}$$
>
> $$\boxed{v_0^2 = \frac{2\mu\left(1/R - 1/r_a\right)}{1 - \left(R/r_a\right)^2\cos^2\gamma}: \ \text{escape speed for } r_a \to \infty, \ \text{circular speed for } \gamma = 0,\ r_a \to R}$$
>
> **Units:** $[\mu/R] = [\mathrm{L^2\,T^{-2}}]$; the denominator is dimensionless
> **Meaning:** the general formula reduces to the escape speed when the apocentre goes to infinity, to the energy balance of a vertical flight when the throw is vertical (no horizontal speed at the top), and to the circular speed for a horizontal throw that never climbs; it gives back the result of the statement.
