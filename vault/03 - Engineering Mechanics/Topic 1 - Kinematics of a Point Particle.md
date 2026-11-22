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
| $S_0 : \{O;\mathcal B_0\}$, $S_1 : \{O_1;\mathcal B_1\}$ | reference frames: an origin and an orthonormal right-handed basis; $S_0$ is also written $Oxyz$ (the notes call the origin of $S_1$ $A$) |
| $\boldsymbol\omega_{10}$ | angular velocity of $\mathcal B_1$ (of $S_1$) with respect to $S_0$ |
| $\left.\dfrac{d\mathbf b}{dt}\right\rvert_0$ | time derivative of the vector $\mathbf b$ taken in $S_0$, as seen by its observer |
| $\mathbf r_0^P$, $\mathbf v_0^P$, $\mathbf a_0^P$ | position, velocity and acceleration of the point particle $P$ with respect to $S_0$ |
| $x, y, z$ | Cartesian coordinates of $P$ in $S_0$ |
| $v = \lvert\mathbf v_0^P\rvert$ | speed (celerity) |
| $s$, $\dot s$ | arc length coordinate along the trajectory, and its rate |
| $\mathbf e_t$, $\mathbf e_n$, $\mathbf e_b$; $\mathcal B_F(P)$, $S_F(P)$ | tangent, normal and binormal unit vectors; intrinsic basis and intrinsic (Frenet-Serret) reference frame at $P$ |
| $C$, $\rho$, $\kappa = 1/\rho$, $\tau$ | centre and radius of the osculating circle (centre and radius of curvature), curvature and torsion of the trajectory |
| $a_t$, $a_n$ | tangential and normal components of the acceleration |
| $\theta_t$ | angle turned by the tangent $\mathbf e_t$; for a planar trajectory, the angle of $\mathbf e_t$ from $Ox$ (the notes write $\theta$) |
| $\mathcal C : \{q_1,q_2,q_3\}$; $\mathbf u_{q_i} = \partial\mathbf r_0^P/\partial q_i$; $\mathcal B_{\mathcal C}(P) : \{\mathbf e_{q_1},\mathbf e_{q_2},\mathbf e_{q_3}\}$, $S_{\mathcal C}$ | coordinate system; coordinate vectors; local unit basis and local reference frame at $P$ (the notes write $C$ for the coordinate system) |
| $R, \theta, z$; $\mathcal B_{\mathrm{cyl}} : \{\mathbf e_R,\mathbf e_\theta,\mathbf e_z\}$ | cylindrical coordinates (distance to $Oz$, azimuth, height) and their local basis (the slides write $\mathcal B_C$); the radius $R$ never carries brackets, a matrix always does |
| $r, \theta, \phi$; $\mathcal B_{\mathrm{sph}} : \{\mathbf e_r,\mathbf e_\theta,\mathbf e_\phi\}$ | spherical coordinates (distance to $O$, azimuth, latitude measured from the plane $Oxy$) and their local basis (the slides write $\mathcal B_S$); the scalar field $\phi$ of Section 8 is unrelated |
| $\varphi = \pi/2 - \phi$ | colatitude, measured from $Oz$ ([Lecture 1, Slide 20]) |
| $[{}_0R_{\mathrm{cyl}}]$, $[{}_0R_{\mathrm{sph}}]$, $[{}_{\mathrm{cyl}}R_{\mathrm{sph}}]$ | change of basis matrices between the local bases and $\mathcal B_0$ |
| $\boldsymbol\omega_{\mathrm{cyl}}$, $\boldsymbol\omega_{\mathrm{sph}}$ | angular velocities of the local bases with respect to $\mathcal B_0$ |
| $q_i$, $n$ | generalized coordinates and number of configuration degrees of freedom |
| $c_{\theta x}$, $s_{\theta x}$ (and likewise for $\theta_y$, $\theta_z$) | short forms of the cosine and sine of $\theta_x$ in the products of rotation matrices of Section 3 (not the arc length $s$) |
| $\gamma_C$ | angle between $\mathbf C$ and the unit normal $\mathbf n$ of the base, in the volume of the parallelepiped (Section 4) |
| $R_0$ | radius of the sphere and of the circular wire of the constraint examples (Section 15); not the cylindrical coordinate $R$ |
| $L$, $L_0$, $d_1$, $d_2$ | length of the string over a pulley, length in contact with the pulley, and depths of the two particles below its axis (Section 15) |

## 1. Mechanical modelling and physical quantities

### Models of reality

Classical (Newtonian) mechanics is governed by Newton's laws. It breaks down at speeds comparable with the speed of light and at atomic scales, but for engineering it is a very good model of reality; the most notable exception in aerospace is the relativistic correction of global navigation satellite systems (Notes.pdf, Ch. 1). In aerospace engineering it is applied to the motion of aircraft (position, velocity, acceleration and stability), of spacecraft (orbits, attitude, launch and orbit transfers) and of their subsystems (engines, flaps, landing gear), and it is the basis of fluid dynamics and structural dynamics.

On the way to aircraft and spacecraft, the course also applies the methods of Newtonian mechanics to simpler devices outside the aerospace field, such as ground vehicles, particles on a wire and spring-mass systems: they make the methods easier to learn, and these simple academic contraptions, or variations of them, often model parts of real aerospace systems directly. The first chapter reviews the linear algebra and vector calculus that the rest of the course needs; most of it should already be known, and the notes strongly advise reviewing the first-year notes of Calculus, Linear Algebra and Physics before starting (Notes.pdf, Ch. 1, p. 9).

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

A vector cannot be represented by a magnitude alone: a displacement needs its starting point and its direction besides its numerical value. Vectors are written in bold, $\mathbf v$, and their magnitude or norm in normal type, $v$ (Notes.pdf, Sec. 1.2). The vectors of mechanics have two or three components; vectors of higher dimension are also used in some formulations of mechanics (Notes.pdf, p. 10, footnote 1). In handwriting a small arrow marks a vector; failing to distinguish a vector from a scalar (and the magnitude of a vector is a scalar) is a serious error in an exam.

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

A set $V$ is a vector space over $\mathbb R$ when it has a vector addition and a multiplication by a scalar with the properties below, for any elements $\mathbf A$, $\mathbf B$ of $V$ and any scalars $\lambda$, $\mu$ (Notes.pdf, Sec. 1.3; [Lecture 1, Slide 5]). The vector spaces of mechanics are the plane $\mathbb R^2$ and space $\mathbb R^3$. They are not the only ones: the set of all scalars and the set of all second-order tensors of a given dimension also have the structure of a vector space (Notes.pdf, p. 11, footnote 4).

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

Eq. 1.17 writes the composite matrix of $n$ sequential changes of basis as the right-to-left product of the matrices of each change. The notes do not say which matrix each factor is. One consistent reading, with Eq. 1.16, is that the factors are the matrices in the other direction, from the old basis to the new one, as the next box shows. Another valid reading takes each factor as the $k$-th rotation written as an active rotation in the fixed basis $\mathcal B_0$; that product, also composed right to left, gives the matrix from $\mathcal B_n$ to $\mathcal B_0$.

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

The product of Eq. 1.23 is written out below, first the two leftmost factors and then the third, with the short forms $c_{\theta x}$, $s_{\theta x}$ for the cosine and sine of $\theta_x$, and likewise for $\theta_y$ and $\theta_z$.

> [!derivation] The 1-2-3 rotation matrix written out
> **Law:** product of matrices, row of the left factor times column of the right factor
> **Source:** Notes.pdf, Eq. 1.23; Notes.pdf, Eq. 1.18; Notes.pdf, Eq. 1.19; Notes.pdf, Eq. 1.20
>
> $$\begin{aligned}
> [{}_0R_1][{}_1R_2] &= \begin{pmatrix} 1 & 0 & 0 \cr 0 & c_{\theta x} & -s_{\theta x} \cr 0 & s_{\theta x} & c_{\theta x} \end{pmatrix}\begin{pmatrix} c_{\theta y} & 0 & s_{\theta y} \cr 0 & 1 & 0 \cr -s_{\theta y} & 0 & c_{\theta y} \end{pmatrix} \quad &\text{(Eqs. 1.18 and 1.19)} \\
> &= \begin{pmatrix} 1\cdot c_{\theta y} + 0\cdot 0 + 0\cdot(-s_{\theta y}) & 1\cdot 0 + 0\cdot 1 + 0\cdot 0 & 1\cdot s_{\theta y} + 0\cdot 0 + 0\cdot c_{\theta y} \cr 0\cdot c_{\theta y} + c_{\theta x}\cdot 0 + (-s_{\theta x})(-s_{\theta y}) & 0\cdot 0 + c_{\theta x}\cdot 1 + (-s_{\theta x})\cdot 0 & 0\cdot s_{\theta y} + c_{\theta x}\cdot 0 + (-s_{\theta x})\,c_{\theta y} \cr 0\cdot c_{\theta y} + s_{\theta x}\cdot 0 + c_{\theta x}(-s_{\theta y}) & 0\cdot 0 + s_{\theta x}\cdot 1 + c_{\theta x}\cdot 0 & 0\cdot s_{\theta y} + s_{\theta x}\cdot 0 + c_{\theta x}\,c_{\theta y} \end{pmatrix} \quad &\text{(row $m$ of the left factor times column $n$ of the right factor)} \\
> &= \begin{pmatrix} c_{\theta y} & 0 & s_{\theta y} \cr s_{\theta x} s_{\theta y} & c_{\theta x} & -s_{\theta x} c_{\theta y} \cr -c_{\theta x} s_{\theta y} & s_{\theta x} & c_{\theta x} c_{\theta y} \end{pmatrix} \quad &\text{(drop the zero products)} \\
> [{}_0R_3] &= \begin{pmatrix} c_{\theta y} & 0 & s_{\theta y} \cr s_{\theta x} s_{\theta y} & c_{\theta x} & -s_{\theta x} c_{\theta y} \cr -c_{\theta x} s_{\theta y} & s_{\theta x} & c_{\theta x} c_{\theta y} \end{pmatrix}\begin{pmatrix} c_{\theta z} & -s_{\theta z} & 0 \cr s_{\theta z} & c_{\theta z} & 0 \cr 0 & 0 & 1 \end{pmatrix} \quad &\text{(right-multiply by Eq. 1.20)} \\
> &= \begin{pmatrix} c_{\theta y} c_{\theta z} + 0\cdot s_{\theta z} + s_{\theta y}\cdot 0 & -c_{\theta y} s_{\theta z} + 0\cdot c_{\theta z} + s_{\theta y}\cdot 0 & c_{\theta y}\cdot 0 + 0\cdot 0 + s_{\theta y}\cdot 1 \cr s_{\theta x} s_{\theta y} c_{\theta z} + c_{\theta x} s_{\theta z} + (-s_{\theta x} c_{\theta y})\cdot 0 & -s_{\theta x} s_{\theta y} s_{\theta z} + c_{\theta x} c_{\theta z} + (-s_{\theta x} c_{\theta y})\cdot 0 & s_{\theta x} s_{\theta y}\cdot 0 + c_{\theta x}\cdot 0 + (-s_{\theta x} c_{\theta y})\cdot 1 \cr -c_{\theta x} s_{\theta y} c_{\theta z} + s_{\theta x} s_{\theta z} + c_{\theta x} c_{\theta y}\cdot 0 & c_{\theta x} s_{\theta y} s_{\theta z} + s_{\theta x} c_{\theta z} + c_{\theta x} c_{\theta y}\cdot 0 & -c_{\theta x} s_{\theta y}\cdot 0 + s_{\theta x}\cdot 0 + c_{\theta x} c_{\theta y}\cdot 1 \end{pmatrix} \quad &\text{(row $m$ times column $n$)} \\
> &= \begin{pmatrix} c_{\theta y} c_{\theta z} & -c_{\theta y} s_{\theta z} & s_{\theta y} \cr s_{\theta x} s_{\theta y} c_{\theta z} + c_{\theta x} s_{\theta z} & c_{\theta x} c_{\theta z} - s_{\theta x} s_{\theta y} s_{\theta z} & -s_{\theta x} c_{\theta y} \cr s_{\theta x} s_{\theta z} - c_{\theta x} s_{\theta y} c_{\theta z} & s_{\theta x} c_{\theta z} + c_{\theta x} s_{\theta y} s_{\theta z} & c_{\theta x} c_{\theta y} \end{pmatrix} \quad &\text{(drop the zero products and order the terms)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_3] = \begin{bmatrix} c_{\theta y} c_{\theta z} & -c_{\theta y} s_{\theta z} & s_{\theta y} \\ s_{\theta x} s_{\theta y} c_{\theta z} + c_{\theta x} s_{\theta z} & c_{\theta x} c_{\theta z} - s_{\theta x} s_{\theta y} s_{\theta z} & -s_{\theta x} c_{\theta y} \\ s_{\theta x} s_{\theta z} - c_{\theta x} s_{\theta y} c_{\theta z} & s_{\theta x} c_{\theta z} + c_{\theta x} s_{\theta y} s_{\theta z} & c_{\theta x} c_{\theta y} \end{bmatrix}}$$
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
> \big([{}_0R_3][{}_0R_3]^T\big)_{11} &= c_{\theta y}^2c_{\theta z}^2 + c_{\theta y}^2s_{\theta z}^2 + s_{\theta y}^2 \quad &\text{(row 1 times row 1)} \\
> &= c_{\theta y}^2\left(c_{\theta z}^2+s_{\theta z}^2\right) + s_{\theta y}^2 \quad &\text{(factor $c_{\theta y}^2$)} \\
> &= c_{\theta y}^2 + s_{\theta y}^2 \quad &\text{(Pythagoras for $\theta_z$)} \\
> &= 1 \quad &\text{(Pythagoras for $\theta_y$)} \\
> \big([{}_0R_3][{}_0R_3]^T\big)_{12} &= c_{\theta y}c_{\theta z}\left(s_{\theta x}s_{\theta y}c_{\theta z} + c_{\theta x}s_{\theta z}\right) - c_{\theta y}s_{\theta z}\left(c_{\theta x}c_{\theta z} - s_{\theta x}s_{\theta y}s_{\theta z}\right) - s_{\theta y}\,s_{\theta x}c_{\theta y} \quad &\text{(row 1 times row 2)} \\
> &= s_{\theta x}s_{\theta y}c_{\theta y}c_{\theta z}^2 + c_{\theta x}c_{\theta y}c_{\theta z}s_{\theta z} - c_{\theta x}c_{\theta y}c_{\theta z}s_{\theta z} + s_{\theta x}s_{\theta y}c_{\theta y}s_{\theta z}^2 - s_{\theta x}s_{\theta y}c_{\theta y} \quad &\text{(expand the products)} \\
> &= s_{\theta x}s_{\theta y}c_{\theta y}\left(c_{\theta z}^2+s_{\theta z}^2\right) - s_{\theta x}s_{\theta y}c_{\theta y} \quad &\text{(the $c_{\theta x}$ terms cancel; factor the rest)} \\
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
> &= \begin{pmatrix} 1\cdot 0 + 0\cdot 0 + 0\cdot 1 \cr 0\cdot 0 + c_{\theta x}\cdot 0 + (-s_{\theta x})\cdot 1 \cr 0\cdot 0 + s_{\theta x}\cdot 0 + c_{\theta x}\cdot 1 \end{pmatrix}_1 \quad &\text{(rows of Eq. 1.18 times the column)} \\
> &= \begin{pmatrix} 0 \cr -s_{\theta x} \cr c_{\theta x} \end{pmatrix}_1 \quad &\text{(third column of Eq. 1.18: $\mathbf k_2 = -s_{\theta x}\,\mathbf j_1 + c_{\theta x}\,\mathbf k_1$)} \\
> [\mathbf k_2]_0 &= [{}_0R_1(z,\theta_z)]\,[\mathbf k_2]_1 \quad &\text{(Eq. 1.12 from $\mathcal B_1$ to $\mathcal B_0$)} \\
> &= \begin{pmatrix} c_{\theta z}\cdot 0 + (-s_{\theta z})(-s_{\theta x}) + 0\cdot c_{\theta x} \cr s_{\theta z}\cdot 0 + c_{\theta z}(-s_{\theta x}) + 0\cdot c_{\theta x} \cr 0\cdot 0 + 0\cdot(-s_{\theta x}) + 1\cdot c_{\theta x} \end{pmatrix}_0 \quad &\text{(rows of Eq. 1.20 times the column)} \\
> &= \begin{pmatrix} s_{\theta z} s_{\theta x} \cr -c_{\theta z} s_{\theta x} \cr c_{\theta x} \end{pmatrix}_0 \quad &\text{(drop the zero products)} \\
> \lVert\mathbf k_2\rVert^2 &= s_{\theta z}^2s_{\theta x}^2 + c_{\theta z}^2s_{\theta x}^2 + c_{\theta x}^2 \quad &\text{(sum of the squared components)} \\
> &= s_{\theta x}^2\left(s_{\theta z}^2 + c_{\theta z}^2\right) + c_{\theta x}^2 \quad &\text{(factor $s_{\theta x}^2$)} \\
> &= s_{\theta x}^2 + c_{\theta x}^2 \quad &\text{(Pythagoras for $\theta_z$)} \\
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
> [\mathbf k_{1'}]_0 &= \begin{pmatrix} 0 \cr -s_{\theta x} \cr c_{\theta x} \end{pmatrix}_0 \quad &\text{(third column of Eq. 1.18)} \\
> [\mathbf k_2]_0 - [\mathbf k_{2'}]_0 &= \begin{pmatrix} s_{\theta z} s_{\theta x} \cr -c_{\theta z} s_{\theta x} + s_{\theta x} \cr 0 \end{pmatrix}_0 \quad &\text{(subtract from the previous result)} \\
> &= s_{\theta x}\begin{pmatrix} s_{\theta z} \cr 1 - c_{\theta z} \cr 0 \end{pmatrix}_0 \quad &\text{(factor $s_{\theta x}$)} \\
> s_{\theta z} = 0 \ \text{and}\ 1 - c_{\theta z} = 0 &\iff \theta_z = 2\pi n,\ n \in \mathbb Z \quad &\text{(the column vanishes only where the sine is zero and the cosine is one)}
> \end{aligned}$$
>
> $$\boxed{\mathbf k_{2'} = -\sin\theta_x\,\mathbf j_0 + \cos\theta_x\,\mathbf k_0 \neq \mathbf k_2\quad\text{unless } \sin\theta_x = 0 \text{ or } \theta_z = 2\pi n,\ n \in \mathbb Z}$$
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
> The base is the parallelogram of $\mathbf A$ and $\mathbf B$, of area $\lVert\mathbf A\times\mathbf B\rVert$ and unit normal $\mathbf n$ along $\mathbf A\times\mathbf B$. The height is the leg along $\mathbf n$ of the right triangle whose hypotenuse is $\mathbf C$; call $\gamma_C$ the angle between $\mathbf C$ and $\mathbf n$.
>
> $$\begin{aligned}
> \mathbf C\cdot(\mathbf A\times\mathbf B) &= \lVert\mathbf A\times\mathbf B\rVert\;C\cos\gamma_C \quad &\text{(Eq. 1.24)} \\
> C\cos\gamma_C &= \pm\,\text{height} \quad &\text{(leg adjacent to $\gamma_C$; positive when $\mathbf C$ is on the side of $\mathbf n$)} \\
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

The differential change of a vector is a vector, with magnitude and direction, and the differential of a tensor is a tensor; so the derivative with respect to time of a vector function of time is again a vector (Notes.pdf, Sec. 1.7). In this chapter there is a single observer, for whom the vectors of $\mathcal B_0$ do not change; how the derivative depends on the observer is introduced with the frames of Chapter 2 (Section 9 of this note) and developed in Chapter 3 ([Lecture 1, Slide 10]; Notes.pdf, p. 28, footnote 10). The derivative is defined as the limit of Eq. 1.51:

| Definition (Eq. 1.51) |
| :--- |
| $\dfrac{d\mathbf A}{dt} = \displaystyle\lim_{\Delta t\to 0}\frac{\mathbf A(t+\Delta t) - \mathbf A(t)}{\Delta t}$ |

Vector differentiation follows the rules of scalar differentiation for addition, multiplication by a scalar and the products, keeping the order of the factors of a cross product. The notes list them at the end of Notes.pdf, Sec. 1.7.1; they are listed here first because the boxes below use them:

| Rule | Equation |
| :--- | :--- |
| $d(\lambda\mathbf A) = d\lambda\,\mathbf A + \lambda\,d\mathbf A$ | Eq. 1.64 |
| $d(\mathbf A + \mathbf B) = d\mathbf A + d\mathbf B$ | Eq. 1.65 |
| $d(\mathbf A\cdot\mathbf B) = d\mathbf A\cdot\mathbf B + \mathbf A\cdot d\mathbf B$ | Eq. 1.66 |
| $d(\mathbf A\times\mathbf B) = d\mathbf A\times\mathbf B + \mathbf A\times d\mathbf B$ | Eq. 1.67 |

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

[Lecture 1, Slide 9] splits a general differential into both parts at once (the slide calls the vector $\mathbf b$; here it keeps the name $\mathbf A$, because $\mathbf e_b$ is the binormal from Section 12 on):

> [!derivation] Parallel and perpendicular parts of the differential of a vector
> **Law:** differential of a product; the unit vector has constant magnitude
> **Source:** [Lecture 1, Slide 9]; Notes.pdf, Eq. 1.64; Notes.pdf, Eq. 1.66
>
> $$\begin{aligned}
> \mathbf A &= A\,\mathbf e_A \quad &\text{(magnitude times unit vector)} \\
> d\mathbf A &= (dA)\,\mathbf e_A + A\,(d\mathbf e_A) \quad &\text{(differential of a product, Eq. 1.64)} \\
> \mathbf e_A\cdot d\mathbf A &= dA\;\mathbf e_A\cdot\mathbf e_A + A\;\mathbf e_A\cdot d\mathbf e_A \quad &\text{(dot-multiply by $\mathbf e_A$)} \\
> &= dA + A\;\mathbf e_A\cdot d\mathbf e_A \quad &\text{($\mathbf e_A\cdot\mathbf e_A = 1$)} \\
> \mathbf e_A\cdot d\mathbf e_A &= \tfrac{1}{2}\,d(\mathbf e_A\cdot\mathbf e_A) \quad &\text{(Eq. 1.66 with both factors $\mathbf e_A$)} \\
> &= \tfrac{1}{2}\,d(1) \quad &\text{($\mathbf e_A$ is a unit vector)} \\
> &= 0 \quad &\text{(differential of a constant)} \\
> \mathbf e_A\cdot d\mathbf A &= dA \quad &\text{(substitute in the fourth row)}
> \end{aligned}$$
>
> $$\boxed{d\mathbf A = (d\mathbf A)_\parallel + (d\mathbf A)_\perp,\qquad (d\mathbf A)_\parallel = dA\,\mathbf e_A,\qquad (d\mathbf A)_\perp = A\,d\mathbf e_A}$$
>
> **Units:** $[\mathbf A]$ in every term
> **Meaning:** the component of $d\mathbf A$ along $\mathbf e_A$ is the change of magnitude and the part perpendicular to $\mathbf e_A$ is the change of direction ([Lecture 1, Slide 9]).

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
> [R_z][R_y] &= \begin{pmatrix} 1\cdot 1 + (-d\theta_z)\cdot 0 + 0\cdot(-d\theta_y) & 1\cdot 0 + (-d\theta_z)\cdot 1 + 0\cdot 0 & 1\cdot d\theta_y + (-d\theta_z)\cdot 0 + 0\cdot 1 \cr d\theta_z\cdot 1 + 1\cdot 0 + 0\cdot(-d\theta_y) & d\theta_z\cdot 0 + 1\cdot 1 + 0\cdot 0 & d\theta_z\cdot d\theta_y + 1\cdot 0 + 0\cdot 1 \cr 0\cdot 1 + 0\cdot 0 + 1\cdot(-d\theta_y) & 0\cdot 0 + 0\cdot 1 + 1\cdot 0 & 0\cdot d\theta_y + 0\cdot 0 + 1\cdot 1 \end{pmatrix} \quad &\text{(row $m$ of $[R_z]$ times column $n$ of $[R_y]$)} \\
> &= \begin{pmatrix} 1 & -d\theta_z & d\theta_y \cr d\theta_z & 1 & d\theta_z d\theta_y \cr -d\theta_y & 0 & 1 \end{pmatrix} \quad &\text{(drop the zero products)} \\
> [R_z][R_y][R_x] &= \begin{pmatrix} 1\cdot 1 + (-d\theta_z)\cdot 0 + d\theta_y\cdot 0 & 1\cdot 0 + (-d\theta_z)\cdot 1 + d\theta_y\cdot d\theta_x & 1\cdot 0 + (-d\theta_z)(-d\theta_x) + d\theta_y\cdot 1 \cr d\theta_z\cdot 1 + 1\cdot 0 + d\theta_z d\theta_y\cdot 0 & d\theta_z\cdot 0 + 1\cdot 1 + d\theta_z d\theta_y\cdot d\theta_x & d\theta_z\cdot 0 + 1\cdot(-d\theta_x) + d\theta_z d\theta_y\cdot 1 \cr (-d\theta_y)\cdot 1 + 0\cdot 0 + 1\cdot 0 & (-d\theta_y)\cdot 0 + 0\cdot 1 + 1\cdot d\theta_x & (-d\theta_y)\cdot 0 + 0\cdot(-d\theta_x) + 1\cdot 1 \end{pmatrix} \quad &\text{(right-multiply by $[R_x]$: row $m$ times column $n$)} \\
> &= \begin{pmatrix} 1 & -d\theta_z + d\theta_y d\theta_x & d\theta_y + d\theta_z d\theta_x \cr d\theta_z & 1 + d\theta_z d\theta_y d\theta_x & -d\theta_x + d\theta_z d\theta_y \cr -d\theta_y & d\theta_x & 1 \end{pmatrix} \quad &\text{(drop the zero products)} \\
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

## 9. Reference frames

Kinematics describes the motion of bodies without considering the forces that cause it: it expresses positions, velocities and accelerations as functions of useful variables, or coordinates, relates them in different reference frames and identifies the constraints of the system. Solving the kinematics is always the first step of a problem in mechanics (Notes.pdf, Ch. 2). From here on the note follows Chapter 2 of the notes and [Lecture 1, Slides 8-28]. See also [[Concept - Cartesian Cylindrical and Spherical Coordinate Systems]], [[Concept - Intrinsic Frenet-Serret Frame and Intrinsic Acceleration]] and [[Concept - Degrees of Freedom Generalized Coordinates and Constraints]].

The motion of an object can only be described relative to something else: other bodies, or a set of space-time coordinates. The description of motion only makes sense relative to a reference frame, which represents an observer, a virtual person located in space with a certain orientation and a certain state of linear motion and rotation (Notes.pdf, Sec. 2.1; [Lecture 1, Slide 8]). For all practical purposes a reference frame is the combination of a point, the origin, and an orthonormal right-handed vector basis:

| Element | Role ([Lecture 1, Slide 8]) |
| :--- | :--- |
| $S_0 : \{O;\mathcal B_0\}$, also written $Oxyz$ (Eq. 2.1) | the reference frame |
| origin $O$ | the point from which the observer measures the position of every other point of space |
| basis $\mathcal B_0 : \{\mathbf i,\mathbf j,\mathbf k\}$ | the orientation (attitude) of the observer in space and its rotation |
| axes $Ox$, $Oy$, $Oz$ and planes $Oxy$, $Oxz$, $Oyz$ | defined naturally by $O$ and the directions of $\mathcal B_0$ |

When there is more than one frame, subindices remove the ambiguity. For a second frame $S_1 : \{O_1;\mathcal B_1\}$, the linear motion of the observer mounted on $S_1$ is the evolution in time of the position of $O_1$ as seen from $S_0$, and its rotation is the evolution in time of the vectors of $\mathcal B_1$ with respect to $\mathcal B_0$; both must be given to define $S_1$ fully with respect to $S_0$ (Notes.pdf, Sec. 2.1). It is sometimes useful to think of a frame as the whole Euclidean space moving with the observer. Frames are often attached to a rigid body (a rotating platform, the chassis of an aircraft, the Earth, the Sun): the observer moves with that body and has its rotation; the notes add that later in the course a reference frame and a rigid body are identified with each other (Notes.pdf, Sec. 2.1; the pointer to the rigid body part, Topics 6 to 8, is this note's own). Frames of relativistic mechanics, where space-time is not absolute, are not covered (Notes.pdf, Sec. 2.1, footnote 9).

![[attachments/EM-T/t1-reference-frames.svg]]

### The observer matters: time derivatives in a frame

The differential, and therefore the rate of change, of a vector depends on the frame it is observed from: an observer of $S_1$ sees the vectors of $\mathcal B_1$ fixed, while the observer of $S_0$ sees them turn. The frame in which a derivative is taken is written as a subindex on the derivative, and in general the derivatives of one vector in $S_0$ and in $S_1$ differ ([Lecture 1, Slide 10]). The vectors of $\mathcal B_0$ do not vary in $S_0$.

> [!derivation] Derivative in S0 of a vector given in the basis of S0
> **Law:** sum and product rules of differentiation; the vectors of $\mathcal B_0$ are constant for the observer of $S_0$
> **Source:** [Lecture 1, Slide 10]; Notes.pdf, Eq. 1.64; Notes.pdf, Eq. 1.65
>
> $$\begin{aligned}
> \mathbf b &= b_{x0}\,\mathbf i_0 + b_{y0}\,\mathbf j_0 + b_{z0}\,\mathbf k_0 \quad &\text{(components in $\mathcal B_0$, Eq. 1.6)} \\
> \left.\frac{d\mathbf b}{dt}\right|_0 &= \frac{db_{x0}}{dt}\,\mathbf i_0 + b_{x0}\left.\frac{d\mathbf i_0}{dt}\right|_0 + \frac{db_{y0}}{dt}\,\mathbf j_0 + b_{y0}\left.\frac{d\mathbf j_0}{dt}\right|_0 + \frac{db_{z0}}{dt}\,\mathbf k_0 + b_{z0}\left.\frac{d\mathbf k_0}{dt}\right|_0 \quad &\text{(sum rule, Eq. 1.65, and product rule, Eq. 1.64, on each term)} \\
> &= \frac{db_{x0}}{dt}\,\mathbf i_0 + \frac{db_{y0}}{dt}\,\mathbf j_0 + \frac{db_{z0}}{dt}\,\mathbf k_0 \quad &\text{(the derivatives of $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$ in $S_0$ are $\mathbf 0$)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf b}{dt}\right|_0 = \frac{db_{x0}}{dt}\,\mathbf i_0 + \frac{db_{y0}}{dt}\,\mathbf j_0 + \frac{db_{z0}}{dt}\,\mathbf k_0}$$
>
> **Units:** $[\mathbf b][\mathrm{T^{-1}}]$ in every term; the unit vectors are dimensionless
> **Meaning:** in the basis of the observer the derivative of a vector is the vector of the derivatives of its components; the derivatives of the scalar components are the same for every observer, and only the derivatives of the unit vectors can differ.

When the components of $\mathbf b$ are known in $\mathcal B_1$, the vectors $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ may rotate as seen from $S_0$ and their derivatives in $S_0$ must be kept ([Lecture 1, Slide 11]). Writing those derivatives with Eq. 1.62 gives the relation between the derivatives taken by the two observers; Chapter 3 of the notes (Topic 5) derives it in full and builds relative motion on it, and it is anticipated here because it explains why the frame subindex is never dropped when two frames are in use.

> [!derivation] Derivative in S0 of a vector given in the basis of S1 (anticipated from Notes.pdf, Ch. 3)
> **Law:** product rule; Eq. 1.62 for the unit vectors of a rotating basis; linearity of the cross product
> **Source:** [Lecture 1, Slide 11]; Notes.pdf, Eq. 3.2; Notes.pdf, Eq. 3.6; Notes.pdf, Eq. 3.7; Notes.pdf, Eq. 3.8; Notes.pdf, Eq. 1.62
>
> $\mathcal B_1$ rotates with the angular velocity $\boldsymbol\omega_{10}$ with respect to $S_0$; its unit vectors have constant magnitude, so each one rotates with $\boldsymbol\omega_{10}$ as seen from $S_0$.
>
> $$\begin{aligned}
> \mathbf b &= b_{x1}\,\mathbf i_1 + b_{y1}\,\mathbf j_1 + b_{z1}\,\mathbf k_1 \quad &\text{(the same vector, components in $\mathcal B_1$)} \\
> \left.\frac{d\mathbf b}{dt}\right|_0 &= \frac{db_{x1}}{dt}\,\mathbf i_1 + \frac{db_{y1}}{dt}\,\mathbf j_1 + \frac{db_{z1}}{dt}\,\mathbf k_1 + b_{x1}\left.\frac{d\mathbf i_1}{dt}\right|_0 + b_{y1}\left.\frac{d\mathbf j_1}{dt}\right|_0 + b_{z1}\left.\frac{d\mathbf k_1}{dt}\right|_0 \quad &\text{(sum and product rules; the vectors of $\mathcal B_1$ are not constant in $S_0$, Eq. 3.2)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \boldsymbol\omega_{10}\times\mathbf i_1,\quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \boldsymbol\omega_{10}\times\mathbf j_1,\quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \boldsymbol\omega_{10}\times\mathbf k_1 \quad &\text{(Eq. 1.62 for each unit vector, Eqs. 3.3 to 3.5)} \\
> b_{x1}\left.\frac{d\mathbf i_1}{dt}\right|_0 + b_{y1}\left.\frac{d\mathbf j_1}{dt}\right|_0 + b_{z1}\left.\frac{d\mathbf k_1}{dt}\right|_0 &= b_{x1}\,\boldsymbol\omega_{10}\times\mathbf i_1 + b_{y1}\,\boldsymbol\omega_{10}\times\mathbf j_1 + b_{z1}\,\boldsymbol\omega_{10}\times\mathbf k_1 \quad &\text{(substitute the previous row)} \\
> &= \boldsymbol\omega_{10}\times\left(b_{x1}\,\mathbf i_1 + b_{y1}\,\mathbf j_1 + b_{z1}\,\mathbf k_1\right) \quad &\text{(linearity of the cross product, Eq. 1.32)} \\
> &= \boldsymbol\omega_{10}\times\mathbf b \quad &\text{(the first row, Eq. 3.6)} \\
> \frac{db_{x1}}{dt}\,\mathbf i_1 + \frac{db_{y1}}{dt}\,\mathbf j_1 + \frac{db_{z1}}{dt}\,\mathbf k_1 &= \left.\frac{d\mathbf b}{dt}\right|_1 \quad &\text{(the box above written for $S_1$, whose vectors are constant for its own observer, Eq. 3.7)} \\
> \left.\frac{d\mathbf b}{dt}\right|_0 &= \left.\frac{d\mathbf b}{dt}\right|_1 + \boldsymbol\omega_{10}\times\mathbf b \quad &\text{(substitute the last two results in the second row, Eq. 3.8)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf b}{dt}\right|_0 = \left.\frac{d\mathbf b}{dt}\right|_1 + \boldsymbol\omega_{10}\times\mathbf b}$$
>
> **Units:** $[\mathbf b][\mathrm{T^{-1}}]$ in every term: $\boldsymbol\omega_{10}$ in $\mathrm{rad/s}$ times $[\mathbf b]$
> **Meaning:** the two observers agree on the derivative of a vector only when $\mathcal B_1$ does not rotate with respect to $\mathcal B_0$; a translation of $O_1$ does not change the orientation of $\mathcal B_1$, so it plays no role. The notes call Eq. 3.8 Coriolis theorem; the derivatives of scalars are the same in every frame (Notes.pdf, Sec. 3.1).

> [!warning] Weird hybrids
> The derivative in $S_1$ of the position vector measured from $S_0$ is a legitimate vector, but it is neither the velocity with respect to $S_0$ nor the velocity with respect to $S_1$: a velocity always pairs the position with respect to a frame with the derivative taken in that same frame ([Lecture 1, Slide 13]).

## 10. Position, velocity and acceleration

Once a reference frame $S_0 : \{O;\mathcal B_0\}$ is defined, vector calculus describes the kinematics of point particles (Notes.pdf, Sec. 2.2). The nomenclature carries the whole meaning of a kinematic vector ([Lecture 1, Slide 12]):

| Part of $\mathbf r_0^P$ | Meaning |
| :--- | :--- |
| bold $\mathbf r$ (an arrow or a bar over the symbol in handwriting) | a vector; the letter $r$ is kept for positions |
| superindex $P$ | the point or particle we refer to |
| subindex $0$ | the reference frame with respect to whose origin the vector is measured; sub- and superindex are dropped only when there is no ambiguity |

The position vectors of one point with respect to $S_0$ and to $S_1$ differ if the origins differ, and the velocities and accelerations with respect to $S_0$ and to $S_1$ differ if the origins translate or the frames rotate with respect to each other ([Lecture 1, Slides 12-13]). When $P$ moves with respect to $S_0$, its position vector is a function of time whose magnitude, direction or both change.

![[attachments/EM-T/t1-position-velocity.svg]]

> [!derivation] Velocity of a point particle with respect to S0
> **Law:** definition of velocity as the rate of change of the position, taken by the observer of $S_0$
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.3; Notes.pdf Fig. 2.1; [Lecture 1, Slide 13]
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OP} \quad &\text{(position vector of $P$ in $S_0$, Eq. 2.2)} \\
> \Delta\mathbf r_0^P &= \mathbf r_0^P(t+\Delta t) - \mathbf r_0^P(t) \quad &\text{(displacement between two consecutive instants, Fig. 2.1)} \\
> \mathbf v_0^P &= \lim_{\Delta t\to 0}\frac{(\mathbf r_0^P + \Delta\mathbf r_0^P) - \mathbf r_0^P}{\Delta t} \quad &\text{(definition of velocity, Eq. 2.3)} \\
> &= \lim_{\Delta t\to 0}\frac{\Delta\mathbf r_0^P}{\Delta t} \quad &\text{(the two $\mathbf r_0^P$ cancel)} \\
> &= \left.\frac{d\mathbf r_0^P}{dt}\right|_0 \quad &\text{(definition of the derivative, Eq. 1.51, taken in $S_0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \lim_{\Delta t\to 0}\frac{\Delta\mathbf r_0^P}{\Delta t} = \left.\frac{d\mathbf r_0^P}{dt}\right|_0}$$
>
> **Units:** $[\mathrm{L}]/[\mathrm{T}] = [\mathrm{L\,T^{-1}}]$, $\mathrm{m/s}$
> **Meaning:** as $\Delta t$ shrinks, the chord $\Delta\mathbf r_0^P$ turns into the tangent to the trajectory, so the velocity always points along the differential of the position, tangent to the path ([Lecture 1, Slide 14]). Its magnitude is the speed or celerity; calling the velocity vector just "speed" is incorrect.

> [!derivation] Acceleration of a point particle with respect to S0
> **Law:** definition of acceleration as the rate of change of the velocity, taken by the observer of $S_0$
> **Source:** Notes.pdf, Eq. 2.4; [Lecture 1, Slide 13]
>
> $$\begin{aligned}
> \Delta\mathbf v_0^P &= \mathbf v_0^P(t+\Delta t) - \mathbf v_0^P(t) \quad &\text{(change of the velocity between two instants)} \\
> \mathbf a_0^P &= \lim_{\Delta t\to 0}\frac{(\mathbf v_0^P + \Delta\mathbf v_0^P) - \mathbf v_0^P}{\Delta t} \quad &\text{(definition of acceleration, Eq. 2.4)} \\
> &= \lim_{\Delta t\to 0}\frac{\Delta\mathbf v_0^P}{\Delta t} \quad &\text{(the two $\mathbf v_0^P$ cancel)} \\
> &= \left.\frac{d\mathbf v_0^P}{dt}\right|_0 \quad &\text{(definition of the derivative, taken in $S_0$)} \\
> &= \left.\frac{d^2\mathbf r_0^P}{dt^2}\right|_0 \quad &\text{(substitute the velocity of the box above)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \left.\frac{d\mathbf v_0^P}{dt}\right|_0 = \left.\frac{d^2\mathbf r_0^P}{dt^2}\right|_0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]/[\mathrm{T}] = [\mathrm{L\,T^{-2}}]$, $\mathrm{m/s^2}$
> **Meaning:** the acceleration, like the velocity, can come from a change of magnitude, of direction or both. Higher derivatives exist but have little interest in mechanics, because Newton's laws involve only the second derivative (Notes.pdf, Sec. 2.2, footnote 11).

> [!derivation] Position, velocity and acceleration in Cartesian components
> **Law:** components in $\mathcal B_0$; derivative in $S_0$ of a vector given in $\mathcal B_0$
> **Source:** Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.7; [Lecture 1, Slide 16]
>
> $$\begin{aligned}
> \mathbf r_0^P &= x\,\mathbf i + y\,\mathbf j + z\,\mathbf k \quad &\text{(the Cartesian coordinates are the components of $\mathbf r_0^P$ in $\mathcal B_0$, Eq. 2.5)} \\
> \mathbf v_0^P &= \left.\frac{d\mathbf r_0^P}{dt}\right|_0 \quad &\text{(Eq. 2.3)} \\
> &= \dot x\,\mathbf i + \dot y\,\mathbf j + \dot z\,\mathbf k \quad &\text{(Section 9, first box: $\mathbf i$, $\mathbf j$, $\mathbf k$ do not change in $S_0$; Eq. 2.6)} \\
> \mathbf a_0^P &= \left.\frac{d\mathbf v_0^P}{dt}\right|_0 \quad &\text{(Eq. 2.4)} \\
> &= \ddot x\,\mathbf i + \ddot y\,\mathbf j + \ddot z\,\mathbf k \quad &\text{(the same rule applied to the components $\dot x$, $\dot y$, $\dot z$; Eq. 2.7)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = x\,\mathbf i + y\,\mathbf j + z\,\mathbf k,\qquad \mathbf v_0^P = \dot x\,\mathbf i + \dot y\,\mathbf j + \dot z\,\mathbf k,\qquad \mathbf a_0^P = \ddot x\,\mathbf i + \ddot y\,\mathbf j + \ddot z\,\mathbf k}$$
>
> **Units:** $\mathrm m$, $\mathrm{m/s}$ and $\mathrm{m/s^2}$ for every component of the three vectors
> **Meaning:** in Cartesian coordinates, and only in them, the coordinates equal the components of the position vector in the associated basis, so differentiating the vectors is differentiating the three coordinates ([Lecture 1, Slide 16]).

> [!derivation] Velocity and acceleration do not depend on the origin
> **Law:** head-to-tail sum of vectors; sum rule of differentiation; points fixed in $S_0$ have zero velocity in $S_0$
> **Source:** Notes.pdf, Sec. 2.2; Notes.pdf, Eq. 1.65; Notes.pdf, Eq. 2.3
>
> Let $O'$ be another point at rest in $S_0$, used as origin instead of $O$.
>
> $$\begin{aligned}
> \overrightarrow{O'P} &= \overrightarrow{O'O} + \overrightarrow{OP} \quad &\text{(head-to-tail sum)} \\
> &= \mathbf r_0^P - \overrightarrow{OO'} \quad &\text{(Eq. 2.2; reversing a vector changes its sign)} \\
> \left.\frac{d\overrightarrow{O'P}}{dt}\right|_0 &= \left.\frac{d\mathbf r_0^P}{dt}\right|_0 - \left.\frac{d\overrightarrow{OO'}}{dt}\right|_0 \quad &\text{(sum rule, Eq. 1.65)} \\
> &= \mathbf v_0^P - \mathbf 0 \quad &\text{(Eq. 2.3; $O$ and $O'$ are both at rest in $S_0$, so $\overrightarrow{OO'}$ is constant there)} \\
> \left.\frac{d^2\overrightarrow{O'P}}{dt^2}\right|_0 &= \left.\frac{d\mathbf v_0^P}{dt}\right|_0 \quad &\text{(differentiate the previous row once more)} \\
> &= \mathbf a_0^P \quad &\text{(Eq. 2.4)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\overrightarrow{O'P}}{dt}\right|_0 = \mathbf v_0^P,\qquad \left.\frac{d^2\overrightarrow{O'P}}{dt^2}\right|_0 = \mathbf a_0^P}$$
>
> **Units:** $\mathrm{m/s}$ and $\mathrm{m/s^2}$
> **Meaning:** the value of the position vector depends on the point chosen as origin, but the velocity and the acceleration depend only on the frame (the observer), not on which of its fixed points is the origin (Notes.pdf, Sec. 2.2).

Over time the velocity may change in magnitude, which goes with an acceleration parallel to the velocity, or in direction, which goes with an acceleration perpendicular to it ([Lecture 1, Slide 14]). This is Eq. 1.63 applied to the velocity vector; Section 13 makes the two parts explicit with the intrinsic basis.

## 11. Trajectory and arc length coordinate

The curve traced by $P$ as seen from $S_0$ is its trajectory or path. The path coordinate, or arc length coordinate, $s$ measures the distance travelled by the particle along the trajectory from an origin chosen arbitrarily on it (Notes.pdf, Sec. 2.3, Fig. 2.1; [Lecture 1, Slide 24]). Knowing the shape of the trajectory and the time law is equivalent to solving the motion:

| Object | What it gives |
| :--- | :--- |
| trajectory $\mathbf r_0^P = \mathbf r_0^P(s)$ | the geometric shape of the path, with each point labelled by its arc length |
| time law $s = s(t)$ | where on the path the particle is at each instant |
| motion $\mathbf r_0^P = \mathbf r_0^P(s(t))$ | the position at every instant, and from it $\mathbf v_0^P$, $\mathbf a_0^P$ and any other quantity of the motion |

The trajectory is specific to the frame from which it is observed: another observer, in a different frame, perceives a different curve for the motion of the same particle (Notes.pdf, Sec. 2.3). Quantities that depend only on the shape of the trajectory, and not on how quickly $P$ moves along it, are called path variables: the unit vectors $\mathbf e_t$, $\mathbf e_n$, $\mathbf e_b$, the curvature $\kappa$, the radius of curvature $\rho$ and the torsion $\tau$ defined in the next section ([Lecture 1, Slide 24]).

## 12. The intrinsic vector basis and reference frame

![[attachments/EM-T/t1-trajectory-triad.svg]]

> [!derivation] Tangent unit vector
> **Law:** definition of the derivative with respect to the arc length; the chord tends to the arc
> **Source:** Notes.pdf, Eq. 2.8; Notes.pdf, Eq. 2.9; [Lecture 1, Slide 25]
>
> $$\begin{aligned}
> \Delta\mathbf r_0^P &= \mathbf r_0^P(s+\Delta s) - \mathbf r_0^P(s) \quad &\text{(chord between two points of the trajectory, Eq. 2.8)} \\
> \frac{d\mathbf r_0^P}{ds} &= \lim_{\Delta s\to 0}\frac{\Delta\mathbf r_0^P}{\Delta s} \quad &\text{(definition of the derivative with respect to $s$)} \\
> \left\lvert\frac{d\mathbf r_0^P}{ds}\right\rvert &= \lim_{\Delta s\to 0}\frac{\lvert\Delta\mathbf r_0^P\rvert}{\Delta s} \quad &\text{(the magnitude of the limit is the limit of the magnitudes)} \\
> &= 1 \quad &\text{(as $\Delta s\to 0$ the chord tends to the arc, whose length is $\Delta s$ by the definition of $s$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_t \equiv \frac{d\mathbf r_0^P}{ds} = \lim_{\Delta s\to 0}\frac{\Delta\mathbf r_0^P}{\Delta s},\qquad \lvert\mathbf e_t\rvert = 1}$$
>
> **Units:** $[\mathrm L]/[\mathrm L]$, dimensionless
> **Meaning:** the direction of the chord tends to the tangent to the curve, so $\mathbf e_t$ is the unit tangent vector, pointing in the sense in which $s$ grows; it changes from point to point, so it is a function of $s$.

> [!derivation] The derivative of the tangent vector is normal to it
> **Law:** $\mathbf e_t$ has unit magnitude; differentiation of a dot product
> **Source:** Notes.pdf, Eq. 2.10; Notes.pdf, Eq. 1.66; Notes.pdf, Eq. 1.25
>
> $$\begin{aligned}
> \mathbf e_t\cdot\mathbf e_t &= 1 \quad &\text{($\mathbf e_t$ is a unit vector at every $s$)} \\
> \frac{d}{ds}\left(\mathbf e_t\cdot\mathbf e_t\right) &= \frac{d\mathbf e_t}{ds}\cdot\mathbf e_t + \mathbf e_t\cdot\frac{d\mathbf e_t}{ds} \quad &\text{(rule of Eq. 1.66, with $s$ as the variable)} \\
> &= 2\,\frac{d\mathbf e_t}{ds}\cdot\mathbf e_t \quad &\text{(commutativity of the dot product, Eq. 1.25)} \\
> \frac{d}{ds}(1) &= 0 \quad &\text{(derivative of a constant)} \\
> 2\,\frac{d\mathbf e_t}{ds}\cdot\mathbf e_t &= 0 \quad &\text{(the derivatives of both sides of the first row are equal)}
> \end{aligned}$$
>
> $$\boxed{2\,\frac{d\mathbf e_t}{ds}\cdot\mathbf e_t = 0}$$
>
> **Units:** $[\mathrm{L^{-1}}]$
> **Meaning:** the vector $d\mathbf e_t/ds$ is always perpendicular to $\mathbf e_t$, the same property as for any unit vector in Section 6: in the limit, the small change of $\mathbf e_t$ between two neighbouring points is normal to it ([Lecture 1, Slide 25]).

At each point the trajectory can be approximated locally by a circular arc, the osculating circle, of centre $C$ (the local centre of curvature) and radius $\rho$; the plane of $\mathbf e_t$ and of the normal vector defined next is the local osculating plane (Notes.pdf, Sec. 2.4, Fig. 2.2; [Lecture 1, Slide 26]).

![[attachments/EM-T/t1-osculating-circle.svg]]

> [!derivation] Normal unit vector, curvature and radius of curvature
> **Law:** normalisation of the derivative of $\mathbf e_t$; geometry of the isosceles triangle of the two tangent vectors; arc of the osculating circle
> **Source:** Notes.pdf, Eq. 2.11; Notes.pdf, Eq. 2.12; Notes.pdf Fig. 2.2; [Lecture 1, Slide 26]
>
> The tangents at $P(s)$ and $P(s+\Delta s)$ are perpendicular to the radii $CP(s)$ and $CP(s+\Delta s)$ of the osculating circle, so the angle between $\mathbf e_t(s)$ and $\mathbf e_t(s+\Delta s)$ equals the angle $\Delta\theta_t$ subtended by the arc at $C$ (the angle turned by the tangent; the notes write $\Delta\theta$) (two angles whose sides are perpendicular pair by pair). Drawn from a common origin, the two unit tangent vectors and $\Delta\mathbf e_t$ form an isosceles triangle with apex angle $\Delta\theta_t$ (detail of Fig. 2.2). Its height from the apex splits it into two right triangles of hypotenuse one, in which half of the base is the leg opposite to the half angle.
>
> $$\begin{aligned}
> \mathbf e_n &= \frac{d\mathbf e_t}{ds}\bigg/\left\lvert\frac{d\mathbf e_t}{ds}\right\rvert \quad &\text{(definition: the derivative of $\mathbf e_t$, normal to it, normalised; Eq. 2.11)} \\
> \lvert\Delta\mathbf e_t\rvert &= 2\cdot 1\cdot\sin\frac{\Delta\theta_t}{2} \quad &\text{(twice the leg opposite to $\Delta\theta_t/2$ in a right triangle of unit hypotenuse)} \\
> &= \Delta\theta_t + O(\Delta\theta_t^3) \quad &\text{(Maclaurin series of the sine, Eq. 1.69)} \\
> \Delta s &= \rho\,\Delta\theta_t \quad &\text{(arc of the osculating circle of radius $\rho$ that subtends $\Delta\theta_t$)} \\
> \left\lvert\frac{d\mathbf e_t}{ds}\right\rvert &= \lim_{\Delta s\to 0}\frac{\lvert\Delta\mathbf e_t\rvert}{\Delta s} \quad &\text{(definition of the derivative; magnitude of a limit)} \\
> &= \frac{d\theta_t}{ds} \quad &\text{(substitute $\lvert\Delta\mathbf e_t\rvert$; the cubic term vanishes in the limit)} \\
> &= \frac{1}{\rho} \quad &\text{(substitute $\Delta s = \rho\,\Delta\theta_t$)} \\
> &\equiv \kappa \quad &\text{(definition of the curvature, Eq. 2.12)} \\
> \frac{d\mathbf e_t}{ds} &= \kappa\,\mathbf e_n \quad &\text{(magnitude times unit vector, from the first row)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\mathbf e_t}{ds} = \kappa\,\mathbf e_n,\qquad \left\lvert\frac{d\mathbf e_t}{ds}\right\rvert = \frac{d\theta_t}{ds} = \frac{1}{\rho} = \kappa}$$
>
> **Units:** $\kappa$ in $[\mathrm{L^{-1}}]$ ($\mathrm{m^{-1}}$), $\rho$ in $\mathrm m$; $\mathbf e_n$ dimensionless
> **Meaning:** $\Delta\mathbf e_t$ points to the inside of the curve, so $\mathbf e_n$ always points towards the centre of the osculating circle $C$, at the distance $\rho$ from $P$. On a circular trajectory $\rho$ is constant and equal to its radius; in general $\rho$ and the osculating circle change with $s$. The magnitude of $d\mathbf e_t/ds$ is the inverse of the local radius of curvature (Notes.pdf, Sec. 2.4).

> [!warning] Straight segments
> On a straight trajectory, or a straight segment of one, the derivative of $\mathbf e_t$ vanishes and $\rho$ tends to infinity, so $\mathbf e_n$ and $\mathbf e_b$ are not defined; the intrinsic frame must then be redefined, choosing $\mathbf e_n$ along any direction perpendicular to $\mathbf e_t$ (Notes.pdf, Sec. 2.4, footnote 12; [Lecture 1, Slide 26]).

The unit vector perpendicular to the osculating plane is the binormal vector; the three unit vectors form the intrinsic vector basis at $P$, and with $P$ as origin they define the intrinsic (Frenet-Serret) reference frame (Notes.pdf, Sec. 2.4; [Lecture 1, Slide 27]).

| Definition | Equation |
| :--- | :--- |
| binormal vector $\mathbf e_b = \mathbf e_t\times\mathbf e_n$ | Sec. 2.4 |
| intrinsic vector basis $\mathcal B_F(P) : \{\mathbf e_t,\mathbf e_n,\mathbf e_b\}$ | Eq. 2.13 |
| intrinsic reference frame $S_F(P) : \{P;\mathcal B_F(P)\}$ | Eq. 2.14 |

> [!derivation] The intrinsic basis is orthonormal and right-handed
> **Law:** magnitude and direction of the cross product; cyclic property of the triple product
> **Source:** Notes.pdf, Eq. 2.13; Notes.pdf, Eq. 1.30; Notes.pdf, Sec. 1.6.2; Notes.pdf, Eq. 1.33
>
> $$\begin{aligned}
> \lvert\mathbf e_b\rvert &= \lvert\mathbf e_t\rvert\,\lvert\mathbf e_n\rvert\,\left\lvert\sin\frac{\pi}{2}\right\rvert \quad &\text{(Eq. 1.30; $\mathbf e_n$ is perpendicular to $\mathbf e_t$ by Eq. 2.10)} \\
> &= 1\cdot 1\cdot 1 \quad &\text{(both factors are unit vectors)} \\
> \mathbf e_b\cdot\mathbf e_t &= 0,\qquad \mathbf e_b\cdot\mathbf e_n = 0 \quad &\text{(a cross product is orthogonal to both of its factors, Sec. 1.6.2)} \\
> [\mathbf e_t,\mathbf e_n,\mathbf e_b] &= [\mathbf e_b,\mathbf e_t,\mathbf e_n] \quad &\text{(cyclic permutation of the triple product, Eq. 1.33)} \\
> &= \mathbf e_b\cdot(\mathbf e_t\times\mathbf e_n) \quad &\text{(definition of the triple product)} \\
> &= \mathbf e_b\cdot\mathbf e_b \quad &\text{(definition of $\mathbf e_b$)} \\
> &= 1 \quad &\text{(unit magnitude, first two rows)}
> \end{aligned}$$
>
> $$\boxed{\mathcal B_F(P) : \{\mathbf e_t,\mathbf e_n,\mathbf e_b\}\ \text{orthonormal},\qquad [\mathbf e_t,\mathbf e_n,\mathbf e_b] = +1\ \text{(right-handed)}}$$
>
> **Units:** dimensionless
> **Meaning:** the triple product of the three unit vectors is the volume of a unit cube taken with the positive sign, so the vectors follow the right-hand rule in the order tangent, normal, binormal. They depend only on $\mathbf r_0^P(s)$, not on the time law $s(t)$: they are path variables, intrinsic to the trajectory (Notes.pdf, Sec. 2.4).

The same differentiation applied to $\mathbf e_n$ and $\mathbf e_b$ gives the Frenet-Serret formulas. For a planar trajectory the notes read the result from Fig. 2.2; for a curve in space $d\mathbf e_n/ds$ gains a component along $\mathbf e_b$, whose magnitude, the torsion $\tau$, also has units of inverse length (Notes.pdf, Sec. 2.4; [Lecture 1, Slide 27]). Both follow from the definitions.

> [!derivation] Frenet-Serret formulas
> **Law:** differentiation of a cross product; orthogonality of the derivative of a unit vector; right-handed cyclic order of $\mathcal B_F(P)$
> **Source:** Notes.pdf, Eq. 2.15; Notes.pdf, Eq. 1.67; Notes.pdf, Eq. 2.12; [Lecture 1, Slide 27]
>
> In the right-handed basis $\mathcal B_F(P)$ the products of its vectors follow the cyclic order: $\mathbf e_t\times\mathbf e_n = \mathbf e_b$, $\mathbf e_n\times\mathbf e_b = \mathbf e_t$, $\mathbf e_b\times\mathbf e_t = \mathbf e_n$, and the reversed products change sign (Eq. 1.31).
>
> $$\begin{aligned}
> \frac{d\mathbf e_b}{ds} &= \frac{d\mathbf e_t}{ds}\times\mathbf e_n + \mathbf e_t\times\frac{d\mathbf e_n}{ds} \quad &\text{(derivative of $\mathbf e_t\times\mathbf e_n$, rule of Eq. 1.67)} \\
> &= \kappa\,\mathbf e_n\times\mathbf e_n + \mathbf e_t\times\frac{d\mathbf e_n}{ds} \quad &\text{(Eq. 2.12)} \\
> &= \mathbf e_t\times\frac{d\mathbf e_n}{ds} \quad &\text{($\mathbf e_n\times\mathbf e_n = \mathbf 0$)} \\
> \frac{d\mathbf e_b}{ds}\cdot\mathbf e_t &= 0 \quad &\text{(a cross product is orthogonal to its factor $\mathbf e_t$)} \\
> \frac{d\mathbf e_b}{ds}\cdot\mathbf e_b &= 0 \quad &\text{($\mathbf e_b$ is a unit vector: the steps of Eq. 2.10)} \\
> \frac{d\mathbf e_b}{ds} &= -\tau\,\mathbf e_n \quad &\text{(the only direction left is $\mathbf e_n$; this row defines the torsion $\tau$, with the sign of the notes)} \\
> \mathbf e_n &= \mathbf e_b\times\mathbf e_t \quad &\text{(cyclic order of the basis)} \\
> \frac{d\mathbf e_n}{ds} &= \frac{d\mathbf e_b}{ds}\times\mathbf e_t + \mathbf e_b\times\frac{d\mathbf e_t}{ds} \quad &\text{(rule of Eq. 1.67)} \\
> &= -\tau\,\mathbf e_n\times\mathbf e_t + \kappa\,\mathbf e_b\times\mathbf e_n \quad &\text{(substitute $d\mathbf e_b/ds$ and Eq. 2.12)} \\
> &= -\tau\,(-\mathbf e_b) + \kappa\,(-\mathbf e_t) \quad &\text{($\mathbf e_n\times\mathbf e_t = -\mathbf e_b$ and $\mathbf e_b\times\mathbf e_n = -\mathbf e_t$, reversed cyclic products)} \\
> &= -\kappa\,\mathbf e_t + \tau\,\mathbf e_b \quad &\text{(reorder)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\mathbf e_t}{ds} = \kappa\,\mathbf e_n,\qquad \frac{d\mathbf e_n}{ds} = -\kappa\,\mathbf e_t + \tau\,\mathbf e_b,\qquad \frac{d\mathbf e_b}{ds} = -\tau\,\mathbf e_n}$$
>
> **Units:** $[\mathrm{L^{-1}}]$ in every term: $\kappa$ and $\tau$ in $\mathrm{m^{-1}}$
> **Meaning:** on a planar trajectory the osculating plane is the plane of the curve, so $\mathbf e_b$ is constant, $\tau$ is zero and the normal vector turns back along the tangent at the rate $\kappa$; on a curve in space the torsion measures how fast the osculating plane twists about the tangent.

The trajectory is specific to the frame $S_0$, so the intrinsic basis and frame also depend on the frame of observation; a subindex $0$ would show it, but using these concepts in two frames at once is unusual, and the notes drop it for $s$, $\mathbf r_0^P(s)$ and the intrinsic vectors (Notes.pdf, Sec. 2.4).

## 13. Velocity and acceleration in the intrinsic basis

With a single frame $S_0$ the derivatives are taken in $S_0$ and the frame subindex of the derivative is dropped; the chain rule through the time law gives the components of the velocity and the acceleration in the intrinsic basis (Notes.pdf, Sec. 2.5; [Lecture 1, Slide 28]).

> [!derivation] Velocity in the intrinsic basis
> **Law:** definition of velocity; chain rule through the time law
> **Source:** Notes.pdf, Eq. 2.16; Notes.pdf, Eq. 2.9; [Lecture 1, Slide 28]
>
> $$\begin{aligned}
> \mathbf v_0^P &= \frac{d\mathbf r_0^P}{dt} \quad &\text{(Eq. 2.3, single frame)} \\
> &= \frac{d\mathbf r_0^P}{ds}\,\frac{ds}{dt} \quad &\text{(chain rule: $\mathbf r_0^P = \mathbf r_0^P(s(t))$)} \\
> &= \dot s\,\mathbf e_t \quad &\text{(Eq. 2.9)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \dot s\,\mathbf e_t,\qquad \dot s \equiv v \ \text{($s$ measured in the sense of motion)}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$: $\dot s$ in $\mathrm{m/s}$ times a dimensionless unit vector
> **Meaning:** the velocity is always tangent to the path and has no normal or binormal component. The identification of $\dot s$ with the speed $v$, which is never negative, is the convention of Notes.pdf, Eq. 2.16: the arc length grows in the sense in which the particle travels. If $s$ is measured the other way, $\dot s$ is negative and the speed is its absolute value, while $\dot s\,\mathbf e_t$ is still the velocity. $\mathbf e_t$ depends only on the shape of the trajectory, not on how fast it is travelled.

> [!derivation] Acceleration in the intrinsic basis
> **Law:** definition of acceleration; product rule; chain rule for $\mathbf e_t(s(t))$; Eq. 2.12
> **Source:** Notes.pdf, Eq. 2.17; Notes.pdf, Eq. 2.18; Notes.pdf, Eq. 2.12; [Lecture 1, Slide 28]
>
> $$\begin{aligned}
> \mathbf a_0^P &= \frac{d}{dt}\left(\dot s\,\mathbf e_t\right) \quad &\text{(Eq. 2.4 applied to Eq. 2.16)} \\
> &= \ddot s\,\mathbf e_t + \dot s\,\frac{d\mathbf e_t}{dt} \quad &\text{(product rule, Eq. 1.64)} \\
> \frac{d\mathbf e_t}{dt} &= \frac{d\mathbf e_t}{ds}\,\frac{ds}{dt} \quad &\text{(chain rule: $\mathbf e_t = \mathbf e_t(s(t))$)} \\
> &= \kappa\,\dot s\,\mathbf e_n \quad &\text{(Eq. 2.12)} \\
> \mathbf a_0^P &= \ddot s\,\mathbf e_t + \dot s\,\kappa\,\dot s\,\mathbf e_n \quad &\text{(substitute in the second row)} \\
> &= \ddot s\,\mathbf e_t + \frac{\dot s^2}{\rho}\,\mathbf e_n \quad &\text{($\kappa = 1/\rho$, Eq. 2.12)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \ddot s\,\mathbf e_t + \frac{\dot s^2}{\rho}\,\mathbf e_n,\qquad a_t = \ddot s,\qquad a_n = \frac{\dot s^2}{\rho} \equiv \frac{v^2}{\rho}}$$
>
> **Units:** $a_t$: $[\mathrm{L\,T^{-2}}]$; $a_n$: $[\mathrm{L\,T^{-1}}]^2/[\mathrm L] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the tangential acceleration comes from the change of the speed and the normal acceleration from the turning of $\mathbf e_t$, the change of direction of the velocity; $a_n$ is never negative, so the normal part always points towards the centre of curvature.

The two results reveal the structure of the motion along its path (Notes.pdf, Sec. 2.5; [Lecture 1, Slide 28]):

- The velocity is always tangent to the path: its normal and binormal components are always zero.
- The acceleration can have a tangential and a normal component, but never a binormal one.
- The velocity and the acceleration always lie in the osculating plane of $\mathbf e_t$ and $\mathbf e_n$.
- The osculating plane is constant only if the path is planar; otherwise it twists around the tangent as the particle moves, because of the torsion.
- The tangential component $a_t$ is related to changes of the speed: if it is zero, the speed is constant.
- The normal component $a_n$ is related to changes of the direction of the velocity: if it is zero, the direction of travel is constant.
- Both components are non-zero unless the speed is constant (then $a_t$ vanishes), the path is straight (then $\rho$ tends to infinity and $a_n$ vanishes) or the particle is momentarily at rest (then $a_n$ vanishes).

### Planar problems in path variables

In planar problems the data are sometimes conditions on the velocity, the acceleration, its tangential or normal component, or the radius of curvature, and the task is to obtain the trajectory and the time law, that is, to solve the motion. With the trajectory in the plane $Oxy$, its Cartesian components follow by integration once the angle $\theta_t$ that the tangent forms with $Ox$ is known as a function of $s$ (Notes.pdf, Sec. 2.5.1, Fig. 2.3).

![[attachments/EM-T/t1-path-angle.svg]]

> [!derivation] Differentials of the coordinates in terms of the arc length
> **Law:** the unit tangent at the angle $\theta_t$ from $Ox$; $d\mathbf r_0^P$ along $\mathbf e_t$ with length $ds$
> **Source:** Notes.pdf, Eq. 2.19; Notes.pdf, Eq. 2.9; Notes.pdf Fig. 2.3; Notes.pdf, Eq. 1.3; Notes.pdf, Eq. 1.4
>
> View with $\mathbf k$ out of the paper (⊙), $\mathbf i$ to the right, $\mathbf j$ up; $\theta_t$ is measured counterclockwise from $Ox$ to $\mathbf e_t$. The differential element is the hypotenuse $ds$ of a right triangle with the leg $dx$ adjacent to $\theta_t$ and the leg $dy$ opposite to it (Fig. 2.3).
>
> $$\begin{aligned}
> \mathbf e_t &= \cos\theta_t\,\mathbf i + \sin\theta_t\,\mathbf j \quad &\text{(unit vector at $\theta_t$ from $Ox$: adjacent leg along $\mathbf i$, opposite leg along $\mathbf j$, Eqs. 1.3 and 1.4)} \\
> d\mathbf r_0^P &= \mathbf e_t\,ds \quad &\text{(Eq. 2.9 multiplied by $ds$)} \\
> dx\,\mathbf i + dy\,\mathbf j &= \cos\theta_t\,ds\,\mathbf i + \sin\theta_t\,ds\,\mathbf j \quad &\text{(differential of $\mathbf r_0^P = x\,\mathbf i + y\,\mathbf j$ on the left; substitute $\mathbf e_t$ on the right)} \\
> dx &= ds\cos\theta_t,\qquad dy = ds\sin\theta_t \quad &\text{(components are unique, Eq. 1.9)}
> \end{aligned}$$
>
> $$\boxed{dx = ds\cos\theta_t,\qquad dy = ds\sin\theta_t}$$
>
> **Units:** $\mathrm m$ in every term
> **Meaning:** marching along the path, each element $ds$ adds its projections on the two axes; the shape of the path is fixed once $\theta_t(s)$ is known.

> [!derivation] Relations among the path variables in the plane
> **Law:** chain rule on $\mathbf e_t(\theta_t(s))$; Eqs. 2.12, 2.16 and 2.18
> **Source:** Notes.pdf, Eq. 2.20; Notes.pdf, Eq. 2.12; Notes.pdf, Eq. 2.16; Notes.pdf, Eq. 2.18
>
> $$\begin{aligned}
> \frac{d\mathbf e_t}{ds} &= \frac{d\cos\theta_t}{d\theta_t}\,\frac{d\theta_t}{ds}\,\mathbf i + \frac{d\sin\theta_t}{d\theta_t}\,\frac{d\theta_t}{ds}\,\mathbf j \quad &\text{(chain rule; $\mathbf i$ and $\mathbf j$ are constant)} \\
> &= -\sin\theta_t\,\frac{d\theta_t}{ds}\,\mathbf i + \cos\theta_t\,\frac{d\theta_t}{ds}\,\mathbf j \quad &\text{(derivatives of the cosine and the sine)} \\
> &= \frac{d\theta_t}{ds}\left(-\sin\theta_t\,\mathbf i + \cos\theta_t\,\mathbf j\right) \quad &\text{(factor the common scalar)} \\
> \left\lvert\frac{d\mathbf e_t}{ds}\right\rvert &= \left\lvert\frac{d\theta_t}{ds}\right\rvert\sqrt{\sin^2\theta_t + \cos^2\theta_t} \quad &\text{(magnitude: Pythagoras on the components)} \\
> &= \left\lvert\frac{d\theta_t}{ds}\right\rvert \quad &\text{($\sin^2 + \cos^2 = 1$)} \\
> \kappa &= \frac{d\theta_t}{ds} \quad &\text{(Eq. 2.12, for a path that turns counterclockwise, with $\theta_t$ growing along $s$)}
> \end{aligned}$$
>
> $$\boxed{v = \dot s,\qquad a_t = \dot v = \ddot s,\qquad a_n = \frac{v^2}{\rho},\qquad \frac{d\theta_t}{ds} = \kappa = \frac{1}{\rho}}$$
>
> **Units:** $v$ in $\mathrm{m/s}$; $a_t$ and $a_n$ in $\mathrm{m/s^2}$; $d\theta_t/ds$ and $\kappa$ in $\mathrm{rad/m}$
> **Meaning:** the vector in brackets is $\mathbf e_t$ turned a quarter turn counterclockwise, which is $\mathbf e_n$ when the path turns counterclockwise; for a path that turns clockwise $\theta_t$ decreases along $s$, its rate is $-\kappa$ and $\mathbf e_n$ is $\mathbf e_t$ turned clockwise. The relations of Eq. 2.20 link the data of a problem with $\theta_t(s)$ and $s(t)$.

> [!derivation] Trajectory from the angle of the tangent
> **Law:** integration of Eq. 2.19 along the path; Barrow's rule
> **Source:** Notes.pdf, Eq. 2.19; Notes.pdf, Sec. 2.5.1
>
> $$\begin{aligned}
> \frac{dx}{ds'} &= \cos\theta_t(s') \quad &\text{(Eq. 2.19 divided by $ds'$; $s'$ is the integration variable)} \\
> \int_{s_0}^{s}\frac{dx}{ds'}\,ds' &= \int_{s_0}^{s}\cos\theta_t(s')\,ds' \quad &\text{(integrate both sides from $s_0$ to $s$)} \\
> \left[\,x\,\right]_{s_0}^{s} &= \int_{s_0}^{s}\cos\theta_t(s')\,ds' \quad &\text{(an antiderivative of $dx/ds'$ is $x$)} \\
> x(s) - x(s_0) &= \int_{s_0}^{s}\cos\theta_t(s')\,ds' \quad &\text{(Barrow's rule)} \\
> y(s) - y(s_0) &= \int_{s_0}^{s}\sin\theta_t(s')\,ds' \quad &\text{(the same three steps with $dy = ds\sin\theta_t$)}
> \end{aligned}$$
>
> $$\boxed{x(s) = x(s_0) + \int_{s_0}^{s}\cos\theta_t(s')\,ds',\qquad y(s) = y(s_0) + \int_{s_0}^{s}\sin\theta_t(s')\,ds'}$$
>
> **Units:** $\mathrm m$: the integrands are dimensionless and $ds'$ is a length
> **Meaning:** the conditions of the problem give $\theta_t(s)$ through Eq. 2.20; these two integrals then give the trajectory, and $\dot s$ gives the time law.

The method can be illustrated with the simplest datum, a constant curvature (an illustration built for this note, not an example of the notes): the path must be a circle of radius equal to the inverse of the curvature, with its centre on the normal through the initial point.

> [!derivation] Illustration: a planar path of constant curvature is a circle
> **Law:** Eq. 2.20 integrated with Barrow's rule; Eq. 2.19 integrated with a change of variable
> **Source:** Notes.pdf, Eq. 2.19; Notes.pdf, Eq. 2.20; Notes.pdf, Sec. 2.5.1
>
> Data: the curvature has the constant value $\kappa_0$ and the path turns counterclockwise; at $s = 0$ the particle is at $(x_0, y_0)$ with the tangent at the angle $\theta_0$.
>
> $$\begin{aligned}
> \int_0^{s}\frac{d\theta_t}{ds'}\,ds' &= \int_0^{s}\kappa_0\,ds' \quad &\text{(Eq. 2.20 integrated from $0$ to $s$)} \\
> \left[\,\theta_t\,\right]_0^{s} &= \left[\,\kappa_0\,s'\,\right]_0^{s} \quad &\text{(antiderivatives: $\theta_t$ and $\kappa_0 s'$)} \\
> \theta_t(s) - \theta_0 &= \kappa_0\,s - 0 \quad &\text{(Barrow's rule)} \\
> x(s) - x_0 &= \int_0^{s}\cos(\theta_0 + \kappa_0 s')\,ds' \quad &\text{(previous box with $s_0 = 0$)} \\
> &= \int_{\theta_0}^{\theta_0 + \kappa_0 s}\cos u\,\frac{du}{\kappa_0} \quad &\text{(change $u = \theta_0 + \kappa_0 s'$, $du = \kappa_0\,ds'$; $s' = 0$ gives $u = \theta_0$, $s' = s$ gives $u = \theta_0 + \kappa_0 s$)} \\
> &= \frac{1}{\kappa_0}\left[\,\sin u\,\right]_{\theta_0}^{\theta_0 + \kappa_0 s} \quad &\text{(an antiderivative of $\cos u$ is $\sin u$)} \\
> &= \frac{\sin(\theta_0 + \kappa_0 s) - \sin\theta_0}{\kappa_0} \quad &\text{(Barrow's rule)} \\
> y(s) - y_0 &= \int_{\theta_0}^{\theta_0 + \kappa_0 s}\sin u\,\frac{du}{\kappa_0} \quad &\text{(the same change of variable in the integral of $\sin\theta_t$)} \\
> &= \frac{1}{\kappa_0}\left[\,-\cos u\,\right]_{\theta_0}^{\theta_0 + \kappa_0 s} \quad &\text{(an antiderivative of $\sin u$ is $-\cos u$)} \\
> &= \frac{\cos\theta_0 - \cos(\theta_0 + \kappa_0 s)}{\kappa_0} \quad &\text{(Barrow's rule)} \\
> x - x_0 + \frac{\sin\theta_0}{\kappa_0} &= \frac{\sin(\theta_0 + \kappa_0 s)}{\kappa_0} \quad &\text{(move the constant term of $x$ to the left)} \\
> y - y_0 - \frac{\cos\theta_0}{\kappa_0} &= -\frac{\cos(\theta_0 + \kappa_0 s)}{\kappa_0} \quad &\text{(move the constant term of $y$ to the left)} \\
> \left(x - x_0 + \frac{\sin\theta_0}{\kappa_0}\right)^2 + \left(y - y_0 - \frac{\cos\theta_0}{\kappa_0}\right)^2 &= \frac{\sin^2(\theta_0 + \kappa_0 s)}{\kappa_0^2} + \frac{\cos^2(\theta_0 + \kappa_0 s)}{\kappa_0^2} \quad &\text{(add the squares of the last two rows)} \\
> &= \frac{1}{\kappa_0^2} \quad &\text{($\sin^2 + \cos^2 = 1$)}
> \end{aligned}$$
>
> $$\boxed{\left(x - x_0 + \frac{\sin\theta_0}{\kappa_0}\right)^2 + \left(y - y_0 - \frac{\cos\theta_0}{\kappa_0}\right)^2 = \frac{1}{\kappa_0^2}}$$
>
> **Units:** $\mathrm{m^2}$ on both sides: $\kappa_0$ in $\mathrm{m^{-1}}$
> **Meaning:** a circle of radius $1/\kappa_0$, which is $\rho$; its centre lies at the distance $\rho$ from the initial point along $-\sin\theta_0\,\mathbf i + \cos\theta_0\,\mathbf j$, the tangent turned a quarter turn counterclockwise, that is along $\mathbf e_n$, as Eq. 2.12 requires.

## 14. Coordinate systems

### Coordinates and the local vector basis

Vector bases describe any vector by its components; reference frames give the position vector and the observer. The position of a point can also be given by its coordinates in a coordinate system: two coordinates locate a point in the plane and three in space (Notes.pdf, Sec. 2.6; [Lecture 1, Slide 15]). The classical spatial coordinates are:

| Coordinates | Description (Notes.pdf, Sec. 2.6) |
| :--- | :--- |
| Cartesian $\{x,y,z\}$ | exist by default in every frame $S_0$: the rectilinear distances from $O$ to $P$ along $\mathbf i$, $\mathbf j$ and $\mathbf k$; the only ones that coincide numerically with the components of $\mathbf r_0^P$ in $\mathcal B_0$ |
| cylindrical $\{R,\theta,z\}$ | orthogonal curvilinear coordinates: $x$ and $y$ replaced by the cylindrical radius and the azimuthal angle; in the plane $Oxy$ alone they are the polar coordinates and $\theta$ is the polar angle |
| spherical $\{r,\theta,\phi\}$ | orthogonal curvilinear coordinates: $\theta$ as in cylindrical coordinates, $R$ and $z$ replaced by the spherical radius and the latitude; the radius equals the magnitude of $\mathbf r_0^P$ |

A coordinate system defines at each point a local vector basis along the directions in which each coordinate grows while the other two are kept constant. The vectors are normalised when necessary, and the coordinates are ordered so that the local basis is orthonormal and right-handed when the coordinates are orthogonal; with the point as origin the local basis defines a local reference frame, which in general changes from point to point (Notes.pdf, Sec. 2.6.1; [Lecture 1, Slide 15]).

![[attachments/EM-T/t1-local-basis.svg]]

> [!derivation] Local vector basis of a coordinate system
> **Law:** the direction of growth of one coordinate, the other two fixed, is the partial derivative of the position vector
> **Source:** Notes.pdf, Eq. 2.21; Notes.pdf, Eq. 2.22; [Lecture 1, Slide 15]; [Lecture 1, Slide 16]
>
> $$\begin{aligned}
> \mathbf r_0^P &= \mathbf r_0^P(q_1, q_2, q_3) \quad &\text{(the position is a function of the three coordinates)} \\
> \mathbf u_{q_i} &= \frac{\partial\mathbf r_0^P}{\partial q_i} \quad &\text{(change of $\mathbf r_0^P$ when only $q_i$ grows, Slide 15)} \\
> \mathbf e_{q_i} &= \frac{\mathbf u_{q_i}}{\lvert\mathbf u_{q_i}\rvert} \quad &\text{(normalised, Sec. 2.6.1)} \\
> \mathbf u_x &= \frac{\partial}{\partial x}\left(x\,\mathbf i + y\,\mathbf j + z\,\mathbf k\right) \quad &\text{(Cartesian case, Eq. 2.5)} \\
> &= \mathbf i \quad &\text{($y$, $z$ and the vectors of $\mathcal B_0$ do not depend on $x$)} \\
> \mathbf u_y &= \mathbf j,\qquad \mathbf u_z = \mathbf k \quad &\text{(the same step for $y$ and $z$; all three already have unit magnitude)}
> \end{aligned}$$
>
> $$\boxed{\mathcal B_{\mathcal C}(P) : \{\mathbf e_{q_1},\mathbf e_{q_2},\mathbf e_{q_3}\},\quad \mathbf e_{q_i} = \frac{\partial\mathbf r_0^P/\partial q_i}{\lvert\partial\mathbf r_0^P/\partial q_i\rvert},\quad S_{\mathcal C} : \{P;\mathcal B_{\mathcal C}(P)\};\qquad \text{Cartesian: } \mathbf e_x = \mathbf i,\ \mathbf e_y = \mathbf j,\ \mathbf e_z = \mathbf k}$$
>
> **Units:** $\mathbf u_{q_i}$ has the units of length divided by those of $q_i$ (dimensionless for a length coordinate, metres per radian for an angle); $\mathbf e_{q_i}$ is dimensionless
> **Meaning:** the coordinate system is orthogonal when the three vectors are mutually perpendicular, as for the Cartesian, cylindrical and spherical systems. In Cartesian coordinates the local basis is the basis $\mathcal B_0$ we started with, the same at every point; in other systems it varies with the coordinates.

### Cylindrical coordinates

Cylindrical coordinates suit motions with some form of cylindrical symmetry. The position of $P$ is given by $R$, the cylindrical radius, the distance from the axis $Oz$ to $P$; by $\theta$, the azimuthal angle between the plane $Oxz$ and the plane that contains $Oz$ and $P$, undefined when $P$ is on $Oz$; and by $z$, the height, the same as the Cartesian $z$ (Notes.pdf, Sec. 2.6.2, Fig. 2.4; [Lecture 1, Slide 17]). Call $P'$ the projection of $P$ on the plane $Oxy$.

![[attachments/EM-T/t1-cylindrical-3d.svg]]

![[attachments/EM-T/t1-cylindrical-plan.svg]]

> [!derivation] Cylindrical coordinates: transformation relations and position vector
> **Law:** right triangle in the plane $Oxy$; Pythagoras
> **Source:** Notes.pdf, Eq. 2.23; Notes.pdf Fig. 2.4; [Lecture 1, Slide 17]; [Lecture 1, Slide 19]
>
> Plan view (⊙ $\mathbf k$ out of the paper, $\mathbf i$ to the right, $\mathbf j$ up): the triangle $O$, $F$, $P'$, with $F$ the foot of the perpendicular from $P'$ to $Ox$, is right-angled at $F$; its hypotenuse $OP'$ has length $R$ and the angle at $O$ is $\theta$.
>
> $$\begin{aligned}
> x &= R\cos\theta \quad &\text{(leg $OF$, adjacent to $\theta$, of the triangle of hypotenuse $R$)} \\
> y &= R\sin\theta \quad &\text{(leg $FP'$, opposite to $\theta$)} \\
> R &= \sqrt{x^2 + y^2} \quad &\text{(Pythagoras in the same triangle; $R$ is not negative)} \\
> \theta &= \arctan(y/x) \quad &\text{(opposite over adjacent; the quadrant is the one of the signs of $x$ and $y$)} \\
> \mathbf r_0^P &= R\cos\theta\,\mathbf i + R\sin\theta\,\mathbf j + z\,\mathbf k \quad &\text{(substitute $x$ and $y$ in Eq. 2.5)}
> \end{aligned}$$
>
> $$\boxed{x = R\cos\theta,\quad y = R\sin\theta;\qquad R = \sqrt{x^2 + y^2},\quad \theta = \arctan(y/x);\qquad \mathbf r_0^P = R\cos\theta\,\mathbf i + R\sin\theta\,\mathbf j + z\,\mathbf k}$$
>
> **Units:** $x$, $y$, $z$, $R$ in $\mathrm m$; $\theta$ in $\mathrm{rad}$
> **Meaning:** the height $z$ is shared with the Cartesian system; only the pair $x$, $y$ is replaced by a distance and an angle in the plane $Oxy$.

> [!derivation] Cylindrical local basis from the position vector
> **Law:** coordinate vectors as partial derivatives, then normalised
> **Source:** Notes.pdf, Eq. 2.24; Notes.pdf, Eq. 2.21; [Lecture 1, Slide 15]; [Lecture 1, Slide 17]
>
> In the plan view $\mathbf e_R$ is the unit vector of $OP'$: the angle $\theta$ lies between $\mathbf i$ and $\mathbf e_R$, so its leg along $\mathbf i$ (adjacent) is the cosine and its leg along $\mathbf j$ (opposite) the sine. $\mathbf e_\theta$ is $\mathbf e_R$ turned a quarter turn counterclockwise, the sense in which $\theta$ grows (right-hand rule about $\mathbf k$, which points out of the paper); the angle $\theta$ lies between $\mathbf j$ and $\mathbf e_\theta$, so its leg along $\mathbf j$ is the cosine, and for $\theta$ in the first quadrant $\mathbf e_\theta$ leans to the left of $\mathbf j$: its other leg points along $-\mathbf i$, which is the minus sign.
>
> $$\begin{aligned}
> \mathbf u_R &= \frac{\partial\mathbf r_0^P}{\partial R} \quad &\text{(Slide 15)} \\
> &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j \quad &\text{($\theta$, $z$ and the vectors of $\mathcal B_0$ do not depend on $R$)} \\
> \lvert\mathbf u_R\rvert &= \sqrt{\cos^2\theta + \sin^2\theta} \quad &\text{(magnitude from the components)} \\
> &= 1 \quad &\text{(Pythagoras: $\mathbf e_R = \mathbf u_R$)} \\
> \mathbf u_\theta &= \frac{\partial\mathbf r_0^P}{\partial\theta} \quad &\text{(Slide 15)} \\
> &= -R\sin\theta\,\mathbf i + R\cos\theta\,\mathbf j \quad &\text{(derivatives of the cosine and the sine; $R$ and $z$ fixed)} \\
> \lvert\mathbf u_\theta\rvert &= R\sqrt{\sin^2\theta + \cos^2\theta} \quad &\text{(magnitude from the components)} \\
> &= R \quad &\text{(Pythagoras)} \\
> \mathbf e_\theta &= -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(divide $\mathbf u_\theta$ by its magnitude $R$)} \\
> \mathbf u_z &= \mathbf k \quad &\text{(only the last term of $\mathbf r_0^P$ depends on $z$; unit magnitude, so $\mathbf e_z = \mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_R = \cos\theta\,\mathbf i + \sin\theta\,\mathbf j,\qquad \mathbf e_\theta = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j,\qquad \mathbf e_z = \mathbf k}$$
>
> **Units:** dimensionless unit vectors; $\mathbf u_\theta$ in metres per radian
> **Meaning:** $\lvert\mathbf u_\theta\rvert$ equal to $R$ says that a change $d\theta$ moves $P$ along a circle of radius $R$ by $R\,d\theta$. The vectors are not the same at all points of space: they vary with $\theta$ ([Lecture 1, Slide 17]).

> [!derivation] Cylindrical change of basis matrix and its checks
> **Law:** columns are the local unit vectors in $\mathcal B_0$; determinant; orthogonality; right-handedness
> **Source:** Notes.pdf, Eq. 2.24; Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15
>
> $$\begin{aligned}
> [{}_0R_{\mathrm{cyl}}] &= \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix} \quad &\text{(columns: $\mathbf e_R$, $\mathbf e_\theta$, $\mathbf e_z$ in $\mathcal B_0$, Eq. 1.13)} \\
> &= [{}_0R_1(z,\theta)] \quad &\text{(Eq. 1.20 with $\theta_z = \theta$: $\mathcal B_{\mathrm{cyl}}$ is $\mathcal B_0$ turned by $\theta$ about $\mathbf k$)} \\
> \det[{}_0R_{\mathrm{cyl}}] &= 1\cdot\left(\cos\theta\cos\theta - (-\sin\theta)\sin\theta\right) \quad &\text{(expand along the third row)} \\
> &= \cos^2\theta + \sin^2\theta \quad &\text{(simplify the signs)} \\
> &= 1 \quad &\text{(Pythagoras)} \\
> \left([{}_0R_{\mathrm{cyl}}][{}_0R_{\mathrm{cyl}}]^T\right)_{11} &= \cos\theta\cos\theta + (-\sin\theta)(-\sin\theta) + 0\cdot 0 \quad &\text{(row 1 times row 1)} \\
> &= 1 \quad &\text{(Pythagoras)} \\
> \left([{}_0R_{\mathrm{cyl}}][{}_0R_{\mathrm{cyl}}]^T\right)_{12} &= \cos\theta\sin\theta + (-\sin\theta)\cos\theta + 0\cdot 0 \quad &\text{(row 1 times row 2)} \\
> &= 0 \quad &\text{(the two products cancel)} \\
> \mathbf e_R\times\mathbf e_\theta &= \cos\theta\,(-\sin\theta)\,\mathbf i\times\mathbf i + \cos\theta\cos\theta\,\mathbf i\times\mathbf j + \sin\theta\,(-\sin\theta)\,\mathbf j\times\mathbf i + \sin\theta\cos\theta\,\mathbf j\times\mathbf j \quad &\text{(distribute, Eq. 1.32)} \\
> &= \cos\theta\cos\theta\,\mathbf i\times\mathbf j + \sin\theta\,(-\sin\theta)\,\mathbf j\times\mathbf i \quad &\text{($\mathbf i\times\mathbf i = \mathbf j\times\mathbf j = \mathbf 0$)} \\
> &= \cos^2\theta\,\mathbf k + \sin^2\theta\,\mathbf k \quad &\text{($\mathbf i\times\mathbf j = \mathbf k$, $\mathbf j\times\mathbf i = -\mathbf k$)} \\
> &= \mathbf e_z \quad &\text{(Pythagoras)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_{\mathrm{cyl}}] = [{}_0R_1(z,\theta)] = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix},\qquad \det = 1,\qquad \mathbf e_R\times\mathbf e_\theta = \mathbf e_z}$$
>
> **Units:** dimensionless
> **Meaning:** the cylindrical basis is a simple rotation of $\mathcal B_0$ about $\mathbf k$ by the azimuth; the remaining entries of $[{}_0R_{\mathrm{cyl}}][{}_0R_{\mathrm{cyl}}]^T$ follow in the same way ($(2,2)$ by Pythagoras, $(1,3)$ and $(2,3)$ are zero), so the basis is orthonormal, and with $\mathbf e_R\times\mathbf e_\theta = \mathbf e_z$ it is right-handed in the order $R$, $\theta$, $z$.

> [!derivation] Time derivatives of the cylindrical unit vectors
> **Law:** partial derivatives with respect to $\theta$; chain rule through $\theta(t)$; Eq. 1.62 with the angular velocity of the local basis
> **Source:** Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26; Notes.pdf, Eq. 2.27; [Lecture 1, Slide 17]; Notes.pdf, Eq. 1.62
>
> The derivatives are taken in $S_0$, where $\mathbf i$, $\mathbf j$, $\mathbf k$ are constant; the local vectors depend on time only through $\theta(t)$.
>
> $$\begin{aligned}
> \frac{\partial\mathbf e_R}{\partial\theta} &= -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(derivatives of the cosine and the sine)} \\
> &= \mathbf e_\theta \quad &\text{(Eq. 2.24)} \\
> \frac{\partial\mathbf e_\theta}{\partial\theta} &= -\cos\theta\,\mathbf i - \sin\theta\,\mathbf j \quad &\text{(derivatives of $-\sin\theta$ and $\cos\theta$)} \\
> &= -\mathbf e_R \quad &\text{(Eq. 2.24)} \\
> \frac{d\mathbf e_R}{dt} &= \frac{\partial\mathbf e_R}{\partial\theta}\,\dot\theta \quad &\text{(chain rule: $\mathbf e_R = \mathbf e_R(\theta(t))$)} \\
> &= \dot\theta\,\mathbf e_\theta \quad &\text{(first result)} \\
> \frac{d\mathbf e_\theta}{dt} &= \frac{\partial\mathbf e_\theta}{\partial\theta}\,\dot\theta \quad &\text{(chain rule)} \\
> &= -\dot\theta\,\mathbf e_R \quad &\text{(second result)} \\
> \frac{d\mathbf e_z}{dt} &= \frac{d\mathbf k}{dt} \quad &\text{($\mathbf e_z = \mathbf k$)} \\
> &= \mathbf 0 \quad &\text{($\mathbf k$ is constant in $S_0$)} \\
> \boldsymbol\omega_{\mathrm{cyl}} &= \dot\theta\,\mathbf k \quad &\text{(the local basis turns about $\mathbf k$ at the rate $\dot\theta$, the simple rotation of the box above)} \\
> \boldsymbol\omega_{\mathrm{cyl}}\times\mathbf e_R &= \dot\theta\left(\cos\theta\,\mathbf k\times\mathbf i + \sin\theta\,\mathbf k\times\mathbf j\right) \quad &\text{(distribute, Eq. 1.32)} \\
> &= \dot\theta\left(\cos\theta\,\mathbf j - \sin\theta\,\mathbf i\right) \quad &\text{($\mathbf k\times\mathbf i = \mathbf j$, $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> &= \dot\theta\,\mathbf e_\theta \quad &\text{(the same as the derivative of $\mathbf e_R$: Eq. 1.62 holds)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\mathbf e_R}{dt} = \dot\theta\,\mathbf e_\theta,\qquad \frac{d\mathbf e_\theta}{dt} = -\dot\theta\,\mathbf e_R,\qquad \frac{d\mathbf e_z}{dt} = \mathbf 0;\qquad \boldsymbol\omega_{\mathrm{cyl}} = \dot\theta\,\mathbf k}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ ($\mathrm{rad/s}$) in every term
> **Meaning:** these are the derivatives of the basis in simple rotation about $\mathbf k$ of Section 6, with $\theta$ in place of $\theta_z$: each vector of the plane $Oxy$ is turned a quarter turn in the sense of growing $\theta$ and scaled by $\dot\theta$, and $\boldsymbol\omega_{\mathrm{cyl}}\times\mathbf e_\theta$ gives $-\dot\theta\,\mathbf e_R$ by the same steps.

> [!derivation] Position and velocity in cylindrical coordinates
> **Law:** position vector rewritten in the local basis; definition of velocity; product rule
> **Source:** Notes.pdf, Eq. 2.28; Notes.pdf, Eq. 2.29; [Lecture 1, Slide 19]
>
> $$\begin{aligned}
> \mathbf r_0^P &= R\cos\theta\,\mathbf i + R\sin\theta\,\mathbf j + z\,\mathbf k \quad &\text{(Eq. 2.23 in Eq. 2.5)} \\
> &= R\left(\cos\theta\,\mathbf i + \sin\theta\,\mathbf j\right) + z\,\mathbf k \quad &\text{(factor $R$)} \\
> &= R\,\mathbf e_R + z\,\mathbf e_z \quad &\text{(Eq. 2.24)} \\
> \mathbf v_0^P &= \frac{d}{dt}\left(R\,\mathbf e_R\right) + \frac{d}{dt}\left(z\,\mathbf e_z\right) \quad &\text{(Eq. 2.3; sum rule, Eq. 1.65)} \\
> &= \dot R\,\mathbf e_R + R\,\frac{d\mathbf e_R}{dt} + \dot z\,\mathbf e_z + z\,\frac{d\mathbf e_z}{dt} \quad &\text{(product rule on both terms, Eq. 1.64)} \\
> &= \dot R\,\mathbf e_R + R\dot\theta\,\mathbf e_\theta + \dot z\,\mathbf e_z + \mathbf 0 \quad &\text{(Eqs. 2.25 and 2.27)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = R\,\mathbf e_R + z\,\mathbf e_z,\qquad \mathbf v_0^P = \dot R\,\mathbf e_R + R\dot\theta\,\mathbf e_\theta + \dot z\,\mathbf e_z}$$
>
> **Units:** $\mathrm{m/s}$ in every term: $\dot R$, $R\dot\theta$ ($\mathrm m$ times $\mathrm{rad/s}$) and $\dot z$
> **Meaning:** the position has no $\mathbf e_\theta$ component, because the azimuth enters only through the direction of $\mathbf e_R$; the velocity has a radial part, a circumferential part, the speed of a point at the distance $R$ from $Oz$ turning at the rate $\dot\theta$, and an axial part.

> [!warning] Typo in Notes.pdf, Eq. 2.29
> The printed Eq. 2.29 (Notes.pdf, p. 33) carries a stray comma between the axial rate and its unit vector, "+ ż, e_z": the term is the axial rate times $\mathbf e_z$, as in the box above and in Eq. 2.30. The typo does not change any result.

> [!derivation] Acceleration in cylindrical coordinates
> **Law:** definition of acceleration; product rule term by term; Eqs. 2.25 to 2.27
> **Source:** Notes.pdf, Eq. 2.30; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26; Notes.pdf, Eq. 2.27; [Lecture 1, Slide 19]
>
> $$\begin{aligned}
> \mathbf a_0^P &= \frac{d}{dt}\left(\dot R\,\mathbf e_R\right) + \frac{d}{dt}\left(R\dot\theta\,\mathbf e_\theta\right) + \frac{d}{dt}\left(\dot z\,\mathbf e_z\right) \quad &\text{(Eq. 2.4 on Eq. 2.29; sum rule)} \\
> \frac{d}{dt}\left(\dot R\,\mathbf e_R\right) &= \ddot R\,\mathbf e_R + \dot R\,\frac{d\mathbf e_R}{dt} \quad &\text{(product rule)} \\
> &= \ddot R\,\mathbf e_R + \dot R\dot\theta\,\mathbf e_\theta \quad &\text{(Eq. 2.25)} \\
> \frac{d}{dt}\left(R\dot\theta\,\mathbf e_\theta\right) &= \dot R\dot\theta\,\mathbf e_\theta + R\ddot\theta\,\mathbf e_\theta + R\dot\theta\,\frac{d\mathbf e_\theta}{dt} \quad &\text{(product rule for the three factors $R$, $\dot\theta$, $\mathbf e_\theta$)} \\
> &= \dot R\dot\theta\,\mathbf e_\theta + R\ddot\theta\,\mathbf e_\theta - R\dot\theta^2\,\mathbf e_R \quad &\text{(Eq. 2.26)} \\
> \frac{d}{dt}\left(\dot z\,\mathbf e_z\right) &= \ddot z\,\mathbf e_z + \dot z\,\frac{d\mathbf e_z}{dt} \quad &\text{(product rule)} \\
> &= \ddot z\,\mathbf e_z \quad &\text{(Eq. 2.27)} \\
> \mathbf a_0^P &= \left(\ddot R - R\dot\theta^2\right)\mathbf e_R + \left(\dot R\dot\theta + \dot R\dot\theta + R\ddot\theta\right)\mathbf e_\theta + \ddot z\,\mathbf e_z \quad &\text{(add the three results and collect by unit vector)} \\
> &= \left(\ddot R - R\dot\theta^2\right)\mathbf e_R + \left(R\ddot\theta + 2\dot R\dot\theta\right)\mathbf e_\theta + \ddot z\,\mathbf e_z \quad &\text{(add the two equal terms)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \left(\ddot R - R\dot\theta^2\right)\mathbf e_R + \left(R\ddot\theta + 2\dot R\dot\theta\right)\mathbf e_\theta + \ddot z\,\mathbf e_z}$$
>
> **Units:** $\mathrm{m/s^2}$ in every term: $\ddot R$, $R\dot\theta^2$, $R\ddot\theta$, $\dot R\dot\theta$ and $\ddot z$ are each a length over a time squared
> **Meaning:** the term in $-R\dot\theta^2$ comes from the turning of $\mathbf e_\theta$ and points towards the axis $Oz$; of the two equal terms in $\dot R\dot\theta$, one comes from the turning of $\mathbf e_R$ while $R$ changes, the other from the change of $R$ in the circumferential velocity. For a circle of fixed radius traversed at a constant rate only $-R\dot\theta^2\,\mathbf e_R$ remains.

> [!derivation] Check: the cylindrical velocity projected on the basis of S0
> **Law:** direct differentiation of the Cartesian coordinates; change of basis with $[{}_0R_{\mathrm{cyl}}]$
> **Source:** [Lecture 1, Slide 19]; Notes.pdf, Eq. 2.23; Notes.pdf, Eq. 1.12
>
> $$\begin{aligned}
> \dot x &= \frac{d}{dt}\left(R\cos\theta\right) \quad &\text{(Eq. 2.23)} \\
> &= \dot R\cos\theta + R\,\frac{d\cos\theta}{dt} \quad &\text{(product rule)} \\
> &= \dot R\cos\theta - R\dot\theta\sin\theta \quad &\text{(chain rule: $\dfrac{d\cos\theta}{dt} = -\sin\theta\,\dot\theta$)} \\
> [\mathbf v_0^P]_0 &= [{}_0R_{\mathrm{cyl}}]\,[\mathbf v_0^P]_{\mathrm{cyl}} \quad &\text{(Eq. 1.12)} \\
> &= \begin{pmatrix} \cos\theta\,\dot R - \sin\theta\,R\dot\theta + 0\cdot\dot z \cr \sin\theta\,\dot R + \cos\theta\,R\dot\theta + 0\cdot\dot z \cr 0\cdot\dot R + 0\cdot R\dot\theta + 1\cdot\dot z \end{pmatrix} \quad &\text{(rows of the matrix times the column $(\dot R,\ R\dot\theta,\ \dot z)$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \left(\dot R\cos\theta - R\dot\theta\sin\theta\right)\mathbf i + \left(\dot R\sin\theta + R\dot\theta\cos\theta\right)\mathbf j + \dot z\,\mathbf k}$$
>
> **Units:** $\mathrm{m/s}$ in every term
> **Meaning:** the first row of the product equals $\dot x$ obtained without the local basis, so both routes agree. Each vector can be written with the coordinates $R$, $\theta$, $z$ in either basis, $\mathcal B_0$ or $\mathcal B_{\mathrm{cyl}}$ ([Lecture 1, Slide 19]); the next box projects the acceleration the same way.

> [!derivation] The cylindrical acceleration projected on the basis of S0
> **Law:** change of basis with $[{}_0R_{\mathrm{cyl}}]$, row times column
> **Source:** [Lecture 1, Slide 19]; Notes.pdf, Eq. 1.12; Notes.pdf, Eq. 2.30
>
> The column of components in $\mathcal B_{\mathrm{cyl}}$ is that of Eq. 2.30: the radial component $\ddot R - R\dot\theta^2$, the azimuthal component $R\ddot\theta + 2\dot R\dot\theta$ and the axial component $\ddot z$.
>
> $$\begin{aligned}
> [\mathbf a_0^P]_0 &= [{}_0R_{\mathrm{cyl}}]\,[\mathbf a_0^P]_{\mathrm{cyl}} \quad &\text{(Eq. 1.12)} \\
> &= \begin{pmatrix} \cos\theta\left(\ddot R - R\dot\theta^2\right) + (-\sin\theta)\left(R\ddot\theta + 2\dot R\dot\theta\right) + 0\cdot\ddot z \cr \sin\theta\left(\ddot R - R\dot\theta^2\right) + \cos\theta\left(R\ddot\theta + 2\dot R\dot\theta\right) + 0\cdot\ddot z \cr 0\cdot\left(\ddot R - R\dot\theta^2\right) + 0\cdot\left(R\ddot\theta + 2\dot R\dot\theta\right) + 1\cdot\ddot z \end{pmatrix} \quad &\text{(rows of the matrix times the column of Eq. 2.30)} \\
> &= \begin{pmatrix} \cos\theta\left(\ddot R - R\dot\theta^2\right) - \sin\theta\left(R\ddot\theta + 2\dot R\dot\theta\right) \cr \sin\theta\left(\ddot R - R\dot\theta^2\right) + \cos\theta\left(R\ddot\theta + 2\dot R\dot\theta\right) \cr \ddot z \end{pmatrix} \quad &\text{(drop the zero products)} \\
> &= \begin{pmatrix} \ddot R\cos\theta - R\dot\theta^2\cos\theta - 2\dot R\dot\theta\sin\theta - R\ddot\theta\sin\theta \cr \ddot R\sin\theta - R\dot\theta^2\sin\theta + 2\dot R\dot\theta\cos\theta + R\ddot\theta\cos\theta \cr \ddot z \end{pmatrix} \quad &\text{(distribute, in the order of the slide)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \left(\ddot R\cos\theta - R\dot\theta^2\cos\theta - 2\dot R\dot\theta\sin\theta - R\ddot\theta\sin\theta\right)\mathbf i + \left(\ddot R\sin\theta - R\dot\theta^2\sin\theta + 2\dot R\dot\theta\cos\theta + R\ddot\theta\cos\theta\right)\mathbf j + \ddot z\,\mathbf k}$$
>
> **Units:** $\mathrm{m/s^2}$ in every term: each is a length over a time squared
> **Meaning:** these are the Cartesian components printed on [Lecture 1, Slide 19], term by term. For a circle of fixed radius traversed at a constant rate only the terms in $R\dot\theta^2$ remain, and they form minus that magnitude times the horizontal direction of $\mathbf e_R$: the acceleration points to the axis.

> [!warning] Cylindrical components are not intrinsic components
> The radial and azimuthal components of Eq. 2.30 cannot, in general, be identified with the tangential and normal accelerations (Notes.pdf, Sec. 2.6.2): $\mathbf e_R$ and $\mathbf e_\theta$ are defined by the coordinate system, $\mathbf e_t$ and $\mathbf e_n$ by the trajectory. They correspond only in special motions, such as a circle in a plane normal to $Oz$ and centred on it, where $\mathbf e_\theta$ is tangent to the path and $-\mathbf e_R$ points to the centre of curvature.

### Spherical coordinates

Spherical coordinates are used in some three-dimensional problems. The position of $P$ is given by $r$, the radius, the distance from $O$ to $P$, equal to the magnitude of $\mathbf r_0^P$; by $\theta$, the azimuthal angle, as in cylindrical coordinates; and by $\phi$, the latitude, the angle between the plane $Oxy$ and the vector $\mathbf r_0^P$, positive above the plane. The coordinates are not well defined at $r$ equal to zero or on the axis $Oz$, where $\theta$ is undefined (Notes.pdf, Sec. 2.6.3, Fig. 2.5; [Lecture 1, Slide 20]): the notes list the latitude of a right angle; by symmetry the latitude of minus a right angle, the other half of the axis, is singular too.

The latitude is measured from the plane $Oxy$, not from the axis $Oz$. Some texts use instead the complementary angle, measured from the pole and called colatitude, $\varphi$; always check which one a statement uses (Notes.pdf, Sec. 2.6; [Lecture 1, Slide 20]).

![[attachments/EM-T/t1-spherical-3d.svg]]

![[attachments/EM-T/t1-spherical-meridian.svg]]

> [!derivation] Latitude and colatitude
> **Law:** the axis $Oz$ is perpendicular to the plane $Oxy$; cosine and sine of a difference
> **Source:** [Lecture 1, Slide 20]; Notes.pdf, Sec. 2.6
>
> Work in the meridian plane, the plane that contains $Oz$ and $P$; it cuts the plane $Oxy$ along the line $OP'$, perpendicular to $Oz$. The colatitude is the angle from $Oz$ to $\mathbf r_0^P$ and the latitude the angle from $OP'$ to $\mathbf r_0^P$, positive towards $Oz$.
>
> $$\begin{aligned}
> \varphi + \phi &= \frac{\pi}{2} \quad &\text{(together they span the right angle between $Oz$ and $OP'$; for $P$ below $Oxy$ the latitude is negative and the colatitude exceeds a right angle by the same amount)} \\
> \varphi &= \frac{\pi}{2} - \phi \quad &\text{(subtract $\phi$)} \\
> \cos\varphi &= \cos\frac{\pi}{2}\cos\phi + \sin\frac{\pi}{2}\sin\phi \quad &\text{(cosine of a difference)} \\
> &= \sin\phi \quad &\text{($\cos\frac{\pi}{2} = 0$, $\sin\frac{\pi}{2} = 1$)} \\
> \sin\varphi &= \sin\frac{\pi}{2}\cos\phi - \cos\frac{\pi}{2}\sin\phi \quad &\text{(sine of a difference)} \\
> &= \cos\phi \quad &\text{(the same values)}
> \end{aligned}$$
>
> $$\boxed{\varphi = \frac{\pi}{2} - \phi,\qquad \cos\varphi = \sin\phi,\qquad \sin\varphi = \cos\phi}$$
>
> **Units:** angles in $\mathrm{rad}$
> **Meaning:** with the colatitude every sine of the latitude becomes a cosine and every cosine a sine; the height of $P$, for instance, is $r$ times the sine of the latitude but $r$ times the cosine of the colatitude. This note, like the notes and slides, uses the latitude $\phi$.

> [!derivation] Spherical coordinates: transformation relations and position vector
> **Law:** two right triangles, one in the meridian plane and one in the plane $Oxy$; Pythagoras
> **Source:** Notes.pdf, Eq. 2.31; Notes.pdf Fig. 2.5; [Lecture 1, Slide 20]; [Lecture 1, Slide 22]
>
> Meridian triangle: $O$, $P'$, $P$, right-angled at $P'$ ($P'P$ parallel to $Oz$, $OP'$ in the plane $Oxy$), hypotenuse $OP$ of length $r$, angle $\phi$ at $O$. Plan triangle: $O$, $F$, $P'$ as in cylindrical coordinates, hypotenuse $OP'$, angle $\theta$ at $O$.
>
> $$\begin{aligned}
> z &= r\sin\phi \quad &\text{(leg $P'P$, opposite to $\phi$ in the meridian triangle of hypotenuse $r$)} \\
> \lvert OP'\rvert &= r\cos\phi \quad &\text{(leg $OP'$, adjacent to $\phi$: the cylindrical radius $R$)} \\
> x &= r\cos\phi\cos\theta \quad &\text{(leg adjacent to $\theta$ in the plan triangle of hypotenuse $r\cos\phi$)} \\
> y &= r\cos\phi\sin\theta \quad &\text{(leg opposite to $\theta$ in the plan triangle)} \\
> r &= \sqrt{x^2 + y^2 + z^2} \quad &\text{(Pythagoras twice: $\lvert OP'\rvert^2 = x^2 + y^2$, then $r^2 = \lvert OP'\rvert^2 + z^2$)} \\
> \theta &= \arctan(y/x) \quad &\text{(plan triangle, as in Eq. 2.23)} \\
> \phi &= \arctan\left(z/\sqrt{x^2 + y^2}\right) \quad &\text{(meridian triangle: opposite over adjacent)} \\
> \mathbf r_0^P &= r\cos\phi\cos\theta\,\mathbf i + r\cos\phi\sin\theta\,\mathbf j + r\sin\phi\,\mathbf k \quad &\text{(substitute $x$, $y$, $z$ in Eq. 2.5)}
> \end{aligned}$$
>
> $$\boxed{x = r\cos\phi\cos\theta,\quad y = r\cos\phi\sin\theta,\quad z = r\sin\phi;\qquad r = \sqrt{x^2 + y^2 + z^2},\quad \theta = \arctan(y/x),\quad \phi = \arctan\left(z/\sqrt{x^2 + y^2}\right)}$$
>
> **Units:** $x$, $y$, $z$, $r$ in $\mathrm m$; $\theta$, $\phi$ in $\mathrm{rad}$
> **Meaning:** the radius is the magnitude of the position vector, a property of the spherical coordinates only; the latitude is the arctangent of a height over a non-negative horizontal distance, so it lies between minus and plus a right angle.

![[attachments/EM-T/t1-spherical-plan.svg]]

> [!derivation] Spherical local basis from the meridian and plan views
> **Law:** projections of unit vectors on the legs of right triangles; the cylindrical vectors of Eq. 2.24
> **Source:** Notes.pdf, Eq. 2.32; Notes.pdf Fig. 2.5; [Lecture 1, Slide 20]
>
> Meridian view: $\mathbf e_R$ (horizontal, along $OP'$) to the right and $\mathbf k$ up. Since $\mathbf k\times\mathbf e_R = \mathbf e_\theta$ (cyclic order of $\mathcal B_{\mathrm{cyl}}$), the vector out of the paper, $\mathbf e_R\times\mathbf k$, is $-\mathbf e_\theta$: $\mathbf e_\theta$ points into the paper (⊗), and the latitude grows counterclockwise in this view. Each unit vector is the hypotenuse (length one) of a right triangle with legs along $\mathbf e_R$ and $\mathbf k$; the leg along $\mathbf e_R$ is then projected on $\mathbf i$ and $\mathbf j$ with the plan triangle.
>
> $$\begin{aligned}
> \mathbf e_r &= \cos\phi\,\mathbf e_R + \sin\phi\,\mathbf k \quad &\text{(along $OP$: $\phi$ lies between $\mathbf e_R$ and $\mathbf e_r$, adjacent leg along $\mathbf e_R$, opposite leg along $\mathbf k$)} \\
> &= \cos\phi\cos\theta\,\mathbf i + \cos\phi\sin\theta\,\mathbf j + \sin\phi\,\mathbf k \quad &\text{(substitute $\mathbf e_R$, Eq. 2.24)} \\
> \mathbf e_\theta &= -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(growing $\theta$ with $r$ and $\phi$ fixed moves $P$ along a horizontal parallel circle: the cylindrical $\mathbf e_\theta$, Eq. 2.24)} \\
> \mathbf e_\phi &= -\sin\phi\,\mathbf e_R + \cos\phi\,\mathbf k \quad &\text{($\mathbf e_r$ turned a quarter turn counterclockwise: $\phi$ lies between $\mathbf k$ and $\mathbf e_\phi$, adjacent leg along $\mathbf k$; $\mathbf e_\phi$ leans back towards the axis $Oz$, so its other leg points along $-\mathbf e_R$)} \\
> &= -\sin\phi\cos\theta\,\mathbf i - \sin\phi\sin\theta\,\mathbf j + \cos\phi\,\mathbf k \quad &\text{(substitute $\mathbf e_R$, Eq. 2.24)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_r = \cos\phi\cos\theta\,\mathbf i + \cos\phi\sin\theta\,\mathbf j + \sin\phi\,\mathbf k,\quad \mathbf e_\theta = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j,\quad \mathbf e_\phi = -\sin\phi\cos\theta\,\mathbf i - \sin\phi\sin\theta\,\mathbf j + \cos\phi\,\mathbf k}$$
>
> **Units:** dimensionless
> **Meaning:** $\mathbf e_r$ points away from $O$, $\mathbf e_\theta$ along the parallel (towards growing azimuth) and $\mathbf e_\phi$ along the meridian towards the north pole; at the latitude zero $\mathbf e_r$ is $\mathbf e_R$ and $\mathbf e_\phi$ is $\mathbf k$.

> [!derivation] Check: the spherical coordinate vectors
> **Law:** coordinate vectors as partial derivatives of the position vector
> **Source:** [Lecture 1, Slide 15]; Notes.pdf, Eq. 2.21; Notes.pdf, Eq. 2.32
>
> $$\begin{aligned}
> \mathbf u_r &= \frac{\partial\mathbf r_0^P}{\partial r} \quad &\text{(Slide 15)} \\
> &= \cos\phi\cos\theta\,\mathbf i + \cos\phi\sin\theta\,\mathbf j + \sin\phi\,\mathbf k \quad &\text{(only the factor $r$ depends on $r$)} \\
> \lvert\mathbf u_r\rvert^2 &= \cos^2\phi\cos^2\theta + \cos^2\phi\sin^2\theta + \sin^2\phi \quad &\text{(sum of the squared components)} \\
> &= \cos^2\phi + \sin^2\phi \quad &\text{(factor $\cos^2\phi$; Pythagoras for $\theta$)} \\
> &= 1 \quad &\text{(Pythagoras for $\phi$)} \\
> \mathbf u_\theta &= \frac{\partial\mathbf r_0^P}{\partial\theta} \quad &\text{(Slide 15)} \\
> &= -r\cos\phi\sin\theta\,\mathbf i + r\cos\phi\cos\theta\,\mathbf j \quad &\text{(derivatives of $\cos\theta$ and $\sin\theta$; the $\mathbf k$ term does not contain $\theta$)} \\
> &= r\cos\phi\,\mathbf e_\theta \quad &\text{(factor $r\cos\phi$)} \\
> \mathbf u_\phi &= \frac{\partial\mathbf r_0^P}{\partial\phi} \quad &\text{(Slide 15)} \\
> &= -r\sin\phi\cos\theta\,\mathbf i - r\sin\phi\sin\theta\,\mathbf j + r\cos\phi\,\mathbf k \quad &\text{(derivatives of $\cos\phi$ and $\sin\phi$)} \\
> &= r\,\mathbf e_\phi \quad &\text{(factor $r$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf u_r = \mathbf e_r,\qquad \mathbf u_\theta = r\cos\phi\,\mathbf e_\theta,\qquad \mathbf u_\phi = r\,\mathbf e_\phi}$$
>
> **Units:** $\mathbf u_r$ dimensionless; $\mathbf u_\theta$ and $\mathbf u_\phi$ in metres per radian
> **Meaning:** normalising the coordinate vectors gives the same three unit vectors as the views; the magnitudes are the radii of the parallel circle, $r\cos\phi$, and of the meridian circle, $r$, on which $P$ moves when only $\theta$ or only $\phi$ changes.

> [!derivation] Spherical change of basis matrix as two simple rotations
> **Law:** columns are the local unit vectors; composition of changes of basis; determinant and orthogonality
> **Source:** Notes.pdf, Eq. 2.32; Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.16; Notes.pdf, Eq. 1.19; Notes.pdf, Eq. 1.20
>
> The second matrix has as columns $\mathbf e_r$, $\mathbf e_\theta$, $\mathbf e_\phi$ written in $\mathcal B_{\mathrm{cyl}}$ (the first expressions of the box above). With $\mathbf e_R$, $\mathbf e_\theta$, $\mathbf e_z$ in the roles of $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$, it is a simple rotation about $\mathbf e_\theta$: in the meridian view $\mathbf e_\theta$ points into the paper, so the counterclockwise latitude is a rotation by $-\phi$ about $\mathbf e_\theta$ by the right-hand rule.
>
> $$\begin{aligned}
> [{}_0R_{\mathrm{sph}}] &= \begin{pmatrix} \cos\phi\cos\theta & -\sin\theta & -\sin\phi\cos\theta \cr \cos\phi\sin\theta & \cos\theta & -\sin\phi\sin\theta \cr \sin\phi & 0 & \cos\phi \end{pmatrix} \quad &\text{(columns: $\mathbf e_r$, $\mathbf e_\theta$, $\mathbf e_\phi$ in $\mathcal B_0$, Eq. 1.13)} \\
> [{}_{\mathrm{cyl}}R_{\mathrm{sph}}] &= \begin{pmatrix} \cos\phi & 0 & -\sin\phi \cr 0 & 1 & 0 \cr \sin\phi & 0 & \cos\phi \end{pmatrix} \quad &\text{(columns: $\mathbf e_r$, $\mathbf e_\theta$, $\mathbf e_\phi$ in $\mathcal B_{\mathrm{cyl}}$)} \\
> &= [{}_0R_1(y,-\phi)] \quad &\text{(Eq. 1.19 with $\theta_y = -\phi$: cosine even, sine odd)} \\
> [{}_0R_{\mathrm{cyl}}]\,[{}_{\mathrm{cyl}}R_{\mathrm{sph}}] &= \begin{pmatrix} \cos\theta\cos\phi + (-\sin\theta)\cdot 0 + 0\cdot\sin\phi & \cos\theta\cdot 0 + (-\sin\theta)\cdot 1 + 0\cdot 0 & \cos\theta(-\sin\phi) + (-\sin\theta)\cdot 0 + 0\cdot\cos\phi \cr \sin\theta\cos\phi + \cos\theta\cdot 0 + 0\cdot\sin\phi & \sin\theta\cdot 0 + \cos\theta\cdot 1 + 0\cdot 0 & \sin\theta(-\sin\phi) + \cos\theta\cdot 0 + 0\cdot\cos\phi \cr 0\cdot\cos\phi + 0\cdot 0 + 1\cdot\sin\phi & 0\cdot 0 + 0\cdot 1 + 1\cdot 0 & 0\cdot(-\sin\phi) + 0\cdot 0 + 1\cdot\cos\phi \end{pmatrix} \quad &\text{(row $m$ of Eq. 1.20 with $\theta_z = \theta$ times column $n$)} \\
> &= [{}_0R_{\mathrm{sph}}] \quad &\text{(drop the zero products: the first row; Eq. 1.16)} \\
> \det[{}_0R_{\mathrm{sph}}] &= \sin\phi\left((-\sin\theta)(-\sin\phi\sin\theta) - (-\sin\phi\cos\theta)\cos\theta\right) + \cos\phi\left(\cos\phi\cos\theta\cos\theta - (-\sin\theta)\cos\phi\sin\theta\right) \quad &\text{(expand along the third row; cofactor signs $+$ at $(3,1)$ and $(3,3)$, entry $(3,2)$ is zero)} \\
> &= \sin\phi\left(\sin\phi\sin^2\theta + \sin\phi\cos^2\theta\right) + \cos\phi\left(\cos\phi\cos^2\theta + \cos\phi\sin^2\theta\right) \quad &\text{(simplify the signs)} \\
> &= \sin^2\phi + \cos^2\phi \quad &\text{(Pythagoras for $\theta$ inside each bracket)} \\
> &= 1 \quad &\text{(Pythagoras for $\phi$)} \\
> \left([{}_0R_{\mathrm{sph}}][{}_0R_{\mathrm{sph}}]^T\right)_{11} &= \cos^2\phi\cos^2\theta + \sin^2\theta + \sin^2\phi\cos^2\theta \quad &\text{(row 1 times row 1)} \\
> &= \left(\cos^2\phi + \sin^2\phi\right)\cos^2\theta + \sin^2\theta \quad &\text{(group the terms in $\cos^2\theta$)} \\
> &= 1 \quad &\text{(Pythagoras twice)} \\
> \left([{}_0R_{\mathrm{sph}}][{}_0R_{\mathrm{sph}}]^T\right)_{13} &= \cos\phi\cos\theta\sin\phi + (-\sin\theta)\cdot 0 + (-\sin\phi\cos\theta)\cos\phi \quad &\text{(row 1 times row 3)} \\
> &= 0 \quad &\text{(the first and last products cancel)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_{\mathrm{sph}}] = [{}_0R_{\mathrm{cyl}}]\,[{}_{\mathrm{cyl}}R_{\mathrm{sph}}] = \begin{bmatrix} \cos\phi\cos\theta & -\sin\theta & -\sin\phi\cos\theta \\ \cos\phi\sin\theta & \cos\theta & -\sin\phi\sin\theta \\ \sin\phi & 0 & \cos\phi \end{bmatrix},\qquad \det = 1}$$
>
> **Units:** dimensionless
> **Meaning:** the spherical basis is reached from $\mathcal B_0$ by turning $\theta$ about $\mathbf k$ and then $-\phi$ about the new $\mathbf e_\theta$; the matrix is orthogonal and its determinant, the triple product of its columns, is $+1$, so the basis is right-handed in the order $r$, $\theta$, $\phi$: $\mathbf e_r\times\mathbf e_\theta = \mathbf e_\phi$, $\mathbf e_\theta\times\mathbf e_\phi = \mathbf e_r$, $\mathbf e_\phi\times\mathbf e_r = \mathbf e_\theta$. Its third row gives $\mathbf k$ in $\mathcal B_{\mathrm{sph}}$: $\mathbf k = \sin\phi\,\mathbf e_r + \cos\phi\,\mathbf e_\phi$.

> [!derivation] Partial derivatives of the spherical unit vectors
> **Law:** differentiation of the components of Eq. 2.32 with respect to one angle, the other fixed; inverse relation between the meridian vectors
> **Source:** [Lecture 1, Slide 20]; Notes.pdf, Eq. 2.32
>
> $$\begin{aligned}
> \frac{\partial\mathbf e_r}{\partial\theta} &= -\cos\phi\sin\theta\,\mathbf i + \cos\phi\cos\theta\,\mathbf j \quad &\text{(derivatives of $\cos\theta$ and $\sin\theta$; $\phi$ fixed)} \\
> &= \cos\phi\,\mathbf e_\theta \quad &\text{(factor $\cos\phi$; Eq. 2.32)} \\
> \frac{\partial\mathbf e_r}{\partial\phi} &= -\sin\phi\cos\theta\,\mathbf i - \sin\phi\sin\theta\,\mathbf j + \cos\phi\,\mathbf k \quad &\text{(derivatives of $\cos\phi$ and $\sin\phi$; $\theta$ fixed)} \\
> &= \mathbf e_\phi \quad &\text{(Eq. 2.32)} \\
> \frac{\partial\mathbf e_\theta}{\partial\theta} &= -\cos\theta\,\mathbf i - \sin\theta\,\mathbf j \quad &\text{(derivatives of $-\sin\theta$ and $\cos\theta$)} \\
> &= -\mathbf e_R \quad &\text{(Eq. 2.24)} \\
> \cos\phi\,\mathbf e_r - \sin\phi\,\mathbf e_\phi &= \cos\phi\left(\cos\phi\,\mathbf e_R + \sin\phi\,\mathbf k\right) - \sin\phi\left(-\sin\phi\,\mathbf e_R + \cos\phi\,\mathbf k\right) \quad &\text{(substitute the first forms of $\mathbf e_r$ and $\mathbf e_\phi$, in $\mathbf e_R$ and $\mathbf k$)} \\
> &= \cos^2\phi\,\mathbf e_R + \cos\phi\sin\phi\,\mathbf k + \sin^2\phi\,\mathbf e_R - \sin\phi\cos\phi\,\mathbf k \quad &\text{(distribute)} \\
> &= \mathbf e_R \quad &\text{(Pythagoras; the $\mathbf k$ terms cancel)} \\
> \frac{\partial\mathbf e_\theta}{\partial\theta} &= -\cos\phi\,\mathbf e_r + \sin\phi\,\mathbf e_\phi \quad &\text{(substitute $\mathbf e_R$)} \\
> \frac{\partial\mathbf e_\theta}{\partial\phi} &= \mathbf 0 \quad &\text{($\mathbf e_\theta$ does not contain $\phi$)} \\
> \frac{\partial\mathbf e_\phi}{\partial\theta} &= \sin\phi\sin\theta\,\mathbf i - \sin\phi\cos\theta\,\mathbf j \quad &\text{(derivatives of $\cos\theta$ and $\sin\theta$)} \\
> &= -\sin\phi\,\mathbf e_\theta \quad &\text{(factor $-\sin\phi$)} \\
> \frac{\partial\mathbf e_\phi}{\partial\phi} &= -\cos\phi\cos\theta\,\mathbf i - \cos\phi\sin\theta\,\mathbf j - \sin\phi\,\mathbf k \quad &\text{(derivatives of $-\sin\phi$ and $\cos\phi$)} \\
> &= -\mathbf e_r \quad &\text{(Eq. 2.32)}
> \end{aligned}$$
>
> $$\boxed{\frac{\partial\mathbf e_r}{\partial\theta} = \cos\phi\,\mathbf e_\theta,\quad \frac{\partial\mathbf e_r}{\partial\phi} = \mathbf e_\phi,\quad \frac{\partial\mathbf e_\theta}{\partial\theta} = -\cos\phi\,\mathbf e_r + \sin\phi\,\mathbf e_\phi,\quad \frac{\partial\mathbf e_\theta}{\partial\phi} = \mathbf 0,\quad \frac{\partial\mathbf e_\phi}{\partial\theta} = -\sin\phi\,\mathbf e_\theta,\quad \frac{\partial\mathbf e_\phi}{\partial\phi} = -\mathbf e_r}$$
>
> **Units:** $\mathrm{rad^{-1}}$
> **Meaning:** each partial derivative is perpendicular to its own unit vector, as it must be; $\mathbf e_\theta$ does not change along a meridian, and its derivative with respect to $\theta$ is $-\mathbf e_R$, pointing towards the axis $Oz$ at every latitude.

> [!derivation] Time derivatives of the spherical unit vectors
> **Law:** chain rule with the two variables $\theta(t)$ and $\phi(t)$; check with Eq. 1.62 and the angular velocity of the local basis
> **Source:** Notes.pdf, Eq. 2.33; Notes.pdf, Eq. 2.34; Notes.pdf, Eq. 2.35; Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 1.73
>
> In a time $dt$ the local basis turns $d\theta$ about $\mathbf k$ (plan view) and $d\phi$ about $-\mathbf e_\theta$ (meridian view); infinitesimal rotations add (Section 7), so its angular velocity is the sum of the two rates along their axes.
>
> $$\begin{aligned}
> \frac{d\mathbf e_r}{dt} &= \frac{\partial\mathbf e_r}{\partial\theta}\,\dot\theta + \frac{\partial\mathbf e_r}{\partial\phi}\,\dot\phi \quad &\text{(chain rule: $\mathbf e_r = \mathbf e_r(\theta(t),\phi(t))$)} \\
> &= \dot\theta\cos\phi\,\mathbf e_\theta + \dot\phi\,\mathbf e_\phi \quad &\text{(partial derivatives of the box above)} \\
> \frac{d\mathbf e_\theta}{dt} &= \frac{\partial\mathbf e_\theta}{\partial\theta}\,\dot\theta + \frac{\partial\mathbf e_\theta}{\partial\phi}\,\dot\phi \quad &\text{(chain rule)} \\
> &= -\dot\theta\cos\phi\,\mathbf e_r + \dot\theta\sin\phi\,\mathbf e_\phi \quad &\text{(partial derivatives; the second one is zero)} \\
> \frac{d\mathbf e_\phi}{dt} &= \frac{\partial\mathbf e_\phi}{\partial\theta}\,\dot\theta + \frac{\partial\mathbf e_\phi}{\partial\phi}\,\dot\phi \quad &\text{(chain rule)} \\
> &= -\dot\theta\sin\phi\,\mathbf e_\theta - \dot\phi\,\mathbf e_r \quad &\text{(partial derivatives)} \\
> \boldsymbol\omega_{\mathrm{sph}} &= \dot\theta\,\mathbf k - \dot\phi\,\mathbf e_\theta \quad &\text{(sum of the two rates of rotation, Eq. 1.73)} \\
> &= \dot\theta\sin\phi\,\mathbf e_r - \dot\phi\,\mathbf e_\theta + \dot\theta\cos\phi\,\mathbf e_\phi \quad &\text{(substitute $\mathbf k$ from the third row of $[{}_0R_{\mathrm{sph}}]$)} \\
> \boldsymbol\omega_{\mathrm{sph}}\times\mathbf e_r &= \dot\theta\sin\phi\,\mathbf e_r\times\mathbf e_r - \dot\phi\,\mathbf e_\theta\times\mathbf e_r + \dot\theta\cos\phi\,\mathbf e_\phi\times\mathbf e_r \quad &\text{(distribute, Eq. 1.32)} \\
> &= \dot\phi\,\mathbf e_\phi + \dot\theta\cos\phi\,\mathbf e_\theta \quad &\text{($\mathbf e_r\times\mathbf e_r = \mathbf 0$, $\mathbf e_\theta\times\mathbf e_r = -\mathbf e_\phi$, $\mathbf e_\phi\times\mathbf e_r = \mathbf e_\theta$)} \\
> \boldsymbol\omega_{\mathrm{sph}}\times\mathbf e_\theta &= \dot\theta\sin\phi\,\mathbf e_r\times\mathbf e_\theta - \dot\phi\,\mathbf e_\theta\times\mathbf e_\theta + \dot\theta\cos\phi\,\mathbf e_\phi\times\mathbf e_\theta \quad &\text{(distribute)} \\
> &= \dot\theta\sin\phi\,\mathbf e_\phi - \dot\theta\cos\phi\,\mathbf e_r \quad &\text{($\mathbf e_r\times\mathbf e_\theta = \mathbf e_\phi$, $\mathbf e_\theta\times\mathbf e_\theta = \mathbf 0$, $\mathbf e_\phi\times\mathbf e_\theta = -\mathbf e_r$)} \\
> \boldsymbol\omega_{\mathrm{sph}}\times\mathbf e_\phi &= \dot\theta\sin\phi\,\mathbf e_r\times\mathbf e_\phi - \dot\phi\,\mathbf e_\theta\times\mathbf e_\phi + \dot\theta\cos\phi\,\mathbf e_\phi\times\mathbf e_\phi \quad &\text{(distribute)} \\
> &= -\dot\theta\sin\phi\,\mathbf e_\theta - \dot\phi\,\mathbf e_r \quad &\text{($\mathbf e_r\times\mathbf e_\phi = -\mathbf e_\theta$, $\mathbf e_\theta\times\mathbf e_\phi = \mathbf e_r$, $\mathbf e_\phi\times\mathbf e_\phi = \mathbf 0$)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\mathbf e_r}{dt} = \dot\theta\cos\phi\,\mathbf e_\theta + \dot\phi\,\mathbf e_\phi,\quad \frac{d\mathbf e_\theta}{dt} = -\dot\theta\cos\phi\,\mathbf e_r + \dot\theta\sin\phi\,\mathbf e_\phi,\quad \frac{d\mathbf e_\phi}{dt} = -\dot\theta\sin\phi\,\mathbf e_\theta - \dot\phi\,\mathbf e_r;\qquad \boldsymbol\omega_{\mathrm{sph}} = \dot\theta\,\mathbf k - \dot\phi\,\mathbf e_\theta}$$
>
> **Units:** $\mathrm{rad/s}$ in every term
> **Meaning:** the three cross products reproduce the three chain-rule results, so the spherical basis rotates as a whole with $\boldsymbol\omega_{\mathrm{sph}}$, as Eq. 1.62 requires; the notes write the intermediate forms in $\mathbf i$, $\mathbf j$, $\mathbf k$ (Eqs. 2.33 to 2.35), which are the partial derivatives above before they are recognised as local vectors.

> [!derivation] Position and velocity in spherical coordinates
> **Law:** position vector rewritten in the local basis; definition of velocity; product rule
> **Source:** Notes.pdf, Eq. 2.36; Notes.pdf, Eq. 2.37; Notes.pdf, Eq. 2.33; [Lecture 1, Slide 22]
>
> $$\begin{aligned}
> \mathbf r_0^P &= r\cos\phi\cos\theta\,\mathbf i + r\cos\phi\sin\theta\,\mathbf j + r\sin\phi\,\mathbf k \quad &\text{(Eq. 2.31 in Eq. 2.5)} \\
> &= r\left(\cos\phi\cos\theta\,\mathbf i + \cos\phi\sin\theta\,\mathbf j + \sin\phi\,\mathbf k\right) \quad &\text{(factor $r$)} \\
> &= r\,\mathbf e_r \quad &\text{(Eq. 2.32)} \\
> \mathbf v_0^P &= \frac{d}{dt}\left(r\,\mathbf e_r\right) \quad &\text{(Eq. 2.3)} \\
> &= \dot r\,\mathbf e_r + r\,\frac{d\mathbf e_r}{dt} \quad &\text{(product rule, Eq. 1.64)} \\
> &= \dot r\,\mathbf e_r + r\left(\dot\theta\cos\phi\,\mathbf e_\theta + \dot\phi\,\mathbf e_\phi\right) \quad &\text{(Eq. 2.33)} \\
> &= \dot r\,\mathbf e_r + r\dot\theta\cos\phi\,\mathbf e_\theta + r\dot\phi\,\mathbf e_\phi \quad &\text{(distribute)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = r\,\mathbf e_r,\qquad \mathbf v_0^P = \dot r\,\mathbf e_r + r\dot\theta\cos\phi\,\mathbf e_\theta + r\dot\phi\,\mathbf e_\phi}$$
>
> **Units:** $\mathrm{m/s}$ in every term: $\dot r$, and lengths times $\mathrm{rad/s}$
> **Meaning:** the radial part stretches $\mathbf r_0^P$; the azimuthal part is the speed of a point on the parallel circle of radius $r\cos\phi$ turning at $\dot\theta$; the meridian part is the speed on the meridian circle of radius $r$ turning at $\dot\phi$.

> [!derivation] Acceleration in spherical coordinates
> **Law:** definition of acceleration; product rule term by term; chain rule; Eqs. 2.33 to 2.35
> **Source:** Notes.pdf, Eq. 2.38; Notes.pdf, Eq. 2.39; Notes.pdf, Eq. 2.40; [Lecture 1, Slide 22]
>
> $$\begin{aligned}
> \mathbf a_0^P &= \frac{d}{dt}\left(\dot r\,\mathbf e_r\right) + \frac{d}{dt}\left(r\dot\theta\cos\phi\,\mathbf e_\theta\right) + \frac{d}{dt}\left(r\dot\phi\,\mathbf e_\phi\right) \quad &\text{(Eq. 2.4 on Eq. 2.37; sum rule)} \\
> \frac{d}{dt}\left(\dot r\,\mathbf e_r\right) &= \ddot r\,\mathbf e_r + \dot r\,\frac{d\mathbf e_r}{dt} \quad &\text{(product rule)} \\
> &= \ddot r\,\mathbf e_r + \dot r\left(\dot\theta\cos\phi\,\mathbf e_\theta + \dot\phi\,\mathbf e_\phi\right) \quad &\text{(Eq. 2.33)} \\
> &= \ddot r\,\mathbf e_r + \dot r\dot\theta\cos\phi\,\mathbf e_\theta + \dot r\dot\phi\,\mathbf e_\phi \quad &\text{(distribute)} \\
> \frac{d}{dt}\left(r\dot\theta\cos\phi\,\mathbf e_\theta\right) &= \dot r\dot\theta\cos\phi\,\mathbf e_\theta + r\ddot\theta\cos\phi\,\mathbf e_\theta + r\dot\theta\,\frac{d\cos\phi}{dt}\,\mathbf e_\theta + r\dot\theta\cos\phi\,\frac{d\mathbf e_\theta}{dt} \quad &\text{(product rule for the four factors $r$, $\dot\theta$, $\cos\phi$, $\mathbf e_\theta$)} \\
> &= \dot r\dot\theta\cos\phi\,\mathbf e_\theta + r\ddot\theta\cos\phi\,\mathbf e_\theta - r\dot\theta\dot\phi\sin\phi\,\mathbf e_\theta + r\dot\theta\cos\phi\,\frac{d\mathbf e_\theta}{dt} \quad &\text{(chain rule: $\dfrac{d\cos\phi}{dt} = -\sin\phi\,\dot\phi$)} \\
> &= \dot r\dot\theta\cos\phi\,\mathbf e_\theta + r\ddot\theta\cos\phi\,\mathbf e_\theta - r\dot\theta\dot\phi\sin\phi\,\mathbf e_\theta + r\dot\theta\cos\phi\left(-\dot\theta\cos\phi\,\mathbf e_r + \dot\theta\sin\phi\,\mathbf e_\phi\right) \quad &\text{(Eq. 2.34)} \\
> &= \dot r\dot\theta\cos\phi\,\mathbf e_\theta + r\ddot\theta\cos\phi\,\mathbf e_\theta - r\dot\theta\dot\phi\sin\phi\,\mathbf e_\theta - r\dot\theta^2\cos^2\phi\,\mathbf e_r + r\dot\theta^2\cos\phi\sin\phi\,\mathbf e_\phi \quad &\text{(distribute)} \\
> \frac{d}{dt}\left(r\dot\phi\,\mathbf e_\phi\right) &= \dot r\dot\phi\,\mathbf e_\phi + r\ddot\phi\,\mathbf e_\phi + r\dot\phi\,\frac{d\mathbf e_\phi}{dt} \quad &\text{(product rule for the three factors $r$, $\dot\phi$, $\mathbf e_\phi$)} \\
> &= \dot r\dot\phi\,\mathbf e_\phi + r\ddot\phi\,\mathbf e_\phi + r\dot\phi\left(-\dot\theta\sin\phi\,\mathbf e_\theta - \dot\phi\,\mathbf e_r\right) \quad &\text{(Eq. 2.35)} \\
> &= \dot r\dot\phi\,\mathbf e_\phi + r\ddot\phi\,\mathbf e_\phi - r\dot\theta\dot\phi\sin\phi\,\mathbf e_\theta - r\dot\phi^2\,\mathbf e_r \quad &\text{(distribute)} \\
> \mathbf a_0^P &= \left(\ddot r - r\dot\theta^2\cos^2\phi - r\dot\phi^2\right)\mathbf e_r + \left(\dot r\dot\theta\cos\phi + \dot r\dot\theta\cos\phi + r\ddot\theta\cos\phi - r\dot\theta\dot\phi\sin\phi - r\dot\theta\dot\phi\sin\phi\right)\mathbf e_\theta + \left(\dot r\dot\phi + r\dot\theta^2\cos\phi\sin\phi + \dot r\dot\phi + r\ddot\phi\right)\mathbf e_\phi \quad &\text{(add the three results and collect by unit vector)} \\
> &= \left(\ddot r - r\dot\theta^2\cos^2\phi - r\dot\phi^2\right)\mathbf e_r + \left(2\dot r\dot\theta\cos\phi + r\ddot\theta\cos\phi - 2r\dot\theta\dot\phi\sin\phi\right)\mathbf e_\theta + \left(2\dot r\dot\phi + r\ddot\phi + r\dot\theta^2\cos\phi\sin\phi\right)\mathbf e_\phi \quad &\text{(add the equal terms)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \left(\ddot r - r\dot\theta^2\cos^2\phi - r\dot\phi^2\right)\mathbf e_r + \left(2\dot r\dot\theta\cos\phi + r\ddot\theta\cos\phi - 2r\dot\theta\dot\phi\sin\phi\right)\mathbf e_\theta + \left(2\dot r\dot\phi + r\ddot\phi + r\dot\theta^2\cos\phi\sin\phi\right)\mathbf e_\phi}$$
>
> **Units:** $\mathrm{m/s^2}$ in every term: each is a length times a squared rate or a length rate times a rate
> **Meaning:** for a motion that stays in the plane $Oxy$ (latitude and its rate zero) the result reduces to $(\ddot r - r\dot\theta^2)\,\mathbf e_r + (r\ddot\theta + 2\dot r\dot\theta)\,\mathbf e_\theta$, which is Eq. 2.30 with $r$ in place of $R$ and no height, as it must. The boxes below project the velocity and this acceleration with $[{}_0R_{\mathrm{sph}}]$ and compare them with [Lecture 1, Slide 22].

> [!derivation] The spherical velocity projected on the basis of S0
> **Law:** change of basis with $[{}_0R_{\mathrm{sph}}]$, row times column; check of the third component by direct differentiation
> **Source:** [Lecture 1, Slide 22]; Notes.pdf, Eq. 1.12; Notes.pdf, Eq. 2.37; Notes.pdf, Eq. 2.31
>
> The column of components in $\mathcal B_{\mathrm{sph}}$ is that of Eq. 2.37: the radial component $\dot r$, the azimuthal component $r\dot\theta\cos\phi$ and the meridian component $r\dot\phi$.
>
> $$\begin{aligned}
> [\mathbf v_0^P]_0 &= [{}_0R_{\mathrm{sph}}]\,[\mathbf v_0^P]_{\mathrm{sph}} \quad &\text{(Eq. 1.12)} \\
> &= \begin{pmatrix} \cos\phi\cos\theta\,\dot r + (-\sin\theta)\,r\dot\theta\cos\phi + (-\sin\phi\cos\theta)\,r\dot\phi \cr \cos\phi\sin\theta\,\dot r + \cos\theta\,r\dot\theta\cos\phi + (-\sin\phi\sin\theta)\,r\dot\phi \cr \sin\phi\,\dot r + 0\cdot r\dot\theta\cos\phi + \cos\phi\,r\dot\phi \end{pmatrix} \quad &\text{(rows of the matrix times the column of Eq. 2.37)} \\
> &= \begin{pmatrix} \dot r\cos\phi\cos\theta - r\dot\phi\sin\phi\cos\theta - r\dot\theta\cos\phi\sin\theta \cr \dot r\cos\phi\sin\theta - r\dot\phi\sin\phi\sin\theta + r\dot\theta\cos\phi\cos\theta \cr \dot r\sin\phi + r\dot\phi\cos\phi \end{pmatrix} \quad &\text{(drop the zero product; order the factors and terms as on the slide)} \\
> \dot z &= \frac{d}{dt}\left(r\sin\phi\right) \quad &\text{(Eq. 2.31)} \\
> &= \dot r\sin\phi + r\,\frac{d\sin\phi}{dt} \quad &\text{(product rule)} \\
> &= \dot r\sin\phi + r\dot\phi\cos\phi \quad &\text{(chain rule: $\dfrac{d\sin\phi}{dt} = \cos\phi\,\dot\phi$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \left(\dot r\cos\phi\cos\theta - r\dot\phi\sin\phi\cos\theta - r\dot\theta\cos\phi\sin\theta\right)\mathbf i + \left(\dot r\cos\phi\sin\theta - r\dot\phi\sin\phi\sin\theta + r\dot\theta\cos\phi\cos\theta\right)\mathbf j + \left(\dot r\sin\phi + r\dot\phi\cos\phi\right)\mathbf k}$$
>
> **Units:** $\mathrm{m/s}$ in every term: $\dot r$, and lengths times $\mathrm{rad/s}$
> **Meaning:** these are the Cartesian components printed on [Lecture 1, Slide 22], term by term, and the third one agrees with the derivative of the height taken without the local basis. At the latitude zero the $\mathbf k$ component is $r\dot\phi$, the meridian part of the velocity, which is then vertical.

> [!derivation] The spherical acceleration projected on the basis of S0: the i component
> **Law:** first row of $[{}_0R_{\mathrm{sph}}]$ times the column of the acceleration; Pythagoras
> **Source:** [Lecture 1, Slide 22]; Notes.pdf, Eq. 1.12; Notes.pdf, Eq. 2.38; Notes.pdf, Eq. 2.39; Notes.pdf, Eq. 2.40
>
> The column of components in $\mathcal B_{\mathrm{sph}}$ is that of the box "Acceleration in spherical coordinates" (Eqs. 2.38 to 2.40), in the order radial, azimuthal, meridian.
>
> $$\begin{aligned}
> a_x &= \cos\phi\cos\theta\,\left(\ddot r - r\dot\theta^2\cos^2\phi - r\dot\phi^2\right) + (-\sin\theta)\,\left(2\dot r\dot\theta\cos\phi + r\ddot\theta\cos\phi - 2r\dot\theta\dot\phi\sin\phi\right) + (-\sin\phi\cos\theta)\,\left(2\dot r\dot\phi + r\ddot\phi + r\dot\theta^2\cos\phi\sin\phi\right) \quad &\text{(first row of $[{}_0R_{\mathrm{sph}}]$ times the column, Eq. 1.12)} \\
> &= \ddot r\cos\phi\cos\theta - r\dot\theta^2\cos^3\phi\cos\theta - r\dot\phi^2\cos\phi\cos\theta - 2\dot r\dot\theta\cos\phi\sin\theta - r\ddot\theta\cos\phi\sin\theta + 2r\dot\theta\dot\phi\sin\phi\sin\theta - 2\dot r\dot\phi\sin\phi\cos\theta - r\ddot\phi\sin\phi\cos\theta - r\dot\theta^2\cos\phi\sin^2\phi\cos\theta \quad &\text{(distribute the three products)} \\
> &= \ddot r\cos\phi\cos\theta - r\dot\phi^2\cos\phi\cos\theta - 2\dot r\dot\theta\cos\phi\sin\theta - r\ddot\theta\cos\phi\sin\theta + 2r\dot\theta\dot\phi\sin\phi\sin\theta - 2\dot r\dot\phi\sin\phi\cos\theta - r\ddot\phi\sin\phi\cos\theta - r\dot\theta^2\cos\phi\cos\theta\left(\cos^2\phi + \sin^2\phi\right) \quad &\text{(group the two terms in $\dot\theta^2$)} \\
> &= \ddot r\cos\phi\cos\theta - 2\dot r\dot\phi\sin\phi\cos\theta - 2\dot r\dot\theta\cos\phi\sin\theta - r\ddot\phi\sin\phi\cos\theta - r\dot\phi^2\cos\phi\cos\theta + 2r\dot\phi\dot\theta\sin\phi\sin\theta - r\ddot\theta\cos\phi\sin\theta - r\dot\theta^2\cos\phi\cos\theta \quad &\text{(Pythagoras; terms in the order of the slide)}
> \end{aligned}$$
>
> $$\boxed{a_x = \ddot r\cos\phi\cos\theta - 2\dot r\dot\phi\sin\phi\cos\theta - 2\dot r\dot\theta\cos\phi\sin\theta - r\ddot\phi\sin\phi\cos\theta - r\dot\phi^2\cos\phi\cos\theta + 2r\dot\phi\dot\theta\sin\phi\sin\theta - r\ddot\theta\cos\phi\sin\theta - r\dot\theta^2\cos\phi\cos\theta}$$
>
> **Units:** $\mathrm{m/s^2}$ in every term
> **Meaning:** this is the $\mathbf i$ component printed on [Lecture 1, Slide 22], term by term; the term in $\dot\theta^2$ reduces to the centripetal acceleration of the parallel circle, of radius $r\cos\phi$, projected on $\mathbf i$.

> [!derivation] The spherical acceleration projected on the basis of S0: the j component
> **Law:** second row of $[{}_0R_{\mathrm{sph}}]$ times the column of the acceleration; Pythagoras
> **Source:** [Lecture 1, Slide 22]; Notes.pdf, Eq. 1.12; Notes.pdf, Eq. 2.38; Notes.pdf, Eq. 2.39; Notes.pdf, Eq. 2.40
>
> $$\begin{aligned}
> a_y &= \cos\phi\sin\theta\,\left(\ddot r - r\dot\theta^2\cos^2\phi - r\dot\phi^2\right) + \cos\theta\,\left(2\dot r\dot\theta\cos\phi + r\ddot\theta\cos\phi - 2r\dot\theta\dot\phi\sin\phi\right) + (-\sin\phi\sin\theta)\,\left(2\dot r\dot\phi + r\ddot\phi + r\dot\theta^2\cos\phi\sin\phi\right) \quad &\text{(second row of $[{}_0R_{\mathrm{sph}}]$ times the column, Eq. 1.12)} \\
> &= \ddot r\cos\phi\sin\theta - r\dot\theta^2\cos^3\phi\sin\theta - r\dot\phi^2\cos\phi\sin\theta + 2\dot r\dot\theta\cos\phi\cos\theta + r\ddot\theta\cos\phi\cos\theta - 2r\dot\theta\dot\phi\sin\phi\cos\theta - 2\dot r\dot\phi\sin\phi\sin\theta - r\ddot\phi\sin\phi\sin\theta - r\dot\theta^2\cos\phi\sin^2\phi\sin\theta \quad &\text{(distribute the three products)} \\
> &= \ddot r\cos\phi\sin\theta - r\dot\phi^2\cos\phi\sin\theta + 2\dot r\dot\theta\cos\phi\cos\theta + r\ddot\theta\cos\phi\cos\theta - 2r\dot\theta\dot\phi\sin\phi\cos\theta - 2\dot r\dot\phi\sin\phi\sin\theta - r\ddot\phi\sin\phi\sin\theta - r\dot\theta^2\cos\phi\sin\theta\left(\cos^2\phi + \sin^2\phi\right) \quad &\text{(group the two terms in $\dot\theta^2$)} \\
> &= \ddot r\cos\phi\sin\theta - 2\dot r\dot\phi\sin\phi\sin\theta + 2\dot r\dot\theta\cos\phi\cos\theta - r\ddot\phi\sin\phi\sin\theta - r\dot\phi^2\cos\phi\sin\theta - 2r\dot\phi\dot\theta\sin\phi\cos\theta + r\ddot\theta\cos\phi\cos\theta - r\dot\theta^2\cos\phi\sin\theta \quad &\text{(Pythagoras; terms in the order of the slide)}
> \end{aligned}$$
>
> $$\boxed{a_y = \ddot r\cos\phi\sin\theta - 2\dot r\dot\phi\sin\phi\sin\theta + 2\dot r\dot\theta\cos\phi\cos\theta - r\ddot\phi\sin\phi\sin\theta - r\dot\phi^2\cos\phi\sin\theta - 2r\dot\phi\dot\theta\sin\phi\cos\theta + r\ddot\theta\cos\phi\cos\theta - r\dot\theta^2\cos\phi\sin\theta}$$
>
> **Units:** $\mathrm{m/s^2}$ in every term
> **Meaning:** this is the $\mathbf j$ component printed on [Lecture 1, Slide 22], term by term; it follows from the $\mathbf i$ component by replacing the cosine of the azimuth by its sine and the sine by minus the cosine (the azimuth decreased by a right angle), as the symmetry about $Oz$ requires.

> [!derivation] The spherical acceleration projected on the basis of S0: the k component
> **Law:** third row of $[{}_0R_{\mathrm{sph}}]$ times the column of the acceleration
> **Source:** [Lecture 1, Slide 22]; Notes.pdf, Eq. 1.12; Notes.pdf, Eq. 2.38; Notes.pdf, Eq. 2.40
>
> $$\begin{aligned}
> a_z &= \sin\phi\,\left(\ddot r - r\dot\theta^2\cos^2\phi - r\dot\phi^2\right) + 0\cdot \left(2\dot r\dot\theta\cos\phi + r\ddot\theta\cos\phi - 2r\dot\theta\dot\phi\sin\phi\right) + \cos\phi\,\left(2\dot r\dot\phi + r\ddot\phi + r\dot\theta^2\cos\phi\sin\phi\right) \quad &\text{(third row of $[{}_0R_{\mathrm{sph}}]$ times the column, Eq. 1.12)} \\
> &= \sin\phi\,\left(\ddot r - r\dot\theta^2\cos^2\phi - r\dot\phi^2\right) + \cos\phi\,\left(2\dot r\dot\phi + r\ddot\phi + r\dot\theta^2\cos\phi\sin\phi\right) \quad &\text{(drop the zero product)} \\
> &= \ddot r\sin\phi - r\dot\theta^2\cos^2\phi\sin\phi - r\dot\phi^2\sin\phi + 2\dot r\dot\phi\cos\phi + r\ddot\phi\cos\phi + r\dot\theta^2\cos^2\phi\sin\phi \quad &\text{(distribute the two products)} \\
> &= \ddot r\sin\phi + 2\dot r\dot\phi\cos\phi + r\ddot\phi\cos\phi - r\dot\phi^2\sin\phi \quad &\text{(the two terms in $\dot\theta^2$ cancel; order of the slide)}
> \end{aligned}$$
>
> $$\boxed{a_z = \ddot r\sin\phi + 2\dot r\dot\phi\cos\phi + r\ddot\phi\cos\phi - r\dot\phi^2\sin\phi}$$
>
> **Units:** $\mathrm{m/s^2}$ in every term
> **Meaning:** this is the $\mathbf k$ component printed on [Lecture 1, Slide 22], term by term. The azimuthal rate does not appear: turning about $Oz$ moves $P$ on a horizontal circle, whose centripetal acceleration is horizontal.

## 15. Degrees of freedom and constraints

The word coordinate is also used in a broader sense. The configuration degrees of freedom of a mechanical system are the number of independent parameters, or generalized coordinates, that must be given to determine fully the position and orientation of all its parts (Notes.pdf, Sec. 2.7). Any parameters that locate a point in space unambiguously will do as coordinates: angles, areas, distances. When a point cannot move freely in space, because it must stay on a surface or a line, or because several particles are related, for example by a string, the possible configurations are described with the minimum number of coordinates; that minimum is the number of configuration degrees of freedom, and the space of all possible values of the chosen coordinates is the configuration space ([Lecture 1, Slide 23]).

| System | Coordinates needed | Source |
| :--- | :--- | :--- |
| free point particle in space | 3 | Notes.pdf, Sec. 2.7 |
| rigid body in space (an aircraft) | 6: three position coordinates of one point and three angular coordinates (Chapter 9) | Notes.pdf, Sec. 2.7 |
| point particle constrained to a plane, or to a surface, $\mathbf r_0^P(q_1,q_2)$ | 2 | Notes.pdf, Sec. 2.7; [Lecture 1, Slide 23] |
| flat plate confined to a plane | 3: two position coordinates of one point and one angle | Notes.pdf, Sec. 2.7 |
| point particle on a curve (a bead sliding on a wire), $\mathbf r_0^P(q_1)$ | 1 | Notes.pdf, Sec. 2.7; [Lecture 1, Slide 23] |
| two particles joined by a string over a pulley | the string ties their motions: equal and opposite displacements | Notes.pdf, Sec. 2.7 |

The number of independent coordinates falls below these values either because the number of spatial dimensions is reduced or because relationships are specified among the coordinates; it is useful to think of those relationships as constraints. A particle on a surface or on a curve needs as many coordinates as the dimension of the underlying object ([Lecture 1, Slide 23]). Chapter 6 (Topic 3) adds the reaction forces that enforce the constraints.

![[attachments/EM-T/t1-constraints.svg]]

> [!derivation] A particle on a sphere and a bead on a circular wire
> **Law:** each constraint equation removes one independent coordinate; Eqs. 2.28, 2.29, 2.36 and 2.37 with the constrained coordinates held fixed
> **Source:** Notes.pdf, Sec. 2.7; [Lecture 1, Slide 23]; Notes.pdf, Eq. 2.31; Notes.pdf, Eq. 2.37; Notes.pdf, Eq. 2.29
>
> Sphere: $P$ stays on a sphere of radius $R_0$ centred at $O$. Wire: $P$ is a bead on a circular wire of radius $R_0$ in the plane $Oxy$, centred at $O$.
>
> $$\begin{aligned}
> x^2 + y^2 + z^2 &= R_0^2 \quad &\text{(sphere: one equation among the three Cartesian coordinates)} \\
> r &= R_0 \quad &\text{(Eq. 2.31: the same constraint in spherical coordinates)} \\
> \mathbf r_0^P &= R_0\,\mathbf e_r(\theta,\phi) \quad &\text{(Eq. 2.36: only $\theta$ and $\phi$ remain free)} \\
> \mathbf v_0^P &= R_0\dot\theta\cos\phi\,\mathbf e_\theta + R_0\dot\phi\,\mathbf e_\phi \quad &\text{(Eq. 2.37 with $\dot r = 0$)} \\
> z = 0,\qquad R &= R_0 \quad &\text{(wire: two equations, the plane and the circle, in cylindrical coordinates)} \\
> \mathbf r_0^P &= R_0\,\mathbf e_R(\theta) \quad &\text{(Eq. 2.28: only $\theta$ remains free)} \\
> \mathbf v_0^P &= R_0\dot\theta\,\mathbf e_\theta \quad &\text{(Eq. 2.29 with $\dot R = 0$ and $\dot z = 0$)}
> \end{aligned}$$
>
> $$\boxed{\text{sphere: } 3 - 1 = 2 \text{ degrees of freedom},\ q_1 = \theta,\ q_2 = \phi;\qquad \text{wire: } 3 - 2 = 1 \text{ degree of freedom},\ q_1 = \theta}$$
>
> **Units:** $R_0$ in $\mathrm m$, angles in $\mathrm{rad}$, velocities in $\mathrm{m/s}$
> **Meaning:** choosing coordinates in which the constraints fix some coordinates leaves exactly the free ones as generalized coordinates; the velocity then has no component along the constrained directions ($\mathbf e_r$ on the sphere, $\mathbf e_R$ and $\mathbf e_z$ on the wire).

> [!derivation] Two particles joined by a string over a pulley
> **Law:** constant length of an inextensible string; time derivative of the constraint
> **Source:** Notes.pdf, Sec. 2.7; [Lecture 1, Slide 23]
>
> Two particles hang on the two sides of a fixed pulley from an inextensible string of length $L$, each moving along its own vertical line; $d_1$ and $d_2$ are their depths below the axis of the pulley, and $L_0$ is the constant length of string in contact with the pulley.
>
> $$\begin{aligned}
> d_1 + d_2 + L_0 &= L \quad &\text{(the string does not stretch)} \\
> \dot d_1 + \dot d_2 &= 0 \quad &\text{(time derivative; $L$ and $L_0$ are constant)} \\
> \dot d_2 &= -\dot d_1 \quad &\text{(solve for $\dot d_2$)}
> \end{aligned}$$
>
> $$\boxed{d_2 = L - L_0 - d_1,\qquad \dot d_2 = -\dot d_1:\quad 2 - 1 = 1 \text{ degree of freedom}}$$
>
> **Units:** $\mathrm m$ and $\mathrm{m/s}$
> **Meaning:** when one particle goes down the other goes up by the same amount, at the same speed: the motions are equal and opposite, and one coordinate, $d_1$, describes the whole system.

We are not restricted to Cartesian, cylindrical or spherical coordinates for positions and angles for orientations: other valid sets of parameters, such as distances or areas, can determine the configuration, and when they are chosen they are called generalized coordinates (Notes.pdf, Sec. 2.7; [Lecture 1, Slide 23]). Analytical mechanics uses generalized coordinates to reduce the equations of motion to their simplest form systematically; it is beyond the scope of the course and is not one of its tools (Notes.pdf, Sec. 2.7, footnote 13).

## 16. Worked example: the helical rocket

> [!example] Out-of-control rocket on a helix ([Lecture 1, Slide 29])
> An out-of-control rocket, modelled as a point particle, traces an upward helical trajectory described in Cartesian coordinates of $S_0$ for positive times by the functions of the table, where $a$, $v_z$ and $\omega$ are constants. (a) Express the position, velocity and acceleration vectors in the Cartesian system with the unit vectors $\mathbf i$, $\mathbf j$, $\mathbf k$. (b) Express them in the cylindrical coordinate system with $\mathbf e_R$, $\mathbf e_\theta$, $\mathbf e_z$. (c) Express the velocity and the acceleration with the intrinsic coordinates $s$, $\rho$ and the basis $\mathbf e_t$, $\mathbf e_n$, $\mathbf e_b$. (d) Compute the modulus of the velocity. (e) Express the arc length coordinate as a function of time. (f) Write the trajectory as a function of the arc length. (g) Find the centre of curvature when the particle is at the point $(a, 0, 0)$.

| Datum | Meaning |
| :--- | :--- |
| $x = a\cos(\omega t)$, $y = a\sin(\omega t)$, $z = v_z t$ | Eqs. (1) to (3) of the slide |
| $a$ (m), positive | radius of the helix |
| $\omega$ (rad/s), positive | constant angular rate about $Oz$ (the magnitude of $\boldsymbol\omega_{\mathrm{cyl}}$) |
| $v_z$ (m/s), positive | constant rate of climb |

![[attachments/EM-T/t1-helix.svg]]

> [!derivation] (a) Position, velocity and acceleration in the Cartesian basis
> **Law:** Cartesian components; chain rule on the trigonometric functions of $\omega t$
> **Source:** Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.7; [Lecture 1, Slide 29]
>
> $$\begin{aligned}
> \mathbf r_0^P &= a\cos(\omega t)\,\mathbf i + a\sin(\omega t)\,\mathbf j + v_z t\,\mathbf k \quad &\text{(Eq. 2.5 with the data)} \\
> \dot x &= a\,\frac{d\cos(\omega t)}{d(\omega t)}\,\frac{d(\omega t)}{dt} \quad &\text{(chain rule)} \\
> &= -a\omega\sin(\omega t) \quad &\text{(derivative of the cosine; $\omega$ constant)} \\
> \dot y &= a\,\frac{d\sin(\omega t)}{d(\omega t)}\,\frac{d(\omega t)}{dt} \quad &\text{(chain rule)} \\
> &= a\omega\cos(\omega t) \quad &\text{(derivative of the sine)} \\
> \dot z &= v_z \quad &\text{(derivative of $v_z t$)} \\
> \ddot x &= -a\omega\cos(\omega t)\,\omega \quad &\text{(chain rule on $\dot x$)} \\
> \ddot y &= -a\omega\sin(\omega t)\,\omega \quad &\text{(chain rule on $\dot y$)} \\
> \ddot z &= 0 \quad &\text{($v_z$ is constant)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = -a\omega\sin(\omega t)\,\mathbf i + a\omega\cos(\omega t)\,\mathbf j + v_z\,\mathbf k,\qquad \mathbf a_0^P = -a\omega^2\cos(\omega t)\,\mathbf i - a\omega^2\sin(\omega t)\,\mathbf j}$$
>
> **Units:** $a\omega$ and $v_z$ in $\mathrm{m/s}$; $a\omega^2$ in $\mathrm{m/s^2}$
> **Meaning:** the acceleration is horizontal and points from $P$ to the axis $Oz$: its components are those of the horizontal part of $\mathbf r_0^P$ times $-\omega^2$.

> [!derivation] (b) Position, velocity and acceleration in the cylindrical basis
> **Law:** transformation relations; position in the local basis; product rule with the derivatives of the cylindrical unit vectors; check with the inverse change of basis
> **Source:** Notes.pdf, Eq. 2.23; Notes.pdf, Eq. 2.24; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26; Notes.pdf, Eq. 2.27; Notes.pdf, Eq. 1.64; Notes.pdf, Eq. 1.14
>
> $$\begin{aligned}
> R &= \sqrt{a^2\cos^2(\omega t) + a^2\sin^2(\omega t)} \quad &\text{(Eq. 2.23)} \\
> &= a \quad &\text{(Pythagoras; $a$ is positive)} \\
> \theta &= \arctan\frac{a\sin(\omega t)}{a\cos(\omega t)} \quad &\text{(Eq. 2.23)} \\
> &= \omega t \quad &\text{(the signs of $x$ and $y$ put $\theta$ in the quadrant of $\omega t$; $\theta$ is taken continuous in time)} \\
> \dot\theta &= \omega \quad &\text{(derivative of $\omega t$; $\omega$ constant)} \\
> \mathbf r_0^P &= a\cos(\omega t)\,\mathbf i + a\sin(\omega t)\,\mathbf j + v_z t\,\mathbf k \quad &\text{(part (a))} \\
> &= a\left(\cos\theta\,\mathbf i + \sin\theta\,\mathbf j\right) + v_z t\,\mathbf k \quad &\text{(factor $a$; $\theta = \omega t$)} \\
> &= a\,\mathbf e_R + v_z t\,\mathbf e_z \quad &\text{(Eq. 2.24)} \\
> \mathbf v_0^P &= \frac{d}{dt}\left(a\,\mathbf e_R\right) + \frac{d}{dt}\left(v_z t\,\mathbf e_z\right) \quad &\text{(Eq. 2.3; sum rule, Eq. 1.65)} \\
> &= 0\,\mathbf e_R + a\,\frac{d\mathbf e_R}{dt} + v_z\,\mathbf e_z + v_z t\,\frac{d\mathbf e_z}{dt} \quad &\text{(product rule on both terms, Eq. 1.64; $a$ constant, the derivative of $v_z t$ is $v_z$)} \\
> &= a\dot\theta\,\mathbf e_\theta + v_z\,\mathbf e_z + \mathbf 0 \quad &\text{(Eqs. 2.25 and 2.27)} \\
> &= a\omega\,\mathbf e_\theta + v_z\,\mathbf e_z \quad &\text{($\dot\theta = \omega$)} \\
> \mathbf a_0^P &= \frac{d}{dt}\left(a\omega\,\mathbf e_\theta\right) + \frac{d}{dt}\left(v_z\,\mathbf e_z\right) \quad &\text{(Eq. 2.4; sum rule)} \\
> &= a\omega\,\frac{d\mathbf e_\theta}{dt} + v_z\,\frac{d\mathbf e_z}{dt} \quad &\text{(product rule; $a\omega$ and $v_z$ are constant)} \\
> &= a\omega\left(-\dot\theta\,\mathbf e_R\right) + v_z\,\mathbf 0 \quad &\text{(Eqs. 2.26 and 2.27)} \\
> &= -a\omega^2\,\mathbf e_R \quad &\text{($\dot\theta = \omega$)} \\
> [{}_{\mathrm{cyl}}R_0] &= [{}_0R_{\mathrm{cyl}}]^T \quad &\text{(Eq. 1.14)} \\
> \left([\mathbf a_0^P]_{\mathrm{cyl}}\right)_1 &= \cos(\omega t)\left(-a\omega^2\cos(\omega t)\right) + \sin(\omega t)\left(-a\omega^2\sin(\omega t)\right) + 0\cdot 0 \quad &\text{(first row of $[{}_{\mathrm{cyl}}R_0]$ times the Cartesian column of part (a))} \\
> &= -a\omega^2 \quad &\text{(Pythagoras)} \\
> \left([\mathbf a_0^P]_{\mathrm{cyl}}\right)_2 &= -\sin(\omega t)\left(-a\omega^2\cos(\omega t)\right) + \cos(\omega t)\left(-a\omega^2\sin(\omega t)\right) + 0\cdot 0 \quad &\text{(second row times the same column)} \\
> &= 0 \quad &\text{(the two products cancel)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = a\,\mathbf e_R + v_z t\,\mathbf e_z,\qquad \mathbf v_0^P = a\omega\,\mathbf e_\theta + v_z\,\mathbf e_z,\qquad \mathbf a_0^P = -a\omega^2\,\mathbf e_R,\qquad \theta = \omega t}$$
>
> **Units:** $\mathrm m$, $\mathrm{m/s}$, $\mathrm{m/s^2}$
> **Meaning:** the rocket stays on the cylinder of radius $a$ about $Oz$; the projection of the Cartesian acceleration of part (a) agrees with the acceleration obtained with the local basis, which is also what Eq. 2.30 gives for a constant radius, azimuthal rate and climb rate: the only acceleration is the centripetal term, directed to the axis.

> [!derivation] (c, d) Velocity in the intrinsic basis and its modulus
> **Law:** speed as the magnitude of the velocity; Eq. 2.16
> **Source:** Notes.pdf, Eq. 2.16; Notes.pdf, Eq. 1.40; [Lecture 1, Slide 28]
>
> $$\begin{aligned}
> \lvert\mathbf v_0^P\rvert^2 &= \mathbf v_0^P\cdot\mathbf v_0^P \quad &\text{(magnitude from the dot product)} \\
> &= (a\omega)^2 + v_z^2 \quad &\text{(components in the orthonormal basis $\mathcal B_{\mathrm{cyl}}$, Eq. 1.40)} \\
> \dot s &= \sqrt{a^2\omega^2 + v_z^2} \quad &\text{(Eq. 2.16: the speed, with $s$ growing along the motion)} \\
> \mathbf e_t &= \frac{\mathbf v_0^P}{\dot s} \quad &\text{(Eq. 2.16 divided by $\dot s$)} \\
> &= \frac{a\omega\,\mathbf e_\theta + v_z\,\mathbf e_z}{\sqrt{a^2\omega^2 + v_z^2}} \quad &\text{(part (b))}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \dot s\,\mathbf e_t,\qquad \lvert\mathbf v_0^P\rvert = \dot s = \sqrt{a^2\omega^2 + v_z^2},\qquad \mathbf e_t = \frac{a\omega\,\mathbf e_\theta + v_z\,\mathbf e_z}{\sqrt{a^2\omega^2 + v_z^2}}}$$
>
> **Units:** $\mathrm{m/s}$; $\mathbf e_t$ dimensionless
> **Meaning:** the speed is constant, and the tangent keeps a constant angle with the horizontal plane, whose tangent is the ratio of the climb rate to the circumferential speed.

> [!derivation] (c) Acceleration in the intrinsic basis: curvature and normal vector
> **Law:** chain rule from $t$ to $s$; Eqs. 2.11, 2.12, 2.17 and 2.18
> **Source:** Notes.pdf, Eq. 2.11; Notes.pdf, Eq. 2.12; Notes.pdf, Eq. 2.17; Notes.pdf, Eq. 2.18; Notes.pdf, Eq. 2.26; Notes.pdf, Eq. 2.27
>
> $$\begin{aligned}
> \frac{d\mathbf e_t}{dt} &= \frac{1}{\dot s}\left(a\omega\,\frac{d\mathbf e_\theta}{dt} + v_z\,\frac{d\mathbf e_z}{dt}\right) \quad &\text{($a$, $\omega$, $v_z$ and $\dot s$ are constant)} \\
> &= \frac{1}{\dot s}\left(a\omega\left(-\omega\,\mathbf e_R\right) + v_z\,\mathbf 0\right) \quad &\text{(Eqs. 2.26 and 2.27 with $\dot\theta = \omega$)} \\
> &= -\frac{a\omega^2}{\dot s}\,\mathbf e_R \quad &\text{(simplify)} \\
> \frac{d\mathbf e_t}{ds} &= \frac{1}{\dot s}\,\frac{d\mathbf e_t}{dt} \quad &\text{(chain rule: $\dfrac{d\mathbf e_t}{dt} = \dfrac{d\mathbf e_t}{ds}\,\dot s$)} \\
> &= -\frac{a\omega^2}{a^2\omega^2 + v_z^2}\,\mathbf e_R \quad &\text{($\dot s^2 = a^2\omega^2 + v_z^2$)} \\
> \kappa &= \frac{a\omega^2}{a^2\omega^2 + v_z^2} \quad &\text{(magnitude, Eq. 2.12)} \\
> \mathbf e_n &= -\mathbf e_R \quad &\text{(direction, Eq. 2.11)} \\
> \rho &= \frac{a^2\omega^2 + v_z^2}{a\omega^2} \quad &\text{(inverse of $\kappa$, Eq. 2.12)} \\
> a_t &= \ddot s = 0 \quad &\text{($\dot s$ is constant, Eq. 2.18)} \\
> a_n &= \frac{\dot s^2}{\rho} \quad &\text{(Eq. 2.18)} \\
> &= \left(a^2\omega^2 + v_z^2\right)\frac{a\omega^2}{a^2\omega^2 + v_z^2} \quad &\text{(substitute $\dot s^2$ and $\rho$)} \\
> &= a\omega^2 \quad &\text{(cancel)} \\
> \mathbf a_0^P &= 0\,\mathbf e_t + a\omega^2\,\mathbf e_n \quad &\text{(Eq. 2.17)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \frac{\dot s^2}{\rho}\,\mathbf e_n = a\omega^2\,\mathbf e_n,\qquad \mathbf e_n = -\mathbf e_R,\qquad \rho = \frac{a^2\omega^2 + v_z^2}{a\omega^2} = a + \frac{v_z^2}{a\omega^2}}$$
>
> **Units:** $\kappa$ in $\mathrm{m^{-1}}$; $\rho$ in $\mathrm m$: $(\mathrm{m^2/s^2})/(\mathrm{m/s^2})$; $a_n$ in $\mathrm{m/s^2}$
> **Meaning:** with $\mathbf e_n$ equal to $-\mathbf e_R$ this is the acceleration of part (b); the radius of curvature exceeds the radius of the cylinder because the climb stretches the curve, and it tends to $a$ (a horizontal circle) as $v_z$ tends to zero.

> [!derivation] (c) Binormal vector, and a check of the Frenet-Serret formulas
> **Law:** definition of the binormal; cross products in the right-handed basis $\mathcal B_{\mathrm{cyl}}$; Eq. 2.15
> **Source:** Notes.pdf, Eq. 2.13; Notes.pdf, Eq. 2.15; Notes.pdf, Eq. 2.26; Notes.pdf, Eq. 1.32
>
> $$\begin{aligned}
> \mathbf e_b &= \mathbf e_t\times\mathbf e_n \quad &\text{(definition)} \\
> &= \frac{1}{\dot s}\left(a\omega\,\mathbf e_\theta + v_z\,\mathbf e_z\right)\times\left(-\mathbf e_R\right) \quad &\text{(substitute $\mathbf e_t$ and $\mathbf e_n$)} \\
> &= \frac{1}{\dot s}\left(-a\omega\,\mathbf e_\theta\times\mathbf e_R - v_z\,\mathbf e_z\times\mathbf e_R\right) \quad &\text{(distribute, Eq. 1.32)} \\
> &= \frac{1}{\dot s}\left(a\omega\,\mathbf e_z - v_z\,\mathbf e_\theta\right) \quad &\text{($\mathbf e_\theta\times\mathbf e_R = -\mathbf e_z$, $\mathbf e_z\times\mathbf e_R = \mathbf e_\theta$)} \\
> \frac{d\mathbf e_b}{dt} &= \frac{1}{\dot s}\left(a\omega\,\mathbf 0 - v_z\left(-\omega\,\mathbf e_R\right)\right) \quad &\text{(Eqs. 2.26 and 2.27)} \\
> &= \frac{v_z\omega}{\dot s}\,\mathbf e_R \quad &\text{(simplify)} \\
> \frac{d\mathbf e_b}{ds} &= \frac{v_z\omega}{\dot s^2}\,\mathbf e_R \quad &\text{(chain rule: divide by $\dot s$)} \\
> &= -\frac{v_z\omega}{a^2\omega^2 + v_z^2}\,\mathbf e_n \quad &\text{($\mathbf e_R = -\mathbf e_n$)} \\
> \tau &= \frac{v_z\omega}{a^2\omega^2 + v_z^2} \quad &\text{(compare with the third Frenet-Serret formula, Eq. 2.15)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_b = \frac{a\omega\,\mathbf e_z - v_z\,\mathbf e_\theta}{\sqrt{a^2\omega^2 + v_z^2}},\qquad \tau = \frac{v_z\omega}{a^2\omega^2 + v_z^2}}$$
>
> **Units:** $\tau$ in $(\mathrm{m/s})(\mathrm{rad/s})/(\mathrm{m^2/s^2}) = \mathrm{m^{-1}}$
> **Meaning:** the derivative of $\mathbf e_b$ lies along $\mathbf e_n$, as Eq. 2.15 requires; the torsion is the extra result of this box (the slide does not ask for it), positive for a climbing helix and zero when $v_z$ vanishes and the path becomes the planar circle.

> [!derivation] (e, f) Time law and trajectory as a function of the arc length
> **Law:** integration of the speed with Barrow's rule; substitution of the inverse time law
> **Source:** Notes.pdf, Eq. 2.16; Notes.pdf, Sec. 2.3; Notes.pdf, Eq. 2.9
>
> The origin of $s$ is the point of the trajectory at the initial instant, $(a, 0, 0)$.
>
> $$\begin{aligned}
> \int_0^t\frac{ds}{dt'}\,dt' &= \int_0^t\sqrt{a^2\omega^2 + v_z^2}\,dt' \quad &\text{(integrate the speed of part (d) from $0$ to $t$)} \\
> \left[\,s\,\right]_0^t &= \left[\sqrt{a^2\omega^2 + v_z^2}\;t'\right]_0^t \quad &\text{(antiderivatives: $s$, and the constant times $t'$)} \\
> s(t) - s(0) &= \sqrt{a^2\omega^2 + v_z^2}\;t - 0 \quad &\text{(Barrow's rule)} \\
> s(t) &= \dot s\,t \quad &\text{($s(0) = 0$; $\dot s$ is the constant speed)} \\
> t &= \frac{s}{\dot s} \quad &\text{(invert the time law)} \\
> \mathbf r_0^P(s) &= a\cos\frac{\omega s}{\dot s}\,\mathbf i + a\sin\frac{\omega s}{\dot s}\,\mathbf j + \frac{v_z s}{\dot s}\,\mathbf k \quad &\text{(substitute $t$ in the position of part (a))} \\
> \frac{d\mathbf r_0^P}{ds} &= -\frac{a\omega}{\dot s}\sin\frac{\omega s}{\dot s}\,\mathbf i + \frac{a\omega}{\dot s}\cos\frac{\omega s}{\dot s}\,\mathbf j + \frac{v_z}{\dot s}\,\mathbf k \quad &\text{(chain rule on each component)} \\
> \left\lvert\frac{d\mathbf r_0^P}{ds}\right\rvert^2 &= \frac{a^2\omega^2\left(\sin^2 + \cos^2\right) + v_z^2}{\dot s^2} \quad &\text{(sum of the squared components)} \\
> &= 1 \quad &\text{(Pythagoras; $\dot s^2 = a^2\omega^2 + v_z^2$)}
> \end{aligned}$$
>
> $$\boxed{s(t) = \sqrt{a^2\omega^2 + v_z^2}\;t,\qquad \mathbf r_0^P(s) = a\cos\frac{\omega s}{\sqrt{a^2\omega^2 + v_z^2}}\,\mathbf i + a\sin\frac{\omega s}{\sqrt{a^2\omega^2 + v_z^2}}\,\mathbf j + \frac{v_z s}{\sqrt{a^2\omega^2 + v_z^2}}\,\mathbf k}$$
>
> **Units:** $s$ in $\mathrm m$; the arguments of the cosine and sine are in $\mathrm{rad}$, $(\mathrm{rad/s})\,\mathrm m/(\mathrm{m/s})$
> **Meaning:** the derivative of the trajectory with respect to $s$ has unit magnitude, as Eq. 2.9 requires of $\mathbf e_t$; one turn of the helix, a change of $2\pi$ in the angle, measures $2\pi\dot s/\omega$ of arc.

> [!derivation] (g) Centre of curvature at the point (a, 0, 0)
> **Law:** the centre of the osculating circle lies at the distance $\rho$ from $P$ along $\mathbf e_n$
> **Source:** Notes.pdf, Sec. 2.4; Notes.pdf Fig. 2.2; Notes.pdf, Eq. 2.24
>
> The point $(a, 0, 0)$ has zero height, so it is reached at $t = 0$, the start of the motion (the limit of positive times); there $\theta$ is zero and $\mathbf e_R$ is $\mathbf i$ (Eq. 2.24).
>
> $$\begin{aligned}
> \overrightarrow{OC} &= \mathbf r_0^P + \rho\,\mathbf e_n \quad &\text{($\mathbf e_n$ points from $P$ to $C$, at the distance $\rho$, Fig. 2.2)} \\
> &= a\,\mathbf i + \frac{a^2\omega^2 + v_z^2}{a\omega^2}\left(-\mathbf i\right) \quad &\text{(at $t = 0$: $\mathbf r_0^P = a\,\mathbf i$, $\mathbf e_n = -\mathbf e_R = -\mathbf i$)} \\
> &= \left(a - a - \frac{v_z^2}{a\omega^2}\right)\mathbf i \quad &\text{(split the fraction)} \\
> &= -\frac{v_z^2}{a\omega^2}\,\mathbf i \quad &\text{(cancel)}
> \end{aligned}$$
>
> $$\boxed{C = \left(-\frac{v_z^2}{a\omega^2},\ 0,\ 0\right)}$$
>
> **Units:** $(\mathrm{m^2/s^2})/(\mathrm{m\,rad^2/s^2}) = \mathrm m$, because the radian is dimensionless (a ratio of two lengths)
> **Meaning:** the centre of curvature is not on the axis of the helix: it lies on the far side of $Oz$, at the distance $v_z^2/(a\omega^2)$ from it, and it moves to $O$, the centre of the horizontal circle, as $v_z$ tends to zero.

> [!key] Kinematics of a point particle
> Choose the reference frame first: an origin and an orthonormal right-handed basis, which define the observer. The position vector with respect to that frame, differentiated once and twice in that frame, gives the velocity and the acceleration; a derivative always carries the frame it is taken in, and two observers agree only if their bases do not rotate relative to each other. The velocity is tangent to the trajectory; the acceleration splits into a tangential part, from the change of speed, and a normal part, from the change of direction, both in the osculating plane. Write vectors in the basis that suits the problem: Cartesian (fixed), cylindrical or spherical (local bases that turn with the coordinates, built column by column as rotations of the fixed basis), or intrinsic (tangent, normal and binormal, which depend only on the shape of the path). Never quote the curvilinear components: derive them from the position vector, the derivatives of the local unit vectors and the product rule. Count the degrees of freedom as the coordinates needed minus the independent constraints, and choose generalized coordinates in which the constraints are automatically satisfied.
