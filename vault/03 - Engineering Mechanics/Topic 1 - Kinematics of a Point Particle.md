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
