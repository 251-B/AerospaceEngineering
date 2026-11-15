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

## 10. Second-order tensors and the tensor product

The rotational inertia of a body is a second-order tensor, so Lecture 8 opens with the tools needed (Slides 3 to 6; Notes.pdf, Sec. 1.6.5). A second-order tensor $\mathbf T$ is a linear relation between vectors: contracted with a vector on one side it gives a vector, and with a vector on each side it gives a scalar. In a basis $\mathcal B_0$ it is represented by a $3\times 3$ matrix of components, written with the basis as subscripts on both sides; the unit tensor $\boldsymbol{\mathcal U}$ has the identity matrix as components in every orthonormal basis.

> [!derivation] Contractions of a tensor with vectors in components
> **Law:** matrix representation of a tensor in $\mathcal B_0\otimes\mathcal B_0$
> **Source:** [Lecture 8, Slide 3]; Notes.pdf, Eq. 1.41
>
> $$\begin{aligned}
> \mathbf T\cdot\mathbf b &= \mathbf d:\quad d_m = \textstyle\sum_n t_{mn}\,b_n \quad &\text{(matrix times column, components in $\mathcal B_0$)} \\
> \mathbf a\cdot\mathbf T &= \mathbf c:\quad c_n = \textstyle\sum_m a_m\,t_{mn} \quad &\text{(row times matrix)} \\
> \mathbf a\cdot\mathbf T\cdot\mathbf b &= s:\quad s = \textstyle\sum_m\sum_n a_m\,t_{mn}\,b_n \quad &\text{(row times matrix times column)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a\cdot\mathbf T\cdot\mathbf b = [\mathbf a]_0^T\,[\mathbf T]_{00}\,[\mathbf b]_0}$$
>
> **Units:** those of $\mathbf a$, $\mathbf T$ and $\mathbf b$ multiplied
> **Meaning:** all three contractions are matrix products, valid only when every factor is written in the same basis.

> [!derivation] The tensor product of two vectors
> **Law:** bilinearity of the tensor product; components in $\mathcal B_0\otimes\mathcal B_0$
> **Source:** Notes.pdf, Eq. 1.36; Notes.pdf, Eq. 1.48; [Lecture 8, Slide 4]
>
> $$\begin{aligned}
> \mathbf u\otimes\mathbf v &= \textstyle\sum_m\sum_n u_m v_n\,\mathbf e_m\otimes\mathbf e_n \quad &\text{(expand both vectors and use bilinearity, Eqs. 1.34-1.35, 1.44-1.47)} \\
> [\mathbf u\otimes\mathbf v]_{00} &= [\mathbf u]_0\,[\mathbf v]_0^T \quad &\text{(entry $mn$ is $u_m v_n$, Eq. 1.48)} \\
> (\mathbf u\otimes\mathbf v)\cdot\mathbf b &= [\mathbf u]_0\big([\mathbf v]_0^T[\mathbf b]_0\big) = \mathbf u\,(\mathbf v\cdot\mathbf b) \quad &\text{(associativity of the matrix product)} \\
> \mathbf a\cdot(\mathbf u\otimes\mathbf v) &= \big([\mathbf a]_0^T[\mathbf u]_0\big)[\mathbf v]_0^T = (\mathbf a\cdot\mathbf u)\,\mathbf v \quad &\text{(same, on the left)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a\cdot(\mathbf u\otimes\mathbf v)\cdot\mathbf b = (\mathbf a\cdot\mathbf u)(\mathbf v\cdot\mathbf b)}$$
>
> **Units:** products of the units of the four vectors
> **Meaning:** the dyad is a construct "waiting" to be dotted with vectors on either side; since it is sometimes written without the symbol, the dot of a dot product must always be written.

> [!derivation] Components of a tensor in a rotated basis
> **Law:** change of basis of both vectors of the linear relation
> **Source:** [Lecture 8, Slide 5]; Notes.pdf, Eq. 1.14
>
> $$\begin{aligned}
> [\mathbf d]_0 &= [\mathbf T]_{00}\,[\mathbf b]_0 \quad &\text{(the relation, written in $\mathcal B_0$)} \\
> [{}_0R_1]\,[\mathbf d]_1 &= [\mathbf T]_{00}\,[{}_0R_1]\,[\mathbf b]_1 \quad &\text{(change of basis of both vectors)} \\
> [\mathbf d]_1 &= [{}_1R_0]\,[\mathbf T]_{00}\,[{}_0R_1]\,[\mathbf b]_1 \quad &\text{(left-multiply by the inverse $[{}_1R_0]$)} \\
> [{}_1R_0] &= [{}_0R_1]^{-1} = [{}_0R_1]^T \quad &\text{(orthogonality, Eq. 1.14)}
> \end{aligned}$$
>
> $$\boxed{[\mathbf T]_{11} = [{}_1R_0]\,[\mathbf T]_{00}\,[{}_0R_1] = [{}_0R_1]^T\,[\mathbf T]_{00}\,[{}_0R_1]}$$
>
> **Units:** those of the tensor (the matrices are dimensionless)
> **Meaning:** the tensor is the same physical object; only the numbers that represent it change with the basis.

A symmetric tensor (equal to its transpose in any orthonormal basis) always has an orthonormal basis of eigenvectors, its principal directions, in which its matrix is diagonal with the eigenvalues on the diagonal ([Lecture 8, Slide 6]). This is proved for the inertia tensor in Section 17.

## 11. Moments of a mass distribution

A point particle needs only its mass; a rigid body needs its spatial mass distribution $\mathcal D$, which affects its rotational dynamics: a metal bar is harder to set spinning about an axis normal to it than about its own long axis ([Lecture 8, Slide 7]). The total mass, the centre of mass and the inertia tensor are built from the zeroth, first and second moments of $\mathcal D$; the definitions hold for any material system, rigid or not (Notes.pdf, Sec. 10).

![[attachments/EM-T/t6-mass-distribution.svg]]

> [!derivation] Moments of a discrete mass distribution
> **Law:** definition of the n-th moment with the tensor product
> **Source:** Notes.pdf, Eq. 10.1; Notes.pdf, Eq. 10.2
>
> $$\begin{aligned}
> \mathcal M_{O,n}^{\mathcal D} &= \sum_{i=1}^{N} \underbrace{\mathbf r_0^{P_i}\otimes\cdots\otimes\mathbf r_0^{P_i}}_{n}\ m_{P_i} \quad &\text{(definition, Eq. 10.1)} \\
> n = 0:\ \ \mathcal M_{O,0}^{\mathcal D} &= \sum_{i=1}^N m_i \quad &\text{(no position factor: a scalar)} \\
> n = 1:\ \ \mathcal M_{O,1}^{\mathcal D} &= \sum_{i=1}^N \mathbf r_0^{P_i}\,m_i \quad &\text{(one factor: a vector)} \\
> n = 2:\ \ \mathcal M_{O,2}^{\mathcal D} &= \sum_{i=1}^N \mathbf r_0^{P_i}\otimes\mathbf r_0^{P_i}\,m_i \quad &\text{(two factors: a second-order tensor)}
> \end{aligned}$$
>
> $$\boxed{\mathcal M_{O,0}^{\mathcal D} = \sum_i m_i,\quad \mathcal M_{O,1}^{\mathcal D} = \sum_i \mathbf r_0^{P_i} m_i,\quad \mathcal M_{O,2}^{\mathcal D} = \sum_i \mathbf r_0^{P_i}\otimes\mathbf r_0^{P_i}\,m_i}$$
>
> **Units:** $[\mathrm M]$, $[\mathrm{M\,L}]$, $[\mathrm{M\,L^2}]$
> **Meaning:** each moment weighs the positions of the particles with their masses; the order of the moment is the number of position factors.

> [!derivation] Moments of a continuous mass distribution
> **Law:** sums replaced by integrals over the mass element
> **Source:** Notes.pdf, Eq. 10.3; Notes.pdf, Eq. 10.4; [Lecture 8, Slide 8]
>
> $$\begin{aligned}
> \mathcal M_{O,n}^{\mathcal D} &= \int_{\mathcal D} \underbrace{\mathbf r_0^{P}\otimes\cdots\otimes\mathbf r_0^{P}}_{n}\ dm \quad &\text{(integration point $P$ runs over $\mathcal D$, Eq. 10.3)} \\
> dm &= \lambda\,d\ell,\quad dm = \sigma\,dA,\quad dm = \rho\,dV \quad &\text{(1D, 2D and 3D bodies; homogeneous when the density is uniform)}
> \end{aligned}$$
>
> $$\boxed{\mathcal M_{O,0}^{\mathcal D} = \int_{\mathcal D} dm,\quad \mathcal M_{O,1}^{\mathcal D} = \int_{\mathcal D}\mathbf r_0^P\,dm,\quad \mathcal M_{O,2}^{\mathcal D} = \int_{\mathcal D}\mathbf r_0^P\otimes\mathbf r_0^P\,dm}$$
>
> **Units:** $[\mathrm M]$, $[\mathrm{M\,L}]$, $[\mathrm{M\,L^2}]$; densities $[\mathrm{M\,L^{-1}}]$, $[\mathrm{M\,L^{-2}}]$, $[\mathrm{M\,L^{-3}}]$
> **Meaning:** from here on only the integrals are written; discrete masses give the sums of Eq. 10.1.

The difficulty of these integrals is usually to write the length, area or volume element with the differentials of the chosen coordinates and to set the limits. The spherical coordinates of the notes measure $\varphi$ from the equatorial plane $Oxy$ (a latitude), not from the $z$ axis.

![[attachments/EM-T/t6-spherical-coordinates.svg]]

> [!derivation] Volume element in cylindrical and spherical coordinates
> **Law:** change of variables with the Jacobian determinant
> **Source:** Notes.pdf, Eq. 10.5; [Lecture 8, Slide 8]; [Lecture 8, Slide 17]
>
> Cylindrical: $x$ and $y$ are the legs of the right triangle with hypotenuse $R$ (adjacent leg $R\cos\theta$, opposite leg $R\sin\theta$). Spherical: in the meridian plane the hypotenuse is $r$, the leg along $z$ (opposite $\varphi$) is $r\sin\varphi$ and the leg in the $Oxy$ plane (adjacent) is $r\cos\varphi$, which then splits with $\theta$.
>
> $$\begin{aligned}
> (x,y,z) &= (R\cos\theta,\ R\sin\theta,\ z) \quad &\text{(cylindrical coordinates)} \\
> \frac{\partial(x,y,z)}{\partial(R,\theta,z)} &= \begin{vmatrix} \cos\theta & -R\sin\theta & 0 \cr \sin\theta & R\cos\theta & 0 \cr 0 & 0 & 1 \end{vmatrix} = R\cos^2\theta + R\sin^2\theta = R \quad &\text{(expand along the third row)} \\
> (x,y,z) &= (r\cos\varphi\cos\theta,\ r\cos\varphi\sin\theta,\ r\sin\varphi) \quad &\text{(spherical coordinates, latitude $\varphi$)} \\
> \frac{\partial(x,y,z)}{\partial(r,\theta,\varphi)} &= \begin{vmatrix} \cos\varphi\cos\theta & -r\cos\varphi\sin\theta & -r\sin\varphi\cos\theta \cr \cos\varphi\sin\theta & r\cos\varphi\cos\theta & -r\sin\varphi\sin\theta \cr \sin\varphi & 0 & r\cos\varphi \end{vmatrix} \quad &\text{(partial derivatives as columns)} \\
> &= \sin\varphi\,(r^2\sin\varphi\cos\varphi) + r\cos\varphi\,(r\cos^2\varphi) \quad &\text{(expand along the third row; $\sin^2\theta+\cos^2\theta = 1$ in each minor)} \\
> &= r^2\cos\varphi\,(\sin^2\varphi + \cos^2\varphi) = r^2\cos\varphi \quad &\text{(factor)}
> \end{aligned}$$
>
> $$\boxed{dV = dx\,dy\,dz = R\,dR\,d\theta\,dz = r^2\cos\varphi\,dr\,d\theta\,d\varphi}$$
>
> **Units:** $[\mathrm{L^3}]$ in each form ($R$ and $r^2$ supply the lengths that the angles lack)
> **Meaning:** the Jacobian is the volume of the small cell swept by the coordinate increments; for exotic coordinates one starts from Cartesian ones and computes it in the same way.

## 12. Total mass and centre of mass

> [!derivation] Total mass
> **Law:** zeroth moment of the mass distribution
> **Source:** Notes.pdf, Eq. 10.6; [Lecture 8, Slide 9]
>
> $$\begin{aligned}
> m &= \mathcal M_{O,0}^{\mathcal D} \quad &\text{(definition)} \\
> &= \int_{\mathcal D} dm \quad &\text{(Eq. 10.4)}
> \end{aligned}$$
>
> $$\boxed{m = \int_{\mathcal D} dm}$$
>
> **Units:** $[\mathrm M]$, kg
> **Meaning:** the sum of all the mass of the system; it does not depend on the point $O$.

> [!derivation] Centre of mass
> **Law:** the first moment is kept when the whole mass is concentrated at $G$
> **Source:** Notes.pdf, Eq. 10.7; Notes.pdf, Eq. 10.8; [Lecture 8, Slide 9]
>
> $$\begin{aligned}
> m\,\mathbf r_0^G &= \mathcal M_{O,1}^{\mathcal D} \quad &\text{(first moment of the mass $m$ placed at $G$)} \\
> &= \int_{\mathcal D}\mathbf r_0^P\,dm \quad &\text{(Eq. 10.4)} \\
> \mathbf r_0^G &= \frac{1}{m}\int_{\mathcal D}\mathbf r_0^P\,dm \quad &\text{(divide by $m \gt 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G = \frac{1}{m}\int_{\mathcal D}\mathbf r_0^P\,dm = \frac{\mathcal M_{O,1}^{\mathcal D}}{\mathcal M_{O,0}^{\mathcal D}}}$$
>
> **Units:** $[\mathrm{M\,L}]/[\mathrm M] = [\mathrm L]$
> **Meaning:** the centre of mass is the mass-weighted average of the positions of all mass elements.

When the mass distribution has a plane or an axis of symmetry, the centre of mass lies on it (Notes.pdf, Sec. 10.3). This is the first of three symmetry theorems of the topic.

> [!derivation] Symmetry theorem 1: the centre of mass lies on a plane or an axis of symmetry
> **Law:** pairing of symmetric mass elements in the first moment
> **Source:** Notes.pdf, Sec. 10.3; Notes.pdf, Eq. 10.8
>
> Plane of symmetry $Oyz$: for every element $dm$ at $(x,y,z)$ there is an equal element at $(-x,y,z)$, so $\mathcal D$ splits into the half with positive $x$ and its mirror image.
>
> $$\begin{aligned}
> \int_{\mathcal D} x\,dm &= \int_{x\gt 0} x\,dm + \int_{x\gt 0} (-x)\,dm \quad &\text{(mirror element of $dm$ has the same mass and coordinate $-x$)} \\
> &= 0 \quad &\text{(the two halves cancel)} \\
> x_G &= \frac{1}{m}\int_{\mathcal D} x\,dm = 0 \quad &\text{($x$ component of Eq. 10.8)} \\
> \text{axis } Oz:\ \ (x,y,z) &\to (-x,-y,z) \ \Longrightarrow\ \int_{\mathcal D} x\,dm = \int_{\mathcal D} y\,dm = 0 \quad &\text{(same pairing for a half-turn symmetry about the axis)}
> \end{aligned}$$
>
> $$\boxed{\text{plane of symmetry } Oyz \Rightarrow x_G = 0;\qquad \text{axis of symmetry } Oz \Rightarrow x_G = y_G = 0}$$
>
> **Units:** $[\mathrm L]$
> **Meaning:** symmetries locate $G$ before any integral is computed; in the examples only the coordinate along the symmetry axis needs integrating.

## 13. Moments and products of inertia

The moments and products of inertia come from the second moment of $\mathcal D$. They have dimensions $[\mathrm{M\,L^2}]$ and are measured in kg·m² (Notes.pdf, Sec. 10.4). The moment of inertia with respect to a point, a line or a plane uses the distance $d$ of each mass element to that point, line or plane; the moment about an axis is the "resistance" the body offers to changes of its angular velocity about that axis ([Lecture 8, Slide 10]).

> [!derivation] Moments of inertia about a point, the coordinate axes and the coordinate planes
> **Law:** definition with the squared distance; Pythagoras for the distances
> **Source:** Notes.pdf, Eq. 10.9; Notes.pdf, Eq. 10.10; Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.12; [Lecture 8, Slide 10]
>
> $$\begin{aligned}
> I &= \int_{\mathcal D} d^2\,dm \quad &\text{(definition, Eq. 10.9)} \\
> d_O^2 &= \lvert\mathbf r_0^P\rvert^2 = x^2+y^2+z^2 \quad &\text{(distance to the point $O$)} \\
> d_{Ox}^2 &= y^2+z^2,\quad d_{Oy}^2 = x^2+z^2,\quad d_{Oz}^2 = x^2+y^2 \quad &\text{(distance to an axis: legs of the right triangle in the plane normal to it)} \\
> d_{Oxy}^2 &= z^2,\quad d_{Oxz}^2 = y^2,\quad d_{Oyz}^2 = x^2 \quad &\text{(distance to a plane: the coordinate normal to it)}
> \end{aligned}$$
>
> $$\boxed{I_O = \int_{\mathcal D}(x^2+y^2+z^2)\,dm,\quad I_x = \int_{\mathcal D}(y^2+z^2)\,dm,\quad I_y = \int_{\mathcal D}(x^2+z^2)\,dm,\quad I_z = \int_{\mathcal D}(x^2+y^2)\,dm,\quad I_{xy} = \int_{\mathcal D}z^2\,dm,\quad I_{xz} = \int_{\mathcal D}y^2\,dm,\quad I_{yz} = \int_{\mathcal D}x^2\,dm}$$
>
> **Units:** $[\mathrm M][\mathrm{L^2}] = [\mathrm{M\,L^2}]$, kg·m²
> **Meaning:** the integrands are squares, so every moment of inertia is positive; $I_O$ is sometimes called the polar moment of inertia.

> [!derivation] Relation between the moments about the point, the axes and the planes
> **Law:** linearity of the integral; regrouping of the squares
> **Source:** Notes.pdf, Eq. 10.13; [Lecture 8, Slide 10]
>
> $$\begin{aligned}
> I_{xy} + I_{xz} + I_{yz} &= \int_{\mathcal D}(z^2 + y^2 + x^2)\,dm = I_O \quad &\text{(add the three plane moments, Eq. 10.12)} \\
> I_x + I_y + I_z &= \int_{\mathcal D}\big[(y^2+z^2)+(x^2+z^2)+(x^2+y^2)\big]\,dm \quad &\text{(add the three axis moments, Eq. 10.11)} \\
> &= \int_{\mathcal D} 2(x^2+y^2+z^2)\,dm = 2I_O \quad &\text{(each square appears twice)}
> \end{aligned}$$
>
> $$\boxed{2I_O = 2\left(I_{xy}+I_{xz}+I_{yz}\right) = I_x + I_y + I_z}$$
>
> **Units:** $[\mathrm{M\,L^2}]$
> **Meaning:** computing two or three of the simple plane integrals gives all the others, which saves work in the examples.

> [!derivation] Flat plate: the polar moment is the sum of the two in-plane moments
> **Law:** body of negligible thickness in the plane $Oxy$
> **Source:** Notes.pdf, Eq. 10.13; Notes.pdf, Eq. 10.20; Notes.pdf, Eq. 10.22; Notes.pdf, Eq. 10.24
>
> $$\begin{aligned}
> z &= 0 \ \ \text{for every } dm \quad &\text{(planar body in $Oxy$)} \\
> I_x &= \int_{\mathcal D} y^2\,dm,\qquad I_y = \int_{\mathcal D} x^2\,dm \quad &\text{(Eq. 10.11 with zero $z$)} \\
> I_z &= \int_{\mathcal D}(x^2+y^2)\,dm = I_y + I_x \quad &\text{(Eq. 10.11 and linearity)} \\
> I_O &= \int_{\mathcal D}(x^2+y^2+0)\,dm = I_z \quad &\text{(Eq. 10.10)} \\
> I_{xy} &= \int_{\mathcal D} 0\,dm = 0 \quad &\text{(Eq. 10.12: consistent with Eq. 10.13, $2I_O = I_x+I_y+I_z = 2I_z$)}
> \end{aligned}$$
>
> $$\boxed{I_O = I_z = I_x + I_y}$$
>
> **Units:** $[\mathrm{M\,L^2}]$
> **Meaning:** for a flat body the moment about the normal axis through $O$ equals the polar moment and is the sum of the moments about the two in-plane axes (the notes write it as the polar moment equal to the sum of the two in-plane moments).

> [!derivation] Products of inertia
> **Law:** definition with signed distances to two orthogonal planes
> **Source:** Notes.pdf, Eq. 10.14; Notes.pdf, Eq. 10.15; [Lecture 8, Slide 11]
>
> $$\begin{aligned}
> P_{\pi_1,\pi_2} &= \int_{\mathcal D} d_1 d_2\,dm \quad &\text{(definition, Eq. 10.14; $d_1$, $d_2$ signed)} \\
> d_{Oxy} &= z,\quad d_{Oxz} = y,\quad d_{Oyz} = x \quad &\text{(signed distance to a coordinate plane: the coordinate normal to it)}
> \end{aligned}$$
>
> $$\boxed{P_{xy,xz} = \int_{\mathcal D} zy\,dm,\qquad P_{xy,yz} = \int_{\mathcal D} zx\,dm,\qquad P_{xz,yz} = \int_{\mathcal D} yx\,dm}$$
>
> **Units:** $[\mathrm{M\,L^2}]$
> **Meaning:** because the distances are signed a product of inertia can be negative; $P_{xy,xz}$ measures the coupling between rotations about the axes $Oy$ and $Oz$ ([Lecture 8, Slide 11]).

> [!derivation] Symmetry theorem 2: a plane of symmetry cancels the products that involve it
> **Law:** pairing of mirror mass elements
> **Source:** Notes.pdf, Sec. 10.4; [Lecture 8, Slide 11]
>
> Plane of symmetry $Oyz$: the mirror element of $dm$ at $(x,y,z)$ sits at $(-x,y,z)$ with the same mass.
>
> $$\begin{aligned}
> P_{xz,yz} &= \int_{x\gt 0} yx\,dm + \int_{x\gt 0} y(-x)\,dm = 0 \quad &\text{(Eq. 10.15; the signed distance $x$ changes sign, $y$ does not)} \\
> P_{xy,yz} &= \int_{x\gt 0} zx\,dm + \int_{x\gt 0} z(-x)\,dm = 0 \quad &\text{(same pairing)} \\
> P_{xy,xz} &= \int_{\mathcal D} zy\,dm \quad &\text{(does not involve $Oyz$: no conclusion)}
> \end{aligned}$$
>
> $$\boxed{Oyz \text{ plane of symmetry} \ \Longrightarrow\ P_{xz,yz} = P_{xy,yz} = 0}$$
>
> **Units:** $[\mathrm{M\,L^2}]$
> **Meaning:** whenever one of the two planes of a product is a plane of symmetry of the body the product vanishes; look for symmetries before integrating.

## 14. Worked examples of the notes and of Lecture 8

The four bodies of Fig. 10.2 are the examples of Notes.pdf, Sec. 10.5, drawn on [Lecture 8, Slides 18-21] for the classroom solution. The moments of the half disk and the moments and products of the half sphere are left as exercises in the notes; they are worked here.

### Half-circumference wire

![[attachments/EM-T/t6-wire.svg]]

> [!example] Half-circumference wire (Notes.pdf, Sec. 10.5; [Lecture 8, Slide 18])
> A wire of radius $R$ and uniform linear density $\lambda$ lies in the plane $Oxy$ along the upper half circle centred at $O$, parametrised by the angle $\theta$ from $Ox$ between $0$ and $\pi$. Find its mass, centre of mass, moments and products of inertia in $S_0$.

> [!derivation] Parametrisation and mass element of the wire
> **Law:** arc length of a parametrised curve
> **Source:** Notes.pdf, Eq. 10.16; Notes.pdf, Eq. 10.17
>
> In the right triangle with hypotenuse $R$ (the radius to the element), the leg along $Ox$ is adjacent to $\theta$ and the leg along $Oy$ is opposite.
>
> $$\begin{aligned}
> x &= R\cos\theta,\qquad y = R\sin\theta,\qquad \theta\in[0,\pi] \quad &\text{(Eq. 10.16)} \\
> d\ell &= \sqrt{\left(\tfrac{dx}{d\theta}\right)^2 + \left(\tfrac{dy}{d\theta}\right)^2}\,d\theta = \sqrt{R^2\sin^2\theta + R^2\cos^2\theta}\,d\theta = R\,d\theta \quad &\text{(arc length; $\tfrac{dx}{d\theta} = -R\sin\theta$, $\tfrac{dy}{d\theta} = R\cos\theta$)}
> \end{aligned}$$
>
> $$\boxed{dm = \lambda\,d\ell = \lambda R\,d\theta}$$
>
> **Units:** $[\mathrm{M\,L^{-1}}][\mathrm L] = [\mathrm M]$
> **Meaning:** the mass element is the density times an arc of radius $R$ and opening $d\theta$.

> [!derivation] Mass and centre of mass of the wire
> **Law:** zeroth and first moments; Barrow's rule
> **Source:** Notes.pdf, Eq. 10.18; Notes.pdf, Eq. 10.19
>
> $$\begin{aligned}
> m &= \int_0^\pi \lambda R\,d\theta = \lambda R\,[\theta]_0^\pi = \lambda R(\pi - 0) \quad &\text{(Eq. 10.6; Barrow)} \\
> \int_{\mathcal D}(x\,\mathbf i + y\,\mathbf j)\,dm &= \int_0^\pi\left(\lambda R^2\cos\theta\,\mathbf i + \lambda R^2\sin\theta\,\mathbf j\right)d\theta \quad &\text{(substitute $x$, $y$ and $dm$)} \\
> &= \lambda R^2[\sin\theta]_0^\pi\,\mathbf i + \lambda R^2[-\cos\theta]_0^\pi\,\mathbf j \quad &\text{(antiderivatives)} \\
> &= \lambda R^2(0-0)\,\mathbf i + \lambda R^2(1+1)\,\mathbf j = 2\lambda R^2\,\mathbf j \quad &\text{(Barrow: $-\cos\pi + \cos 0 = 2$)} \\
> \mathbf r_0^G &= \frac{2\lambda R^2}{\pi\lambda R}\,\mathbf j \quad &\text{(Eq. 10.8)}
> \end{aligned}$$
>
> $$\boxed{m = \pi\lambda R,\qquad \mathbf r_0^G = \frac{2}{\pi}R\,\mathbf j}$$
>
> **Units:** $[\mathrm{M\,L^{-1}}][\mathrm L] = [\mathrm M]$; $[\mathrm L]$
> **Meaning:** $G$ lies on the symmetry axis $Oy$, as symmetry theorem 1 predicts, at about $0.64R$: off the wire itself.

> [!derivation] Moments of inertia of the wire
> **Law:** definitions of Eq. 10.11; half-angle identity; flat body relation
> **Source:** Notes.pdf, Eq. 10.20; Notes.pdf, Eq. 10.21; Notes.pdf, Eq. 10.22
>
> $$\begin{aligned}
> I_z &= \int_0^\pi R^2(\cos^2\theta + \sin^2\theta)\,\lambda R\,d\theta = \lambda R^3[\theta]_0^\pi = \pi\lambda R^3 = mR^2 \quad &\text{($x^2+y^2 = R^2$; Barrow; Eq. 10.18)} \\
> I_x &= \int_0^\pi R^2\sin^2\theta\,\lambda R\,d\theta = \lambda R^3\int_0^\pi\frac{1-\cos 2\theta}{2}\,d\theta \quad &\text{($I_x = \int y^2\,dm$ for $z = 0$; half-angle identity)} \\
> &= \lambda R^3\left[\frac{\theta}{2} - \frac{\sin 2\theta}{4}\right]_0^\pi = \lambda R^3\,\frac{\pi}{2} = \frac12 mR^2 \quad &\text{(antiderivative; Barrow, $\sin 2\pi = \sin 0 = 0$)} \\
> I_y &= I_z - I_x = mR^2 - \tfrac12 mR^2 \quad &\text{(flat body: $I_O = I_z = I_x + I_y$)}
> \end{aligned}$$
>
> $$\boxed{I_z = mR^2 \equiv I_O,\qquad I_x = \tfrac12 mR^2,\qquad I_y = \tfrac12 mR^2}$$
>
> **Units:** $[\mathrm M][\mathrm{L^2}]$
> **Meaning:** all the mass is at the distance $R$ from $O$, so the polar moment is $mR^2$; it splits equally between the two in-plane axes for a half circle.

> [!derivation] Products of inertia of the wire
> **Law:** definitions of Eq. 10.15; substitution $u = \sin\theta$
> **Source:** Notes.pdf, Eq. 10.23
>
> $$\begin{aligned}
> P_{xy,xz} &= \int_{\mathcal D} zy\,dm = 0,\qquad P_{xy,yz} = \int_{\mathcal D} zx\,dm = 0 \quad &\text{($z = 0$: the wire lies in $Oxy$)} \\
> P_{xz,yz} &= \int_0^\pi R\sin\theta\,R\cos\theta\,\lambda R\,d\theta = \lambda R^3\int_0^\pi\sin\theta\cos\theta\,d\theta \quad &\text{(substitute; note the factor $R^3$)} \\
> \int_0^\pi\sin\theta\cos\theta\,d\theta &= \int_{0}^{0} u\,du = 0 \quad &\text{($u = \sin\theta$, $du = \cos\theta\,d\theta$; limits $\sin 0 = \sin\pi = 0$)}
> \end{aligned}$$
>
> $$\boxed{P_{xy,xz} = P_{xy,yz} = P_{xz,yz} = 0}$$
>
> **Units:** $[\mathrm{M\,L^2}]$
> **Meaning:** $Oyz$ is a plane of symmetry of the wire (symmetry theorem 2), so the last product vanishes without integrating.

> [!warning] Erratum in the source
> Notes.pdf, Eq. 10.23 prints the factor in front of the integral as $\lambda R^2$. With $x$, $y$ and $dm$ of Eqs. 10.16 and 10.17 the integrand carries three factors $R$, so the factor is $\lambda R^3$, as in the box above. The result, zero, is not affected.

### Homogeneous rectangular plate

![[attachments/EM-T/t6-plate.svg]]

> [!example] Homogeneous plate (Notes.pdf, Sec. 10.5; [Lecture 8, Slide 19])
> A homogeneous plate of mass $M$, length $L$ along $Ox$, width $W$ along $Oy$ and negligible thickness has its centre at $O$. Find its moments and products of inertia in $S_0$, and the product of inertia in a frame $S_1$ with origin at the corner $A$ and axes along the edges. Fig. 10.2(b) does not draw $S_1$; the limits of Eq. 10.27 place $A$ at the corner with the plate in the positive quadrant of $x_1$, $y_1$, and the figure here draws it so.

> [!derivation] Density, mass element and centre of mass of the plate
> **Law:** uniform area density; symmetry theorem 1
> **Source:** Notes.pdf, Sec. 10.5; Notes.pdf, Eq. 10.8
>
> $$\begin{aligned}
> \sigma &= \frac{M}{LW} \quad &\text{(mass over area, homogeneous plate)} \\
> dm &= \sigma\,dA = \frac{M}{LW}\,dx\,dy \quad &\text{(Cartesian area element)} \\
> x_G &= y_G = 0 \quad &\text{($Oxz$ and $Oyz$ are planes of symmetry)}
> \end{aligned}$$
>
> $$\boxed{dm = \frac{M}{LW}\,dx\,dy,\qquad G \equiv O}$$
>
> **Units:** $[\mathrm M]/[\mathrm{L^2}]\cdot[\mathrm{L^2}] = [\mathrm M]$
> **Meaning:** the centre of mass is the geometric centre of the plate.

> [!derivation] Moments of inertia of the plate about its centre
> **Law:** definitions of Eqs. 10.10 and 10.11 as double integrals; Barrow's rule
> **Source:** Notes.pdf, Eq. 10.24; Notes.pdf, Eq. 10.25; Notes.pdf, Eq. 10.26
>
> $$\begin{aligned}
> \int_{-L/2}^{L/2} x^2\,dx &= \left[\frac{x^3}{3}\right]_{-L/2}^{L/2} = \frac{1}{3}\left(\frac{L^3}{8} + \frac{L^3}{8}\right) = \frac{L^3}{12} \quad &\text{(antiderivative and Barrow)} \\
> I_y &= \int_{-W/2}^{W/2}\int_{-L/2}^{L/2}\frac{M}{LW}x^2\,dx\,dy = \frac{M}{LW}\cdot\frac{L^3}{12}\cdot W = \frac{1}{12}ML^2 \quad &\text{($I_y = \int x^2\,dm$ for $z = 0$; the $y$ integral gives $W$)} \\
> I_x &= \int_{-W/2}^{W/2}\int_{-L/2}^{L/2}\frac{M}{LW}y^2\,dx\,dy = \frac{M}{LW}\cdot L\cdot\frac{W^3}{12} = \frac{1}{12}MW^2 \quad &\text{(same steps with $y$)} \\
> I_O = I_z &= \int_{-W/2}^{W/2}\int_{-L/2}^{L/2}\frac{M}{LW}(x^2+y^2)\,dx\,dy = I_y + I_x \quad &\text{(flat plate; linearity)}
> \end{aligned}$$
>
> $$\boxed{I_O = I_z = \tfrac{1}{12}M(L^2+W^2),\qquad I_x = \tfrac{1}{12}MW^2,\qquad I_y = \tfrac{1}{12}ML^2 = I_O - I_x}$$
>
> **Units:** $[\mathrm M][\mathrm{L^2}]$
> **Meaning:** the moment about an in-plane axis grows with the square of the dimension perpendicular to that axis.

> [!derivation] Product of inertia of the plate in the corner frame
> **Law:** definition of Eq. 10.15 in $S_1$; separable double integral
> **Source:** Notes.pdf, Eq. 10.27
>
> $$\begin{aligned}
> P_{x_1y_1,x_1z_1} &= P_{x_1y_1,y_1z_1} = 0 \quad &\text{(they involve the plane $Ax_1y_1$, which contains the whole plate: $z_1 = 0$)} \\
> P_{x_1z_1,y_1z_1} &= \int_0^W\int_0^L\frac{M}{LW}\,x_1 y_1\,dx_1\,dy_1 \quad &\text{(Eq. 10.15 in $S_1$)} \\
> &= \frac{M}{LW}\left[\frac{x_1^2}{2}\right]_0^L\left[\frac{y_1^2}{2}\right]_0^W = \frac{M}{LW}\cdot\frac{L^2}{2}\cdot\frac{W^2}{2} \quad &\text{(separable integrand; Barrow)}
> \end{aligned}$$
>
> $$\boxed{P_{x_1z_1,y_1z_1} = \tfrac14 MLW}$$
>
> **Units:** $[\mathrm M][\mathrm L][\mathrm L]$
> **Meaning:** in $S_0$ every product vanishes by symmetry; seen from the corner the whole plate lies in the quadrant where both signed distances are positive, so this product is positive.

### Homogeneous half disk

![[attachments/EM-T/t6-half-disk.svg]]

> [!example] Half disk (Notes.pdf, Sec. 10.5; [Lecture 8, Slide 20])
> A homogeneous half disk of radius $R$ and area density $\sigma$ occupies the upper half of the disk centred at $O$ in the plane $Oxy$. Find its mass and centre of mass; the moments and products of inertia, left as an exercise in the notes, are worked here as well.

> [!derivation] Parametrisation and mass element of the half disk
> **Law:** polar coordinates in the plane; Jacobian $r$
> **Source:** Notes.pdf, Eq. 10.28; Notes.pdf, Eq. 10.29; Notes.pdf, Eq. 10.5
>
> In the right triangle with hypotenuse $r$, the leg along $Ox$ is adjacent to $\theta$ and the leg along $Oy$ is opposite.
>
> $$\begin{aligned}
> x &= r\cos\theta,\qquad y = r\sin\theta,\qquad r\in[0,R],\ \theta\in[0,\pi] \quad &\text{(Eq. 10.28)} \\
> dA &= r\,dr\,d\theta \quad &\text{(cylindrical element of Eq. 10.5 without the $dz$)}
> \end{aligned}$$
>
> $$\boxed{dm = \sigma\,dA = \sigma\,r\,dr\,d\theta}$$
>
> **Units:** $[\mathrm{M\,L^{-2}}][\mathrm{L^2}] = [\mathrm M]$
> **Meaning:** the area element is a small annular sector, of sides $dr$ and $r\,d\theta$.

> [!derivation] Mass and centre of mass of the half disk
> **Law:** zeroth and first moments; Barrow's rule
> **Source:** Notes.pdf, Eq. 10.30; Notes.pdf, Eq. 10.31
>
> $$\begin{aligned}
> m &= \sigma\int_0^\pi\int_0^R r\,dr\,d\theta = \sigma\left[\frac{r^2}{2}\right]_0^R[\theta]_0^\pi = \sigma\,\frac{R^2}{2}\,\pi \quad &\text{(separable; Barrow)} \\
> x_G &= 0 \quad &\text{($Oyz$ is a plane of symmetry: symmetry theorem 1)} \\
> \int_{\mathcal D} y\,dm &= \sigma\int_0^\pi\int_0^R r^2\sin\theta\,dr\,d\theta = \sigma\left[\frac{r^3}{3}\right]_0^R[-\cos\theta]_0^\pi = \sigma\,\frac{R^3}{3}\cdot 2 \quad &\text{($y\,dm = r\sin\theta\cdot\sigma r\,dr\,d\theta$; Barrow)} \\
> y_G &= \frac{2}{\pi\sigma R^2}\cdot\frac{2\sigma R^3}{3} \quad &\text{(Eq. 10.8)}
> \end{aligned}$$
>
> $$\boxed{m = \sigma\,\frac{\pi R^2}{2},\qquad x_G = 0,\qquad y_G = \frac{4}{3\pi}R}$$
>
> **Units:** $[\mathrm M]$; $[\mathrm L]$
> **Meaning:** $G$ is on the symmetry axis at about $0.42R$, closer to the diameter than the centre of mass of the wire, because the mass now fills the interior.

> [!derivation] Moments and products of inertia of the half disk (exercise of the notes)
> **Law:** definitions of Eqs. 10.11 and 10.15 in polar coordinates; half-angle identities
> **Source:** Notes.pdf, Sec. 10.5; Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.30
>
> $$\begin{aligned}
> I_x &= \sigma\int_0^\pi\int_0^R r^2\sin^2\theta\,r\,dr\,d\theta = \sigma\left[\frac{r^4}{4}\right]_0^R\left[\frac{\theta}{2}-\frac{\sin2\theta}{4}\right]_0^\pi = \sigma\,\frac{R^4}{4}\cdot\frac{\pi}{2} \quad &\text{($I_x = \int y^2\,dm$; Barrow)} \\
> &= \frac{\sigma\pi R^2}{2}\cdot\frac{R^2}{4} = \frac14 mR^2 \quad &\text{(Eq. 10.30)} \\
> I_y &= \sigma\int_0^\pi\int_0^R r^2\cos^2\theta\,r\,dr\,d\theta = \sigma\,\frac{R^4}{4}\left[\frac{\theta}{2}+\frac{\sin2\theta}{4}\right]_0^\pi = \frac14 mR^2 \quad &\text{($\cos^2\theta = \tfrac{1+\cos2\theta}{2}$; Barrow)} \\
> I_z &= I_x + I_y = \frac12 mR^2 \quad &\text{(flat plate relation)} \\
> P_{xz,yz} &= \sigma\int_0^R r^3\,dr\int_0^\pi\sin\theta\cos\theta\,d\theta = \sigma\,\frac{R^4}{4}\cdot 0 \quad &\text{(the angular integral vanishes as for the wire)}
> \end{aligned}$$
>
> $$\boxed{I_x = I_y = \tfrac14 mR^2,\qquad I_z = I_O = \tfrac12 mR^2,\qquad P_{xy,xz} = P_{xy,yz} = P_{xz,yz} = 0}$$
>
> **Units:** $[\mathrm M][\mathrm{L^2}]$
> **Meaning:** per unit mass the half disk has the same moments about $O$ as the full disk, because each half carries half the mass at the same distances; the products vanish because the body is planar and $Oyz$ is a plane of symmetry.

### Homogeneous half sphere

![[attachments/EM-T/t6-half-sphere.svg]]

> [!example] Half sphere (Notes.pdf, Sec. 10.5; [Lecture 8, Slide 21])
> A homogeneous solid half sphere of radius $R$ and density $\rho$ rests on its flat face, the disk of radius $R$ in the plane $Oxy$ centred at $O$, with the dome towards positive $z$. Find its mass and centre of mass; the moments and products of inertia, left as an exercise in the notes, are worked here as well. The notes refer to Fig. 10.2(c), but the half sphere is drawn in Fig. 10.2(d).

> [!derivation] Mass element of the half sphere
> **Law:** spherical volume element; limits of the half sphere
> **Source:** Notes.pdf, Eq. 10.32; Notes.pdf, Eq. 10.5
>
> $$\begin{aligned}
> dm &= \rho\,dV \quad &\text{(volume density)} \\
> dV &= r^2\cos\varphi\,dr\,d\theta\,d\varphi \quad &\text{(Eq. 10.5, latitude $\varphi$)} \\
> r &\in[0,R],\quad \theta\in[0,2\pi],\quad \varphi\in[0,\tfrac{\pi}{2}] \quad &\text{(upper half: non-negative latitude)}
> \end{aligned}$$
>
> $$\boxed{dm = \rho\,r^2\cos\varphi\,dr\,d\theta\,d\varphi}$$
>
> **Units:** $[\mathrm{M\,L^{-3}}][\mathrm{L^3}] = [\mathrm M]$
> **Meaning:** the element is a small spherical cell of edges $dr$, $r\,d\varphi$ and $r\cos\varphi\,d\theta$.

> [!warning] Erratum in the source
> Notes.pdf, Eq. 10.32 prints the mass element without the density, as the volume element alone. The density is needed for the dimensions of a mass, and Eqs. 10.33 and 10.34 put it back in front of the integrals; the box above keeps the complete form.

> [!derivation] Mass and centre of mass of the half sphere
> **Law:** zeroth and first moments; substitution $u = \sin\varphi$
> **Source:** Notes.pdf, Eq. 10.33; Notes.pdf, Eq. 10.34
>
> $$\begin{aligned}
> m &= \rho\int_0^R r^2\,dr\int_0^{\pi/2}\cos\varphi\,d\varphi\int_0^{2\pi}d\theta = \rho\,\frac{R^3}{3}\,[\sin\varphi]_0^{\pi/2}\,2\pi = \rho\,\frac{R^3}{3}\cdot 1\cdot 2\pi \quad &\text{(separable integrand; Barrow)} \\
> x_G &= y_G = 0 \quad &\text{($Oz$ is an axis of symmetry: symmetry theorem 1)} \\
> \int_{\mathcal D} z\,dm &= \rho\int_0^R r^3\,dr\int_0^{\pi/2}\sin\varphi\cos\varphi\,d\varphi\int_0^{2\pi}d\theta \quad &\text{($z = r\sin\varphi$, opposite leg of the meridian triangle)} \\
> \int_0^{\pi/2}\sin\varphi\cos\varphi\,d\varphi &= \int_0^1 u\,du = \left[\frac{u^2}{2}\right]_0^1 = \frac12 \quad &\text{($u = \sin\varphi$, $du = \cos\varphi\,d\varphi$; limits $0$ and $1$)} \\
> z_G &= \frac{1}{m}\,\rho\,\frac{R^4}{4}\cdot\frac12\cdot 2\pi = \frac{3}{2\pi\rho R^3}\cdot\frac{\pi\rho R^4}{4} \quad &\text{(Eq. 10.8)}
> \end{aligned}$$
>
> $$\boxed{m = \tfrac23\rho\pi R^3,\qquad x_G = y_G = 0,\qquad z_G = \tfrac38 R}$$
>
> **Units:** $[\mathrm{M\,L^{-3}}][\mathrm{L^3}] = [\mathrm M]$; $[\mathrm L]$
> **Meaning:** half the mass of the full sphere, with $G$ on the axis at three eighths of the radius above the flat face.

> [!derivation] Moments and products of inertia of the half sphere about O (exercise of the notes)
> **Law:** definitions of Eqs. 10.11, 10.12 and 10.15; substitution $u = \sin\varphi$; symmetry theorem 2
> **Source:** Notes.pdf, Sec. 10.5; Notes.pdf, Eq. 10.12; Notes.pdf, Eq. 10.13
>
> $$\begin{aligned}
> \int_0^{\pi/2}\cos^3\varphi\,d\varphi &= \int_0^{\pi/2}(1-\sin^2\varphi)\cos\varphi\,d\varphi = \int_0^1(1-u^2)\,du = \left[u - \frac{u^3}{3}\right]_0^1 = \frac23 \quad &\text{($u = \sin\varphi$, $du = \cos\varphi\,d\varphi$; Barrow)} \\
> I_z &= \rho\int_0^R r^4\,dr\int_0^{\pi/2}\cos^3\varphi\,d\varphi\int_0^{2\pi}d\theta = \rho\,\frac{R^5}{5}\cdot\frac23\cdot2\pi = \frac{4}{15}\pi\rho R^5 = \frac25 mR^2 \quad &\text{($x^2+y^2 = r^2\cos^2\varphi$, adjacent leg squared)} \\
> I_{xy} &= \rho\int_0^R r^4\,dr\int_0^{\pi/2}\sin^2\varphi\cos\varphi\,d\varphi\int_0^{2\pi}d\theta = \rho\,\frac{R^5}{5}\left[\frac{u^3}{3}\right]_0^1 2\pi = \frac15 mR^2 \quad &\text{($z^2 = r^2\sin^2\varphi$; same substitution)} \\
> I_{xz} &= I_{yz} = \tfrac12\,(I_{xz}+I_{yz}) = \tfrac12\int_{\mathcal D}(x^2+y^2)\,dm = \tfrac12 I_z = \tfrac15 mR^2 \quad &\text{(the axis $Oz$ is an axis of revolution: $\int y^2\,dm = \int x^2\,dm$)} \\
> I_x &= \int_{\mathcal D}(y^2+z^2)\,dm = I_{xz} + I_{xy} = \tfrac25 mR^2,\qquad I_y = I_{yz} + I_{xy} = \tfrac25 mR^2 \quad &\text{(Eqs. 10.11 and 10.12)} \\
> P_{xz,yz} &= \rho\int_0^R r^4\,dr\int_0^{\pi/2}\cos^3\varphi\,d\varphi\int_0^{2\pi}\cos\theta\sin\theta\,d\theta = 0 \quad &\text{($\int_0^{2\pi}\cos\theta\sin\theta\,d\theta = [\tfrac12\sin^2\theta]_0^{2\pi} = 0$)} \\
> P_{xy,yz} &= P_{xy,xz} = 0 \quad &\text{($Oyz$ and $Oxz$ are planes of symmetry: symmetry theorem 2)}
> \end{aligned}$$
>
> $$\boxed{I_x = I_y = I_z = \tfrac25 mR^2,\qquad I_O = \tfrac35 mR^2,\qquad P_{xy,xz} = P_{xy,yz} = P_{xz,yz} = 0}$$
>
> **Units:** $[\mathrm{M\,L^{-3}}][\mathrm{L^5}] = [\mathrm M][\mathrm{L^2}]$
> **Meaning:** check with Eq. 10.13: the three axis moments add to $\tfrac65 mR^2 = 2I_O$, and directly $I_O = \rho\,\tfrac{R^5}{5}\cdot 1\cdot 2\pi = \tfrac35 mR^2$; about $O$ the half sphere has the moments of the full sphere per unit mass.

## 15. The tensor of inertia

The moments and products of inertia appear in the dynamics as the components of one second-order tensor, the tensor of inertia about a point (Notes.pdf, Sec. 10.6; [Lecture 8, Slide 12]).

> [!derivation] Components of the tensor of inertia
> **Law:** definition of the tensor; components of the unit tensor and of the dyad
> **Source:** Notes.pdf, Eq. 10.35; Notes.pdf, Eq. 10.36; Notes.pdf, Eq. 10.37; Notes.pdf, Eq. 10.38; [Lecture 8, Slide 12]
>
> $$\begin{aligned}
> \boldsymbol{\mathcal I}_O &= \int_{\mathcal D}\Big[(r_0^P)^2\,\boldsymbol{\mathcal U} - \mathbf r_0^P\otimes\mathbf r_0^P\Big]\,dm \quad &\text{(definition, Eq. 10.35)} \\
> \big[(r_0^P)^2\boldsymbol{\mathcal U}\big]_{00} &= (x^2+y^2+z^2)\begin{bmatrix} 1&0&0 \cr 0&1&0 \cr 0&0&1\end{bmatrix} \quad &\text{(Eq. 10.36, with $\mathbf r_0^P = x\,\mathbf i + y\,\mathbf j + z\,\mathbf k$)} \\
> \big[\mathbf r_0^P\otimes\mathbf r_0^P\big]_{00} &= \begin{bmatrix} x^2&xy&xz \cr xy&y^2&yz \cr xz&yz&z^2\end{bmatrix} \quad &\text{(Eq. 10.37, Eq. 1.48 with $\mathbf u = \mathbf v = \mathbf r_0^P$)} \\
> [\boldsymbol{\mathcal I}_O]_{00} &= \int_{\mathcal D}\begin{bmatrix} y^2+z^2&-xy&-xz \cr -xy&x^2+z^2&-yz \cr -xz&-yz&x^2+y^2\end{bmatrix}dm \quad &\text{(subtract entry by entry)} \\
> &= \begin{bmatrix} I_x & -P_{xz,yz} & -P_{xy,yz} \cr -P_{xz,yz} & I_y & -P_{xy,xz} \cr -P_{xy,yz} & -P_{xy,xz} & I_z \end{bmatrix} \quad &\text{(integrate each entry: Eqs. 10.11 and 10.15)}
> \end{aligned}$$
>
> $$\boxed{[\boldsymbol{\mathcal I}_O]_{00} = \begin{bmatrix} I_x & -P_{xz,yz} & -P_{xy,yz} \\ -P_{xz,yz} & I_y & -P_{xy,xz} \\ -P_{xy,yz} & -P_{xy,xz} & I_z \end{bmatrix}_{00}}$$
>
> **Units:** $[\mathrm{M\,L^2}]$ in every entry
> **Meaning:** the diagonal holds the moments about the coordinate axes and the off-diagonal entries minus the products of inertia; the matrix is symmetric, and the second term of the integrand is the second moment of the mass distribution.

![[attachments/EM-T/t6-distance-to-line.svg]]

> [!derivation] Moment of inertia about any line through O
> **Law:** double contraction of the tensor; Pythagoras in the triangle of $\mathbf r_0^P$ and the line
> **Source:** Notes.pdf, Eq. 10.39; Notes.pdf, Eq. 1.36; [Lecture 8, Slide 13]
>
> In the right triangle formed by $O$, the element $P$ and the foot of the perpendicular from $P$ to the line $\ell$, the hypotenuse is $r_0^P$, the leg along $\ell$ is $\mathbf r_0^P\cdot\mathbf u$ (adjacent to the angle between $\mathbf r_0^P$ and $\mathbf u$) and the opposite leg is the distance $d$.
>
> $$\begin{aligned}
> \mathbf u\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf u &= \int_{\mathcal D}\Big[(r_0^P)^2\,\mathbf u\cdot\boldsymbol{\mathcal U}\cdot\mathbf u - \mathbf u\cdot(\mathbf r_0^P\otimes\mathbf r_0^P)\cdot\mathbf u\Big]dm \quad &\text{(contract Eq. 10.35 on both sides; linearity)} \\
> &= \int_{\mathcal D}\Big[(r_0^P)^2\,(\mathbf u\cdot\mathbf u) - (\mathbf u\cdot\mathbf r_0^P)(\mathbf r_0^P\cdot\mathbf u)\Big]dm \quad &\text{(Eq. 1.36)} \\
> &= \int_{\mathcal D}\Big[(r_0^P)^2 - (\mathbf r_0^P\cdot\mathbf u)^2\Big]dm \quad &\text{($\mathbf u$ is a unit vector)} \\
> d^2 &= (r_0^P)^2 - (\mathbf r_0^P\cdot\mathbf u)^2 \quad &\text{(Pythagoras: hypotenuse squared minus adjacent leg squared)}
> \end{aligned}$$
>
> $$\boxed{I_\ell = \mathbf u\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf u = \int_{\mathcal D} d^2\,dm}$$
>
> **Units:** $[\mathrm{M\,L^2}]$
> **Meaning:** the tensor stores the moments about every line through $O$, not only the coordinate axes; with $\mathbf u = \mathbf i$ it returns the entry $I_x$.

> [!derivation] Product of inertia of any two perpendicular planes through O
> **Law:** double contraction with two orthogonal unit normals
> **Source:** Notes.pdf, Eq. 10.40; Notes.pdf, Eq. 1.36
>
> $$\begin{aligned}
> \mathbf u_1\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf u_2 &= \int_{\mathcal D}\Big[(r_0^P)^2\,(\mathbf u_1\cdot\mathbf u_2) - (\mathbf u_1\cdot\mathbf r_0^P)(\mathbf r_0^P\cdot\mathbf u_2)\Big]dm \quad &\text{(Eq. 1.36)} \\
> \mathbf u_1\cdot\mathbf u_2 &= 0 \quad &\text{(perpendicular planes have orthogonal normals)} \\
> d_1 &= \mathbf r_0^P\cdot\mathbf u_1,\qquad d_2 = \mathbf r_0^P\cdot\mathbf u_2 \quad &\text{(signed distances to the planes through $O$ of normals $\mathbf u_1$, $\mathbf u_2$)} \\
> \mathbf u_1\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf u_2 &= -\int_{\mathcal D} d_1 d_2\,dm = -P_{\pi_1,\pi_2} \quad &\text{(Eq. 10.14)}
> \end{aligned}$$
>
> $$\boxed{P_{\pi_1,\pi_2} = -\mathbf u_1\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf u_2}$$
>
> **Units:** $[\mathrm{M\,L^2}]$
> **Meaning:** reversing one normal reverses one signed distance and therefore the sign of the product (footnote 17 of the notes).

> [!derivation] The tensor of inertia is symmetric and positive definite
> **Law:** symmetry of the dyad of a vector with itself; squared distances
> **Source:** [Lecture 8, Slide 12]; Notes.pdf, Eq. 10.39
>
> $$\begin{aligned}
> \big[\mathbf r_0^P\otimes\mathbf r_0^P\big]^T_{00} &= \big([\mathbf r_0^P]_0[\mathbf r_0^P]_0^T\big)^T = [\mathbf r_0^P]_0[\mathbf r_0^P]_0^T \quad &\text{(transpose of a product reverses the order)} \\
> \mathbf u\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf u &= u^2\int_{\mathcal D} d_{\mathbf u}^2\,dm \ \geq\ 0 \quad &\text{(Eq. 10.39 for the unit vector $\mathbf u/u$, multiplied by $u^2$)} \\
> \int_{\mathcal D} d_{\mathbf u}^2\,dm &= 0 \iff d_{\mathbf u} = 0 \text{ for every } dm \quad &\text{(an integral of a non-negative function vanishes only if the function does)}
> \end{aligned}$$
>
> $$\boxed{[\boldsymbol{\mathcal I}_O]_{00}^T = [\boldsymbol{\mathcal I}_O]_{00},\qquad \mathbf u\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf u \gt 0\ \ \forall\,\mathbf u \neq \mathbf 0}$$
>
> **Units:** $[\mathrm{M\,L^2}]$ times the square of the units of $\mathbf u$
> **Meaning:** a body has a strictly positive moment about every axis; the only limit case is an ideal bar of zero thickness about its own line, where all the mass lies on the axis and the moment is zero.

## 16. Change of basis of the tensor of inertia

To contract the tensor with a vector both must be written in consistent bases: a tensor in $\mathcal B_0\otimes\mathcal B_0$ with vectors in $\mathcal B_0$ (Notes.pdf, Sec. 10.7). A tensor stays the same physical entity when the basis changes, like a vector; only its component matrix changes.

> [!derivation] Inertia tensor in a rotated basis
> **Law:** change of basis of a second-order tensor; components as double contractions
> **Source:** Notes.pdf, Eq. 10.41; [Lecture 8, Slide 5]; [Lecture 8, Slide 13]
>
> $$\begin{aligned}
> \big([\boldsymbol{\mathcal I}_O]_{11}\big)_{mn} &= \mathbf u_m\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf u_n \quad &\text{(component $mn$ in $\mathcal B_1 = \{\mathbf u_1,\mathbf u_2,\mathbf u_3\}$)} \\
> &= [\mathbf u_m]_0^T\,[\boldsymbol{\mathcal I}_O]_{00}\,[\mathbf u_n]_0 \quad &\text{(contraction in $\mathcal B_0$ components)} \\
> [\mathbf u_n]_0 &= \text{column } n \text{ of } [{}_0R_1] \quad &\text{(Eq. 1.13)}
> \end{aligned}$$
>
> $$\boxed{[\boldsymbol{\mathcal I}_O]_{11} = [{}_0R_1]^T\cdot[\boldsymbol{\mathcal I}_O]_{00}\cdot[{}_0R_1]}$$
>
> **Units:** $[\mathrm{M\,L^2}]$ (the rotation matrices are dimensionless)
> **Meaning:** the same rule as for any second-order tensor (Section 10); it gives the moments and products of inertia about any rotated set of axes through $O$.

## 17. Principal axes of inertia

There is always a rotated basis $\mathcal B_1$, of vectors $\mathbf e_1$, $\mathbf e_2$, $\mathbf e_3$, in which the tensor of inertia is diagonal. Its vectors are the principal axes or directions of inertia and the diagonal entries the principal moments of inertia; finding them means diagonalising the tensor (Notes.pdf, Sec. 10.7.1; [Lecture 8, Slide 13]). The notes invoke the spectral theorem; the boxes below prove the two facts it rests on for a real symmetric matrix.

> [!derivation] Eigenvalue problem of the tensor of inertia
> **Law:** principal direction: the tensor maps it onto a multiple of itself
> **Source:** Notes.pdf, Eq. 10.43; [Lecture 8, Slide 13]
>
> $$\begin{aligned}
> \boldsymbol{\mathcal I}_O\cdot\mathbf e_i &= I_i\,\mathbf e_i \quad &\text{(definition of principal direction and principal moment)} \\
> \big([\boldsymbol{\mathcal I}_O]_{00} - I_i[U]\big)[\mathbf e_i]_0 &= [\mathbf 0] \quad &\text{(in $\mathcal B_0$ components)} \\
> \det\big([\boldsymbol{\mathcal I}_O]_{00} - I\,[U]\big) &= 0 \quad &\text{(non-zero solution: singular matrix; a cubic equation for $I$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol{\mathcal I}_O\cdot\mathbf e_i = I_i\,\mathbf e_i,\qquad \det\big([\boldsymbol{\mathcal I}_O]_{00} - I\,[U]\big) = 0}$$
>
> **Units:** $[\mathrm{M\,L^2}]$ for the principal moments; the directions are unit vectors
> **Meaning:** the three roots of the cubic are the principal moments; each one gives its principal direction by solving the linear system.

> [!derivation] Principal moments are real and positive, principal directions orthogonal
> **Law:** symmetry of the tensor; positive definiteness
> **Source:** Notes.pdf, Sec. 10.7.1; [Lecture 8, Slide 6]; [Lecture 8, Slide 12]
>
> Write $[\boldsymbol{\mathcal I}]$ for the real symmetric matrix and a bar for the complex conjugate.
>
> $$\begin{aligned}
> \bar{\mathbf e}^T[\boldsymbol{\mathcal I}]\,\mathbf e &= I\,\bar{\mathbf e}^T\mathbf e \quad &\text{(left-multiply the eigen equation by $\bar{\mathbf e}^T$)} \\
> \overline{\bar{\mathbf e}^T[\boldsymbol{\mathcal I}]\,\mathbf e} &= \mathbf e^T[\boldsymbol{\mathcal I}]\,\bar{\mathbf e} = \bar{\mathbf e}^T[\boldsymbol{\mathcal I}]^T\mathbf e = \bar{\mathbf e}^T[\boldsymbol{\mathcal I}]\,\mathbf e \quad &\text{(real entries; a scalar equals its transpose; symmetry)} \\
> \bar I &= I \quad &\text{($\bar{\mathbf e}^T\mathbf e = \lvert\mathbf e\rvert^2 \gt 0$ is real: the principal moments are real)} \\
> I_i &= \mathbf e_i\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf e_i \gt 0 \quad &\text{(unit eigenvector; positive definiteness)} \\
> \mathbf e_m\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf e_n &= I_n\,\mathbf e_m\cdot\mathbf e_n = I_m\,\mathbf e_m\cdot\mathbf e_n \quad &\text{(contract on the right first, or on the left first using symmetry)} \\
> (I_m - I_n)\,\mathbf e_m\cdot\mathbf e_n &= 0 \quad &\text{(subtract)}
> \end{aligned}$$
>
> $$\boxed{I_i \in \mathbb R,\quad I_i \gt 0,\qquad I_m \neq I_n \Rightarrow \mathbf e_m\cdot\mathbf e_n = 0}$$
>
> **Units:** $[\mathrm{M\,L^2}]$
> **Meaning:** principal directions of different principal moments are orthogonal; for a repeated moment every direction of its eigenplane is principal, and two orthogonal ones are chosen, so an orthonormal principal basis always exists.

> [!derivation] Diagonal form in the principal basis
> **Law:** change of basis of the tensor to $\mathcal B_1 = \{\mathbf e_1,\mathbf e_2,\mathbf e_3\}$
> **Source:** Notes.pdf, Eq. 10.42; Notes.pdf, Eq. 10.41
>
> $$\begin{aligned}
> [{}_0R_1] &= \big[\,[\mathbf e_1]_0\ \big|\ [\mathbf e_2]_0\ \big|\ [\mathbf e_3]_0\,\big],\qquad \mathbf e_3 = \mathbf e_1\times\mathbf e_2 \quad &\text{(orthonormal; the sign of $\mathbf e_3$ is chosen so that the determinant is one)} \\
> \big([\boldsymbol{\mathcal I}_O]_{11}\big)_{mn} &= \mathbf e_m\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf e_n = I_n\,\mathbf e_m\cdot\mathbf e_n = I_n\,\delta_{mn} \quad &\text{(Eq. 10.41 entry by entry; Eq. 10.43; orthonormality)}
> \end{aligned}$$
>
> $$\boxed{[\boldsymbol{\mathcal I}_O]_{11} = \begin{bmatrix} I_1 & 0 & 0 \\ 0 & I_2 & 0 \\ 0 & 0 & I_3 \end{bmatrix}_{11}}$$
>
> **Units:** $[\mathrm{M\,L^2}]$
> **Meaning:** in the principal basis all products of inertia vanish; any orthonormal basis in which the tensor is diagonal is a principal basis.

Symmetries of the body often give the principal basis without solving the cubic ([Lecture 8, Slide 13]).

> [!derivation] Symmetry theorem 3: two planes of symmetry make the tensor diagonal
> **Law:** symmetry theorem 2 applied to each product
> **Source:** [Lecture 8, Slide 13]; [Lecture 8, Slide 11]; Notes.pdf, Eq. 10.38
>
> Planes of symmetry $Oxz$ and $Oyz$ (two coordinate planes).
>
> $$\begin{aligned}
> P_{xz,yz} &= 0 \quad &\text{(involves $Oxz$ and $Oyz$, both of symmetry)} \\
> P_{xy,yz} &= 0 \quad &\text{(involves $Oyz$, a plane of symmetry)} \\
> P_{xy,xz} &= 0 \quad &\text{(involves $Oxz$, a plane of symmetry)}
> \end{aligned}$$
>
> $$\boxed{[\boldsymbol{\mathcal I}_O]_{00} = \begin{bmatrix} I_x & 0 & 0 \\ 0 & I_y & 0 \\ 0 & 0 & I_z \end{bmatrix}_{00}\ \text{ and } \mathcal B_0 \text{ is principal}}$$
>
> **Units:** $[\mathrm{M\,L^2}]$
> **Meaning:** every product involves at least one of any two coordinate planes, so two planes of symmetry cancel all three; the plate, the half disk and the half sphere of Section 14 have diagonal tensors in $S_0$ for this reason.

## 18. Change of reference point: Steiner's theorem

Consider the frame $S_0$ with origin $O$ and a parallel frame $S_G$ with origin at the centre of mass $G$ and the same basis $\mathcal B_0$ (Fig. 10.3). Steiner's theorem relates the tensors about $O$ and about $G$ (Notes.pdf, Sec. 10.8; [Lecture 8, Slides 14-15]).

![[attachments/EM-T/t6-steiner.svg]]

> [!derivation] The first moment about the centre of mass vanishes
> **Law:** decomposition of the position vector; definition of the centre of mass
> **Source:** Notes.pdf, Eq. 10.44; Notes.pdf, Eq. 10.45; Notes.pdf, Eq. 10.46; [Lecture 8, Slide 14]
>
> $$\begin{aligned}
> \mathbf r_0^P &= \mathbf r_0^G + \mathbf r_G^P \quad &\text{($\mathbf{OP} = \mathbf{OG} + \mathbf{GP}$)} \\
> \int_{\mathcal D}\mathbf r_G^P\,dm &= \int_{\mathcal D}\mathbf r_0^P\,dm - \mathbf r_0^G\int_{\mathcal D}dm = m\,\mathbf r_0^G - m\,\mathbf r_0^G = \mathbf 0 \quad &\text{(Eqs. 10.6 and 10.7; $\mathbf r_0^G$ is constant over $\mathcal D$)} \\
> \int_{\mathcal D}(\mathbf r_0^G\cdot\mathbf r_G^P)\,\boldsymbol{\mathcal U}\,dm &= \Big(\mathbf r_0^G\cdot\int_{\mathcal D}\mathbf r_G^P\,dm\Big)\boldsymbol{\mathcal U} = \mathbf 0 \quad &\text{(constant factors out; Eq. 10.44)} \\
> \int_{\mathcal D}\mathbf r_G^P\otimes\mathbf r_0^G\,dm &= \Big(\int_{\mathcal D}\mathbf r_G^P\,dm\Big)\otimes\mathbf r_0^G = \mathbf 0,\quad \int_{\mathcal D}\mathbf r_0^G\otimes\mathbf r_G^P\,dm = \mathbf 0 \quad &\text{(bilinearity, Eqs. 1.34-1.35)}
> \end{aligned}$$
>
> $$\boxed{\int_{\mathcal D}\mathbf r_G^P\,dm = \mathbf 0}$$
>
> **Units:** $[\mathrm{M\,L}]$
> **Meaning:** about its own centre of mass a body has zero first moment, so every term linear in the position relative to $G$ integrates to zero.

> [!derivation] Steiner's theorem in tensor (matrix) form
> **Law:** expansion of the definition of the tensor about $O$ with the position relative to $G$
> **Source:** Notes.pdf, Eq. 10.47; Notes.pdf, Eq. 10.48; [Lecture 8, Slide 14]; [Lecture 8, Slide 15]
>
> $$\begin{aligned}
> (r_0^P)^2 &= (\mathbf r_0^G+\mathbf r_G^P)\cdot(\mathbf r_0^G+\mathbf r_G^P) = (r_0^G)^2 + (r_G^P)^2 + 2\,\mathbf r_0^G\cdot\mathbf r_G^P \quad &\text{(distributive dot product)} \\
> \mathbf r_0^P\otimes\mathbf r_0^P &= \mathbf r_0^G\otimes\mathbf r_0^G + \mathbf r_G^P\otimes\mathbf r_G^P + \mathbf r_0^G\otimes\mathbf r_G^P + \mathbf r_G^P\otimes\mathbf r_0^G \quad &\text{(bilinearity, Eqs. 1.34-1.35)} \\
> \boldsymbol{\mathcal I}_O &= \int_{\mathcal D}\Big[(r_0^G)^2\boldsymbol{\mathcal U} - \mathbf r_0^G\otimes\mathbf r_0^G\Big]dm + \int_{\mathcal D}\Big[(r_G^P)^2\boldsymbol{\mathcal U} - \mathbf r_G^P\otimes\mathbf r_G^P\Big]dm + \int_{\mathcal D}\Big[2(\mathbf r_0^G\cdot\mathbf r_G^P)\boldsymbol{\mathcal U} - \mathbf r_0^G\otimes\mathbf r_G^P - \mathbf r_G^P\otimes\mathbf r_0^G\Big]dm \quad &\text{(substitute in Eq. 10.35 and group)} \\
> &= m\Big[(r_0^G)^2\boldsymbol{\mathcal U} - \mathbf r_0^G\otimes\mathbf r_0^G\Big] + \boldsymbol{\mathcal I}_G + \mathbf 0 \quad &\text{(constant integrand; Eq. 10.47; Eqs. 10.45-10.46)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol{\mathcal I}_O = \boldsymbol{\mathcal I}_G + m\Big[(r_0^G)^2\,\boldsymbol{\mathcal U} - \mathbf r_0^G\otimes\mathbf r_0^G\Big]}$$
>
> **Units:** $[\mathrm{M\,L^2}] = [\mathrm{M\,L^2}] + [\mathrm M][\mathrm{L^2}]$
> **Meaning:** the tensor about $O$ is the tensor about $G$ plus the tensor about $O$ of a point particle of the whole mass placed at $G$; in components all three terms must be written in the same basis, which is why $S_G$ is taken parallel to $S_0$.

> [!derivation] Steiner's theorem between two points that are not the centre of mass
> **Law:** Steiner's theorem applied twice through $G$
> **Source:** Notes.pdf, Sec. 10.8; [Lecture 8, Slide 15]
>
> $$\begin{aligned}
> \boldsymbol{\mathcal I}_A &= \boldsymbol{\mathcal I}_G + m\Big[(r_A^G)^2\boldsymbol{\mathcal U} - \mathbf r_A^G\otimes\mathbf r_A^G\Big] \quad &\text{(Eq. 10.48 from $G$ to $A$)} \\
> \boldsymbol{\mathcal I}_G &= \boldsymbol{\mathcal I}_A - m\Big[(r_A^G)^2\boldsymbol{\mathcal U} - \mathbf r_A^G\otimes\mathbf r_A^G\Big] \quad &\text{(solve for the tensor about $G$)} \\
> \boldsymbol{\mathcal I}_C &= \boldsymbol{\mathcal I}_G + m\Big[(r_C^G)^2\boldsymbol{\mathcal U} - \mathbf r_C^G\otimes\mathbf r_C^G\Big] \quad &\text{(Eq. 10.48 from $G$ to the second point $C$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol{\mathcal I}_C = \boldsymbol{\mathcal I}_A - m\Big[(r_A^G)^2\boldsymbol{\mathcal U} - \mathbf r_A^G\otimes\mathbf r_A^G\Big] + m\Big[(r_C^G)^2\boldsymbol{\mathcal U} - \mathbf r_C^G\otimes\mathbf r_C^G\Big]}$$
>
> **Units:** $[\mathrm{M\,L^2}]$
> **Meaning:** the theorem always passes through $G$; there is no direct shortcut between two arbitrary points (the slide names them $A$ and $B$, here $A$ and $C$ to avoid confusion with the body $B$).

> [!derivation] Check of Eq. 10.27 with Steiner's theorem
> **Law:** off-diagonal entry of Steiner's theorem in components
> **Source:** Notes.pdf, Eq. 10.48; Notes.pdf, Eq. 10.27; Notes.pdf, Eq. 10.38
>
> In $S_1$ (corner $A$, axes along the edges) the centre of the plate is at $x_1 = L/2$, $y_1 = W/2$, $z_1 = 0$.
>
> $$\begin{aligned}
> \big[m\big((r_A^G)^2\boldsymbol{\mathcal U} - \mathbf r_A^G\otimes\mathbf r_A^G\big)\big]_{12} &= M\big(0 - x_G y_G\big) = -M\,\frac{L}{2}\cdot\frac{W}{2} \quad &\text{(entry (1,2): the unit tensor has zero off-diagonal entries)} \\
> -P^A_{x_1z_1,y_1z_1} &= -P^G_{xz,yz} - \tfrac14 MLW \quad &\text{(entry (1,2) of Eq. 10.48, using Eq. 10.38)} \\
> P^G_{xz,yz} &= 0 \quad &\text{(symmetry theorem 2 for the centred plate)}
> \end{aligned}$$
>
> $$\boxed{P^A_{x_1z_1,y_1z_1} = \tfrac14 MLW}$$
>
> **Units:** $[\mathrm M][\mathrm L][\mathrm L]$
> **Meaning:** Steiner's theorem reproduces the direct integral of Eq. 10.27: the product of inertia about the corner is that of a point mass $M$ at the centre.

The most used special case keeps only one diagonal entry of the theorem: the moment about an axis through $O$ parallel to an axis through $G$ (Notes.pdf, Sec. 10.8.1; [Lecture 8, Slide 16]). It is the tool of planar problems, where only the moment about the axis normal to the plane of motion is needed.

![[attachments/EM-T/t6-parallel-axis.svg]]

> [!derivation] Parallel axis theorem
> **Law:** definition of the moment about an axis; decomposition of the coordinates through $G$
> **Source:** Notes.pdf, Sec. 10.8.1; [Lecture 8, Slide 16]
>
> $$\begin{aligned}
> x_0^P &= x_0^G + x_G^P,\qquad y_0^P = y_0^G + y_G^P \quad &\text{(components of $\mathbf r_0^P = \mathbf r_0^G + \mathbf r_G^P$)} \\
> I_{z_0} &= \int_{\mathcal D}\Big[(x_0^P)^2 + (y_0^P)^2\Big]dm \quad &\text{(Eq. 10.11 about $Oz_0$)} \\
> &= \int_{\mathcal D}\Big[(x_G^P)^2 + (x_0^G)^2 + 2x_G^P x_0^G + (y_G^P)^2 + (y_0^G)^2 + 2y_G^P y_0^G\Big]dm \quad &\text{(square of a sum)} \\
> &= \int_{\mathcal D}\Big[(x_G^P)^2+(y_G^P)^2\Big]dm + \Big[(x_0^G)^2+(y_0^G)^2\Big]\int_{\mathcal D}dm + 2x_0^G\int_{\mathcal D}x_G^P\,dm + 2y_0^G\int_{\mathcal D}y_G^P\,dm \quad &\text{(linearity; constants out of the integrals)} \\
> &= I_{z_G} + m\Big[(x_0^G)^2+(y_0^G)^2\Big] + 0 + 0 \quad &\text{(Eq. 10.11 about $Gz_G$; Eq. 10.44 componentwise)}
> \end{aligned}$$
>
> $$\boxed{I_{z_0} = I_{z_G} + m\Big[(x_0^G)^2 + (y_0^G)^2\Big]}$$
>
> **Units:** $[\mathrm{M\,L^2}] = [\mathrm{M\,L^2}] + [\mathrm M][\mathrm{L^2}]$
> **Meaning:** the moment about an axis is the moment about the parallel axis through $G$ plus the mass times the squared distance between the axes; the added term is never negative, so among parallel axes the one through $G$ has the smallest moment, wherever $O$ is.

> [!info] Extension: Steiner's theorem applied to the half disk and the half sphere
> The notes and slides do not move the tensors of their examples to $G$. The box below applies Eq. 10.48 to the results of Section 14 as an illustration of the matrix form; it is an extension, not a course example.

> [!derivation] Central tensors of the half disk and the half sphere
> **Law:** Steiner's theorem in components with $G$ on the symmetry axis
> **Source:** Notes.pdf, Eq. 10.48; Notes.pdf, Eq. 10.31; Notes.pdf, Eq. 10.34 (extension)
>
> $$\begin{aligned}
> (r_0^G)^2[U] - [\mathbf r_0^G\otimes\mathbf r_0^G]_{00} &= y_G^2\,\mathrm{diag}(1,1,1) - \mathrm{diag}(0,y_G^2,0) = \mathrm{diag}(y_G^2,\,0,\,y_G^2) \quad &\text{(half disk: $\mathbf r_0^G = y_G\,\mathbf j$; Eq. 1.48)} \\
> [\boldsymbol{\mathcal I}_G]_{00} &= \mathrm{diag}\big(\tfrac14 mR^2,\ \tfrac14 mR^2,\ \tfrac12 mR^2\big) - m\,\mathrm{diag}\big(\tfrac{16R^2}{9\pi^2},\,0,\,\tfrac{16R^2}{9\pi^2}\big) \quad &\text{(Eq. 10.48 solved for the central tensor; $y_G^2 = \tfrac{16R^2}{9\pi^2}$)} \\
> (r_0^G)^2[U] - [\mathbf r_0^G\otimes\mathbf r_0^G]_{00} &= \mathrm{diag}(z_G^2,\,z_G^2,\,0) \quad &\text{(half sphere: $\mathbf r_0^G = z_G\,\mathbf k$)} \\
> [\boldsymbol{\mathcal I}_G]_{00} &= \tfrac25 mR^2\,\mathrm{diag}(1,1,1) - m\,\tfrac{9R^2}{64}\,\mathrm{diag}(1,1,0) \quad &\text{(Eq. 10.48; $z_G^2 = \tfrac{9R^2}{64}$; $\tfrac25 - \tfrac{9}{64} = \tfrac{128-45}{320}$)}
> \end{aligned}$$
>
> $$\boxed{\text{half disk: } I_{x_G} = \Big(\tfrac14 - \tfrac{16}{9\pi^2}\Big)mR^2,\ I_{y_G} = \tfrac14 mR^2,\ I_{z_G} = \Big(\tfrac12 - \tfrac{16}{9\pi^2}\Big)mR^2;\qquad \text{half sphere: } I_{x_G} = I_{y_G} = \tfrac{83}{320}mR^2,\ I_{z_G} = \tfrac25 mR^2}$$
>
> **Units:** $[\mathrm M][\mathrm{L^2}]$
> **Meaning:** only the moments about axes that do not pass through $G$ change, and they decrease: about $0.070mR^2$ and $0.320mR^2$ for the half disk, $0.259mR^2$ for the half sphere; the axis of symmetry keeps its moment.

## 19. Practical formulary

| Result | Formula | Source |
| :--- | :--- | :--- |
| Velocity field | $\mathbf v_0^A = \mathbf v_0^P + \boldsymbol\omega_{B0}\times\mathbf{PA}$ | Eq. 9.3 |
| Acceleration field | $\mathbf a_0^A = \mathbf a_0^P + \boldsymbol\alpha_{B0}\times\mathbf{PA} + \boldsymbol\omega_{B0}\times(\boldsymbol\omega_{B0}\times\mathbf{PA})$ | Eq. 9.4 |
| Slip speed (same for all points) | $\mathbf v_0^A\cdot\mathbf e_\omega = \mathbf v_0^P\cdot\mathbf e_\omega = v_{0\parallel}$ | Eq. 9.5 |
| Decomposition of the velocity | $\mathbf v_0^A = \mathbf v_{0\parallel} + \mathbf v_{0\perp}^A$ | Eq. 9.6 |
| Equal projections | $\mathbf v_0^A\cdot\mathbf{PA} = \mathbf v_0^P\cdot\mathbf{PA}$ | Eq. 9.7 |
| Point of the instantaneous axis (and slip) | $\mathbf{AI} = \boldsymbol\omega_{B0}\times\mathbf v_0^A/\omega_{B0}^2$, $\mathbf v_0^I = \mathbf v_{0\parallel}$ | Eqs. 9.10, 9.11 |
| Screw field | $\mathbf v_0^A = \mathbf v_{0\parallel} + \boldsymbol\omega_{B0}\times\mathbf{IA}$, $\lvert\mathbf v_{0\perp}^A\rvert = \omega_{B0}\,d_A$ | Sec. 9.1.3 |
| Body point on a geometric point | $\mathbf r_0^A = \mathbf r_0^{A(B)}$, $\mathbf v_0^A - \mathbf v_0^{A(B)} = \mathbf v_B^A$ | Eqs. 9.14, 9.15 |
| Rotation matrix | $[{}_1R_0] = [{}_0R_1]^T$, $\det[{}_0R_1] = 1$, $[{}_0R_2] = [{}_0R_1][{}_1R_2]$ | Eqs. 1.14-1.16 |
| 3-1-3 Euler angles | $[{}_0R_B] = [{}_0R_1(z,\psi)][{}_1R_2(x,\theta)][{}_2R_B(z,\varphi)]$ | Eqs. 9.16-9.19 |
| Angular velocity (3-1-3) | $\boldsymbol\omega_{B0} = \dot\varphi\,\mathbf k_B + \dot\theta\,\mathbf i_1 + \dot\psi\,\mathbf k_0$ | Eq. 9.21 |
| Body components (3-1-3) | $(\dot\theta\cos\varphi + \dot\psi\sin\theta\sin\varphi,\ -\dot\theta\sin\varphi + \dot\psi\sin\theta\cos\varphi,\ \dot\varphi + \dot\psi\cos\theta)$ | Eqs. 9.22-9.24 |
| 3-2-1 (yaw, pitch, roll) | $[{}_0R_B] = [{}_0R_1(z,\psi)][{}_1R_2(y,\theta)][{}_2R_B(x,\varphi)]$; body rates $(\dot\varphi - \dot\psi\sin\theta,\ \dot\theta\cos\varphi + \dot\psi\cos\theta\sin\varphi,\ -\dot\theta\sin\varphi + \dot\psi\cos\theta\cos\varphi)$ (extension) | Eqs. 1.18-1.20, 3.14 |
| Singularities | 3-1-3 at $\theta \in \{0,\pi\}$; 3-2-1 at $\theta \in \{\pi/2, 3\pi/2\}$ | Sec. 9.2.2 |
| Degrees of freedom | 6 for a free rigid body | Sec. 9.3 |
| Volume element | $dV = dx\,dy\,dz = R\,dR\,d\theta\,dz = r^2\cos\varphi\,dr\,d\theta\,d\varphi$ | Eq. 10.5 |
| Mass and centre of mass | $m = \int_{\mathcal D}dm$, $\mathbf r_0^G = \frac1m\int_{\mathcal D}\mathbf r_0^P\,dm$ | Eqs. 10.6, 10.8 |
| Moments of inertia | $I_x = \int(y^2+z^2)\,dm$, $I_{xy} = \int z^2\,dm$, $I_O = \int(x^2+y^2+z^2)\,dm$ | Eqs. 10.10-10.12 |
| Relation of moments | $2I_O = 2(I_{xy}+I_{xz}+I_{yz}) = I_x+I_y+I_z$; flat plate $I_O = I_z = I_x + I_y$ | Eq. 10.13 |
| Products of inertia | $P_{xy,xz} = \int zy\,dm$, $P_{xy,yz} = \int zx\,dm$, $P_{xz,yz} = \int yx\,dm$ | Eq. 10.15 |
| Symmetry theorems | $G$ on a plane or axis of symmetry; a plane of symmetry cancels the products that involve it; two planes of symmetry make the tensor diagonal | Secs. 10.3, 10.4; Lecture 8, Slide 13 |
| Wire | $m = \pi\lambda R$, $\mathbf r_0^G = \frac2\pi R\,\mathbf j$, $I_z = mR^2$, $I_x = I_y = \frac12 mR^2$ | Eqs. 10.18-10.22 |
| Plate | $I_z = \frac1{12}M(L^2+W^2)$, $I_x = \frac1{12}MW^2$, $I_y = \frac1{12}ML^2$, corner $P = \frac14 MLW$ | Eqs. 10.24-10.27 |
| Half disk | $m = \sigma\pi R^2/2$, $y_G = \frac{4R}{3\pi}$, $I_x = I_y = \frac14 mR^2$, $I_z = \frac12 mR^2$ | Eqs. 10.30-10.31 |
| Half sphere | $m = \frac23\rho\pi R^3$, $z_G = \frac38 R$, $I_x = I_y = I_z = \frac25 mR^2$ | Eqs. 10.33-10.34 |
| Tensor of inertia | $\boldsymbol{\mathcal I}_O = \int_{\mathcal D}[(r_0^P)^2\boldsymbol{\mathcal U} - \mathbf r_0^P\otimes\mathbf r_0^P]\,dm$, matrix of $I_x$, $-P_{xz,yz}$, ... | Eqs. 10.35, 10.38 |
| Moment about a line, product of two planes | $I_\ell = \mathbf u\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf u$, $P_{\pi_1,\pi_2} = -\mathbf u_1\cdot\boldsymbol{\mathcal I}_O\cdot\mathbf u_2$ | Eqs. 10.39, 10.40 |
| Change of basis | $[\boldsymbol{\mathcal I}_O]_{11} = [{}_0R_1]^T[\boldsymbol{\mathcal I}_O]_{00}[{}_0R_1]$ | Eq. 10.41 |
| Principal axes | $\boldsymbol{\mathcal I}_O\cdot\mathbf e_i = I_i\mathbf e_i$, $[\boldsymbol{\mathcal I}_O]_{11} = \mathrm{diag}(I_1,I_2,I_3)$ | Eqs. 10.42, 10.43 |
| Steiner | $\boldsymbol{\mathcal I}_O = \boldsymbol{\mathcal I}_G + m[(r_0^G)^2\boldsymbol{\mathcal U} - \mathbf r_0^G\otimes\mathbf r_0^G]$ | Eq. 10.48 |
| Parallel axis | $I_{z_0} = I_{z_G} + m[(x_0^G)^2 + (y_0^G)^2]$ | Sec. 10.8.1 |

**Back to:** [[Engineering Mechanics MOC]]
