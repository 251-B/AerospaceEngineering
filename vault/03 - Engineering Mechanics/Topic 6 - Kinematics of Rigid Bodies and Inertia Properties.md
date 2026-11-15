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
> **Meaning:** for a rotation about the second axis the minus sign moves below the diagonal, because the cyclic order is $z \to x$ (the pair $\mathbf k_1$, $\mathbf i_1$ is the right-handed pair in this view); a positive pitch raises the nose axis $\mathbf i$ above the horizontal plane only when $\mathbf k$ points down, as in aircraft axes.

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

