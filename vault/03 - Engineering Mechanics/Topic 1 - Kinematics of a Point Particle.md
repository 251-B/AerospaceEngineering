---
title: "Topic 1 - Kinematics of a Point Particle"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/teoria/Notes.pdf"
type: "Theory"
language: "English"
tags:
  - theory
  - topic-1
  - point-particle
  - kinematics
  - vectors
  - change-of-basis
  - simple-rotations
  - angular-velocity
  - intrinsic-basis
  - coordinate-systems
---

# Topic 1 - Kinematics of a Point Particle

> Kinematics describes motion without asking what causes it, and every quantity it uses is a vector or a tensor whose meaning does not depend on the basis chosen to write it: the work is to pick convenient bases, relate them through change of basis (rotation) matrices built from simple rotations, and differentiate vectors in time, where a vector of constant magnitude can only rotate, so its derivative is the cross product of an angular velocity $\boldsymbol\omega$ with it. With a reference frame $S_0$ fixed, the position $\mathbf r_0^P$ of a point particle, differentiated once and twice, gives its velocity $\mathbf v_0^P$ and acceleration $\mathbf a_0^P$, which can be written in Cartesian, cylindrical, spherical or intrinsic components.

This note follows `Notes.pdf` Chapter 1 (Getting started, Eqs. 1.1 to 1.79: mechanical modelling, vectors and tensors, vector bases, change of basis and rotation matrices, vector operations and vector differential calculus) and Chapter 2 (Kinematics of point particles, Eqs. 2.1 to 2.40: reference frames, position, velocity and acceleration, the trajectory and the intrinsic basis, curvilinear coordinates, degrees of freedom and constraints), and the deck of Lecture 1 (Fundamentals and particle kinematics), in the order of the notes. Chapter 1 is mathematical: its "first principles" are the definitions of the basis, of the dot and cross products and of the derivative, and every rotation matrix is built here column by column from the projections of the rotated unit vectors. See also [[Concept - Mechanical Modeling and Physical Quantities]], [[Concept - Vector Bases Rotation Matrices and Poisson Theorem]] and [[Concept - Attitude of a Reference Frame and Euler Angles]].

| Symbol | Meaning |
| :--- | :--- |
| $\mathbf A$, $A = \lVert\mathbf A\rVert$ | a vector (bold) and its magnitude or norm (normal type face) |
| $\mathbf e_A = \mathbf A/A$ | unit vector along $\mathbf A$ |
| $\mathcal B_0 : \{\mathbf i,\mathbf j,\mathbf k\}$ | canonical orthonormal right-handed basis, also written $\{\mathbf i_0,\mathbf j_0,\mathbf k_0\}$; axes $Ox$, $Oy$, $Oz$ |
| $\mathcal B_1 : \{\mathbf i_1,\mathbf j_1,\mathbf k_1\}$, $\mathcal B_2$, $\mathcal B_3$ | other orthonormal right-handed bases |
| $A_{x0}, A_{y0}, A_{z0}$ | components of $\mathbf A$ in $\mathcal B_0$ (written $A_x, A_y, A_z$ when only one basis is used) |
| $[\mathbf A]_0$ | column matrix of the components of $\mathbf A$ in $\mathcal B_0$ (the subindex names the basis) |
| $\ell_{x1,x0}$, $\ell_{x1,y0}$, ... | component of $\mathbf i_1$ along $\mathbf i_0$, along $\mathbf j_0$, ... (direction cosines) |
| $[{}_0R_1]$ | change of basis (rotation) matrix from $\mathcal B_1$ to $\mathcal B_0$: $[\mathbf A]_0 = [{}_0R_1][\mathbf A]_1$ |
| $[{}_0R_1(x,\theta_x)]$, $[{}_0R_1(y,\theta_y)]$, $[{}_0R_1(z,\theta_z)]$ | simple rotations by the angles $\theta_x$, $\theta_y$, $\theta_z$ about $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$ |
| $[U]$ | identity matrix |
| $\theta$ | angle of a vector about an axis, measured from a reference direction (from $Ox$ about $\mathbf k$ in the plane $Oxy$) |
| $\theta_{AB}$ | angle between the vectors $\mathbf A$ and $\mathbf B$ drawn from a common origin (the notes write $\theta$) |
| $\alpha, \beta, \gamma$ | direction angles of a unit vector with $\mathbf i$, $\mathbf j$, $\mathbf k$ |
| $[\mathbf A,\mathbf B,\mathbf C]$ | triple product $\mathbf A\cdot(\mathbf B\times\mathbf C)$ |
| $\bar{\bar M}$, $\mathbf A\otimes\mathbf B$ | second-order tensor (two bars, as in the notes) and tensor product |
| $\mathbf M$, $h$ | moment of a vector about a point, and distance from the point to its line of action (the notes write $\ell$) |
| $\mathbf e_\omega$, $\boldsymbol\omega$ | unit vector of the rotation axis and angular velocity vector |
| $[\Omega]$ | angular velocity matrix (antisymmetric) |
| $\nabla f$, $\nabla\cdot\mathbf A$, $\nabla\times\mathbf A$ | gradient, divergence and curl |

## 1. Mechanical modelling and physical quantities

### Models of reality

Classical (Newtonian) mechanics is governed by Newton's laws. It breaks down at speeds comparable with the speed of light and at atomic scales, but for engineering it is a very good model of reality; the most notable exception in aerospace is the relativistic correction of global navigation satellite systems (Notes.pdf, Ch. 1). In aerospace engineering it is applied to the motion of aircraft (position, velocity, acceleration and stability), of spacecraft (orbits, attitude, launch and orbit transfers) and of their subsystems (engines, flaps, landing gear), and it is the basis of fluid dynamics and structural dynamics.

All design and analysis activities require a model of the reality we want to study ([Lecture 1, Slide 3]; Notes.pdf, Sec. 1.1). The model identifies the design parameters, gives the performance figures and shows how each parameter affects the operation. It is built with linear algebra and calculus, and it is not the reality: it is a simplified representation that ignores some aspects of the system and its environment. Trying to "solve reality" directly leads to analysis paralysis; only after stating the simplifying assumptions can we solve a version of the problem. The conclusions of a model must always be validated against reality ([Lecture 1, Slide 3]).

Before solving a problem, write down explicitly (Notes.pdf, Sec. 1.1):

1. What the system under analysis is, what its environment is, and where the boundary between them lies.
2. What the interactions between the system and the environment are.
3. Which assumptions are taken at each step of the formulation.

The course idealises real objects in two ways ([Lecture 1, Slide 3]; Notes.pdf, Sec. 1.1):

| Model | What it keeps | When it is used |
| :--- | :--- | :--- |
| Point particle | no dimensions; only the translational motion | the dimensions do not matter to the motion and the orientation in space is of no interest (an aircraft for its flight performance) |
| Rigid body | finite size, no deformation; translation and rotation (position and attitude) | deformations are negligible compared with the overall motion (an aircraft responding to a perturbation of its flight condition) |
| Deformable body | elastic or inelastic deformation | outside the scope of the course (each element of an aircraft deflects in flight, some of them a lot) |

### Scalars, vectors and tensors

A physical quantity is anything we can measure or describe about a mechanical system ([Lecture 1, Slide 4]). Mechanical models use three kinds (Notes.pdf, Sec. 1.2):

| Kind | Order | Representation in a basis | Examples |
| :--- | :--- | :--- | :--- |
| Scalar | zero (an element of $\mathbb R$, a few of $\mathbb C$) | one number plus its units | mass, time, energy |
| Vector | one (an element of $\mathbb R^N$, $N$ = 2 or 3) | a column of $N$ numbers plus units | position, displacement, velocity, acceleration, angular velocity, force |
| Second-order tensor | two (an element of $\mathbb R^N\times\mathbb R^N$) | an $N\times N$ matrix plus units | tensor of inertia of a rigid body |

A vector cannot be represented by a magnitude alone: a displacement needs its starting point and its direction besides its numerical value. Vectors are written in bold, $\mathbf v$, and their magnitude or norm in normal type, $v$ (Notes.pdf, Sec. 1.2). In handwriting a small arrow marks a vector; failing to distinguish a vector from a scalar (and the magnitude of a vector is a scalar) is a serious error in an exam.

A tensor describes linear relations between vectors, scalars and other tensors. With a vector $\mathbf A$ and a tensor $\bar{\bar M}$ of matching dimension, the contractions below are a vector and a scalar (Notes.pdf, Sec. 1.2; [Lecture 1, Slide 4]):

| Contraction | Result |
| :--- | :--- |
| $\mathbf B = \bar{\bar M}\cdot\mathbf A$ | a vector |
| $p = \mathbf A\cdot\bar{\bar M}\cdot\mathbf A$ | a scalar |

Not every list of numbers is a physical vector or tensor: the set must have the structure of a vector space, the elements must have a physical meaning, and their meaning and behaviour must remain unaltered under rotations and other simple transformations of the plane and space (Notes.pdf, Sec. 1.2).

> [!key] Physical quantities do not depend on the observer
> A physical quantity does not depend on the observer, on his or her frame of reference or on its velocity ([Lecture 1, Slide 4]). Its components do depend on the basis in which they are written, but the vector or tensor itself is the same entity ([Lecture 1, Slide 6]).

### Free, sliding and bound vectors

Depending on what they represent, vectors are further classified by the role of their point of application (Notes.pdf, Sec. 1.2; [Lecture 1, Slide 4] calls bound vectors "fixed"):

| Class | What may be changed without changing its effect | Examples in the notes |
| :--- | :--- | :--- |
| Free vector | it may be shifted anywhere, keeping magnitude and direction; the point of application has no physical relevance | angular velocity, torque |
| Sliding vector | it may be moved along its line of action only | force on a rigid body (applying it on a different line does matter) |
| Bound vector | nothing: magnitude, direction and point of application are fixed | force on a deformable body |

The vectors of a vector basis are always free vectors (Notes.pdf, Sec. 1.4).

## 2. Vector spaces, bases and components

### Vector spaces

A set $V$ is a vector space over $\mathbb R$ when it has a vector addition and a multiplication by a scalar with the properties below, for any elements $\mathbf A$, $\mathbf B$ of $V$ and any scalars $\lambda$, $\mu$ (Notes.pdf, Sec. 1.3; [Lecture 1, Slide 5]). The vector spaces of mechanics are the plane $\mathbb R^2$ and space $\mathbb R^3$.

| Operation | Required properties |
| :--- | :--- |
| Addition | associative and commutative; null vector $\mathbf 0$; inverse $-\mathbf A$ with $\mathbf A + (-\mathbf A) = \mathbf 0$ |
| Multiplication by a scalar | unity, $1\,\mathbf A = \mathbf A$; $\lambda(\mu\mathbf A) = (\lambda\mu)\mathbf A$ |
| Both together | $(\lambda+\mu)\mathbf A = \lambda\mathbf A + \mu\mathbf A$ and $\lambda(\mathbf A+\mathbf B) = \lambda\mathbf A + \lambda\mathbf B$ |

A scalar multiple $\lambda\mathbf A$ is parallel to $\mathbf A$: it points in the same direction when $\lambda$ is positive and in the opposite direction (antiparallel) when it is negative, and its magnitude is $|\lambda|$ times that of $\mathbf A$ (Notes.pdf, Sec. 1.3). This gives every non-zero vector its unit vector.

> [!derivation] Magnitude and direction: the unit vector of a vector
> **Law:** magnitude of a scalar multiple; multiplication by the inverse of the magnitude
> **Source:** Notes.pdf, Sec. 1.3; [Lecture 1, Slide 5]
>
> $$\begin{aligned}
> \lVert\lambda\mathbf A\rVert &= |\lambda|\,A \quad &\text{(magnitude of a scalar multiple, Sec. 1.3)} \\
> \mathbf e_A &= \frac{1}{A}\,\mathbf A \quad &\text{(choose $\lambda = 1/A$, positive because $\mathbf A \neq \mathbf 0$)} \\
> \lVert\mathbf e_A\rVert &= \frac{1}{A}\,A \quad &\text{(first row with $|\lambda| = 1/A$)} \\
> &= 1 \quad &\text{(simplify)} \\
> A\,\mathbf e_A &= \mathbf A \quad &\text{(multiply the second row by $A$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_A = \frac{\mathbf A}{A},\qquad \lVert\mathbf e_A\rVert = 1,\qquad \mathbf A = A\,\mathbf e_A}$$
>
> **Units:** $\mathbf e_A$ is $[\mathbf A]/[\mathbf A] = [1]$, dimensionless; $A$ carries all the units of $\mathbf A$
> **Meaning:** a vector is the product of a scalar that encodes its magnitude and a unit vector that encodes its direction; the unit vector is parallel to $\mathbf A$ and points the same way.

### Orthonormal right-handed bases

A vector basis is an ordered set of $N$ linearly independent vectors, $N$ being the dimension of the space; by linear combination (superposition) they span the whole space, so any vector can be given by its components in the basis (Notes.pdf, Sec. 1.4; [Lecture 1, Slide 6]). The course uses only orthonormal right-handed bases, such as the canonical basis of Eq. 1.1, whose vectors $\mathbf i$, $\mathbf j$, $\mathbf k$ lie along the coordinate axes $Ox$, $Oy$, $Oz$ (Notes.pdf Fig. 1.1). The three conditions of [Lecture 1, Slide 6] are:

| Condition | Statement |
| :--- | :--- |
| Unit vectors | $\lVert\mathbf i\rVert = \lVert\mathbf j\rVert = \lVert\mathbf k\rVert = 1$ |
| Mutually orthogonal | each pair is perpendicular: $\mathbf i\cdot\mathbf j = \mathbf j\cdot\mathbf k = \mathbf k\cdot\mathbf i = 0$ |
| Right-handed | $\mathbf i\times\mathbf j = \mathbf k$: thumb, index and middle finger of the right hand, at 90 degrees from each other, point along $\mathbf i$, $\mathbf j$, $\mathbf k$ in that order |

When several bases are used they carry an index, $\mathcal B_0$, $\mathcal B_1$, and the relations among them must always be stated ([Lecture 1, Slide 6]).

![[attachments/EM-T/t1-basis-components.svg]]

> [!derivation] Components of a vector in a basis
> **Law:** decomposition along the coordinate axes; a vector along an axis is its magnitude times the unit vector of the axis
> **Source:** Notes.pdf, Eq. 1.2; Notes.pdf Fig. 1.1; [Lecture 1, Slide 6]
>
> $$\begin{aligned}
> \mathbf A &= \mathbf A_x + \mathbf A_y + \mathbf A_z \quad &\text{(sum of three vectors along $Ox$, $Oy$, $Oz$: the edges of the box of Fig. 1.1)} \\
> &= A_x\,\mathbf i + A_y\,\mathbf j + A_z\,\mathbf k \quad &\text{(each edge is its signed length times the unit vector of its axis)} \\
> &= \begin{bmatrix} A_x \cr A_y \cr A_z \end{bmatrix}_0 \quad &\text{(column matrix of the components; the subindex names the basis $\mathcal B_0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf A = A_x\,\mathbf i + A_y\,\mathbf j + A_z\,\mathbf k = \begin{bmatrix} A_x \\ A_y \\ A_z \end{bmatrix}_0}$$
>
> **Units:** each component carries the units of $\mathbf A$; the unit vectors are dimensionless
> **Meaning:** the components are a representation of the vector, not the vector: the same vector has other components in another basis, which is why the subindex of the basis may only be dropped when the context makes it evident.

### Components of a vector with a known angle

A recurring situation: $\mathbf A$ lies in a coordinate plane, here $Oxy$, and we know its magnitude $A$ and the angle $\theta$ it forms with one of the axes, here $Ox$, measured counterclockwise when $\mathbf k$ points out of the paper (Notes.pdf, Sec. 1.4.1, Fig. 1.2). When $A$ and $\theta$ are not known, they are defined as unknowns and carried through the problem.

![[attachments/EM-T/t1-known-angle.svg]]

> [!derivation] Components from the magnitude and the angle with the axis Ox
> **Law:** right triangle formed by $\mathbf A$ and its projections on $Ox$ and $Oy$
> **Source:** Notes.pdf, Eq. 1.3; Notes.pdf, Eq. 1.4; Notes.pdf, Eq. 1.5; Notes.pdf Fig. 1.2
>
> View with $\mathbf k$ out of the paper (⊙), $\mathbf i$ to the right and $\mathbf j$ up. The right triangle has the vertex $O$, the tip of $\mathbf A$ and the foot of the perpendicular from the tip to $Ox$: its hypotenuse is $\mathbf A$ (length $A$), the leg on $Ox$ is adjacent to $\theta$ and the leg parallel to $Oy$ is opposite to $\theta$.
>
> $$\begin{aligned}
> \cos\theta &= \frac{A_x}{A} \quad &\text{(adjacent leg over hypotenuse)} \\
> A_x &= A\cos\theta \quad &\text{(multiply by $A$)} \\
> \sin\theta &= \frac{A_y}{A} \quad &\text{(opposite leg over hypotenuse)} \\
> A_y &= A\sin\theta \quad &\text{(multiply by $A$)} \\
> A_z &= 0 \quad &\text{($\mathbf A$ lies in the plane $Oxy$, normal to $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf A = A\cos\theta\,\mathbf i + A\sin\theta\,\mathbf j}$$
>
> **Units:** $[\mathbf A]\cdot[1]$ in both components: the cosine and the sine are ratios of lengths
> **Meaning:** the triangle is drawn with $\theta$ in the first quadrant; for any other $\theta$ the signs of $\cos\theta$ and $\sin\theta$ give the signs of the components (with $\theta$ slightly above a right angle, $A_x$ is small and negative).

An angle is often measured from the other axis of the plane, for instance from the vertical $Oy$. Calling it $\beta$ (it is the direction angle of $\mathbf A$ with $\mathbf j$, see Eq. 1.29 below), the roles of sine and cosine swap, and the swap is proved from the angle $\theta$ of the standard polar convention.

> [!derivation] Components when the angle is measured from the axis Oy
> **Law:** complementary angles; cosine and sine of a difference
> **Source:** Notes.pdf, Eq. 1.3; Notes.pdf, Eq. 1.4; Notes.pdf, Sec. 1.4.1
>
> In the same view, $\beta$ is measured clockwise from $\mathbf j$ towards $\mathbf i$, so that $\theta$ and $\beta$ together fill the right angle between $Ox$ and $Oy$ (the figure above marks both). In the same triangle the leg parallel to $Oy$ is adjacent to $\beta$ and the leg on $Ox$ is opposite to it.
>
> $$\begin{aligned}
> \theta &= \frac{\pi}{2} - \beta \quad &\text{(the two angles complete the right angle between $\mathbf i$ and $\mathbf j$)} \\
> A_x &= A\cos\left(\frac{\pi}{2}-\beta\right) \quad &\text{(substitute in Eq. 1.3)} \\
> &= A\left(\cos\frac{\pi}{2}\cos\beta + \sin\frac{\pi}{2}\sin\beta\right) \quad &\text{(cosine of a difference)} \\
> &= A\sin\beta \quad &\text{($\cos\frac{\pi}{2} = 0$, $\sin\frac{\pi}{2} = 1$)} \\
> A_y &= A\sin\left(\frac{\pi}{2}-\beta\right) \quad &\text{(substitute in Eq. 1.4)} \\
> &= A\left(\sin\frac{\pi}{2}\cos\beta - \cos\frac{\pi}{2}\sin\beta\right) \quad &\text{(sine of a difference)} \\
> &= A\cos\beta \quad &\text{($\cos\frac{\pi}{2} = 0$, $\sin\frac{\pi}{2} = 1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf A = A\sin\beta\,\mathbf i + A\cos\beta\,\mathbf j}$$
>
> **Units:** $[\mathbf A]$ in both components
> **Meaning:** the cosine always goes with the leg adjacent to the angle that was given: with an angle measured from $Oy$ the cosine multiplies $\mathbf j$; a vector along $\mathbf j$ ($\beta$ equal to zero) has only the component $A_y$, as it must.

> [!key] Projecting when the plane is not a coordinate plane
> When $\mathbf A$ lies in a plane that is not a coordinate plane, define a new basis in which it is, related to the first one by a chain of simple rotations (Section 3 below). Draw more than one sketch: a general view of the projection, plus one auxiliary diagram per coordinate plane involved (Notes.pdf, Sec. 1.4.1).

## 3. Working with several bases: change of basis and rotation matrices

### The change of basis matrix

Different vector quantities are often easier to describe in different bases, so a procedure to pass the components of a vector from one basis to another is needed (Notes.pdf, Sec. 1.5). Take two orthonormal right-handed bases $\mathcal B_0$ and $\mathcal B_1$. The physical vector $\mathbf A$ is one entity, written in either basis (Eq. 1.6). To relate the two sets of components systematically, each vector of $\mathcal B_1$ is first written in $\mathcal B_0$; the nine numbers $\ell_{x1,x0}$, ..., $\ell_{z1,z0}$ are the change of basis relations of Eq. 1.8 ([Lecture 1, Slide 7]).

| Change of basis relations (Eq. 1.8) |
| :--- |
| $\mathbf i_1 = \ell_{x1,x0}\,\mathbf i_0 + \ell_{x1,y0}\,\mathbf j_0 + \ell_{x1,z0}\,\mathbf k_0$ |
| $\mathbf j_1 = \ell_{y1,x0}\,\mathbf i_0 + \ell_{y1,y0}\,\mathbf j_0 + \ell_{y1,z0}\,\mathbf k_0$ |
| $\mathbf k_1 = \ell_{z1,x0}\,\mathbf i_0 + \ell_{z1,y0}\,\mathbf j_0 + \ell_{z1,z0}\,\mathbf k_0$ |

> [!derivation] Components in the old basis from components in the new one
> **Law:** substitution of the change of basis relations; uniqueness of the components in a basis
> **Source:** Notes.pdf, Eq. 1.6; Notes.pdf, Eq. 1.9; Notes.pdf, Eq. 1.12; Notes.pdf, Eq. 1.13; [Lecture 1, Slide 7]
>
> $$\begin{aligned}
> \mathbf A &= A_{x1}\,\mathbf i_1 + A_{y1}\,\mathbf j_1 + A_{z1}\,\mathbf k_1 \quad &\text{(the vector written in $\mathcal B_1$, Eq. 1.6)} \\
> &= A_{x1}\left(\ell_{x1,x0}\mathbf i_0 + \ell_{x1,y0}\mathbf j_0 + \ell_{x1,z0}\mathbf k_0\right) + A_{y1}\left(\ell_{y1,x0}\mathbf i_0 + \ell_{y1,y0}\mathbf j_0 + \ell_{y1,z0}\mathbf k_0\right) + A_{z1}\left(\ell_{z1,x0}\mathbf i_0 + \ell_{z1,y0}\mathbf j_0 + \ell_{z1,z0}\mathbf k_0\right) \quad &\text{(substitute Eq. 1.8)} \\
> &= \left(\ell_{x1,x0}A_{x1} + \ell_{y1,x0}A_{y1} + \ell_{z1,x0}A_{z1}\right)\mathbf i_0 + \left(\ell_{x1,y0}A_{x1} + \ell_{y1,y0}A_{y1} + \ell_{z1,y0}A_{z1}\right)\mathbf j_0 + \left(\ell_{x1,z0}A_{x1} + \ell_{y1,z0}A_{y1} + \ell_{z1,z0}A_{z1}\right)\mathbf k_0 \quad &\text{(collect the coefficients of $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$)} \\
> A_{x0} &= \ell_{x1,x0}A_{x1} + \ell_{y1,x0}A_{y1} + \ell_{z1,x0}A_{z1} \quad &\text{(compare with $\mathbf A = A_{x0}\mathbf i_0 + A_{y0}\mathbf j_0 + A_{z0}\mathbf k_0$: components are unique, Eq. 1.9)} \\
> A_{y0} &= \ell_{x1,y0}A_{x1} + \ell_{y1,y0}A_{y1} + \ell_{z1,y0}A_{z1} \quad &\text{(coefficient of $\mathbf j_0$, Eq. 1.10)} \\
> A_{z0} &= \ell_{x1,z0}A_{x1} + \ell_{y1,z0}A_{y1} + \ell_{z1,z0}A_{z1} \quad &\text{(coefficient of $\mathbf k_0$, Eq. 1.11)}
> \end{aligned}$$
>
> $$\boxed{\begin{bmatrix} A_{x0} \\ A_{y0} \\ A_{z0} \end{bmatrix}_0 = [{}_0R_1]\begin{bmatrix} A_{x1} \\ A_{y1} \\ A_{z1} \end{bmatrix}_1,\qquad [{}_0R_1] = \begin{bmatrix} \ell_{x1,x0} & \ell_{y1,x0} & \ell_{z1,x0} \\ \ell_{x1,y0} & \ell_{y1,y0} & \ell_{z1,y0} \\ \ell_{x1,z0} & \ell_{y1,z0} & \ell_{z1,z0} \end{bmatrix}}$$
>
> **Units:** the entries $\ell$ are components of unit vectors, dimensionless; both columns carry the units of $\mathbf A$
> **Meaning:** right-multiplying $[{}_0R_1]$ by the components of a vector in $\mathcal B_1$ gives its components in $\mathcal B_0$; the subindex of each column matrix says in which basis it is written, otherwise the expression would be ambiguous.

> [!derivation] The columns of the matrix are the new unit vectors written in the old basis
> **Law:** the change of basis applied to $\mathbf i_1$, whose components in its own basis are one, zero, zero
> **Source:** Notes.pdf, Eq. 1.7; Notes.pdf, Eq. 1.12; Notes.pdf, Sec. 1.5
>
> $$\begin{aligned}
> [\mathbf i_1]_1 &= \begin{bmatrix} 1 \cr 0 \cr 0 \end{bmatrix}_1 \quad &\text{($\mathbf i_1 = 1\,\mathbf i_1 + 0\,\mathbf j_1 + 0\,\mathbf k_1$)} \\
> [\mathbf i_1]_0 &= [{}_0R_1]\begin{bmatrix} 1 \cr 0 \cr 0 \end{bmatrix}_1 \quad &\text{(Eq. 1.12)} \\
> &= \begin{bmatrix} \ell_{x1,x0}\cdot 1 + \ell_{y1,x0}\cdot 0 + \ell_{z1,x0}\cdot 0 \cr \ell_{x1,y0}\cdot 1 + \ell_{y1,y0}\cdot 0 + \ell_{z1,y0}\cdot 0 \cr \ell_{x1,z0}\cdot 1 + \ell_{y1,z0}\cdot 0 + \ell_{z1,z0}\cdot 0 \end{bmatrix}_0 \quad &\text{(each row of the matrix times the column)} \\
> &= \begin{bmatrix} \ell_{x1,x0} \cr \ell_{x1,y0} \cr \ell_{x1,z0} \end{bmatrix}_0 \quad &\text{(the first column of $[{}_0R_1]$, which is Eq. 1.7)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \Big[\,[\mathbf i_1]_0\ \Big|\ [\mathbf j_1]_0\ \Big|\ [\mathbf k_1]_0\,\Big]}$$
>
> **Units:** dimensionless
> **Meaning:** the same product with the columns of zeros and one in the second and third places gives $\mathbf j_1$ and $\mathbf k_1$, so a change of basis matrix is written column by column: column $n$ is the $n$-th new unit vector projected on the old basis. This is how every rotation matrix of this note is built.

The orthonormality of both bases makes $[{}_0R_1]$ an orthogonal matrix. The notes list its properties without demonstration (Notes.pdf, Sec. 1.5); Section 5 proves the first two once the dot and triple products are written in components.

| Property | Statement |
| :--- | :--- |
| Inverse equals transpose (Eq. 1.14) | $[{}_1R_0] = [{}_0R_1]^{-1} = [{}_0R_1]^T$, hence $[{}_0R_1]^T[{}_0R_1] = [U]$ |
| Unit determinant (Eq. 1.15) | $\lvert[{}_0R_1]\rvert = 1$ |
| Eigenvalues | one eigenvalue equal to 1; in general the other two are complex conjugates of unit absolute value |
| Columns and rows | the columns are $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$; the rows are $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$ in $\mathcal B_1$ |

> [!warning] Changing the basis does not move the vector
> When the components of $\mathbf A$ are passed from one basis to another, the vector is not moved or rotated: it is only described from a different basis, so the numbers that represent it change (Notes.pdf, Sec. 1.5).

### Composition of changes of basis

> [!derivation] Chaining two changes of basis
> **Law:** substitution of one change of basis into the other
> **Source:** Notes.pdf, Eq. 1.16; Notes.pdf, Eq. 1.12
>
> $$\begin{aligned}
> [\mathbf A]_0 &= [{}_0R_1]\,[\mathbf A]_1 \quad &\text{(from $\mathcal B_1$ to $\mathcal B_0$, Eq. 1.12)} \\
> [\mathbf A]_1 &= [{}_1R_2]\,[\mathbf A]_2 \quad &\text{(from $\mathcal B_2$ to $\mathcal B_1$, the same law)} \\
> [\mathbf A]_0 &= [{}_0R_1]\,[{}_1R_2]\,[\mathbf A]_2 \quad &\text{(substitute the second row into the first)} \\
> [\mathbf A]_0 &= [{}_0R_2]\,[\mathbf A]_2 \quad &\text{(definition of the matrix from $\mathcal B_2$ to $\mathcal B_0$; true for every $\mathbf A$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_2] = [{}_0R_1]\,[{}_1R_2]}$$
>
> **Units:** dimensionless
> **Meaning:** going from $\mathcal B_2$ to $\mathcal B_0$ directly is the same as going through $\mathcal B_1$; the matrices are written in the order of the bases, from the first to the last, and in general they do not commute.

Eq. 1.17 writes the composite matrix of $n$ sequential changes of basis as the right-to-left product of the matrices of each change. Read with Eq. 1.16, this holds for the matrices in the other direction, from the old basis to the new one, as the next box shows.

> [!derivation] Right-to-left product of n changes of basis
> **Law:** Eq. 1.16 repeated; transpose of a product; inverse equals transpose
> **Source:** Notes.pdf, Eq. 1.17; Notes.pdf, Eq. 1.16; Notes.pdf, Eq. 1.14
>
> $$\begin{aligned}
> [{}_0R_n] &= [{}_0R_1]\,[{}_1R_2]\cdots[{}_{n-1}R_n] \quad &\text{(Eq. 1.16 applied $n-1$ times)} \\
> [{}_nR_0] &= [{}_0R_n]^T \quad &\text{(Eq. 1.14)} \\
> &= [{}_{n-1}R_n]^T\cdots[{}_1R_2]^T\,[{}_0R_1]^T \quad &\text{(the transpose of a product is the product of the transposes in reverse order)} \\
> &= [{}_nR_{n-1}]\cdots[{}_2R_1]\,[{}_1R_0] \quad &\text{(Eq. 1.14 for each factor)}
> \end{aligned}$$
>
> $$\boxed{[R] = [R_n]\cdots[R_2]\,[R_1],\qquad [R_k] = [{}_kR_{k-1}],\quad [R] = [{}_nR_0]}$$
>
> **Units:** dimensionless
> **Meaning:** the matrix of the $k$-th change, from $\mathcal B_{k-1}$ to $\mathcal B_k$, multiplies on the left of the earlier ones; whichever direction is used, state clearly the relation between the bases, either with Eq. 1.8 or with the matrix of Eq. 1.13 (Notes.pdf, Sec. 1.5).

### Equivalence with rotations

A result due to Euler states that any two right-handed bases are related by a single rotation: there is always an axis, of unit vector $\mathbf e$, and an angle such that rotating $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$ about that axis by that angle makes them coincide with $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ (Notes.pdf, Sec. 1.5.1). The rotation is represented by the same matrix as the change of basis.

> [!derivation] The rotation that carries B0 onto B1 has the matrix of the change of basis
> **Law:** a rotation maps $\mathbf i_0$ to $\mathbf i_1$, $\mathbf j_0$ to $\mathbf j_1$, $\mathbf k_0$ to $\mathbf k_1$; linearity of the rotation
> **Source:** Notes.pdf, Sec. 1.5.1; Notes.pdf, Eq. 1.13
>
> $$\begin{aligned}
> [\mathbf i_0]_0 &= \begin{bmatrix} 1 \cr 0 \cr 0 \end{bmatrix}_0 \ \longrightarrow\ [\mathbf i_1]_0 = \begin{bmatrix} \ell_{x1,x0} \cr \ell_{x1,y0} \cr \ell_{x1,z0} \end{bmatrix}_0 \quad &\text{(the rotation maps $\mathbf i_0$ onto $\mathbf i_1$, Eq. 1.7)} \\
> \begin{bmatrix} A'_x \cr A'_y \cr A'_z \end{bmatrix}_0 &= A_x [\mathbf i_1]_0 + A_y [\mathbf j_1]_0 + A_z [\mathbf k_1]_0 \quad &\text{(a rotation is linear: $A_x\mathbf i_0 + A_y\mathbf j_0 + A_z\mathbf k_0$ goes to $A_x\mathbf i_1 + A_y\mathbf j_1 + A_z\mathbf k_1$)} \\
> &= [{}_0R_1]\begin{bmatrix} A_x \cr A_y \cr A_z \end{bmatrix}_0 \quad &\text{(a matrix times a column is the combination of its columns, which are $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$)}
> \end{aligned}$$
>
> $$\boxed{[\mathbf A']_0 = [{}_0R_1]\,[\mathbf A]_0}$$
>
> **Units:** dimensionless matrix; both columns carry the units of $\mathbf A$
> **Meaning:** the same operation as Eq. 1.12, provided that the primed components are read as the components of the vector in $\mathcal B_0$ and the unprimed ones as its components in $\mathcal B_1$.

> [!key] Two readings of one matrix
> $[{}_0R_1]$ is either the static relation between the components of a vector in $\mathcal B_1$ and in $\mathcal B_0$, or the dynamic transformation of the components of a vector rotated as seen from the single basis $\mathcal B_0$; the mathematical operation is the same. From here on we say that $\mathcal B_1$ is rotated with respect to $\mathcal B_0$ and call $[{}_0R_1]$ a rotation matrix (Notes.pdf, Sec. 1.5.1).

### Simple rotations

A rotation is simple when its axis is one of the vectors of $\mathcal B_0$. That vector is stationary, so the corresponding vector of $\mathcal B_1$ coincides with it, while the rest of space rotates by an angle about it, positive by the right-hand rule: with the fingers of the right hand curled in the sense of the rotation, the thumb points along the positive axis (Notes.pdf, Sec. 1.5.2, Fig. 1.3). Each matrix is written by looking down from the stationary axis, so that it points out of the paper, and projecting the two rotated vectors on the two fixed ones.

![[attachments/EM-T/t1-rotation-x.svg]]

> [!derivation] Simple rotation about the x axis
> **Law:** simple rotation by $\theta_x$ about $\mathbf i_0$, positive by the right-hand rule; columns are the rotated vectors in $\mathcal B_0$
> **Source:** Notes.pdf, Eq. 1.18; Notes.pdf Fig. 1.3
>
> View with $\mathbf i_0 \equiv \mathbf i_1$ out of the paper (⊙), $\mathbf j_0$ to the right and $\mathbf k_0$ up ($\mathbf j_0\times\mathbf k_0 = \mathbf i_0$). With the thumb along $\mathbf i_0$ the fingers curl counterclockwise, so positive $\theta_x$ is counterclockwise. Each rotated unit vector is the hypotenuse (length one) of a right triangle whose legs lie along $\mathbf j_0$ and $\mathbf k_0$.
>
> $$\begin{aligned}
> \mathbf i_1 &= \mathbf i_0 \quad &\text{(the axis of the rotation does not move)} \\
> \mathbf j_1 &= \cos\theta_x\,\mathbf j_0 + \sin\theta_x\,\mathbf k_0 \quad &\text{($\theta_x$ lies between $\mathbf j_0$ and $\mathbf j_1$: adjacent leg along $\mathbf j_0$, opposite leg along $\mathbf k_0$)} \\
> \mathbf k_1 &= -\sin\theta_x\,\mathbf j_0 + \cos\theta_x\,\mathbf k_0 \quad &\text{($\theta_x$ lies between $\mathbf k_0$ and $\mathbf k_1$: adjacent leg along $\mathbf k_0$; $\mathbf k_0$ turned counterclockwise leans left, so the opposite leg points along $-\mathbf j_0$)} \\
> [{}_0R_1] &= \begin{pmatrix} 1 & 0 & 0 \cr 0 & \cos\theta_x & -\sin\theta_x \cr 0 & \sin\theta_x & \cos\theta_x \end{pmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos\theta_x\cos\theta_x - (-\sin\theta_x)\sin\theta_x\right) \quad &\text{(expand along the first row)} \\
> &= \cos^2\theta_x + \sin^2\theta_x \quad &\text{(simplify the signs)} \\
> &= 1 \quad &\text{(Pythagoras on the unit hypotenuse)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{pmatrix} 1 & 0 & 0 \cr 0 & \cos^2\theta_x + \sin^2\theta_x & \cos\theta_x\sin\theta_x - \sin\theta_x\cos\theta_x \cr 0 & \sin\theta_x\cos\theta_x - \cos\theta_x\sin\theta_x & \sin^2\theta_x + \cos^2\theta_x \end{pmatrix} \quad &\text{(entry $(m,n)$ is row $m$ times row $n$)} \\
> &= [U] \quad &\text{(diagonal: Pythagoras; off-diagonal: the two products cancel)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1(x,\theta_x)] = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\theta_x & -\sin\theta_x \\ 0 & \sin\theta_x & \cos\theta_x \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** the only minus sign sits in the column of $\mathbf k_1$, in the row of $\mathbf j_0$: the rotated third vector acquires a component along the negative second axis.

![[attachments/EM-T/t1-rotation-y.svg]]

> [!derivation] Simple rotation about the y axis
> **Law:** simple rotation by $\theta_y$ about $\mathbf j_0$, positive by the right-hand rule; columns are the rotated vectors in $\mathcal B_0$
> **Source:** Notes.pdf, Eq. 1.19; Notes.pdf Fig. 1.3
>
> View with $\mathbf j_0 \equiv \mathbf j_1$ out of the paper (⊙). Since $\mathbf k_0\times\mathbf i_0 = \mathbf j_0$, the pair in the right-handed order is $\mathbf k_0$, $\mathbf i_0$: $\mathbf k_0$ to the right and $\mathbf i_0$ up. Positive $\theta_y$ is counterclockwise in this view.
>
> $$\begin{aligned}
> \mathbf j_1 &= \mathbf j_0 \quad &\text{(the axis of the rotation does not move)} \\
> \mathbf k_1 &= \cos\theta_y\,\mathbf k_0 + \sin\theta_y\,\mathbf i_0 \quad &\text{($\theta_y$ lies between $\mathbf k_0$ and $\mathbf k_1$: adjacent leg along $\mathbf k_0$, opposite leg along $\mathbf i_0$)} \\
> \mathbf i_1 &= \cos\theta_y\,\mathbf i_0 - \sin\theta_y\,\mathbf k_0 \quad &\text{($\theta_y$ lies between $\mathbf i_0$ and $\mathbf i_1$: adjacent leg along $\mathbf i_0$; $\mathbf i_0$ turned counterclockwise leans left, so the opposite leg points along $-\mathbf k_0$)} \\
> [{}_0R_1] &= \begin{pmatrix} \cos\theta_y & 0 & \sin\theta_y \cr 0 & 1 & 0 \cr -\sin\theta_y & 0 & \cos\theta_y \end{pmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos\theta_y\cos\theta_y - \sin\theta_y(-\sin\theta_y)\right) \quad &\text{(expand along the second row; the cofactor sign of entry $(2,2)$ is $+$)} \\
> &= \cos^2\theta_y + \sin^2\theta_y \quad &\text{(simplify the signs)} \\
> &= 1 \quad &\text{(Pythagoras on the unit hypotenuse)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{pmatrix} \cos^2\theta_y + \sin^2\theta_y & 0 & -\cos\theta_y\sin\theta_y + \sin\theta_y\cos\theta_y \cr 0 & 1 & 0 \cr -\sin\theta_y\cos\theta_y + \cos\theta_y\sin\theta_y & 0 & \sin^2\theta_y + \cos^2\theta_y \end{pmatrix} \quad &\text{(entry $(m,n)$ is row $m$ times row $n$)} \\
> &= [U] \quad &\text{(diagonal: Pythagoras; off-diagonal: the two products cancel)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1(y,\theta_y)] = \begin{bmatrix} \cos\theta_y & 0 & \sin\theta_y \\ 0 & 1 & 0 \\ -\sin\theta_y & 0 & \cos\theta_y \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** here the minus sign sits in the column of $\mathbf i_1$, in the row of $\mathbf k_0$, below the diagonal, because in the cyclic order $x \to y \to z \to x$ the vector that follows the axis $\mathbf j_0$ is $\mathbf k_0$, not $\mathbf i_0$.

> [!warning] The y rotation drawn with x to the right
> If the plane $Oxz$ is drawn with $\mathbf i_0$ to the right and $\mathbf k_0$ up, then $\mathbf j_0$ points into the paper (⊗) and positive $\theta_y$ looks clockwise. Drawing it counterclockwise in that view flips the sign of both sines. Draw the view from the stationary axis, with that axis out of the paper (Notes.pdf, Sec. 1.5.2).

![[attachments/EM-T/t1-rotation-z.svg]]

> [!derivation] Simple rotation about the z axis
> **Law:** simple rotation by $\theta_z$ about $\mathbf k_0$, positive by the right-hand rule; columns are the rotated vectors in $\mathcal B_0$
> **Source:** Notes.pdf, Eq. 1.20; Notes.pdf Fig. 1.3
>
> View with $\mathbf k_0 \equiv \mathbf k_1$ out of the paper (⊙), $\mathbf i_0$ to the right and $\mathbf j_0$ up ($\mathbf i_0\times\mathbf j_0 = \mathbf k_0$). Positive $\theta_z$ is counterclockwise.
>
> $$\begin{aligned}
> \mathbf k_1 &= \mathbf k_0 \quad &\text{(the axis of the rotation does not move)} \\
> \mathbf i_1 &= \cos\theta_z\,\mathbf i_0 + \sin\theta_z\,\mathbf j_0 \quad &\text{($\theta_z$ lies between $\mathbf i_0$ and $\mathbf i_1$: adjacent leg along $\mathbf i_0$, opposite leg along $\mathbf j_0$)} \\
> \mathbf j_1 &= -\sin\theta_z\,\mathbf i_0 + \cos\theta_z\,\mathbf j_0 \quad &\text{($\theta_z$ lies between $\mathbf j_0$ and $\mathbf j_1$: adjacent leg along $\mathbf j_0$; $\mathbf j_0$ turned counterclockwise leans left, so the opposite leg points along $-\mathbf i_0$)} \\
> [{}_0R_1] &= \begin{pmatrix} \cos\theta_z & -\sin\theta_z & 0 \cr \sin\theta_z & \cos\theta_z & 0 \cr 0 & 0 & 1 \end{pmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos\theta_z\cos\theta_z - (-\sin\theta_z)\sin\theta_z\right) \quad &\text{(expand along the third row)} \\
> &= \cos^2\theta_z + \sin^2\theta_z \quad &\text{(simplify the signs)} \\
> &= 1 \quad &\text{(Pythagoras on the unit hypotenuse)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{pmatrix} \cos^2\theta_z + \sin^2\theta_z & \cos\theta_z\sin\theta_z - \sin\theta_z\cos\theta_z & 0 \cr \sin\theta_z\cos\theta_z - \cos\theta_z\sin\theta_z & \sin^2\theta_z + \cos^2\theta_z & 0 \cr 0 & 0 & 1 \end{pmatrix} \quad &\text{(entry $(m,n)$ is row $m$ times row $n$)} \\
> &= [U] \quad &\text{(diagonal: Pythagoras; off-diagonal: the two products cancel)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1(z,\theta_z)] = \begin{bmatrix} \cos\theta_z & -\sin\theta_z & 0 \\ \sin\theta_z & \cos\theta_z & 0 \\ 0 & 0 & 1 \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** with $\theta_z$ equal to zero the matrix is $[U]$ and with a quarter turn $\mathbf i_1$ becomes $\mathbf j_0$ and $\mathbf j_1$ becomes $-\mathbf i_0$, as the view shows.

The inverse of a simple rotation is the simple rotation about the same axis by the opposite angle: only the position of the minus sign in front of the sines changes (Notes.pdf, Sec. 1.5.2).

> [!derivation] The inverse simple rotation has the opposite angle
> **Law:** parity of cosine and sine; inverse equals transpose
> **Source:** Notes.pdf, Sec. 1.5.2; Notes.pdf, Eq. 1.18; Notes.pdf, Eq. 1.14
>
> $$\begin{aligned}
> [{}_0R_1(x,-\theta_x)] &= \begin{pmatrix} 1 & 0 & 0 \cr 0 & \cos(-\theta_x) & -\sin(-\theta_x) \cr 0 & \sin(-\theta_x) & \cos(-\theta_x) \end{pmatrix} \quad &\text{(Eq. 1.18 with $-\theta_x$)} \\
> &= \begin{pmatrix} 1 & 0 & 0 \cr 0 & \cos\theta_x & \sin\theta_x \cr 0 & -\sin\theta_x & \cos\theta_x \end{pmatrix} \quad &\text{(cosine is even, sine is odd)} \\
> &= [{}_0R_1(x,\theta_x)]^T \quad &\text{(rows and columns exchanged)} \\
> &= [{}_1R_0(x,\theta_x)] \quad &\text{(Eq. 1.14)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_0(x,\theta_x)] = [{}_0R_1(x,-\theta_x)]}$$
>
> **Units:** dimensionless
> **Meaning:** undoing a rotation means turning back by the same angle about the same axis; the same steps hold for the $y$ and $z$ rotations.

### Sequences of simple rotations

In general none of the vectors of a new basis $\mathcal B_3$ coincides with a vector of $\mathcal B_0$, and their relative orientation may change in time. A general rotation can always be decomposed into three sequential simple rotations; which simple rotations and their order are chosen is not unique (Notes.pdf, Sec. 1.5.3). The notes illustrate it with an $x$ rotation, then a $y$ rotation about the new $\mathbf j_1$, then a $z$ rotation about the new $\mathbf k_2$, through the intermediate bases $\mathcal B_1$ and $\mathcal B_2$.

> [!warning] Wording in Notes.pdf, Sec. 1.5.3
> The notes say that "we can reach $\mathcal B_0$ from $\mathcal B_3$" with the $x$, $y$, $z$ rotations; Eqs. 1.21 and 1.22 define $\mathcal B_1$ as a rotation away from $\mathcal B_0$ and $\mathcal B_3$ as the last one, so the sequence goes from $\mathcal B_0$ to $\mathcal B_3$. The equations are right; only the sentence is reversed.

> [!derivation] Composite matrix of three simple rotations
> **Law:** chaining of changes of basis, Eq. 1.16, through two intermediate bases
> **Source:** Notes.pdf, Eq. 1.21; Notes.pdf, Eq. 1.22; Notes.pdf, Eq. 1.23
>
> $$\begin{aligned}
> [\mathbf A]_0 &= [{}_0R_1(x,\theta_x)]\,[\mathbf A]_1 \quad &\text{($x$ rotation about $\mathbf i_0 \equiv \mathbf i_1$, Eq. 1.21)} \\
> [\mathbf A]_1 &= [{}_1R_2(y,\theta_y)]\,[\mathbf A]_2 \quad &\text{($y$ rotation about $\mathbf j_1 \equiv \mathbf j_2$, Eq. 1.22)} \\
> [\mathbf A]_2 &= [{}_2R_3(z,\theta_z)]\,[\mathbf A]_3 \quad &\text{($z$ rotation about $\mathbf k_2 \equiv \mathbf k_3$, Eq. 1.22)} \\
> [\mathbf A]_0 &= [{}_0R_1(x,\theta_x)]\,[{}_1R_2(y,\theta_y)]\,[{}_2R_3(z,\theta_z)]\,[\mathbf A]_3 \quad &\text{(plug each expression into the former)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_3] = [{}_0R_1(x,\theta_x)]\,[{}_1R_2(y,\theta_y)]\,[{}_2R_3(z,\theta_z)]}$$
>
> **Units:** dimensionless
> **Meaning:** the angles of such a sequence are Euler angles, here of type 1-2-3; another common choice is 3-1-3, a $z$, then an $x$, then a $z$ rotation (Notes.pdf, Sec. 1.5.3; Topic 6 develops them).

The product of Eq. 1.23 is written out below, first the two leftmost factors and then the third, with the short forms $c_x$, $s_x$ for the cosine and sine of $\theta_x$, and likewise for $\theta_y$ and $\theta_z$.

> [!derivation] The 1-2-3 rotation matrix written out
> **Law:** product of matrices, row of the left factor times column of the right factor
> **Source:** Notes.pdf, Eq. 1.23; Notes.pdf, Eq. 1.18; Notes.pdf, Eq. 1.19; Notes.pdf, Eq. 1.20
>
> $$\begin{aligned}
> [{}_0R_1][{}_1R_2] &= \begin{pmatrix} 1 & 0 & 0 \cr 0 & c_x & -s_x \cr 0 & s_x & c_x \end{pmatrix}\begin{pmatrix} c_y & 0 & s_y \cr 0 & 1 & 0 \cr -s_y & 0 & c_y \end{pmatrix} \quad &\text{(Eqs. 1.18 and 1.19)} \\
> &= \begin{pmatrix} 1\cdot c_y + 0\cdot 0 + 0\cdot(-s_y) & 1\cdot 0 + 0\cdot 1 + 0\cdot 0 & 1\cdot s_y + 0\cdot 0 + 0\cdot c_y \cr 0\cdot c_y + c_x\cdot 0 + (-s_x)(-s_y) & 0\cdot 0 + c_x\cdot 1 + (-s_x)\cdot 0 & 0\cdot s_y + c_x\cdot 0 + (-s_x)\,c_y \cr 0\cdot c_y + s_x\cdot 0 + c_x(-s_y) & 0\cdot 0 + s_x\cdot 1 + c_x\cdot 0 & 0\cdot s_y + s_x\cdot 0 + c_x\,c_y \end{pmatrix} \quad &\text{(row $m$ of the left factor times column $n$ of the right factor)} \\
> &= \begin{pmatrix} c_y & 0 & s_y \cr s_x s_y & c_x & -s_x c_y \cr -c_x s_y & s_x & c_x c_y \end{pmatrix} \quad &\text{(drop the zero products)} \\
> [{}_0R_3] &= \begin{pmatrix} c_y & 0 & s_y \cr s_x s_y & c_x & -s_x c_y \cr -c_x s_y & s_x & c_x c_y \end{pmatrix}\begin{pmatrix} c_z & -s_z & 0 \cr s_z & c_z & 0 \cr 0 & 0 & 1 \end{pmatrix} \quad &\text{(right-multiply by Eq. 1.20)} \\
> &= \begin{pmatrix} c_y c_z + 0\cdot s_z + s_y\cdot 0 & -c_y s_z + 0\cdot c_z + s_y\cdot 0 & c_y\cdot 0 + 0\cdot 0 + s_y\cdot 1 \cr s_x s_y c_z + c_x s_z + (-s_x c_y)\cdot 0 & -s_x s_y s_z + c_x c_z + (-s_x c_y)\cdot 0 & s_x s_y\cdot 0 + c_x\cdot 0 + (-s_x c_y)\cdot 1 \cr -c_x s_y c_z + s_x s_z + c_x c_y\cdot 0 & c_x s_y s_z + s_x c_z + c_x c_y\cdot 0 & -c_x s_y\cdot 0 + s_x\cdot 0 + c_x c_y\cdot 1 \end{pmatrix} \quad &\text{(row $m$ times column $n$)} \\
> &= \begin{pmatrix} c_y c_z & -c_y s_z & s_y \cr s_x s_y c_z + c_x s_z & c_x c_z - s_x s_y s_z & -s_x c_y \cr s_x s_z - c_x s_y c_z & s_x c_z + c_x s_y s_z & c_x c_y \end{pmatrix} \quad &\text{(drop the zero products and order the terms)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_3] = \begin{bmatrix} c_y c_z & -c_y s_z & s_y \\ s_x s_y c_z + c_x s_z & c_x c_z - s_x s_y s_z & -s_x c_y \\ s_x s_z - c_x s_y c_z & s_x c_z + c_x s_y s_z & c_x c_y \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** the columns are $\mathbf i_3$, $\mathbf j_3$, $\mathbf k_3$ in $\mathcal B_0$; with $\theta_y$ and $\theta_z$ equal to zero the matrix reduces to the $x$ rotation of Eq. 1.18, as it must.

> [!derivation] The composite matrix is again a rotation matrix
> **Law:** determinant of a product; transpose of a product; one diagonal and one off-diagonal entry written out
> **Source:** Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.23
>
> $$\begin{aligned}
> \det[{}_0R_3] &= \det[{}_0R_1]\,\det[{}_1R_2]\,\det[{}_2R_3] \quad &\text{(the determinant of a product is the product of the determinants)} \\
> &= 1\cdot 1\cdot 1 \quad &\text{(each simple rotation has unit determinant, boxes above)} \\
> &= 1 \quad &\text{(multiply)} \\
> \big([{}_0R_3][{}_0R_3]^T\big)_{11} &= c_y^2c_z^2 + c_y^2s_z^2 + s_y^2 \quad &\text{(row 1 times row 1)} \\
> &= c_y^2\left(c_z^2+s_z^2\right) + s_y^2 \quad &\text{(factor $c_y^2$)} \\
> &= c_y^2 + s_y^2 \quad &\text{(Pythagoras for $\theta_z$)} \\
> &= 1 \quad &\text{(Pythagoras for $\theta_y$)} \\
> \big([{}_0R_3][{}_0R_3]^T\big)_{12} &= c_yc_z\left(s_xs_yc_z + c_xs_z\right) - c_ys_z\left(c_xc_z - s_xs_ys_z\right) - s_y\,s_xc_y \quad &\text{(row 1 times row 2)} \\
> &= s_xs_yc_yc_z^2 + c_xc_yc_zs_z - c_xc_yc_zs_z + s_xs_yc_ys_z^2 - s_xs_yc_y \quad &\text{(expand the products)} \\
> &= s_xs_yc_y\left(c_z^2+s_z^2\right) - s_xs_yc_y \quad &\text{(the $c_x$ terms cancel; factor the rest)} \\
> &= 0 \quad &\text{(Pythagoras for $\theta_z$)}
> \end{aligned}$$
>
> $$\boxed{\det[{}_0R_3] = 1,\qquad [{}_0R_3][{}_0R_3]^T = [U]}$$
>
> **Units:** dimensionless
> **Meaning:** a sequence of rotations is a rotation; the remaining entries follow in the same way, and in general they all follow from the transpose of the product, $[{}_2R_3]^T[{}_1R_2]^T[{}_0R_1]^T$, multiplied against the product itself.

The next example applies the advice of Notes.pdf, Sec. 1.4.1: a direction that lies in no coordinate plane is found with a chain of two simple rotations, one 2D view per rotation.

> [!example] Illustration: a direction given by two successive rotations (not in the notes)
> The basis $\mathcal B_1$ is obtained from $\mathcal B_0$ by a simple rotation of angle $\theta_z$ about $\mathbf k_0$, and $\mathcal B_2$ from $\mathcal B_1$ by a simple rotation of angle $\theta_x$ about the new first vector $\mathbf i_1$. Find the components in $\mathcal B_0$ of the unit vector $\mathbf k_2$, and show that performing the same two simple rotations in the opposite order (first about $\mathbf i_0$, then about the new third vector) does not give the same vector.
>
> | Datum | Meaning |
> | :--- | :--- |
> | $\theta_z$ | angle of the first rotation, about $\mathbf k_0 \equiv \mathbf k_1$ |
> | $\theta_x$ | angle of the second rotation, about $\mathbf i_1 \equiv \mathbf i_2$ |

![[attachments/EM-T/t1-two-rotations.svg]]

> [!derivation] The unit vector k2 in the basis B0
> **Law:** composition of changes of basis; columns of the simple rotation matrices
> **Source:** Notes.pdf, Eq. 1.16; Notes.pdf, Eq. 1.18; Notes.pdf, Eq. 1.20
>
> $$\begin{aligned}
> [\mathbf k_2]_2 &= \begin{pmatrix} 0 \cr 0 \cr 1 \end{pmatrix}_2 \quad &\text{($\mathbf k_2$ in its own basis)} \\
> [\mathbf k_2]_1 &= [{}_1R_2(x,\theta_x)]\,[\mathbf k_2]_2 \quad &\text{(Eq. 1.12 from $\mathcal B_2$ to $\mathcal B_1$)} \\
> &= \begin{pmatrix} 1\cdot 0 + 0\cdot 0 + 0\cdot 1 \cr 0\cdot 0 + c_x\cdot 0 + (-s_x)\cdot 1 \cr 0\cdot 0 + s_x\cdot 0 + c_x\cdot 1 \end{pmatrix}_1 \quad &\text{(rows of Eq. 1.18 times the column)} \\
> &= \begin{pmatrix} 0 \cr -s_x \cr c_x \end{pmatrix}_1 \quad &\text{(third column of Eq. 1.18: $\mathbf k_2 = -s_x\,\mathbf j_1 + c_x\,\mathbf k_1$)} \\
> [\mathbf k_2]_0 &= [{}_0R_1(z,\theta_z)]\,[\mathbf k_2]_1 \quad &\text{(Eq. 1.12 from $\mathcal B_1$ to $\mathcal B_0$)} \\
> &= \begin{pmatrix} c_z\cdot 0 + (-s_z)(-s_x) + 0\cdot c_x \cr s_z\cdot 0 + c_z(-s_x) + 0\cdot c_x \cr 0\cdot 0 + 0\cdot(-s_x) + 1\cdot c_x \end{pmatrix}_0 \quad &\text{(rows of Eq. 1.20 times the column)} \\
> &= \begin{pmatrix} s_z s_x \cr -c_z s_x \cr c_x \end{pmatrix}_0 \quad &\text{(drop the zero products)} \\
> \lVert\mathbf k_2\rVert^2 &= s_z^2s_x^2 + c_z^2s_x^2 + c_x^2 \quad &\text{(sum of the squared components)} \\
> &= s_x^2\left(s_z^2 + c_z^2\right) + c_x^2 \quad &\text{(factor $s_x^2$)} \\
> &= s_x^2 + c_x^2 \quad &\text{(Pythagoras for $\theta_z$)} \\
> &= 1 \quad &\text{(Pythagoras for $\theta_x$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf k_2 = \sin\theta_z\sin\theta_x\,\mathbf i_0 - \cos\theta_z\sin\theta_x\,\mathbf j_0 + \cos\theta_x\,\mathbf k_0}$$
>
> **Units:** dimensionless, as a unit vector must be
> **Meaning:** $\mathbf k_2$ leans away from $\mathbf k_0$ by the angle $\theta_x$, towards $-\mathbf j_1$ (second view), and $\mathbf j_1$ itself is $\mathbf j_0$ turned by $\theta_z$ (first view); with $\theta_x$ equal to zero there is no tilt and $\mathbf k_2$ is $\mathbf k_0$.

> [!derivation] The same rotations in the opposite order
> **Law:** composition of changes of basis; the axis of a simple rotation does not move
> **Source:** Notes.pdf, Eq. 1.17; Notes.pdf, Eq. 1.18
>
> Let $\mathcal B_{1'}$ be $\mathcal B_0$ rotated by $\theta_x$ about $\mathbf i_0$ and $\mathcal B_{2'}$ be $\mathcal B_{1'}$ rotated by $\theta_z$ about $\mathbf k_{1'}$.
>
> $$\begin{aligned}
> \mathbf k_{2'} &= \mathbf k_{1'} \quad &\text{(the second rotation is about $\mathbf k_{1'}$, which does not move)} \\
> [\mathbf k_{1'}]_0 &= \begin{pmatrix} 0 \cr -s_x \cr c_x \end{pmatrix}_0 \quad &\text{(third column of Eq. 1.18)} \\
> [\mathbf k_2]_0 - [\mathbf k_{2'}]_0 &= \begin{pmatrix} s_z s_x \cr -c_z s_x + s_x \cr 0 \end{pmatrix}_0 \quad &\text{(subtract from the previous result)}
> \end{aligned}$$
>
> $$\boxed{\mathbf k_{2'} = -\sin\theta_x\,\mathbf j_0 + \cos\theta_x\,\mathbf k_0 \neq \mathbf k_2\quad\text{unless } \sin\theta_x = 0 \text{ or } \theta_z = 0}$$
>
> **Units:** dimensionless
> **Meaning:** the difference vanishes only when $\sin\theta_x$ is zero (no tilt) or when $\theta_z$ is a whole number of turns (no first turn); finite rotations do not commute, so the order of a sequence must always be stated.

## 4. Vector operations

Besides addition and multiplication by a scalar, mechanics uses the dot (inner, scalar) product, which gives the vector space a Euclidean structure (distances, norms and angles), the cross (vector) product, the triple (mixed) product and the tensor (outer, dyadic) product (Notes.pdf, Sec. 1.6; [Lecture 1, Slide 5]). In this section they are defined without any basis; Section 5 writes them in components.

### Dot product

The dot product of two vectors is a scalar (Notes.pdf, Sec. 1.6.1). With $\theta_{AB}$ the angle between $\mathbf A$ and $\mathbf B$ drawn from a common origin:

| Definition and properties | Equation |
| :--- | :--- |
| $p = \mathbf A\cdot\mathbf B = A\,B\cos\theta_{AB}$ | Eq. 1.24 |
| commutative: $\mathbf A\cdot\mathbf B = \mathbf B\cdot\mathbf A$ | Eq. 1.25 |
| linear: $(\lambda\mathbf A + \mu\mathbf B)\cdot\mathbf C = \lambda\,\mathbf A\cdot\mathbf C + \mu\,\mathbf B\cdot\mathbf C$ | Eq. 1.26 |
| positive-definite: $\mathbf A\cdot\mathbf A \geq 0$, and $\mathbf A\cdot\mathbf A = 0$ only for $\mathbf A = \mathbf 0$ | Eq. 1.27 |
| norm: $\lVert\mathbf v\rVert = \sqrt{\mathbf v\cdot\mathbf v} = v$ | Sec. 1.6.1 |

Since the cosine is even, it makes no difference which vector is taken first when measuring $\theta_{AB}$, which agrees with the commutative property. A zero dot product means that one of the vectors is zero or that they are orthogonal (perpendicular, zero cosine) (Notes.pdf, Sec. 1.6.1; [Lecture 1, Slide 5]).

![[attachments/EM-T/t1-dot-product.svg]]

> [!derivation] Projection on a unit vector, and the components as projections
> **Law:** definition of the dot product with a unit vector; linearity; orthonormality of the basis
> **Source:** Notes.pdf, Eq. 1.24; Notes.pdf, Eq. 1.26; Notes.pdf, Eq. 1.28
>
> $$\begin{aligned}
> \mathbf A\cdot\mathbf e_B &= A\cdot 1\cdot\cos\theta_{AB} \quad &\text{(Eq. 1.24 with $\lVert\mathbf e_B\rVert = 1$)} \\
> &= A\cos\theta_{AB} \quad &\text{(the leg of the right triangle of hypotenuse $A$ adjacent to $\theta_{AB}$: the projection of $\mathbf A$ on the line of $\mathbf e_B$)} \\
> \mathbf A\cdot\mathbf i &= \left(A_x\mathbf i + A_y\mathbf j + A_z\mathbf k\right)\cdot\mathbf i \quad &\text{(components of $\mathbf A$, Eq. 1.2)} \\
> &= A_x\,\mathbf i\cdot\mathbf i + A_y\,\mathbf j\cdot\mathbf i + A_z\,\mathbf k\cdot\mathbf i \quad &\text{(linearity, Eq. 1.26)} \\
> &= A_x\cdot 1 + A_y\cdot 0 + A_z\cdot 0 \quad &\text{($\cos 0 = 1$ for $\mathbf i$ with itself, $\cos\frac{\pi}{2} = 0$ for the other two)} \\
> &= A_x \quad &\text{(simplify; likewise with $\mathbf j$ and $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf A\cdot\mathbf e_B = A\cos\theta_{AB},\qquad A_x = \mathbf A\cdot\mathbf i,\quad A_y = \mathbf A\cdot\mathbf j,\quad A_z = \mathbf A\cdot\mathbf k}$$
>
> **Units:** $[\mathbf A]\cdot[1]$: a projection carries the units of the projected vector
> **Meaning:** the dot product with a unit vector is the projection on its direction, and the components of a vector in an orthonormal basis are its projections on the basis vectors (the notes add that, strictly, these are the covariant components, which coincide with the contravariant ones in an orthonormal basis).

When a unit vector $\mathbf e$ is projected on the three vectors of $\mathcal B_0$, the dot products are its direction cosines; the direction angles $\alpha$, $\beta$, $\gamma$ with $\mathbf i$, $\mathbf j$, $\mathbf k$ are taken between zero and $\pi$ to avoid ambiguity (Notes.pdf, Sec. 1.6.1, Fig. 1.4).

![[attachments/EM-T/t1-direction-angles.svg]]

> [!derivation] Direction cosines and the entries of the rotation matrix
> **Law:** components as projections; dot product of two unit vectors
> **Source:** Notes.pdf, Eq. 1.29; Notes.pdf, Eq. 1.28; Notes.pdf, Eq. 1.7
>
> $$\begin{aligned}
> \mathbf e &= (\mathbf e\cdot\mathbf i)\,\mathbf i + (\mathbf e\cdot\mathbf j)\,\mathbf j + (\mathbf e\cdot\mathbf k)\,\mathbf k \quad &\text{(Eq. 1.28 applied to $\mathbf e$)} \\
> \mathbf e\cdot\mathbf i &= 1\cdot 1\cdot\cos\alpha \quad &\text{(Eq. 1.24; both vectors are unit vectors, $\alpha$ is the angle between them)} \\
> \mathbf e &= \cos\alpha\,\mathbf i + \cos\beta\,\mathbf j + \cos\gamma\,\mathbf k \quad &\text{(same step with $\mathbf j$ and $\mathbf k$)} \\
> \mathbf i_1\cdot\mathbf i_0 &= \ell_{x1,x0}\,\mathbf i_0\cdot\mathbf i_0 + \ell_{x1,y0}\,\mathbf j_0\cdot\mathbf i_0 + \ell_{x1,z0}\,\mathbf k_0\cdot\mathbf i_0 \quad &\text{(dot-multiply Eq. 1.7 by $\mathbf i_0$; linearity)} \\
> &= \ell_{x1,x0} \quad &\text{(orthonormality of $\mathcal B_0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e = \cos\alpha\,\mathbf i + \cos\beta\,\mathbf j + \cos\gamma\,\mathbf k,\qquad \ell_{x1,x0} = \mathbf i_1\cdot\mathbf i_0}$$
>
> **Units:** dimensionless
> **Meaning:** every entry of $[{}_0R_1]$ is a direction cosine, the cosine of the angle between one new and one old unit vector; for the $z$ rotation of Section 3, $\mathbf i_1\cdot\mathbf i_0$ is $\cos\theta_z$, the entry $(1,1)$ of Eq. 1.20.

The dot is also used for the contraction of a vector with a tensor: $\mathbf A\cdot\bar{\bar M}$ is a vector, the operation is not commutative, and it only makes sense when the dimensions of the vector and the tensor match (Notes.pdf, Sec. 1.6.1).

### Cross product

In $\mathbb R^3$ the cross (vector) product of $\mathbf A$ and $\mathbf B$ is a vector $\mathbf C$, orthogonal to both factors (normal to their plane), with the sense given by the right-hand rule, and with the magnitude and properties below (Notes.pdf, Sec. 1.6.2, Fig. 1.5):

| Definition and properties | Equation |
| :--- | :--- |
| $C = A\,B\,\lvert\sin\theta_{AB}\rvert$ | Eq. 1.30 |
| anticommutative: $\mathbf A\times\mathbf B = -\mathbf B\times\mathbf A$ | Eq. 1.31 |
| linear: $(\lambda\mathbf A + \mu\mathbf B)\times\mathbf C = \lambda\,\mathbf A\times\mathbf C + \mu\,\mathbf B\times\mathbf C$ | Eq. 1.32 |
| non-associative: in general $\mathbf A\times(\mathbf B\times\mathbf C) \neq (\mathbf A\times\mathbf B)\times\mathbf C$ | Sec. 1.6.2 |

![[attachments/EM-T/t1-cross-product.svg]]

> [!derivation] The magnitude of the cross product is the area of the parallelogram
> **Law:** area of a parallelogram as base times height; right triangle on the side $\mathbf B$
> **Source:** Notes.pdf, Eq. 1.30; Notes.pdf Fig. 1.5
>
> The parallelogram has the sides $\mathbf A$ and $\mathbf B$ drawn from a common origin. Its height over the base $\mathbf A$ is the opposite leg, relative to $\theta_{AB}$, of the right triangle whose hypotenuse is the side $\mathbf B$.
>
> $$\begin{aligned}
> \text{area} &= \text{base}\cdot\text{height} \quad &\text{(area of a parallelogram)} \\
> \text{height} &= B\,\lvert\sin\theta_{AB}\rvert \quad &\text{(opposite leg over hypotenuse $B$; the absolute value keeps the height positive)} \\
> \text{area} &= A\,B\,\lvert\sin\theta_{AB}\rvert \quad &\text{(base $A$)} \\
> &= C \quad &\text{(Eq. 1.30)}
> \end{aligned}$$
>
> $$\boxed{\lVert\mathbf A\times\mathbf B\rVert = A\,B\,\lvert\sin\theta_{AB}\rvert = \text{area of the parallelogram of } \mathbf A \text{ and } \mathbf B}$$
>
> **Units:** $[\mathbf A][\mathbf B]$: for two lengths, an area $[\mathrm{L^2}]$
> **Meaning:** the cross product is largest for perpendicular factors and vanishes for collinear ones, whose parallelogram has no area.

> [!derivation] The cross product of a vector with itself vanishes
> **Law:** anticommutativity
> **Source:** Notes.pdf, Eq. 1.31; Notes.pdf, Sec. 1.6.2
>
> $$\begin{aligned}
> \mathbf A\times\mathbf A &= -\mathbf A\times\mathbf A \quad &\text{(Eq. 1.31 with $\mathbf B = \mathbf A$)} \\
> 2\,\mathbf A\times\mathbf A &= \mathbf 0 \quad &\text{(add $\mathbf A\times\mathbf A$ to both sides)} \\
> \mathbf A\times\mathbf A &= \mathbf 0 \quad &\text{(divide by two)}
> \end{aligned}$$
>
> $$\boxed{\mathbf A\times\mathbf A = \mathbf 0}$$
>
> **Units:** $[\mathbf A]^2$
> **Meaning:** the same follows from Eq. 1.30 with a zero angle; more generally a zero cross product means that a factor is zero or that the factors are collinear (parallel or antiparallel).

### Perpendicular and parallel vectors

The two products give the conditions that are imposed again and again in mechanics (Notes.pdf, Sec. 1.6.3; [Lecture 1, Slide 5]):

| Condition | Imposed by |
| :--- | :--- |
| $\mathbf A$ and $\mathbf B$ perpendicular | $\mathbf A\cdot\mathbf B = 0$ |
| $\mathbf A$ and $\mathbf B$ collinear (parallel or antiparallel) | $\mathbf A\times\mathbf B = \mathbf 0$ |

### Triple product

The triple product of $\mathbf A$, $\mathbf B$, $\mathbf C$ is the scalar $[\mathbf A,\mathbf B,\mathbf C]$, the dot product of $\mathbf A$ with the cross product of $\mathbf B$ and $\mathbf C$. It is the volume of the parallelepiped of the three vectors when they are given in right-hand-rule order, and minus that volume otherwise; it is unchanged by a cyclic permutation of the factors (Eq. 1.33, proved in components in Section 5) (Notes.pdf, Sec. 1.6.4, Fig. 1.6).

![[attachments/EM-T/t1-triple-product.svg]]

> [!derivation] The triple product is the volume of the parallelepiped
> **Law:** volume as base area times height; dot product with the unit normal of the base
> **Source:** Notes.pdf, Eq. 1.33; Notes.pdf Fig. 1.6; Notes.pdf, Eq. 1.30
>
> The base is the parallelogram of $\mathbf A$ and $\mathbf B$, of area $\lVert\mathbf A\times\mathbf B\rVert$ and unit normal $\mathbf n$ along $\mathbf A\times\mathbf B$. The height is the leg along $\mathbf n$ of the right triangle whose hypotenuse is $\mathbf C$; call $\varphi_C$ the angle between $\mathbf C$ and $\mathbf n$.
>
> $$\begin{aligned}
> \mathbf C\cdot(\mathbf A\times\mathbf B) &= \lVert\mathbf A\times\mathbf B\rVert\;C\cos\varphi_C \quad &\text{(Eq. 1.24)} \\
> C\cos\varphi_C &= \pm\,\text{height} \quad &\text{(leg adjacent to $\varphi_C$; positive when $\mathbf C$ is on the side of $\mathbf n$)} \\
> \mathbf C\cdot(\mathbf A\times\mathbf B) &= \pm\,\text{base}\cdot\text{height} \quad &\text{(the base area is $\lVert\mathbf A\times\mathbf B\rVert$, Eq. 1.30)}
> \end{aligned}$$
>
> $$\boxed{[\mathbf A,\mathbf B,\mathbf C] = \mathbf A\cdot(\mathbf B\times\mathbf C) = \mathbf C\cdot(\mathbf A\times\mathbf B) = \pm\,\text{volume}}$$
>
> **Units:** $[\mathbf A][\mathbf B][\mathbf C]$: for three lengths, a volume $[\mathrm{L^3}]$
> **Meaning:** the sign is $+$ when $\mathbf A$, $\mathbf B$, $\mathbf C$ follow the right-hand rule ($\mathbf C$ on the side of $\mathbf A\times\mathbf B$); the triple product vanishes when the three vectors are coplanar, because the box is flat.

### Tensor product

The tensor (outer, dyadic) product of two vectors is a second-order tensor, or dyadic, $\mathbf A\otimes\mathbf B$ (Notes.pdf, Sec. 1.6.5). The dot product returns an object one order lower than its inputs; the outer product returns one order higher.

| Property | Equation |
| :--- | :--- |
| bilinear in the first factor: $(\lambda\mathbf A + \mu\mathbf B)\otimes\mathbf C = \lambda\,\mathbf A\otimes\mathbf C + \mu\,\mathbf B\otimes\mathbf C$ | Eq. 1.34 |
| bilinear in the second factor: $\mathbf A\otimes(\lambda\mathbf B + \mu\mathbf C) = \lambda\,\mathbf A\otimes\mathbf B + \mu\,\mathbf A\otimes\mathbf C$ | Eq. 1.35 |
| not commutative: $\mathbf A\otimes\mathbf B \neq \mathbf B\otimes\mathbf A$ | Sec. 1.6.5 |
| contraction with a vector: $\mathbf A\cdot(\mathbf B\otimes\mathbf C) = (\mathbf A\cdot\mathbf B)\,\mathbf C$ and $(\mathbf A\otimes\mathbf B)\cdot\mathbf C = \mathbf A\,(\mathbf B\cdot\mathbf C)$ | Eq. 1.36 (proved in Section 5) |
| rank of $\mathbf A\otimes\mathbf B$: two for non-zero, non-collinear factors; one for non-zero collinear factors; zero if a factor is zero | Sec. 1.6.5 |

### Useful vector relations

Two identities are used throughout the course (Notes.pdf, Sec. 1.6.6); both are proved in components in Section 5.

| Identity | Equation |
| :--- | :--- |
| double vector product: $\mathbf A\times(\mathbf B\times\mathbf C) = (\mathbf A\cdot\mathbf C)\,\mathbf B - (\mathbf A\cdot\mathbf B)\,\mathbf C$ | Eq. 1.37 |
| $(\mathbf A\times\mathbf B)\cdot(\mathbf C\times\mathbf D) = (\mathbf A\cdot\mathbf C)(\mathbf B\cdot\mathbf D) - (\mathbf A\cdot\mathbf D)(\mathbf B\cdot\mathbf C)$ | Eq. 1.38 |

## 5. Operations in component form and the moment of a vector

Every operation of Section 4 was defined without a basis, which is why vector equations express physical laws: these cannot depend on the basis used to study them. To compute, or to measure a direction, a basis is introduced and the operations are written in components (Notes.pdf, Sec. 1.6.7). A vector equation is three scalar equations: two vectors are equal when their projections on the three axes are equal.

> [!warning] One basis at a time
> Vector (and tensor) operations can only be carried out in components once all the participating vectors are written in the same basis; vector-tensor and tensor-tensor operations need consistent bases (Notes.pdf, Sec. 1.6.7). Change the basis of a vector with $[{}_0R_1]$ first, then operate.

> [!derivation] Linear combination in components
> **Law:** components in a basis; distributivity of the multiplication by a scalar
> **Source:** Notes.pdf, Eq. 1.39; Notes.pdf, Eq. 1.2
>
> $$\begin{aligned}
> \mathbf C &= \lambda\left(A_x\mathbf i + A_y\mathbf j + A_z\mathbf k\right) + \mu\left(B_x\mathbf i + B_y\mathbf j + B_z\mathbf k\right) \quad &\text{(write $\lambda\mathbf A + \mu\mathbf B$ in components)} \\
> &= \lambda A_x\mathbf i + \lambda A_y\mathbf j + \lambda A_z\mathbf k + \mu B_x\mathbf i + \mu B_y\mathbf j + \mu B_z\mathbf k \quad &\text{(distribute the scalars, Sec. 1.3)} \\
> &= (\lambda A_x + \mu B_x)\,\mathbf i + (\lambda A_y + \mu B_y)\,\mathbf j + (\lambda A_z + \mu B_z)\,\mathbf k \quad &\text{(collect the coefficient of each unit vector)}
> \end{aligned}$$
>
> $$\boxed{C_x = \lambda A_x + \mu B_x,\qquad C_y = \lambda A_y + \mu B_y,\qquad C_z = \lambda A_z + \mu B_z}$$
>
> **Units:** each term carries the units of $\mathbf C$
> **Meaning:** addition, subtraction and multiplication by a scalar act component by component.

### Dot and cross products in components

> [!derivation] Dot product in components
> **Law:** linearity and commutativity of the dot product; orthonormality of the basis
> **Source:** Notes.pdf, Eq. 1.40; Notes.pdf, Eq. 1.41; Notes.pdf, Eq. 1.26
>
> $$\begin{aligned}
> \mathbf A\cdot\mathbf B &= \left(A_x\mathbf i + A_y\mathbf j + A_z\mathbf k\right)\cdot\left(B_x\mathbf i + B_y\mathbf j + B_z\mathbf k\right) \quad &\text{(components of both vectors in $\mathcal B_0$)} \\
> &= A_xB_x\,\mathbf i\cdot\mathbf i + A_xB_y\,\mathbf i\cdot\mathbf j + A_xB_z\,\mathbf i\cdot\mathbf k + A_yB_x\,\mathbf j\cdot\mathbf i + A_yB_y\,\mathbf j\cdot\mathbf j + A_yB_z\,\mathbf j\cdot\mathbf k + A_zB_x\,\mathbf k\cdot\mathbf i + A_zB_y\,\mathbf k\cdot\mathbf j + A_zB_z\,\mathbf k\cdot\mathbf k \quad &\text{(distribute: Eqs. 1.25 and 1.26)} \\
> &= A_xB_x\cdot 1 + A_xB_y\cdot 0 + A_xB_z\cdot 0 + A_yB_x\cdot 0 + A_yB_y\cdot 1 + A_yB_z\cdot 0 + A_zB_x\cdot 0 + A_zB_y\cdot 0 + A_zB_z\cdot 1 \quad &\text{($\mathbf i\cdot\mathbf i = \mathbf j\cdot\mathbf j = \mathbf k\cdot\mathbf k = 1$; the mixed products vanish)} \\
> &= A_xB_x + A_yB_y + A_zB_z \quad &\text{(drop the zero terms)} \\
> &= \begin{bmatrix} A_x & A_y & A_z \end{bmatrix}_0\begin{bmatrix} B_x \cr B_y \cr B_z \end{bmatrix}_0 \quad &\text{(row times column)}
> \end{aligned}$$
>
> $$\boxed{\mathbf A\cdot\mathbf B = A_xB_x + A_yB_y + A_zB_z = [\mathbf A]_0^T\,[\mathbf B]_0}$$
>
> **Units:** $[\mathbf A][\mathbf B]$ in every term
> **Meaning:** in a matrix context the notation $\mathbf A\cdot\mathbf B$ is shorthand for the row of $\mathbf A$ times the column of $\mathbf B$; in a vector context the transpose can be dropped.

> [!derivation] Cross products of the basis vectors
> **Law:** magnitude, direction and sense of the cross product; right-handed basis; anticommutativity
> **Source:** Notes.pdf, Eq. 1.42; Notes.pdf, Eq. 1.30; Notes.pdf, Eq. 1.31
>
> $$\begin{aligned}
> \mathbf i\times\mathbf i &= \mathbf j\times\mathbf j = \mathbf k\times\mathbf k = \mathbf 0 \quad &\text{(a vector with itself, Sec. 4)} \\
> \lVert\mathbf i\times\mathbf j\rVert &= 1\cdot 1\cdot\left|\sin\frac{\pi}{2}\right| \quad &\text{(Eq. 1.30 for two perpendicular unit vectors)} \\
> &= 1 \quad &\text{(the product is a unit vector)} \\
> \mathbf i\times\mathbf j &= \mathbf k \quad &\text{(normal to $\mathbf i$ and $\mathbf j$, sense of the right-hand rule: the basis is right-handed)} \\
> \mathbf j\times\mathbf k &= \mathbf i,\quad \mathbf k\times\mathbf i = \mathbf j \quad &\text{(same argument for the pairs in the cyclic order $\mathbf j, \mathbf k, \mathbf i$)} \\
> \mathbf j\times\mathbf i &= -\mathbf k,\quad \mathbf k\times\mathbf j = -\mathbf i,\quad \mathbf i\times\mathbf k = -\mathbf j \quad &\text{(anticommutativity, Eq. 1.31)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i\times\mathbf j = \mathbf k,\quad \mathbf j\times\mathbf k = \mathbf i,\quad \mathbf k\times\mathbf i = \mathbf j,\qquad \text{reversed order: minus sign}}$$
>
> **Units:** dimensionless
> **Meaning:** in the cyclic order $\mathbf i \to \mathbf j \to \mathbf k \to \mathbf i$ the product of two consecutive vectors is the third; against the cycle it is minus the third.

> [!derivation] Cross product in components
> **Law:** linearity of the cross product in both factors; cross products of the basis vectors
> **Source:** Notes.pdf, Eq. 1.42; Notes.pdf, Eq. 1.32
>
> $$\begin{aligned}
> \mathbf A\times\mathbf B &= \left(A_x\mathbf i + A_y\mathbf j + A_z\mathbf k\right)\times\left(B_x\mathbf i + B_y\mathbf j + B_z\mathbf k\right) \quad &\text{(components of both vectors in $\mathcal B_0$)} \\
> &= A_xB_x\,\mathbf i\times\mathbf i + A_xB_y\,\mathbf i\times\mathbf j + A_xB_z\,\mathbf i\times\mathbf k + A_yB_x\,\mathbf j\times\mathbf i + A_yB_y\,\mathbf j\times\mathbf j + A_yB_z\,\mathbf j\times\mathbf k + A_zB_x\,\mathbf k\times\mathbf i + A_zB_y\,\mathbf k\times\mathbf j + A_zB_z\,\mathbf k\times\mathbf k \quad &\text{(distribute: Eq. 1.32, and Eq. 1.31 for the second factor)} \\
> &= \mathbf 0 + A_xB_y\,\mathbf k - A_xB_z\,\mathbf j - A_yB_x\,\mathbf k + \mathbf 0 + A_yB_z\,\mathbf i + A_zB_x\,\mathbf j - A_zB_y\,\mathbf i + \mathbf 0 \quad &\text{(products of the basis vectors, box above)} \\
> &= (A_yB_z - A_zB_y)\,\mathbf i + (A_zB_x - A_xB_z)\,\mathbf j + (A_xB_y - A_yB_x)\,\mathbf k \quad &\text{(collect the coefficient of each unit vector)} \\
> &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr A_x & A_y & A_z \cr B_x & B_y & B_z \end{vmatrix} \quad &\text{(expanding the determinant along its first row, with signs $+,-,+$, gives the same three terms)}
> \end{aligned}$$
>
> $$\boxed{\mathbf A\times\mathbf B = (A_yB_z - A_zB_y)\,\mathbf i + (A_zB_x - A_xB_z)\,\mathbf j + (A_xB_y - A_yB_x)\,\mathbf k = \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \\ A_x & A_y & A_z \\ B_x & B_y & B_z \end{vmatrix}}$$
>
> **Units:** $[\mathbf A][\mathbf B]$ in every term
> **Meaning:** each component of the product involves only the other two components of the factors; for two vectors in the plane $Oxy$ only the $\mathbf k$ component survives, normal to the plane, as the right-hand rule requires.

> [!warning] Typos in Notes.pdf, Sec. 1.6.7
> The sentence before Eq. 1.42 says "we can express the tensor product as a determinant": it is the vector (cross) product. In Eq. 1.44 the last component of $\mathbf B$ is printed in lower case; it is $B_z$, as in Eqs. 1.45 to 1.47. Neither typo affects the equations.

### Triple product in components

> [!derivation] Triple product as a determinant
> **Law:** cross product and dot product in components; expansion of a determinant along its first row
> **Source:** Notes.pdf, Eq. 1.43; Notes.pdf, Eq. 1.42; Notes.pdf, Eq. 1.40
>
> $$\begin{aligned}
> \mathbf B\times\mathbf C &= (B_yC_z - B_zC_y)\,\mathbf i + (B_zC_x - B_xC_z)\,\mathbf j + (B_xC_y - B_yC_x)\,\mathbf k \quad &\text{(Eq. 1.42)} \\
> \mathbf A\cdot(\mathbf B\times\mathbf C) &= A_x(B_yC_z - B_zC_y) + A_y(B_zC_x - B_xC_z) + A_z(B_xC_y - B_yC_x) \quad &\text{(Eq. 1.40)} \\
> \begin{vmatrix} A_x & A_y & A_z \cr B_x & B_y & B_z \cr C_x & C_y & C_z \end{vmatrix} &= A_x(B_yC_z - B_zC_y) - A_y(B_xC_z - B_zC_x) + A_z(B_xC_y - B_yC_x) \quad &\text{(expand along the first row)} \\
> -A_y(B_xC_z - B_zC_x) &= A_y(B_zC_x - B_xC_z) \quad &\text{(the middle terms of both lines agree)}
> \end{aligned}$$
>
> $$\boxed{\mathbf A\cdot(\mathbf B\times\mathbf C) = \begin{vmatrix} A_x & A_y & A_z \\ B_x & B_y & B_z \\ C_x & C_y & C_z \end{vmatrix}}$$
>
> **Units:** $[\mathbf A][\mathbf B][\mathbf C]$
> **Meaning:** the determinant vanishes whenever the three vectors are linearly dependent: they are then coplanar and the parallelepiped has zero volume.

> [!derivation] Cyclic permutation of the triple product
> **Law:** exchanging two rows of a determinant changes its sign
> **Source:** Notes.pdf, Eq. 1.33; Notes.pdf, Eq. 1.43
>
> $$\begin{aligned}
> \mathbf C\cdot(\mathbf A\times\mathbf B) &= \begin{vmatrix} C_x & C_y & C_z \cr A_x & A_y & A_z \cr B_x & B_y & B_z \end{vmatrix} \quad &\text{(Eq. 1.43 with the factors $\mathbf C$, $\mathbf A$, $\mathbf B$)} \\
> &= -\begin{vmatrix} A_x & A_y & A_z \cr C_x & C_y & C_z \cr B_x & B_y & B_z \end{vmatrix} \quad &\text{(exchange rows 1 and 2)} \\
> &= \begin{vmatrix} A_x & A_y & A_z \cr B_x & B_y & B_z \cr C_x & C_y & C_z \end{vmatrix} \quad &\text{(exchange rows 2 and 3: a second minus sign)} \\
> &= \mathbf A\cdot(\mathbf B\times\mathbf C) \quad &\text{(Eq. 1.43)} \\
> \mathbf B\cdot(\mathbf C\times\mathbf A) &= \mathbf A\cdot(\mathbf B\times\mathbf C) \quad &\text{(same two exchanges: rows 1 and 3, then rows 2 and 3)}
> \end{aligned}$$
>
> $$\boxed{[\mathbf A,\mathbf B,\mathbf C] = \mathbf A\cdot(\mathbf B\times\mathbf C) = \mathbf C\cdot(\mathbf A\times\mathbf B) = \mathbf B\cdot(\mathbf C\times\mathbf A)}$$
>
> **Units:** $[\mathbf A][\mathbf B][\mathbf C]$
> **Meaning:** a cyclic permutation keeps the right-hand order of the three edges, hence the same signed volume; swapping two factors reverses the order and changes the sign.

### The properties of the rotation matrix, proved

With the dot and triple products in components, the properties of $[{}_0R_1]$ stated in Section 3 follow from the orthonormality and handedness of $\mathcal B_1$. Call $\mathbf u_1$, $\mathbf u_2$, $\mathbf u_3$ the vectors $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$, so that column $n$ of $[{}_0R_1]$ is $[\mathbf u_n]_0$.

> [!derivation] The rotation matrix is orthogonal
> **Law:** orthonormality of $\mathcal B_1$; dot product in components; the inverse undoes the change of basis
> **Source:** Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.40; Notes.pdf, Eq. 1.12
>
> $$\begin{aligned}
> \big([{}_0R_1]^T[{}_0R_1]\big)_{mn} &= [\mathbf u_m]_0^T\,[\mathbf u_n]_0 \quad &\text{(row $m$ of the transpose is column $m$ of the matrix)} \\
> &= \mathbf u_m\cdot\mathbf u_n \quad &\text{(dot product in components, Eq. 1.41)} \\
> &= \begin{cases} 1, & m = n \cr 0, & m \neq n \end{cases} \quad &\text{($\mathcal B_1$ is orthonormal)} \\
> [\mathbf A]_0 &= [{}_0R_1]\,[{}_1R_0]\,[\mathbf A]_0 \quad &\text{(go from $\mathcal B_0$ to $\mathcal B_1$ and back, Eq. 1.12 twice; true for every $\mathbf A$)} \\
> [{}_0R_1]\,[{}_1R_0] &= [U] \quad &\text{(so $[{}_1R_0]$ is the inverse of $[{}_0R_1]$)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_0] = [{}_0R_1]^{-1} = [{}_0R_1]^T,\qquad [{}_0R_1]^T[{}_0R_1] = [U]}$$
>
> **Units:** dimensionless
> **Meaning:** inverting a change of basis costs a transposition; since the columns of $[{}_1R_0]$ are $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$ in $\mathcal B_1$, these are the rows of $[{}_0R_1]$.

> [!derivation] The determinant of the rotation matrix is one
> **Law:** determinant of the transpose; triple product as a determinant; right-handed basis
> **Source:** Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.43
>
> $$\begin{aligned}
> \lvert[{}_0R_1]\rvert &= \lvert[{}_0R_1]^T\rvert \quad &\text{(a matrix and its transpose have the same determinant)} \\
> &= \mathbf u_1\cdot(\mathbf u_2\times\mathbf u_3) \quad &\text{(the rows of the transpose are $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$; Eq. 1.43)} \\
> &= \mathbf i_1\cdot\mathbf i_1 \quad &\text{($\mathbf j_1\times\mathbf k_1 = \mathbf i_1$: $\mathcal B_1$ is right-handed)} \\
> &= 1 \quad &\text{($\mathbf i_1$ is a unit vector)}
> \end{aligned}$$
>
> $$\boxed{\lvert[{}_0R_1]\rvert = 1}$$
>
> **Units:** dimensionless
> **Meaning:** a change between two right-handed bases has determinant plus one; a left-handed $\mathcal B_1$ would give minus one, which is why the course uses only right-handed bases.

### Tensor product in components

> [!derivation] Tensor product in components
> **Law:** bilinearity of the tensor product; tensor basis built from $\mathcal B_0$
> **Source:** Notes.pdf, Eq. 1.44; Notes.pdf, Eq. 1.47; Notes.pdf, Eq. 1.48
>
> $$\begin{aligned}
> \mathbf A\otimes\mathbf B &= \left(A_x\mathbf i + A_y\mathbf j + A_z\mathbf k\right)\otimes\left(B_x\mathbf i + B_y\mathbf j + B_z\mathbf k\right) \quad &\text{(components of both vectors, Eq. 1.44)} \\
> &= A_xB_x\,\mathbf i\otimes\mathbf i + A_xB_y\,\mathbf i\otimes\mathbf j + A_xB_z\,\mathbf i\otimes\mathbf k + A_yB_x\,\mathbf j\otimes\mathbf i + A_yB_y\,\mathbf j\otimes\mathbf j + A_yB_z\,\mathbf j\otimes\mathbf k + A_zB_x\,\mathbf k\otimes\mathbf i + A_zB_y\,\mathbf k\otimes\mathbf j + A_zB_z\,\mathbf k\otimes\mathbf k \quad &\text{(bilinearity, Eqs. 1.34 and 1.35; Eqs. 1.45 to 1.47)} \\
> &= \begin{bmatrix} A_xB_x & A_xB_y & A_xB_z \cr A_yB_x & A_yB_y & A_yB_z \cr A_zB_x & A_zB_y & A_zB_z \end{bmatrix}_{00} \quad &\text{(the nine coefficients in the basis $\mathcal B_0\otimes\mathcal B_0$; row: first factor, column: second factor)} \\
> &= [\mathbf A]_0\,[\mathbf B]_0^T \quad &\text{(column of $\mathbf A$ times row of $\mathbf B$: entry $(m,n)$ is $A_mB_n$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf A\otimes\mathbf B = \begin{bmatrix} A_xB_x & A_xB_y & A_xB_z \\ A_yB_x & A_yB_y & A_yB_z \\ A_zB_x & A_zB_y & A_zB_z \end{bmatrix}_{00}}$$
>
> **Units:** $[\mathbf A][\mathbf B]$ in every entry
> **Meaning:** the subindices $00$ say in which bases the tensor is written; exchanging the factors transposes the matrix, so the tensor product is not commutative.

> [!derivation] Contraction of a tensor product with a vector
> **Law:** contraction in components as a product of a row, or a column, with the matrix of the tensor
> **Source:** Notes.pdf, Eq. 1.36; Notes.pdf, Eq. 1.48; Notes.pdf, Eq. 1.40
>
> $$\begin{aligned}
> \big(\mathbf A\cdot(\mathbf B\otimes\mathbf C)\big)_n &= A_x\,B_xC_n + A_y\,B_yC_n + A_z\,B_zC_n \quad &\text{(row of $\mathbf A$ times column $n$ of Eq. 1.48 with $\mathbf B$, $\mathbf C$)} \\
> &= \left(A_xB_x + A_yB_y + A_zB_z\right)C_n \quad &\text{(factor $C_n$, common to the three terms)} \\
> &= (\mathbf A\cdot\mathbf B)\,C_n \quad &\text{(Eq. 1.40)} \\
> \big((\mathbf A\otimes\mathbf B)\cdot\mathbf C\big)_m &= A_mB_xC_x + A_mB_yC_y + A_mB_zC_z \quad &\text{(row $m$ of Eq. 1.48 times the column of $\mathbf C$)} \\
> &= A_m\,(\mathbf B\cdot\mathbf C) \quad &\text{(factor $A_m$; Eq. 1.40)}
> \end{aligned}$$
>
> $$\boxed{\mathbf A\cdot(\mathbf B\otimes\mathbf C) = (\mathbf A\cdot\mathbf B)\,\mathbf C,\qquad (\mathbf A\otimes\mathbf B)\cdot\mathbf C = \mathbf A\,(\mathbf B\cdot\mathbf C)}$$
>
> **Units:** $[\mathbf A][\mathbf B][\mathbf C]$ on both sides
> **Meaning:** a vector dotted from the left contracts with the first factor of the dyadic and from the right with the second, so the two contractions differ in general.

### The useful relations, proved

> [!derivation] Double vector product
> **Law:** cross product in components, applied twice; add and subtract one term
> **Source:** Notes.pdf, Eq. 1.37; Notes.pdf, Eq. 1.42; Notes.pdf, Eq. 1.40
>
> $$\begin{aligned}
> \big(\mathbf A\times(\mathbf B\times\mathbf C)\big)_x &= A_y\,(\mathbf B\times\mathbf C)_z - A_z\,(\mathbf B\times\mathbf C)_y \quad &\text{($x$ component of Eq. 1.42 with the second factor $\mathbf B\times\mathbf C$)} \\
> &= A_y\left(B_xC_y - B_yC_x\right) - A_z\left(B_zC_x - B_xC_z\right) \quad &\text{(components of $\mathbf B\times\mathbf C$, Eq. 1.42)} \\
> &= A_yB_xC_y - A_yB_yC_x - A_zB_zC_x + A_zB_xC_z \quad &\text{(expand)} \\
> &= B_x\left(A_yC_y + A_zC_z\right) - C_x\left(A_yB_y + A_zB_z\right) \quad &\text{(group the terms with $B_x$ and with $C_x$)} \\
> &= B_x\left(A_xC_x + A_yC_y + A_zC_z\right) - C_x\left(A_xB_x + A_yB_y + A_zB_z\right) \quad &\text{(add and subtract $A_xB_xC_x$)} \\
> &= (\mathbf A\cdot\mathbf C)\,B_x - (\mathbf A\cdot\mathbf B)\,C_x \quad &\text{(Eq. 1.40)}
> \end{aligned}$$
>
> $$\boxed{\mathbf A\times(\mathbf B\times\mathbf C) = (\mathbf A\cdot\mathbf C)\,\mathbf B - (\mathbf A\cdot\mathbf B)\,\mathbf C}$$
>
> **Units:** $[\mathbf A][\mathbf B][\mathbf C]$ in every term
> **Meaning:** the $y$ and $z$ components follow by the cyclic relabelling $x \to y \to z \to x$, which leaves Eq. 1.42 unchanged; the double product lies in the plane of $\mathbf B$ and $\mathbf C$, and it is not associative.

> [!derivation] Dot product of two cross products
> **Law:** cyclic permutation of the triple product; double vector product; linearity
> **Source:** Notes.pdf, Eq. 1.38; Notes.pdf, Eq. 1.33; Notes.pdf, Eq. 1.37
>
> Call $\mathbf E$ the cross product of $\mathbf A$ and $\mathbf B$.
>
> $$\begin{aligned}
> (\mathbf A\times\mathbf B)\cdot(\mathbf C\times\mathbf D) &= \mathbf E\cdot(\mathbf C\times\mathbf D) \quad &\text{(definition of $\mathbf E$)} \\
> &= \mathbf C\cdot(\mathbf D\times\mathbf E) \quad &\text{(cyclic permutation, Eq. 1.33)} \\
> \mathbf D\times(\mathbf A\times\mathbf B) &= (\mathbf D\cdot\mathbf B)\,\mathbf A - (\mathbf D\cdot\mathbf A)\,\mathbf B \quad &\text{(Eq. 1.37 with the factors $\mathbf D$, $\mathbf A$, $\mathbf B$)} \\
> \mathbf C\cdot(\mathbf D\times\mathbf E) &= (\mathbf D\cdot\mathbf B)(\mathbf C\cdot\mathbf A) - (\mathbf D\cdot\mathbf A)(\mathbf C\cdot\mathbf B) \quad &\text{(dot-multiply by $\mathbf C$; linearity, Eq. 1.26)} \\
> &= (\mathbf A\cdot\mathbf C)(\mathbf B\cdot\mathbf D) - (\mathbf A\cdot\mathbf D)(\mathbf B\cdot\mathbf C) \quad &\text{(commutativity, Eq. 1.25)}
> \end{aligned}$$
>
> $$\boxed{(\mathbf A\times\mathbf B)\cdot(\mathbf C\times\mathbf D) = (\mathbf A\cdot\mathbf C)(\mathbf B\cdot\mathbf D) - (\mathbf A\cdot\mathbf D)(\mathbf B\cdot\mathbf C)}$$
>
> **Units:** $[\mathbf A][\mathbf B][\mathbf C][\mathbf D]$ in every term
> **Meaning:** with $\mathbf C$ equal to $\mathbf A$ and $\mathbf D$ equal to $\mathbf B$ it gives the squared magnitude of the cross product as $A^2B^2$ minus the squared dot product, that is $A^2B^2\sin^2\theta_{AB}$, in agreement with Eq. 1.30.

### Moment of a vector

Take a sliding or bound vector $\mathbf A$, a point $O$ and any point $P$ on the line of action of $\mathbf A$. The cross product of $\mathbf{OP}$ with $\mathbf A$ is the moment of $\mathbf A$ about $O$ (Eq. 1.49); it is perpendicular to the plane that contains $\mathbf{OP}$ and $\mathbf A$ (Notes.pdf, Sec. 1.6.8, Fig. 1.7).

![[attachments/EM-T/t1-moment.svg]]

> [!derivation] The moment depends only on the distance to the line of action
> **Law:** definition of the moment; decomposition of $\mathbf{OP}$ along and across the line of action; linearity of the cross product
> **Source:** Notes.pdf, Eq. 1.49; Notes.pdf, Eq. 1.50; Notes.pdf Fig. 1.7
>
> Split $\mathbf{OP}$ into a part parallel to $\mathbf A$ and a part perpendicular to it. The perpendicular part is the leg of the right triangle $O$, $P$, foot of the perpendicular from $O$ to the line, that is normal to the line; its length $h$ is the distance from $O$ to the line of action.
>
> $$\begin{aligned}
> \mathbf M &= \mathbf{OP}\times\mathbf A \quad &\text{(definition, Eq. 1.49)} \\
> \mathbf{OP} &= \mathbf{OP}_\parallel + \mathbf{OP}_\perp \quad &\text{(parallel and perpendicular parts with respect to $\mathbf A$)} \\
> \mathbf M &= \mathbf{OP}_\parallel\times\mathbf A + \mathbf{OP}_\perp\times\mathbf A \quad &\text{(linearity, Eq. 1.32)} \\
> \mathbf{OP}_\parallel\times\mathbf A &= \mathbf 0 \quad &\text{(collinear factors, Sec. 1.6.2)} \\
> \lVert\mathbf{OP}_\perp\times\mathbf A\rVert &= h\,A\left|\sin\frac{\pi}{2}\right| \quad &\text{(Eq. 1.30 with perpendicular factors)} \\
> &= h\,A \quad &\text{(the sine of a right angle is one)} \\
> \mathbf M &= h\,A\,\mathbf e_M \quad &\text{($\mathbf e_M$: unit normal to the plane of $\mathbf{OP}$ and $\mathbf A$, right-hand rule, Eq. 1.50)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M = \mathbf{OP}\times\mathbf A = h\,A\,\mathbf e_M}$$
>
> **Units:** $[\mathrm L][\mathbf A]$; for a force, $[\mathrm L][\mathrm{M\,L\,T^{-2}}] = [\mathrm{M\,L^2\,T^{-2}}]$, a torque in $\mathrm{N\,m}$
> **Meaning:** only the distance from $O$ to the line of action and the magnitude of $\mathbf A$ matter: the moment is zero when the line of action passes through $O$.

> [!derivation] The moment does not depend on the point chosen on the line of action
> **Law:** two points of the line of action differ by a multiple of $\mathbf A$; linearity of the cross product
> **Source:** Notes.pdf, Sec. 1.6.8; Notes.pdf, Eq. 1.49; Notes.pdf, Eq. 1.32
>
> $$\begin{aligned}
> \mathbf{PP'} &= \lambda\,\mathbf A \quad &\text{($P'$ is another point of the line of action)} \\
> \mathbf{OP'}\times\mathbf A &= \left(\mathbf{OP} + \lambda\,\mathbf A\right)\times\mathbf A \quad &\text{($\mathbf{OP'} = \mathbf{OP} + \mathbf{PP'}$)} \\
> &= \mathbf{OP}\times\mathbf A + \lambda\,\mathbf A\times\mathbf A \quad &\text{(linearity, Eq. 1.32)} \\
> &= \mathbf{OP}\times\mathbf A \quad &\text{($\mathbf A\times\mathbf A = \mathbf 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf{OP'}\times\mathbf A = \mathbf{OP}\times\mathbf A = \mathbf M}$$
>
> **Units:** $[\mathrm L][\mathbf A]$
> **Meaning:** sliding the vector along its line of action does not change its moment, which is why a force on a rigid body is a sliding vector.

## 6. Time derivative of a vector

The differential change of a vector is a vector, with magnitude and direction, and the differential of a tensor is a tensor; so the derivative with respect to time of a vector function of time is again a vector (Notes.pdf, Sec. 1.7). In this chapter there is a single observer, for whom the vectors of $\mathcal B_0$ do not change; how the derivative depends on the observer is the subject of Chapter 2 ([Lecture 1, Slide 10]). The derivative is defined as the limit of Eq. 1.51:

| Definition (Eq. 1.51) |
| :--- |
| $\dfrac{d\mathbf A}{dt} = \displaystyle\lim_{\Delta t\to 0}\frac{\mathbf A(t+\Delta t) - \mathbf A(t)}{\Delta t}$ |

A vector changes when its magnitude, its direction or both change, and the rate of change is the vector sum of the two rates (Notes.pdf, Sec. 1.7.1; [Lecture 1, Slide 9]). The dot over a scalar always denotes its time derivative.

> [!derivation] Rate of change due to a change of magnitude
> **Law:** the direction is fixed, so the unit vector is constant
> **Source:** Notes.pdf, Eq. 1.52; Notes.pdf Fig. 1.8
>
> $$\begin{aligned}
> \mathbf A &= A\,\mathbf e_A \quad &\text{(magnitude times unit vector, Sec. 1.3)} \\
> d\mathbf A &= dA\,\mathbf e_A \quad &\text{(only $A$ changes, from $A$ to $A + dA$; $\mathbf e_A$ is constant)} \\
> \frac{d\mathbf A}{dt} &= \frac{dA}{dt}\,\mathbf e_A \quad &\text{(divide by $dt$)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\mathbf A}{dt} = \frac{dA}{dt}\,\mathbf e_A}$$
>
> **Units:** $[\mathbf A]\,[\mathrm{T^{-1}}]$ on both sides
> **Meaning:** a change of magnitude alone gives a derivative parallel to $\mathbf A$: positive along $\mathbf e_A$ when the vector grows, negative when it shrinks.

> [!derivation] A change of direction alone gives a perpendicular differential
> **Law:** constant magnitude; differential of a dot product
> **Source:** Notes.pdf, Eq. 1.53; Notes.pdf, Eq. 1.66; [Lecture 1, Slide 9]
>
> $$\begin{aligned}
> \mathbf A\cdot\mathbf A &= A^2 = \text{constant} \quad &\text{(only the direction changes)} \\
> d(\mathbf A\cdot\mathbf A) &= 0 \quad &\text{(differential of a constant)} \\
> d(\mathbf A\cdot\mathbf A) &= d\mathbf A\cdot\mathbf A + \mathbf A\cdot d\mathbf A \quad &\text{(differential of a dot product, Eq. 1.66)} \\
> &= 2\,\mathbf A\cdot d\mathbf A \quad &\text{(commutativity, Eq. 1.25)} \\
> \mathbf A\cdot d\mathbf A &= 0 \quad &\text{(the last two rows and the second one)}
> \end{aligned}$$
>
> $$\boxed{\lVert\mathbf A\rVert = \text{constant}\ \Longrightarrow\ \mathbf A\cdot d\mathbf A = 0}$$
>
> **Units:** $[\mathbf A]^2$
> **Meaning:** $d\mathbf A$ is orthogonal to $\mathbf A$; a sketch with a finite $d\mathbf A$ shows them only nearly perpendicular, and the orthogonality is exact in the limit of a vanishing angle (Notes.pdf Fig. 1.9). In particular the derivative of a unit vector is always perpendicular to it.

[Lecture 1, Slide 9] splits a general differential into both parts at once:

> [!derivation] Parallel and perpendicular parts of the differential of a vector
> **Law:** differential of a product; the unit vector has constant magnitude
> **Source:** [Lecture 1, Slide 9]; Notes.pdf, Eq. 1.64; Notes.pdf, Eq. 1.66
>
> $$\begin{aligned}
> \mathbf b &= b\,\mathbf e_b \quad &\text{(magnitude times unit vector)} \\
> d\mathbf b &= (db)\,\mathbf e_b + b\,(d\mathbf e_b) \quad &\text{(differential of a product, Eq. 1.64)} \\
> \mathbf e_b\cdot d\mathbf b &= db\;\mathbf e_b\cdot\mathbf e_b + b\;\mathbf e_b\cdot d\mathbf e_b \quad &\text{(dot-multiply by $\mathbf e_b$)} \\
> &= db + b\;\mathbf e_b\cdot d\mathbf e_b \quad &\text{($\mathbf e_b\cdot\mathbf e_b = 1$)} \\
> \mathbf e_b\cdot d\mathbf e_b &= \tfrac{1}{2}\,d(\mathbf e_b\cdot\mathbf e_b) \quad &\text{(Eq. 1.66 with both factors $\mathbf e_b$)} \\
> &= \tfrac{1}{2}\,d(1) \quad &\text{($\mathbf e_b$ is a unit vector)} \\
> &= 0 \quad &\text{(differential of a constant)} \\
> \mathbf e_b\cdot d\mathbf b &= db \quad &\text{(substitute in the fourth row)}
> \end{aligned}$$
>
> $$\boxed{d\mathbf b = (d\mathbf b)_\parallel + (d\mathbf b)_\perp,\qquad (d\mathbf b)_\parallel = db\,\mathbf e_b,\qquad (d\mathbf b)_\perp = b\,d\mathbf e_b}$$
>
> **Units:** $[\mathbf b]$ in every term
> **Meaning:** the component of $d\mathbf b$ along $\mathbf e_b$ is the change of magnitude and the part perpendicular to $\mathbf e_b$ is the change of direction ([Lecture 1, Slide 9]).

> [!warning] The magnitude of the differential is not the differential of the magnitude
> When the direction of $\mathbf A$ changes, the change of its magnitude, $dA$, differs from the magnitude of its change, $\lvert d\mathbf A\rvert$: a vector of constant magnitude has zero $dA$ but a non-zero $\lvert d\mathbf A\rvert$ (Notes.pdf, Sec. 1.7.1, footnote 8).

### Rotation in the plane of the paper

Let $\mathbf A$ rotate counterclockwise in the plane of the paper, with constant magnitude, its angle $\theta$ growing at a given rate (the time derivative of $\theta$). The rotation is about the axis normal to the paper, along $\mathbf k$ coming out of the page, so that it is right-handed (Notes.pdf, Sec. 1.7.1, Fig. 1.9).

![[attachments/EM-T/t1-rotating-vector-plane.svg]]

> [!derivation] Derivative of a vector that rotates about the normal to the paper
> **Law:** arc of a circle of radius $A$; direction of the change normal to $\mathbf A$ in the sense of the rotation
> **Source:** Notes.pdf, Eq. 1.54; Notes.pdf, Eq. 1.55; Notes.pdf, Eq. 1.56; Notes.pdf Fig. 1.9
>
> View with $\mathbf k$ out of the paper (⊙), $\mathbf i$ to the right and $\mathbf j$ up; $\theta$ is the angle of $\mathbf A$ from $\mathbf i$, counterclockwise.
>
> $$\begin{aligned}
> d\theta &= \dot\theta\,dt \quad &\text{(angle turned in the time $dt$)} \\
> \lvert d\mathbf A\rvert &= A\,d\theta \quad &\text{(the tip moves on a circle of radius $A$; the chord tends to the arc)} \\
> &= A\,\dot\theta\,dt \quad &\text{(substitute $d\theta$, Eq. 1.54)} \\
> \left\lvert\frac{d\mathbf A}{dt}\right\rvert &= A\,\dot\theta \quad &\text{(divide by $dt$, Eq. 1.55)} \\
> \lVert\mathbf k\times\mathbf A\rVert &= 1\cdot A\left|\sin\frac{\pi}{2}\right| \quad &\text{(Eq. 1.30: $\mathbf k$ is perpendicular to $\mathbf A$)} \\
> &= A \quad &\text{(the sine of a right angle is one)} \\
> \frac{d\mathbf A}{dt} &= \dot\theta\,\mathbf k\times\mathbf A \quad &\text{($\mathbf k\times\mathbf A$ is $\mathbf A$ turned a quarter turn counterclockwise: the direction of $d\mathbf A$; same magnitude $A\dot\theta$)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\mathbf A}{dt} = \dot\theta\,\mathbf k\times\mathbf A}$$
>
> **Units:** $[\mathrm{T^{-1}}][\mathbf A]$ on the right, $[\mathbf A][\mathrm{T^{-1}}]$ on the left
> **Meaning:** the derivative is tangent to the circle described by the tip of $\mathbf A$, in the sense of the rotation, and proportional to the rate $\dot\theta$; a clockwise rotation has negative $\dot\theta$ and reverses it.

The same result follows in components, with the chain rule written out; this is the check of Eq. 1.56 from Eqs. 1.3 and 1.4.

> [!derivation] Check of Eq. 1.56 in components
> **Law:** components with a known angle; chain rule; cross products of the basis vectors
> **Source:** Notes.pdf, Eq. 1.56; Notes.pdf, Eq. 1.3; Notes.pdf, Eq. 1.4; Notes.pdf, Eq. 1.42
>
> $$\begin{aligned}
> \mathbf A &= A\cos\theta\,\mathbf i + A\sin\theta\,\mathbf j \quad &\text{(Eqs. 1.3 and 1.4; $A$ constant, $\theta = \theta(t)$)} \\
> \frac{d}{dt}\cos\theta(t) &= \frac{d\cos\theta}{d\theta}\,\frac{d\theta}{dt} \quad &\text{(chain rule)} \\
> &= -\sin\theta\,\dot\theta \quad &\text{(derivative of the cosine)} \\
> \frac{d}{dt}\sin\theta(t) &= \frac{d\sin\theta}{d\theta}\,\frac{d\theta}{dt} \quad &\text{(chain rule)} \\
> &= \cos\theta\,\dot\theta \quad &\text{(derivative of the sine)} \\
> \frac{d\mathbf A}{dt} &= -A\sin\theta\,\dot\theta\,\mathbf i + A\cos\theta\,\dot\theta\,\mathbf j \quad &\text{($\mathbf i$, $\mathbf j$ and $A$ are constant)} \\
> \dot\theta\,\mathbf k\times\mathbf A &= \dot\theta\left(A\cos\theta\,\mathbf k\times\mathbf i + A\sin\theta\,\mathbf k\times\mathbf j\right) \quad &\text{(distribute, Eq. 1.32)} \\
> &= \dot\theta\left(A\cos\theta\,\mathbf j - A\sin\theta\,\mathbf i\right) \quad &\text{($\mathbf k\times\mathbf i = \mathbf j$, $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> &= -A\sin\theta\,\dot\theta\,\mathbf i + A\cos\theta\,\dot\theta\,\mathbf j \quad &\text{(reorder: the fourth row)}
> \end{aligned}$$
>
> $$\boxed{\frac{d}{dt}\left(A\cos\theta\,\mathbf i + A\sin\theta\,\mathbf j\right) = \dot\theta\,\mathbf k\times\mathbf A}$$
>
> **Units:** $[\mathbf A][\mathrm{T^{-1}}]$ in every term
> **Meaning:** both routes agree; with $\theta$ equal to zero the derivative is $A\dot\theta\,\mathbf j$, perpendicular to $\mathbf A$ (which then lies along $\mathbf i$) and pointing in the sense of the rotation.

### Rotation about a general axis

Now $\mathbf A$, of constant magnitude, rotates about a general axis of unit vector $\mathbf e_\omega$, oriented so that the rotation obeys the right-hand rule, and $\theta$ is the angle turned about that axis (Notes.pdf, Sec. 1.7.1, Fig. 1.10).

![[attachments/EM-T/t1-rotating-vector-3d.svg]]

> [!derivation] Derivative of a vector that rotates about a general axis: the angular velocity
> **Law:** decomposition along and across the axis; the perpendicular part describes a circle
> **Source:** Notes.pdf, Eq. 1.57; Notes.pdf, Eq. 1.59; Notes.pdf, Eq. 1.60; Notes.pdf, Eq. 1.61; Notes.pdf, Eq. 1.62; Notes.pdf Fig. 1.10
>
> The perpendicular part is the leg, normal to the axis, of the right triangle whose hypotenuse is $\mathbf A$ and whose other leg lies on the axis; with $\theta_{\omega A}$ the angle between $\mathbf e_\omega$ and $\mathbf A$, it is the leg opposite to $\theta_{\omega A}$.
>
> $$\begin{aligned}
> \mathbf A &= \mathbf A_\parallel + \mathbf A_\perp \quad &\text{(parallel and perpendicular to $\mathbf e_\omega$, Eq. 1.57)} \\
> A_\parallel &= \mathbf e_\omega\cdot\mathbf A \quad &\text{(projection on the unit vector of the axis, Eq. 1.58)} \\
> A_\perp &= A\sin\theta_{\omega A} \quad &\text{(opposite leg over hypotenuse $A$)} \\
> &= \lvert\mathbf e_\omega\times\mathbf A\rvert \quad &\text{(Eq. 1.30 with $\lVert\mathbf e_\omega\rVert = 1$, Eq. 1.59)} \\
> d\mathbf A_\parallel &= \mathbf 0 \quad &\text{(the rotation does not affect the part along its own axis)} \\
> d\mathbf A &= d\mathbf A_\perp \quad &\text{($\mathbf A_\perp$ describes a circle of radius $A_\perp$ in the plane normal to $\mathbf e_\omega$)} \\
> \lvert d\mathbf A\rvert &= A_\perp\,d\theta \quad &\text{(arc of that circle)} \\
> &= \dot\theta\,\lvert\mathbf e_\omega\times\mathbf A\rvert\,dt \quad &\text{($d\theta = \dot\theta\,dt$ and $A_\perp$ from above, Eq. 1.60)} \\
> \mathbf e_\omega\times\mathbf A &= \mathbf e_\omega\times\mathbf A_\parallel + \mathbf e_\omega\times\mathbf A_\perp \quad &\text{(linearity, Eq. 1.32)} \\
> &= \mathbf e_\omega\times\mathbf A_\perp \quad &\text{($\mathbf A_\parallel$ is collinear with $\mathbf e_\omega$)} \\
> \frac{d\mathbf A}{dt} &= \dot\theta\,\mathbf e_\omega\times\mathbf A \quad &\text{($\mathbf e_\omega\times\mathbf A_\perp$ is tangent to the circle in the sense of the rotation; magnitudes agree, Eq. 1.61)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\mathbf A}{dt} = \dot\theta\,\mathbf e_\omega\times\mathbf A = \boldsymbol\omega\times\mathbf A,\qquad \boldsymbol\omega = \dot\theta\,\mathbf e_\omega}$$
>
> **Units:** $\boldsymbol\omega$ in $[\mathrm{T^{-1}}]$ ($\mathrm{rad/s}$); both sides $[\mathbf A][\mathrm{T^{-1}}]$
> **Meaning:** $\boldsymbol\omega$, the angular velocity of the rotation of $\mathbf A$, lies along the axis of rotation, points in the direction given by the right-hand rule, and its magnitude is the instantaneous rate of rotation; with $\mathbf e_\omega$ equal to $\mathbf k$ and $\mathbf A$ in the plane of the paper this is Eq. 1.56.

Eq. 1.62 also holds when the axis does not pass through the origin of $\mathbf A$: a rotation about an arbitrary axis is a rotation about a parallel axis plus a translation, and a translation changes neither the magnitude nor the direction of a vector (Notes.pdf, Sec. 1.7.1).

> [!derivation] Rate of change in the general case
> **Law:** magnitude times unit vector; product rule; Eq. 1.62 for the unit vector
> **Source:** Notes.pdf, Eq. 1.63; Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 1.64
>
> $$\begin{aligned}
> \mathbf A(t) &= A(t)\,\mathbf e_A(t) \quad &\text{(magnitude times unit vector)} \\
> \frac{d\mathbf A}{dt} &= \frac{dA}{dt}\,\mathbf e_A + A\,\frac{d\mathbf e_A}{dt} \quad &\text{(product rule, Eq. 1.64)} \\
> \frac{d\mathbf e_A}{dt} &= \boldsymbol\omega\times\mathbf e_A \quad &\text{(Eq. 1.62: $\mathbf e_A$ has constant magnitude one and rotates with $\boldsymbol\omega$)} \\
> \frac{d\mathbf A}{dt} &= \frac{dA}{dt}\,\mathbf e_A + A\,\boldsymbol\omega\times\mathbf e_A \quad &\text{(substitute)} \\
> &= \frac{dA}{dt}\,\mathbf e_A + \boldsymbol\omega\times\mathbf A \quad &\text{(linearity: $A\,\boldsymbol\omega\times\mathbf e_A = \boldsymbol\omega\times(A\,\mathbf e_A)$)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\mathbf A}{dt} = \frac{dA}{dt}\,\mathbf e_A + \boldsymbol\omega\times\mathbf A}$$
>
> **Units:** $[\mathbf A][\mathrm{T^{-1}}]$ in every term
> **Meaning:** the first term, due to the change of magnitude only, is parallel to $\mathbf A$; the second, due to the change of direction only, is orthogonal to both $\mathbf A$ and $\boldsymbol\omega$.

Vector differentiation follows the rules of scalar differentiation for addition, multiplication by a scalar and the products, keeping the order of the factors of a cross product (Notes.pdf, Sec. 1.7.1):

| Rule | Equation |
| :--- | :--- |
| $d(\lambda\mathbf A) = d\lambda\,\mathbf A + \lambda\,d\mathbf A$ | Eq. 1.64 |
| $d(\mathbf A + \mathbf B) = d\mathbf A + d\mathbf B$ | Eq. 1.65 |
| $d(\mathbf A\cdot\mathbf B) = d\mathbf A\cdot\mathbf B + \mathbf A\cdot d\mathbf B$ | Eq. 1.66 |
| $d(\mathbf A\times\mathbf B) = d\mathbf A\times\mathbf B + \mathbf A\times d\mathbf B$ | Eq. 1.67 |

### The unit vectors of a rotating basis

The vectors of a basis $\mathcal B_1$ that rotates with respect to $\mathcal B_0$ have constant magnitude and keep their mutual angles, so all three rotate with the same angular velocity $\boldsymbol\omega$ and Eq. 1.62 gives their derivatives. For a simple rotation this can be checked from the columns of the rotation matrix, differentiated with the chain rule; the derivative is the one seen by the observer for whom $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$ are constant ([Lecture 1, Slide 10]).

![[attachments/EM-T/t1-rotating-basis.svg]]

> [!derivation] Derivatives of the unit vectors of a basis in simple rotation about z
> **Law:** columns of Eq. 1.20 with $\theta_z = \theta_z(t)$; chain rule; Eq. 1.62 with the angular velocity along $\mathbf k_0$
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 1.42; [Lecture 1, Slide 10]
>
> View with $\mathbf k_0 \equiv \mathbf k_1$ out of the paper (⊙), $\mathbf i_0$ to the right, $\mathbf j_0$ up; $\theta_z$ grows counterclockwise.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\theta_z\,\mathbf i_0 + \sin\theta_z\,\mathbf j_0 \quad &\text{(first column of Eq. 1.20)} \\
> \frac{d\mathbf i_1}{dt} &= \frac{d\cos\theta_z}{d\theta_z}\,\dot\theta_z\,\mathbf i_0 + \frac{d\sin\theta_z}{d\theta_z}\,\dot\theta_z\,\mathbf j_0 \quad &\text{(chain rule; $\mathbf i_0$ and $\mathbf j_0$ are constant)} \\
> &= -\sin\theta_z\,\dot\theta_z\,\mathbf i_0 + \cos\theta_z\,\dot\theta_z\,\mathbf j_0 \quad &\text{(derivatives of cosine and sine)} \\
> &= \dot\theta_z\,\mathbf j_1 \quad &\text{(second column of Eq. 1.20: $\mathbf j_1 = -\sin\theta_z\,\mathbf i_0 + \cos\theta_z\,\mathbf j_0$)} \\
> \dot\theta_z\,\mathbf k_0\times\mathbf i_1 &= \dot\theta_z\left(\cos\theta_z\,\mathbf k_0\times\mathbf i_0 + \sin\theta_z\,\mathbf k_0\times\mathbf j_0\right) \quad &\text{(distribute, Eq. 1.32)} \\
> &= \dot\theta_z\left(\cos\theta_z\,\mathbf j_0 - \sin\theta_z\,\mathbf i_0\right) \quad &\text{($\mathbf k_0\times\mathbf i_0 = \mathbf j_0$, $\mathbf k_0\times\mathbf j_0 = -\mathbf i_0$)} \\
> &= \dot\theta_z\,\mathbf j_1 \quad &\text{(the same vector: Eq. 1.62 holds with $\boldsymbol\omega = \dot\theta_z\,\mathbf k_0$)} \\
> \frac{d\mathbf j_1}{dt} &= -\cos\theta_z\,\dot\theta_z\,\mathbf i_0 - \sin\theta_z\,\dot\theta_z\,\mathbf j_0 \quad &\text{(chain rule on the second column)} \\
> &= -\dot\theta_z\,\mathbf i_1 \quad &\text{(first column of Eq. 1.20)} \\
> \frac{d\mathbf k_1}{dt} &= \mathbf 0 \quad &\text{($\mathbf k_1 = \mathbf k_0$, the fixed axis, constant for this observer)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\mathbf i_1}{dt} = \dot\theta_z\,\mathbf j_1 = \boldsymbol\omega\times\mathbf i_1,\quad \frac{d\mathbf j_1}{dt} = -\dot\theta_z\,\mathbf i_1 = \boldsymbol\omega\times\mathbf j_1,\quad \frac{d\mathbf k_1}{dt} = \mathbf 0 = \boldsymbol\omega\times\mathbf k_1,\qquad \boldsymbol\omega = \dot\theta_z\,\mathbf k_0}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ in every term (unit vectors are dimensionless)
> **Meaning:** each derivative is the unit vector turned a quarter turn in the sense of the rotation and scaled by the rate $\dot\theta_z$, perpendicular to the vector itself as every derivative of a unit vector must be; $\mathbf k_0\times\mathbf j_1$ is $-\mathbf i_1$ by the same distributive steps.

## 7. Infinitesimal rotations and the angular velocity vector

Finite rotations do not commute (Section 3). For two small simple rotations about orthogonal axes the difference between the two orders becomes negligible, and in the limit of infinitesimal (differential) rotations the product no longer depends on the order (Notes.pdf, Sec. 1.7.2). This gives a second route to the angular velocity, through the matrices of Section 3.

> [!derivation] Cosine and sine of a differential angle
> **Law:** Maclaurin series of the cosine and the sine
> **Source:** Notes.pdf, Eq. 1.68; Notes.pdf, Eq. 1.69
>
> $$\begin{aligned}
> \cos(d\theta) &= 1 - \frac{d\theta^2}{2!} + \frac{d\theta^4}{4!} - \cdots \quad &\text{(Maclaurin series of the cosine)} \\
> &= 1 + O(d\theta^2) \quad &\text{(the first omitted term is of second order)} \\
> \sin(d\theta) &= d\theta - \frac{d\theta^3}{3!} + \cdots \quad &\text{(Maclaurin series of the sine)} \\
> &= d\theta + O(d\theta^3) \quad &\text{(the first omitted term is of third order)}
> \end{aligned}$$
>
> $$\boxed{\cos(d\theta) = 1 + O(d\theta^2),\qquad \sin(d\theta) = d\theta + O(d\theta^3)}$$
>
> **Units:** angles in radians, dimensionless
> **Meaning:** to first order a differential rotation leaves the projections along the old axes unchanged and adds a cross term equal to the angle; for an angle of $0.01$ rad the neglected part of the cosine is $5\times 10^{-5}$.

> [!derivation] First-order simple rotation matrices
> **Law:** Eqs. 1.18 to 1.20 with differential angles, first-order terms kept
> **Source:** Notes.pdf, Eq. 1.70; Notes.pdf, Eq. 1.18; Notes.pdf, Eq. 1.19; Notes.pdf, Eq. 1.20
>
> $$\begin{aligned}
> [R_x] &= \begin{pmatrix} 1 & 0 & 0 \cr 0 & \cos d\theta_x & -\sin d\theta_x \cr 0 & \sin d\theta_x & \cos d\theta_x \end{pmatrix} \quad &\text{(Eq. 1.18 with the angle $d\theta_x$)} \\
> &= \begin{pmatrix} 1 & 0 & 0 \cr 0 & 1 & -d\theta_x \cr 0 & d\theta_x & 1 \end{pmatrix} \quad &\text{(Eqs. 1.68 and 1.69 to first order)} \\
> [R_y] &= \begin{pmatrix} 1 & 0 & d\theta_y \cr 0 & 1 & 0 \cr -d\theta_y & 0 & 1 \end{pmatrix} \quad &\text{(same steps on Eq. 1.19)} \\
> [R_z] &= \begin{pmatrix} 1 & -d\theta_z & 0 \cr d\theta_z & 1 & 0 \cr 0 & 0 & 1 \end{pmatrix} \quad &\text{(same steps on Eq. 1.20)}
> \end{aligned}$$
>
> $$\boxed{[R_x] = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & -d\theta_x \\ 0 & d\theta_x & 1 \end{bmatrix},\quad [R_y] = \begin{bmatrix} 1 & 0 & d\theta_y \\ 0 & 1 & 0 \\ -d\theta_y & 0 & 1 \end{bmatrix},\quad [R_z] = \begin{bmatrix} 1 & -d\theta_z & 0 \\ d\theta_z & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** each matrix is the identity plus an antisymmetric matrix of first order; the minus signs sit where they sit in Eqs. 1.18 to 1.20.

> [!derivation] Product of three infinitesimal rotations
> **Law:** product of matrices, row times column; terms of second and third order dropped
> **Source:** Notes.pdf, Eq. 1.71; Notes.pdf, Eq. 1.70
>
> $$\begin{aligned}
> [R_x][R_y] &= \begin{pmatrix} 1\cdot 1 + 0\cdot 0 + 0\cdot(-d\theta_y) & 1\cdot 0 + 0\cdot 1 + 0\cdot 0 & 1\cdot d\theta_y + 0\cdot 0 + 0\cdot 1 \cr 0\cdot 1 + 1\cdot 0 + (-d\theta_x)(-d\theta_y) & 0\cdot 0 + 1\cdot 1 + (-d\theta_x)\cdot 0 & 0\cdot d\theta_y + 1\cdot 0 + (-d\theta_x)\cdot 1 \cr 0\cdot 1 + d\theta_x\cdot 0 + 1\cdot(-d\theta_y) & 0\cdot 0 + d\theta_x\cdot 1 + 1\cdot 0 & 0\cdot d\theta_y + d\theta_x\cdot 0 + 1\cdot 1 \end{pmatrix} \quad &\text{(row $m$ of $[R_x]$ times column $n$ of $[R_y]$)} \\
> &= \begin{pmatrix} 1 & 0 & d\theta_y \cr d\theta_x d\theta_y & 1 & -d\theta_x \cr -d\theta_y & d\theta_x & 1 \end{pmatrix} \quad &\text{(drop the zero products)} \\
> &= \begin{pmatrix} 1 & 0 & d\theta_y \cr 0 & 1 & -d\theta_x \cr -d\theta_y & d\theta_x & 1 \end{pmatrix} \quad &\text{(drop the second-order product $d\theta_x d\theta_y$)} \\
> [R_x][R_y][R_z] &= \begin{pmatrix} 1\cdot 1 + 0\cdot d\theta_z + d\theta_y\cdot 0 & 1\cdot(-d\theta_z) + 0\cdot 1 + d\theta_y\cdot 0 & 1\cdot 0 + 0\cdot 0 + d\theta_y\cdot 1 \cr 0\cdot 1 + 1\cdot d\theta_z + (-d\theta_x)\cdot 0 & 0\cdot(-d\theta_z) + 1\cdot 1 + (-d\theta_x)\cdot 0 & 0\cdot 0 + 1\cdot 0 + (-d\theta_x)\cdot 1 \cr (-d\theta_y)\cdot 1 + d\theta_x d\theta_z + 1\cdot 0 & (-d\theta_y)(-d\theta_z) + d\theta_x\cdot 1 + 1\cdot 0 & (-d\theta_y)\cdot 0 + d\theta_x\cdot 0 + 1\cdot 1 \end{pmatrix} \quad &\text{(right-multiply by $[R_z]$, row times column)} \\
> &= \begin{pmatrix} 1 & -d\theta_z & d\theta_y \cr d\theta_z & 1 & -d\theta_x \cr -d\theta_y + d\theta_x d\theta_z & d\theta_x + d\theta_y d\theta_z & 1 \end{pmatrix} \quad &\text{(drop the zero products)} \\
> &= \begin{pmatrix} 1 & -d\theta_z & d\theta_y \cr d\theta_z & 1 & -d\theta_x \cr -d\theta_y & d\theta_x & 1 \end{pmatrix} \quad &\text{(drop the second-order products)}
> \end{aligned}$$
>
> $$\boxed{[R] = [R_x][R_y][R_z] = \begin{bmatrix} 1 & -d\theta_z & d\theta_y \\ d\theta_z & 1 & -d\theta_x \\ -d\theta_y & d\theta_x & 1 \end{bmatrix}}$$
>
> **Units:** dimensionless
> **Meaning:** three numbers, $d\theta_x$, $d\theta_y$, $d\theta_z$, define the whole infinitesimal rotation; each one appears where its own simple rotation puts it.

> [!derivation] Infinitesimal rotations commute
> **Law:** the same product in the reverse order, compared to first order
> **Source:** Notes.pdf, Sec. 1.7.2; Notes.pdf, Eq. 1.71
>
> $$\begin{aligned}
> [R_z][R_y] &= \begin{pmatrix} 1 & -d\theta_z & d\theta_y \cr d\theta_z & 1 & d\theta_z d\theta_y \cr -d\theta_y & 0 & 1 \end{pmatrix} \quad &\text{(row times column; the only product of two non-zero off-diagonal entries is $d\theta_z\cdot d\theta_y$ in entry $(2,3)$)} \\
> [R_z][R_y][R_x] &= \begin{pmatrix} 1 & -d\theta_z + d\theta_y d\theta_x & d\theta_y + d\theta_z d\theta_x \cr d\theta_z & 1 + d\theta_z d\theta_y d\theta_x & -d\theta_x + d\theta_z d\theta_y \cr -d\theta_y & d\theta_x & 1 \end{pmatrix} \quad &\text{(right-multiply by $[R_x]$, row times column)} \\
> &= \begin{pmatrix} 1 & -d\theta_z & d\theta_y \cr d\theta_z & 1 & -d\theta_x \cr -d\theta_y & d\theta_x & 1 \end{pmatrix} \quad &\text{(drop the products of second and third order)}
> \end{aligned}$$
>
> $$\boxed{[R_z][R_y][R_x] = [R_x][R_y][R_z] + O(d\theta^2)}$$
>
> **Units:** dimensionless
> **Meaning:** the two orders differ only in second-order terms, in contrast with the finite rotations of Section 3; the notes state that infinitesimal rotations commute in general.

Let a vector $\mathbf A$ of constant magnitude undergo the differential rotation $[R]$ of Eq. 1.71 between $t$ and $t + dt$, read as a rotation seen from the single basis $\mathcal B_0$ (Notes.pdf, Sec. 1.5.1 and 1.7.2).

![[attachments/EM-T/t1-infinitesimal-rotation.svg]]

> [!derivation] Angular velocity matrix and angular velocity vector
> **Law:** definition of the derivative; rotation of the components by $[R]$; cross product in components
> **Source:** Notes.pdf, Eq. 1.72; Notes.pdf, Eq. 1.73; Notes.pdf, Eq. 1.71; Notes.pdf, Eq. 1.42
>
> Write $\omega_x$, $\omega_y$, $\omega_z$ for the rates $d\theta_x/dt$, $d\theta_y/dt$, $d\theta_z/dt$.
>
> $$\begin{aligned}
> [\mathbf A(t+dt)]_0 &= [R]\,[\mathbf A(t)]_0 \quad &\text{(the vector rotated by $[R]$, Sec. 1.5.1)} \\
> \frac{d\mathbf A}{dt} &= \frac{[R]\,\mathbf A - \mathbf A}{dt} \quad &\text{(definition of the derivative, Eq. 1.51)} \\
> &= \frac{[R] - [U]}{dt}\,\mathbf A \quad &\text{(factor $\mathbf A$ on the right)} \\
> &= \begin{pmatrix} 0 & -\omega_z & \omega_y \cr \omega_z & 0 & -\omega_x \cr -\omega_y & \omega_x & 0 \end{pmatrix}\begin{pmatrix} A_x \cr A_y \cr A_z \end{pmatrix} \quad &\text{(subtract $[U]$ from Eq. 1.71, divide each entry by $dt$: the matrix $[\Omega]$)} \\
> &= \begin{pmatrix} 0\cdot A_x - \omega_z A_y + \omega_y A_z \cr \omega_z A_x + 0\cdot A_y - \omega_x A_z \cr -\omega_y A_x + \omega_x A_y + 0\cdot A_z \end{pmatrix} \quad &\text{(rows of $[\Omega]$ times the column)} \\
> \boldsymbol\omega\times\mathbf A &= (\omega_yA_z - \omega_zA_y)\,\mathbf i + (\omega_zA_x - \omega_xA_z)\,\mathbf j + (\omega_xA_y - \omega_yA_x)\,\mathbf k \quad &\text{(Eq. 1.42 with $\boldsymbol\omega = \omega_x\mathbf i + \omega_y\mathbf j + \omega_z\mathbf k$)} \\
> [\Omega]^T &= -[\Omega] \quad &\text{(exchanging rows and columns changes every sign: antisymmetric)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\mathbf A}{dt} = [\Omega]\,\mathbf A \equiv \boldsymbol\omega\times\mathbf A,\qquad \boldsymbol\omega = \frac{d\theta_x}{dt}\,\mathbf i + \frac{d\theta_y}{dt}\,\mathbf j + \frac{d\theta_z}{dt}\,\mathbf k}$$
>
> **Units:** $[\Omega]$ and $\boldsymbol\omega$ in $[\mathrm{T^{-1}}]$ (rad/s); both sides $[\mathbf A][\mathrm{T^{-1}}]$
> **Meaning:** the antisymmetric angular velocity matrix and the angular velocity vector hold the same three numbers; mechanics uses the vector, which lies along the axis of rotation, follows the right-hand rule and has the angular rate as its magnitude, the same object as in Eq. 1.62.

## 8. Gradient, divergence and curl

Let $x$, $y$, $z$ be the Cartesian coordinates of space and $\mathcal B_0$ the canonical basis. The nabla symbol is shorthand for the differential operator built from the three partial derivatives (Notes.pdf, Secs. 1.7.3 and 1.7.4):

| Definition | Equation |
| :--- | :--- |
| $\nabla = \dfrac{\partial}{\partial x}\,\mathbf i + \dfrac{\partial}{\partial y}\,\mathbf j + \dfrac{\partial}{\partial z}\,\mathbf k$ | Sec. 1.7.3 |
| gradient of a scalar function: $\nabla f = \dfrac{\partial f}{\partial x}\,\mathbf i + \dfrac{\partial f}{\partial y}\,\mathbf j + \dfrac{\partial f}{\partial z}\,\mathbf k$ | Eq. 1.74 |
| divergence of a vector function: $\mathrm{div}(\mathbf A) = \nabla\cdot\mathbf A = \dfrac{\partial A_x}{\partial x} + \dfrac{\partial A_y}{\partial y} + \dfrac{\partial A_z}{\partial z}$ | Eq. 1.75 |
| curl (rotational) of a vector function: $\mathrm{rot}(\mathbf A) = \nabla\times\mathbf A$, components in the box below | Eq. 1.76 |

The gradient points in the direction in which $f$ grows, and its magnitude is the rate of growth in that direction. The divergence of a vector is a scalar and its curl is a vector, in symmetry with the dot and cross products (Notes.pdf, Sec. 1.7.4). A vector function with zero divergence is solenoidal; one with zero curl is irrotational.

> [!derivation] The curl as the cross product of nabla with the vector
> **Law:** cross product in components with the operator $\nabla$ as first factor
> **Source:** Notes.pdf, Eq. 1.76; Notes.pdf, Eq. 1.42
>
> $$\begin{aligned}
> \nabla\times\mathbf A &= \left(\nabla_yA_z - \nabla_zA_y\right)\mathbf i + \left(\nabla_zA_x - \nabla_xA_z\right)\mathbf j + \left(\nabla_xA_y - \nabla_yA_x\right)\mathbf k \quad &\text{(Eq. 1.42 with the factors $\nabla$ and $\mathbf A$; the operator acts on the component to its right)} \\
> &= \left(\frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z}\right)\mathbf i + \left(\frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x}\right)\mathbf j + \left(\frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y}\right)\mathbf k \quad &\text{(components of $\nabla$: the partial derivatives)}
> \end{aligned}$$
>
> $$\boxed{\nabla\times\mathbf A = \left(\frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z}\right)\mathbf i + \left(\frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x}\right)\mathbf j + \left(\frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y}\right)\mathbf k}$$
>
> **Units:** $[\mathbf A][\mathrm{L^{-1}}]$ in every term
> **Meaning:** the same pattern as $\mathbf A\times\mathbf B$ in Eq. 1.42; Eq. 1.76 of the notes prints every component with the opposite sign (warning below).

> [!derivation] Erratum check: the curl of a uniform rotation
> **Law:** velocity field of a rotation about $Oz$, from Eq. 1.62 and the cross product in components; curl of that field
> **Source:** Notes.pdf, Eq. 1.76; Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 1.42
>
> Take the field of the velocities of the points of space rotating with constant angular velocity $\omega\,\mathbf k$ about $Oz$; the position of a point is $x\,\mathbf i + y\,\mathbf j + z\,\mathbf k$.
>
> $$\begin{aligned}
> \mathbf A &= \omega\,\mathbf k\times\left(x\,\mathbf i + y\,\mathbf j + z\,\mathbf k\right) \quad &\text{(Eq. 1.62 applied to the position vector)} \\
> &= \omega x\,\mathbf k\times\mathbf i + \omega y\,\mathbf k\times\mathbf j + \omega z\,\mathbf k\times\mathbf k \quad &\text{(distribute, Eq. 1.32)} \\
> &= -\omega y\,\mathbf i + \omega x\,\mathbf j \quad &\text{($\mathbf k\times\mathbf i = \mathbf j$, $\mathbf k\times\mathbf j = -\mathbf i$, $\mathbf k\times\mathbf k = \mathbf 0$)} \\
> (\nabla\times\mathbf A)_z &= \frac{\partial(\omega x)}{\partial x} - \frac{\partial(-\omega y)}{\partial y} \quad &\text{($\mathbf k$ component of the box above)} \\
> &= \omega + \omega \quad &\text{(differentiate; $\omega$ is constant)} \\
> &= 2\omega \quad &\text{(add)} \\
> \frac{\partial A_x}{\partial y} - \frac{\partial A_y}{\partial x} &= \frac{\partial(-\omega y)}{\partial y} - \frac{\partial(\omega x)}{\partial x} \quad &\text{(the $\mathbf k$ component as printed in Eq. 1.76)} \\
> &= -2\omega \quad &\text{(differentiate and add)}
> \end{aligned}$$
>
> $$\boxed{\nabla\times(\omega\,\mathbf k\times\mathbf r) = 2\omega\,\mathbf k}$$
>
> **Units:** $[\mathrm{T^{-1}}]$: the curl of a velocity field is a rate of rotation
> **Meaning:** the curl of a rigid rotation is twice its angular velocity and points along it by the right-hand rule; the printed Eq. 1.76 would give minus that, which confirms that its signs are reversed.

> [!warning] Erratum to Notes.pdf, Eq. 1.76
> Every component of the curl in Eq. 1.76 is printed with the opposite sign: the notes write the derivative of the $y$ component with respect to $z$ minus the derivative of the $z$ component with respect to $y$ for the $\mathbf i$ component, and likewise for the others. The cross product rule of Eq. 1.42 gives the opposite order (first box of this section), and the uniform rotation of the second box shows the difference. Eqs. 1.77 to 1.79 and the definitions of solenoidal and irrotational fields are not affected, because they only involve a zero curl or a curl of either sign.

> [!derivation] The curl of a gradient vanishes
> **Law:** curl in components applied to the gradient; equality of the mixed second partial derivatives (Schwarz)
> **Source:** Notes.pdf, Eq. 1.77; Notes.pdf, Eq. 1.74
>
> $f$ is assumed twice continuously differentiable.
>
> $$\begin{aligned}
> \big(\nabla\times(\nabla f)\big)_x &= \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial z}\right) - \frac{\partial}{\partial z}\left(\frac{\partial f}{\partial y}\right) \quad &\text{($x$ component of the curl with $\mathbf A = \nabla f$, Eq. 1.74)} \\
> &= \frac{\partial^2 f}{\partial y\,\partial z} - \frac{\partial^2 f}{\partial z\,\partial y} \quad &\text{(second partial derivatives)} \\
> &= 0 \quad &\text{(the order of differentiation does not matter)}
> \end{aligned}$$
>
> $$\boxed{\nabla\times(\nabla f) = \mathbf 0}$$
>
> **Units:** $[f][\mathrm{L^{-2}}]$
> **Meaning:** the $y$ and $z$ components cancel in the same way (cyclic relabelling): a gradient field is always irrotational.

> [!derivation] The divergence of a curl vanishes
> **Law:** divergence in components applied to the curl; equality of the mixed second partial derivatives
> **Source:** Notes.pdf, Eq. 1.78; Notes.pdf, Eq. 1.75
>
> $\mathbf A$ is assumed twice continuously differentiable.
>
> $$\begin{aligned}
> \nabla\cdot(\nabla\times\mathbf A) &= \frac{\partial}{\partial x}\left(\frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z}\right) + \frac{\partial}{\partial y}\left(\frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x}\right) + \frac{\partial}{\partial z}\left(\frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y}\right) \quad &\text{(Eq. 1.75 applied to the components of the curl)} \\
> &= \frac{\partial^2 A_z}{\partial x\,\partial y} - \frac{\partial^2 A_y}{\partial x\,\partial z} + \frac{\partial^2 A_x}{\partial y\,\partial z} - \frac{\partial^2 A_z}{\partial y\,\partial x} + \frac{\partial^2 A_y}{\partial z\,\partial x} - \frac{\partial^2 A_x}{\partial z\,\partial y} \quad &\text{(distribute the derivatives)} \\
> &= 0 \quad &\text{(the terms cancel in pairs: $A_z$ first and fourth, $A_y$ second and fifth, $A_x$ third and sixth)}
> \end{aligned}$$
>
> $$\boxed{\nabla\cdot(\nabla\times\mathbf A) = 0}$$
>
> **Units:** $[\mathbf A][\mathrm{L^{-2}}]$
> **Meaning:** a curl field is always solenoidal; the result holds whatever the sign convention of the curl.

Helmholtz's theorem states that a twice continuously differentiable vector field can be written as the gradient of a scalar field plus the curl of a vector field (Notes.pdf, Sec. 1.7.4). With Eqs. 1.77 and 1.78, a solenoidal field is then the curl of a vector field and an irrotational field is the gradient of a scalar field.

| Helmholtz decomposition (Eq. 1.79) | Consequence |
| :--- | :--- |
| $\mathbf A = \nabla\phi + \nabla\times\mathbf B$ | solenoidal: $\mathbf A = \nabla\times\mathbf B$; irrotational: $\mathbf A = \nabla\phi$ |
