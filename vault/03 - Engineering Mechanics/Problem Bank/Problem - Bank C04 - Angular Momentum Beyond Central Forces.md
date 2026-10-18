---
materia: Engineering Mechanics
tema: "Unit 4: angular momentum theorem, planar motion, moving reference points"
bank_id: C04
title: "Angular momentum under a non-central force and about a moving point"
category: conceptual_question
archetype: central-force
level: conceptual
unit: 4
difficulty: 2
points: 2.0
time_minutes: 15
official: false
origen: "Question written for the bank in the style of the true/false questions of the final exams (MECHANICS_FINALEXAM_2013, 2014 and 2015); not an official exercise. Verified with scripts/mechanics/c04.py"
tags:
  - problem-bank
  - midterm-1
  - angular-momentum
  - central-force
  - planar-motion
---

# Bank C04 — Angular momentum under a non-central force and about a moving point

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the true/false questions of the final exams. Method: Notes §4.8 (angular momentum about an arbitrary point, Eqs. 4.48 to 4.55) and §4.8.1 (central force motion). Every number was checked with SymPy.

## Statement

A point particle $P$ of mass $m$ moves with respect to the inertial frame $S_0=\{O;\mathbf i,\mathbf j,\mathbf k\}$, with no gravity. $r=|\mathbf r_P|$ is its distance to $O$, $\mathbf u_r=\mathbf r_P/r$, and $\{\mathbf e_R,\mathbf e_\varphi,\mathbf k\}$ is the cylindrical basis about the $z$ axis. The angular momentum about a point $A$ is $\mathbf H_A=\mathbf r_{AP}\times m\mathbf v_P$ (absolute velocity, Notes Eq. 4.48). Decide whether each statement is TRUE or FALSE and justify the answer. A verdict without a justification scores nothing.

## (a) A force with an azimuthal part [1.0 pts]

$P$ moves under $\mathbf F=f(r)\,\mathbf u_r+q(r)\,\mathbf e_\varphi$, with $f$ and $q$ known functions and $q\neq0$. At $t=0$, $P$ is in the plane $z=0$ and its velocity is parallel to that plane. Statement: "Since $\mathbf F$ is not central, $\mathbf H_O$ is not conserved, and therefore the trajectory of $P$ cannot be planar."

### Hint

Planarity needs a constant **direction** of $\mathbf H_O$, not a constant vector. Look at $F_z$ on the plane $z=0$, and at the direction of $\mathbf M_O=\mathbf r_P\times\mathbf F$ there.

### Checkpoint

- FALSE (the first half is true, the conclusion is not).
- $F_z=f(r)\,z/r$: zero on $z=0$, so with $z(0)=\dot z(0)=0$ the solution keeps $z\equiv0$: the motion is planar.
- $\mathbf M_O=r\,q(r)\,\mathbf k\neq\mathbf 0$ on the plane: $\mathbf H_O=mR^2\dot\varphi\,\mathbf k$ changes magnitude, $\dfrac{d}{dt}\big(mR^2\dot\varphi\big)=R\,q(R)$, but keeps its direction $\mathbf k$.

### Solution

#### Step 1. The plane $z=0$ is invariant

In Cartesian components $\mathbf u_r=(x,y,z)/r$ and $\mathbf e_\varphi=(-y,x,0)/\sqrt{x^2+y^2}$, so the $z$ component of Newton's law is

$$m\ddot z=f(r)\,\frac{z}{r}$$

With $z(0)=0$ and $\dot z(0)=0$, the function $z(t)\equiv0$ satisfies this equation and the initial conditions; by uniqueness it is the solution. $P$ never leaves the plane $z=0$: the trajectory **is** planar.

#### Step 2. Angular momentum is not conserved

On the plane, $\mathbf r_P=R\,\mathbf e_R$ (with $R=r$) and $\mathbf M_O=\mathbf r_P\times\mathbf F=R\,\mathbf e_R\times\big(f\,\mathbf e_R+q\,\mathbf e_\varphi\big)=R\,q(R)\,\mathbf k\neq\mathbf 0$. By Notes Eq. 4.53 ($O$ fixed), $\dot{\mathbf H}_O=\mathbf M_O$. With $\mathbf v_P=\dot R\,\mathbf e_R+R\dot\varphi\,\mathbf e_\varphi$:

$$\mathbf H_O=R\,\mathbf e_R\times m\big(\dot R\,\mathbf e_R+R\dot\varphi\,\mathbf e_\varphi\big)=mR^2\dot\varphi\,\mathbf k,\qquad \frac{d}{dt}\big(mR^2\dot\varphi\big)=m\big(2R\dot R\dot\varphi+R^2\ddot\varphi\big)=mR\,a_\varphi=R\,q(R)$$

So $\mathbf H_O$ is not conserved (the areal velocity $\tfrac12R^2\dot\varphi$ is not constant either), but it always points along $\mathbf k$.

#### Step 3. Where the reasoning breaks

Conservation of $\mathbf H_O$ is sufficient for planar motion (Notes §4.8.1, property 2) but not necessary. Here $\mathbf M_O$ is parallel to $\mathbf H_O$: only the magnitude changes, and $\mathbf r_P\cdot\mathbf H_O=0$ keeps $P$ in the fixed plane normal to $\mathbf k$. The statement is FALSE.

## (b) Angular momentum about a moving point [1.0 pts]

Now $P$ moves under a central force towards $O$ on a circle of radius $\rho$ with constant angular rate $n$: $\mathbf r_P=\rho(\cos nt\,\mathbf i+\sin nt\,\mathbf j)$. A point $A$ moves with constant velocity, $\mathbf r_A=ut\,\mathbf i$ ($u>0$). Statement: "A frame translating with $A$ at constant velocity is inertial, so the angular momentum of $P$ about $A$, $\mathbf H_A$, is conserved just like $\mathbf H_O$."

### Hint

Use $\dfrac{d\mathbf H_A}{dt}=\mathbf M_A-\mathbf v_A\times m\mathbf v_P$ (Notes Eq. 4.52). Is the force central with respect to $A$?

### Checkpoint

- FALSE.
- $\mathbf M_A=\mathbf r_{AP}\times\mathbf F=-\mathbf r_A\times\mathbf F\neq\mathbf 0$ once $A\neq O$, and $\mathbf v_A\times m\mathbf v_P\neq\mathbf 0$.
- $H_{A,z}=m\big(n\rho^2-ut\,n\rho\cos nt\big)$, $\ \dot H_{A,z}=-mun\rho\,(\cos nt-nt\sin nt)$, equal to $-mun\rho\neq0$ at $t=0$.
- Even the relative angular momentum $\mathbf H_{A,A}$ of Notes Eq. 4.55 changes: $\dot H_{A,A,z}=M_{A,z}=mun^2\rho\,t\sin nt$.

### Solution

#### Step 1. The theorem about a moving point

Differentiating $\mathbf H_A=(\mathbf r_P-\mathbf r_A)\times m\mathbf v_P$ with the product rule:

$$\frac{d\mathbf H_A}{dt}=(\mathbf v_P-\mathbf v_A)\times m\mathbf v_P+(\mathbf r_P-\mathbf r_A)\times m\mathbf a_P=\mathbf M_A-\mathbf v_A\times m\mathbf v_P$$

because $\mathbf v_P\times\mathbf v_P=\mathbf 0$ and $m\mathbf a_P=\mathbf F$ (Notes Eq. 4.52). Both terms must vanish for conservation. The force passes through $O$, not through $A$: $\mathbf M_A=(\mathbf r_P-\mathbf r_A)\times\mathbf F=-\mathbf r_A\times\mathbf F$, since $\mathbf r_P\times\mathbf F=\mathbf 0$.

#### Step 2. Direct computation

$\mathbf v_P=n\rho(-\sin nt\,\mathbf i+\cos nt\,\mathbf j)$ and $\mathbf r_P-\mathbf r_A=(\rho\cos nt-ut)\,\mathbf i+\rho\sin nt\,\mathbf j$, so

$$H_{A,z}=m\big[(\rho\cos nt-ut)\,n\rho\cos nt+\rho\sin nt\;n\rho\sin nt\big]=m\big(n\rho^2-ut\,n\rho\cos nt\big)$$

Differentiating with the product rule, $\frac{d}{dt}(t\cos nt)=\cos nt-nt\sin nt$:

$$\dot H_{A,z}=-mun\rho\,\big(\cos nt-nt\sin nt\big),\qquad \dot H_{A,z}(0)=-mun\rho\neq0$$

At $t=0$, $A=O$ and $\mathbf M_A=\mathbf 0$, yet $\mathbf H_A$ changes because of $-\mathbf v_A\times m\mathbf v_P=-u\,\mathbf i\times mn\rho\,\mathbf j=-mun\rho\,\mathbf k$.

#### Step 3. The inertial frame of $A$ does not help

In the frame $S_A$ that translates with $A$ (inertial, since $\mathbf a_A=\mathbf 0$), Notes Eq. 4.55 gives $\dot{\mathbf H}_{A,A}=\mathbf M_A$ for $\mathbf H_{A,A}=\mathbf r_{AP}\times m(\mathbf v_P-\mathbf v_A)$. With $\mathbf F=-mn^2\mathbf r_P$, $\mathbf M_A=-ut\,\mathbf i\times(-mn^2\rho)(\cos nt\,\mathbf i+\sin nt\,\mathbf j)=mun^2\rho\,t\sin nt\,\mathbf k$, nonzero for instance at $nt=\pi/2$. A frame being inertial does not make the force central about its origin. The statement is FALSE.

## Interpretation

- **Dimensional check:** $mR^2\dot\varphi$ and $mn\rho^2$ are kg m$^2$ s$^{-1}$; $R\,q(R)$ and $mun\rho$ are N m = kg m$^2$ s$^{-2}$.
- **Limits:** in (a), $q\to0$ gives a central force and $mR^2\dot\varphi$ constant; if the initial velocity had a $z$ component, $F_z=fz/r$ would not vanish and the motion would in general leave the plane. In (b), $u\to0$ ($A$ fixed at $O$) recovers $\dot{\mathbf H}_A=\mathbf 0$.
- **Common mistakes in the exam:** (1) treating "angular momentum conserved" as the only route to planar motion; (2) applying $\dot{\mathbf H}_A=\mathbf M_A$ about a moving point without the term $-\mathbf v_A\times m\mathbf v_P$; (3) thinking that a force is central about every point of an inertial frame.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
