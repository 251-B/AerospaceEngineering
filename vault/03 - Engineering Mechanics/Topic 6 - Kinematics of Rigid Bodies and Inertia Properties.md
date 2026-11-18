---
title: "Topic 6 - Kinematics of Rigid Bodies and Inertia Properties"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/teoria/Notes.pdf"
type: "Theory"
language: "English"
tags:
  - theory
  - topic-6
  - rigid-body
  - euler-angles
  - inertia-tensor
  - centre-of-mass
  - principal-axes
  - steiner-theorem
---

# Topic 6 - Kinematics of Rigid Bodies and Inertia Properties

> A rigid body is kinematically the same object as a reference frame attached to it: its whole velocity field follows from the velocity of one body point and the angular velocity $\boldsymbol\omega_{B0}$, its attitude follows from three Euler angles, and its instantaneous motion is always a screw about the instantaneous axis of rotation and slip. Its mass distribution enters the mechanics only through three objects built from the zeroth, first and second moments of that distribution: the total mass $m$, the centre of mass $G$ and the tensor of inertia $\boldsymbol{\mathcal I}_O$, which changes basis like any second-order tensor, has an orthonormal principal basis, and moves from $G$ to any point $O$ by Steiner's theorem.

This note follows `Notes.pdf` Chapter 9 (Kinematics of rigid bodies, Eqs. 9.1 to 9.24) and Chapter 10 (Geometry of masses and inertia properties, Eqs. 10.1 to 10.48), and the decks of Lecture 7 (Rigid body kinematics, Slides 1 to 14) and Lecture 8 (Inertia properties, Slides 1 to 22), in the order of the notes. Earlier results that are used are cited, not re-derived: the change of basis of Chapter 1 (Eqs. 1.6 to 1.23), the tensor product (Eqs. 1.34 to 1.48), the double vector product (Eq. 1.37), and the Coriolis theorem with the composition laws of Chapter 3 (Eqs. 3.8 to 3.27). See also [[Concept - Vector Bases Rotation Matrices and Poisson Theorem]], [[Concept - Attitude of a Reference Frame and Euler Angles]] and [[Concept - Angular Velocity Angular Acceleration and Coriolis Theorem]].

| Symbol | Meaning |
| :--- | :--- |
| $S_0 = \{O;\mathcal B_0\}$ | fixed (reference) frame, basis $\{\mathbf i_0,\mathbf j_0,\mathbf k_0\}$ |
| $S_B = \{P;\mathcal B_B\}$ | body-fixed frame with origin at the body point $P$, basis $\{\mathbf i_B,\mathbf j_B,\mathbf k_B\}$ (the slides write $S_b$) |
| $\boldsymbol\omega_{B0}$, $\boldsymbol\alpha_{B0}$ | angular velocity and angular acceleration of $S_B$ (of the body) with respect to $S_0$ |
| $\mathbf v_0^A$, $\mathbf a_0^A$ | velocity and acceleration of the point $A$ as seen from $S_0$ |
| $\mathbf r_B^A = \mathbf{PA}$ | position of $A$ in $S_B$ |
| $\mathbf e_\omega = \boldsymbol\omega_{B0}/\omega_{B0}$ | unit vector along the angular velocity |
| $v_{0\parallel}$, $\mathbf v_{0\parallel}$ | slip speed and slip velocity (component along $\mathbf e_\omega$) |
| $A(B)$ | the body point that instantaneously coincides with the geometric point $A$ |
| $[{}_0R_1]$ | change of basis matrix from $\mathcal B_1$ to $\mathcal B_0$ (column $n$ = vector $n$ of $\mathcal B_1$ written in $\mathcal B_0$) |
| $\psi,\ \theta,\ \varphi$ | Euler angles: precession, nutation, spin (3-1-3); yaw, pitch, roll (3-2-1) |
| $\mathcal D$, $dm$ | mass distribution and its mass element; $dm = \lambda\,d\ell = \sigma\,dA = \rho\,dV$ |
| $\mathcal M_{O,n}^{\mathcal D}$ | $n$-th moment of the mass distribution about $O$ |
| $I_x, I_y, I_z$; $I_{xy}, I_{xz}, I_{yz}$; $I_O$ | moments of inertia about the axes, about the planes and about the point $O$ |
| $P_{xy,xz}$, $P_{xy,yz}$, $P_{xz,yz}$ | products of inertia with respect to pairs of coordinate planes |
| $\boldsymbol{\mathcal I}_O$, $\boldsymbol{\mathcal U}$ | tensor of inertia about $O$ (the notes write it with the subscript of the frame origin) and unit tensor |
| $[\boldsymbol{\mathcal I}_O]_{00}$ | components of the tensor in the tensor basis $\mathcal B_0\otimes\mathcal B_0$ |
| $I_1, I_2, I_3$; $\mathbf e_1,\mathbf e_2,\mathbf e_3$ | principal moments and principal directions of inertia |

## 1. The rigid body model and body-fixed reference frames

> [!summary] What you need to know
> - A **rigid body** never changes shape: the distance between any two of its points stays the same, and so does every angle between its segments.
> - It is an idealisation. Real materials deform a little, but often too little to change the motion.
> - Three body points $P$, $Q$, $R$ that are not on one line are enough to fix a frame $S_B$ to the body: origin at $P$, and an orthonormal basis $\{\mathbf i_B, \mathbf j_B, \mathbf k_B\}$ built from the segments $\mathbf{PQ}$ and $\mathbf{PR}$.
> - Knowing where the body is and knowing where $S_B$ is are the same thing: both move together and turn with one angular velocity, $\boldsymbol\omega_{B0}$.
>
> $$\boxed{\frac{d}{dt}\lvert\mathbf{AB}\rvert = 0 \quad \text{for every pair of body points } A,\ B}$$
>
> **Slides:** [Lecture 7, Slide 3]; [Lecture 7, Slide 4]; Notes.pdf, Sec. 9

The point particle model ignores the dimensions of an object, its mass distribution and its orientation (attitude) in space. The rigid body model keeps the last two: a rigid body is a body of finite, indeformable geometry (Notes.pdf, Sec. 9; [Lecture 7, Slide 3]). Like the point particle, it is an idealisation: all materials deform somewhat under load, but in many Flight Mechanics problems these small deformations do not affect the motion.

The defining kinematic constraint is that the distance between any two body points stays constant in time ([Lecture 7, Slide 3]). The first consequence is that angles between body segments are also constant.

> [!derivation] Rigidity keeps distances and angles
> **Law:** rigid body constraint; definition of the angle through the dot product
> **Source:** [Lecture 7, Slide 3]; Notes.pdf, Eq. 1.24
>
> For three body points $A$, $B$, $C$ the constraint states that $\lvert\mathbf{BA}\rvert$, $\lvert\mathbf{BC}\rvert$ and $\lvert\mathbf{AC}\rvert$ are constant. The angle $ABC$ follows from them:
>
> $$\begin{aligned}
> \lvert\mathbf{AC}\rvert^2 &= (\mathbf{BC}-\mathbf{BA})\cdot(\mathbf{BC}-\mathbf{BA}) \quad &\text{(since $\mathbf{AC} = \mathbf{AB}+\mathbf{BC} = \mathbf{BC}-\mathbf{BA}$)} \\
> &= \lvert\mathbf{BC}\rvert^2 + \lvert\mathbf{BA}\rvert^2 - 2\,\mathbf{BA}\cdot\mathbf{BC} \quad &\text{(distributive and commutative dot product, Eqs. 1.25-1.26)} \\
> \mathbf{BA}\cdot\mathbf{BC} &= \lvert\mathbf{BA}\rvert\,\lvert\mathbf{BC}\rvert\cos\widehat{ABC} \quad &\text{(definition of the dot product, Eq. 1.24)} \\
> \cos\widehat{ABC} &= \frac{\lvert\mathbf{BA}\rvert^2+\lvert\mathbf{BC}\rvert^2-\lvert\mathbf{AC}\rvert^2}{2\,\lvert\mathbf{BA}\rvert\,\lvert\mathbf{BC}\rvert} \quad &\text{(eliminate the dot product between both lines)}
> \end{aligned}$$
>
> $$\boxed{\frac{d}{dt}\lvert\mathbf{AB}\rvert = 0\ \ \forall A,B \in B \quad\Longrightarrow\quad \frac{d}{dt}\widehat{ABC} = 0}$$
>
> **Units:** the cosine is a ratio $[\mathrm{L^2}]/[\mathrm{L^2}] = [1]$
> **Meaning:** a rigid body keeps every length and every angle, so a triad of vectors drawn on it keeps its shape: it can only translate and rotate.

A body-fixed reference frame $S_B$ is built from three non-collinear body points $P$, $Q$, $R$: the origin is $P$ and the vectors $\mathbf{PQ}$, $\mathbf{PR}$ and their vector product are attached to the body (Notes.pdf, Sec. 9; [Lecture 7, Slide 4]). They need not be orthonormal, but we always choose a right-handed orthonormal basis built from them, as below. The choice of origin and basis is not unique.

![[attachments/EM-T/t6-body-frame.svg]]

> [!derivation] An orthonormal right-handed body basis from three body points
> **Law:** normalisation and vector product; right-hand rule
> **Source:** Notes.pdf, Sec. 9; [Lecture 7, Slide 4]
>
> $$\begin{aligned}
> \mathbf i_B &= \frac{\mathbf{PQ}}{\lvert\mathbf{PQ}\rvert} \quad &\text{(unit vector along the first body segment)} \\
> \mathbf k_B &= \frac{\mathbf{PQ}\times\mathbf{PR}}{\lvert\mathbf{PQ}\times\mathbf{PR}\rvert} \quad &\text{(normal to the plane $PQR$; non-zero because the points are not collinear)} \\
> \mathbf j_B &= \mathbf k_B\times\mathbf i_B \quad &\text{(completes the triad; $\mathbf k_B \perp \mathbf i_B$, so $\lvert\mathbf j_B\rvert = 1$)} \\
> \mathbf i_B\times\mathbf j_B &= \mathbf i_B\times(\mathbf k_B\times\mathbf i_B) = (\mathbf i_B\cdot\mathbf i_B)\mathbf k_B - (\mathbf i_B\cdot\mathbf k_B)\mathbf i_B = \mathbf k_B \quad &\text{(double vector product, Eq. 1.37: the basis is right-handed)}
> \end{aligned}$$
>
> $$\boxed{\mathcal B_B = \{\mathbf i_B,\ \mathbf j_B,\ \mathbf k_B\},\qquad \mathbf i_B\times\mathbf j_B = \mathbf k_B}$$
>
> **Units:** each vector is a ratio $[\mathrm L]/[\mathrm L]$ or $[\mathrm{L^2}]/[\mathrm{L^2}]$: dimensionless, as unit vectors must be
> **Meaning:** the three vectors are built only from body segments, whose lengths and angles never change, so the basis moves with the body and rotates with its angular velocity.

Two observations make the rigid body and its body-fixed frame interchangeable (Notes.pdf, Sec. 9; [Lecture 7, Slide 4]):

1. $S_B$ keeps its orientation relative to the body, so both rotate with the same angular velocity $\boldsymbol\omega_{B0}$: knowing the attitude of the body and knowing the attitude of $S_B$ are the same thing.
2. For an observer on $S_B$ every body point is at rest. Every point of the Euclidean space attached to $S_B$ can be treated as a body point, even outside the physical body.

> [!key] Rigid body and reference frame
> From the kinematic point of view a rigid body is fully equivalent to a reference frame: its shape and dimensions can be ignored and it can be replaced by $S_B$. Conversely, any reference frame can be thought of as a rigid body with a Euclidean space attached to it ([Lecture 7, Slide 4]).

## 2. Velocity and acceleration fields of a rigid body

> [!summary] What you need to know
> - Take one body point $P$ whose motion you know. Every other body point $A$ moves like $P$, plus a rotation about $P$.
> - **Velocity:** add the rotation term $\boldsymbol\omega_{B0}\times\mathbf{PA}$ to the velocity of $P$. **Acceleration:** add two terms, the angular acceleration term and the centripetal term.
> - If $\boldsymbol\omega_{B0}$ is zero, every point has the same velocity: the body is in pure translation.
> - All points share the velocity component along $\boldsymbol\omega_{B0}$ (the **slip velocity**). Only the perpendicular part changes from point to point.
> - Two body points always have the same velocity projection on the line that joins them, otherwise their distance would change. Use it to check that measured velocities fit a rigid body.
>
> $$\boxed{\mathbf v_0^A = \mathbf v_0^P + \boldsymbol\omega_{B0}\times\mathbf{PA},\qquad \mathbf a_0^A = \mathbf a_0^P + \boldsymbol\alpha_{B0}\times\mathbf{PA} + \boldsymbol\omega_{B0}\times(\boldsymbol\omega_{B0}\times\mathbf{PA})}$$
>
> **Slides:** [Lecture 7, Slide 6]; [Lecture 7, Slide 7]; Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 9.4

Let $P$ be the origin of $S_B$ and $A$ any other body point (Fig. 9.1 of the notes). The composition laws of relative motion, Eqs. 3.26 and 3.27, are applied with the moving frame $S_B$; the relative velocity and acceleration of a body point in $S_B$ are zero by the definition of body point ([Lecture 7, Slide 5]).

> [!derivation] Velocity of a body point from the composition of velocities
> **Law:** composition of velocities with the moving frame $S_B$; $A$ is at rest in $S_B$
> **Source:** Notes.pdf, Eq. 9.1; Notes.pdf, Eq. 3.26; [Lecture 7, Slide 6]
>
> $$\begin{aligned}
> \mathbf v_0^A &= \mathbf v_0^P + \mathbf v_B^A + \boldsymbol\omega_{B0}\times\mathbf r_B^A \quad &\text{(Eq. 3.26 with the moving frame $S_B$ of origin $P$)} \\
> \mathbf v_B^A &= \mathbf 0 \quad &\text{($A$ is a body point: it does not move in $S_B$)} \\
> \mathbf v_0^A &= \mathbf v_0^P + \boldsymbol\omega_{B0}\times\mathbf r_B^A \quad &\text{(substitute the zero relative velocity)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^A = \mathbf v_B^A + \mathbf v_0^P + \boldsymbol\omega_{B0}\times\mathbf r_B^A,\qquad \mathbf v_B^A = \mathbf 0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}] = [\mathrm{L\,T^{-1}}] + [\mathrm{T^{-1}}][\mathrm L]$
> **Meaning:** Eq. 9.1 is the general composition law with its relative term crossed out: a body point is dragged by the frame, it never moves relative to it.

> [!derivation] Acceleration of a body point from the composition of accelerations
> **Law:** composition of accelerations with the moving frame $S_B$; $A$ is at rest in $S_B$
> **Source:** Notes.pdf, Eq. 9.2; Notes.pdf, Eq. 3.27; [Lecture 7, Slide 6]
>
> $$\begin{aligned}
> \mathbf a_0^A &= \mathbf a_B^A + \mathbf a_0^P + \boldsymbol\alpha_{B0}\times\mathbf r_B^A + \boldsymbol\omega_{B0}\times(\boldsymbol\omega_{B0}\times\mathbf r_B^A) + 2\boldsymbol\omega_{B0}\times\mathbf v_B^A \quad &\text{(Eq. 3.27 with the moving frame $S_B$)} \\
> \mathbf a_B^A &= \mathbf 0,\quad \mathbf v_B^A = \mathbf 0 \quad &\text{($A$ is at rest in $S_B$ at every instant)} \\
> 2\boldsymbol\omega_{B0}\times\mathbf v_B^A &= \mathbf 0 \quad &\text{(no relative velocity: no Coriolis term)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^A = \mathbf a_0^P + \boldsymbol\alpha_{B0}\times\mathbf r_B^A + \boldsymbol\omega_{B0}\times(\boldsymbol\omega_{B0}\times\mathbf r_B^A)}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}] = [\mathrm{L\,T^{-2}}] + [\mathrm{T^{-2}}][\mathrm L] + [\mathrm{T^{-1}}][\mathrm{T^{-1}}][\mathrm L]$
> **Meaning:** of the five terms of Eq. 3.27 only the drag terms survive: the acceleration of the origin, the Euler term and the centripetal term.

> [!derivation] Velocity and acceleration fields
> **Law:** position of $A$ in $S_B$ written as the body segment from the origin
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 6]
>
> $$\begin{aligned}
> \mathbf r_B^A &= \mathbf{PA} \quad &\text{($P$ is the origin of $S_B$)} \\
> \mathbf v_0^A &= \mathbf v_0^P + \boldsymbol\omega_{B0}\times\mathbf{PA} \quad &\text{(substitute in Eq. 9.1)} \\
> \mathbf a_0^A &= \mathbf a_0^P + \boldsymbol\alpha_{B0}\times\mathbf{PA} + \boldsymbol\omega_{B0}\times(\boldsymbol\omega_{B0}\times\mathbf{PA}) \quad &\text{(substitute in Eq. 9.2)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^A = \mathbf v_0^P + \boldsymbol\omega_{B0}\times\mathbf{PA},\qquad \mathbf a_0^A = \mathbf a_0^P + \boldsymbol\alpha_{B0}\times\mathbf{PA} + \boldsymbol\omega_{B0}\times(\boldsymbol\omega_{B0}\times\mathbf{PA})}$$
>
> **Units:** velocity $[\mathrm{L\,T^{-1}}]$ and acceleration $[\mathrm{L\,T^{-2}}]$ in every term
> **Meaning:** the motion of every body point is the motion of an arbitrarily chosen body point $P$ plus a rotation about $P$; these two formulas are the velocity field and the acceleration field of the rigid body.

To know the whole velocity field at an instant it is enough to know the velocity of one body point and $\boldsymbol\omega_{B0}$ (Notes.pdf, Sec. 9.1.1). The field has the following properties.

> [!derivation] Pure translation
> **Law:** velocity field with zero angular velocity
> **Source:** Notes.pdf, Eq. 9.3; [Lecture 7, Slide 6]
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0} &= \mathbf 0 \quad &\text{(hypothesis)} \\
> \mathbf v_0^A &= \mathbf v_0^P + \mathbf 0\times\mathbf{PA} = \mathbf v_0^P \quad &\text{(Eq. 9.3; the vector product with the zero vector vanishes)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{B0} = \mathbf 0 \ \Longrightarrow\ \mathbf v_0^A = \mathbf v_0^P\quad \forall A}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** all points have the same velocity: the body moves, at that instant, in pure translation.

> [!derivation] All body points share the velocity component along the angular velocity
> **Law:** dot product of the velocity field with $\mathbf e_\omega$; triple product with two parallel vectors
> **Source:** Notes.pdf, Eq. 9.5; [Lecture 7, Slide 6]; Notes.pdf, Eq. 1.33
>
> $$\begin{aligned}
> \mathbf e_\omega &= \frac{\boldsymbol\omega_{B0}}{\omega_{B0}} \quad &\text{(unit vector of the angular velocity, $\omega_{B0} \neq 0$)} \\
> \mathbf v_0^A\cdot\mathbf e_\omega &= \mathbf v_0^P\cdot\mathbf e_\omega + (\boldsymbol\omega_{B0}\times\mathbf{PA})\cdot\mathbf e_\omega \quad &\text{(dot-multiply Eq. 9.3 by $\mathbf e_\omega$)} \\
> (\boldsymbol\omega_{B0}\times\mathbf{PA})\cdot\mathbf e_\omega &= \omega_{B0}\,(\mathbf e_\omega\times\mathbf{PA})\cdot\mathbf e_\omega = 0 \quad &\text{(a vector product is perpendicular to both factors)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^A\cdot\mathbf e_\omega = \mathbf v_0^P\cdot\mathbf e_\omega = v_{0\parallel}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the component of the velocity along the angular velocity, the slip speed, is the same for every body point; when it is zero the motion is a pure rotation.

> [!derivation] Parallel and perpendicular parts of the velocity
> **Law:** decomposition of a vector along a unit vector and in the plane normal to it
> **Source:** Notes.pdf, Eq. 9.6; [Lecture 7, Slide 6]; Notes.pdf, Eq. 1.57
>
> $$\begin{aligned}
> \mathbf v_{0\parallel} &= (\mathbf v_0^A\cdot\mathbf e_\omega)\,\mathbf e_\omega = v_{0\parallel}\,\mathbf e_\omega \quad &\text{(projection on $\mathbf e_\omega$; identical for all points by Eq. 9.5)} \\
> \mathbf v_{0\perp}^A &= \mathbf v_0^A - \mathbf v_{0\parallel} \quad &\text{(remainder, in the plane normal to $\boldsymbol\omega_{B0}$)} \\
> \mathbf v_{0\perp}^A\cdot\mathbf e_\omega &= v_{0\parallel} - v_{0\parallel} = 0 \quad &\text{(check: the remainder has no component along $\mathbf e_\omega$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^A = \mathbf v_{0\parallel} + \mathbf v_{0\perp}^A}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the slip velocity is common to the whole body; only the perpendicular part changes from point to point.

> [!derivation] Equal projections along the segment joining two points
> **Law:** dot product of the velocity field with $\mathbf{PA}$
> **Source:** Notes.pdf, Eq. 9.7; [Lecture 7, Slide 7]
>
> $$\begin{aligned}
> \mathbf v_0^A\cdot\mathbf{PA} &= \mathbf v_0^P\cdot\mathbf{PA} + (\boldsymbol\omega_{B0}\times\mathbf{PA})\cdot\mathbf{PA} \quad &\text{(dot-multiply Eq. 9.3 by $\mathbf{PA}$)} \\
> (\boldsymbol\omega_{B0}\times\mathbf{PA})\cdot\mathbf{PA} &= 0 \quad &\text{(the vector product is perpendicular to $\mathbf{PA}$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^A\cdot\mathbf{PA} = \mathbf v_0^P\cdot\mathbf{PA}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}][\mathrm L] = [\mathrm{L^2\,T^{-1}}]$ on both sides
> **Meaning:** any two body points have the same velocity projection on the line that joins them; otherwise their distance would change and the body would not be rigid.

![[attachments/EM-T/t6-projection-property.svg]]

The velocities of three non-collinear body points $A$, $C$, $D$ also fix the field, through Eqs. 9.12 and 9.13 ([Lecture 7, Slide 7] writes them with $B$ and $C$). The data must be compatible, or the object is not a rigid body.

> [!derivation] Field from three non-collinear points and compatibility of the data
> **Law:** velocity field between pairs of body points
> **Source:** Notes.pdf, Eq. 9.12; Notes.pdf, Eq. 9.13; [Lecture 7, Slide 7]
>
> $$\begin{aligned}
> \mathbf v_0^C &= \mathbf v_0^A + \boldsymbol\omega_{B0}\times\mathbf{AC} \quad &\text{(Eq. 9.3 from $A$ to $C$: three scalar equations)} \\
> \mathbf v_0^D &= \mathbf v_0^A + \boldsymbol\omega_{B0}\times\mathbf{AD} \quad &\text{(Eq. 9.3 from $A$ to $D$: three more scalar equations)} \\
> (\mathbf v_0^C-\mathbf v_0^A)\cdot\mathbf{AC} &= 0,\quad (\mathbf v_0^D-\mathbf v_0^A)\cdot\mathbf{AD} = 0,\quad (\mathbf v_0^D-\mathbf v_0^C)\cdot\mathbf{CD} = 0 \quad &\text{(Eq. 9.7 for the three pairs: conditions on the data)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^C - \mathbf v_0^A = \boldsymbol\omega_{B0}\times\mathbf{AC},\qquad \mathbf v_0^D - \mathbf v_0^A = \boldsymbol\omega_{B0}\times\mathbf{AD}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}] = [\mathrm{T^{-1}}][\mathrm L]$
> **Meaning:** six scalar equations for the three unknown components of $\boldsymbol\omega_{B0}$; they have a solution only when the nine measured components satisfy the three equal-projection conditions, which is what "compatible data" means.

> [!key] What fixes the instantaneous velocity field
> Completely determining the instantaneous velocity field of a rigid body is equivalent to knowing $\boldsymbol\omega_{B0}$ and the velocity of one body point ([Lecture 7, Slide 7]). Other equivalent data sets (Notes.pdf, Sec. 9.1.3): a point of the instantaneous axis, $\boldsymbol\omega_{B0}$ and the slip speed; the velocities of three non-collinear points; or the velocities of two points plus one extra independent condition.

## 3. Instantaneous axis of rotation and slip, and helical motion

> [!summary] What you need to know
> - At every instant there is one line, parallel to $\boldsymbol\omega_{B0}$, called the **instantaneous axis of rotation and slip**.
> - The points on that line move only with the slip velocity $\mathbf v_{0\parallel}$, the smallest speed in the body.
> - To find it, start from a point $A$ of known velocity: the formula below gives $I$, the point of the axis closest to $A$. The axis is the line through $I$ along $\boldsymbol\omega_{B0}$.
> - Every other point moves like a screw: it turns around the axis at a speed $\omega_{B0}\,d$, where $d$ is its distance to the axis, and slides along it with the common slip. With zero slip the motion is a pure rotation about the axis.
>
> $$\boxed{\mathbf{AI} = \frac{\boldsymbol\omega_{B0}\times\mathbf v_0^A}{\omega_{B0}^2},\qquad \mathbf v_0^I = \mathbf v_{0\parallel}}$$
>
> **Slides:** [Lecture 7, Slide 8]; [Lecture 7, Slide 9]; Notes.pdf, Eq. 9.10; Notes.pdf, Eq. 9.11

In a pure rotation (zero slip speed) the instantaneous axis of rotation is the locus of body points with zero velocity; it is the line parallel to $\boldsymbol\omega_{B0}$ through any one such point $I$ (Notes.pdf, Sec. 9.1.2).

> [!derivation] Condition for a point of the instantaneous axis
> **Law:** velocity field from the known point $A$; double vector product
> **Source:** Notes.pdf, Eq. 9.8; Notes.pdf, Eq. 9.9; Notes.pdf, Eq. 1.37; [Lecture 7, Slide 9]
>
> $$\begin{aligned}
> \mathbf v_0^I &= \mathbf v_0^A + \boldsymbol\omega_{B0}\times\mathbf{AI} = \mathbf 0 \quad &\text{(Eq. 9.3 from $A$ to $I$; $I$ has zero velocity)} \\
> \boldsymbol\omega_{B0}\times\mathbf v_0^A + \boldsymbol\omega_{B0}\times(\boldsymbol\omega_{B0}\times\mathbf{AI}) &= \mathbf 0 \quad &\text{(cross-multiply on the left by $\boldsymbol\omega_{B0}$)} \\
> \boldsymbol\omega_{B0}\times(\boldsymbol\omega_{B0}\times\mathbf{AI}) &= (\boldsymbol\omega_{B0}\cdot\mathbf{AI})\,\boldsymbol\omega_{B0} - (\boldsymbol\omega_{B0}\cdot\boldsymbol\omega_{B0})\,\mathbf{AI} \quad &\text{(Eq. 1.37 with $\mathbf A = \mathbf B = \boldsymbol\omega_{B0}$, $\mathbf C = \mathbf{AI}$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{B0}\times\mathbf v_0^A + (\boldsymbol\omega_{B0}\cdot\mathbf{AI})\,\boldsymbol\omega_{B0} - \omega_{B0}^2\,\mathbf{AI} = \mathbf 0}$$
>
> **Units:** $[\mathrm{T^{-1}}][\mathrm{L\,T^{-1}}] = [\mathrm{T^{-2}}][\mathrm L] = [\mathrm{L\,T^{-2}}]$ in every term
> **Meaning:** Eq. 9.9 is satisfied by every point of the axis; the middle term is what distinguishes one of them from another.

> [!derivation] The foot of the perpendicular from A to the axis
> **Law:** choice of $I$ with $\mathbf{AI}$ perpendicular to the angular velocity
> **Source:** Notes.pdf, Eq. 9.10; [Lecture 7, Slide 9]
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0}\cdot\mathbf{AI} &= 0 \quad &\text{(choose $I$ as the foot of the perpendicular from $A$, Fig. 9.3)} \\
> \boldsymbol\omega_{B0}\times\mathbf v_0^A - \omega_{B0}^2\,\mathbf{AI} &= \mathbf 0 \quad &\text{(the middle term of Eq. 9.9 vanishes)} \\
> \mathbf{AI} &= \frac{\boldsymbol\omega_{B0}\times\mathbf v_0^A}{\omega_{B0}^2} \quad &\text{(divide by $\omega_{B0}^2 \neq 0$)} \\
> \mathbf v_0^{I'} &= \mathbf v_0^I + \boldsymbol\omega_{B0}\times(s\,\boldsymbol\omega_{B0}) = \mathbf v_0^I \quad &\text{(any $I'$ with $\mathbf{II'} = s\,\boldsymbol\omega_{B0}$ has the same velocity: the axis)}
> \end{aligned}$$
>
> $$\boxed{\mathbf{AI} = \frac{\boldsymbol\omega_{B0}\times\mathbf v_0^A}{\omega_{B0}^2}}$$
>
> **Units:** $[\mathrm{T^{-1}}][\mathrm{L\,T^{-1}}]/[\mathrm{T^{-2}}] = [\mathrm L]$
> **Meaning:** the axis is the line through $I$ parallel to $\boldsymbol\omega_{B0}$; any other choice $I'$ on it keeps the middle term of Eq. 9.9 and makes the computation longer.

![[attachments/EM-T/t6-iar-foot.svg]]

Remarks of the notes (Notes.pdf, Sec. 9.1.2): the axis can change in time (hence "instantaneous"), and the ruled surfaces it sweeps, seen from $S_0$ and from $S_B$, help to picture the motion; the point $I$ and even the whole axis may lie outside the physical body, but it is still a point of the Euclidean space attached to $S_B$; and the axis depends on the frame from which it is computed.

In the general case the slip speed is not zero. The instantaneous axis of rotation and slip is then the locus of points with minimum velocity: the points whose velocity has no perpendicular part, so that it equals the slip velocity ([Lecture 7, Slide 8]).

> [!derivation] Instantaneous axis of rotation and slip
> **Law:** velocity field with the slip velocity imposed; the slip velocity is parallel to the angular velocity
> **Source:** Notes.pdf, Eq. 9.11; Notes.pdf, Eq. 9.10; [Lecture 7, Slide 9]
>
> $$\begin{aligned}
> \mathbf v_0^I &= \mathbf v_0^A + \boldsymbol\omega_{B0}\times\mathbf{AI} = \mathbf v_{0\parallel} \quad &\text{(the perpendicular part of the velocity of $I$ vanishes)} \\
> \boldsymbol\omega_{B0}\times\mathbf v_0^A + \boldsymbol\omega_{B0}\times(\boldsymbol\omega_{B0}\times\mathbf{AI}) &= \boldsymbol\omega_{B0}\times\mathbf v_{0\parallel} = \mathbf 0 \quad &\text{(cross-multiply by $\boldsymbol\omega_{B0}$; $\mathbf v_{0\parallel}$ is parallel to it)} \\
> \mathbf{AI} &= \frac{\boldsymbol\omega_{B0}\times\mathbf v_0^A}{\omega_{B0}^2} \quad &\text{(same steps as Eq. 9.10 with $\mathbf{AI}$ perpendicular to $\boldsymbol\omega_{B0}$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^I = \mathbf v_{0\parallel},\qquad \mathbf{AI} = \frac{\boldsymbol\omega_{B0}\times\mathbf v_0^A}{\omega_{B0}^2}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ and $[\mathrm L]$
> **Meaning:** the same formula locates the axis with or without slip; with zero slip speed it is just the instantaneous axis of rotation.

The general instantaneous motion of a rigid body is therefore a pure rotation about the instantaneous axis plus a pure translation along it with the slip velocity: a screw, or helical, motion (Notes.pdf, Sec. 9.1.3; [Lecture 7, Slide 8]).

![[attachments/EM-T/t6-screw-field.svg]]

> [!derivation] The screw (helical) velocity field
> **Law:** velocity field from a point $I$ of the axis; magnitude of a vector product of perpendicular vectors
> **Source:** Notes.pdf, Sec. 9.1.3; Notes.pdf, Eq. 9.6; [Lecture 7, Slide 8]
>
> $$\begin{aligned}
> \mathbf v_0^A &= \mathbf v_0^I + \boldsymbol\omega_{B0}\times\mathbf{IA} \quad &\text{(Eq. 9.3 from $I$ to $A$)} \\
> &= \mathbf v_{0\parallel} + \boldsymbol\omega_{B0}\times\mathbf{IA} \quad &\text{(Eq. 9.11)} \\
> \mathbf v_{0\perp}^A &= \boldsymbol\omega_{B0}\times\mathbf{IA} \quad &\text{(compare with Eq. 9.6)} \\
> \lvert\mathbf v_{0\perp}^A\rvert &= \omega_{B0}\,d_A \quad &\text{(choose $I$ as the foot of the perpendicular from $A$: $\mathbf{IA} \perp \boldsymbol\omega_{B0}$, $d_A = \lvert\mathbf{IA}\rvert$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^A = \mathbf v_{0\parallel} + \boldsymbol\omega_{B0}\times\mathbf{IA},\qquad \lvert\mathbf v_{0\perp}^A\rvert = \omega_{B0}\,d_A}$$
>
> **Units:** $[\mathrm{T^{-1}}][\mathrm L] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** in each plane normal to the angular velocity the perpendicular velocities are tangent to circles centred on the axis and grow linearly with the distance to it (Fig. 9.4); on top of them every point has the same slip velocity.

> [!info] Extension: the helix of a steady screw motion
> The notes and slides call the general motion a screw. When the axis is fixed and the angular velocity and slip speed are constant (an assumption added here), each body point describes a helix about the axis; the box below shows it. This is an extension, not course content.

> [!derivation] A body point in steady screw motion describes a helix
> **Law:** position about a fixed axis; time derivative with the chain rule
> **Source:** Notes.pdf, Sec. 9.1.3 (extension)
>
> Take the axis as the line through $I$ along $\mathbf e_\omega$, and two fixed unit vectors $\mathbf e_1$, $\mathbf e_2$ normal to it with $\mathbf e_1\times\mathbf e_2 = \mathbf e_\omega$; $d$ is the distance of the point to the axis.
>
> $$\begin{aligned}
> \mathbf{IA}(t) &= d\cos(\omega t)\,\mathbf e_1 + d\sin(\omega t)\,\mathbf e_2 + v_{0\parallel}\,t\,\mathbf e_\omega \quad &\text{(rotation by $\omega t$ about the axis plus slip $v_{0\parallel}t$)} \\
> \frac{d\mathbf{IA}}{dt} &= -d\,\omega\sin(\omega t)\,\mathbf e_1 + d\,\omega\cos(\omega t)\,\mathbf e_2 + v_{0\parallel}\,\mathbf e_\omega \quad &\text{(chain rule, $\tfrac{d}{dt}\cos(\omega t) = -\omega\sin(\omega t)$)} \\
> \omega\,\mathbf e_\omega\times\left(d\cos(\omega t)\,\mathbf e_1 + d\sin(\omega t)\,\mathbf e_2\right) &= d\,\omega\cos(\omega t)\,\mathbf e_2 - d\,\omega\sin(\omega t)\,\mathbf e_1 \quad &\text{(since $\mathbf e_\omega\times\mathbf e_1 = \mathbf e_2$, $\mathbf e_\omega\times\mathbf e_2 = -\mathbf e_1$)} \\
> \text{pitch} &= v_{0\parallel}\,\frac{2\pi}{\omega} \quad &\text{(advance along the axis during one turn, of duration $2\pi/\omega$)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\mathbf{IA}}{dt} = v_{0\parallel}\,\mathbf e_\omega + \boldsymbol\omega_{B0}\times\mathbf{IA},\qquad \text{pitch} = \frac{2\pi\,v_{0\parallel}}{\omega}}$$
>
> **Units:** pitch $[\mathrm{L\,T^{-1}}][\mathrm T] = [\mathrm L]$
> **Meaning:** the derivative reproduces the screw velocity field, and the trajectory is a circular helix of radius $d$ wound about the axis.

## 4. Worked example: three measurements on a rigid airplane

> [!summary] What you need to know
> - **Data:** the velocities of three points $G$, $A$ and $C$ of an airplane.
> - **Step 1.** Check the data fit a rigid body: equal projections for the three pairs of points.
> - **Step 2.** Write the velocity field from $G$ to $A$ and from $G$ to $C$. One pair alone leaves the angular velocity undetermined; the two together fix it.
> - **Step 3.** Project a velocity on $\boldsymbol\omega_{B0}$ to get the slip, then locate the axis with the formula of Section 3.
> - **Result:** the slip is not zero, so the airplane screws about an axis parallel to $\mathbf i+\mathbf j+\mathbf k$.
>
> $$\boxed{\boldsymbol\omega_{B0} = \mathbf i + \mathbf j + \mathbf k\ \ \mathrm{rad/s},\qquad \mathbf v_{0\parallel} = 2\mathbf i + 2\mathbf j + 2\mathbf k\ \ \mathrm{m/s}}$$
>
> **Slides:** [Lecture 7, Slide 7]; [Lecture 7, Slide 10]

> [!example] Rigid airplane ([Lecture 7, Slides 10-11])
> Three simultaneous measurements are made of the motion of a rigid airplane: the centre of mass $G$, a point $A$ on the wing and a point $C$ on the vertical tail, with the positions and velocities of the table below (basis $\mathcal B_0$, metres and metres per second). Slide 11 is left blank for the classroom solution; the questions answered here are the ones the deck prepares in Slides 7 and 9: the data are checked for compatibility, the angular velocity of the airplane is found, and then the slip velocity and the instantaneous axis of rotation and slip.

| Point | Position (m) | Velocity (m/s) |
| :--- | :--- | :--- |
| $G$ | $\mathbf r_0^G = \mathbf 0$ | $\mathbf v_0^G = 4\mathbf i + 2\mathbf j$ |
| $A$ | $\mathbf r_0^A = -\mathbf i + 2\mathbf j$ | $\mathbf v_0^A = 2\mathbf i + \mathbf j + 3\mathbf k$ |
| $C$ | $\mathbf r_0^C = -4\mathbf i + \mathbf k$ | $\mathbf v_0^C = 5\mathbf i - 3\mathbf j + 4\mathbf k$ |

![[attachments/EM-T/t6-airplane-example.svg]]

> [!derivation] Compatibility: equal projections for the three pairs
> **Law:** equal-projection property of the rigid velocity field
> **Source:** Notes.pdf, Eq. 9.7; [Lecture 7, Slide 7]; [Lecture 7, Slide 10]
>
> $$\begin{aligned}
> \mathbf{GA} &= \mathbf r_0^A - \mathbf r_0^G = (-1,\,2,\,0)\ \mathrm m \quad &\text{(difference of position vectors)} \\
> \mathbf v_0^G\cdot\mathbf{GA} &= 4(-1) + 2(2) + 0(0) = 0,\qquad \mathbf v_0^A\cdot\mathbf{GA} = 2(-1) + 1(2) + 3(0) = 0 \quad &\text{(Eq. 1.40, components in $\mathcal B_0$)} \\
> \mathbf{GC} &= (-4,\,0,\,1)\ \mathrm m \quad &\text{(difference of position vectors)} \\
> \mathbf v_0^G\cdot\mathbf{GC} &= -16 + 0 + 0 = -16,\qquad \mathbf v_0^C\cdot\mathbf{GC} = -20 + 0 + 4 = -16 \quad &\text{(Eq. 1.40)} \\
> \mathbf{AC} &= \mathbf r_0^C - \mathbf r_0^A = (-3,\,-2,\,1)\ \mathrm m \quad &\text{(difference of position vectors)} \\
> \mathbf v_0^A\cdot\mathbf{AC} &= -6 - 2 + 3 = -5,\qquad \mathbf v_0^C\cdot\mathbf{AC} = -15 + 6 + 4 = -5 \quad &\text{(Eq. 1.40)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^G\cdot\mathbf{GA} = \mathbf v_0^A\cdot\mathbf{GA},\quad \mathbf v_0^G\cdot\mathbf{GC} = \mathbf v_0^C\cdot\mathbf{GC},\quad \mathbf v_0^A\cdot\mathbf{AC} = \mathbf v_0^C\cdot\mathbf{AC}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}][\mathrm L]$: $0$, $-16$ and $-5\ \mathrm{m^2/s}$
> **Meaning:** the three measurements are compatible with a rigid body, so an angular velocity that reproduces them exists.

> [!derivation] Velocity field from G to A
> **Law:** velocity field of the rigid body; vector product in components
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 1.42; [Lecture 7, Slide 7]
>
> Unknown: $\boldsymbol\omega_{B0} = \omega_x\mathbf i + \omega_y\mathbf j + \omega_z\mathbf k$.
>
> $$\begin{aligned}
> \mathbf v_0^A - \mathbf v_0^G &= (2-4,\ 1-2,\ 3-0) = (-2,\,-1,\,3)\ \mathrm{m/s} \quad &\text{(left-hand side of Eq. 9.3)} \\
> \boldsymbol\omega_{B0}\times\mathbf{GA} &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr \omega_x & \omega_y & \omega_z \cr -1 & 2 & 0 \end{vmatrix} \quad &\text{(Eq. 1.42)} \\
> &= (\omega_y\cdot 0 - 2\omega_z)\,\mathbf i + (-\omega_z - 0\cdot\omega_x)\,\mathbf j + (2\omega_x + \omega_y)\,\mathbf k \quad &\text{(expand the determinant along its first row)} \\
> -2\omega_z &= -2,\qquad -\omega_z = -1,\qquad 2\omega_x + \omega_y = 3 \quad &\text{(equate components)}
> \end{aligned}$$
>
> $$\boxed{\omega_z = 1\ \mathrm{rad/s},\qquad 2\omega_x + \omega_y = 3\ \mathrm{rad/s}}$$
>
> **Units:** $[\mathrm{T^{-1}}][\mathrm L] = [\mathrm{L\,T^{-1}}]$, so each component of the angular velocity is in $\mathrm{rad/s}$
> **Meaning:** one pair of points fixes the angular velocity only up to its component along $\mathbf{GA}$: the first two equations repeat each other, which is the compatibility of the pair.

> [!derivation] Velocity field from G to C
> **Law:** velocity field of the rigid body; vector product in components
> **Source:** Notes.pdf, Eq. 9.12; Notes.pdf, Eq. 1.42; [Lecture 7, Slide 7]
>
> $$\begin{aligned}
> \mathbf v_0^C - \mathbf v_0^G &= (5-4,\ -3-2,\ 4-0) = (1,\,-5,\,4)\ \mathrm{m/s} \quad &\text{(left-hand side)} \\
> \boldsymbol\omega_{B0}\times\mathbf{GC} &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr \omega_x & \omega_y & \omega_z \cr -4 & 0 & 1 \end{vmatrix} \quad &\text{(Eq. 1.42)} \\
> &= (\omega_y - 0)\,\mathbf i + (-4\omega_z - \omega_x)\,\mathbf j + (0 + 4\omega_y)\,\mathbf k \quad &\text{(expand along the first row)} \\
> \omega_y &= 1,\qquad -4\omega_z - \omega_x = -5,\qquad 4\omega_y = 4 \quad &\text{(equate components)} \\
> \omega_x &= 5 - 4\omega_z = 5 - 4 = 1 \quad &\text{(use $\omega_z = 1$ from the pair $G$, $A$)} \\
> 2\omega_x + \omega_y &= 2 + 1 = 3 \quad &\text{(check of the third equation of the pair $G$, $A$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{B0} = \mathbf i + \mathbf j + \mathbf k\ \ \mathrm{rad/s}}$$
>
> **Units:** $\mathrm{rad/s}$, that is $[\mathrm{T^{-1}}]$
> **Meaning:** the second pair removes the indeterminacy of the first, and every one of the six scalar equations is satisfied: the data are consistent.

> [!derivation] Slip velocity of the airplane
> **Law:** common component of the velocity along the angular velocity
> **Source:** Notes.pdf, Eq. 9.5; Notes.pdf, Eq. 9.6; [Lecture 7, Slide 6]
>
> $$\begin{aligned}
> \omega_{B0} &= \sqrt{1^2+1^2+1^2} = \sqrt 3\ \mathrm{rad/s} \quad &\text{(magnitude)} \\
> \mathbf v_0^G\cdot\boldsymbol\omega_{B0} &= 4 + 2 + 0 = 6,\quad \mathbf v_0^A\cdot\boldsymbol\omega_{B0} = 2+1+3 = 6,\quad \mathbf v_0^C\cdot\boldsymbol\omega_{B0} = 5-3+4 = 6 \quad &\text{(same value for the three points, Eq. 9.5)} \\
> \mathbf v_{0\parallel} &= \frac{\mathbf v_0^G\cdot\boldsymbol\omega_{B0}}{\omega_{B0}^2}\,\boldsymbol\omega_{B0} = \frac{6}{3}(\mathbf i+\mathbf j+\mathbf k) \quad &\text{(projection on $\mathbf e_\omega$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_{0\parallel} = 2\mathbf i + 2\mathbf j + 2\mathbf k\ \mathrm{m/s},\qquad v_{0\parallel} = 2\sqrt 3\ \mathrm{m/s}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}][\mathrm{T^{-1}}]/[\mathrm{T^{-2}}]\cdot[\mathrm{T^{-1}}] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the slip speed is not zero, so the instantaneous motion of the airplane is a genuine screw motion, not a pure rotation.

> [!derivation] Instantaneous axis of rotation and slip of the airplane
> **Law:** foot of the perpendicular from $G$ to the axis
> **Source:** Notes.pdf, Eq. 9.10; Notes.pdf, Eq. 9.11; [Lecture 7, Slide 9]
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0}\times\mathbf v_0^G &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr 1 & 1 & 1 \cr 4 & 2 & 0 \end{vmatrix} = (0-2)\,\mathbf i + (4-0)\,\mathbf j + (2-4)\,\mathbf k \quad &\text{(Eq. 1.42)} \\
> \mathbf{GI} &= \frac{-2\mathbf i + 4\mathbf j - 2\mathbf k}{3} \quad &\text{(Eq. 9.10 with $A$ replaced by $G$, $\omega_{B0}^2 = 3$)} \\
> \boldsymbol\omega_{B0}\times\mathbf{GI} &= \tfrac13\begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr 1 & 1 & 1 \cr -2 & 4 & -2 \end{vmatrix} = \tfrac13\left[(-2-4)\,\mathbf i + (-2+2)\,\mathbf j + (4+2)\,\mathbf k\right] \quad &\text{(check, Eq. 1.42)} \\
> \mathbf v_0^I &= (4\mathbf i + 2\mathbf j) + (-2\mathbf i + 2\mathbf k) = 2\mathbf i + 2\mathbf j + 2\mathbf k \quad &\text{(Eq. 9.3 from $G$ to $I$: equals the slip velocity)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^I = -\tfrac23\,\mathbf i + \tfrac43\,\mathbf j - \tfrac23\,\mathbf k\ \ \mathrm m,\qquad \text{axis: } \mathbf r_0^I + s\,(\mathbf i+\mathbf j+\mathbf k)}$$
>
> **Units:** $[\mathrm{T^{-1}}][\mathrm{L\,T^{-1}}]/[\mathrm{T^{-2}}] = [\mathrm L]$
> **Meaning:** the airplane screws about a line through $I$, about $1.6\ \mathrm m$ from $G$, parallel to $\mathbf i+\mathbf j+\mathbf k$; along it every point moves only with the slip velocity, the minimum speed in the body.

## 5. Points of a rigid body

> [!summary] What you need to know
> - A geometric point $A$ (for example a contact point, or a point sliding over the body) can sit on top of a body point $A(B)$ at one instant.
> - They are at the same place, but they need not have the same velocity: the difference is the velocity of $A$ relative to the body.
> - The velocity and acceleration fields of Section 2 hold only for body points. Never put the velocity of a non-body point into them.
>
> $$\boxed{\mathbf r_0^A = \mathbf r_0^{A(B)},\qquad \mathbf v_0^A \neq \mathbf v_0^{A(B)} \ \text{ unless } \ \mathbf v_B^A = \mathbf 0}$$
>
> **Slides:** [Lecture 7, Slide 5]; Notes.pdf, Eq. 9.14; Notes.pdf, Eq. 9.15

Equations 9.3 and 9.4 hold only when both points are body points: points that move with the body and have zero velocity and acceleration in $S_B$ ([Lecture 7, Slide 5]; Notes.pdf, Sec. 9.1.4). Often a body point is fixed by a geometric condition (the centre of a rectangular plate). Sometimes it must be defined as the body point that instantaneously coincides with a geometric point $A$ that does not belong to the body; the notes write it $A(B)$ and the slides $A(b)$. Both have the same position, but not the same velocity or acceleration.

> [!derivation] A geometric point and the body point on top of it
> **Law:** composition of velocities for $A$ (not a body point) and velocity field for $A(B)$ (a body point)
> **Source:** Notes.pdf, Eq. 9.14; Notes.pdf, Eq. 9.15; Notes.pdf, Eq. 3.26; [Lecture 7, Slide 5]
>
> $$\begin{aligned}
> \mathbf r_0^A &= \mathbf r_0^{A(B)} \quad &\text{(by definition $A(B)$ lies on $A$ at this instant)} \\
> \mathbf v_0^A &= \mathbf v_0^P + \mathbf v_B^A + \boldsymbol\omega_{B0}\times\mathbf{PA} \quad &\text{(Eq. 3.26 with moving frame $S_B$; $A$ may move in $S_B$)} \\
> \mathbf v_0^{A(B)} &= \mathbf v_0^P + \boldsymbol\omega_{B0}\times\mathbf{PA} \quad &\text{(Eq. 9.3: $A(B)$ is a body point, $\mathbf v_B^{A(B)} = \mathbf 0$)} \\
> \mathbf v_0^A - \mathbf v_0^{A(B)} &= \mathbf v_B^A \quad &\text{(subtract the two lines)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^A = \mathbf r_0^{A(B)},\qquad \mathbf v_0^A \neq \mathbf v_0^{A(B)}\ \text{ unless }\ \mathbf v_B^A = \mathbf 0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** plugging the velocity of a non-body point into the field equation is wrong: the difference is exactly the velocity of $A$ relative to the body; the same holds, mutatis mutandis, for the accelerations.

The body point that lies on $A$ changes as the body moves, so $A(B)$ names a different material point at each instant. The notation is used only where ambiguity is possible; in every problem each point must be declared as a body point or not. Points outside the physical body that move rigidly with $S_B$ are also body points (Notes.pdf, Sec. 9.1.4).

## 6. Orthogonal rotation matrices

> [!summary] What you need to know
> - The matrix $[{}_0R_1]$ turns the components of a vector in basis $\mathcal B_1$ into its components in basis $\mathcal B_0$. The vector itself does not move.
> - **How to build it:** column 1 is $\mathbf i_1$ written in $\mathcal B_0$, column 2 is $\mathbf j_1$, column 3 is $\mathbf k_1$.
> - **How to undo it:** transpose it. Its determinant is $1$ because both bases are right-handed.
> - **Several rotations in a row:** multiply the matrices from the first rotation to the last. The order matters.
>
> $$\boxed{[\mathbf b]_0 = [{}_0R_1]\,[\mathbf b]_1,\qquad [{}_1R_0] = [{}_0R_1]^T,\qquad [{}_0R_2] = [{}_0R_1]\,[{}_1R_2]}$$
>
> **Slides:** Notes.pdf, Eq. 1.12; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.16

Since a rigid body is replaced by $S_B$, its attitude is the attitude of the basis $\mathcal B_B$ with respect to $\mathcal B_0$, described by a change of basis matrix (Notes.pdf, Sec. 1.5). This section collects the properties of those matrices that the Euler angles use. The notes state the orthogonality and the unit determinant without proof (Eqs. 1.14 and 1.15); the two boxes below prove them from the orthonormality and the handedness of the bases.

> [!derivation] Change of basis matrix
> **Law:** components of one basis in the other; uniqueness of components
> **Source:** Notes.pdf, Eq. 1.8; Notes.pdf, Eq. 1.12; Notes.pdf, Eq. 1.13
>
> $$\begin{aligned}
> \mathbf i_1 &= \ell_{x1,x0}\,\mathbf i_0 + \ell_{x1,y0}\,\mathbf j_0 + \ell_{x1,z0}\,\mathbf k_0,\ \ \text{and likewise for } \mathbf j_1,\ \mathbf k_1 \quad &\text{(change of basis, Eq. 1.8)} \\
> \mathbf b &= b_{x1}\mathbf i_1 + b_{y1}\mathbf j_1 + b_{z1}\mathbf k_1 \quad &\text{(the same vector written in $\mathcal B_1$, Eq. 1.6)} \\
> b_{x0} &= \ell_{x1,x0}\,b_{x1} + \ell_{y1,x0}\,b_{y1} + \ell_{z1,x0}\,b_{z1},\ \ \text{and likewise for } b_{y0},\ b_{z0} \quad &\text{(substitute Eq. 1.8 and collect the coefficient of $\mathbf i_0$, Eqs. 1.9-1.11)}
> \end{aligned}$$
>
> $$\boxed{[\mathbf b]_0 = [{}_0R_1]\,[\mathbf b]_1,\qquad [{}_0R_1] = \big[\,[\mathbf i_1]_0\ \big|\ [\mathbf j_1]_0\ \big|\ [\mathbf k_1]_0\,\big]}$$
>
> **Units:** the entries are direction cosines, dimensionless $[1]$
> **Meaning:** column $n$ of the matrix is the $n$-th vector of the new basis written in the old one; the vector itself is not moved, only described from another basis.

> [!derivation] The change of basis matrix is orthogonal
> **Law:** orthonormality of $\mathcal B_1$; dot product in components
> **Source:** Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.40
>
> $$\begin{aligned}
> \big([{}_0R_1]^T[{}_0R_1]\big)_{mn} &= [\mathbf u_m]_0^T\,[\mathbf u_n]_0 \quad &\text{(row $m$ of the transpose is column $m$; $\mathbf u_1,\mathbf u_2,\mathbf u_3 = \mathbf i_1,\mathbf j_1,\mathbf k_1$)} \\
> &= \mathbf u_m\cdot\mathbf u_n \quad &\text{(dot product in components, Eq. 1.40)} \\
> &= \delta_{mn} \quad &\text{($\mathcal B_1$ is orthonormal)} \\
> [{}_1R_0] &= [{}_0R_1]^{-1} \quad &\text{(inverse operation, by definition)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1]^T\,[{}_0R_1] = [U],\qquad [{}_1R_0] = [{}_0R_1]^{-1} = [{}_0R_1]^T}$$
>
> **Units:** dimensionless
> **Meaning:** inverting a change of basis costs nothing: transpose the matrix; so the rows of the matrix are the old basis vectors written in the new basis.

> [!derivation] The determinant of a rotation matrix is one
> **Law:** determinant as a triple product; right-handed basis
> **Source:** Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.43
>
> $$\begin{aligned}
> \det[{}_0R_1] &= \det [{}_0R_1]^T = [\mathbf i_1]_0\cdot\big([\mathbf j_1]_0\times[\mathbf k_1]_0\big) \quad &\text{(rows of the transpose are $\mathbf i_1,\mathbf j_1,\mathbf k_1$; Eq. 1.43)} \\
> \mathbf j_1\times\mathbf k_1 &= \mathbf i_1 \quad &\text{($\mathcal B_1$ is right-handed)} \\
> \det[{}_0R_1] &= \mathbf i_1\cdot\mathbf i_1 = 1 \quad &\text{($\mathbf i_1$ is a unit vector)}
> \end{aligned}$$
>
> $$\boxed{\det[{}_0R_1] = 1}$$
>
> **Units:** dimensionless
> **Meaning:** the matrix maps a right-handed basis onto a right-handed basis; a left-handed one would give minus one. With the orthogonality it means $[{}_0R_1]$ is a rotation: it has the eigenvalue one, whose eigenvector is the axis of the equivalent single rotation (Notes.pdf, Sec. 1.5.1).

> [!derivation] Composition of changes of basis
> **Law:** chaining two changes of basis
> **Source:** Notes.pdf, Eq. 1.16; Notes.pdf, Eq. 1.23
>
> $$\begin{aligned}
> [\mathbf b]_0 &= [{}_0R_1]\,[\mathbf b]_1 \quad &\text{(from $\mathcal B_1$ to $\mathcal B_0$)} \\
> [\mathbf b]_1 &= [{}_1R_2]\,[\mathbf b]_2 \quad &\text{(from $\mathcal B_2$ to $\mathcal B_1$)} \\
> [\mathbf b]_0 &= [{}_0R_1]\,[{}_1R_2]\,[\mathbf b]_2 \quad &\text{(substitute the second line into the first)} \\
> \det\big([{}_0R_1][{}_1R_2]\big) &= 1\cdot 1 = 1,\quad \big([{}_0R_1][{}_1R_2]\big)^T[{}_0R_1][{}_1R_2] = [{}_1R_2]^T[U][{}_1R_2] = [U] \quad &\text{(the product is again a rotation matrix)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_2] = [{}_0R_1]\,[{}_1R_2]}$$
>
> **Units:** dimensionless
> **Meaning:** a sequence of rotations is a product of matrices written from the first to the last; the product does not commute, so the order of the rotations matters.

## 7. Euler angles of type 3-1-3

> [!summary] What you need to know
> - Three angles give the attitude of the body. In the 3-1-3 sequence: **precession** $\psi$ about $\mathbf k_0$, then **nutation** $\theta$ about the new axis $\mathbf i_1$ (the line of nodes), then **spin** $\varphi$ about the body axis $\mathbf k_B$.
> - Each turn is a simple rotation with its own $3\times 3$ matrix. The matrix of the body is their product, in that order.
> - The nutation $\theta$ is the angle between $\mathbf k_0$ and $\mathbf k_B$.
> - The angular velocity is the sum of the three angle rates, each along its own axis. Write the three in one basis before adding them.
>
> $$\boxed{[{}_0R_B] = [{}_0R_1(z,\psi)]\,[{}_1R_2(x,\theta)]\,[{}_2R_B(z,\varphi)],\qquad \boldsymbol\omega_{B0} = \dot\psi\,\mathbf k_0 + \dot\theta\,\mathbf i_1 + \dot\varphi\,\mathbf k_B}$$
>
> **Slides:** [Lecture 7, Slide 12]; Notes.pdf, Eq. 9.19; Notes.pdf, Eq. 9.21

The attitude of $S_B$ with respect to $S_0$ is given by three angles; when they are three successive simple rotations they are called Euler angles (Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]). The standard set is the 3-1-3 sequence of Fig. 9.5: precession about the third axis, nutation about the new first axis, spin about the new third axis. Each simple rotation is drawn looking down its axis, which then points out of the paper, as recommended in Notes.pdf, Sec. 1.5.2.

![[attachments/EM-T/t6-euler-313-psi.svg]]

> [!derivation] Precession: simple rotation about the third axis
> **Law:** simple rotation by $\psi$ about $\mathbf k_0$, positive by the right-hand rule
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 1.20; [Lecture 7, Slide 12]
>
> View with $\mathbf k_0$ out of the paper (⊙), $\mathbf i_0$ to the right and $\mathbf j_0$ up. The positive sense of $\psi$ is counterclockwise in this view (thumb along $\mathbf k_0$, fingers curl from $\mathbf i_0$ towards $\mathbf j_0$).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0 \quad &\text{(right triangle with hypotenuse $\lvert\mathbf i_1\rvert = 1$: adjacent leg along $\mathbf i_0$, opposite leg along $\mathbf j_0$)} \\
> \mathbf j_1 &= -\sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf j_0 \quad &\text{($\mathbf j_0$ turned counterclockwise leans towards $-\mathbf i_0$: opposite leg $\sin\psi$ along $-\mathbf i_0$)} \\
> \mathbf k_1 &= \mathbf k_0 \quad &\text{(the rotation axis does not move)} \\
> \det[{}_0R_1] &= \cos^2\psi + \sin^2\psi = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\psi+\sin^2\psi & \cos\psi\sin\psi-\sin\psi\cos\psi & 0 \cr \sin\psi\cos\psi-\cos\psi\sin\psi & \sin^2\psi+\cos^2\psi & 0 \cr 0 & 0 & 1\end{bmatrix} = [U] \quad &\text{(row by row products)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1(z,\psi)] = \begin{bmatrix} \cos\psi & -\sin\psi & 0 \\ \sin\psi & \cos\psi & 0 \\ 0 & 0 & 1 \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** the columns are $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$; the only minus sign sits where the rotated second axis acquires a component along the negative first axis.

![[attachments/EM-T/t6-euler-313-theta.svg]]

> [!derivation] Nutation: simple rotation about the new first axis
> **Law:** simple rotation by $\theta$ about $\mathbf i_1$, positive by the right-hand rule
> **Source:** Notes.pdf, Eq. 9.17; Notes.pdf, Eq. 1.18; [Lecture 7, Slide 12]
>
> View with $\mathbf i_1$ out of the paper (⊙), $\mathbf j_1$ to the right and $\mathbf k_1$ up (since $\mathbf j_1\times\mathbf k_1 = \mathbf i_1$). Positive $\theta$ is counterclockwise.
>
> $$\begin{aligned}
> \mathbf i_2 &= \mathbf i_1 \quad &\text{(the rotation axis does not move)} \\
> \mathbf j_2 &= \cos\theta\,\mathbf j_1 + \sin\theta\,\mathbf k_1 \quad &\text{(hypotenuse $1$; adjacent leg along $\mathbf j_1$, opposite leg along $\mathbf k_1$)} \\
> \mathbf k_2 &= -\sin\theta\,\mathbf j_1 + \cos\theta\,\mathbf k_1 \quad &\text{($\mathbf k_1$ turned counterclockwise leans towards $-\mathbf j_1$)} \\
> \det[{}_1R_2] &= \cos^2\theta + \sin^2\theta = 1 \quad &\text{(expand along the first row)} \\
> \mathbf j_2\cdot\mathbf k_2 &= -\cos\theta\sin\theta + \sin\theta\cos\theta = 0 \quad &\text{(columns orthogonal; each has unit norm)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_2(x,\theta)] = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** the nutation tilts the third axis away from $\mathbf k_0$ by the angle $\theta$ about the line of nodes $\mathbf i_1$.

![[attachments/EM-T/t6-euler-313-phi.svg]]

> [!derivation] Spin: simple rotation about the new third axis
> **Law:** simple rotation by $\varphi$ about $\mathbf k_2$, positive by the right-hand rule
> **Source:** Notes.pdf, Eq. 9.18; Notes.pdf, Eq. 1.20; [Lecture 7, Slide 12]
>
> View with $\mathbf k_2$ out of the paper (⊙), $\mathbf i_2$ to the right and $\mathbf j_2$ up. Positive $\varphi$ is counterclockwise.
>
> $$\begin{aligned}
> \mathbf i_B &= \cos\varphi\,\mathbf i_2 + \sin\varphi\,\mathbf j_2 \quad &\text{(hypotenuse $1$; adjacent leg along $\mathbf i_2$, opposite leg along $\mathbf j_2$)} \\
> \mathbf j_B &= -\sin\varphi\,\mathbf i_2 + \cos\varphi\,\mathbf j_2 \quad &\text{($\mathbf j_2$ turned counterclockwise leans towards $-\mathbf i_2$)} \\
> \mathbf k_B &= \mathbf k_2 \quad &\text{(the rotation axis does not move)} \\
> \det[{}_2R_B] &= \cos^2\varphi + \sin^2\varphi = 1 \quad &\text{(expand along the third row)}
> \end{aligned}$$
>
> $$\boxed{[{}_2R_B(z,\varphi)] = \begin{bmatrix} \cos\varphi & -\sin\varphi & 0 \\ \sin\varphi & \cos\varphi & 0 \\ 0 & 0 & 1 \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** the spin turns the body about its own symmetry-like axis $\mathbf k_B$; the matrix has the same form as the precession one.

> [!derivation] Composed matrix of the 3-1-3 sequence
> **Law:** composition of changes of basis; matrix product row by column
> **Source:** Notes.pdf, Eq. 9.19; Notes.pdf, Eq. 1.16
>
> Abbreviations: $c_\psi$ and $s_\psi$ stand for the cosine and sine of $\psi$, and likewise for $\theta$ and $\varphi$.
>
> $$\begin{aligned}
> [{}_0R_2] &= [{}_0R_1][{}_1R_2] = \begin{bmatrix} c_\psi & -s_\psi c_\theta & s_\psi s_\theta \cr s_\psi & c_\psi c_\theta & -c_\psi s_\theta \cr 0 & s_\theta & c_\theta \end{bmatrix} \quad &\text{(Eq. 1.16; e.g. entry (1,3) is $c_\psi\cdot 0 + (-s_\psi)(-s_\theta) + 0\cdot c_\theta$)} \\
> [{}_0R_B] &= [{}_0R_2][{}_2R_B] \quad &\text{(Eq. 1.16 again)} \\
> &= \begin{bmatrix} c_\psi c_\varphi - s_\psi c_\theta s_\varphi & -c_\psi s_\varphi - s_\psi c_\theta c_\varphi & s_\psi s_\theta \cr s_\psi c_\varphi + c_\psi c_\theta s_\varphi & -s_\psi s_\varphi + c_\psi c_\theta c_\varphi & -c_\psi s_\theta \cr s_\theta s_\varphi & s_\theta c_\varphi & c_\theta \end{bmatrix} \quad &\text{(column 1 is $c_\varphi$ col 1 $+ s_\varphi$ col 2; column 2 is $-s_\varphi$ col 1 $+ c_\varphi$ col 2; column 3 unchanged)} \\
> \det[{}_0R_B] &= 1\cdot 1\cdot 1 = 1 \quad &\text{(determinant of a product)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_B] = [{}_0R_1(z,\psi)]\cdot[{}_1R_2(x,\theta)]\cdot[{}_2R_B(z,\varphi)]}$$
>
> **Units:** dimensionless
> **Meaning:** the third column gives the body axis in the fixed basis, with $\mathbf k_B\cdot\mathbf k_0 = \cos\theta$: the nutation is the angle between the two third axes.

> [!derivation] Inverse of the composed matrix
> **Law:** orthogonality; transpose of a product
> **Source:** Notes.pdf, Eq. 9.20; Notes.pdf, Eq. 1.14
>
> $$\begin{aligned}
> [{}_BR_0] &= [{}_0R_B]^{-1} = [{}_0R_B]^T \quad &\text{(Eq. 1.14)} \\
> &= \big([{}_0R_1][{}_1R_2][{}_2R_B]\big)^T \quad &\text{(Eq. 9.19)} \\
> &= [{}_2R_B]^T[{}_1R_2]^T[{}_0R_1]^T \quad &\text{(the transpose of a product reverses the order)}
> \end{aligned}$$
>
> $$\boxed{[{}_BR_0] = [{}_2R_B(z,\varphi)]^T\cdot[{}_1R_2(x,\theta)]^T\cdot[{}_0R_1(z,\psi)]^T}$$
>
> **Units:** dimensionless
> **Meaning:** to pass components from $\mathcal B_0$ to $\mathcal B_B$ undo the rotations in reverse order, each by its transpose (the same matrix with the opposite angle).

The angular velocity follows from the additivity of angular velocities, Eq. 3.14 (Notes.pdf, Sec. 9.2). Each simple rotation contributes the rate of its angle along its own axis; the first box shows why, for the precession.

> [!derivation] Angular velocity of a simple rotation
> **Law:** time derivative of the basis vectors with the chain rule; Poisson formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 1.63
>
> $$\begin{aligned}
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \frac{d}{dt}\left(\cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0\right) = -\sin\psi\,\dot\psi\,\mathbf i_0 + \cos\psi\,\dot\psi\,\mathbf j_0 \quad &\text{(chain rule; $\mathbf i_0,\mathbf j_0$ fixed in $S_0$)} \\
> &= \dot\psi\,\mathbf j_1 \quad &\text{(Eq. 9.16)} \\
> \dot\psi\,\mathbf k_0\times\mathbf i_1 &= \dot\psi\,\mathbf k_1\times\mathbf i_1 = \dot\psi\,\mathbf j_1 \quad &\text{($\mathbf k_1 = \mathbf k_0$; right-handed $\mathcal B_1$)} \\
> \left.\frac{d\mathbf j_1}{dt}\right|_0 &= -\cos\psi\,\dot\psi\,\mathbf i_0 - \sin\psi\,\dot\psi\,\mathbf j_0 = -\dot\psi\,\mathbf i_1 = \dot\psi\,\mathbf k_0\times\mathbf j_1 \quad &\text{(chain rule; $\mathbf k_1\times\mathbf j_1 = -\mathbf i_1$)} \\
> \left.\frac{d\mathbf k_1}{dt}\right|_0 &= \mathbf 0 = \dot\psi\,\mathbf k_0\times\mathbf k_1 \quad &\text{($\mathbf k_1 = \mathbf k_0$ is constant)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \dot\psi\,\mathbf k_0}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** the three Poisson formulas $d\mathbf u/dt = \boldsymbol\omega_{10}\times\mathbf u$ hold with this vector; in the same way the nutation gives $\dot\theta\,\mathbf i_1$ and the spin $\dot\varphi\,\mathbf k_B$.

> [!derivation] Angular velocity of the body from the Euler angle rates
> **Law:** additivity of angular velocities
> **Source:** Notes.pdf, Eq. 9.21; Notes.pdf, Eq. 3.14
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0} &= \boldsymbol\omega_{B2} + \boldsymbol\omega_{20} \quad &\text{(Eq. 3.14 with the intermediate frame $S_2$)} \\
> \boldsymbol\omega_{20} &= \boldsymbol\omega_{21} + \boldsymbol\omega_{10} \quad &\text{(Eq. 3.14 with the intermediate frame $S_1$)} \\
> \boldsymbol\omega_{10} &= \dot\psi\,\mathbf k_0,\quad \boldsymbol\omega_{21} = \dot\theta\,\mathbf i_1,\quad \boldsymbol\omega_{B2} = \dot\varphi\,\mathbf k_B \quad &\text{(simple rotations about their own axes)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{B0} = \boldsymbol\omega_{B2} + \boldsymbol\omega_{21} + \boldsymbol\omega_{10} = \dot\varphi\,\mathbf k_B + \dot\theta\,\mathbf i_1 + \dot\psi\,\mathbf k_0}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ in every term
> **Meaning:** the angular velocity is the vector sum of the three rates, each along a different axis of a different basis; before computing with it, all terms must be written in one basis.

> [!derivation] Body components of the angular velocity
> **Law:** inverse changes of basis of Eqs. 9.17 and 9.18
> **Source:** Notes.pdf, Eq. 9.22; Notes.pdf, Eq. 9.23; Notes.pdf, Eq. 9.24
>
> $$\begin{aligned}
> \mathbf i_2 &= \cos\varphi\,\mathbf i_B - \sin\varphi\,\mathbf j_B,\qquad \mathbf j_2 = \sin\varphi\,\mathbf i_B + \cos\varphi\,\mathbf j_B \quad &\text{(rows of $[{}_2R_B]$, i.e. columns of its transpose)} \\
> \mathbf i_1 &= \mathbf i_2 = \cos\varphi\,\mathbf i_B - \sin\varphi\,\mathbf j_B \quad &\text{(Eq. 9.17: $\mathbf i_2 = \mathbf i_1$)} \\
> \mathbf k_1 &= \sin\theta\,\mathbf j_2 + \cos\theta\,\mathbf k_2 \quad &\text{(third row of $[{}_1R_2]$)} \\
> \mathbf k_0 &= \mathbf k_1 = \sin\theta\sin\varphi\,\mathbf i_B + \sin\theta\cos\varphi\,\mathbf j_B + \cos\theta\,\mathbf k_B \quad &\text{(substitute $\mathbf j_2$ and $\mathbf k_2 = \mathbf k_B$)} \\
> \boldsymbol\omega_{B0} &= \dot\varphi\,\mathbf k_B + \dot\theta(\cos\varphi\,\mathbf i_B - \sin\varphi\,\mathbf j_B) + \dot\psi(\sin\theta\sin\varphi\,\mathbf i_B + \sin\theta\cos\varphi\,\mathbf j_B + \cos\theta\,\mathbf k_B) \quad &\text{(substitute in Eq. 9.21)}
> \end{aligned}$$
>
> $$\boxed{\omega_{B0,x_B} = \dot\theta\cos\varphi + \dot\psi\sin\theta\sin\varphi,\quad \omega_{B0,y_B} = -\dot\theta\sin\varphi + \dot\psi\sin\theta\cos\varphi,\quad \omega_{B0,z_B} = \dot\varphi + \dot\psi\cos\theta}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** these are the components a gyroscope fixed on the body would measure; for zero nutation the first two vanish and the third is the sum of precession and spin rates.

> [!derivation] Angular acceleration from the body components
> **Law:** the angular acceleration is the same derivative in $S_0$ and in $S_B$; product and chain rules
> **Source:** Notes.pdf, Eq. 3.9; Notes.pdf, Sec. 9.2
>
> $$\begin{aligned}
> \boldsymbol\alpha_{B0} &= \left.\frac{d\boldsymbol\omega_{B0}}{dt}\right|_0 = \left.\frac{d\boldsymbol\omega_{B0}}{dt}\right|_B + \boldsymbol\omega_{B0}\times\boldsymbol\omega_{B0} = \left.\frac{d\boldsymbol\omega_{B0}}{dt}\right|_B \quad &\text{(Coriolis theorem, Eq. 3.8; the vector product vanishes)} \\
> \frac{d}{dt}(\dot\theta\cos\varphi + \dot\psi\sin\theta\sin\varphi) &= \ddot\theta\cos\varphi - \dot\theta\dot\varphi\sin\varphi + \ddot\psi\sin\theta\sin\varphi + \dot\psi\dot\theta\cos\theta\sin\varphi + \dot\psi\dot\varphi\sin\theta\cos\varphi \quad &\text{(product rule; chain rule on each sine and cosine)} \\
> \frac{d}{dt}(-\dot\theta\sin\varphi + \dot\psi\sin\theta\cos\varphi) &= -\ddot\theta\sin\varphi - \dot\theta\dot\varphi\cos\varphi + \ddot\psi\sin\theta\cos\varphi + \dot\psi\dot\theta\cos\theta\cos\varphi - \dot\psi\dot\varphi\sin\theta\sin\varphi \quad &\text{(product and chain rules)} \\
> \frac{d}{dt}(\dot\varphi + \dot\psi\cos\theta) &= \ddot\varphi + \ddot\psi\cos\theta - \dot\psi\dot\theta\sin\theta \quad &\text{(product and chain rules)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\alpha_{B0} = \dot\omega_{B0,x_B}\,\mathbf i_B + \dot\omega_{B0,y_B}\,\mathbf j_B + \dot\omega_{B0,z_B}\,\mathbf k_B}$$
>
> **Units:** $[\mathrm{T^{-2}}]$ in every term
> **Meaning:** only for the angular velocity of $S_B$ itself may the body components be differentiated directly; in any other moving frame the Coriolis theorem adds a term.

## 8. Other Euler sequences, singularities and equivalent sets

> [!summary] What you need to know
> - Aircraft use the 3-2-1 sequence: **yaw** $\psi$ about $\mathbf k_0$, **pitch** $\theta$ about the new axis $\mathbf j_1$, **roll** $\varphi$ about the nose axis $\mathbf i_B$.
> - In the matrix of a rotation about the second axis, the minus sign moves below the diagonal.
> - Every set of three angles has attitudes where two of its rotations turn about the same line, and only their sum or difference is defined. For 3-1-3 this happens at $\theta$ equal to $0$ or $\pi$; for yaw, pitch and roll at a pitch of a right angle (nose straight up or down).
> - The same attitude can be described by more than one set of angles.
>
> $$\boxed{[{}_1R_2(y,\theta)] = \begin{bmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{bmatrix}}$$
>
> **Slides:** [Lecture 7, Slide 12]; Notes.pdf, Sec. 9.2.1; Notes.pdf, Sec. 9.2.2

Twelve sequences are possible, with the only rule that two successive rotations are never about the same axis (Notes.pdf, Sec. 9.2.1):

| First axis 1 | First axis 2 | First axis 3 |
| :--- | :--- | :--- |
| 1-2-1, 1-2-3, 1-3-1, 1-3-2 | 2-1-2, 2-1-3, 2-3-1, 2-3-2 | 3-1-2, 3-1-3, 3-2-1, 3-2-3 |

| Use | Sequence | First angle | Second angle | Third angle |
| :--- | :--- | :--- | :--- | :--- |
| Standard (notes) | 3-1-3 | precession $\psi$ | nutation $\theta$ | spin $\varphi$ |
| Orbit of a satellite in an Earth-centred inertial equatorial frame | 3-1-3 | right ascension of the ascending node $\Omega$ | inclination $i$ | argument of the pericentre $\omega$ |
| Flight Mechanics | 3-2-1 | yaw $\psi$ (guiñada) | pitch $\theta$ (cabeceo) | roll $\varphi$ (alabeo) |

The notes only name the 3-2-1 sequence. Its matrices follow directly from the simple rotations of Eqs. 1.18 to 1.20, as below: the yaw is the same rotation as the precession (Eq. 9.16, same view), the pitch is about the new second axis and the roll about the new first axis.

![[attachments/EM-T/t6-euler-321-theta.svg]]

> [!derivation] Pitch: simple rotation about the new second axis
> **Law:** simple rotation by $\theta$ about $\mathbf j_1$, positive by the right-hand rule
> **Source:** Notes.pdf, Eq. 1.19; Notes.pdf, Sec. 9.2.1
>
> View with $\mathbf j_1$ out of the paper (⊙), $\mathbf k_1$ to the right and $\mathbf i_1$ up (since $\mathbf k_1\times\mathbf i_1 = \mathbf j_1$). Positive $\theta$ is counterclockwise, turning $\mathbf k_1$ towards $\mathbf i_1$.
>
> $$\begin{aligned}
> \mathbf k_2 &= \cos\theta\,\mathbf k_1 + \sin\theta\,\mathbf i_1 \quad &\text{(hypotenuse $1$; adjacent leg along $\mathbf k_1$, opposite leg along $\mathbf i_1$)} \\
> \mathbf i_2 &= \cos\theta\,\mathbf i_1 - \sin\theta\,\mathbf k_1 \quad &\text{($\mathbf i_1$, pointing up, turned counterclockwise leans towards $-\mathbf k_1$)} \\
> \mathbf j_2 &= \mathbf j_1 \quad &\text{(the rotation axis does not move)} \\
> \det[{}_1R_2] &= \cos\theta\cos\theta - \sin\theta(-\sin\theta) = 1 \quad &\text{(expand along the second row)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_2(y,\theta)] = \begin{bmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** for a rotation about the second axis the minus sign moves below the diagonal, because the cyclic order is $z \to x$ (the pair $\mathbf k_1$, $\mathbf i_1$ is the right-handed pair in this view); a positive pitch turns the first axis towards the negative third axis, which is nose-up in aircraft axes, where the third axis points down.

![[attachments/EM-T/t6-euler-321-phi.svg]]

> [!derivation] Roll: simple rotation about the new first axis and composed 3-2-1 matrix
> **Law:** simple rotation by $\varphi$ about $\mathbf i_2$; composition of changes of basis
> **Source:** Notes.pdf, Eq. 1.18; Notes.pdf, Eq. 1.16; Notes.pdf, Sec. 9.2.1
>
> View with $\mathbf i_2$ out of the paper (⊙), $\mathbf j_2$ to the right and $\mathbf k_2$ up. With the abbreviations of the 3-1-3 box:
>
> $$\begin{aligned}
> \mathbf j_B &= c_\varphi\,\mathbf j_2 + s_\varphi\,\mathbf k_2,\qquad \mathbf k_B = -s_\varphi\,\mathbf j_2 + c_\varphi\,\mathbf k_2,\qquad \mathbf i_B = \mathbf i_2 \quad &\text{(same triangles as the nutation, Eq. 9.17)} \\
> [{}_0R_1][{}_1R_2] &= \begin{bmatrix} c_\psi c_\theta & -s_\psi & c_\psi s_\theta \cr s_\psi c_\theta & c_\psi & s_\psi s_\theta \cr -s_\theta & 0 & c_\theta \end{bmatrix} \quad &\text{(row by column product of Eq. 9.16 and the pitch matrix)} \\
> [{}_0R_B] &= [{}_0R_1][{}_1R_2][{}_2R_B(x,\varphi)] = \begin{bmatrix} c_\psi c_\theta & -s_\psi c_\varphi + c_\psi s_\theta s_\varphi & s_\psi s_\varphi + c_\psi s_\theta c_\varphi \cr s_\psi c_\theta & c_\psi c_\varphi + s_\psi s_\theta s_\varphi & -c_\psi s_\varphi + s_\psi s_\theta c_\varphi \cr -s_\theta & c_\theta s_\varphi & c_\theta c_\varphi \end{bmatrix} \quad &\text{(column 2 is $c_\varphi$ col 2 $+ s_\varphi$ col 3; column 3 is $-s_\varphi$ col 2 $+ c_\varphi$ col 3)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_B]_{3\text{-}2\text{-}1} = [{}_0R_1(z,\psi)]\cdot[{}_1R_2(y,\theta)]\cdot[{}_2R_B(x,\varphi)]}$$
>
> **Units:** dimensionless
> **Meaning:** the first column is the body axis $\mathbf i_B$ (the nose) in $\mathcal B_0$: its heading is the yaw and its elevation out of the $x_0 y_0$ plane is fixed by the pitch alone.

> [!info] Extension: body components of the angular velocity for yaw, pitch and roll
> The notes give the body components only for the 3-1-3 sequence (Eqs. 9.22 to 9.24). The same steps applied to the 3-2-1 sequence give the box below; it is an extension.

> [!derivation] Angular velocity in body axes for the 3-2-1 sequence
> **Law:** additivity of angular velocities; inverse changes of basis
> **Source:** Notes.pdf, Eq. 3.14; Notes.pdf, Eq. 9.21 (extension to the 3-2-1 sequence)
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0} &= \dot\varphi\,\mathbf i_B + \dot\theta\,\mathbf j_1 + \dot\psi\,\mathbf k_0 \quad &\text{(Eq. 3.14: roll about $\mathbf i_2 = \mathbf i_B$, pitch about $\mathbf j_1$, yaw about $\mathbf k_0$)} \\
> \mathbf j_1 &= \mathbf j_2 = c_\varphi\,\mathbf j_B - s_\varphi\,\mathbf k_B \quad &\text{(second row of $[{}_2R_B(x,\varphi)]$)} \\
> \mathbf k_0 &= \mathbf k_1 = -s_\theta\,\mathbf i_2 + c_\theta\,\mathbf k_2 \quad &\text{(third row of the pitch matrix)} \\
> \mathbf k_2 &= s_\varphi\,\mathbf j_B + c_\varphi\,\mathbf k_B \quad &\text{(third row of $[{}_2R_B(x,\varphi)]$)} \\
> \boldsymbol\omega_{B0} &= (\dot\varphi - \dot\psi s_\theta)\,\mathbf i_B + (\dot\theta c_\varphi + \dot\psi c_\theta s_\varphi)\,\mathbf j_B + (-\dot\theta s_\varphi + \dot\psi c_\theta c_\varphi)\,\mathbf k_B \quad &\text{(substitute and collect)}
> \end{aligned}$$
>
> $$\boxed{\omega_{x_B} = \dot\varphi - \dot\psi\sin\theta,\quad \omega_{y_B} = \dot\theta\cos\varphi + \dot\psi\cos\theta\sin\varphi,\quad \omega_{z_B} = -\dot\theta\sin\varphi + \dot\psi\cos\theta\cos\varphi}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** with all angles small the body rates reduce to the three angle rates; at a pitch of a right angle the yaw and roll rates enter only through their difference, which is the singularity below.

Every choice of Euler angles has singular attitudes: when the second rotation aligns the first and third rotation axes, the first and third angles are not defined separately, only their sum or difference (Notes.pdf, Sec. 9.2.2; [Lecture 7, Slide 12]). The definition is chosen so that the singularity is rarely met (an aircraft is seldom completely nose-up or nose-down); it is the "gimbal lock" of three-gimbal systems. Quaternions avoid it but are beyond the course.

> [!derivation] Singularity of the 3-1-3 angles
> **Law:** composed matrix at zero nutation; addition formulas
> **Source:** Notes.pdf, Sec. 9.2.2; Notes.pdf, Eq. 9.19; [Lecture 7, Slide 12]
>
> $$\begin{aligned}
> [{}_1R_2(x,0)] &= [U] \quad &\text{(cosine one, sine zero)} \\
> [{}_0R_B] &= [{}_0R_1(z,\psi)][{}_2R_B(z,\varphi)] = \begin{bmatrix} c_\psi c_\varphi - s_\psi s_\varphi & -c_\psi s_\varphi - s_\psi c_\varphi & 0 \cr s_\psi c_\varphi + c_\psi s_\varphi & -s_\psi s_\varphi + c_\psi c_\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(row by column product)} \\
> &= [{}_0R_B(z,\psi+\varphi)] \quad &\text{(cosine and sine of a sum)} \\
> [{}_0R_1(z,\psi)]\,\mathrm{diag}(1,-1,-1)\,[{}_2R_B(z,\varphi)] &= \begin{bmatrix} \cos(\psi-\varphi) & \sin(\psi-\varphi) & 0 \cr \sin(\psi-\varphi) & -\cos(\psi-\varphi) & 0 \cr 0 & 0 & -1 \end{bmatrix} \quad &\text{(nutation $\pi$: only the difference survives)}
> \end{aligned}$$
>
> $$\boxed{\theta = 0:\ [{}_0R_B] = [{}_0R_1(z,\psi+\varphi)],\qquad \theta = \pi:\ [{}_0R_B] \text{ depends only on } \psi-\varphi}$$
>
> **Units:** dimensionless
> **Meaning:** with the nutation at zero or a half turn the first and third axes coincide, so precession and spin rotate about the same line and cannot be separated.

> [!derivation] Singularity of the yaw, pitch and roll angles
> **Law:** composed 3-2-1 matrix at a pitch of a right angle; difference formulas
> **Source:** Notes.pdf, Sec. 9.2.2
>
> $$\begin{aligned}
> c_\theta &= 0,\qquad s_\theta = 1 \quad &\text{(pitch of a right angle)} \\
> -s_\psi c_\varphi + c_\psi s_\varphi &= \sin(\varphi-\psi),\qquad s_\psi s_\varphi + c_\psi c_\varphi = \cos(\varphi-\psi) \quad &\text{(sine and cosine of a difference)} \\
> [{}_0R_B] &= \begin{bmatrix} 0 & \sin(\varphi-\psi) & \cos(\varphi-\psi) \cr 0 & \cos(\varphi-\psi) & -\sin(\varphi-\psi) \cr -1 & 0 & 0 \end{bmatrix} \quad &\text{(substitute in the composed 3-2-1 matrix)}
> \end{aligned}$$
>
> $$\boxed{\theta = \tfrac{\pi}{2}:\ [{}_0R_B] \text{ depends only on } \varphi - \psi}$$
>
> **Units:** dimensionless
> **Meaning:** nose straight up (or down, for a pitch of three right angles): yaw and roll turn about the same vertical line and only their difference is defined.

Any attitude also has several equivalent sets of Euler angles ([Lecture 7, Slide 12]). The slide illustrates this for the 3-1-3 sequence with a pair of sets; the second set of that pair, as printed, does not give the same attitude.

> [!warning] Erratum in the source
> [Lecture 7, Slide 12] gives the sets with precession $\pi/2$, nutation $\pi/2$, spin $0$ and with precession $-\pi/2$, nutation $\pi/2$, spin $\pi$ as the same attitude. The box below shows they are different attitudes; the set equivalent to the first is precession $-\pi/2$, nutation $-\pi/2$, spin $\pi$ (the general rule adds a half turn to the first and third angles and changes the sign of the nutation). The note keeps the corrected set.

> [!derivation] Check of the equivalent 3-1-3 sets of Slide 12
> **Law:** third and first columns of the composed 3-1-3 matrix
> **Source:** Notes.pdf, Eq. 9.19; [Lecture 7, Slide 12]
>
> $$\begin{aligned}
> [\mathbf k_B]_0 &= (s_\psi s_\theta,\ -c_\psi s_\theta,\ c_\theta) \quad &\text{(third column of Eq. 9.19)} \\
> (\tfrac{\pi}{2},\tfrac{\pi}{2},0):\ [\mathbf k_B]_0 &= (1,\,0,\,0),\qquad (-\tfrac{\pi}{2},\tfrac{\pi}{2},\pi):\ [\mathbf k_B]_0 = (-1,\,0,\,0) \quad &\text{(substitute: the printed sets differ)} \\
> (-\tfrac{\pi}{2},-\tfrac{\pi}{2},\pi):\ [\mathbf k_B]_0 &= \big((-1)(-1),\ -0\cdot(-1),\ 0\big) = (1,\,0,\,0) \quad &\text{(corrected set: same third axis)} \\
> [\mathbf i_B]_0 &= (c_\psi c_\varphi - s_\psi c_\theta s_\varphi,\ s_\psi c_\varphi + c_\psi c_\theta s_\varphi,\ s_\theta s_\varphi) \quad &\text{(first column of Eq. 9.19)} \\
> (\tfrac{\pi}{2},\tfrac{\pi}{2},0):\ [\mathbf i_B]_0 &= (0,\,1,\,0),\qquad (-\tfrac{\pi}{2},-\tfrac{\pi}{2},\pi):\ [\mathbf i_B]_0 = \big(0,\ (-1)(-1),\ 0\big) = (0,\,1,\,0) \quad &\text{(same first axis)}
> \end{aligned}$$
>
> $$\boxed{(\psi,\theta,\varphi) = \left(\tfrac{\pi}{2},\tfrac{\pi}{2},0\right)\ \equiv\ \left(-\tfrac{\pi}{2},-\tfrac{\pi}{2},\pi\right)}$$
>
> **Units:** dimensionless
> **Meaning:** two bases with the same first and third vectors have the same second one ($\mathbf j_B = \mathbf k_B\times\mathbf i_B$), so the corrected sets describe one attitude; the printed second set turns the body axis to the opposite side.

## 9. Degrees of freedom of a rigid body

> [!summary] What you need to know
> - A free rigid body needs six numbers to place it: three for the position of one of its points and three angles for its attitude.
> - Rigidity removes every other coordinate of its particles: once the six are known, the position of every point is known.
>
> $$\boxed{\text{free rigid body: } 3 \text{ coordinates} + 3 \text{ angles} = 6 \text{ degrees of freedom}}$$
>
> **Slides:** [Lecture 7, Slide 13]; Notes.pdf, Sec. 9.3

The motion of a rigid body is the translation of one body point plus a rotation about it (Eq. 9.3). Without constraints the point needs three coordinates (commonly the centre of mass $G$, defined in Section 11) and the attitude three more, such as the Euler angles (Notes.pdf, Sec. 9.3; [Lecture 7, Slide 13]).

> [!derivation] Six degrees of freedom of a free rigid body
> **Law:** counting coordinates minus independent rigidity constraints
> **Source:** Notes.pdf, Sec. 9.3; [Lecture 7, Slide 3]; [Lecture 7, Slide 13]
>
> $$\begin{aligned}
> 3N &\quad &\text{(coordinates of $N$ point particles, the body seen as a collection of particles)} \\
> 9 - 3 &= 6 \quad &\text{(three non-collinear points: nine coordinates, three fixed mutual distances)} \\
> 3 - 3 &= 0 \quad &\text{(each further point: three coordinates fixed by its three distances to the first three points)} \\
> 3 + 3 &= 6 \quad &\text{(equivalently: position of one point plus three attitude angles)}
> \end{aligned}$$
>
> $$\boxed{\text{free rigid body: } 6 \text{ degrees of freedom}}$$
>
> **Units:** a count, dimensionless
> **Meaning:** the rigidity constraint reduces the $3N$ coordinates of the particles to six; given them the position of every point is known without ambiguity.

> [!key] Solving the kinematics of a rigid body ([Lecture 7, Slide 13])
> A free rigid body is equivalent to a reference frame and has six degrees of freedom. A common choice of coordinates is three for the position of a body point $A$ (later, the centre of mass $G$) and three for the attitude (Euler angles), with $S_B$ defined from them. Solving the kinematics of the body means giving, as functions of the six coordinates and their derivatives, the position, velocity and acceleration of one point, $\mathbf r_0^A$, $\mathbf v_0^A$, $\mathbf a_0^A$; the attitude, $\mathbf i_B$, $\mathbf j_B$, $\mathbf k_B$; and the angular velocity and acceleration, $\boldsymbol\omega_{B0}$, $\boldsymbol\alpha_{B0}$. Other choices may suit a given problem better.


## 10. Mass distributions, their moments and second-order tensors

> [!summary] What you need to know
> - Everything about inertia comes from three integrals of the mass over the body: the **zeroth moment** (a number), the **first moment** (a vector) and the **second moment** (a tensor).
> - The next sections turn them into the total mass, the centre of mass and the tensor of inertia.
> - A second-order tensor is stored as a $3\times 3$ matrix in a basis. Its contraction with two vectors is computed as row, times matrix, times column.
> - To integrate, use the volume element of the coordinates you chose, with its stretching factor: $R$ in cylindrical coordinates, $r^2\cos\phi$ in spherical ones (with $\phi$ the latitude).
>
> $$\boxed{dV = dx\,dy\,dz = R\,dR\,d\theta\,dz = r^2\cos\phi\,dr\,d\theta\,d\phi}$$
>
> **Slides:** [Lecture 8, Slide 3]; [Lecture 8, Slide 8]; Notes.pdf, Eq. 10.1; Notes.pdf, Eq. 10.5

The point particle needs a single inertia property, its mass. A rigid body also keeps its spatial mass distribution $\mathcal D$, which governs its rotational dynamics: a metal bar is harder to set spinning about an axis across it than about its own long axis ([Lecture 8, Slide 7]). The inertia properties defined in this part of the note are the total mass, the centre of mass and the moments, products and tensor of inertia; they are built from the zeroth, first and second moments of the mass distribution and are valid for any material system, rigid or not (Notes.pdf, Sec. 10). A superscript naming the body is added when more than one body is present.

### Second-order tensors and the tensor product

The tensor of inertia is a second-order tensor, so the lecture opens with the few tensor operations it needs ([Lecture 8, Slides 3-6]); the notes collect them in Chapter 1 (Notes.pdf, Eqs. 1.34 to 1.48).

| Object | Meaning |
| :--- | :--- |
| $\mathcal T$ | a second-order tensor: a linear map that, dot-multiplied with a vector, gives a vector, and with a vector on each side gives a scalar |
| $[\mathcal T]_{00}$ | its $3\times 3$ matrix of components in the tensor basis $\mathcal B_0\otimes\mathcal B_0$ |
| $\mathbf u\otimes\mathbf v$ | tensor product (dyad) of two vectors; the slides sometimes omit the symbol and write $\mathbf u\mathbf v$ |
| $\boldsymbol{\mathcal U}$ | unit tensor, identity matrix of components in every orthonormal basis |
| symmetric tensor | a tensor whose component matrix equals its transpose |

> [!derivation] Contractions of a second-order tensor in matrix form
> **Law:** components of vectors and tensors in the basis $\mathcal B_0$; tensor product
> **Source:** [Lecture 8, Slide 3]; [Lecture 8, Slide 4]; Notes.pdf, Eq. 1.36; Notes.pdf, Eq. 1.48
>
> A vector is a column of three components and a tensor a square matrix of nine, both in $\mathcal B_0$.
>
> $$\begin{aligned}
> [\mathcal T\cdot\mathbf b]_0 &= [\mathcal T]_{00}\,[\mathbf b]_0 \quad &\text{(right contraction: matrix times column)} \\
> [\mathbf a\cdot\mathcal T]_0^{T} &= [\mathbf a]_0^{T}\,[\mathcal T]_{00} \quad &\text{(left contraction: row times matrix)} \\
> \mathbf a\cdot\mathcal T\cdot\mathbf b &= [\mathbf a]_0^{T}\,[\mathcal T]_{00}\,[\mathbf b]_0 \quad &\text{(double contraction: a scalar)} \\
> [\mathbf u\otimes\mathbf v]_{00} &= [\mathbf u]_0\,[\mathbf v]_0^{T} = \begin{bmatrix} u_x v_x & u_x v_y & u_x v_z \cr u_y v_x & u_y v_y & u_y v_z \cr u_z v_x & u_z v_y & u_z v_z \end{bmatrix} \quad &\text{(tensor product, column times row, Eq. 1.48)} \\
> \mathbf a\cdot(\mathbf u\otimes\mathbf v)\cdot\mathbf b &= [\mathbf a]_0^{T}[\mathbf u]_0\,[\mathbf v]_0^{T}[\mathbf b]_0 = (\mathbf a\cdot\mathbf u)(\mathbf v\cdot\mathbf b) \quad &\text{(associativity of the matrix product, Eq. 1.36)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a\cdot\mathcal T\cdot\mathbf b = [\mathbf a]_0^{T}[\mathcal T]_{00}[\mathbf b]_0,\qquad \mathbf a\cdot(\mathbf u\otimes\mathbf v)\cdot\mathbf b = (\mathbf a\cdot\mathbf u)(\mathbf v\cdot\mathbf b)}$$
>
> **Units:** the dimension of a contraction is the product of the dimensions of its factors; for a tensor of inertia in $\mathrm{kg\,m^2}$ and two unit vectors the scalar is in $\mathrm{kg\,m^2}$
> **Meaning:** a dyad is a pair of vectors "waiting" for a vector on its left and on its right; the dot is what tells a contraction from a tensor product, so it is never omitted.

The lecture also states the two facts about symmetric tensors that Section 15 uses: their components change basis with the change of basis matrix on both sides ([Lecture 8, Slide 5]), and there is always an orthonormal basis of eigenvectors in which the matrix is diagonal, the principal directions of the tensor ([Lecture 8, Slide 6]).

### Moments of a mass distribution

| Symbol | Meaning |
| :--- | :--- |
| $m_i$, $\mathbf r_0^{P_i}$ | mass and position of the particle $P_i$ of a discrete system, $i$ from $1$ to $N$ |
| $dm$, $\mathbf r_0^{P}$ | mass element of a continuous distribution and position of its integration point $P$ |
| $\lambda$, $\sigma$, $\rho$ | linear ($\mathrm{kg/m}$), area ($\mathrm{kg/m^2}$) and volume ($\mathrm{kg/m^3}$) densities |
| $d\ell$, $dA$, $dV$ | length, area and volume elements |
| homogeneous body | a body whose density is uniform in space |

![[attachments/EM-T/t6-mass-distribution.svg]]

> [!derivation] Zeroth, first and second moments of a mass distribution
> **Law:** definition of the $n$-th moment of a mass distribution about $O$
> **Source:** Notes.pdf, Eq. 10.1; Notes.pdf, Eq. 10.2; Notes.pdf, Eq. 10.3; Notes.pdf, Eq. 10.4; [Lecture 8, Slide 8]
>
> $$\begin{aligned}
> \mathcal M_{O,n}^{\mathcal D} &= \sum_{i=1}^{N} \underbrace{\mathbf r_0^{P_i}\otimes\mathbf r_0^{P_i}\otimes\cdots\otimes\mathbf r_0^{P_i}}_{n}\,m_i \quad &\text{(discrete system, Eq. 10.1)} \\
> \mathcal M_{O,0}^{\mathcal D} &= \sum_{i=1}^{N} m_i,\quad \mathcal M_{O,1}^{\mathcal D} = \sum_{i=1}^{N} \mathbf r_0^{P_i}\,m_i,\quad \mathcal M_{O,2}^{\mathcal D} = \sum_{i=1}^{N} \mathbf r_0^{P_i}\otimes\mathbf r_0^{P_i}\,m_i \quad &\text{(set $n = 0, 1, 2$; Eq. 10.2)} \\
> \mathcal M_{O,n}^{\mathcal D} &= \int_{\mathcal D} \underbrace{\mathbf r_0^{P}\otimes\cdots\otimes\mathbf r_0^{P}}_{n}\,dm \quad &\text{(continuous system: the sum over particles becomes an integral, Eq. 10.3)} \\
> dm &= \lambda\,d\ell = \sigma\,dA = \rho\,dV \quad &\text{(1D, 2D and 3D bodies)}
> \end{aligned}$$
>
> $$\boxed{\mathcal M_{O,0}^{\mathcal D} = \int_{\mathcal D} dm,\qquad \mathcal M_{O,1}^{\mathcal D} = \int_{\mathcal D}\mathbf r_0^{P}\,dm,\qquad \mathcal M_{O,2}^{\mathcal D} = \int_{\mathcal D}\mathbf r_0^{P}\otimes\mathbf r_0^{P}\,dm}$$
>
> **Units:** $[\mathrm M]$ (a scalar), $[\mathrm{M\,L}]$ (a vector) and $[\mathrm{M\,L^2}]$ (a second-order tensor): $\mathrm{kg}$, $\mathrm{kg\,m}$, $\mathrm{kg\,m^2}$
> **Meaning:** the three moments are a scalar, a vector and a tensor; the next sections show that they are the total mass, the mass times the position of the centre of mass, and the second-moment part of the tensor of inertia. Discrete masses add sums of the form of Eq. 10.1 to every integral.

The hard part of these integrals is writing the element of length, area or volume in terms of the differentials of the coordinates that describe the body, and then the limits of every coordinate. For uncommon coordinates one starts from Cartesian coordinates and multiplies by the Jacobian of the change of variables (Notes.pdf, Sec. 10.1). In the spherical coordinates of the notes the angle $\phi$ is a latitude, measured from the plane $Oxy$, not from the axis $Oz$.

> [!derivation] Volume element in cylindrical and spherical coordinates
> **Law:** change of variables in a triple integral; the Jacobian determinant
> **Source:** Notes.pdf, Eq. 10.5; [Lecture 8, Slide 8]; [Lecture 8, Slide 17]
>
> Cylindrical coordinates: $x$, $y$, $z$ written with $R$, $\theta$, $z$.
>
> $$\begin{aligned}
> x &= R\cos\theta,\quad y = R\sin\theta,\quad z = z \quad &\text{(definition of the coordinates)} \\
> J_{\mathrm{cyl}} &= \begin{vmatrix} \cos\theta & -R\sin\theta & 0 \cr \sin\theta & R\cos\theta & 0 \cr 0 & 0 & 1 \end{vmatrix} \quad &\text{(columns: partial derivatives with respect to $R$, $\theta$, $z$)} \\
> &= R\cos^2\theta + R\sin^2\theta = R \quad &\text{(expand along the third row; $\cos^2\theta+\sin^2\theta = 1$)}
> \end{aligned}$$
>
> Spherical coordinates with latitude: the projection of $\mathbf r_0^P$ on the plane $Oxy$ is the leg $r\cos\phi$ adjacent to $\phi$ in the right triangle whose hypotenuse is $r$; the opposite leg $r\sin\phi$ is the height $z$.
>
> $$\begin{aligned}
> x &= r\cos\phi\cos\theta,\quad y = r\cos\phi\sin\theta,\quad z = r\sin\phi \quad &\text{(project the leg $r\cos\phi$ on the axes $Ox$, $Oy$)} \\
> J_{\mathrm{sph}} &= \begin{vmatrix} \cos\phi\cos\theta & -r\cos\phi\sin\theta & -r\sin\phi\cos\theta \cr \cos\phi\sin\theta & r\cos\phi\cos\theta & -r\sin\phi\sin\theta \cr \sin\phi & 0 & r\cos\phi \end{vmatrix} \quad &\text{(columns: derivatives with respect to $r$, $\theta$, $\phi$)} \\
> &= \sin\phi\,\big(r^2\sin^2\theta\sin\phi\cos\phi + r^2\cos^2\theta\sin\phi\cos\phi\big) + r\cos\phi\,\big(r\cos^2\phi\cos^2\theta + r\cos^2\phi\sin^2\theta\big) \quad &\text{(expand along the third row)} \\
> &= r^2\cos\phi\,\big(\sin^2\phi + \cos^2\phi\big) = r^2\cos\phi \quad &\text{(use $\sin^2\theta+\cos^2\theta = 1$ twice)}
> \end{aligned}$$
>
> $$\boxed{dV = dx\,dy\,dz = R\,dR\,d\theta\,dz = r^2\cos\phi\,dr\,d\theta\,d\phi}$$
>
> **Units:** $[\mathrm L]^3$ in the three forms: $R\,dR\,dz$ carries $[\mathrm L^3]$ with $d\theta$ dimensionless, and $r^2\,dr$ carries $[\mathrm L^3]$ with $d\theta\,d\phi$ dimensionless
> **Meaning:** the factors $R$ and $r^2\cos\phi$ are the stretching of the coordinate box into a true volume; with the latitude convention the factor is $\cos\phi$, positive for $\phi$ between minus and plus a right angle.

## 11. Total mass and centre of mass

> [!summary] What you need to know
> - **Total mass:** add up all the mass elements of the body.
> - **Centre of mass** $G$: the average position of the mass, each element weighted by its own mass.
> - **Symmetry first:** a plane of symmetry contains $G$, and so does an axis of symmetry. This gives coordinates of $G$ before any integral.
> - **Composite bodies:** treat each part as a particle of its own mass placed at its own centre of mass. A hole is a part with negative mass.
>
> $$\boxed{m = \int_{\mathcal D} dm,\qquad \mathbf r_0^G = \frac{1}{m}\int_{\mathcal D}\mathbf r_0^P\,dm = \frac{\sum_k m_k\,\mathbf r_0^{G_k}}{\sum_k m_k}}$$
>
> **Slides:** [Lecture 8, Slide 9]; [Lecture 8, Slide 17]; Notes.pdf, Eq. 10.8; Notes.pdf, Sec. 10.3

| Symbol | Meaning |
| :--- | :--- |
| $m$ | total mass of the material system |
| $G$, $\mathbf r_0^G$ | centre of mass and its position in $S_0$ |
| $x_G$, $y_G$, $z_G$ | components of $\mathbf r_0^G$ in $\mathcal B_0$ |
| $\mathcal D_1$, $\mathcal D_2$; $m_1$, $m_2$; $G_1$, $G_2$ | two parts of a composite body, their masses and centres of mass |

![[attachments/EM-T/t6-centre-of-mass.svg]]

> [!derivation] Total mass and position of the centre of mass
> **Law:** definitions of the total mass and of the centre of mass
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.7; Notes.pdf, Eq. 10.8; [Lecture 8, Slide 9]
>
> $$\begin{aligned}
> m &= \mathcal M_{O,0}^{\mathcal D} = \int_{\mathcal D} dm \quad &\text{(total mass: zeroth moment, Eq. 10.6)} \\
> m\,\mathbf r_0^G &= \mathcal M_{O,1}^{\mathcal D} = \int_{\mathcal D}\mathbf r_0^P\,dm \quad &\text{(G: the point that, holding the whole mass, keeps the first moment, Eq. 10.7)} \\
> \mathbf r_0^G &= \frac{1}{m}\int_{\mathcal D}\mathbf r_0^P\,dm \quad &\text{(divide by the scalar $m$)} \\
> x_G &= \frac{1}{m}\int_{\mathcal D}x\,dm,\quad y_G = \frac{1}{m}\int_{\mathcal D}y\,dm,\quad z_G = \frac{1}{m}\int_{\mathcal D}z\,dm \quad &\text{(components in $\mathcal B_0$: constant unit vectors leave the integral)}
> \end{aligned}$$
>
> $$\boxed{m = \int_{\mathcal D} dm,\qquad \mathbf r_0^G = \frac{1}{m}\int_{\mathcal D}\mathbf r_0^P\,dm = \frac{\mathcal M_{O,1}^{\mathcal D}}{\mathcal M_{O,0}^{\mathcal D}}}$$
>
> **Units:** $[\mathrm M]$ for $m$; $[\mathrm{M\,L}]/[\mathrm M] = [\mathrm L]$ for $\mathbf r_0^G$
> **Meaning:** the centre of mass is the mass-weighted average of the positions of all the mass elements: the quotient of the first and the zeroth moments.

The centre of mass does not depend on the origin chosen to compute it: moving the origin from $O$ to $O'$ adds the same vector to every position and to $\mathbf r_0^G$, because the weights add up to $m$.

### Symmetry and the centre of mass

When the mass distribution has a plane or an axis of symmetry, the centre of mass lies on it (Notes.pdf, Sec. 10.3). "Symmetric" means that the reflection in the plane (or the half-turn about the axis) maps the body onto itself and every mass element onto a mirror element of the same mass.

![[attachments/EM-T/t6-symmetry-theorems.svg]]

> [!derivation] First symmetry theorem: the centre of mass lies on a plane or axis of symmetry
> **Law:** pairing of mirror mass elements in the first moment
> **Source:** Notes.pdf, Sec. 10.3; Notes.pdf, Eq. 10.8
>
> Take the plane of symmetry as $Oyz$: the element $dm$ at $(x, y, z)$ has a mirror element $dm$ at $(-x, y, z)$.
>
> $$\begin{aligned}
> \int_{\mathcal D} x\,dm &= \int_{\mathcal D^{+}} x\,dm + \int_{\mathcal D^{-}} x\,dm \quad &\text{(split the body into its halves with positive and negative $x$)} \\
> \int_{\mathcal D^{-}} x\,dm &= \int_{\mathcal D^{+}} (-x)\,dm \quad &\text{(map each element of the negative half to its mirror: same mass, opposite $x$)} \\
> \int_{\mathcal D} x\,dm &= \int_{\mathcal D^{+}} x\,dm - \int_{\mathcal D^{+}} x\,dm = 0 \quad &\text{(the two halves cancel)} \\
> x_G &= \frac{1}{m}\int_{\mathcal D} x\,dm = 0 \quad &\text{(Eq. 10.8, first component)}
> \end{aligned}$$
>
> For an axis of symmetry $Oz$ the half-turn sends $(x, y, z)$ to $(-x, -y, z)$, and the same pairing cancels both $\int x\,dm$ and $\int y\,dm$.
>
> $$\boxed{\text{plane of symmetry } Oyz \Rightarrow x_G = 0;\qquad \text{axis of symmetry } Oz \Rightarrow x_G = y_G = 0}$$
>
> **Units:** $\int x\,dm$ in $[\mathrm{M\,L}]$, $x_G$ in $[\mathrm L]$; the result is a zero length
> **Meaning:** spotting a plane or axis of symmetry fixes one or two coordinates of $G$ before any integral is computed.

### Composite bodies and holes

The lecture recommends to "divide and conquer": break a complex geometry into simpler parts, add their contributions, and treat holes by subtraction ([Lecture 8, Slide 17]). All the inertia properties are integrals over $\mathcal D$, so they are additive over disjoint parts.

![[attachments/EM-T/t6-composite-bodies.svg]]

> [!derivation] Centre of mass of a composite body and of a body with a hole
> **Law:** additivity of the integral over disjoint domains; definition of the centre of mass
> **Source:** [Lecture 8, Slide 17]; Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.8
>
> $$\begin{aligned}
> m &= \int_{\mathcal D_1} dm + \int_{\mathcal D_2} dm = m_1 + m_2 \quad &\text{(the body is the union of the disjoint parts $\mathcal D_1$ and $\mathcal D_2$)} \\
> m\,\mathbf r_0^G &= \int_{\mathcal D_1}\mathbf r_0^P\,dm + \int_{\mathcal D_2}\mathbf r_0^P\,dm \quad &\text{(first moment, split the same way)} \\
> &= m_1\,\mathbf r_0^{G_1} + m_2\,\mathbf r_0^{G_2} \quad &\text{(Eq. 10.7 applied to each part)} \\
> \mathbf r_0^G &= \frac{m_1\,\mathbf r_0^{G_1} + m_2\,\mathbf r_0^{G_2}}{m_1 + m_2} \quad &\text{(divide by the total mass)} \\
> \mathbf r_0^G &= \frac{m_1\,\mathbf r_0^{G_1} - m_2\,\mathbf r_0^{G_2}}{m_1 - m_2} \quad &\text{(a hole $\mathcal D_2$ cut out of a full body $\mathcal D_1$: a part of negative mass)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G = \frac{\sum_k m_k\,\mathbf r_0^{G_k}}{\sum_k m_k},\qquad \text{holes enter with } m_k < 0}$$
>
> **Units:** $[\mathrm M][\mathrm L]/[\mathrm M] = [\mathrm L]$
> **Meaning:** each part acts as a point particle of its own mass at its own centre of mass; the same additivity holds for the moments, products and tensors of inertia, provided they are taken about the same point and in the same basis.

## 12. Moments and products of inertia

> [!summary] What you need to know
> - **Moment of inertia about an axis:** each mass element times the square of its distance to the axis, added over the body. It is never negative, and mass far from the axis counts most.
> - **Products of inertia** keep the signs of the coordinates, so they can be negative. They measure how unevenly the mass is spread about the axes.
> - A plane of symmetry makes zero every product of inertia that involves that plane.
> - **Flat body** in the plane $Oxy$: the moment about $Oz$ is the sum of the moments about $Ox$ and $Oy$, so two integrals give all three.
> - **Shortcut:** the three moments about the axes add up to twice the moment about the point $O$.
>
> $$\boxed{I_z = \int_{\mathcal D}(x^2+y^2)\,dm,\qquad P_{xz,yz} = \int_{\mathcal D} xy\,dm,\qquad I_x + I_y + I_z = 2\,I_O}$$
>
> **Slides:** [Lecture 8, Slide 10]; [Lecture 8, Slide 11]; Notes.pdf, Eq. 10.13; Notes.pdf, Eq. 10.22

The moments and products of inertia come from the second moment of the mass distribution and govern rotational dynamics. They have dimensions $[\mathrm{M\,L^2}]$ and SI unit $\mathrm{kg\,m^2}$ (Notes.pdf, Sec. 10.4). The moment of inertia of a body about an axis is the "resistance" it offers to changes of its angular velocity about that axis ([Lecture 8, Slide 10]).

| Symbol | Meaning |
| :--- | :--- |
| $d$ | distance from the mass element to the point, line or plane considered |
| $I_r^b$ | moment of inertia of the body $b$ about the axis $r$ (the slides' notation) |
| $I_O$ | moment of inertia about the point $O$ (polar moment of inertia) |
| $I_x$, $I_y$, $I_z$ | moments of inertia about the axes $Ox$, $Oy$, $Oz$ |
| $I_{xy}$, $I_{xz}$, $I_{yz}$ | moments of inertia about the planes $Oxy$, $Oxz$, $Oyz$ |
| $\pi_1$, $\pi_2$; $d_1$, $d_2$ | two orthogonal planes and the signed distances of the mass element to them |
| $P_{xy,xz}$, $P_{xy,yz}$, $P_{xz,yz}$ | products of inertia with respect to pairs of coordinate planes |

![[attachments/EM-T/t6-inertia-distances.svg]]

> [!derivation] Moments of inertia about a point, the coordinate axes and the coordinate planes
> **Law:** definition of the moment of inertia; Pythagoras in $\mathcal B_0$
> **Source:** Notes.pdf, Eq. 10.9; Notes.pdf, Eq. 10.10; Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.12; [Lecture 8, Slide 10]
>
> The element $dm$ sits at $\mathbf r_0^P = x\,\mathbf i + y\,\mathbf j + z\,\mathbf k$.
>
> $$\begin{aligned}
> I &= \int_{\mathcal D} d^2\,dm \quad &\text{(definition, Eq. 10.9)} \\
> d_O^2 &= \lvert\mathbf r_0^P\rvert^2 = x^2+y^2+z^2 \quad &\text{(distance to the point $O$)} \\
> d_{Ox}^2 &= y^2+z^2,\quad d_{Oy}^2 = x^2+z^2,\quad d_{Oz}^2 = x^2+y^2 \quad &\text{(distance to an axis: hypotenuse of the two coordinates normal to it)} \\
> d_{Oxy}^2 &= z^2,\quad d_{Oxz}^2 = y^2,\quad d_{Oyz}^2 = x^2 \quad &\text{(distance to a plane: the coordinate normal to it)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} I_O = \int_{\mathcal D}(x^2+y^2+z^2)\,dm,\qquad I_x = \int_{\mathcal D}(y^2+z^2)\,dm,\quad I_y = \int_{\mathcal D}(x^2+z^2)\,dm,\quad I_z = \int_{\mathcal D}(x^2+y^2)\,dm \\ I_{xy} = \int_{\mathcal D} z^2\,dm,\quad I_{xz} = \int_{\mathcal D} y^2\,dm,\quad I_{yz} = \int_{\mathcal D} x^2\,dm \end{gathered}}$$
>
> **Units:** $[\mathrm L^2][\mathrm M] = [\mathrm{M\,L^2}]$, in $\mathrm{kg\,m^2}$
> **Meaning:** mass far from the axis weighs with the square of its distance; the integrand is never negative, so no moment of inertia is negative.

> [!derivation] Relation between the moments about the point, the axes and the planes
> **Law:** add the definitions of Eqs. 10.10 to 10.12
> **Source:** Notes.pdf, Eq. 10.13; [Lecture 8, Slide 10]
>
> $$\begin{aligned}
> I_{xy}+I_{xz}+I_{yz} &= \int_{\mathcal D}(z^2+y^2+x^2)\,dm = I_O \quad &\text{(sum of the three plane moments, Eq. 10.12)} \\
> I_x+I_y+I_z &= \int_{\mathcal D}\big[(y^2+z^2)+(x^2+z^2)+(x^2+y^2)\big]\,dm \quad &\text{(sum of the three axis moments, Eq. 10.11)} \\
> &= \int_{\mathcal D} 2\,(x^2+y^2+z^2)\,dm = 2\,I_O \quad &\text{(each square appears twice; Eq. 10.10)}
> \end{aligned}$$
>
> $$\boxed{2\,I_O = 2\,(I_{xy}+I_{xz}+I_{yz}) = I_x+I_y+I_z}$$
>
> **Units:** $\mathrm{kg\,m^2}$ in every term
> **Meaning:** the moment about a point is the sum of the moments about three orthogonal planes through it, and half the sum of the moments about three orthogonal axes through it; it often saves one integral.

> [!warning] Erratum in the source
> The notes state that the moment of inertia "is always positive" (Notes.pdf, Sec. 10.4) and [Lecture 8, Slide 12] calls the tensor of inertia "definite-positive". The integrand is never negative, so the correct statement is "never negative" (positive semi-definite): the moment vanishes when all the mass lies on the axis. Check: for a thin straight wire along $Ox$ every element has $y$ and $z$ equal to zero, so the integrand of $I_x$ vanishes everywhere and $I_x$ is zero, although the wire has mass. For any body that is not contained in a line the moments are strictly positive and the slide's statement holds.

### Products of inertia

> [!derivation] Products of inertia with respect to the coordinate planes
> **Law:** definition of the product of inertia with signed distances
> **Source:** Notes.pdf, Eq. 10.14; Notes.pdf, Eq. 10.15; [Lecture 8, Slide 11]
>
> $$\begin{aligned}
> P_{\pi_1,\pi_2} &= \int_{\mathcal D} d_1\,d_2\,dm \quad &\text{(definition for two orthogonal planes, Eq. 10.14)} \\
> d_{Oxy} &= z,\quad d_{Oxz} = y,\quad d_{Oyz} = x \quad &\text{(signed distance to a coordinate plane: the coordinate along its normal)} \\
> P_{xy,xz} &= \int_{\mathcal D} z\,y\,dm,\quad P_{xy,yz} = \int_{\mathcal D} z\,x\,dm,\quad P_{xz,yz} = \int_{\mathcal D} y\,x\,dm \quad &\text{(the three pairs of coordinate planes)}
> \end{aligned}$$
>
> $$\boxed{P_{xy,xz} = \int_{\mathcal D} zy\,dm,\qquad P_{xy,yz} = \int_{\mathcal D} zx\,dm,\qquad P_{xz,yz} = \int_{\mathcal D} yx\,dm}$$
>
> **Units:** $[\mathrm L][\mathrm L][\mathrm M] = [\mathrm{M\,L^2}]$, in $\mathrm{kg\,m^2}$
> **Meaning:** the signs of the distances are kept, so a product of inertia can be negative; $P_{xy,xz}$ measures the coupling between rotations about $Oy$ and $Oz$ ([Lecture 8, Slide 11]), the two axes normal to its planes.

> [!derivation] Second symmetry theorem: a plane of symmetry cancels its products of inertia
> **Law:** pairing of mirror mass elements in the product integral
> **Source:** Notes.pdf, Sec. 10.4; [Lecture 8, Slide 11]
>
> Let $Oyz$ be a plane of symmetry: the element $dm$ at $(x, y, z)$ has a mirror element $dm$ at $(-x, y, z)$.
>
> $$\begin{aligned}
> P_{xz,yz} &= \int_{\mathcal D^{+}} y\,x\,dm + \int_{\mathcal D^{+}} y\,(-x)\,dm = 0 \quad &\text{(the mirror element has the same $y$ and the opposite $x$)} \\
> P_{xy,yz} &= \int_{\mathcal D^{+}} z\,x\,dm + \int_{\mathcal D^{+}} z\,(-x)\,dm = 0 \quad &\text{(same $z$, opposite $x$)} \\
> P_{xy,xz} &= \int_{\mathcal D^{+}} z\,y\,dm + \int_{\mathcal D^{+}} z\,y\,dm = 2\int_{\mathcal D^{+}} zy\,dm \quad &\text{(neither factor changes sign: no cancellation)}
> \end{aligned}$$
>
> $$\boxed{Oyz \text{ plane of symmetry} \Rightarrow P_{xz,yz} = P_{xy,yz} = 0}$$
>
> **Units:** $\mathrm{kg\,m^2}$; the result is a zero product of inertia
> **Meaning:** every product of inertia that involves a plane of symmetry vanishes; the product of the other two planes survives in general. Checking the symmetries before integrating saves most of the work.

### Flat bodies

For a planar body of negligible thickness in the plane $Oxy$ every mass element has zero $z$ coordinate (Notes.pdf, Sec. 10.5, below Eq. 10.21).

![[attachments/EM-T/t6-flat-plate.svg]]

> [!derivation] Perpendicular axis relation of a flat body
> **Law:** Eqs. 10.10, 10.11 and 10.15 with the coordinate normal to the body set to zero
> **Source:** Notes.pdf, Eq. 10.13; Notes.pdf, Eq. 10.22; Notes.pdf, Eq. 10.24
>
> $$\begin{aligned}
> I_x &= \int_{\mathcal D}(y^2+0)\,dm = \int_{\mathcal D}y^2\,dm,\qquad I_y = \int_{\mathcal D}(x^2+0)\,dm = \int_{\mathcal D}x^2\,dm \quad &\text{(Eq. 10.11 with $z$ zero)} \\
> I_z &= \int_{\mathcal D}(x^2+y^2)\,dm = I_y + I_x \quad &\text{(linearity of the integral)} \\
> I_O &= \int_{\mathcal D}(x^2+y^2+0)\,dm = I_z \quad &\text{(Eq. 10.10 with $z$ zero)} \\
> P_{xy,xz} &= \int_{\mathcal D}0\cdot y\,dm = 0,\qquad P_{xy,yz} = \int_{\mathcal D}0\cdot x\,dm = 0 \quad &\text{(the body lies in the plane $Oxy$)}
> \end{aligned}$$
>
> $$\boxed{I_z = I_O = I_x + I_y,\qquad P_{xy,xz} = P_{xy,yz} = 0}$$
>
> **Units:** $\mathrm{kg\,m^2}$ in every term
> **Meaning:** the moment about the axis normal to a flat body equals the sum of the moments about two orthogonal in-plane axes through the same point, so only two in-plane integrals are needed; the plane of the body acts as a plane of symmetry for the products.

## 13. Worked examples: wire, plate, half disk and half sphere

> [!summary] What you need to know
> - Four bodies, always worked in the same order: mass element, total mass, centre of mass (symmetry first), then the moments and products of inertia.
> - **Half-circumference wire:** $G$ is on the axis of symmetry at about $0.64R$ from the centre, off the wire itself.
> - **Half disk:** $G$ is at about $0.42R$, closer to the centre than for the wire, because more of the mass is near the centre.
> - **Half sphere:** $G$ is on the axis, below mid-height, because most of the volume is near the flat face.
> - **Rectangular plate** $L\times W$: the moment about an axis depends only on how far the mass spreads away from that axis.
>
> $$\boxed{y_G^{\text{wire}} = \frac{2R}{\pi},\qquad y_G^{\text{half disk}} = \frac{4R}{3\pi},\qquad z_G^{\text{half sphere}} = \frac{3R}{8},\qquad I_z^{\text{plate}} = \frac{M(L^2+W^2)}{12}}$$
>
> **Slides:** [Lecture 8, Slide 18]; [Lecture 8, Slide 19]; [Lecture 8, Slide 20]; [Lecture 8, Slide 21]

The notes illustrate the definitions with four homogeneous bodies of Fig. 10.2, which the lecture repeats as its last four slides (Notes.pdf, Sec. 10.5; [Lecture 8, Slides 18-21]). The notes leave the moments of inertia of the half disk and of the half sphere as exercises; they are solved here and marked as extensions.

### Half-circumference wire

> [!example] Half-circumference wire (Notes.pdf, Sec. 10.5; [Lecture 8, Slide 18])
> A homogeneous wire of linear density $\lambda$ has the shape of a half circumference of radius $R$ centred at $O$ in the plane $Oxy$, on the side of positive $y$. The polar angle $\theta$, measured from $Ox$ towards $Oy$, runs from zero to $\pi$ along the wire. Find its mass, its centre of mass, its moments of inertia about the coordinate axes and its products of inertia.

![[attachments/EM-T/t6-half-wire.svg]]

> [!derivation] Mass element and total mass of the wire
> **Law:** linear density; arc length of a circle; Eq. 10.6
> **Source:** Notes.pdf, Eq. 10.16; Notes.pdf, Eq. 10.17; Notes.pdf, Eq. 10.18; [Lecture 8, Slide 18]
>
> $$\begin{aligned}
> x &= R\cos\theta,\quad y = R\sin\theta \quad &\text{(parametric equation, Eq. 10.16; $\theta$ from $0$ to $\pi$)} \\
> d\ell &= \sqrt{\Big(\tfrac{dx}{d\theta}\Big)^2+\Big(\tfrac{dy}{d\theta}\Big)^2}\,d\theta = \sqrt{R^2\sin^2\theta+R^2\cos^2\theta}\,d\theta = R\,d\theta \quad &\text{(arc length; derivatives of the parametrization)} \\
> dm &= \lambda\,d\ell = \lambda R\,d\theta \quad &\text{(Eq. 10.17)} \\
> m &= \int_0^{\pi}\lambda R\,d\theta = \lambda R\,\big[\theta\big]_0^{\pi} = \lambda R\,(\pi - 0) \quad &\text{(antiderivative $\theta$; Barrow's rule with both limits)}
> \end{aligned}$$
>
> $$\boxed{m = \pi\lambda R}$$
>
> **Units:** $[\mathrm{M\,L^{-1}}][\mathrm L] = [\mathrm M]$
> **Meaning:** the mass is the density times the length of the half circumference, $\pi R$.

> [!derivation] Centre of mass of the wire
> **Law:** definition of the centre of mass
> **Source:** Notes.pdf, Eq. 10.8; Notes.pdf, Eq. 10.19; [Lecture 8, Slide 18]
>
> $$\begin{aligned}
> \mathbf r_0^G &= \frac{1}{m}\int_{\mathcal D}(x\,\mathbf i + y\,\mathbf j)\,dm = \frac{1}{\pi\lambda R}\int_0^{\pi}\big(\lambda R^2\cos\theta\,\mathbf i + \lambda R^2\sin\theta\,\mathbf j\big)\,d\theta \quad &\text{(Eq. 10.19; substitute $x$, $y$ and $dm$)} \\
> \int_0^{\pi}\cos\theta\,d\theta &= \big[\sin\theta\big]_0^{\pi} = \sin\pi - \sin 0 = 0 \quad &\text{(antiderivative of $\cos\theta$; Barrow)} \\
> \int_0^{\pi}\sin\theta\,d\theta &= \big[-\cos\theta\big]_0^{\pi} = -\cos\pi + \cos 0 = 2 \quad &\text{(antiderivative of $\sin\theta$; Barrow)} \\
> \mathbf r_0^G &= \frac{\lambda R^2}{\pi\lambda R}\,(0\,\mathbf i + 2\,\mathbf j) \quad &\text{(collect)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G = \frac{2}{\pi}R\,\mathbf j}$$
>
> **Units:** $[\mathrm{M\,L^{-1}}][\mathrm L^2]/[\mathrm M] = [\mathrm L]$
> **Meaning:** $G$ lies on the axis of symmetry $Oy$, as the first symmetry theorem predicts, at about $0.64R$ from $O$: off the wire itself.

> [!derivation] Moments of inertia of the wire about Oz and Ox
> **Law:** Eq. 10.11; half-angle identities
> **Source:** Notes.pdf, Eq. 10.20; Notes.pdf, Eq. 10.21; [Lecture 8, Slide 18]
>
> $$\begin{aligned}
> I_z &= \int_{\mathcal D}(x^2+y^2)\,dm = \int_0^{\pi}R^2(\cos^2\theta+\sin^2\theta)\,\lambda R\,d\theta = \lambda R^3\big[\theta\big]_0^{\pi} = \pi\lambda R^3 \quad &\text{(every point is at distance $R$ from $Oz$; Barrow)} \\
> I_x &= \int_{\mathcal D}y^2\,dm = \lambda R^3\int_0^{\pi}\sin^2\theta\,d\theta \quad &\text{($z$ is zero; $y = R\sin\theta$)} \\
> \sin^2\theta &= \tfrac12(1-\cos 2\theta) \quad &\text{(half-angle identity)} \\
> \int_0^{\pi}\sin^2\theta\,d\theta &= \Big[\tfrac{\theta}{2}-\tfrac{\sin 2\theta}{4}\Big]_0^{\pi} = \Big(\tfrac{\pi}{2}-\tfrac{\sin 2\pi}{4}\Big)-\Big(0-\tfrac{\sin 0}{4}\Big) = \tfrac{\pi}{2} \quad &\text{(antiderivative; Barrow with both limits)} \\
> I_x &= \tfrac{\pi}{2}\lambda R^3 = \tfrac12\,(\pi\lambda R)\,R^2 \quad &\text{(write with $m$)}
> \end{aligned}$$
>
> $$\boxed{I_z = I_O = mR^2,\qquad I_x = \tfrac12\,mR^2}$$
>
> **Units:** $[\mathrm{M\,L^{-1}}][\mathrm L^3] = [\mathrm{M\,L^2}]$
> **Meaning:** all the mass of the wire is at the same distance $R$ from $Oz$, so $I_z$ is that of a ring; because the wire is planar, $I_z$ is also the polar moment $I_O$.

> [!derivation] Moment about Oy and products of inertia of the wire
> **Law:** perpendicular axis relation of a flat body; second symmetry theorem
> **Source:** Notes.pdf, Eq. 10.22; Notes.pdf, Eq. 10.23; [Lecture 8, Slide 18]
>
> $$\begin{aligned}
> I_y &= I_z - I_x = mR^2 - \tfrac12 mR^2 = \tfrac12 mR^2 \quad &\text{(flat body, Section 12: $I_z = I_x + I_y$)} \\
> I_y &= \lambda R^3\int_0^{\pi}\cos^2\theta\,d\theta = \lambda R^3\Big[\tfrac{\theta}{2}+\tfrac{\sin 2\theta}{4}\Big]_0^{\pi} = \tfrac{\pi}{2}\lambda R^3 \quad &\text{(direct check; $\cos^2\theta = \tfrac12(1+\cos 2\theta)$, Barrow)} \\
> P_{xy,xz} &= P_{xy,yz} = 0 \quad &\text{(the wire lies in $Oxy$: $z$ is zero)} \\
> P_{xz,yz} &= \lambda R^3\int_0^{\pi}\cos\theta\sin\theta\,d\theta = \lambda R^3\Big[\tfrac{\sin^2\theta}{2}\Big]_0^{\pi} = \lambda R^3\Big(\tfrac{\sin^2\pi}{2}-\tfrac{\sin^2 0}{2}\Big) = 0 \quad &\text{(substitution $u = \sin\theta$, $du = \cos\theta\,d\theta$; Barrow)}
> \end{aligned}$$
>
> $$\boxed{I_y = \tfrac12\,mR^2,\qquad P_{xy,xz} = P_{xy,yz} = P_{xz,yz} = 0}$$
>
> **Units:** $\mathrm{kg\,m^2}$
> **Meaning:** the integral confirms what symmetry predicts: $Oyz$ is a plane of symmetry of the wire, so $P_{xz,yz}$ vanishes, and $Oxy$ contains the wire.

### Homogeneous rectangular plate

> [!example] Homogeneous plate (Notes.pdf, Sec. 10.5; [Lecture 8, Slide 19])
> A homogeneous plate of mass $M$, length $L$ along $Ox$, width $W$ along $Oy$ and negligible thickness is centred at $O$. Find its moments and products of inertia in $S_0$, and the product of inertia with respect to the planes $Ax_1z_1$ and $Ay_1z_1$ of a frame $S_1$ with origin at a corner $A$ of the plate.

![[attachments/EM-T/t6-plate.svg]]

> [!info] Note on the source figure
> The notes refer to the frame $S_1$ "as shown in Fig. 10.2(b)", but the figure does not draw it. The limits of Eq. 10.27 (from zero to $L$ and from zero to $W$, with a positive result) fix it: origin $A$ at a corner of the plate, $Ax_1$ along the side of length $L$ and $Ay_1$ along the side of width $W$, both pointing into the plate, parallel to $Ox$ and $Oy$. The figure above draws it that way, and the Steiner check of Section 16 confirms the value.

> [!derivation] Surface density, mass element and centre of mass of the plate
> **Law:** area density of a homogeneous body; first symmetry theorem
> **Source:** Notes.pdf, Sec. 10.5; Notes.pdf, Eq. 10.24; [Lecture 8, Slide 19]
>
> $$\begin{aligned}
> \sigma &= \frac{M}{LW} \quad &\text{(homogeneous: mass divided by area)} \\
> dm &= \sigma\,dA = \frac{M}{LW}\,dx\,dy \quad &\text{(Cartesian area element)} \\
> x_G &= 0,\quad y_G = 0 \quad &\text{($Oyz$ and $Oxz$ are planes of symmetry)}
> \end{aligned}$$
>
> $$\boxed{dm = \frac{M}{LW}\,dx\,dy,\qquad G \equiv O}$$
>
> **Units:** $\sigma$ in $[\mathrm M]/[\mathrm L^2] = \mathrm{kg/m^2}$; $dm$ in $\mathrm{kg}$
> **Meaning:** two planes of symmetry through $O$ put the centre of mass at the centre of the plate.

> [!derivation] Moments of inertia of the plate about its central axes
> **Law:** Eq. 10.11 as a double integral over the rectangle
> **Source:** Notes.pdf, Eq. 10.24; Notes.pdf, Eq. 10.25; Notes.pdf, Eq. 10.26; [Lecture 8, Slide 19]
>
> $$\begin{aligned}
> I_x &= \int_{-W/2}^{W/2}\int_{-L/2}^{L/2}\frac{M}{LW}\,y^2\,dx\,dy = \frac{M}{LW}\int_{-W/2}^{W/2}y^2\,\big[x\big]_{-L/2}^{L/2}\,dy \quad &\text{(inner integral in $x$; $y^2$ is constant there)} \\
> &= \frac{M}{LW}\,L\int_{-W/2}^{W/2}y^2\,dy = \frac{M}{W}\Big[\frac{y^3}{3}\Big]_{-W/2}^{W/2} \quad &\text{(Barrow: $L/2 - (-L/2) = L$)} \\
> &= \frac{M}{W}\Big(\frac{W^3}{24}+\frac{W^3}{24}\Big) = \frac{1}{12}MW^2 \quad &\text{(Barrow with both limits)} \\
> I_y &= \frac{M}{LW}\int_{-W/2}^{W/2}\Big[\frac{x^3}{3}\Big]_{-L/2}^{L/2}dy = \frac{M}{LW}\,\frac{L^3}{12}\,\big[y\big]_{-W/2}^{W/2} = \frac{1}{12}ML^2 \quad &\text{(same steps with $x^2$)} \\
> I_z &= \int_{-W/2}^{W/2}\int_{-L/2}^{L/2}\frac{M}{LW}(x^2+y^2)\,dx\,dy = I_y + I_x \quad &\text{(linearity; flat body, $I_z = I_O$)}
> \end{aligned}$$
>
> $$\boxed{I_O = I_z = \tfrac{1}{12}M(L^2+W^2),\qquad I_x = \tfrac{1}{12}MW^2,\qquad I_y = \tfrac{1}{12}ML^2 = I_O - I_x}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$, in $\mathrm{kg\,m^2}$
> **Meaning:** the moment about $Ox$ depends only on the width $W$, the spread of the mass away from $Ox$; the long side $L$ makes $I_y$ the larger one when $L$ exceeds $W$.

> [!derivation] Products of inertia of the plate in S0 and at the corner A
> **Law:** second symmetry theorem; Eq. 10.15 as a double integral
> **Source:** Notes.pdf, Eq. 10.27; Notes.pdf, Sec. 10.5; [Lecture 8, Slide 19]
>
> $$\begin{aligned}
> P_{xy,xz} &= P_{xy,yz} = 0 \quad &\text{(the plate lies in $Oxy$)} \\
> P_{xz,yz} &= 0 \quad &\text{($Oyz$ and $Oxz$ are planes of symmetry through $O$)} \\
> P_{x_1z_1,y_1z_1} &= \int_0^{W}\int_0^{L}\frac{M}{LW}\,x\,y\,dx\,dy = \frac{M}{LW}\int_0^{W}y\Big[\frac{x^2}{2}\Big]_0^{L}dy \quad &\text{(coordinates measured from the corner $A$; inner integral in $x$)} \\
> &= \frac{M}{LW}\,\frac{L^2}{2}\Big[\frac{y^2}{2}\Big]_0^{W} = \frac{M}{LW}\,\frac{L^2}{2}\,\frac{W^2}{2} \quad &\text{(Barrow with both limits, twice)}
> \end{aligned}$$
>
> $$\boxed{P_{x_1z_1,y_1z_1} = \tfrac14\,MLW}$$
>
> **Units:** $[\mathrm M][\mathrm L][\mathrm L] = \mathrm{kg\,m^2}$
> **Meaning:** seen from the corner the whole plate lies in the quadrant of positive $x_1$ and $y_1$, so the product is positive; the planes through $A$ are no longer planes of symmetry. The products with the plane $Ax_1y_1$ stay zero because the plate lies in it.

### Homogeneous half disk

> [!example] Half disk (Notes.pdf, Sec. 10.5; [Lecture 8, Slide 20])
> A homogeneous half disk of radius $R$ and area density $\sigma$ lies in the plane $Oxy$, centred at $O$, on the side of positive $y$. Find its mass and its centre of mass (notes), and its moments of inertia about the coordinate axes (left as an exercise in the notes).

![[attachments/EM-T/t6-half-disk.svg]]

> [!derivation] Mass element and mass of the half disk
> **Law:** polar coordinates in the plane; area density
> **Source:** Notes.pdf, Eq. 10.28; Notes.pdf, Eq. 10.29; Notes.pdf, Eq. 10.30; [Lecture 8, Slide 20]
>
> $$\begin{aligned}
> x &= r\cos\theta,\quad y = r\sin\theta \quad &\text{(Eq. 10.28; $r$ from $0$ to $R$, $\theta$ from $0$ to $\pi$)} \\
> dA &= r\,dr\,d\theta \quad &\text{(Jacobian $r$ of the polar coordinates, Section 10 with $z$ fixed)} \\
> dm &= \sigma\,r\,dr\,d\theta \quad &\text{(Eq. 10.29)} \\
> m &= \sigma\int_0^{\pi}\int_0^{R}r\,dr\,d\theta = \sigma\Big[\frac{r^2}{2}\Big]_0^{R}\big[\theta\big]_0^{\pi} = \sigma\,\frac{R^2}{2}\,\pi \quad &\text{(the limits are constant: the integral factorizes; Barrow)}
> \end{aligned}$$
>
> $$\boxed{m = \sigma\,\frac{\pi R^2}{2}}$$
>
> **Units:** $[\mathrm{M\,L^{-2}}][\mathrm L^2] = [\mathrm M]$
> **Meaning:** the density times the area of half a circle.

> [!derivation] Centre of mass of the half disk
> **Law:** definition of the centre of mass; first symmetry theorem
> **Source:** Notes.pdf, Eq. 10.31; [Lecture 8, Slide 20]
>
> $$\begin{aligned}
> x_G &= 0 \quad &\text{($Oyz$ is a plane of symmetry)} \\
> y_G &= \frac{1}{m}\int_{\mathcal D}y\,dm = \frac{2}{\pi\sigma R^2}\,\sigma\int_0^{\pi}\int_0^{R}r\sin\theta\;r\,dr\,d\theta \quad &\text{(Eq. 10.31: $y = r\sin\theta$, $dm = \sigma r\,dr\,d\theta$)} \\
> &= \frac{2}{\pi R^2}\Big[\frac{r^3}{3}\Big]_0^{R}\big[-\cos\theta\big]_0^{\pi} = \frac{2}{\pi R^2}\,\frac{R^3}{3}\,(1+1) \quad &\text{(factorize; Barrow with both limits)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G = \frac{4R}{3\pi}\,\mathbf j}$$
>
> **Units:** $[\mathrm L^3]/[\mathrm L^2] = [\mathrm L]$
> **Meaning:** $G$ is at about $0.42R$ from $O$ on the axis of symmetry, closer to $O$ than for the wire ($0.64R$), because the half disk keeps mass near the centre.

> [!derivation] Extension: moments of inertia of the half disk (exercise of the notes)
> **Law:** Eq. 10.11 in polar coordinates; perpendicular axis relation
> **Source:** Notes.pdf, Sec. 10.5; Notes.pdf, Eq. 10.11; [Lecture 8, Slide 20]
>
> $$\begin{aligned}
> I_x &= \int_{\mathcal D}y^2\,dm = \sigma\int_0^{\pi}\int_0^{R}r^2\sin^2\theta\;r\,dr\,d\theta = \sigma\Big[\frac{r^4}{4}\Big]_0^{R}\int_0^{\pi}\sin^2\theta\,d\theta \quad &\text{($z$ is zero; factorize)} \\
> &= \sigma\,\frac{R^4}{4}\,\Big[\frac{\theta}{2}-\frac{\sin 2\theta}{4}\Big]_0^{\pi} = \sigma\,\frac{R^4}{4}\,\frac{\pi}{2} = \frac{\pi\sigma R^2}{2}\,\frac{R^2}{4} \quad &\text{(half-angle identity; Barrow)} \\
> I_y &= \sigma\,\frac{R^4}{4}\Big[\frac{\theta}{2}+\frac{\sin 2\theta}{4}\Big]_0^{\pi} = \sigma\,\frac{R^4}{4}\,\frac{\pi}{2} \quad &\text{(same with $x^2 = r^2\cos^2\theta$)} \\
> I_z &= I_x + I_y = \sigma\,\frac{\pi R^4}{4} \quad &\text{(flat body)} \\
> P_{xz,yz} &= \sigma\Big[\frac{r^4}{4}\Big]_0^{R}\Big[\frac{\sin^2\theta}{2}\Big]_0^{\pi} = 0,\qquad P_{xy,xz} = P_{xy,yz} = 0 \quad &\text{($Oyz$ symmetry; body in $Oxy$)}
> \end{aligned}$$
>
> $$\boxed{I_x = I_y = \tfrac14\,mR^2,\qquad I_z = I_O = \tfrac12\,mR^2,\qquad \text{all products zero}}$$
>
> **Units:** $[\mathrm{M\,L^{-2}}][\mathrm L^4] = \mathrm{kg\,m^2}$
> **Meaning:** these are the values of a full disk per unit mass: each half of a disk carries half the mass and half the moment about any diameter or about the normal axis through the centre.

### Homogeneous half sphere

> [!example] Half sphere (Notes.pdf, Sec. 10.5; [Lecture 8, Slide 21])
> A solid homogeneous half sphere (hemisphere) of radius $R$ and volume density $\rho$ has its flat face on the plane $Oxy$, centred at $O$, and lies on the side of positive $z$. Find its mass and its centre of mass (notes), and its moments and products of inertia about $O$ (left as an exercise in the notes). The spherical coordinates are those of Section 10: radius $r$, longitude $\theta$ measured in $Oxy$ from $Ox$, latitude $\phi$ measured from $Oxy$.

![[attachments/EM-T/t6-half-sphere.svg]]

> [!warning] Erratum in the source
> Eq. 10.32 of the notes reads "dm equals r squared cos phi dr dtheta dphi": the density is missing. The right-hand side is the volume element of Eq. 10.5, in cubic metres, so it cannot be a mass; Eq. 10.33, in the next line, does carry $\rho$. The note writes the mass element with $\rho$. The same paragraph refers to the half sphere as Fig. 10.2(c); it is Fig. 10.2(d).

> [!derivation] Mass element and mass of the half sphere
> **Law:** volume density; spherical volume element of Eq. 10.5
> **Source:** Notes.pdf, Eq. 10.5; Notes.pdf, Eq. 10.32; Notes.pdf, Eq. 10.33; [Lecture 8, Slide 21]
>
> $$\begin{aligned}
> dm &= \rho\,dV = \rho\,r^2\cos\phi\,dr\,d\theta\,d\phi \quad &\text{(Eq. 10.32 with the density restored)} \\
> m &= \rho\int_0^{R}r^2\,dr\int_0^{\pi/2}\cos\phi\,d\phi\int_0^{2\pi}d\theta \quad &\text{(limits: $r$ to $R$, upper half $\phi$ from $0$ to $\pi/2$, full turn in $\theta$; the integral factorizes)} \\
> \int_0^{R}r^2\,dr &= \Big[\frac{r^3}{3}\Big]_0^{R} = \frac{R^3}{3},\quad \int_0^{\pi/2}\cos\phi\,d\phi = \big[\sin\phi\big]_0^{\pi/2} = 1,\quad \int_0^{2\pi}d\theta = 2\pi \quad &\text{(Barrow with both limits)} \\
> m &= \rho\,\frac{R^3}{3}\cdot 1\cdot 2\pi \quad &\text{(product of the three factors)}
> \end{aligned}$$
>
> $$\boxed{m = \tfrac23\,\rho\pi R^3}$$
>
> **Units:** $[\mathrm{M\,L^{-3}}][\mathrm L^3] = [\mathrm M]$
> **Meaning:** the density times half the volume of a sphere.

> [!derivation] Centre of mass of the half sphere
> **Law:** definition of the centre of mass; first symmetry theorem
> **Source:** Notes.pdf, Eq. 10.34; [Lecture 8, Slide 21]
>
> $$\begin{aligned}
> x_G &= y_G = 0 \quad &\text{($Oz$ is an axis of symmetry)} \\
> z_G &= \frac{1}{m}\int_{\mathcal D}z\,dm = \frac{\rho}{m}\int_0^{R}r^3\,dr\int_0^{\pi/2}\sin\phi\cos\phi\,d\phi\int_0^{2\pi}d\theta \quad &\text{($z = r\sin\phi$ times $\rho r^2\cos\phi$)} \\
> \int_0^{\pi/2}\sin\phi\cos\phi\,d\phi &= \Big[\frac{\sin^2\phi}{2}\Big]_0^{\pi/2} = \frac12 - 0 \quad &\text{(substitution $u = \sin\phi$, $du = \cos\phi\,d\phi$; Barrow)} \\
> z_G &= \frac{3}{2\rho\pi R^3}\,\rho\,\frac{R^4}{4}\,\frac12\,2\pi \quad &\text{(Barrow for $r^3$: $R^4/4$; substitute $m$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G = \tfrac38\,R\,\mathbf k}$$
>
> **Units:** $[\mathrm L^4]/[\mathrm L^3] = [\mathrm L]$
> **Meaning:** $G$ lies on the axis of symmetry, below mid-height, because most of the volume of the hemisphere is near its flat face.

> [!derivation] Extension: moments and products of inertia of the half sphere about O (exercise of the notes)
> **Law:** Eqs. 10.10, 10.11 and 10.13 in spherical coordinates; second symmetry theorem
> **Source:** Notes.pdf, Sec. 10.5; Notes.pdf, Eq. 10.13; [Lecture 8, Slide 21]
>
> $$\begin{aligned}
> I_O &= \int_{\mathcal D}r^2\,dm = \rho\Big[\frac{r^5}{5}\Big]_0^{R}\big[\sin\phi\big]_0^{\pi/2}\big[\theta\big]_0^{2\pi} = \frac{2\pi\rho R^5}{5} \quad &\text{(distance to $O$ is $r$; Barrow three times)} \\
> I_z &= \int_{\mathcal D}(x^2+y^2)\,dm = \rho\int_0^{R}r^4\,dr\int_0^{\pi/2}\cos^3\phi\,d\phi\int_0^{2\pi}d\theta \quad &\text{(distance to $Oz$ is the leg $r\cos\phi$)} \\
> \int_0^{\pi/2}\cos^3\phi\,d\phi &= \int_0^{1}(1-u^2)\,du = \Big[u-\frac{u^3}{3}\Big]_0^{1} = \frac23 \quad &\text{($u = \sin\phi$, $du = \cos\phi\,d\phi$, limits $0$ and $1$; Barrow)} \\
> I_z &= \rho\,\frac{R^5}{5}\,\frac23\,2\pi = \frac{4\pi\rho R^5}{15} \quad &\text{(product of the factors)} \\
> I_x &= I_y = \tfrac12\,(2I_O - I_z) = \tfrac12\Big(\frac{4\pi\rho R^5}{5}-\frac{4\pi\rho R^5}{15}\Big) = \frac{4\pi\rho R^5}{15} \quad &\text{(Eq. 10.13; $I_x = I_y$ by the axial symmetry)} \\
> P_{xz,yz} &= P_{xy,yz} = 0,\qquad P_{xy,xz} = 0 \quad &\text{($Oyz$ and $Oxz$ are planes of symmetry; each product involves one of them)}
> \end{aligned}$$
>
> $$\boxed{I_x = I_y = I_z = \tfrac25\,mR^2,\qquad I_O = \tfrac35\,mR^2,\qquad \text{all products about } O \text{ zero}}$$
>
> **Units:** $[\mathrm{M\,L^{-3}}][\mathrm L^5] = \mathrm{kg\,m^2}$; with $m$ from the previous box the ratios are dimensionless
> **Meaning:** about $O$ the hemisphere has the moments of a full sphere per unit mass: the mirror half below $Oxy$ would add an equal contribution. The tensor about $O$ is a multiple of the unit tensor, so every axis through $O$ is principal.

## 14. The tensor of inertia

> [!summary] What you need to know
> - The **tensor of inertia** about $O$ puts all the moments and products about $O$ into one symmetric $3\times 3$ matrix: moments on the diagonal, products with a minus sign off it.
> - With it, the moment of inertia about any line through $O$ (unit vector $\mathbf u$) is a single matrix product.
> - Two planes of symmetry make every product zero: the matrix is diagonal and the coordinate axes are principal.
>
> $$\boxed{[\boldsymbol{\mathcal I}_O]_{00} = \begin{bmatrix} I_x & -P_{xz,yz} & -P_{xy,yz} \\ -P_{xz,yz} & I_y & -P_{xy,xz} \\ -P_{xy,yz} & -P_{xy,xz} & I_z \end{bmatrix},\qquad I_\ell = [\mathbf u]_0^T\,[\boldsymbol{\mathcal I}_O]_{00}\,[\mathbf u]_0}$$
>
> **Slides:** [Lecture 8, Slide 13]; Notes.pdf, Eq. 10.38; Notes.pdf, Eq. 10.39

The moments and products of inertia appear in the dynamics of material systems as the components of one second-order tensor, the tensor of inertia (Notes.pdf, Sec. 10.6). The notes define it directly; Chapter 11 shows that it is the tensor that turns the angular velocity of a rigid body into its angular momentum and kinetic energy (Notes.pdf, Sec. 11.2), which is why it "describes the rotational inertia" of the body ([Lecture 8, Slide 12]).

| Symbol | Meaning |
| :--- | :--- |
| $\boldsymbol{\mathcal I}_O$ | tensor of inertia of the material system about the point $O$, origin of $S_0$ |
| $[\boldsymbol{\mathcal I}_O]_{00}$ | its components in $\mathcal B_0\otimes\mathcal B_0$ |
| $\ell$, $\mathbf u$ | a line through $O$ and its unit vector |
| $I_\ell$ | moment of inertia about the line $\ell$ |
| $\mathbf u_1$, $\mathbf u_2$ | unit normals of two orthogonal planes through $O$ |

> [!derivation] Definition and components of the tensor of inertia
> **Law:** definition of the tensor of inertia; components of the unit tensor and of a dyad
> **Source:** Notes.pdf, Eq. 10.35; Notes.pdf, Eq. 10.36; Notes.pdf, Eq. 10.37; Notes.pdf, Eq. 10.38; [Lecture 8, Slide 12]
>
> $$\begin{aligned}
> \boldsymbol{\mathcal I}_O &= \int_{\mathcal D}\Big[(r_0^P)^2\,\boldsymbol{\mathcal U} - \mathbf r_0^P\otimes\mathbf r_0^P\Big]\,dm \quad &\text{(definition, Eq. 10.35)} \\
> \big[(r_0^P)^2\,\boldsymbol{\mathcal U}\big]_{00} &= \begin{bmatrix} x^2+y^2+z^2 & 0 & 0 \cr 0 & x^2+y^2+z^2 & 0 \cr 0 & 0 & x^2+y^2+z^2 \end{bmatrix} \quad &\text{(Eq. 10.36: $(r_0^P)^2$ times the identity)} \\
> \big[\mathbf r_0^P\otimes\mathbf r_0^P\big]_{00} &= \begin{bmatrix} x^2 & xy & xz \cr xy & y^2 & yz \cr xz & yz & z^2 \end{bmatrix} \quad &\text{(Eq. 10.37: column times row, Eq. 1.48)} \\
> [\boldsymbol{\mathcal I}_O]_{00} &= \int_{\mathcal D}\begin{bmatrix} y^2+z^2 & -xy & -xz \cr -xy & x^2+z^2 & -yz \cr -xz & -yz & x^2+y^2 \end{bmatrix}dm \quad &\text{(subtract entry by entry; the basis is constant, so the integral acts on each entry)} \\
> &= \begin{bmatrix} I_x & -P_{xz,yz} & -P_{xy,yz} \cr -P_{xz,yz} & I_y & -P_{xy,xz} \cr -P_{xy,yz} & -P_{xy,xz} & I_z \end{bmatrix} \quad &\text{(identify each entry with Eqs. 10.11 and 10.15)}
> \end{aligned}$$
>
> $$\boxed{[\boldsymbol{\mathcal I}_O]_{00} = \begin{bmatrix} I_x & -P_{xz,yz} & -P_{xy,yz} \cr -P_{xz,yz} & I_y & -P_{xy,xz} \cr -P_{xy,yz} & -P_{xy,xz} & I_z \end{bmatrix}_{00}}$$
>
> **Units:** every entry in $[\mathrm{M\,L^2}]$, $\mathrm{kg\,m^2}$
> **Meaning:** the diagonal holds the moments of inertia about the coordinate axes and the off-diagonal entries the products of inertia with a minus sign; the entry in row $x$ and column $y$ is minus the product of the two planes normal to $Ox$ and $Oy$. The matrix is symmetric, and its second-moment part is $\mathcal M_{O,2}^{\mathcal D}$.

![[attachments/EM-T/t6-tensor-axis.svg]]

> [!derivation] Moment of inertia about any line through O
> **Law:** Pythagoras for the distance to a line; contraction of the unit tensor and of a dyad
> **Source:** Notes.pdf, Eq. 10.39; Notes.pdf, Eq. 1.36; [Lecture 8, Slide 13]
>
> The vector $\mathbf r_0^P$ is the hypotenuse of a right triangle whose leg along $\ell$ is the projection $\mathbf r_0^P\cdot\mathbf u$ and whose other leg is the distance $d$ to the line.
>
> $$\begin{aligned}
> d^2 &= (r_0^P)^2 - (\mathbf r_0^P\cdot\mathbf u)^2 \quad &\text{(Pythagoras in that right triangle)} \\
> \mathbf u\cdot\boldsymbol{\mathcal U}\cdot\mathbf u &= \mathbf u\cdot\mathbf u = 1,\qquad \mathbf u\cdot(\mathbf r_0^P\otimes\mathbf r_0^P)\cdot\mathbf u = (\mathbf u\cdot\mathbf r_0^P)(\mathbf r_0^P\cdot\mathbf u) \quad &\text{(unit tensor; Eq. 1.36)} \\
> d^2 &= \mathbf u\cdot\Big[(r_0^P)^2\,\boldsymbol{\mathcal U} - \mathbf r_0^P\otimes\mathbf r_0^P\Big]\cdot\mathbf u \quad &\text{(write both terms as contractions)} \\
> I_\ell &= \int_{\mathcal D}d^2\,dm = \mathbf u\cdot\Big\{\int_{\mathcal D}\Big[(r_0^P)^2\,\boldsymbol{\mathcal U} - \mathbf r_0^P\otimes\mathbf r_0^P\Big]dm\Big\}\cdot\mathbf u \quad &\text{(Eq. 10.9; the constant $\mathbf u$ leaves the integral)}
> \end{aligned}$$
>
> $$\boxed{I_\ell = \mathbf u\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf u = [\mathbf u]_0^{T}[\boldsymbol{\mathcal I}_O]_{00}[\mathbf u]_0}$$
>
> **Units:** $[\mathrm{M\,L^2}]$ times two dimensionless unit vectors: $\mathrm{kg\,m^2}$
> **Meaning:** the six independent components of the tensor give the moment of inertia about every line through $O$; with $\mathbf u$ equal to $\mathbf i$ the formula returns the first diagonal entry, $I_x$. Since every $d^2$ is never negative, the tensor is positive semi-definite ([Lecture 8, Slide 12]; see the erratum of Section 12).

> [!derivation] Product of inertia of any two orthogonal planes through O
> **Law:** signed distance to a plane through $O$; orthogonality of the normals
> **Source:** Notes.pdf, Eq. 10.40; Notes.pdf, Eq. 10.14; Notes.pdf, Eq. 1.36
>
> $$\begin{aligned}
> d_1 &= \mathbf r_0^P\cdot\mathbf u_1,\qquad d_2 = \mathbf r_0^P\cdot\mathbf u_2 \quad &\text{(signed distance: projection on the normal of each plane)} \\
> \mathbf u_1\cdot\boldsymbol{\mathcal U}\cdot\mathbf u_2 &= \mathbf u_1\cdot\mathbf u_2 = 0 \quad &\text{(the planes are orthogonal, so are their normals)} \\
> -\mathbf u_1\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf u_2 &= -\int_{\mathcal D}\Big[(r_0^P)^2\cdot 0 - (\mathbf u_1\cdot\mathbf r_0^P)(\mathbf r_0^P\cdot\mathbf u_2)\Big]dm = \int_{\mathcal D}d_1\,d_2\,dm \quad &\text{(Eq. 10.35 contracted; Eq. 1.36)}
> \end{aligned}$$
>
> $$\boxed{P_{\pi_1,\pi_2} = -\,\mathbf u_1\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf u_2}$$
>
> **Units:** $\mathrm{kg\,m^2}$
> **Meaning:** reversing one normal reverses the sign of the product (Notes.pdf, Sec. 10.6, footnote 17); with $\mathbf u_1$ equal to $\mathbf j$ and $\mathbf u_2$ equal to $\mathbf i$ the formula returns $P_{xz,yz}$, the entry of the matrix with its minus sign removed.

> [!derivation] Third symmetry theorem: two planes of symmetry make the tensor diagonal
> **Law:** second symmetry theorem applied to two coordinate planes
> **Source:** [Lecture 8, Slide 13]; Notes.pdf, Sec. 10.4; Notes.pdf, Eq. 10.38
>
> $$\begin{aligned}
> Oyz \text{ symmetric} &\Rightarrow P_{xz,yz} = P_{xy,yz} = 0 \quad &\text{(the two products that involve $Oyz$, Section 12)} \\
> Oxz \text{ symmetric} &\Rightarrow P_{xz,yz} = P_{xy,xz} = 0 \quad &\text{(the two products that involve $Oxz$)} \\
> [\boldsymbol{\mathcal I}_O]_{00} &= \begin{bmatrix} I_x & 0 & 0 \cr 0 & I_y & 0 \cr 0 & 0 & I_z \end{bmatrix}_{00} \quad &\text{(the three products vanish in Eq. 10.38)}
> \end{aligned}$$
>
> $$\boxed{\text{two coordinate planes of symmetry} \Rightarrow [\boldsymbol{\mathcal I}_O]_{00} \text{ diagonal: } \mathbf i,\ \mathbf j,\ \mathbf k \text{ are principal}}$$
>
> **Units:** $\mathrm{kg\,m^2}$
> **Meaning:** each coordinate plane appears in two of the three products, and two different planes together appear in all three, so two planes of symmetry cancel every product. The plate and the half sphere of Section 13 have two planes of symmetry through $O$; the half disk has one and lies in $Oxy$, which cancels the other two products; all three have diagonal tensors about $O$.

> [!derivation] Extension: moment of the rectangular plate about its diagonal
> **Law:** moment about a line through $O$ from the tensor of inertia
> **Source:** Notes.pdf, Eq. 10.39; Notes.pdf, Eq. 10.25; Notes.pdf, Eq. 10.26
>
> The diagonal of the plate of Section 13 passes through $G \equiv O$ with unit vector along $(L, W, 0)$; the tensor about $O$ is diagonal by the third symmetry theorem.
>
> $$\begin{aligned}
> [\mathbf u]_0 &= \frac{1}{\sqrt{L^2+W^2}}\begin{bmatrix} L \cr W \cr 0 \end{bmatrix} \quad &\text{(diagonal direction, normalised)} \\
> I_\ell &= \frac{1}{L^2+W^2}\begin{bmatrix} L & W & 0 \end{bmatrix}\begin{bmatrix} \tfrac{1}{12}MW^2 & 0 & 0 \cr 0 & \tfrac{1}{12}ML^2 & 0 \cr 0 & 0 & \tfrac{1}{12}M(L^2+W^2) \end{bmatrix}\begin{bmatrix} L \cr W \cr 0 \end{bmatrix} \quad &\text{(Eq. 10.39 in matrix form)} \\
> &= \frac{1}{L^2+W^2}\Big(\tfrac{1}{12}MW^2L^2 + \tfrac{1}{12}ML^2W^2\Big) \quad &\text{(row times matrix times column)}
> \end{aligned}$$
>
> $$\boxed{I_\ell = \frac{ML^2W^2}{6\,(L^2+W^2)}}$$
>
> **Units:** $[\mathrm M][\mathrm L^4]/[\mathrm L^2] = \mathrm{kg\,m^2}$
> **Meaning:** for a square plate, with $L$ and $W$ both equal to $a$, the result is $Ma^2/12$, the same as about $Ox$: the in-plane moment of a square about its centre is the same for every direction.

## 15. Change of basis of the tensor and principal axes of inertia

> [!summary] What you need to know
> - To write the tensor in a rotated basis, multiply by the rotation matrix on both sides (transpose on the left).
> - **Principal axes** are the directions in which the tensor is diagonal. They are the eigenvectors of its matrix, and the **principal moments** are the eigenvalues.
> - Principal directions of different principal moments are perpendicular, so the principal basis is orthonormal.
> - The symmetries of the body often give the principal axes without solving anything.
>
> $$\boxed{[\boldsymbol{\mathcal I}_O]_{11} = [{}_0R_1]^T\,[\boldsymbol{\mathcal I}_O]_{00}\,[{}_0R_1],\qquad \det\big([\boldsymbol{\mathcal I}_O]_{00} - I\,\mathbb 1\big) = 0}$$
>
> **Slides:** [Lecture 8, Slide 6]; [Lecture 8, Slide 13]; Notes.pdf, Eq. 10.41; Notes.pdf, Eq. 10.43

A tensor and a vector can only be contracted when both are written in consistent bases: if the tensor is in $\mathcal B_0\otimes\mathcal B_0$, the vector must be in $\mathcal B_0$ (Notes.pdf, Sec. 10.7). A change of basis changes the component matrix, never the tensor, just as for a vector.

| Symbol | Meaning |
| :--- | :--- |
| $\mathcal B_1$ | a rotated orthonormal basis $\{\mathbf i_1,\mathbf j_1,\mathbf k_1\}$ |
| $[{}_0R_1]$ | change of basis matrix from $\mathcal B_1$ to $\mathcal B_0$: column $n$ holds vector $n$ of $\mathcal B_1$ in $\mathcal B_0$ (Section 6) |
| $[\boldsymbol{\mathcal I}_O]_{11}$ | components of the same tensor in $\mathcal B_1\otimes\mathcal B_1$ |
| $\mathbf e_1$, $\mathbf e_2$, $\mathbf e_3$; $I_1$, $I_2$, $I_3$ | principal directions (unit eigenvectors) and principal moments (eigenvalues) |

> [!derivation] Components of the tensor of inertia in a rotated basis
> **Law:** components of a second-order tensor as double contractions; change of basis of vectors
> **Source:** Notes.pdf, Eq. 10.41; [Lecture 8, Slide 5]; [Lecture 8, Slide 13]; Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14
>
> Write the vectors of $\mathcal B_1$ as $\mathbf b_1$, $\mathbf b_2$, $\mathbf b_3$ (that is $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$).
>
> $$\begin{aligned}
> \big([\boldsymbol{\mathcal I}_O]_{11}\big)_{mn} &= \mathbf b_m\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf b_n \quad &\text{(entry $mn$ in $\mathcal B_1\otimes\mathcal B_1$: contract with the $m$-th and $n$-th basis vectors)} \\
> &= [\mathbf b_m]_0^{T}\,[\boldsymbol{\mathcal I}_O]_{00}\,[\mathbf b_n]_0 \quad &\text{(evaluate the scalar with every factor in $\mathcal B_0$, Section 10)} \\
> [\mathbf b_n]_0 &= \text{column } n \text{ of } [{}_0R_1] \quad &\text{(definition of the change of basis matrix)} \\
> [\boldsymbol{\mathcal I}_O]_{11} &= [{}_0R_1]^{T}\,[\boldsymbol{\mathcal I}_O]_{00}\,[{}_0R_1] \quad &\text{(the nine entries at once: rows of $[{}_0R_1]^{T}$ times columns of $[{}_0R_1]$)} \\
> [\boldsymbol{\mathcal I}_O]_{00} &= [{}_0R_1]\,[\boldsymbol{\mathcal I}_O]_{11}\,[{}_0R_1]^{T} \quad &\text{(invert: $[{}_0R_1]^{-1} = [{}_0R_1]^{T}$, Section 6)}
> \end{aligned}$$
>
> $$\boxed{[\boldsymbol{\mathcal I}_O]_{11} = [{}_0R_1]^{T}\cdot[\boldsymbol{\mathcal I}_O]_{00}\cdot[{}_0R_1]}$$
>
> **Units:** $[{}_0R_1]$ is dimensionless, so both matrices are in $\mathrm{kg\,m^2}$
> **Meaning:** the rule holds for every second-order tensor; the slides write the left factor as $[{}_1R_0]$, which is the same matrix because a rotation matrix is orthogonal. A symmetric matrix stays symmetric, since the transpose of the product is the product of the transposes in reverse order.

### Principal axes of inertia

There is always a rotated basis in which the tensor of inertia is diagonal; its directions are the principal axes (directions) of inertia and its diagonal entries the principal moments of inertia (Notes.pdf, Sec. 10.7.1; [Lecture 8, Slide 13]). Because the tensor is symmetric, the spectral theorem of linear algebra guarantees that they exist and that the principal moments are real ([Lecture 8, Slide 6]).

![[attachments/EM-T/t6-principal-axes.svg]]

> [!derivation] Principal moments and directions as an eigenvalue problem
> **Law:** diagonal form of the tensor; eigenvalue problem of a symmetric tensor
> **Source:** Notes.pdf, Eq. 10.42; Notes.pdf, Eq. 10.43; [Lecture 8, Slide 6]; [Lecture 8, Slide 13]
>
> $$\begin{aligned}
> [\boldsymbol{\mathcal I}_O]_{11} &= \begin{bmatrix} I_1 & 0 & 0 \cr 0 & I_2 & 0 \cr 0 & 0 & I_3 \end{bmatrix}_{11} \quad &\text{(principal basis $\mathcal B_1$ of vectors $\mathbf e_1$, $\mathbf e_2$, $\mathbf e_3$, Eq. 10.42)} \\
> \boldsymbol{\mathcal I}_O\cdot\mathbf e_i &= I_i\,\mathbf e_i \quad &\text{(column $i$ of a diagonal matrix: Eq. 10.43, no sum over $i$)} \\
> \big([\boldsymbol{\mathcal I}_O]_{00} - I_i\,\mathbb 1\big)[\mathbf e_i]_0 &= \mathbf 0 \quad &\text{(the same equation in $\mathcal B_0$; $\mathbb 1$ is the identity matrix)} \\
> \det\big([\boldsymbol{\mathcal I}_O]_{00} - I\,\mathbb 1\big) &= 0 \quad &\text{(a non-zero solution needs a singular matrix: cubic in $I$)} \\
> I_i &= \mathbf e_i\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf e_i \geq 0 \quad &\text{(Eq. 10.39 with the unit vector $\mathbf e_i$: each principal moment is the moment about its axis)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol{\mathcal I}_O\cdot\mathbf e_i = I_i\,\mathbf e_i,\qquad \det\big([\boldsymbol{\mathcal I}_O]_{00} - I\,\mathbb 1\big) = 0}$$
>
> **Units:** the eigenvalues $I_i$ in $\mathrm{kg\,m^2}$; the eigenvectors are unit vectors, dimensionless
> **Meaning:** the three roots of the cubic are the principal moments and the unit solutions of each linear system the principal directions; symmetries of the body often give them without solving anything ([Lecture 8, Slide 13]).

> [!derivation] Principal directions of different principal moments are orthogonal
> **Law:** symmetry of the tensor of inertia
> **Source:** [Lecture 8, Slide 6]; Notes.pdf, Sec. 10.7.1; Notes.pdf, Eq. 10.38
>
> $$\begin{aligned}
> \mathbf e_i\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf e_j &= \mathbf e_i\cdot(I_j\,\mathbf e_j) = I_j\,(\mathbf e_i\cdot\mathbf e_j) \quad &\text{(contract Eq. 10.43 for $\mathbf e_j$ with $\mathbf e_i$ on the left)} \\
> \mathbf e_i\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf e_j &= \mathbf e_j\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf e_i = I_i\,(\mathbf e_i\cdot\mathbf e_j) \quad &\text{(symmetric matrix: $[\mathbf a]^{T}[\boldsymbol{\mathcal I}][\mathbf b] = [\mathbf b]^{T}[\boldsymbol{\mathcal I}][\mathbf a]$)} \\
> (I_i - I_j)\,(\mathbf e_i\cdot\mathbf e_j) &= 0 \quad &\text{(subtract the two lines)}
> \end{aligned}$$
>
> $$\boxed{I_i \neq I_j \Rightarrow \mathbf e_i\cdot\mathbf e_j = 0}$$
>
> **Units:** $\mathrm{kg\,m^2}$ times a dimensionless dot product
> **Meaning:** principal directions of distinct principal moments are automatically orthogonal; when two principal moments coincide, every direction of their plane is principal and an orthonormal pair is chosen in it. Either way the principal basis is orthonormal, and it is chosen right-handed.

> [!derivation] Extension: principal axes of a square plate about a corner
> **Law:** Eq. 10.11 and Eq. 10.15 from the corner; eigenvalue problem; change of basis of the tensor
> **Source:** Notes.pdf, Eq. 10.27; Notes.pdf, Eq. 10.41; Notes.pdf, Eq. 10.43
>
> The plate of Section 13 with $L$ and $W$ both equal to $a$, about its corner $A$ in the frame $S_1$ (coordinates $x$, $y$ from the corner, $dm$ equal to $M\,dx\,dy/a^2$).
>
> $$\begin{aligned}
> I_{x_1} &= \frac{M}{a^2}\int_0^{a}\int_0^{a}y^2\,dx\,dy = \frac{M}{a^2}\,\big[x\big]_0^{a}\Big[\frac{y^3}{3}\Big]_0^{a} = \tfrac13 Ma^2 \quad &\text{(Eq. 10.11 with $z$ zero; Barrow)} \\
> I_{y_1} &= \tfrac13 Ma^2,\qquad I_{z_1} = I_{x_1} + I_{y_1} = \tfrac23 Ma^2,\qquad P_{x_1z_1,y_1z_1} = \tfrac14 Ma^2 \quad &\text{(same steps with $x^2$; flat body; Eq. 10.27)} \\
> [\boldsymbol{\mathcal I}_A]_{11} &= Ma^2\begin{bmatrix} \tfrac13 & -\tfrac14 & 0 \cr -\tfrac14 & \tfrac13 & 0 \cr 0 & 0 & \tfrac23 \end{bmatrix} \quad &\text{(Eq. 10.38: the other two products vanish, plate in $Ax_1y_1$)} \\
> \Big(\tfrac13 - \tfrac{I}{Ma^2}\Big)^2 - \tfrac{1}{16} &= 0 \quad &\text{(characteristic equation of the in-plane block; $\mathbf k_1$ is already principal)} \\
> \frac{I}{Ma^2} &= \tfrac13 \mp \tfrac14 = \tfrac{1}{12},\ \tfrac{7}{12} \quad &\text{(square root of both sides)} \\
> \mathbf e_1 &= \tfrac{1}{\sqrt2}(\mathbf i_1+\mathbf j_1),\quad \mathbf e_2 = \tfrac{1}{\sqrt2}(-\mathbf i_1+\mathbf j_1),\quad \mathbf e_3 = \mathbf k_1 \quad &\text{(solve each system: $\tfrac{1}{12}$ gives equal components, $\tfrac{7}{12}$ opposite ones)} \\
> [{}_1R_2] &= \frac{1}{\sqrt2}\begin{bmatrix} 1 & -1 & 0 \cr 1 & 1 & 0 \cr 0 & 0 & \sqrt2 \end{bmatrix},\quad \det = \tfrac12(1+1) = 1,\quad [{}_1R_2][{}_1R_2]^{T} = \mathbb 1 \quad &\text{(columns: principal vectors; a rotation of $\pi/4$ about $\mathbf k_1$, which points out of the paper)} \\
> [{}_1R_2]^{T}[\boldsymbol{\mathcal I}_A]_{11}[{}_1R_2] &= Ma^2\,\mathrm{diag}\Big(\tfrac{1}{12},\ \tfrac{7}{12},\ \tfrac23\Big) \quad &\text{(Eq. 10.41: the off-diagonal entries cancel)}
> \end{aligned}$$
>
> $$\boxed{I_1 = \tfrac{1}{12}Ma^2 \text{ along the diagonal},\qquad I_2 = \tfrac{7}{12}Ma^2,\qquad I_3 = \tfrac23 Ma^2 \text{ along } \mathbf k_1}$$
>
> **Units:** $\mathrm{kg\,m^2}$; the rotation matrix is dimensionless
> **Meaning:** about the corner the axes along the sides are not principal, because the product of inertia is non-zero; the principal axes are the diagonal of the square through $A$, which is a line of symmetry of the plate, and the line perpendicular to it. The smallest moment is about the diagonal, along which the mass lies closest. The sum of the in-plane principal moments, $\tfrac23 Ma^2$, equals $I_3$, as a flat body requires.

## 16. Change of reference point: Steiner's theorem

> [!summary] What you need to know
> - **Steiner's theorem** moves the tensor of inertia from the centre of mass $G$ to any other point $O$: add the tensor of a single particle of mass $m$ placed at $G$.
> - It only links $G$ with another point. To go from $A$ to $B$, go from $A$ to $G$ (subtract), then from $G$ to $B$ (add).
> - Both tensors must be written in parallel bases.
> - **Parallel axis theorem:** the moment about an axis is the moment about the parallel axis through $G$ plus $m$ times the squared distance between the two axes. The axis through $G$ gives the smallest moment.
>
> $$\boxed{\boldsymbol{\mathcal I}_O = \boldsymbol{\mathcal I}_G + m\Big[(r_0^G)^2\,\boldsymbol{\mathcal U} - \mathbf r_0^G\otimes\mathbf r_0^G\Big],\qquad I_{z_0} = I_{z_G} + m\Big[(x_0^G)^2+(y_0^G)^2\Big]}$$
>
> **Slides:** [Lecture 8, Slide 14]; [Lecture 8, Slide 15]; [Lecture 8, Slide 16]; Notes.pdf, Eq. 10.48

The tensor of inertia depends on the point about which it is taken. Steiner's theorem relates the tensor about any point $O$ to the tensor about the centre of mass $G$ (Notes.pdf, Sec. 10.8; [Lecture 8, Slides 14-15]).

| Symbol | Meaning |
| :--- | :--- |
| $S_G = \{G;\mathcal B_0\}$ | frame with origin at $G$ and the same basis as $S_0$ (parallel to it) |
| $\mathbf r_G^P$ | position of the mass element relative to $G$, components $x_G^P$, $y_G^P$, $z_G^P$ |
| $\mathbf r_0^G$ | position of $G$ in $S_0$, components $x_0^G$, $y_0^G$, $z_0^G$ |
| $\boldsymbol{\mathcal I}_G$ | tensor of inertia about $G$ |
| $I_{z_G}$, $I_{z_0}$ | moments of inertia about the parallel axes $Gz_G$ and $Oz_0$ |

![[attachments/EM-T/t6-steiner.svg]]

> [!derivation] The first moment about the centre of mass vanishes
> **Law:** definition of the centre of mass; linearity of the integral
> **Source:** Notes.pdf, Eq. 10.44; Notes.pdf, Eq. 10.45; Notes.pdf, Eq. 10.46; [Lecture 8, Slide 14]
>
> $$\begin{aligned}
> \mathbf r_0^P &= \mathbf r_0^G + \mathbf r_G^P \quad &\text{(vector sum, $\mathbf{OP} = \mathbf{OG} + \mathbf{GP}$)} \\
> \int_{\mathcal D}\mathbf r_G^P\,dm &= \int_{\mathcal D}\mathbf r_0^P\,dm - \mathbf r_0^G\int_{\mathcal D}dm = m\,\mathbf r_0^G - m\,\mathbf r_0^G = \mathbf 0 \quad &\text{($\mathbf r_0^G$ is constant over the body; Eqs. 10.6 and 10.7; Eq. 10.44)} \\
> \int_{\mathcal D}(\mathbf r_0^G\cdot\mathbf r_G^P)\,\boldsymbol{\mathcal U}\,dm &= \Big(\mathbf r_0^G\cdot\int_{\mathcal D}\mathbf r_G^P\,dm\Big)\boldsymbol{\mathcal U} = \mathbf 0 \quad &\text{(constant factors leave the integral; Eq. 10.45)} \\
> \int_{\mathcal D}(\mathbf r_G^P\otimes\mathbf r_0^G)\,dm &= \Big(\int_{\mathcal D}\mathbf r_G^P\,dm\Big)\otimes\mathbf r_0^G = \mathbf 0,\qquad \int_{\mathcal D}(\mathbf r_0^G\otimes\mathbf r_G^P)\,dm = \mathbf 0 \quad &\text{(linearity of the tensor product, Eqs. 1.34-1.35; Eq. 10.46)}
> \end{aligned}$$
>
> $$\boxed{\int_{\mathcal D}\mathbf r_G^P\,dm = \mathbf 0\ \Rightarrow\ \text{every term linear in } \mathbf r_G^P \text{ integrates to zero}}$$
>
> **Units:** $[\mathrm{M\,L}]$ for the first moment, $[\mathrm{M\,L^2}]$ for the two tensor integrals
> **Meaning:** measured from $G$ the mass distribution has no first moment; this is the property that makes $G$ the natural point for inertia.

> [!derivation] Steiner's theorem for the tensor of inertia
> **Law:** definition of the tensor of inertia at $O$ and at $G$; expansion of the square and of the dyad
> **Source:** Notes.pdf, Eq. 10.47; Notes.pdf, Eq. 10.48; [Lecture 8, Slide 14]; [Lecture 8, Slide 15]
>
> $$\begin{aligned}
> (r_0^P)^2 &= (\mathbf r_0^G+\mathbf r_G^P)\cdot(\mathbf r_0^G+\mathbf r_G^P) = (r_0^G)^2 + (r_G^P)^2 + 2\,\mathbf r_0^G\cdot\mathbf r_G^P \quad &\text{(distributive and commutative dot product)} \\
> \mathbf r_0^P\otimes\mathbf r_0^P &= \mathbf r_0^G\otimes\mathbf r_0^G + \mathbf r_G^P\otimes\mathbf r_G^P + \mathbf r_0^G\otimes\mathbf r_G^P + \mathbf r_G^P\otimes\mathbf r_0^G \quad &\text{(bilinearity of the tensor product, Eqs. 1.34-1.35; not commutative, so both cross terms stay)} \\
> \boldsymbol{\mathcal I}_O &= \int_{\mathcal D}\Big[(r_G^P)^2\boldsymbol{\mathcal U} - \mathbf r_G^P\otimes\mathbf r_G^P\Big]dm + \Big[(r_0^G)^2\boldsymbol{\mathcal U} - \mathbf r_0^G\otimes\mathbf r_0^G\Big]\int_{\mathcal D}dm + (\text{terms linear in } \mathbf r_G^P) \quad &\text{(substitute in Eq. 10.35 and group)} \\
> &= \boldsymbol{\mathcal I}_G + m\Big[(r_0^G)^2\boldsymbol{\mathcal U} - \mathbf r_0^G\otimes\mathbf r_0^G\Big] + \mathbf 0 \quad &\text{(Eq. 10.47; Eq. 10.6; Eqs. 10.44 to 10.46)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol{\mathcal I}_O = \boldsymbol{\mathcal I}_G + m\Big[(r_0^G)^2\,\boldsymbol{\mathcal U} - \mathbf r_0^G\otimes\mathbf r_0^G\Big]}$$
>
> **Units:** $[\mathrm{M\,L^2}]$ on both sides: $m$ in $\mathrm{kg}$ times $(r_0^G)^2$ in $\mathrm{m^2}$
> **Meaning:** the tensor about $O$ is the tensor about $G$ plus the tensor about $O$ of a point particle of mass $m$ placed at $G$.

> [!derivation] Steiner's theorem in components
> **Law:** Eqs. 10.36 to 10.38 applied to a single particle of mass $m$ at $G$
> **Source:** Notes.pdf, Eq. 10.48; Notes.pdf, Eq. 10.38; [Lecture 8, Slide 15]
>
> $$\begin{aligned}
> m\Big[(r_0^G)^2\boldsymbol{\mathcal U} - \mathbf r_0^G\otimes\mathbf r_0^G\Big]_{00} &= m\begin{bmatrix} (y_0^G)^2+(z_0^G)^2 & -x_0^Gy_0^G & -x_0^Gz_0^G \cr -x_0^Gy_0^G & (x_0^G)^2+(z_0^G)^2 & -y_0^Gz_0^G \cr -x_0^Gz_0^G & -y_0^Gz_0^G & (x_0^G)^2+(y_0^G)^2 \end{bmatrix} \quad &\text{(Eq. 10.38 with the integral replaced by one particle)} \\
> I_{x} &= I_{x_G} + m\big[(y_0^G)^2+(z_0^G)^2\big] \quad &\text{(diagonal entry $xx$)} \\
> P_{xz,yz} &= P_{x_Gz_G,y_Gz_G} + m\,x_0^G\,y_0^G \quad &\text{(entry $xy$ with its minus sign removed)}
> \end{aligned}$$
>
> $$\boxed{I_{x} = I_{x_G} + m\big[(y_0^G)^2+(z_0^G)^2\big],\qquad P_{xz,yz} = P_{x_Gz_G,y_Gz_G} + m\,x_0^G y_0^G \quad \text{(and cyclically)}}$$
>
> **Units:** $\mathrm{kg\,m^2}$ in every term
> **Meaning:** all the terms must be in the same tensor basis, which is why $S_G$ is taken parallel to $S_0$ (Notes.pdf, Sec. 10.8); if the tensor about $G$ is known in another basis, it is rotated first with Eq. 10.41 ([Lecture 8, Slide 15]).

> [!derivation] From a point A to a point B: Steiner's theorem twice
> **Law:** Steiner's theorem applied from $G$ to each of the two points
> **Source:** Notes.pdf, Sec. 10.8; [Lecture 8, Slide 15]
>
> $$\begin{aligned}
> \boldsymbol{\mathcal I}_A &= \boldsymbol{\mathcal I}_G + m\Big[(r_A^G)^2\boldsymbol{\mathcal U} - \mathbf r_A^G\otimes\mathbf r_A^G\Big] \quad &\text{(Eq. 10.48 with $O$ replaced by $A$; $\mathbf r_A^G$ is $\mathbf{AG}$)} \\
> \boldsymbol{\mathcal I}_G &= \boldsymbol{\mathcal I}_A - m\Big[(r_A^G)^2\boldsymbol{\mathcal U} - \mathbf r_A^G\otimes\mathbf r_A^G\Big] \quad &\text{(first step: from $A$ down to $G$)} \\
> \boldsymbol{\mathcal I}_B &= \boldsymbol{\mathcal I}_G + m\Big[(r_B^G)^2\boldsymbol{\mathcal U} - \mathbf r_B^G\otimes\mathbf r_B^G\Big] \quad &\text{(second step: from $G$ up to $B$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol{\mathcal I}_B = \boldsymbol{\mathcal I}_A - m\Big[(r_A^G)^2\boldsymbol{\mathcal U} - \mathbf r_A^G\otimes\mathbf r_A^G\Big] + m\Big[(r_B^G)^2\boldsymbol{\mathcal U} - \mathbf r_B^G\otimes\mathbf r_B^G\Big]}$$
>
> **Units:** $\mathrm{kg\,m^2}$ in every term
> **Meaning:** the theorem only links a point to the centre of mass; the particle term computed with $\mathbf{AB}$ directly would be wrong, because the cross terms vanish only when the integrals are taken from $G$.

> [!derivation] Check of Eq. 10.27 with Steiner's theorem
> **Law:** Steiner's theorem in components from the centre of the plate to its corner
> **Source:** Notes.pdf, Eq. 10.48; Notes.pdf, Eq. 10.25; Notes.pdf, Eq. 10.26; Notes.pdf, Eq. 10.27
>
> For the plate of Section 13, $G$ is at the centre; seen from the corner $A$, with axes along the sides, $\mathbf r_A^G$ has components $L/2$, $W/2$, $0$.
>
> $$\begin{aligned}
> P_{x_1z_1,y_1z_1} &= 0 + M\,\tfrac{L}{2}\,\tfrac{W}{2} \quad &\text{(central product zero by symmetry; particle term $m\,x_0^G y_0^G$)} \\
> I_{x_1} &= \tfrac{1}{12}MW^2 + M\Big(\tfrac{W}{2}\Big)^2 = \tfrac13 MW^2,\qquad I_{y_1} = \tfrac{1}{12}ML^2 + M\Big(\tfrac{L}{2}\Big)^2 = \tfrac13 ML^2 \quad &\text{(diagonal entries; Eqs. 10.25 and 10.26)}
> \end{aligned}$$
>
> $$\boxed{P_{x_1z_1,y_1z_1} = \tfrac14 MLW \ \text{(Eq. 10.27 confirmed)},\qquad I_{x_1} = \tfrac13 MW^2,\qquad I_{y_1} = \tfrac13 ML^2}$$
>
> **Units:** $\mathrm{kg\,m^2}$
> **Meaning:** the direct integral from the corner and Steiner's theorem agree; with $L$ and $W$ both equal to $a$ they also reproduce the corner tensor used for the principal axes in Section 15.

### Parallel axis theorem

Often only the moment of inertia about an axis $Gz_G$ through $G$ is known and the moment about a parallel axis $Oz_0$ is needed, as in planar problems, where only the moment about the axis normal to the plane of motion enters (Notes.pdf, Sec. 10.8.1; [Lecture 8, Slide 16]).

![[attachments/EM-T/t6-parallel-axis.svg]]

> [!derivation] Parallel axis theorem
> **Law:** Eq. 10.11 with the coordinates split at $G$; Eq. 10.44
> **Source:** Notes.pdf, Sec. 10.8.1; Notes.pdf, Eq. 10.44; [Lecture 8, Slide 16]
>
> $$\begin{aligned}
> x_0^P &= x_0^G + x_G^P,\qquad y_0^P = y_0^G + y_G^P \quad &\text{(components of $\mathbf r_0^P = \mathbf r_0^G + \mathbf r_G^P$)} \\
> I_{z_0} &= \int_{\mathcal D}\Big[(x_0^P)^2+(y_0^P)^2\Big]dm = \int_{\mathcal D}\Big[(x_G^P)^2+(x_0^G)^2+2x_G^Px_0^G+(y_G^P)^2+(y_0^G)^2+2y_G^Py_0^G\Big]dm \quad &\text{(Eq. 10.11; expand both squares)} \\
> &= \int_{\mathcal D}\Big[(x_G^P)^2+(y_G^P)^2\Big]dm + \Big[(x_0^G)^2+(y_0^G)^2\Big]\int_{\mathcal D}dm + 2x_0^G\int_{\mathcal D}x_G^P\,dm + 2y_0^G\int_{\mathcal D}y_G^P\,dm \quad &\text{(constants leave the integrals)} \\
> &= I_{z_G} + m\Big[(x_0^G)^2+(y_0^G)^2\Big] + 0 + 0 \quad &\text{(Eq. 10.11 at $G$; Eq. 10.6; components of Eq. 10.44)}
> \end{aligned}$$
>
> $$\boxed{I_{z_0} = I_{z_G} + m\Big[(x_0^G)^2+(y_0^G)^2\Big] \geq I_{z_G}}$$
>
> **Units:** $\mathrm{kg\,m^2}$: $m$ times the square of the distance between the two axes
> **Meaning:** the bracket is the squared distance between the parallel axes, so the moment about an axis through $G$ is the smallest of all the moments about axes parallel to it, wherever $O$ is. It is the $zz$ entry of Steiner's theorem.

> [!derivation] Extension: central moments of the wire and of the half sphere
> **Law:** parallel axis theorem used from $O$ down to $G$
> **Source:** Notes.pdf, Sec. 10.8.1; Notes.pdf, Eq. 10.19; Notes.pdf, Eq. 10.20; Notes.pdf, Eq. 10.34
>
> $$\begin{aligned}
> I_{z_G}^{\text{wire}} &= I_z - m\Big(\tfrac{2R}{\pi}\Big)^2 = mR^2\Big(1 - \tfrac{4}{\pi^2}\Big) \quad &\text{(Eq. 10.20; $G$ at distance $2R/\pi$ from $Oz$, Eq. 10.19)} \\
> I_{x_G}^{\text{sphere}} &= I_x - m\Big(\tfrac{3R}{8}\Big)^2 = mR^2\Big(\tfrac25 - \tfrac{9}{64}\Big) = \tfrac{128-45}{320}\,mR^2 \quad &\text{($I_x$ from Section 13; $G$ at height $3R/8$, Eq. 10.34, so at that distance from $Ox$)} \\
> I_{z_G}^{\text{sphere}} &= I_z = \tfrac25 mR^2 \quad &\text{($G$ lies on $Oz$: zero distance between the axes)}
> \end{aligned}$$
>
> $$\boxed{I_{z_G}^{\text{wire}} = \Big(1-\tfrac{4}{\pi^2}\Big)mR^2 \approx 0.595\,mR^2,\qquad I_{x_G}^{\text{sphere}} = I_{y_G}^{\text{sphere}} = \tfrac{83}{320}\,mR^2,\quad I_{z_G}^{\text{sphere}} = \tfrac25\,mR^2}$$
>
> **Units:** $\mathrm{kg\,m^2}$
> **Meaning:** both central moments are smaller than those about $O$, as the theorem requires; the subtraction always goes from a known moment towards $G$, never between two points that are both away from $G$.

> [!key] Computing the inertia properties of a rigid body ([Lecture 8, Slide 17])
> The mass, centre of mass and tensor of inertia need triple integrals. Look for symmetries first: they place $G$ and cancel products of inertia. Divide complex geometries into simple parts and add their contributions, about the same point and in the same basis; treat holes by subtraction. Write the volume element in the coordinates that fit the body (Cartesian, cylindrical or spherical, Eq. 10.5) with explicit limits for every coordinate. Take the tensor about $G$, move it to any other point with Steiner's theorem, rotate it with the change of basis matrix, and diagonalise it to get the principal axes and moments.

> [!recap] Review in one minute
> 1. A rigid body keeps its shape; a frame $S_B$ fixed to it moves and turns with it.
> 2. Velocity of any body point: the velocity of a known body point plus $\boldsymbol\omega_{B0}\times\mathbf{PA}$. Acceleration: two more terms.
> 3. All points share the slip velocity along $\boldsymbol\omega_{B0}$; the axis of rotation and slip is where the speed is smallest.
> 4. The fields hold only for body points.
> 5. A change of basis matrix has the new basis vectors as columns, is undone by transposing, and rotations multiply in order.
> 6. Euler angles (3-1-3 or yaw, pitch and roll) give the attitude; the angular velocity is the sum of the three angle rates, each on its own axis; every set has a singular attitude.
> 7. A free rigid body has six degrees of freedom.
> 8. Mass, centre of mass and tensor of inertia are the zeroth, first and second moments of the mass. Use symmetry before integrating.
> 9. The tensor of inertia gives the moment about any line; its eigenvectors are the principal axes.
> 10. Steiner's theorem moves the tensor between $G$ and any point; the axis through $G$ has the smallest moment.
>
> Keep the boxed results of each section at hand: [Engineering Mechanics formula sheet](../formula-sheet/index.html).
