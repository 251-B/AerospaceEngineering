---
title: "Topic 5: Relative Motion"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
ground_truth: "slides/05_-_Relative_motion.pdf (Slides 1-31) & teoria/Notes.pdf (Sections 1.5, 1.7, Chapter 3, Section 4.9)"
tier: "Theory Master Guide"
language: "English"
tags:
  - topic-5
  - relative-motion
  - coriolis-theorem
  - inertia-forces
  - euler-angles
---

# 🔄 Topic 5: Relative Motion

## 📌 Syllabus & Pedagogical Map
This guide develops **relative motion** of the point particle: how two observers that move with respect to each other describe the same particle, and how Newton's second law must be corrected when it is written in a non-inertial reference frame. It follows **`slides/05_-_Relative_motion.pdf`** (Slides 1–31) in the same order, and the corresponding text of **`teoria/Notes.pdf`**: Section 1.5 (change of basis, simple rotations and sequences of rotations, Eqs. 1.6–1.23), Section 1.7 (angular velocity, Eqs. 1.62 and 1.73), Chapter 3 (Coriolis theorem and relative kinematics, Eqs. 3.1–3.29) and Section 4.9 (dynamics of relative motion, Eqs. 4.59–4.63). Equation numbers quoted below are the numbers printed in `Notes.pdf`. Every step that the slides leave to the reader (the derivative of a basis vector in the Slide 16 example, the Slide 18 example, the composite angular velocity of Slides 20–21 and the 3-2-1 exercise of Slide 21) is written out in full.

* [[Concept - Attitude of a Reference Frame and Euler Angles|Attitude of a Reference Frame & Euler Angles]]
* [[Concept - Angular Velocity Angular Acceleration and Coriolis Theorem|Angular Velocity, Angular Acceleration & Coriolis Theorem]]
* [[Concept - Relative Kinematics of the Point Particle|Relative Kinematics of the Point Particle]]
* [[Concept - Inertia Forces and Dynamics in Non-Inertial Frames|Inertia Forces & Dynamics in Non-Inertial Frames]]
* [[Formula Sheet - Topic 5 Relative Motion|Formula Sheet: Topic 5 Relative Motion]]
* [[Problem Set - Topic 5 Relative Motion|Official Problem Statements]]
* [[Solution Set - Topic 5 Relative Motion|Full Analytical Solutions]]

Prerequisites: [[Concept - Vector Bases Rotation Matrices and Poisson Theorem]] (Topic 1) and [[Concept - Newton Laws and Equations of Motion]] (Topic 2).

> **Central idea.** A vector can be *defined* in one reference frame, *differentiated* in another and *expressed* in yet another basis (Slides 17 and 20). Position vectors only add (Notes Eq. 3.16), but time derivatives depend on the observer: the Coriolis theorem (Notes Eq. 3.8) is the rule that converts a derivative taken in a moving frame into a derivative taken in a fixed one, and everything else in this topic (relative velocity, relative acceleration, inertia forces) follows from applying it.

---

## 🧭 1. Introduction: Observers and Reference Frames (Slide 3, Notes Ch. 3)

### 1.1 Different observers see different motions
When we drive a car or travel on an airplane, our reference frame moves with respect to the frame of an observer on the ground, and the velocities and accelerations that we measure differ from those measured on the ground (Notes Ch. 3, p. 36). For a particle $P$ observed from two frames $S_0$ and $S_1$ (Slide 3):
$$ \mathbf{r}_0^P \neq \mathbf{r}_1^P, \qquad \mathbf{v}_0^P \neq \mathbf{v}_1^P, \qquad \mathbf{a}_0^P \neq \mathbf{a}_1^P $$
The subscript names the observer (the reference frame in which the quantity is measured) and the superscript names the point.

### 1.2 Why we need relative motion
* An **observer** is the same thing as a **reference frame** (Slide 3).
* Quite often one of the two descriptions is easy to compute and the other is the one we need (Notes p. 36).
* Newton's laws apply only in **inertial** frames, and any accelerating or rotating frame is **non-inertial** (Notes p. 36). To use observations made in a moving frame we must either translate them to an inertial frame, or add *inertia (fictitious) forces*, as done in Section 10.

### 1.3 Absolute and relative quantities
Quantities measured with respect to a frame called "fixed" are named **absolute**; those measured with respect to a "moving" frame are **relative** (Notes p. 36). The naming is a convention: calling a frame "fixed" or "moving", and a quantity "absolute" or "relative", is completely arbitrary and subjective (Slide 23).

### 1.4 First step: the motion of the frames themselves
To understand relative motion we first need to describe how one reference frame moves with respect to another (Slide 3). A frame $S_1 = \{A; \mathcal{B}_1\}$ has two independent ingredients:
1. **Position and translational motion**: the motion of its origin $A$ (Section 2).
2. **Attitude and rotation**: the orientation of its vector basis $\mathcal{B}_1$ (Sections 3–4) and how it changes in time (Sections 5–7). *Attitude* means orientation.

---

## 📍 2. Position and Translational Motion of a Reference Frame (Slide 4)

Consider two reference frames $S_0 = \{O; \mathcal{B}_0\}$ and $S_1 = \{A; \mathcal{B}_1\}$. The **translational motion** of $S_1$ with respect to $S_0$ is the motion of the origin $A$ as seen from $S_0$:
$$ \mathbf{r}_0^A, \qquad \mathbf{v}_0^A = \left.\frac{d\mathbf{r}_0^A}{dt}\right|_0, \qquad \mathbf{a}_0^A = \left.\frac{d\mathbf{v}_0^A}{dt}\right|_0 $$
Alternatively, we can describe the motion of $O$ as seen from $S_1$, with $\mathbf{r}_1^O, \mathbf{v}_1^O, \mathbf{a}_1^O$. The positions are opposite vectors, because $\mathbf{r}_1^O = \mathbf{AO} = -\mathbf{OA}$:
$$ \mathbf{r}_1^O = -\mathbf{r}_0^A $$
but **in general** (Slide 4)
$$ \mathbf{v}_1^O \neq -\mathbf{v}_0^A, \qquad \mathbf{a}_1^O \neq -\mathbf{a}_0^A $$
**Why.** $\mathbf{v}_1^O$ is the derivative of $\mathbf{r}_1^O$ taken *in $S_1$*, while $\mathbf{v}_0^A$ is the derivative of $\mathbf{r}_0^A$ taken *in $S_0$*. If $\mathcal{B}_1$ rotates with respect to $\mathcal{B}_0$, the two derivatives of the same vector differ; the Coriolis theorem of Section 5 gives $\mathbf{v}_1^O = -\left.\frac{d\mathbf{r}_0^A}{dt}\right|_1 = -\left(\mathbf{v}_0^A - \boldsymbol{\omega}_{10}\times\mathbf{r}_0^A\right)$, which equals $-\mathbf{v}_0^A$ only when $\boldsymbol{\omega}_{10}\times\mathbf{r}_0^A = \mathbf{0}$ (for instance when $S_1$ does not rotate).

---

## 🧭 3. Attitude of a Reference Frame: the Change of Basis (Slides 5–7, Notes Sec. 1.5)

### 3.1 Definition of attitude
The **attitude** of $S_1$ with respect to $S_0$ is its instantaneous orientation in space. The position of the origin does not matter: only the directions of the vectors of the bases (Slide 5).

### 3.2 Change-of-basis relations
The simplest way to describe the attitude is to write the vectors of $\mathcal{B}_1$ in terms of the vectors of $\mathcal{B}_0$ (Slide 5, Notes Eq. 1.8):
$$ \begin{cases} \mathbf{i}_1 = \ell_{x1,x0}\,\mathbf{i}_0 + \ell_{x1,y0}\,\mathbf{j}_0 + \ell_{x1,z0}\,\mathbf{k}_0 \\ \mathbf{j}_1 = \ell_{y1,x0}\,\mathbf{i}_0 + \ell_{y1,y0}\,\mathbf{j}_0 + \ell_{y1,z0}\,\mathbf{k}_0 \\ \mathbf{k}_1 = \ell_{z1,x0}\,\mathbf{i}_0 + \ell_{z1,y0}\,\mathbf{j}_0 + \ell_{z1,z0}\,\mathbf{k}_0 \end{cases} $$
The coefficient $\ell_{x1,x0}$ is the component of $\mathbf{i}_1$ along $\mathbf{i}_0$; since both are unit vectors, $\ell_{x1,x0} = \mathbf{i}_1\cdot\mathbf{i}_0$ is the cosine of the angle between them (a *direction cosine*).

### 3.3 Components of a vector in either basis
Any vector $\mathbf{b}$ can be written in either basis; the vector itself is the same physical entity (Slide 5, Notes Eq. 1.6):
$$ \mathbf{b} = b_{x0}\mathbf{i}_0 + b_{y0}\mathbf{j}_0 + b_{z0}\mathbf{k}_0 = b_{x1}\mathbf{i}_1 + b_{y1}\mathbf{j}_1 + b_{z1}\mathbf{k}_1 $$
**Derivation of the transformation (Notes Eqs. 1.9–1.12).** Substitute the three change-of-basis relations into the second expression:
$$ \mathbf{b} = b_{x1}\left(\ell_{x1,x0}\mathbf{i}_0 + \ell_{x1,y0}\mathbf{j}_0 + \ell_{x1,z0}\mathbf{k}_0\right) + b_{y1}\left(\ell_{y1,x0}\mathbf{i}_0 + \ell_{y1,y0}\mathbf{j}_0 + \ell_{y1,z0}\mathbf{k}_0\right) + b_{z1}\left(\ell_{z1,x0}\mathbf{i}_0 + \ell_{z1,y0}\mathbf{j}_0 + \ell_{z1,z0}\mathbf{k}_0\right) $$
Collect the terms that multiply $\mathbf{i}_0$, $\mathbf{j}_0$ and $\mathbf{k}_0$ and compare with $b_{x0}\mathbf{i}_0 + b_{y0}\mathbf{j}_0 + b_{z0}\mathbf{k}_0$ (the components in a basis are unique):
$$ b_{x0} = \ell_{x1,x0}b_{x1} + \ell_{y1,x0}b_{y1} + \ell_{z1,x0}b_{z1}, \quad b_{y0} = \ell_{x1,y0}b_{x1} + \ell_{y1,y0}b_{y1} + \ell_{z1,y0}b_{z1}, \quad b_{z0} = \ell_{x1,z0}b_{x1} + \ell_{y1,z0}b_{y1} + \ell_{z1,z0}b_{z1} $$
In matrix form (Slide 5, Notes Eqs. 1.12–1.13):
$$ \begin{bmatrix} b_{x0} \\ b_{y0} \\ b_{z0} \end{bmatrix}_0 = [{}_0R_1]\cdot\begin{bmatrix} b_{x1} \\ b_{y1} \\ b_{z1} \end{bmatrix}_1, \qquad [{}_0R_1] = \begin{bmatrix} \ell_{x1,x0} & \ell_{y1,x0} & \ell_{z1,x0} \\ \ell_{x1,y0} & \ell_{y1,y0} & \ell_{z1,y0} \\ \ell_{x1,z0} & \ell_{y1,z0} & \ell_{z1,z0} \end{bmatrix} $$
$[{}_0R_1]$ is the **change-of-basis matrix from $\mathcal{B}_1$ to $\mathcal{B}_0$**: right-multiplied by the components in $\mathcal{B}_1$ it gives the components in $\mathcal{B}_0$. The subscript on each column matrix names its basis; without it the expressions would be ambiguous (Notes footnote 5).

> [!warning] Changing basis does not move the vector
> When the components of $\mathbf{b}$ are changed from one basis to another, the vector itself is not moved and not rotated: it is only described from a different basis, so the numbers that represent it change (Notes Sec. 1.5).

### 3.4 Properties of $[{}_0R_1]$ (Slide 6, Notes Eqs. 1.14–1.15)
For two right-handed orthonormal bases:
1. **$[{}_0R_1]$ is orthogonal**: the inverse transformation equals the transpose,
   $$ [{}_1R_0] = [{}_0R_1]^{-1} = [{}_0R_1]^T, \qquad [{}_0R_1]^T[{}_0R_1] = [U] $$
   Writing the inverse relations $\mathbf{i}_0 = \ell_{x0,x1}\mathbf{i}_1 + \ell_{x0,y1}\mathbf{j}_1 + \ell_{x0,z1}\mathbf{k}_1$, etc., this means $\ell_{x0,x1} = \ell_{x1,x0}$, $\ell_{x0,y1} = \ell_{y1,x0}$, and so on (Slide 6). This is consistent with $\ell_{x0,y1} = \mathbf{i}_0\cdot\mathbf{j}_1 = \mathbf{j}_1\cdot\mathbf{i}_0 = \ell_{y1,x0}$.
2. **Unit determinant**: $|[{}_0R_1]| = 1$ (Notes Eq. 1.15), because both bases are right-handed.
3. **The columns** of $[{}_0R_1]$ are the components of $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ in $\mathcal{B}_0$ (Slide 6). This is the practical way to write the matrix: column $n$ is the $n$-th vector of $\mathcal{B}_1$ written in $\mathcal{B}_0$.
4. **The rows** of $[{}_0R_1]$ are the components of $\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0$ in $\mathcal{B}_1$ (Slide 6).
5. **Eigenvalues**: $\lambda = 1,\ e^{i\beta},\ e^{-i\beta}$ (Slide 6).

### 3.5 Axis and angle of rotation (Slide 6, Notes Sec. 1.5.1)
A result due to Euler states that any two right-handed bases are related by a **single rotation**: there is always an axis (unit vector $\mathbf{e}$) and an angle such that rotating $\{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ about that axis by that angle makes them coincide with $\{\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$ (Notes Sec. 1.5.1). In terms of the matrix (Slide 6):
* the **axis of rotation** is the eigenspace associated with $\lambda = 1$; a vector on this axis has identical components in $\mathcal{B}_1$ and in $\mathcal{B}_0$ (indeed $[{}_0R_1]\mathbf{e} = 1\cdot\mathbf{e}$);
* the **rotation angle** about this axis is $\beta$, the argument of the two complex eigenvalues.

The same matrix can therefore be read in two ways (Notes Sec. 1.5.1): as the static relation between the components of a vector in $\mathcal{B}_1$ and $\mathcal{B}_0$, or as the rotation that, seen from $\mathcal{B}_0$, carries $\mathcal{B}_0$ onto $\mathcal{B}_1$. For this reason $[{}_0R_1]$ is called a **rotation matrix**.

### 3.6 Composition rules (Slide 7, Notes Eq. 1.16)
With three bases $\mathcal{B}_0, \mathcal{B}_1, \mathcal{B}_2$, the change-of-basis relations of $\mathcal{B}_1$ in $\mathcal{B}_0$ (matrix $[{}_0R_1]$) and of $\mathcal{B}_2$ in $\mathcal{B}_1$ (matrix $[{}_1R_2]$) can be composed. For example, substituting the expressions of $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ into $\mathbf{i}_2 = \ell_{x2,x1}\mathbf{i}_1 + \ell_{x2,y1}\mathbf{j}_1 + \ell_{x2,z1}\mathbf{k}_1$ gives $\mathbf{i}_2$ directly in $\mathcal{B}_0$ (Slide 7):
$$ \mathbf{i}_2 = \ell_{x2,x1}\left(\ell_{x1,x0}\mathbf{i}_0 + \ell_{x1,y0}\mathbf{j}_0 + \ell_{x1,z0}\mathbf{k}_0\right) + \ell_{x2,y1}\left(\ell_{y1,x0}\mathbf{i}_0 + \ell_{y1,y0}\mathbf{j}_0 + \ell_{y1,z0}\mathbf{k}_0\right) + \ell_{x2,z1}\left(\ell_{z1,x0}\mathbf{i}_0 + \ell_{z1,y0}\mathbf{j}_0 + \ell_{z1,z0}\mathbf{k}_0\right) $$
Equivalently, the matrices compose. From $[\mathbf{b}]_0 = [{}_0R_1][\mathbf{b}]_1$ and $[\mathbf{b}]_1 = [{}_1R_2][\mathbf{b}]_2$, substituting the second into the first:
$$ [\mathbf{b}]_0 = [{}_0R_1]\cdot[{}_1R_2]\cdot[\mathbf{b}]_2 \quad\Longrightarrow\quad [{}_0R_2] = [{}_0R_1]\cdot[{}_1R_2] $$
The product is in general **not commutative**: $[R_i][R_j] \neq [R_j][R_i]$ (Notes Sec. 1.5).

---

## 🔁 4. Simple Rotations and Euler Angles (Slides 8–13, Notes Secs. 1.5.2–1.5.3)

### 4.1 Simple rotations (Slide 8, Notes Eqs. 1.18–1.20)
A **simple rotation** is one whose axis of rotation is along one of the vectors of the basis. That vector is unchanged by the rotation (e.g. $\mathbf{i}_1 \equiv \mathbf{i}_0$), and the rest of space turns by an angle positive according to the right-hand rule (Notes Sec. 1.5.2).

**Rotation about $\mathbf{i}_0$ by $\theta_x$.** Looking down from $\mathbf{i}_0$ at the $Oyz$ plane:
$$ \begin{cases} \mathbf{i}_1 = \mathbf{i}_0 \\ \mathbf{j}_1 = \cos\theta_x\,\mathbf{j}_0 + \sin\theta_x\,\mathbf{k}_0 \\ \mathbf{k}_1 = -\sin\theta_x\,\mathbf{j}_0 + \cos\theta_x\,\mathbf{k}_0 \end{cases} \qquad [{}_0R_1(x,\theta_x)] = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\theta_x & -\sin\theta_x \\ 0 & \sin\theta_x & \cos\theta_x \end{bmatrix} $$
**Rotation about $\mathbf{j}_0$ by $\theta_y$.**
$$ \begin{cases} \mathbf{i}_1 = \cos\theta_y\,\mathbf{i}_0 - \sin\theta_y\,\mathbf{k}_0 \\ \mathbf{j}_1 = \mathbf{j}_0 \\ \mathbf{k}_1 = \sin\theta_y\,\mathbf{i}_0 + \cos\theta_y\,\mathbf{k}_0 \end{cases} \qquad [{}_0R_1(y,\theta_y)] = \begin{bmatrix} \cos\theta_y & 0 & \sin\theta_y \\ 0 & 1 & 0 \\ -\sin\theta_y & 0 & \cos\theta_y \end{bmatrix} $$
**Rotation about $\mathbf{k}_0$ by $\theta_z$.**
$$ \begin{cases} \mathbf{i}_1 = \cos\theta_z\,\mathbf{i}_0 + \sin\theta_z\,\mathbf{j}_0 \\ \mathbf{j}_1 = -\sin\theta_z\,\mathbf{i}_0 + \cos\theta_z\,\mathbf{j}_0 \\ \mathbf{k}_1 = \mathbf{k}_0 \end{cases} \qquad [{}_0R_1(z,\theta_z)] = \begin{bmatrix} \cos\theta_z & -\sin\theta_z & 0 \\ \sin\theta_z & \cos\theta_z & 0 \\ 0 & 0 & 1 \end{bmatrix} $$
In each matrix the columns are the relations on the left, as stated in Section 3.4. **Check** (for $z$): $\det = \cos^2\theta_z + \sin^2\theta_z = 1$, and the columns are orthonormal: $(\cos\theta_z)(-\sin\theta_z) + (\sin\theta_z)(\cos\theta_z) + 0 = 0$.

The inverse matrices are the same with the opposite angle ($\theta \to -\theta$): only the position of the minus sign in front of the sines changes. To avoid sign errors, always draw the rotation looking down from the stationary axis (Notes Sec. 1.5.2). The $y$ case looks different from the other two only because, seen from $\mathbf{j}_0$, the plane is $Ozx$ (in that cyclic order), so the minus sign appears in the $\mathbf{i}_1$ row.

### 4.2 Euler angles (Slide 9, Notes Sec. 1.5.3)
Any attitude can be represented as the composition of **three simple rotations about different axes**. To relate $\mathcal{B}_0$ to $\mathcal{B}_3$ we introduce the auxiliary bases $\mathcal{B}_1$ and $\mathcal{B}_2$ (Slide 9):
1. $\mathcal{B}_0 \to \mathcal{B}_1$: rotation $\psi$ about $\mathbf{k}_0 \equiv \mathbf{k}_1$;
2. $\mathcal{B}_1 \to \mathcal{B}_2$: rotation $\theta$ about $\mathbf{i}_1 \equiv \mathbf{i}_2$;
3. $\mathcal{B}_2 \to \mathcal{B}_3$: rotation $\varphi$ about $\mathbf{k}_2 \equiv \mathbf{k}_3$.

By the composition rule (Section 3.6, Notes Eq. 1.16):
$$ [{}_0R_3] = [{}_0R_1]\cdot[{}_1R_2]\cdot[{}_2R_3] $$
The angles $\psi$ (**precession**), $\theta$ (**nutation**) and $\varphi$ (**spin**) are the **standard Euler angles**, also called **3-1-3 Euler angles** after the order of the rotation axes: third axis, then first axis, then third again. There are many other choices; a common one is **3-2-1 (yaw, pitch, roll)**. The only rule is that the same axis cannot be repeated in two consecutive rotations (Slide 9). The Notes also show the 1-2-3 sequence (Notes Eq. 1.23).

### 4.3 Example: 3-2-1 attitude of the Space Shuttle (Slides 10–13)
We describe the attitude of the red frame $S_r$ (attached to the shuttle) with respect to the blue frame $S_b$ with 3-2-1 Euler angles, the convention of flight mechanics. Both frames start coincident (Slide 10).
1. **First rotation**, angle $\psi$ about $\mathbf{k}_b \equiv \mathbf{k}_1$ (Slide 11):
   $$ \mathbf{i}_1 = \cos\psi\,\mathbf{i}_b + \sin\psi\,\mathbf{j}_b, \qquad \mathbf{j}_1 = -\sin\psi\,\mathbf{i}_b + \cos\psi\,\mathbf{j}_b, \qquad \mathbf{k}_1 = \mathbf{k}_b $$
2. **Second rotation**, angle $\theta$ about $\mathbf{j}_1 \equiv \mathbf{j}_2$ (Slide 12):
   $$ \mathbf{i}_2 = \cos\theta\,\mathbf{i}_1 - \sin\theta\,\mathbf{k}_1, \qquad \mathbf{j}_2 = \mathbf{j}_1, \qquad \mathbf{k}_2 = \sin\theta\,\mathbf{i}_1 + \cos\theta\,\mathbf{k}_1 $$
3. **Third rotation**, angle $\varphi$ about $\mathbf{i}_2 \equiv \mathbf{i}_r$ (Slide 13):
   $$ \mathbf{i}_r = \mathbf{i}_2, \qquad \mathbf{j}_r = \cos\varphi\,\mathbf{j}_2 + \sin\varphi\,\mathbf{k}_2, \qquad \mathbf{k}_r = -\sin\varphi\,\mathbf{j}_2 + \cos\varphi\,\mathbf{k}_2 $$
Writing each step as a matrix (columns = the relations above) and composing, $[{}_bR_r] = [{}_bR_1(z,\psi)]\cdot[{}_1R_2(y,\theta)]\cdot[{}_2R_r(x,\varphi)]$:
$$ [{}_bR_r] = \begin{bmatrix} \cos\psi\cos\theta & \cos\psi\sin\theta\sin\varphi - \sin\psi\cos\varphi & \cos\psi\sin\theta\cos\varphi + \sin\psi\sin\varphi \\ \sin\psi\cos\theta & \sin\psi\sin\theta\sin\varphi + \cos\psi\cos\varphi & \sin\psi\sin\theta\cos\varphi - \cos\psi\sin\varphi \\ -\sin\theta & \cos\theta\sin\varphi & \cos\theta\cos\varphi \end{bmatrix} $$
**How the first column is obtained** (the others follow the same way): $\mathbf{i}_r = \mathbf{i}_2 = \cos\theta\,\mathbf{i}_1 - \sin\theta\,\mathbf{k}_1 = \cos\theta(\cos\psi\,\mathbf{i}_b + \sin\psi\,\mathbf{j}_b) - \sin\theta\,\mathbf{k}_b$, so its components in $\mathcal{B}_b$ are $(\cos\psi\cos\theta,\ \sin\psi\cos\theta,\ -\sin\theta)$. Check: the squared norm is $\cos^2\theta(\cos^2\psi + \sin^2\psi) + \sin^2\theta = 1$.

---

## 🌀 5. Angular Motion of a Reference Frame (Slides 14–16, Notes Secs. 1.7 and 3.1)

### 5.1 Angular velocity vector (Slide 14)
So far the change of basis was stationary. But bases can rotate with respect to each other as a function of time. The rotation of $\mathcal{B}_1$ with respect to $\mathcal{B}_0$ is represented at each instant by the **angular velocity vector** $\boldsymbol{\omega}_{10}$ (Slide 14):
* its **direction** is the direction of the instantaneous axis of rotation of $\mathcal{B}_1$ (right-hand rule);
* its **magnitude** is the angular rate.

The angular velocity and the motion of the origin of $S_1$ are unrelated: they are two completely different things (Slide 14).

**Where $\boldsymbol{\omega}$ comes from (Notes Sec. 1.7.1).** A vector $\mathbf{A}$ of constant magnitude that rotates about an axis $\mathbf{e}_\omega$ at rate $\dot\theta$ keeps its component along $\mathbf{e}_\omega$, while its perpendicular part describes a circle; in a time $dt$ it changes by $|d\mathbf{A}| = A_\perp\,d\theta = \dot\theta\,|\mathbf{e}_\omega\times\mathbf{A}|\,dt$, in the direction of $\mathbf{e}_\omega\times\mathbf{A}$. Hence (Notes Eq. 1.62)
$$ \frac{d\mathbf{A}}{dt} = \dot\theta\,\mathbf{e}_\omega\times\mathbf{A} = \boldsymbol{\omega}\times\mathbf{A}, \qquad \boldsymbol{\omega} = \dot\theta\,\mathbf{e}_\omega $$
For infinitesimal rotations about the three axes, $\boldsymbol{\omega} = \frac{d\theta_x}{dt}\mathbf{i} + \frac{d\theta_y}{dt}\mathbf{j} + \frac{d\theta_z}{dt}\mathbf{k}$ (Notes Eq. 1.73).

### 5.2 Derivative of the basis vectors of $\mathcal{B}_1$ seen from $S_0$
The vectors of $\mathcal{B}_1$ are unit vectors: they change only in direction. Applying the previous result to each of them (Slide 14, Notes Eqs. 3.3–3.5):
$$ \left.\frac{d\mathbf{i}_1}{dt}\right|_0 = \boldsymbol{\omega}_{10}\times\mathbf{i}_1, \qquad \left.\frac{d\mathbf{j}_1}{dt}\right|_0 = \boldsymbol{\omega}_{10}\times\mathbf{j}_1, \qquad \left.\frac{d\mathbf{k}_1}{dt}\right|_0 = \boldsymbol{\omega}_{10}\times\mathbf{k}_1 $$

### 5.3 Derivative of a vector that is constant in $S_1$ (Slide 14)
Let $\mathbf{c} = c_{x1}\mathbf{i}_1 + c_{y1}\mathbf{j}_1 + c_{z1}\mathbf{k}_1$ with constant components (a vector "attached" to $S_1$). Seen from $S_0$, by the product rule each term gives $\dot c_{x1}\mathbf{i}_1 + c_{x1}\,d\mathbf{i}_1/dt|_0$ with $\dot c_{x1} = 0$:
$$ \left.\frac{d\mathbf{c}}{dt}\right|_0 = c_{x1}\left.\frac{d\mathbf{i}_1}{dt}\right|_0 + c_{y1}\left.\frac{d\mathbf{j}_1}{dt}\right|_0 + c_{z1}\left.\frac{d\mathbf{k}_1}{dt}\right|_0 = c_{x1}\,\boldsymbol{\omega}_{10}\times\mathbf{i}_1 + c_{y1}\,\boldsymbol{\omega}_{10}\times\mathbf{j}_1 + c_{z1}\,\boldsymbol{\omega}_{10}\times\mathbf{k}_1 $$
Since a scalar factor can be moved inside the cross product and the cross product is distributive:
$$ \left.\frac{d\mathbf{c}}{dt}\right|_0 = \boldsymbol{\omega}_{10}\times\left(c_{x1}\mathbf{i}_1 + c_{y1}\mathbf{j}_1 + c_{z1}\mathbf{k}_1\right) = \boldsymbol{\omega}_{10}\times\mathbf{c} $$

### 5.4 Angular acceleration vector (Slide 15, Notes Eq. 3.9)
The rotation can also be accelerated. The **angular acceleration vector** is
$$ \boldsymbol{\alpha}_{10} = \left.\frac{d\boldsymbol{\omega}_{10}}{dt}\right|_0 $$
* Its direction may differ from the direction of $\boldsymbol{\omega}_{10}$ (Slide 15).
* $\boldsymbol{\omega}_{10}$ does not describe the current attitude of $S_1$, only how the attitude is changing in time.
* The component of $\boldsymbol{\alpha}_{10}$ **parallel** to $\boldsymbol{\omega}_{10}$ describes how the **magnitude** of $\boldsymbol{\omega}_{10}$ changes; the **perpendicular** component describes how its **direction** changes. (With $\boldsymbol{\omega}_{10} = \omega_{10}\mathbf{e}_\omega$, the product rule gives $\boldsymbol{\alpha}_{10} = \dot\omega_{10}\,\mathbf{e}_\omega + \omega_{10}\,d\mathbf{e}_\omega/dt|_0$; the first term is parallel and the second is perpendicular to $\mathbf{e}_\omega$ because $\mathbf{e}_\omega$ is a unit vector, Notes Eq. 1.53.)

### 5.5 Example: simple rotation about $\mathbf{k}_0$ (Slide 16)
At $t = 0$ the frames $S_1$ and $S_0$ coincide; thereafter $S_1$ performs a simple rotation about $\mathbf{k}_0$ with angle $\psi = \psi(t)$:
$$ \mathbf{i}_1 = \cos\psi\,\mathbf{i}_0 + \sin\psi\,\mathbf{j}_0, \qquad \mathbf{j}_1 = -\sin\psi\,\mathbf{i}_0 + \cos\psi\,\mathbf{j}_0, \qquad \mathbf{k}_1 = \mathbf{k}_0 $$
**Direct differentiation in $S_0$** ($\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0$ are constant there). By the chain rule, $\frac{d}{dt}\cos\psi(t) = -\sin\psi\,\dot\psi$ and $\frac{d}{dt}\sin\psi(t) = \cos\psi\,\dot\psi$:
$$ \left.\frac{d\mathbf{i}_1}{dt}\right|_0 = \dot\psi\left(-\sin\psi\,\mathbf{i}_0 + \cos\psi\,\mathbf{j}_0\right) = \dot\psi\,\mathbf{j}_1, \qquad \left.\frac{d\mathbf{j}_1}{dt}\right|_0 = \dot\psi\left(-\cos\psi\,\mathbf{i}_0 - \sin\psi\,\mathbf{j}_0\right) = -\dot\psi\,\mathbf{i}_1, \qquad \left.\frac{d\mathbf{k}_1}{dt}\right|_0 = \mathbf{0} $$
**Identification of $\boldsymbol{\omega}_{10}$.** Try $\boldsymbol{\omega}_{10} = \dot\psi\,\mathbf{k}_0 = \dot\psi\,\mathbf{k}_1$: then $\boldsymbol{\omega}_{10}\times\mathbf{i}_1 = \dot\psi\,\mathbf{k}_1\times\mathbf{i}_1 = \dot\psi\,\mathbf{j}_1$, $\boldsymbol{\omega}_{10}\times\mathbf{j}_1 = \dot\psi\,\mathbf{k}_1\times\mathbf{j}_1 = -\dot\psi\,\mathbf{i}_1$ and $\boldsymbol{\omega}_{10}\times\mathbf{k}_1 = \mathbf{0}$, which reproduce the three derivatives. Therefore
$$ \boldsymbol{\omega}_{10} = \dot\psi\,\mathbf{k}_0, \qquad \boldsymbol{\alpha}_{10} = \left.\frac{d(\dot\psi\,\mathbf{k}_0)}{dt}\right|_0 = \ddot\psi\,\mathbf{k}_0 $$
Here $\boldsymbol{\alpha}_{10}\parallel\boldsymbol{\omega}_{10}$: only the magnitude of the angular velocity changes.

---

## ⚙️ 6. The Coriolis Theorem (Slides 17–18, Notes Sec. 3.1)

### 6.1 Statement of the problem
Consider a vector $\mathbf{b} = b_{x1}(t)\,\mathbf{i}_1 + b_{y1}(t)\,\mathbf{j}_1 + b_{z1}(t)\,\mathbf{k}_1$ that is **not constant** in $S_1$ (Slide 17; the Notes use $\mathbf{A}$, Eq. 3.1). We want its time derivative as seen from $S_0$, knowing its components in $\mathcal{B}_1$.

### 6.2 Derivation (Notes Eqs. 3.2–3.8)
**Derivative in $S_1$.** In $S_1$ the vectors $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ are constant, so only the components change (Notes Eq. 3.7):
$$ \left.\frac{d\mathbf{b}}{dt}\right|_1 = \frac{db_{x1}}{dt}\mathbf{i}_1 + \frac{db_{y1}}{dt}\mathbf{j}_1 + \frac{db_{z1}}{dt}\mathbf{k}_1 $$
**Derivative in $S_0$.** In $S_0$ the vectors of $\mathcal{B}_1$ are *not* constant, so the product rule must be applied to each term, $\frac{d}{dt}\left(b_{x1}\mathbf{i}_1\right) = \dot b_{x1}\,\mathbf{i}_1 + b_{x1}\,\frac{d\mathbf{i}_1}{dt}\big|_0$ (Notes Eq. 3.2):
$$ \left.\frac{d\mathbf{b}}{dt}\right|_0 = \underbrace{\frac{db_{x1}}{dt}\mathbf{i}_1 + \frac{db_{y1}}{dt}\mathbf{j}_1 + \frac{db_{z1}}{dt}\mathbf{k}_1}_{= \left.d\mathbf{b}/dt\right|_1} + \underbrace{b_{x1}\left.\frac{d\mathbf{i}_1}{dt}\right|_0 + b_{y1}\left.\frac{d\mathbf{j}_1}{dt}\right|_0 + b_{z1}\left.\frac{d\mathbf{k}_1}{dt}\right|_0}_{= \boldsymbol{\omega}_{10}\times\mathbf{b}} $$
The second group is exactly the computation of Section 5.3 with $c \to b$ (Notes Eq. 3.6): $b_{x1}\,\boldsymbol{\omega}_{10}\times\mathbf{i}_1 + b_{y1}\,\boldsymbol{\omega}_{10}\times\mathbf{j}_1 + b_{z1}\,\boldsymbol{\omega}_{10}\times\mathbf{k}_1 = \boldsymbol{\omega}_{10}\times\mathbf{b}$. Therefore:
$$ \boxed{\left.\frac{d\mathbf{b}}{dt}\right|_0 = \left.\frac{d\mathbf{b}}{dt}\right|_1 + \boldsymbol{\omega}_{10}\times\mathbf{b}} \qquad \text{(Coriolis theorem)} $$
This is Notes Eq. 3.8 (Slide 17).

### 6.3 Meaning and remarks
* The derivative of $\mathbf{b}$ in $S_0$ equals the derivative of $\mathbf{b}$ in $S_1$ plus the rotation of $\mathbf{b}$ due to the angular motion of $S_1$ with respect to $S_0$ (Slide 17).
* When differentiating vectors, the reference frame **matters**, so the frame of every derivative must be written explicitly. Derivatives of **scalars** are the same in every frame (Notes p. 37).
* The theorem was derived for a frame that only rotates, but it holds unchanged when $S_1$ also translates, because a translation does not change the orientation of $\{\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$ (Notes p. 37).
* **Remember**: a vector can be *defined* in one reference frame, be *differentiated* in another and be *expressed* in yet another basis (Slide 17).

### 6.4 Consequence: $\boldsymbol{\alpha}_{10}$ is the same seen from $S_0$ and $S_1$ (Notes Eq. 3.9)
Apply the theorem to $\mathbf{b} = \boldsymbol{\omega}_{10}$:
$$ \boldsymbol{\alpha}_{10} \equiv \left.\frac{d\boldsymbol{\omega}_{10}}{dt}\right|_0 = \left.\frac{d\boldsymbol{\omega}_{10}}{dt}\right|_1 + \underbrace{\boldsymbol{\omega}_{10}\times\boldsymbol{\omega}_{10}}_{=\ \mathbf{0}} = \left.\frac{d\boldsymbol{\omega}_{10}}{dt}\right|_1 $$
because the cross product of a vector with itself vanishes. The angular acceleration vector may in general not be parallel to $\boldsymbol{\omega}_{10}$.

### 6.5 Example (Slide 18)
Consider $\mathbf{b} = t\,\mathbf{i}_1 + t^2\,\mathbf{j}_1 + t^3\,\mathbf{k}_1$, with $S_1$ rotating about $\mathbf{k}_0 \equiv \mathbf{k}_1$ by the angle $\psi(t)$ as in Section 5.5 (so $\boldsymbol{\omega}_{10} = \dot\psi\,\mathbf{k}_1$). Compute its derivative in $S_1$ and in $S_0$.

**In $S_1$:** only the components change; $\frac{d}{dt}t = 1$, $\frac{d}{dt}t^2 = 2t$, $\frac{d}{dt}t^3 = 3t^2$:
$$ \left.\frac{d\mathbf{b}}{dt}\right|_1 = \mathbf{i}_1 + 2t\,\mathbf{j}_1 + 3t^2\,\mathbf{k}_1 $$
**Rotation term.** Using $\mathbf{k}_1\times\mathbf{i}_1 = \mathbf{j}_1$, $\mathbf{k}_1\times\mathbf{j}_1 = -\mathbf{i}_1$, $\mathbf{k}_1\times\mathbf{k}_1 = \mathbf{0}$:
$$ \boldsymbol{\omega}_{10}\times\mathbf{b} = \dot\psi\,\mathbf{k}_1\times\left(t\,\mathbf{i}_1 + t^2\,\mathbf{j}_1 + t^3\,\mathbf{k}_1\right) = \dot\psi\,t\,\mathbf{j}_1 - \dot\psi\,t^2\,\mathbf{i}_1 $$
**In $S_0$ (Coriolis theorem):**
$$ \left.\frac{d\mathbf{b}}{dt}\right|_0 = \left(1 - \dot\psi\,t^2\right)\mathbf{i}_1 + \left(2t + \dot\psi\,t\right)\mathbf{j}_1 + 3t^2\,\mathbf{k}_1 $$
Note that this derivative *taken in $S_0$* is *expressed in $\mathcal{B}_1$*. **Cross-check** by brute force: writing $\mathbf{b}$ in $\mathcal{B}_0$ with the relations of Section 5.5 and differentiating component by component gives the same vector (verified symbolically). Homogeneity: in each component the rotation term has the same units as the $S_1$ derivative, because $\dot\psi$ (in $\text{s}^{-1}$) multiplies a component of $\mathbf{b}$, exactly as $d/dt$ divides it by time; for instance in $\mathbf{i}_1$, $\dot\psi\,t^2$ and $\frac{d}{dt}(t) = 1$ are both "component of $\mathbf{b}$ per second".

---

## ➕ 7. Composition of Angular Motions (Slide 19, Notes Eqs. 3.10–3.15)

### 7.1 Angular velocities add
If $S_2$ rotates with respect to $S_1$ with $\boldsymbol{\omega}_{21}$, and $S_1$ rotates with respect to $S_0$ with $\boldsymbol{\omega}_{10}$, the rotation of $S_2$ with respect to $S_0$ is (Slide 19, Notes Eq. 3.10)
$$ \boldsymbol{\omega}_{20} = \boldsymbol{\omega}_{21} + \boldsymbol{\omega}_{10} $$
**Why.** For any vector $\mathbf{c}$ constant in $S_2$, apply Coriolis twice: $\left.\frac{d\mathbf{c}}{dt}\right|_1 = \boldsymbol{\omega}_{21}\times\mathbf{c}$ and $\left.\frac{d\mathbf{c}}{dt}\right|_0 = \left.\frac{d\mathbf{c}}{dt}\right|_1 + \boldsymbol{\omega}_{10}\times\mathbf{c} = (\boldsymbol{\omega}_{21} + \boldsymbol{\omega}_{10})\times\mathbf{c}$. Comparing with the definition $\left.\frac{d\mathbf{c}}{dt}\right|_0 = \boldsymbol{\omega}_{20}\times\mathbf{c}$ for every $\mathbf{c}$ gives the rule.

### 7.2 Angular accelerations do not simply add
Differentiate $\boldsymbol{\omega}_{20} = \boldsymbol{\omega}_{21} + \boldsymbol{\omega}_{10}$ in $S_0$ (Slide 19, Notes Eq. 3.11):
$$ \left.\frac{d\boldsymbol{\omega}_{20}}{dt}\right|_0 = \left.\frac{d\boldsymbol{\omega}_{21}}{dt}\right|_0 + \left.\frac{d\boldsymbol{\omega}_{10}}{dt}\right|_0 $$
The last term is $\boldsymbol{\alpha}_{10}$. The first one is the derivative in $S_0$ of a vector naturally defined in $S_1$; by the Coriolis theorem, $\left.\frac{d\boldsymbol{\omega}_{21}}{dt}\right|_0 = \left.\frac{d\boldsymbol{\omega}_{21}}{dt}\right|_1 + \boldsymbol{\omega}_{10}\times\boldsymbol{\omega}_{21} = \boldsymbol{\alpha}_{21} + \boldsymbol{\omega}_{10}\times\boldsymbol{\omega}_{21}$. Hence (Notes Eq. 3.12)
$$ \boldsymbol{\alpha}_{20} = \boldsymbol{\alpha}_{21} + \boldsymbol{\omega}_{10}\times\boldsymbol{\omega}_{21} + \boldsymbol{\alpha}_{10} $$
The extra term $\boldsymbol{\omega}_{10}\times\boldsymbol{\omega}_{21}$ appears because $\boldsymbol{\omega}_{21}$ is carried around by the rotation of $S_1$, so its direction changes in $S_0$ even if it is constant in $S_1$.

### 7.3 Inverse motion
The rotation of $S_0$ with respect to $S_1$ satisfies (Slide 19, Notes Eq. 3.13)
$$ \boldsymbol{\omega}_{01} = -\boldsymbol{\omega}_{10}, \qquad \boldsymbol{\alpha}_{01} = -\boldsymbol{\alpha}_{10} $$
(The first follows from Section 7.1 with $S_2 = S_0$: $\boldsymbol{\omega}_{00} = \mathbf{0} = \boldsymbol{\omega}_{01} + \boldsymbol{\omega}_{10}$; the second by differentiating, since $\boldsymbol{\alpha}$ is the same in both frames, Section 6.4.) In general $\boldsymbol{\omega}_{lm}$ is the angular velocity of frame $l$ as seen from frame $m$. When the composition formulas are used in components, **every vector must first be expressed in the same basis** (Notes p. 38).

---

## 🎯 8. Angular Velocity from Simple Rotations (Slides 20–21)

### 8.1 3-1-3 Euler angles as functions of time
Consider the three sequential simple rotations of the 3-1-3 Euler angles, $\psi(t), \theta(t), \varphi(t)$: $S_0 \to S_1 \to S_2 \to S_3$ (Slide 20). Each simple rotation is a rotation about a fixed axis of the two bases it connects, so by Section 5.5 its angular velocity is the rate of its angle times its axis (Slide 20):
$$ \boldsymbol{\omega}_{10} = \dot\psi\,\mathbf{k}_0 \equiv \dot\psi\,\mathbf{k}_1, \qquad \boldsymbol{\omega}_{21} = \dot\theta\,\mathbf{i}_1 \equiv \dot\theta\,\mathbf{i}_2, \qquad \boldsymbol{\omega}_{32} = \dot\varphi\,\mathbf{k}_2 \equiv \dot\varphi\,\mathbf{k}_3 $$
By the composition rule (Section 7.1) applied twice:
$$ \boldsymbol{\omega}_{30} = \boldsymbol{\omega}_{32} + \boldsymbol{\omega}_{21} + \boldsymbol{\omega}_{10} = \dot\varphi\,\mathbf{k}_2 + \dot\theta\,\mathbf{i}_1 + \dot\psi\,\mathbf{k}_0 $$
This vector is mixed: each term is written in a different basis. Again: a vector can be defined in one frame, differentiated in another and expressed in a different basis, or in general as a linear combination of other vectors (Slide 20).

### 8.2 Expressed in $\mathcal{B}_0$ (Slide 21)
The rotations are: $\mathbf{i}_1 = \cos\psi\,\mathbf{i}_0 + \sin\psi\,\mathbf{j}_0$, $\mathbf{j}_1 = -\sin\psi\,\mathbf{i}_0 + \cos\psi\,\mathbf{j}_0$, $\mathbf{k}_1 = \mathbf{k}_0$ (about $\mathbf{k}_0$), then $\mathbf{j}_2 = \cos\theta\,\mathbf{j}_1 + \sin\theta\,\mathbf{k}_1$, $\mathbf{k}_2 = -\sin\theta\,\mathbf{j}_1 + \cos\theta\,\mathbf{k}_1$ (about $\mathbf{i}_1$). So
$$ \mathbf{k}_2 = -\sin\theta\left(-\sin\psi\,\mathbf{i}_0 + \cos\psi\,\mathbf{j}_0\right) + \cos\theta\,\mathbf{k}_0 = \sin\theta\sin\psi\,\mathbf{i}_0 - \sin\theta\cos\psi\,\mathbf{j}_0 + \cos\theta\,\mathbf{k}_0 $$
Substituting $\mathbf{k}_2$ and $\mathbf{i}_1$ in $\boldsymbol{\omega}_{30}$ and collecting terms:
$$ \boldsymbol{\omega}_{30} = \left(\dot\theta\cos\psi + \dot\varphi\sin\psi\sin\theta\right)\mathbf{i}_0 + \left(\dot\theta\sin\psi - \dot\varphi\cos\psi\sin\theta\right)\mathbf{j}_0 + \left(\dot\varphi\cos\theta + \dot\psi\right)\mathbf{k}_0 $$

### 8.3 Expressed in $\mathcal{B}_3$ (Slide 21)
The last rotation (about $\mathbf{k}_2$) is $\mathbf{i}_3 = \cos\varphi\,\mathbf{i}_2 + \sin\varphi\,\mathbf{j}_2$, $\mathbf{j}_3 = -\sin\varphi\,\mathbf{i}_2 + \cos\varphi\,\mathbf{j}_2$, $\mathbf{k}_3 = \mathbf{k}_2$. Its inverse (transpose) gives $\mathbf{i}_2 = \cos\varphi\,\mathbf{i}_3 - \sin\varphi\,\mathbf{j}_3$ and $\mathbf{j}_2 = \sin\varphi\,\mathbf{i}_3 + \cos\varphi\,\mathbf{j}_3$. Inverting the second rotation, $\mathbf{k}_1 = \sin\theta\,\mathbf{j}_2 + \cos\theta\,\mathbf{k}_2$. Then
$$ \mathbf{i}_1 = \mathbf{i}_2 = \cos\varphi\,\mathbf{i}_3 - \sin\varphi\,\mathbf{j}_3, \qquad \mathbf{k}_0 = \mathbf{k}_1 = \sin\theta\sin\varphi\,\mathbf{i}_3 + \sin\theta\cos\varphi\,\mathbf{j}_3 + \cos\theta\,\mathbf{k}_3 $$
and, with $\mathbf{k}_2 = \mathbf{k}_3$:
$$ \boldsymbol{\omega}_{30} = \left(\dot\theta\cos\varphi + \dot\psi\sin\varphi\sin\theta\right)\mathbf{i}_3 + \left(-\dot\theta\sin\varphi + \dot\psi\cos\varphi\sin\theta\right)\mathbf{j}_3 + \left(\dot\varphi + \dot\psi\cos\theta\right)\mathbf{k}_3 $$

### 8.4 Exercise of Slide 21: 3-2-1 (yaw-pitch-roll) angles
With the rotations of Section 4.3 ($\psi$ about $\mathbf{k}_b$, $\theta$ about $\mathbf{j}_1$, $\varphi$ about $\mathbf{i}_2$), the same reasoning gives
$$ \boldsymbol{\omega}_{rb} = \dot\psi\,\mathbf{k}_b + \dot\theta\,\mathbf{j}_1 + \dot\varphi\,\mathbf{i}_2 $$
**In $\mathcal{B}_b$:** with $\mathbf{j}_1 = -\sin\psi\,\mathbf{i}_b + \cos\psi\,\mathbf{j}_b$ and $\mathbf{i}_2 = \cos\theta\cos\psi\,\mathbf{i}_b + \cos\theta\sin\psi\,\mathbf{j}_b - \sin\theta\,\mathbf{k}_b$:
$$ \boldsymbol{\omega}_{rb} = \left(\dot\varphi\cos\theta\cos\psi - \dot\theta\sin\psi\right)\mathbf{i}_b + \left(\dot\varphi\cos\theta\sin\psi + \dot\theta\cos\psi\right)\mathbf{j}_b + \left(\dot\psi - \dot\varphi\sin\theta\right)\mathbf{k}_b $$
**In $\mathcal{B}_r$:** inverting the third rotation, $\mathbf{j}_2 = \cos\varphi\,\mathbf{j}_r - \sin\varphi\,\mathbf{k}_r$ and $\mathbf{k}_2 = \sin\varphi\,\mathbf{j}_r + \cos\varphi\,\mathbf{k}_r$; inverting the second, $\mathbf{k}_1 = -\sin\theta\,\mathbf{i}_2 + \cos\theta\,\mathbf{k}_2$. Hence $\mathbf{j}_1 = \mathbf{j}_2 = \cos\varphi\,\mathbf{j}_r - \sin\varphi\,\mathbf{k}_r$ and $\mathbf{k}_b = \mathbf{k}_1 = -\sin\theta\,\mathbf{i}_r + \cos\theta\sin\varphi\,\mathbf{j}_r + \cos\theta\cos\varphi\,\mathbf{k}_r$, so
$$ \boldsymbol{\omega}_{rb} = \left(\dot\varphi - \dot\psi\sin\theta\right)\mathbf{i}_r + \left(\dot\theta\cos\varphi + \dot\psi\cos\theta\sin\varphi\right)\mathbf{j}_r + \left(\dot\psi\cos\theta\cos\varphi - \dot\theta\sin\varphi\right)\mathbf{k}_r $$
Both results were checked symbolically against the matrix definition $[\Omega] = \dot{[R]}\,[R]^T$ of Notes Sec. 1.7.2.

---

## 🛰️ 9. Configuration and Motion of a Reference Frame (Slide 22, Notes Sec. 3.2)

The configuration and motion of $S_1 = \{A; \mathcal{B}_1\}$ with respect to $S_0$ are completely specified if we provide (Slide 22):
1. the **position of its origin** as a function of time, $\mathbf{r}_0^A(t)$;
2. the **attitude of its basis** as a function of time, $\mathbf{i}_1(t), \mathbf{j}_1(t), \mathbf{k}_1(t)$, for instance through Euler angles $\psi(t), \theta(t), \varphi(t)$ (equivalently the rotation matrix $[{}_0R_1]$).

From this information we can compute:
* the velocity and acceleration of the origin, $\mathbf{v}_0^A(t)$ and $\mathbf{a}_0^A(t)$;
* the angular velocity and angular acceleration of the basis, $\boldsymbol{\omega}_{10}(t)$ and $\boldsymbol{\alpha}_{10}(t)$.

The expressions of relative motion are particularly useful when the motion of $S_1$ is **known a priori**: then none of these functions of time are unknowns of the problem (Slide 22, Notes Sec. 3.2).

---

## 🚀 10. Relative Kinematics of the Point Particle (Slides 23–26, Notes Sec. 3.2)

### 10.1 Motivation (Slide 23)
* Often we have more than one observer and need to relate the position, velocity and acceleration of $P$ that each sees. Example: sensors on an experimental aircraft measure a hurricane; the motion of the aircraft must be taken into account to "translate" the measurements to a ground-based frame.
* In other cases it is simpler to obtain these vectors in a moving frame than in the fixed one.

### 10.2 Position (Slide 23, Notes Eq. 3.16)
Point $P$ is observed from the fixed frame $S_0 = \{O; \mathcal{B}_0\}$ and from the moving frame $S_1 = \{A; \mathcal{B}_1\}$. The vector sum $\mathbf{OP} = \mathbf{OA} + \mathbf{AP}$ gives
$$ \mathbf{r}_0^P = \mathbf{r}_0^A + \mathbf{r}_1^P $$
The **absolute position** $\mathbf{r}_0^P$ (in $S_0$) equals the position of the origin of $S_1$, $\mathbf{r}_0^A$, plus the **relative position** $\mathbf{r}_1^P$ (in $S_1$).

### 10.3 Velocity (Slide 24, Notes Eqs. 3.17–3.20)
**Step 1: differentiate the position in $S_0$.** By definition the absolute velocity is the derivative of $\mathbf{r}_0^P$ in $S_0$; the derivative of a sum is the sum of the derivatives:
$$ \mathbf{v}_0^P \equiv \left.\frac{d\mathbf{r}_0^P}{dt}\right|_0 = \left.\frac{d\mathbf{r}_0^A}{dt}\right|_0 + \left.\frac{d\mathbf{r}_1^P}{dt}\right|_0 $$
**Step 2: identify the first term.** $\left.\frac{d\mathbf{r}_0^A}{dt}\right|_0 = \mathbf{v}_0^A$, the velocity of the origin.
**Step 3: Coriolis theorem on the second term.** $\mathbf{r}_1^P$ is naturally described in $S_1$, so (Notes Eq. 3.18)
$$ \left.\frac{d\mathbf{r}_1^P}{dt}\right|_0 = \left.\frac{d\mathbf{r}_1^P}{dt}\right|_1 + \boldsymbol{\omega}_{10}\times\mathbf{r}_1^P, \qquad \left.\frac{d\mathbf{r}_1^P}{dt}\right|_1 \equiv \mathbf{v}_1^P \ \text{(relative velocity, Notes Eq. 3.19)} $$
**Result** (Notes Eq. 3.20):
$$ \boxed{\mathbf{v}_0^P = \mathbf{v}_0^A + \mathbf{v}_1^P + \boldsymbol{\omega}_{10}\times\mathbf{r}_1^P} $$
The absolute velocity equals the velocity of the origin of $S_1$, plus the relative velocity, plus the term $\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P$ associated with the rotation of $S_1$ with respect to $S_0$ (Slide 24).

### 10.4 Acceleration (Slide 25, Notes Eqs. 3.21–3.25)
**Step 1: differentiate the velocity in $S_0$** (Notes Eq. 3.21):
$$ \mathbf{a}_0^P \equiv \left.\frac{d\mathbf{v}_0^P}{dt}\right|_0 = \left.\frac{d\mathbf{v}_0^A}{dt}\right|_0 + \left.\frac{d\mathbf{v}_1^P}{dt}\right|_0 + \left.\frac{d}{dt}\right|_0\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) $$
**Step 2: first term.** $\left.\frac{d\mathbf{v}_0^A}{dt}\right|_0 = \mathbf{a}_0^A$.
**Step 3: second term, Coriolis theorem** (Notes Eq. 3.22), with $\left.\frac{d\mathbf{v}_1^P}{dt}\right|_1 \equiv \mathbf{a}_1^P$ the **relative acceleration** (Notes Eq. 3.24):
$$ \left.\frac{d\mathbf{v}_1^P}{dt}\right|_0 = \mathbf{a}_1^P + \boldsymbol{\omega}_{10}\times\mathbf{v}_1^P $$
**Step 4: third term, product rule for the cross product** (Notes Eq. 1.67), then Coriolis on $\mathbf{r}_1^P$ as in Section 10.3 (Notes Eq. 3.23):
$$ \left.\frac{d}{dt}\right|_0\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) = \underbrace{\left.\frac{d\boldsymbol{\omega}_{10}}{dt}\right|_0}_{\boldsymbol{\alpha}_{10}}\times\mathbf{r}_1^P + \boldsymbol{\omega}_{10}\times\underbrace{\left.\frac{d\mathbf{r}_1^P}{dt}\right|_0}_{\mathbf{v}_1^P + \boldsymbol{\omega}_{10}\times\mathbf{r}_1^P} = \boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P + \boldsymbol{\omega}_{10}\times\mathbf{v}_1^P + \boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) $$
**Step 5: add the three terms.** The term $\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P$ appears twice (once from Step 3 and once from Step 4), which produces the factor 2 (Notes Eq. 3.25):
$$ \boxed{\mathbf{a}_0^P = \mathbf{a}_0^A + \mathbf{a}_1^P + \boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P + \boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) + 2\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P} $$
The absolute acceleration equals the acceleration of the origin of $S_1$, plus the relative acceleration, plus three terms associated with the rotation of $S_1$ with respect to $S_0$ (Slide 25):
| Term | Name |
| :--- | :--- |
| $\mathbf{a}_0^A$ | acceleration of the origin of $S_1$ |
| $\mathbf{a}_1^P$ | relative acceleration |
| $\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P$ | Euler acceleration |
| $\boldsymbol{\omega}_{10}\times(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P)$ | centripetal acceleration |
| $2\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P$ | Coriolis acceleration |

### 10.5 Summary (Slide 26, Notes Eqs. 3.16, 3.26–3.27)
$$ \mathbf{r}_0^P = \mathbf{r}_0^A + \mathbf{r}_1^P $$
$$ \mathbf{v}_0^P = \mathbf{v}_0^A + \mathbf{v}_1^P + \boldsymbol{\omega}_{10}\times\mathbf{r}_1^P $$
$$ \mathbf{a}_0^P = \mathbf{a}_0^A + \mathbf{a}_1^P + \boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P + \boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) + 2\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P $$
The right-hand sides use only relative quantities ($\mathbf{r}_1^P, \mathbf{v}_1^P, \mathbf{a}_1^P$) plus the information on the motion of $S_1$: $\mathbf{r}_0^A, \mathbf{v}_0^A, \mathbf{a}_0^A, \boldsymbol{\omega}_{10}, \boldsymbol{\alpha}_{10}$ (Slide 26).

### 10.6 Remarks on each term (Notes p. 39)
1. The translation of the origin $A$ appears only through $\mathbf{v}_0^A$ and $\mathbf{a}_0^A$. All other terms come from the relative motion of $P$ in $S_1$ and/or the angular motion of $S_1$ with respect to $S_0$.
2. The direction of $\boldsymbol{\omega}_{10}$ is the direction of the axis of rotation of $S_1$ with respect to $S_0$.
3. $\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P$ is perpendicular to $\boldsymbol{\omega}_{10}$ and to $\mathbf{r}_1^P$; its magnitude is $\omega_{10}\,r_{1,\perp}^P$, where $r_{1,\perp}^P$ is the component of $\mathbf{r}_1^P$ perpendicular to $\boldsymbol{\omega}_{10}$.
4. The same holds for $\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P$ with respect to $\boldsymbol{\alpha}_{10}$; since $\boldsymbol{\omega}_{10}$ and $\boldsymbol{\alpha}_{10}$ are in general not parallel, this term can have a component along $\boldsymbol{\omega}_{10}$.
5. The centripetal term has magnitude $r_{1,\perp}^P\,\omega_{10}^2$ and always points toward the line defined by the origin $A$ and $\boldsymbol{\omega}_{10}$.
6. The factor 2 of the Coriolis term comes from two different effects of equal importance (Steps 3 and 4 above): the rotation of the relative velocity vector, and the change of the rotation term $\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P$ as $P$ moves in $S_1$. The Coriolis acceleration appears only in a rotating frame and only when the particle has relative velocity.

### 10.7 Translating frame without rotation (Notes Eqs. 3.28–3.29)
If $S_1$ only translates, $\boldsymbol{\omega}_{10} = \mathbf{0}$ and $\boldsymbol{\alpha}_{10} = \mathbf{0}$:
$$ \mathbf{v}_0^P = \mathbf{v}_0^A + \mathbf{v}_1^P, \qquad \mathbf{a}_0^P = \mathbf{a}_0^A + \mathbf{a}_1^P $$
The motions simply add. If moreover $\mathbf{v}_0^A$ is constant (which requires $A$ to move on a straight line), $\mathbf{a}_0^A = \mathbf{0}$ and $\mathbf{a}_0^P = \mathbf{a}_1^P$: both observers measure the same acceleration.

---

## 🧲 11. Relative Dynamics: Inertia Forces (Slides 27–28, Notes Sec. 4.9)

### 11.1 The problem (Slide 27)
Newton's laws of motion are valid only in an **inertial** reference frame. Assuming $S_0$ is inertial, the equation of motion of $P$ (mass $m^P$, resultant of the actual forces $\mathbf{F}$) is (Notes Eq. 4.59)
$$ m^P\mathbf{a}_0^P = \mathbf{F} $$
If $S_1$ accelerates or rotates relative to $S_0$, it is non-inertial. Can Newton's laws be fixed so that they can be applied in $S_1$?

### 11.2 Derivation (Slide 27, Notes Eqs. 4.60–4.63)
**Step 1.** Substitute the acceleration formula of Section 10.4 into Newton's law (Notes Eq. 4.60):
$$ m^P\left[\mathbf{a}_0^A + \mathbf{a}_1^P + \boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P + \boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) + 2\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P\right] = \mathbf{F} $$
**Step 2.** Keep the relative acceleration on the left and move every other term to the right (Notes Eq. 4.61):
$$ m^P\mathbf{a}_1^P = \mathbf{F} - m^P\mathbf{a}_0^A - m^P\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P - m^P\boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) - 2m^P\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P $$
**Step 3.** Define the **fictitious** or **inertia force** (Notes Eq. 4.62):
$$ \mathbf{F}_i = -m^P\mathbf{a}_0^A - m^P\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P - m^P\boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) - 2m^P\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P $$
so that (Notes Eq. 4.63)
$$ \boxed{m^P\mathbf{a}_1^P = \mathbf{F} + \mathbf{F}_i} $$
Newton's laws can be applied in a non-inertial frame if we introduce the inertia force (Slide 27).

### 11.3 Interpretation
Eq. 4.63 contains exactly the same information as Eq. 4.60: terms have only been moved from one side to the other. The new reading is that an observer on $S_1$ can apply Newton's second law **provided he adds the force $\mathbf{F}_i$** to the actual forces. Every term of $\mathbf{F}_i$ can be computed from the relative position and velocity of $P$ once $\mathbf{a}_0^A$, $\boldsymbol{\omega}_{10}$ and $\boldsymbol{\alpha}_{10}$ are known (Notes p. 53).

### 11.4 Names of the four terms (Slide 28, Notes p. 53)
| Term | Name | Symbol (Slides 29–31) |
| :--- | :--- | :--- |
| $-m^P\mathbf{a}_0^A$ | force due to the acceleration of the origin | $\mathbf{F}_A$ |
| $-m^P\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P$ | Euler's force | $\mathbf{F}_E$ |
| $-m^P\boldsymbol{\omega}_{10}\times(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P)$ | centrifugal force due to the rotation of $S_1$ | $\mathbf{F}_C$ |
| $-2m^P\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P$ | Coriolis force | $\mathbf{F}_{COR}$ |

### 11.5 General properties (Slide 28)
* All inertia forces are **proportional to the mass** of the particle.
* Forces 1 to 3 are **locally indistinguishable from a gravitational force field**: an observer in $S_1$ cannot tell them apart from an actual gravitational force.
* Force 4 (Coriolis) is different: it is zero if the particle is at rest in $S_1$, and it appears only when $P$ has a relative velocity with a component perpendicular to $\boldsymbol{\omega}_{10}$.
* We can now obtain the equations of motion of a particle in inertial and non-inertial reference frames. **Choose the simplest option for each problem** (Slide 28).

### 11.6 Physical intuition (Notes p. 53)
Despite being fictitious, an observer on a non-inertial frame may feel these forces as very real; but they are due solely to the motion (with respect to an inertial frame) of the frame in which the modified law is applied.
* **Braking vehicle.** We tend to go forward when a vehicle suddenly brakes, and it is common to say that the inertia force $-m\mathbf{a}_0^A$ "pushes" us. For an observer on the ground no such force exists: the vehicle decelerates because of the friction of the wheels with the ground, and the passenger's mass tends to continue its forward motion.
* **Turning vehicle.** The road applies a transverse friction force that accelerates the vehicle toward the centre of curvature (a normal acceleration). The passenger tends to continue in uniform rectilinear motion and feels "pushed outward", until the seat and the floor transmit the necessary force: this is the centrifugal force seen from the vehicle.
* **Accelerating merry-go-round.** Besides the outward centrifugal force, a child feels a force pointing backward with respect to the direction of travel, due to the Euler term $-m\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P$.
* **Ball thrown on the merry-go-round.** A ball passed from the outer to the inner part deviates from the expected straight line toward the direction of travel, because of the Coriolis force. The same force explains the sense of rotation of hurricanes in the Northern and Southern hemispheres, and why a cannonball shot toward the East lands farther than one shot equally toward the West.

In summary, the motion of a particle can always be analysed in two ways: with the original Newton's second law in an inertial frame, or with the modified law (inertia forces added) in a non-inertial frame (Notes p. 53).

---

## ⚡ 12. Energy and Potentials in a Non-Inertial Frame (Slides 29–31)

### 12.1 Energy and other quantities in $S_1$ (Slide 29)
We can always define the kinetic energy $T_1^P = \tfrac12 m^P\,\mathbf{v}_1^P\cdot\mathbf{v}_1^P$ and the mechanical energy $E_1^P$ of $P$ in $S_1$ even if $S_1$ is non-inertial. If the necessary conditions are met (the same as before: all the forces that do work in $S_1$, inertia forces included, derive from a potential), $E_1^P$ is a conserved quantity of motion. Similarly, the angular momentum $\mathbf{H}_{A1}^P$, or any other quantity used so far, can be defined in $S_1$ (Slide 29).

### 12.2 Force due to the acceleration of the origin (Slide 29)
If $\mathbf{a}_0^A$ is **constant**, $\mathbf{F}_A = -m^P\mathbf{a}_0^A$ is a homogeneous force field in $S_1$ (same vector at every point, like uniform gravity) and has a potential:
$$ V_1 = m^P\,\mathbf{a}_0^A\cdot\mathbf{r}_1^P, \qquad \mathbf{F}_A = -\nabla V_1 = -m^P\mathbf{a}_0^A $$
**Check.** With $\mathbf{r}_1^P = x_1\mathbf{i}_1 + y_1\mathbf{j}_1 + z_1\mathbf{k}_1$ and constant components $a_x, a_y, a_z$ of $\mathbf{a}_0^A$, $V_1 = m^P(a_x x_1 + a_y y_1 + a_z z_1)$, so $\partial V_1/\partial x_1 = m^P a_x$, etc., and $-\nabla V_1 = -m^P\mathbf{a}_0^A$.

### 12.3 Centrifugal force (Slide 30)
Decompose the relative position into its parts parallel and perpendicular to the rotation axis, with $\boldsymbol{\omega}_{10} = \omega_{10}\,\mathbf{e}_\omega$:
$$ \mathbf{r}_1^P = \mathbf{r}_\parallel + \mathbf{r}_\perp, \qquad \mathbf{r}_\parallel = r_\parallel\,\mathbf{e}_\omega, \quad r_\parallel = \mathbf{e}_\omega\cdot\mathbf{r}_1^P $$
**Step 1: double cross product** ($\mathbf{a}\times(\mathbf{b}\times\mathbf{c}) = (\mathbf{a}\cdot\mathbf{c})\,\mathbf{b} - (\mathbf{a}\cdot\mathbf{b})\,\mathbf{c}$):
$$ \boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) = \left(\boldsymbol{\omega}_{10}\cdot\mathbf{r}_1^P\right)\boldsymbol{\omega}_{10} - \left(\omega_{10}\right)^2\mathbf{r}_1^P $$
**Step 2: substitute** $\boldsymbol{\omega}_{10}\cdot\mathbf{r}_1^P = \omega_{10}\,r_\parallel$ and $\boldsymbol{\omega}_{10} = \omega_{10}\mathbf{e}_\omega$:
$$ \boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) = \left(\omega_{10}\right)^2\left[r_\parallel\,\mathbf{e}_\omega - \mathbf{r}_1^P\right] = -\left(\omega_{10}\right)^2\mathbf{r}_\perp $$
**Result:**
$$ \mathbf{F}_C = -m^P\boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) = m^P\left(\omega_{10}\right)^2\mathbf{r}_\perp $$
$\mathbf{F}_C$ is proportional to $(\omega_{10})^2$ and to $r_\perp$, and points in the direction of $\mathbf{r}_\perp$: radially outward from the rotation axis (Slide 30). If $\boldsymbol{\omega}_{10}$ is **constant**, it admits a potential in $S_1$:
$$ V_1 = -\frac12 m^P\left(\omega_{10}\right)^2\left(r_\perp\right)^2, \qquad \mathbf{F}_C = -\nabla V_1 = m^P\left(\omega_{10}\right)^2\mathbf{r}_\perp $$
**Check.** $(r_\perp)^2 = \mathbf{r}_1^P\cdot\mathbf{r}_1^P - (\mathbf{e}_\omega\cdot\mathbf{r}_1^P)^2$, so $\nabla (r_\perp)^2 = 2\mathbf{r}_1^P - 2(\mathbf{e}_\omega\cdot\mathbf{r}_1^P)\,\mathbf{e}_\omega = 2\mathbf{r}_\perp$, and $-\nabla V_1 = \tfrac12 m^P(\omega_{10})^2\cdot 2\mathbf{r}_\perp$. For a rotation about $\mathbf{k}_1$ this reads $V_1 = -\tfrac12 m^P\omega_{10}^2(x_1^2 + y_1^2)$.

### 12.4 Euler force (Slide 31)
$\mathbf{F}_E = -m^P\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P$ is always perpendicular to $\boldsymbol{\alpha}_{10}$ and to $\mathbf{r}_1^P$. It does **not** admit a potential: $\nabla\times\mathbf{F}_E \neq \mathbf{0}$ (Slide 31). (For a given $\boldsymbol{\alpha}_{10}$, $\nabla\times(\boldsymbol{\alpha}_{10}\times\mathbf{r}) = 2\boldsymbol{\alpha}_{10}$, so $\nabla\times\mathbf{F}_E = -2m^P\boldsymbol{\alpha}_{10}$, non-zero whenever the frame has angular acceleration.)

### 12.5 Coriolis force (Slide 31)
$\mathbf{F}_{COR} = -2m^P\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P$ is always perpendicular to $\boldsymbol{\omega}_{10}$ and to $\mathbf{v}_1^P$. Its magnitude is proportional to $v_\perp$, the component of $\mathbf{v}_1^P$ perpendicular to $\boldsymbol{\omega}_{10}$. Because it is perpendicular to $\mathbf{v}_1^P$, its power in $S_1$ vanishes:
$$ \mathbf{F}_{COR}\cdot\mathbf{v}_1^P = -2m^P\left(\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P\right)\cdot\mathbf{v}_1^P = 0 $$
so **$\mathbf{F}_{COR}$ never exerts work** (Slide 31) and never spoils the conservation of $E_1^P$.

**Example: equatorial launch (Slide 31).** On the equator, $\boldsymbol{\omega}_{10}$ points north (horizontal). For a projectile launched **toward the East**, $\mathbf{v}_1^P$ has an eastward component and $-2m^P\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P$ has an **upward** component: the trajectory is higher and longer than without rotation. **Toward the West** the Coriolis force points **downward** and the trajectory is lower and shorter. (With local unit vectors East $\mathbf{e}_E$, North $\mathbf{e}_N$, Up $\mathbf{e}_U$, right-handed in that order, $\mathbf{e}_N\times\mathbf{e}_E = -\mathbf{e}_U$, so $-2m\Omega\,\mathbf{e}_N\times(v\,\mathbf{e}_E) = 2m\Omega v\,\mathbf{e}_U$.) This is the cannonball effect of Section 11.6.

### 12.6 Conservation of $E_1^P$ in a frame rotating at constant rate
For a frame with fixed origin ($\mathbf{a}_0^A = \mathbf{0}$) rotating with constant $\boldsymbol{\omega}_{10}$ ($\boldsymbol{\alpha}_{10} = \mathbf{0}$), the Euler force vanishes, the centrifugal force has the potential of Section 12.3 and the Coriolis force does no work. If the actual forces that do work are conservative (and the constraints are fixed **in $S_1$**), then
$$ E_1^P = \frac12 m^P\left|\mathbf{v}_1^P\right|^2 + V(\mathbf{r}_1^P) - \frac12 m^P\omega_{10}^2 r_\perp^2 = \text{const} $$
This is the energy integral used in the rotating-wire and rotating-ring problems of this topic. If $\boldsymbol{\omega}_{10}$ depends on time, the Euler force appears and the centrifugal potential depends explicitly on time, so $E_1^P$ is in general not conserved.

---

## 📐 13. Method for Relative-Motion Problems
This checklist condenses Slides 22, 26 and 28 into the order used in the solved problems:
1. **Choose the frames.** $S_0$ inertial; $S_1$ attached to the moving body (wire, ring, platform, spacecraft) so that the constraint or the motion is simple in $S_1$.
2. **Describe the motion of $S_1$**: $\mathbf{r}_0^A, \mathbf{v}_0^A, \mathbf{a}_0^A$ and $[{}_0R_1]$, $\boldsymbol{\omega}_{10}, \boldsymbol{\alpha}_{10}$ (Section 9).
3. **Relative kinematics of $P$ in $S_1$**: $\mathbf{r}_1^P, \mathbf{v}_1^P, \mathbf{a}_1^P$ with the coordinates of the problem.
4. **Either** compute $\mathbf{a}_0^P$ with Notes Eq. 3.27 and write $m\mathbf{a}_0^P = \mathbf{F}$ in $S_0$, **or** write $m\mathbf{a}_1^P = \mathbf{F} + \mathbf{F}_i$ in $S_1$ (Notes Eq. 4.63). Both give the same equations.
5. **Project** on the directions where the reactions vanish to get the equations of motion; project on the others to get the reactions.
6. **First integrals**: $E_1^P$ if $\mathbf{a}_0^A$ and $\boldsymbol{\omega}_{10}$ are constant (or zero) and the constraints are fixed in $S_1$.

---

## 🗺️ 14. Source Map
| Content | Notes.pdf (printed pages) | Slides |
| :--- | :--- | :--- |
| Observers, absolute and relative | Ch. 3 introduction (p. 36) | 3, 23 |
| Translational motion of a frame | Sec. 3.2 (p. 38) | 4 |
| Change of basis, properties, composition | Sec. 1.5, Eqs. 1.6–1.17 (pp. 13–14) | 5–7 |
| Axis and angle of rotation | Sec. 1.5.1 (pp. 14–15) | 6 |
| Simple rotations | Sec. 1.5.2, Eqs. 1.18–1.20 (pp. 15–16) | 8 |
| Euler angles, 3-2-1 example | Sec. 1.5.3, Eqs. 1.21–1.23 (pp. 16–17) | 9–13 |
| Angular velocity and acceleration | Sec. 1.7, Eqs. 1.62, 1.73; Eqs. 3.3–3.5, 3.9 (pp. 21–25, 37) | 14–16 |
| Coriolis theorem | Sec. 3.1, Eqs. 3.1–3.8 (pp. 36–37) | 17–18 |
| Composition of angular motions | Eqs. 3.10–3.15 (pp. 37–38) | 19 |
| Angular velocity from Euler angles | none | 20–21 |
| Configuration and motion of a frame | Sec. 3.2 (p. 38) | 22 |
| Relative kinematics | Sec. 3.2, Eqs. 3.16–3.29 (pp. 38–40) | 23–26 |
| Relative dynamics, inertia forces | Sec. 4.9, Eqs. 4.59–4.63 (pp. 52–53) | 27–28 |
| Potentials, Euler and Coriolis forces | none | 29–31 |

Worked problems (Problems 7, 9, 20, 21, 25, 26, 27, 28, 30, 33, 34, 36, 37, 40, 41, 47, 49, 51 of Problems.pdf) are solved step by step, in the order of the course, in [[Solution Set - Topic 5 Relative Motion]].
