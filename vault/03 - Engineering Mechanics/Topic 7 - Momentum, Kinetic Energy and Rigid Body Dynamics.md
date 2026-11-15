---
title: "Topic 7 - Momentum, Kinetic Energy and Rigid Body Dynamics"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/teoria/Notes.pdf"
type: "Theory"
language: "English"
tags:
  - theory
  - topic-7
  - rigid-body
  - angular-momentum
  - kinetic-energy
  - euler-equations
---

# Topic 7 - Momentum, Kinetic Energy and Rigid Body Dynamics

> The linear momentum, the angular momentum and the kinetic energy of a point particle are extended to a rigid body by integrating over its mass distribution, and the velocity field of the body turns those integrals into compact expressions built from the mass $m$, the centre of mass $G$, the angular velocity $\boldsymbol\omega_{B0}$ and the tensor of inertia. Newton's second law, written for every particle of the body and summed, then gives the two vector equations that govern a free rigid body: the motion of $G$ under the resultant force $\mathbf F$, and the evolution of the angular momentum under the resultant moment $\mathbf M_A$. Written in a body-fixed principal basis, the second one becomes Euler's equations. The work and energy theorem closes the topic. The chapter follows chapters 11 and 12 of the course notes and Lectures 9 and 10.

## 1. Linear momentum of a rigid body

The notes treat a general material system $B$ first and only use the rigidity of the body when the velocity field is needed. The symbols of the whole topic are collected here.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $S_0\{O; B_0\}$ | inertial (fixed) reference frame, basis $B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$ | - |
| $S_A\{A; B_0\}$, $S_G\{G; B_0\}$ | frames with origin at a point $A$ or at the centre of mass $G$, axes parallel to those of $S_0$ (they translate, they do not rotate) | - |
| $S_B\{A; B_B\}$ | body-fixed frame, basis $B_B = \{\mathbf e_1, \mathbf e_2, \mathbf e_3\}$ | - |
| $\mathcal D(\mathbf r_0^P)$, $dm$ | mass distribution of the body and mass of one material element at $P$ | kg |
| $m = \int_{\mathcal D} dm$ | total mass (Notes Eq. 10.6) | kg |
| $\mathbf r_0^P$, $\mathbf r_A^P = \overrightarrow{AP}$, $\mathbf r_G^P = \overrightarrow{GP}$ | position of $P$ seen from $O$, $A$, $G$ | m |
| $\mathbf v_0^P$, $\mathbf v_0^{A(B)}$ | velocity in $S_0$ of $P$ and of the body point $A(B)$ that coincides with $A$ at the instant | m/s |
| $\boldsymbol\omega_{B0}$, $\boldsymbol\alpha_{B0}$ | angular velocity and angular acceleration of the body relative to $S_0$ | rad/s, rad/s$^2$ |
| $\overline{\overline{\mathcal I}}_A$, $\overline{\overline{\mathcal U}}$ | tensor of inertia about $A$ (Notes Eq. 10.35) and unit tensor | kg m$^2$, - |
| $\mathbf p_0$, $\mathbf H_{A,0}$, $T_0$ | linear momentum, angular momentum about $A$ and kinetic energy, all in $S_0$ | kg m/s, kg m$^2$/s, J |
| $\mathbf F$, $\mathbf M_A$, $\mathbf Q_k$ | resultant external force, resultant external moment about $A$, external torques | N, N m, N m |

![[attachments/EM-T/t7-material-system.svg]]

The linear momentum of an element of mass $dm$ is the momentum of a point particle (Notes Eq. 4.1) with that mass; the momentum of the body is the integral over $\mathcal D$.

> [!derivation] Linear momentum of a material system
> **Law:** momentum of each material element (Eq. 4.1) summed over the mass distribution
> **Source:** Notes.pdf, Eq. 11.1; [Lecture 9, Slide 3]
>
> $$\begin{aligned}
> d\mathbf p_0 &= \mathbf v_0^P\,dm \quad &\text{(momentum of an element of mass dm, Notes Eq. 4.1)} \\
> \mathbf p_0 &= \int_{\mathcal D} d\mathbf p_0 \quad &\text{(sum of the momenta of all the elements)} \\
> &= \int_{\mathcal D} \mathbf v_0^P\,dm \quad &\text{(substitution of the element momentum)}
> \end{aligned}$$
>
> $$\boxed{\mathbf p_0 = \int_{\mathcal D} d\mathbf p_0 = \int_{\mathcal D} \mathbf v_0^P\,dm}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]\,[\mathrm{M}] = [\mathrm{M\,L\,T^{-1}}]$, kg m/s
> **Meaning:** the momentum of the body is the vector sum of the momenta of all its material elements.

The definition of the centre of mass (Notes Eq. 10.8) is differentiated in time. The mass of each material element does not change while the body moves, so the time derivative can be taken inside the integral over the material elements.

> [!derivation] Momentum equals mass times the velocity of the centre of mass
> **Law:** definition of the centre of mass, differentiated in $S_0$
> **Source:** Notes.pdf, Eq. 11.2; Notes.pdf, Eq. 11.3; [Lecture 9, Slide 3]
>
> $$\begin{aligned}
> m\,\mathbf r_0^G &= \int_{\mathcal D} \mathbf r_0^P\,dm \quad &\text{(Notes Eq. 10.8 multiplied by m: Eq. 11.2)} \\
> \left.\frac{d}{dt}\left(m\,\mathbf r_0^G\right)\right|_0 &= m\left.\frac{d\mathbf r_0^G}{dt}\right|_0 = m\,\mathbf v_0^G \quad &\text{(m is constant; definition of velocity)} \\
> \left.\frac{d}{dt}\int_{\mathcal D} \mathbf r_0^P\,dm\right|_0 &= \int_{\mathcal D} \left.\frac{d\mathbf r_0^P}{dt}\right|_0 dm \quad &\text{(the mass dm of each element is constant in time)} \\
> &= \int_{\mathcal D} \mathbf v_0^P\,dm \quad &\text{(definition of velocity of each element)} \\
> &= \mathbf p_0 \quad &\text{(Eq. 11.1)}
> \end{aligned}$$
>
> $$\boxed{m\,\mathbf v_0^G = \int_{\mathcal D} \mathbf v_0^P\,dm = \mathbf p_0}$$
>
> **Units:** $[\mathrm{M}]\,[\mathrm{L\,T^{-1}}] = [\mathrm{M\,L\,T^{-1}}]$ on both sides
> **Meaning:** the momentum of the body equals that of a point particle with the total mass $m$ located at $G$ and moving like $G$ (Notes Eq. 11.3).

## 2. Angular momentum of a rigid body

### 2.1 Definition and expansion with the velocity field

> [!derivation] Angular momentum about a point A
> **Law:** angular momentum of each material element (Eq. 4.48) summed over the body
> **Source:** Notes.pdf, Eq. 11.4; [Lecture 9, Slide 4]
>
> $$\begin{aligned}
> d\mathbf H_{A,0} &= \mathbf r_A^P \times \mathbf v_0^P\,dm \quad &\text{(angular momentum of the element about A, Notes Eq. 4.48)} \\
> \mathbf H_{A,0} &= \int_{\mathcal D} d\mathbf H_{A,0} \quad &\text{(sum over all the elements)} \\
> &= \int_{\mathcal D} \mathbf r_A^P \times \mathbf v_0^P\,dm \quad &\text{(substitution)} \\
> &\equiv \int_{\mathcal D} \overrightarrow{AP} \times \mathbf v_0^P\,dm \quad &\text{(notation of Lecture 9, Slide 4)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{A,0} = \int_{\mathcal D} \mathbf r_A^P \times \mathbf v_0^P\,dm}$$
>
> **Units:** $[\mathrm{L}]\,[\mathrm{L\,T^{-1}}]\,[\mathrm{M}] = [\mathrm{M\,L^2\,T^{-1}}]$, kg m$^2$/s
> **Meaning:** the arm is measured from $A$, but the velocity is the absolute velocity in $S_0$, not the velocity relative to $A$.

The point $A$ may or may not belong to the body. The notes write $A(B)$ for the point of the body that occupies the position of $A$ at the instant considered (Notes Sec. 9.1.4): both have the same position, but in general not the same velocity.

> [!derivation] Velocity field written from the body point A(B)
> **Law:** velocity field of the rigid body between two body points
> **Source:** Notes.pdf, Eq. 11.5; Notes.pdf, Eq. 9.3; [Lecture 9, Slide 4]
>
> $$\begin{aligned}
> \mathbf v_0^{Q_2} &= \mathbf v_0^{Q_1} + \boldsymbol\omega_{B0} \times \overrightarrow{Q_1 Q_2} \quad &\text{(Notes Eq. 9.3 for two body points Q1, Q2)} \\
> \mathbf v_0^{P} &= \mathbf v_0^{A(B)} + \boldsymbol\omega_{B0} \times \overrightarrow{A(B)P} \quad &\text{(choice Q1 = A(B), Q2 = P)} \\
> \overrightarrow{A(B)P} &= \mathbf r_0^P - \mathbf r_0^{A(B)} = \mathbf r_0^P - \mathbf r_0^{A} = \mathbf r_A^P \quad &\text{(A and A(B) have the same position, Notes Eq. 9.14)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \mathbf v_0^{A(B)} + \boldsymbol\omega_{B0} \times \mathbf r_A^P}$$
>
> **Units:** $[\mathrm{T^{-1}}]\,[\mathrm{L}] = [\mathrm{L\,T^{-1}}]$, every term a velocity
> **Meaning:** the velocity of any element is a translation with $A(B)$ plus a rotation about it.

> [!derivation] First expansion of the angular momentum
> **Law:** velocity field substituted in the definition; centre of mass
> **Source:** Notes.pdf, Eq. 11.6; Notes.pdf, Eq. 11.7; [Lecture 9, Slide 4]
>
> $$\begin{aligned}
> \mathbf H_{A,0} &= \int_{\mathcal D} \mathbf r_A^P \times \left(\mathbf v_0^{A(B)} + \boldsymbol\omega_{B0} \times \mathbf r_A^P\right) dm \quad &\text{(Eq. 11.5 in Eq. 11.4)} \\
> &= \int_{\mathcal D} \mathbf r_A^P \times \mathbf v_0^{A(B)}\,dm + \int_{\mathcal D} \mathbf r_A^P \times \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) dm \quad &\text{(distributive property of the cross product)} \\
> &= \left(\int_{\mathcal D} \mathbf r_A^P\,dm\right) \times \mathbf v_0^{A(B)} + \int_{\mathcal D} \mathbf r_A^P \times \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) dm \quad &\text{(the velocity of A(B) is the same for every element: Eq. 11.6)} \\
> \int_{\mathcal D} \mathbf r_A^P\,dm &= \int_{\mathcal D} \left(\mathbf r_0^P - \mathbf r_0^A\right) dm \quad &\text{(position of P relative to A)} \\
> &= \int_{\mathcal D} \mathbf r_0^P\,dm - \mathbf r_0^A \int_{\mathcal D} dm \quad &\text{(the position of A does not depend on P)} \\
> &= m\,\mathbf r_0^G - m\,\mathbf r_0^A \quad &\text{(Notes Eqs. 10.8 and 10.6)} \\
> &= m\,\mathbf r_A^G \quad &\text{(position of G relative to A)}
> \end{aligned}$$
>
> $$\boxed{\left(\int_{\mathcal D} \mathbf r_A^P\,dm\right) \times \mathbf v_0^{A(B)} = m\,\mathbf r_A^G \times \mathbf v_0^{A(B)}}$$
>
> **Units:** $[\mathrm{M}]\,[\mathrm{L}]\,[\mathrm{L\,T^{-1}}] = [\mathrm{M\,L^2\,T^{-1}}]$, an angular momentum
> **Meaning:** the translational part of the velocity field contributes like a point mass $m$ placed at $G$ moving with $\mathbf v_0^{A(B)}$.

> [!derivation] Double vector product of the rotational term
> **Law:** expansion of the double vector product, Notes Eq. 1.37
> **Source:** Notes.pdf, Eq. 11.8; Notes.pdf, Eq. 11.9; [Lecture 9, Slide 4]
>
> $$\begin{aligned}
> \mathbf A \times (\mathbf B \times \mathbf C) &= (\mathbf A \cdot \mathbf C)\,\mathbf B - (\mathbf A \cdot \mathbf B)\,\mathbf C \quad &\text{(Notes Eq. 1.37, written as Eq. 11.8)} \\
> \mathbf r_A^P \times \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) &= \left(\mathbf r_A^P \cdot \mathbf r_A^P\right)\boldsymbol\omega_{B0} - \left(\mathbf r_A^P \cdot \boldsymbol\omega_{B0}\right)\mathbf r_A^P \quad &\text{(A = r, B = omega, C = r)} \\
> &= (r_A^P)^2\,\boldsymbol\omega_{B0} - \left(\mathbf r_A^P \cdot \boldsymbol\omega_{B0}\right)\mathbf r_A^P \quad &\text{(the dot product of a vector with itself is its squared modulus)}
> \end{aligned}$$
>
> $$\boxed{\int_{\mathcal D} \mathbf r_A^P \times \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) dm = \int_{\mathcal D} \left[(r_A^P)^2\,\boldsymbol\omega_{B0} - \left(\mathbf r_A^P \cdot \boldsymbol\omega_{B0}\right)\mathbf r_A^P\right] dm}$$
>
> **Units:** $[\mathrm{L^2}]\,[\mathrm{T^{-1}}]\,[\mathrm{M}] = [\mathrm{M\,L^2\,T^{-1}}]$ in both terms
> **Meaning:** the rotational part of the angular momentum has a component along $\boldsymbol\omega_{B0}$ and a component along each arm $\mathbf r_A^P$.

> [!derivation] Rotational term written with the tensor of inertia
> **Law:** unit tensor, dyadic product (Eq. 1.36) and tensor of inertia (Eq. 10.35)
> **Source:** Notes.pdf, Eq. 11.10; Notes.pdf, Eq. 10.35; [Lecture 9, Slide 4]
>
> $$\begin{aligned}
> (r_A^P)^2\,\boldsymbol\omega_{B0} &= (r_A^P)^2\,\overline{\overline{\mathcal U}} \cdot \boldsymbol\omega_{B0} \quad &\text{(the unit tensor maps every vector onto itself)} \\
> \mathbf r_A^P\left(\mathbf r_A^P \cdot \boldsymbol\omega_{B0}\right) &= \left(\mathbf r_A^P \otimes \mathbf r_A^P\right) \cdot \boldsymbol\omega_{B0} \quad &\text{(Notes Eq. 1.36 with A = B = r, C = omega)} \\
> \left[\left(\mathbf r_A^P \otimes \mathbf r_A^P\right) \cdot \boldsymbol\omega_{B0}\right]_i &= \sum_{j} r_i\,r_j\,\omega_j = r_i \left(\sum_j r_j\,\omega_j\right) \quad &\text{(component check of footnote 18, ri taken out of the sum)} \\
> \int_{\mathcal D} \mathbf r_A^P \times \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) dm &= \int_{\mathcal D} \left[(r_A^P)^2\,\overline{\overline{\mathcal U}} \cdot \boldsymbol\omega_{B0} - \left(\mathbf r_A^P \otimes \mathbf r_A^P\right) \cdot \boldsymbol\omega_{B0}\right] dm \quad &\text{(both rows in Eq. 11.9)} \\
> &= \left\{\int_{\mathcal D} \left[(r_A^P)^2\,\overline{\overline{\mathcal U}} - \mathbf r_A^P \otimes \mathbf r_A^P\right] dm\right\} \cdot \boldsymbol\omega_{B0} \quad &\text{(the angular velocity is the same for every element)} \\
> &= \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0} \quad &\text{(Notes Eq. 10.35 written about the point A)}
> \end{aligned}$$
>
> $$\boxed{\int_{\mathcal D} \mathbf r_A^P \times \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) dm = \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0}}$$
>
> **Units:** $[\mathrm{M\,L^2}]\,[\mathrm{T^{-1}}] = [\mathrm{M\,L^2\,T^{-1}}]$
> **Meaning:** all the information about the mass distribution needed by the rotational part sits in the six independent components of the tensor of inertia about $A$.

> [!derivation] Angular momentum about A, first form
> **Law:** sum of the translational and the rotational terms
> **Source:** Notes.pdf, Eq. 11.11; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.13; [Lecture 9, Slide 5]
>
> $$\begin{aligned}
> \mathbf H_{A,0} &= m\,\mathbf r_A^G \times \mathbf v_0^{A(B)} + \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0} \quad &\text{(Eqs. 11.6, 11.7 and 11.10)} \\
> \mathbf H_{G,0} &= \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0} + m\,\mathbf r_G^G \times \mathbf v_0^{G} = \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0} \quad &\text{(case A = G: the arm from G to G is zero, Eq. 11.12)} \\
> \mathbf H_{A,0} &= \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0} + m\,\mathbf r_A^G \times \mathbf 0 = \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0} \quad &\text{(case A fixed body point: its velocity is zero, Eq. 11.13)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{A,0} = \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0} + m\,\mathbf r_A^G \times \mathbf v_0^{A(B)}}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-1}}]$ in both terms
> **Meaning:** the expression is short when $A$ is $G$ or a fixed point of the body; for any other point the extra term must be kept.

### 2.2 Second expansion about the centre of mass: change of pole

The frame $S_G\{G; B_0\}$ has its origin at $G$ and axes parallel to those of $S_0$: it translates with $G$ and does not rotate, so it is not body-fixed in general [Lecture 9, Slide 4]. The velocity of an element seen from $S_G$ is written $\mathbf v_G^P$.

> [!derivation] Four integrals of the second expansion
> **Law:** position split through G, velocity field from G, first moment about G (Eq. 10.44)
> **Source:** Notes.pdf, Eq. 11.14; Notes.pdf, Eq. 11.15; Notes.pdf, Eq. 11.16; [Lecture 9, Slide 6]
>
> $$\begin{aligned}
> \mathbf r_A^P &= \mathbf r_A^G + \mathbf r_G^P \quad &\text{(vector sum of the arms A to G and G to P)} \\
> \mathbf v_0^P &= \mathbf v_0^G + \boldsymbol\omega_{B0} \times \mathbf r_G^P \quad &\text{(Notes Eq. 9.3 from G, which is fixed in the body)} \\
> \mathbf H_{A,0} &= \int_{\mathcal D} \left(\mathbf r_A^G + \mathbf r_G^P\right) \times \left(\mathbf v_0^G + \boldsymbol\omega_{B0} \times \mathbf r_G^P\right) dm \quad &\text{(both rows in Eq. 11.4)} \\
> &= \int_{\mathcal D} \mathbf r_A^G \times \mathbf v_0^G\,dm + \int_{\mathcal D} \mathbf r_G^P \times \mathbf v_0^G\,dm + \int_{\mathcal D} \mathbf r_A^G \times \left(\boldsymbol\omega_{B0} \times \mathbf r_G^P\right) dm + \int_{\mathcal D} \mathbf r_G^P \times \left(\boldsymbol\omega_{B0} \times \mathbf r_G^P\right) dm \quad &\text{(distributive property, four terms)} \\
> \int_{\mathcal D} \mathbf r_A^G \times \mathbf v_0^G\,dm &= m\,\mathbf r_A^G \times \mathbf v_0^G \quad &\text{(both vectors constant over the body, Eq. 11.14)} \\
> \int_{\mathcal D} \mathbf r_G^P \times \mathbf v_0^G\,dm &= \left(\int_{\mathcal D} \mathbf r_G^P\,dm\right) \times \mathbf v_0^G = \mathbf 0 \quad &\text{(first moment about G is zero, Notes Eq. 10.44: Eq. 11.15)} \\
> \int_{\mathcal D} \mathbf r_A^G \times \left(\boldsymbol\omega_{B0} \times \mathbf r_G^P\right) dm &= \mathbf r_A^G \times \left(\boldsymbol\omega_{B0} \times \int_{\mathcal D} \mathbf r_G^P\,dm\right) = \mathbf 0 \quad &\text{(same reason, Eq. 11.16)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{A,0} = m\,\mathbf r_A^G \times \mathbf v_0^G + \int_{\mathcal D} \mathbf r_G^P \times \left(\boldsymbol\omega_{B0} \times \mathbf r_G^P\right) dm}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-1}}]$ in both terms
> **Meaning:** the cross terms vanish because the mass is balanced about $G$; only a translational and a purely rotational term survive.

> [!derivation] The remaining integral is the angular momentum seen from S_G
> **Law:** composition of velocities between $S_0$ and the translating frame $S_G$
> **Source:** Notes.pdf, Eq. 11.17; Notes.pdf, Eq. 11.18; Notes.pdf, Eq. 11.19; [Lecture 9, Slide 7]
>
> $$\begin{aligned}
> \mathbf v_G^P &= \mathbf v_0^P - \mathbf v_0^G \quad &\text{(SG translates with G and does not rotate)} \\
> &= \boldsymbol\omega_{B0} \times \mathbf r_G^P \quad &\text{(velocity field from G)} \\
> \int_{\mathcal D} \mathbf r_G^P \times \left(\boldsymbol\omega_{B0} \times \mathbf r_G^P\right) dm &= \int_{\mathcal D} \mathbf r_G^P \times \mathbf v_G^P\,dm \equiv \mathbf H_{G,G} \quad &\text{(definition Eq. 11.4 in the frame SG: Eq. 11.17)} \\
> \mathbf H_{G,G} &= \int_{\mathcal D} \mathbf r_G^P \times \left(\mathbf v_0^P - \mathbf v_0^G\right) dm \quad &\text{(first row, Eq. 11.18)} \\
> &= \int_{\mathcal D} \mathbf r_G^P \times \mathbf v_0^P\,dm - \left(\int_{\mathcal D} \mathbf r_G^P\,dm\right) \times \mathbf v_0^G \quad &\text{(distributive property; G velocity out of the integral)} \\
> &= \mathbf H_{G,0} + \mathbf 0 \quad &\text{(Eq. 11.4 with A = G, and Notes Eq. 10.44: Eq. 11.19)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{G,G} \equiv \mathbf H_{G,0}}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-1}}]$ on both sides
> **Meaning:** about the centre of mass, the angular momentum is the same whether the velocities are measured in $S_0$ or in the translating frame $S_G$.

> [!derivation] Change of pole from G to any point A
> **Law:** second expansion combined with the result about G
> **Source:** Notes.pdf, Eq. 11.20; Notes.pdf, Eq. 11.21; [Lecture 9, Slide 7]
>
> $$\begin{aligned}
> \mathbf H_{A,0} &= m\,\mathbf r_A^G \times \mathbf v_0^G + \mathbf H_{G,G} \quad &\text{(previous two boxes)} \\
> &= \mathbf H_{G,0} + m\,\mathbf r_A^G \times \mathbf v_0^G \quad &\text{(H about G is the same in SG and S0: Eq. 11.20)} \\
> &= \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0} + m\,\mathbf r_A^G \times \mathbf v_0^G \quad &\text{(Eq. 11.12: Eq. 11.21)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{A,0} = \mathbf H_{G,0} + m\,\mathbf r_A^G \times \mathbf v_0^G = \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0} + m\,\mathbf r_A^G \times \mathbf v_0^G}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-1}}]$ in every term
> **Meaning:** the angular momentum about $A$ is the angular momentum of the rotation about $G$ plus that of a point mass $m$ at $G$ moving with $\mathbf v_0^G$, seen from $A$.

> [!info] Extension: change of pole between two arbitrary points
> The notes give the change of pole from $G$ to $A$ only. Applying Eq. 11.20 twice gives the rule between any two points $A$ and $C$; it is the same rule as the change of reduction point of a system of forces (Notes Eq. 12.15), with the momentum $\mathbf p_0$ in the place of the force. This box is an extension.

> [!derivation] Change of pole between A and C (extension)
> **Law:** Eq. 11.20 written about two points and subtracted
> **Source:** Notes.pdf, Eq. 11.20; Notes.pdf, Eq. 11.3
>
> $$\begin{aligned}
> \mathbf H_{C,0} - \mathbf H_{A,0} &= \left(\mathbf H_{G,0} + m\,\mathbf r_C^G \times \mathbf v_0^G\right) - \left(\mathbf H_{G,0} + m\,\mathbf r_A^G \times \mathbf v_0^G\right) \quad &\text{(Eq. 11.20 about C and about A)} \\
> &= m\left(\mathbf r_C^G - \mathbf r_A^G\right) \times \mathbf v_0^G \quad &\text{(the rotational term cancels)} \\
> &= \mathbf r_C^A \times m\,\mathbf v_0^G \quad &\text{(r from C to G minus r from A to G is r from C to A)} \\
> &= \mathbf r_C^A \times \mathbf p_0 \quad &\text{(Eq. 11.3)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{C,0} = \mathbf H_{A,0} + \overrightarrow{CA} \times \mathbf p_0}$$
>
> **Units:** $[\mathrm{L}]\,[\mathrm{M\,L\,T^{-1}}] = [\mathrm{M\,L^2\,T^{-1}}]$
> **Meaning:** moving the pole only adds the moment of the momentum, placed at the old pole; if the body has zero momentum, the angular momentum is the same about every point.

## 3. Kinetic energy of a rigid body

> [!derivation] Kinetic energy of a material system
> **Law:** kinetic energy of each element (Eq. 4.2) summed over the mass distribution
> **Source:** Notes.pdf, Eq. 11.22; [Lecture 9, Slide 8]
>
> $$\begin{aligned}
> dT_0 &= \tfrac{1}{2}\left(v_0^P\right)^2 dm \quad &\text{(Notes Eq. 4.2 for an element of mass dm)} \\
> T_0 &= \int_{\mathcal D} dT_0 \quad &\text{(sum over the elements)} \\
> &= \frac{1}{2}\int_{\mathcal D} \left(v_0^P\right)^2 dm \quad &\text{(constant factor out of the integral)}
> \end{aligned}$$
>
> $$\boxed{T_0 = \int_{\mathcal D} dT_0 = \frac{1}{2}\int_{\mathcal D} \left(v_0^P\right)^2 dm}$$
>
> **Units:** $[\mathrm{L^2\,T^{-2}}]\,[\mathrm{M}] = [\mathrm{M\,L^2\,T^{-2}}]$, J
> **Meaning:** a positive scalar, zero only when every element is at rest in $S_0$.

### 3.1 Expansion with the velocity field from A(B)

> [!derivation] Kinetic energy expanded from the body point A(B)
> **Law:** velocity field Eq. 11.5 and the square of a sum
> **Source:** Notes.pdf, Eq. 11.23; Notes.pdf, Eq. 11.24; [Lecture 9, Slide 8]
>
> $$\begin{aligned}
> T_0 &= \frac{1}{2}\int_{\mathcal D} \left(\mathbf v_0^{A(B)} + \boldsymbol\omega_{B0} \times \mathbf r_A^P\right) \cdot \left(\mathbf v_0^{A(B)} + \boldsymbol\omega_{B0} \times \mathbf r_A^P\right) dm \quad &\text{(Eq. 11.5 in Eq. 11.22)} \\
> &= \frac{1}{2}\int_{\mathcal D} \left[\left(v_0^{A(B)}\right)^2 + 2\,\mathbf v_0^{A(B)} \cdot \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) + \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) \cdot \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right)\right] dm \quad &\text{(square of a sum of two vectors)} \\
> &= \frac{1}{2}m\left(v_0^{A(B)}\right)^2 + \left[\boldsymbol\omega_{B0} \times \left(\int_{\mathcal D} \mathbf r_A^P\,dm\right)\right] \cdot \mathbf v_0^{A(B)} + \frac{1}{2}\int_{\mathcal D} \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) \cdot \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) dm \quad &\text{(constant vectors out of the integrals: Eq. 11.23)} \\
> \left[\boldsymbol\omega_{B0} \times \left(\int_{\mathcal D} \mathbf r_A^P\,dm\right)\right] \cdot \mathbf v_0^{A(B)} &= m\left(\boldsymbol\omega_{B0} \times \mathbf r_A^G\right) \cdot \mathbf v_0^{A(B)} \quad &\text{(first moment about A, Eq. 11.7: Eq. 11.24)}
> \end{aligned}$$
>
> $$\boxed{T_0 = \frac{1}{2}m\left(v_0^{A(B)}\right)^2 + m\left(\boldsymbol\omega_{B0} \times \mathbf r_A^G\right) \cdot \mathbf v_0^{A(B)} + \frac{1}{2}\int_{\mathcal D} \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) \cdot \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) dm}$$
>
> **Units:** $[\mathrm{M}]\,[\mathrm{L^2\,T^{-2}}] = [\mathrm{M\,L^2\,T^{-2}}]$ in each of the three terms
> **Meaning:** a translational term, a coupling term and a rotational term; the last one is reduced next.

> [!derivation] Rotational term of the kinetic energy
> **Law:** dot product of two vector products, Notes Eq. 1.38; unit tensor and dyadic product
> **Source:** Notes.pdf, Eq. 11.25; Notes.pdf, Eq. 11.26; Notes.pdf, Eq. 11.27; Notes.pdf, Eq. 11.28; Notes.pdf, Eq. 11.29; [Lecture 9, Slide 8]
>
> $$\begin{aligned}
> (\mathbf A \times \mathbf B) \cdot (\mathbf C \times \mathbf D) &= (\mathbf A \cdot \mathbf C)(\mathbf B \cdot \mathbf D) - (\mathbf A \cdot \mathbf D)(\mathbf B \cdot \mathbf C) \quad &\text{(Notes Eq. 1.38: Eq. 11.25)} \\
> \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) \cdot \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) &= \left(\boldsymbol\omega_{B0} \cdot \boldsymbol\omega_{B0}\right)\left(\mathbf r_A^P \cdot \mathbf r_A^P\right) - \left(\boldsymbol\omega_{B0} \cdot \mathbf r_A^P\right)\left(\mathbf r_A^P \cdot \boldsymbol\omega_{B0}\right) \quad &\text{(A = C = omega, B = D = r: Eq. 11.26)} \\
> \left(\boldsymbol\omega_{B0} \cdot \boldsymbol\omega_{B0}\right)\left(r_A^P\right)^2 &= \boldsymbol\omega_{B0} \cdot \left(r_A^P\right)^2 \overline{\overline{\mathcal U}} \cdot \boldsymbol\omega_{B0} \quad &\text{(scalar factor moved inside; unit tensor: Eq. 11.27)} \\
> \left(\boldsymbol\omega_{B0} \cdot \mathbf r_A^P\right)\left(\mathbf r_A^P \cdot \boldsymbol\omega_{B0}\right) &= \sum_{i}\sum_{j} \omega_i\,r_i\,r_j\,\omega_j = \boldsymbol\omega_{B0} \cdot \left(\mathbf r_A^P \otimes \mathbf r_A^P\right) \cdot \boldsymbol\omega_{B0} \quad &\text{(components of the dyadic product: Eq. 11.28)} \\
> \frac{1}{2}\int_{\mathcal D} \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) \cdot \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) dm &= \frac{1}{2}\int_{\mathcal D} \left[\boldsymbol\omega_{B0} \cdot \left(r_A^P\right)^2 \overline{\overline{\mathcal U}} \cdot \boldsymbol\omega_{B0} - \boldsymbol\omega_{B0} \cdot \left(\mathbf r_A^P \otimes \mathbf r_A^P\right) \cdot \boldsymbol\omega_{B0}\right] dm \quad &\text{(the two previous rows)} \\
> &= \frac{1}{2}\boldsymbol\omega_{B0} \cdot \left\{\int_{\mathcal D} \left[\left(r_A^P\right)^2 \overline{\overline{\mathcal U}} - \mathbf r_A^P \otimes \mathbf r_A^P\right] dm\right\} \cdot \boldsymbol\omega_{B0} \quad &\text{(the angular velocity is the same for every element)} \\
> &= \frac{1}{2}\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0} \quad &\text{(Notes Eq. 10.35 about A: Eq. 11.29)}
> \end{aligned}$$
>
> $$\boxed{\frac{1}{2}\int_{\mathcal D} \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) \cdot \left(\boldsymbol\omega_{B0} \times \mathbf r_A^P\right) dm = \frac{1}{2}\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0}}$$
>
> **Units:** $[\mathrm{T^{-1}}]\,[\mathrm{M\,L^2}]\,[\mathrm{T^{-1}}] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the rotational kinetic energy is a quadratic form of the angular velocity whose matrix is the tensor of inertia.

> [!derivation] Kinetic energy about A(B), and its two simple cases
> **Law:** sum of the three terms; particular choices of A
> **Source:** Notes.pdf, Eq. 11.30; Notes.pdf, Eq. 11.31; Notes.pdf, Eq. 11.32; [Lecture 9, Slide 9]
>
> $$\begin{aligned}
> T_0 &= \frac{1}{2}\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0} + \frac{1}{2}m\left(v_0^{A(B)}\right)^2 + m\left(\boldsymbol\omega_{B0} \times \mathbf r_A^G\right) \cdot \mathbf v_0^{A(B)} \quad &\text{(Eqs. 11.23, 11.24 and 11.29: Eq. 11.30)} \\
> T_0 &= \frac{1}{2}\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0} + \frac{1}{2}m\left(v_0^G\right)^2 \quad &\text{(A = G: the arm from G to G is zero, Eq. 11.31)} \\
> T_0 &= \frac{1}{2}\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0} \quad &\text{(A fixed body point: zero velocity, Eq. 11.32)}
> \end{aligned}$$
>
> $$\boxed{T_0 = \frac{1}{2}\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0} + \frac{1}{2}m\left(v_0^{A(B)}\right)^2 + m\left(\boldsymbol\omega_{B0} \times \mathbf r_A^G\right) \cdot \mathbf v_0^{A(B)}}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]$ in each term
> **Meaning:** the coupling term disappears when the reference point is $G$ or a fixed point of the body.

### 3.2 Expansion about the centre of mass (Koenig's theorem)

> [!derivation] Kinetic energy split into translation of G and rotation about G
> **Law:** velocity field from G, square of a sum, first moment about G (Eq. 10.44)
> **Source:** Notes.pdf, Eq. 11.33; Notes.pdf, Eq. 11.34; Notes.pdf, Eq. 11.35; Notes.pdf, Eq. 11.36; Notes.pdf, Eq. 11.37; [Lecture 9, Slide 10]
>
> $$\begin{aligned}
> \left(v_0^P\right)^2 &= \mathbf v_0^P \cdot \mathbf v_0^P = \left(\mathbf v_0^G + \boldsymbol\omega_{B0} \times \mathbf r_G^P\right) \cdot \left(\mathbf v_0^G + \boldsymbol\omega_{B0} \times \mathbf r_G^P\right) \quad &\text{(velocity field from G)} \\
> &= \left(v_0^G\right)^2 + \left|\boldsymbol\omega_{B0} \times \mathbf r_G^P\right|^2 + 2\,\mathbf v_0^G \cdot \left(\boldsymbol\omega_{B0} \times \mathbf r_G^P\right) \quad &\text{(square of a sum: Eq. 11.33)} \\
> \frac{1}{2}\int_{\mathcal D} \left(v_0^G\right)^2 dm &= \frac{1}{2}m\left(v_0^G\right)^2 \quad &\text{(constant over the body: Eq. 11.34)} \\
> \int_{\mathcal D} \mathbf v_0^G \cdot \left(\boldsymbol\omega_{B0} \times \mathbf r_G^P\right) dm &= \mathbf v_0^G \cdot \left(\boldsymbol\omega_{B0} \times \int_{\mathcal D} \mathbf r_G^P\,dm\right) = 0 \quad &\text{(Notes Eq. 10.44: Eq. 11.35)} \\
> \frac{1}{2}\int_{\mathcal D} \left|\boldsymbol\omega_{B0} \times \mathbf r_G^P\right|^2 dm &= \frac{1}{2}\int_{\mathcal D} \left(v_G^P\right)^2 dm = T_G \quad &\text{(velocity seen from SG, kinetic energy in SG: Eq. 11.36)} \\
> T_0 &= \frac{1}{2}m\left(v_0^G\right)^2 + 0 + T_G \quad &\text{(the three integrals in Eq. 11.22)}
> \end{aligned}$$
>
> $$\boxed{T_0 = T_G + \frac{1}{2}m\left(v_0^G\right)^2}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]$ on both sides
> **Meaning:** the kinetic energy is the energy of the rotation about $G$ (seen from the translating frame $S_G$) plus that of a point mass $m$ moving with $G$; comparing with Eq. 11.31, the energy seen from $S_G$ is one half of the quadratic form of the tensor of inertia about $G$.

> [!note]
> In the literature Eq. 11.37 is known as Koenig's theorem for the kinetic energy, and Eq. 11.20 as the corresponding theorem for the angular momentum. The notes do not use the name; the results are those of the notes.

### 3.3 Kinetic energy and the instantaneous axis of rotation

> [!info] Extension: kinetic energy as one half of the moment of inertia about the axis of rotation times the angular speed squared
> The notes write the kinetic energy with the tensor of inertia (Eqs. 11.31 and 11.32). The scalar form below follows from them and from the moment of inertia about a line (Notes Eq. 10.39); it is not printed in chapter 11, so it is marked as an extension. Two cases are covered: a body with a fixed point $A$, and a body whose instantaneous axis of rotation has zero slip velocity (Notes Eq. 9.8), the case of every plane motion. The unit vector of the axis is $\mathbf e_\omega$ and the angular speed is $\omega$.

> [!derivation] T as one half of I times omega squared (extension)
> **Law:** Eq. 11.32 (or Eq. 11.30 at a point of zero velocity) with the moment of inertia about a line, Eq. 10.39
> **Source:** Notes.pdf, Eq. 11.32; Notes.pdf, Eq. 10.39; Notes.pdf, Eq. 9.8
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0} &= \omega\,\mathbf e_\omega \quad &\text{(modulus times unit vector of the angular velocity)} \\
> T_0 &= \frac{1}{2}\left(\omega\,\mathbf e_\omega\right) \cdot \overline{\overline{\mathcal I}}_A \cdot \left(\omega\,\mathbf e_\omega\right) \quad &\text{(A fixed body point, Eq. 11.32)} \\
> &= \frac{1}{2}\omega^2\left(\mathbf e_\omega \cdot \overline{\overline{\mathcal I}}_A \cdot \mathbf e_\omega\right) \quad &\text{(scalars out of the bilinear form)} \\
> &= \frac{1}{2}I_\ell\,\omega^2 \quad &\text{(Notes Eq. 10.39: moment of inertia about the line through A along the axis)} \\
> \mathbf v_0^{I(B)} &= \mathbf 0 \quad &\text{(point I of the instantaneous axis with zero slip, Notes Eq. 9.8)} \\
> T_0 &= \frac{1}{2}\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_I \cdot \boldsymbol\omega_{B0} + \frac{1}{2}m\cdot 0 + m\left(\boldsymbol\omega_{B0} \times \mathbf r_I^G\right) \cdot \mathbf 0 \quad &\text{(Eq. 11.30 at the instant, with A = I)} \\
> &= \frac{1}{2}I_\ell\,\omega^2 \quad &\text{(same steps as for the fixed point)}
> \end{aligned}$$
>
> $$\boxed{T_0 = \frac{1}{2}I_\ell\,\omega^2, \qquad I_\ell = \mathbf e_\omega \cdot \overline{\overline{\mathcal I}}_A \cdot \mathbf e_\omega}$$
>
> **Units:** $[\mathrm{M\,L^2}]\,[\mathrm{T^{-2}}] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** at that instant the body moves as a pure rotation about the axis, and its energy is that of rotation about that line; the tensor about $I$ changes from instant to instant, because $I$ is a different body point each time.

> [!derivation] Moment of inertia about the axis from the parallel axis through G (extension)
> **Law:** Steiner's theorem, Notes Eq. 10.48, projected on the unit vector of the axis
> **Source:** Notes.pdf, Eq. 10.48; Notes.pdf, Eq. 10.39
>
> $$\begin{aligned}
> \overline{\overline{\mathcal I}}_A &= \overline{\overline{\mathcal I}}_G + m\left[\left(r_A^G\right)^2 \overline{\overline{\mathcal U}} - \mathbf r_A^G \otimes \mathbf r_A^G\right] \quad &\text{(Notes Eq. 10.48 with origin A)} \\
> \mathbf e_\omega \cdot \overline{\overline{\mathcal I}}_A \cdot \mathbf e_\omega &= \mathbf e_\omega \cdot \overline{\overline{\mathcal I}}_G \cdot \mathbf e_\omega + m\left[\left(r_A^G\right)^2 - \left(\mathbf r_A^G \cdot \mathbf e_\omega\right)^2\right] \quad &\text{(unit tensor and dyadic product contracted with the unit vector)} \\
> \left(r_A^G\right)^2 - \left(\mathbf r_A^G \cdot \mathbf e_\omega\right)^2 &= d^2 \quad &\text{(right triangle: hypotenuse r, leg along the axis r cos, other leg d, distance from G to the axis)}
> \end{aligned}$$
>
> $$\boxed{I_\ell = I_{\ell G} + m\,d^2}$$
>
> **Units:** $[\mathrm{M\,L^2}]$ in each term
> **Meaning:** the parallel axis through $G$ always gives the smallest moment of inertia in a family of parallel axes.

## 4. Equations of motion of a material system

A material system is regarded as a collection of point particles $P_i$, $i$ from 1 to $N$ (for a continuous body the sums become integrals without changing the results). Two kinds of forces act on it (Notes Fig. 12.1):

| Symbol | Meaning |
| :--- | :--- |
| $\mathbf f_{P_j}^{P_i}$ | internal force on $P_i$ caused by the particle $P_j$ of the same system |
| $\mathbf F^{P_i}$ | external force on $P_i$ caused by the environment |
| $\mathbf F$ | resultant of the external forces |
| $\mathbf M_A$ | resultant moment of the external forces about $A$ |

![[attachments/EM-T/t7-internal-external-forces.svg]]

A system of $N$ free particles has $3N$ degrees of freedom and needs the $3N$ scalar equations of Newton's second law. A rigid body is an infinite collection of particles, but the rigidity constraint leaves only 6 degrees of freedom, so 6 independent scalar equations are enough [Lecture 10, Slide 3]. These are the two vector equations derived in this section.

> [!derivation] Internal forces: action and reaction, and their moment
> **Law:** Newton's third law with collinear internal forces
> **Source:** Notes.pdf, Eq. 12.1; Notes.pdf, Eq. 12.2; [Lecture 10, Slide 3]
>
> $$\begin{aligned}
> \mathbf f_{P_j}^{P_i} &= -\mathbf f_{P_i}^{P_j} \quad &\text{(third law: equal and opposite, Eq. 12.1)} \\
> \mathbf f_{P_j}^{P_i} &= \lambda_{ij}\,\overrightarrow{P_i P_j} \quad &\text{(collinear: parallel to the line from Pi to Pj, lambda a scalar)} \\
> \mathbf r_A^{P_i} \times \mathbf f_{P_j}^{P_i} + \mathbf r_A^{P_j} \times \mathbf f_{P_i}^{P_j} &= \left(\mathbf r_A^{P_i} - \mathbf r_A^{P_j}\right) \times \mathbf f_{P_j}^{P_i} \quad &\text{(third law in the second term)} \\
> &= \overrightarrow{P_j P_i} \times \lambda_{ij}\,\overrightarrow{P_i P_j} \quad &\text{(difference of the arms; collinearity)} \\
> &= \mathbf 0 \quad &\text{(cross product of two parallel vectors)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_A^{P_i} \times \mathbf f_{P_j}^{P_i} = -\mathbf r_A^{P_j} \times \mathbf f_{P_i}^{P_j}}$$
>
> **Units:** $[\mathrm{L}]\,[\mathrm{M\,L\,T^{-2}}] = [\mathrm{M\,L^2\,T^{-2}}]$, N m
> **Meaning:** an internal pair has zero resultant and zero moment about any point.

> [!derivation] Resultant force equation
> **Law:** Newton's second law for every particle, summed
> **Source:** Notes.pdf, Eq. 12.3; Notes.pdf, Eq. 12.4; [Lecture 10, Slide 4]
>
> $$\begin{aligned}
> \mathbf F^{P_i} + \sum_{j \neq i} \mathbf f_{P_j}^{P_i} &= m^{P_i}\,\mathbf a_0^{P_i}, \quad i = 1, \dots, N \quad &\text{(second law in the inertial frame S0, Eq. 12.3)} \\
> \sum_{i=1}^{N} \mathbf F^{P_i} + \sum_{i=1}^{N}\sum_{j \neq i} \mathbf f_{P_j}^{P_i} &= \sum_{i=1}^{N} m^{P_i}\,\mathbf a_0^{P_i} \quad &\text{(sum of the N equations)} \\
> \sum_{i=1}^{N}\sum_{j \neq i} \mathbf f_{P_j}^{P_i} &= \sum_{i \lt j}\left(\mathbf f_{P_j}^{P_i} + \mathbf f_{P_i}^{P_j}\right) = \mathbf 0 \quad &\text{(grouped in pairs; Eq. 12.1)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F = \sum_{i=1}^{N} \mathbf F^{P_i} = \sum_{i=1}^{N} m^{P_i}\,\mathbf a_0^{P_i}}$$
>
> **Units:** $[\mathrm{M}]\,[\mathrm{L\,T^{-2}}] = [\mathrm{M\,L\,T^{-2}}]$, N
> **Meaning:** only external forces appear in the resultant.

> [!derivation] Resultant moment equation
> **Law:** moment of Newton's second law about A for every particle, summed
> **Source:** Notes.pdf, Eq. 12.5; [Lecture 10, Slide 5]
>
> $$\begin{aligned}
> \mathbf r_A^{P_i} \times \left(\mathbf F^{P_i} + \sum_{j \neq i} \mathbf f_{P_j}^{P_i}\right) &= m^{P_i}\,\mathbf r_A^{P_i} \times \mathbf a_0^{P_i} \quad &\text{(cross product of Eq. 12.3 with the arm from A)} \\
> \sum_{i=1}^{N} \mathbf r_A^{P_i} \times \mathbf F^{P_i} + \sum_{i \lt j}\left(\mathbf r_A^{P_i} \times \mathbf f_{P_j}^{P_i} + \mathbf r_A^{P_j} \times \mathbf f_{P_i}^{P_j}\right) &= \sum_{i=1}^{N} m^{P_i}\,\mathbf r_A^{P_i} \times \mathbf a_0^{P_i} \quad &\text{(sum, internal terms grouped in pairs)} \\
> \sum_{i \lt j}\left(\mathbf r_A^{P_i} \times \mathbf f_{P_j}^{P_i} + \mathbf r_A^{P_j} \times \mathbf f_{P_i}^{P_j}\right) &= \mathbf 0 \quad &\text{(Eq. 12.2)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M_A = \sum_{i=1}^{N} \mathbf r_A^{P_i} \times \mathbf F^{P_i} = \sum_{i=1}^{N} m^{P_i}\,\mathbf r_A^{P_i} \times \mathbf a_0^{P_i}}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]$, N m
> **Meaning:** only the external forces contribute to the resultant moment about any point $A$.

> [!derivation] Motion of the centre of mass
> **Law:** constant particle masses; definition of the centre of mass differentiated twice
> **Source:** Notes.pdf, Eq. 12.6; Notes.pdf, Eq. 12.7; Notes.pdf, Eq. 12.8; [Lecture 10, Slide 4]; [Lecture 9, Slide 12]
>
> $$\begin{aligned}
> \mathbf F &= \sum_{i=1}^{N} m^{P_i}\,\mathbf a_0^{P_i} = \sum_{i=1}^{N} m^{P_i} \frac{d^2\mathbf r_0^{P_i}}{dt^2} \quad &\text{(acceleration as second derivative of the position)} \\
> &= \frac{d^2}{dt^2}\sum_{i=1}^{N} m^{P_i}\,\mathbf r_0^{P_i} \quad &\text{(constant masses: derivative out of the sum, Eq. 12.6)} \\
> &= \frac{d^2}{dt^2}\left(m\,\mathbf r_0^G\right) \quad &\text{(definition of the centre of mass, discrete form of Notes Eq. 10.8)} \\
> &= m\frac{d\mathbf v_0^G}{dt} = m\,\mathbf a_0^G \quad &\text{(m constant: Eq. 12.7)} \\
> \left.\frac{d\mathbf p_0}{dt}\right|_0 &= \left.\frac{d}{dt}\left(m\,\mathbf v_0^G\right)\right|_0 = m\,\mathbf a_0^G \quad &\text{(Eq. 11.3 differentiated)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf p_0}{dt}\right|_0 = \mathbf F = m\,\mathbf a_0^G}$$
>
> **Units:** $[\mathrm{M}]\,[\mathrm{L\,T^{-2}}] = [\mathrm{M\,L\,T^{-2}}]$, N
> **Meaning:** the centre of mass moves like a point particle of mass $m$ under the resultant of the external forces, whatever the internal forces are.

> [!derivation] Inertia term of the moment equation
> **Law:** angular momentum of a particle about a moving point A (Eq. 4.52) and the product rule
> **Source:** Notes.pdf, Eq. 12.9; Notes.pdf, Eq. 12.10; Notes.pdf, Eq. 12.11; [Lecture 10, Slide 5]
>
> $$\begin{aligned}
> \sum_{i=1}^{N} m^{P_i}\,\mathbf r_A^{P_i} \times \mathbf a_0^{P_i} &= \sum_{i=1}^{N}\left(\mathbf r_0^{P_i} - \mathbf r_0^A\right) \times m^{P_i}\,\mathbf a_0^{P_i} \quad &\text{(arm written with positions from O: Eq. 12.9)} \\
> \mathbf H_{A,0}^{P_i} &= \mathbf r_A^{P_i} \times m^{P_i}\,\mathbf v_0^{P_i} = \left(\mathbf r_0^{P_i} - \mathbf r_0^A\right) \times m^{P_i}\,\mathbf v_0^{P_i} \quad &\text{(angular momentum of Pi about A, Eq. 12.10)} \\
> \left.\frac{d\mathbf H_{A,0}^{P_i}}{dt}\right|_0 &= \left(\mathbf r_0^{P_i} - \mathbf r_0^A\right) \times m^{P_i}\,\mathbf a_0^{P_i} + \left(\mathbf v_0^{P_i} - \mathbf v_0^A\right) \times m^{P_i}\,\mathbf v_0^{P_i} \quad &\text{(product rule for the cross product)} \\
> &= \mathbf r_A^{P_i} \times m^{P_i}\,\mathbf a_0^{P_i} - \mathbf v_0^A \times m^{P_i}\,\mathbf v_0^{P_i} \quad &\text{(the velocity crossed with itself is zero: Eq. 12.11)}
> \end{aligned}$$
>
> $$\boxed{m^{P_i}\,\mathbf r_A^{P_i} \times \mathbf a_0^{P_i} = \left.\frac{d\mathbf H_{A,0}^{P_i}}{dt}\right|_0 + \mathbf v_0^A \times m^{P_i}\,\mathbf v_0^{P_i}}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]$ in each term
> **Meaning:** the moment of the inertia of each particle is the rate of its angular momentum plus a term due to the motion of the pole $A$.

> [!derivation] Angular momentum equation of a material system
> **Law:** sum over the particles; definition of the centre of mass
> **Source:** Notes.pdf, Eq. 12.12; Notes.pdf, Eq. 12.13; [Lecture 10, Slide 5]; [Lecture 9, Slide 13]
>
> $$\begin{aligned}
> \sum_{i=1}^{N} m^{P_i}\,\mathbf r_A^{P_i} \times \mathbf a_0^{P_i} &= \sum_{i=1}^{N}\left.\frac{d\mathbf H_{A,0}^{P_i}}{dt}\right|_0 + \mathbf v_0^A \times \sum_{i=1}^{N} m^{P_i}\,\mathbf v_0^{P_i} \quad &\text{(Eq. 12.11 summed; the velocity of A is common)} \\
> &= \left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 + m\,\mathbf v_0^A \times \mathbf v_0^G \quad &\text{(total angular momentum; Eq. 11.3 in discrete form: Eq. 12.12)} \\
> \mathbf M_A &= \left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 + m\,\mathbf v_0^A \times \mathbf v_0^G \quad &\text{(Eq. 12.5)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 = \mathbf M_A - m\,\mathbf v_0^A \times \mathbf v_0^G}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]$ in each term
> **Meaning:** the particle law of Notes Eq. 4.52 holds for any material system with its total angular momentum; $\mathbf v_0^A$ is the velocity of the geometric point $A$, which may or may not belong to the body.

Equations 12.8 and 12.13 are the evolution equations of the total linear and angular momentum. For a deformable body with $N$ particles they are not enough ($3N$ degrees of freedom), and the individual equations 12.3 are needed. For a free rigid body (6 degrees of freedom) Eqs. 12.8 and 12.13 solve the dynamics completely (Notes Sec. 12.1).

### 4.1 Energy equation of a material system

> [!derivation] Kinetic energy equation of a system of particles
> **Law:** dot product of Newton's second law with the velocity of each particle; chain rule
> **Source:** [Lecture 10, Slide 6]; [Lecture 9, Slide 14]; Notes.pdf, Eq. 4.11
>
> $$\begin{aligned}
> m^{P_i}\,\mathbf v_0^{P_i} \cdot \mathbf a_0^{P_i} &= \mathbf v_0^{P_i} \cdot \mathbf F^{P_i} + \sum_{j \neq i} \mathbf v_0^{P_i} \cdot \mathbf f_{P_j}^{P_i} \quad &\text{(Eq. 12.3 dotted with the velocity of Pi)} \\
> \left.\frac{d}{dt}\left(\mathbf v_0^{P_i} \cdot \mathbf v_0^{P_i}\right)\right|_0 &= 2\,\mathbf v_0^{P_i} \cdot \left.\frac{d\mathbf v_0^{P_i}}{dt}\right|_0 \quad &\text{(product rule for the dot product)} \\
> m^{P_i}\,\mathbf v_0^{P_i} \cdot \mathbf a_0^{P_i} &= \frac{1}{2}m^{P_i}\left.\frac{d\left(v_0^{P_i}\right)^2}{dt}\right|_0 = \left.\frac{dT_0^{P_i}}{dt}\right|_0 \quad &\text{(previous row; Notes Eq. 4.2)} \\
> \sum_{i=1}^{N}\left.\frac{dT_0^{P_i}}{dt}\right|_0 &= \sum_{i=1}^{N} \mathbf v_0^{P_i} \cdot \mathbf F^{P_i} + \sum_{i=1}^{N}\sum_{j \neq i} \mathbf v_0^{P_i} \cdot \mathbf f_{P_j}^{P_i} \quad &\text{(sum of the N equations)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{dT_0}{dt}\right|_0 = \dot W_0 + \dot w_0}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-3}}]$, W, in each term
> **Meaning:** $\dot W_0$ is the power of the external forces and $\dot w_0$ that of the internal forces; unlike the resultant force and moment, the internal power does not cancel in general.

> [!derivation] The internal forces of a rigid body do no work
> **Law:** third law, collinearity and the velocity field of a rigid body
> **Source:** [Lecture 10, Slide 6]; [Lecture 10, Slide 8]; Notes.pdf, Eq. 9.3
>
> $$\begin{aligned}
> \mathbf v_0^{P_i} \cdot \mathbf f_{P_j}^{P_i} + \mathbf v_0^{P_j} \cdot \mathbf f_{P_i}^{P_j} &= \left(\mathbf v_0^{P_i} - \mathbf v_0^{P_j}\right) \cdot \mathbf f_{P_j}^{P_i} \quad &\text{(Eq. 12.1 in the second term)} \\
> \mathbf v_0^{P_i} - \mathbf v_0^{P_j} &= \boldsymbol\omega_{B0} \times \overrightarrow{P_j P_i} \quad &\text{(velocity field of the rigid body, Notes Eq. 9.3)} \\
> \left(\mathbf v_0^{P_i} - \mathbf v_0^{P_j}\right) \cdot \mathbf f_{P_j}^{P_i} &= \left(\boldsymbol\omega_{B0} \times \overrightarrow{P_j P_i}\right) \cdot \left(-\lambda_{ij}\,\overrightarrow{P_j P_i}\right) \quad &\text{(collinear internal force)} \\
> &= 0 \quad &\text{(a vector product is perpendicular to each of its factors)}
> \end{aligned}$$
>
> $$\boxed{\dot w_0 = 0 \quad\Rightarrow\quad \left.\frac{dT_0}{dt}\right|_0 = \dot W_0}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-3}}]$ on both sides
> **Meaning:** the distance between two points of a rigid body never changes, so each internal pair does equal and opposite powers; the energy equation of a rigid body is not independent of Eqs. 12.8 and 12.13.

> [!example] Interlude of the slides: a spring between two particles
> Internal forces, like external ones, can be conservative: there is then a function $V$ of the positions of the two particles whose partial derivatives give the pair of forces [Lecture 10, Slide 7]. The slide takes two particles $P_1$ and $P_2$ joined by a spring of stiffness $k$ and natural length zero. Each internal potential energy term appears only once in the energy equation, not once per particle.

![[attachments/EM-T/t7-spring-pair.svg]]

> [!derivation] Forces of the spring from its potential energy
> **Law:** conservative internal pair, force as minus the gradient (Eq. 4.19) with respect to the position of each particle
> **Source:** [Lecture 10, Slide 7]; Notes.pdf, Eq. 4.19
>
> $$\begin{aligned}
> V &= \frac{1}{2}k\left|\mathbf r_0^{P_1} - \mathbf r_0^{P_2}\right|^2 = \frac{1}{2}k\left[\left(x^{P_1} - x^{P_2}\right)^2 + \left(y^{P_1} - y^{P_2}\right)^2 + \left(z^{P_1} - z^{P_2}\right)^2\right] \quad &\text{(potential of the slide in Cartesian components)} \\
> \frac{\partial V}{\partial x^{P_1}} &= \frac{1}{2}k \cdot 2\left(x^{P_1} - x^{P_2}\right) \cdot 1 = k\left(x^{P_1} - x^{P_2}\right) \quad &\text{(chain rule: outer square, inner derivative 1)} \\
> \frac{\partial V}{\partial x^{P_2}} &= \frac{1}{2}k \cdot 2\left(x^{P_1} - x^{P_2}\right) \cdot (-1) = -k\left(x^{P_1} - x^{P_2}\right) \quad &\text{(chain rule: inner derivative minus 1)} \\
> \mathbf f_{P_2}^{P_1} &= -\frac{\partial V}{\partial x^{P_1}}\mathbf i - \frac{\partial V}{\partial y^{P_1}}\mathbf j - \frac{\partial V}{\partial z^{P_1}}\mathbf k = -k\left(\mathbf r_0^{P_1} - \mathbf r_0^{P_2}\right) \quad &\text{(same steps for y and z)} \\
> \mathbf f_{P_1}^{P_2} &= -\frac{\partial V}{\partial x^{P_2}}\mathbf i - \frac{\partial V}{\partial y^{P_2}}\mathbf j - \frac{\partial V}{\partial z^{P_2}}\mathbf k = +k\left(\mathbf r_0^{P_1} - \mathbf r_0^{P_2}\right) \quad &\text{(same steps for y and z)} \\
> \dot w_0 &= \mathbf f_{P_2}^{P_1} \cdot \mathbf v_0^{P_1} + \mathbf f_{P_1}^{P_2} \cdot \mathbf v_0^{P_2} = -k\left(\mathbf r_0^{P_1} - \mathbf r_0^{P_2}\right) \cdot \left(\mathbf v_0^{P_1} - \mathbf v_0^{P_2}\right) \quad &\text{(power of the internal pair)} \\
> &= -\frac{d}{dt}\left[\frac{1}{2}k\left|\mathbf r_0^{P_1} - \mathbf r_0^{P_2}\right|^2\right] = -\frac{dV}{dt} \quad &\text{(chain rule on the squared modulus)}
> \end{aligned}$$
>
> $$\boxed{\mathbf f_{P_2}^{P_1} = -k\left(\mathbf r_0^{P_1} - \mathbf r_0^{P_2}\right), \qquad \mathbf f_{P_1}^{P_2} = +k\left(\mathbf r_0^{P_1} - \mathbf r_0^{P_2}\right), \qquad \dot w_0 = -\frac{dV}{dt}}$$
>
> **Units:** $[\mathrm{M\,T^{-2}}]\,[\mathrm{L}] = [\mathrm{M\,L\,T^{-2}}]$ for the forces; $[\mathrm{M\,T^{-2}}]\,[\mathrm{L^2}] = [\mathrm{M\,L^2\,T^{-2}}]$ for $V$
> **Meaning:** the pair obeys the third law and is collinear; its power is not zero because the spring changes length (the system is not rigid), and it enters the energy balance through the single term $V$.

## 5. General equations for a rigid body

### 5.1 Choice of the point A

> [!derivation] The two convenient choices of the point of moments
> **Law:** Eq. 12.13 with the extra term made zero; Eqs. 11.12 and 11.13
> **Source:** Notes.pdf, Eq. 12.13; [Lecture 10, Slide 8]
>
> $$\begin{aligned}
> \left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 &= \mathbf M_A - m\,\mathbf v_0^A \times \mathbf v_0^G \quad &\text{(Eq. 12.13)} \\
> m\,\mathbf v_0^G \times \mathbf v_0^G &= \mathbf 0 \quad &\text{(choice 1: A = G, a vector crossed with itself)} \\
> m\,\mathbf 0 \times \mathbf v_0^G &= \mathbf 0 \quad &\text{(choice 2: A a fixed point of the body)} \\
> \mathbf H_{A,0} &= \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0} \quad &\text{(Eqs. 11.12 and 11.13 for both choices)}
> \end{aligned}$$
>
> $$\boxed{m\,\mathbf a_0^G = \mathbf F, \qquad \left.\frac{d}{dt}\left(\overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0}\right)\right|_0 = \mathbf M_A \quad (A \equiv G \text{ or } A \text{ fixed body point})}$$
>
> **Units:** N on the left equation, N m on the right equation
> **Meaning:** the translation depends only on the resultant force and the mass; the rotation only on the resultant moment and the tensor of inertia.

The centre of mass is the point used for a general motion. When the body has a fixed point, that point is preferable: the reaction that keeps it fixed is unknown, but it has no moment about the pivot, so it does not appear in the rotational equations (Notes Sec. 12.2). The translational and rotational equations are coupled in general; the six scalar equations are of second order, so 12 initial conditions are needed, for example the coordinates of $G$, three Euler angles and their first derivatives at the initial instant.

### 5.2 External torques

When two external forces are equal and opposite but have different lines of action, their resultant is zero and they produce a torque $\mathbf Q_k$, the same about every point. It is convenient to replace such pairs by their torques.

> [!derivation] Resultant moment with external torques
> **Law:** moment of the external forces plus the free vectors of the torques
> **Source:** Notes.pdf, Eq. 12.14; [Lecture 10, Slide 12]
>
> $$\begin{aligned}
> \mathbf M_A &= \sum_{i=1}^{N} \mathbf r_A^{P_i} \times \mathbf F^{P_i} + \sum_{k=1}^{M} \mathbf Q_k \quad &\text{(Eq. 12.5 redefined with M external torques)} \\
> \mathbf r_A^{P} \times \mathbf F^{P} + \mathbf r_A^{P'} \times \left(-\mathbf F^{P}\right) &= \left(\mathbf r_A^{P} - \mathbf r_A^{P'}\right) \times \mathbf F^{P} = \overrightarrow{P'P} \times \mathbf F^{P} \quad &\text{(a couple: the arm from A cancels, so it is a free vector)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M_A = \sum_{i=1}^{N} \mathbf r_A^{P_i} \times \mathbf F^{P_i} + \sum_{k=1}^{M} \mathbf Q_k}$$
>
> **Units:** N m in every term
> **Meaning:** with this definition Eq. 12.13 stays unchanged; internal torques, if any, cancel in pairs and do not affect a rigid body.

### 5.3 Equivalence and reduction of systems of forces and moments

The external forces on a rigid body are sliding vectors and the torques are free vectors, so the dynamics depend only on the pair $\{\mathbf F; \mathbf M_A\}$, the reduction of the system at $A$. Two systems are equivalent when they have the same resultant force and the same resultant moment about one point [Lecture 10, Slide 9]. These ideas apply to rigid bodies only.

![[attachments/EM-T/t7-equivalent-force-systems.svg]]

> [!derivation] Conditions of equivalence of two load systems
> **Law:** definition of equivalence through the reduction at A
> **Source:** Notes.pdf, Sec. 12.2; [Lecture 10, Slide 9]
>
> $$\begin{aligned}
> \mathbf F_1^{P_1} + \mathbf F_2^{P_2} + \dots &= \mathbf F_3^{P_3} + \mathbf F_4^{P_4} + \dots \quad &\text{(same resultant force)} \\
> \mathbf r_A^{P_1} \times \mathbf F_1^{P_1} + \mathbf r_A^{P_2} \times \mathbf F_2^{P_2} + \dots + \mathbf Q_1 + \mathbf Q_2 + \dots &= \mathbf r_A^{P_3} \times \mathbf F_3^{P_3} + \mathbf r_A^{P_4} \times \mathbf F_4^{P_4} + \dots + \mathbf Q_3 + \mathbf Q_4 + \dots \quad &\text{(same resultant moment about one point A)}
> \end{aligned}$$
>
> $$\boxed{\{\mathbf F_1^{P_1}, \mathbf F_2^{P_2}, \dots; \mathbf Q_1, \mathbf Q_2, \dots\} \sim \{\mathbf F_3^{P_3}, \mathbf F_4^{P_4}, \dots; \mathbf Q_3, \mathbf Q_4, \dots\} \iff \{\mathbf F; \mathbf M_A\} \text{ equal}}$$
>
> **Units:** N for the first condition, N m for the second
> **Meaning:** equivalent systems give the same motion of the rigid body; the next box shows that one point is enough.

> [!derivation] Change of the reduction point
> **Law:** definition of the resultant moment with the arms split through A
> **Source:** Notes.pdf, Eq. 12.15; [Lecture 10, Slide 10]
>
> $$\begin{aligned}
> \mathbf M_B &= \sum_{i} \mathbf r_B^{P_i} \times \mathbf F^{P_i} + \sum_k \mathbf Q_k \quad &\text{(Eq. 12.14 about B)} \\
> &= \sum_{i} \left(\overrightarrow{BA} + \mathbf r_A^{P_i}\right) \times \mathbf F^{P_i} + \sum_k \mathbf Q_k \quad &\text{(arm from B split through A)} \\
> &= \overrightarrow{BA} \times \sum_i \mathbf F^{P_i} + \sum_{i} \mathbf r_A^{P_i} \times \mathbf F^{P_i} + \sum_k \mathbf Q_k \quad &\text{(distributive property; BA common to all forces)} \\
> &= \mathbf M_A + \overrightarrow{BA} \times \mathbf F \quad &\text{(Eq. 12.14 about A; resultant force)} \\
> &= \mathbf M_A + \mathbf F \times \overrightarrow{AB} \quad &\text{(anticommutativity: BA cross F equals F cross AB)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M_B = \mathbf M_A + \overrightarrow{BA} \times \mathbf F = \mathbf M_A + \mathbf F \times \overrightarrow{AB}}$$
>
> **Units:** N m in every term
> **Meaning:** the same law as the velocity field of a rigid body (Notes Eq. 9.3), with the moment in the place of the velocity and the force in the place of the angular velocity.

> [!derivation] Invariant of the system and central axis
> **Law:** dot product of Eq. 12.15 with the force; analogy with the instantaneous axis (Eq. 9.10)
> **Source:** Notes.pdf, Eq. 12.15; Notes.pdf, Eq. 9.10
>
> $$\begin{aligned}
> \mathbf M_B \cdot \mathbf F &= \mathbf M_A \cdot \mathbf F + \left(\mathbf F \times \overrightarrow{AB}\right) \cdot \mathbf F \quad &\text{(Eq. 12.15 dotted with F)} \\
> &= \mathbf M_A \cdot \mathbf F \quad &\text{(a vector product is perpendicular to F)} \\
> M_\parallel &\equiv \frac{\mathbf M_A \cdot \mathbf F}{F} \quad &\text{(component along F: the same for every point A)} \\
> \overrightarrow{AB} &= \frac{\mathbf F \times \mathbf M_A}{F^2} \quad &\text{(candidate foot of the central axis, perpendicular to F, as Eq. 9.10)} \\
> \mathbf M_B &= \mathbf M_A + \frac{\mathbf F \times \left(\mathbf F \times \mathbf M_A\right)}{F^2} \quad &\text{(Eq. 12.15)} \\
> &= \mathbf M_A + \frac{\left(\mathbf F \cdot \mathbf M_A\right)\mathbf F - F^2\,\mathbf M_A}{F^2} \quad &\text{(Notes Eq. 1.37)} \\
> &= M_\parallel\,\frac{\mathbf F}{F} \quad &\text{(the two terms in MA cancel)}
> \end{aligned}$$
>
> $$\boxed{M_\parallel = \frac{\mathbf M_A \cdot \mathbf F}{F} \text{ is invariant; on the central axis } \mathbf M_B = M_\parallel\,\frac{\mathbf F}{F}}$$
>
> **Units:** N m
> **Meaning:** on the central axis the moment is minimum and parallel to the force (analogous to the instantaneous axis of rotation and slip); the position of the foot is an extension of the notes, which state only that the line exists.

> [!derivation] Couple of forces and moment about the centre of mass
> **Law:** Eq. 12.15 with zero resultant; Eqs. 12.8 and 12.13 with A at G
> **Source:** Notes.pdf, Eq. 12.15; Notes.pdf, Eq. 12.16
>
> $$\begin{aligned}
> \mathbf M_B &= \mathbf M_A + \mathbf 0 \times \overrightarrow{AB} = \mathbf M_A \quad &\text{(a couple has zero resultant: the moment is the same at every point)} \\
> \mathbf M_G &= \mathbf M_C + \overrightarrow{GC} \times \mathbf F \quad &\text{(Eq. 12.15 from C to G)} \\
> &= \mathbf M_C - \overrightarrow{CG} \times \mathbf F \quad &\text{(GC is minus CG)} \\
> \left.\frac{d\mathbf H_{G,0}}{dt}\right|_0 &= \mathbf M_G - m\,\mathbf v_0^G \times \mathbf v_0^G = \mathbf M_G \quad &\text{(Eq. 12.13 with A = G)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf H_{G,0}}{dt}\right|_0 = \mathbf M_G = \mathbf M_C - \overrightarrow{CG} \times \mathbf F}$$
>
> **Units:** N m in every term
> **Meaning:** the moment about $G$ may be computed at any convenient point $C$ and moved to $G$.

> [!info] Extension: reduction of gravity at the centre of mass
> The notes give the potential energy of the weight (Eq. 12.34, Section 8) but do not reduce the weight itself. The reduction below follows from the definition of the centre of mass and Eq. 12.15; it is marked as an extension. The gravitational acceleration $\mathbf g$ is uniform over the body.

> [!derivation] Weight of a rigid body reduced at G (extension)
> **Law:** resultant and moment of the distributed weight; first moment about G is zero (Eq. 10.44)
> **Source:** Notes.pdf, Eq. 10.44; Notes.pdf, Eq. 12.15
>
> $$\begin{aligned}
> d\mathbf F_g &= \mathbf g\,dm \quad &\text{(weight of an element)} \\
> \mathbf F_g &= \int_{\mathcal D} \mathbf g\,dm = m\,\mathbf g \quad &\text{(uniform g out of the integral; Notes Eq. 10.6)} \\
> \mathbf M_{G,g} &= \int_{\mathcal D} \mathbf r_G^P \times \mathbf g\,dm = \left(\int_{\mathcal D} \mathbf r_G^P\,dm\right) \times \mathbf g \quad &\text{(g common to all the elements)} \\
> &= \mathbf 0 \quad &\text{(Notes Eq. 10.44)} \\
> \mathbf M_{A,g} &= \mathbf M_{G,g} + \overrightarrow{AG} \times m\,\mathbf g = \mathbf r_A^G \times m\,\mathbf g \quad &\text{(Eq. 12.15 from G to A)}
> \end{aligned}$$
>
> $$\boxed{\{\mathbf F_g; \mathbf M_{G,g}\} = \{m\,\mathbf g; \mathbf 0\}, \qquad \mathbf M_{A,g} = \mathbf r_A^G \times m\,\mathbf g}$$
>
> **Units:** N for the force; m times N for the moment
> **Meaning:** the weight of a rigid body is equivalent to one force $m\,\mathbf g$ applied at $G$; it never produces a moment about $G$.

## 6. Rate of change of angular momentum and Euler's equations

### 6.1 Derivative of the angular momentum in the body frame

> [!derivation] The tensor of inertia is not constant in S_0
> **Law:** product rule for a tensor times a vector, Eqs. 11.12 and 11.13
> **Source:** Notes.pdf, Eq. 12.17; Notes.pdf, Eq. 12.18; Notes.pdf, Eq. 12.19
>
> $$\begin{aligned}
> \mathbf H_{A,0} &= \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0} \quad &\text{(A is G or a fixed body point: Eq. 12.17)} \\
> \left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 &= \left.\frac{d}{dt}\left(\overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0}\right)\right|_0 \quad &\text{(left-hand side of Eq. 12.13: Eq. 12.18)} \\
> &= \left.\frac{d\overline{\overline{\mathcal I}}_A}{dt}\right|_0 \cdot \boldsymbol\omega_{B0} + \overline{\overline{\mathcal I}}_A \cdot \left.\frac{d\boldsymbol\omega_{B0}}{dt}\right|_0 \quad &\text{(product rule)} \\
> &= \left.\frac{d\overline{\overline{\mathcal I}}_A}{dt}\right|_0 \cdot \boldsymbol\omega_{B0} + \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\alpha_{B0} \quad &\text{(definition of angular acceleration, Notes Eq. 3.9)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d}{dt}\left(\overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0}\right)\right|_0 = \left.\frac{d\overline{\overline{\mathcal I}}_A}{dt}\right|_0 \cdot \boldsymbol\omega_{B0} + \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\alpha_{B0}}$$
>
> **Units:** $[\mathrm{M\,L^2}]\,[\mathrm{T^{-2}}] = [\mathrm{M\,L^2\,T^{-2}}]$, N m
> **Meaning:** when the body rotates, its mass distribution seen from $S_0$ changes, so the components of the tensor in $B_0$ change in time.

> [!derivation] Derivative computed in the body-fixed frame
> **Law:** Coriolis theorem (Eq. 3.8) between $S_0$ and the body frame $S_B\{A; B_B\}$
> **Source:** Notes.pdf, Eq. 12.20; Notes.pdf, Eq. 12.21; Notes.pdf, Eq. 12.22; [Lecture 10, Slide 13]
>
> $$\begin{aligned}
> \left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 &= \left.\frac{d\mathbf H_{A,0}}{dt}\right|_B + \boldsymbol\omega_{B0} \times \mathbf H_{A,0} \quad &\text{(Notes Eq. 3.8 with the body frame: Eq. 12.20)} \\
> \left.\frac{d\mathbf H_{A,0}}{dt}\right|_B &= \overline{\overline{\mathcal I}}_A \cdot \left.\frac{d\boldsymbol\omega_{B0}}{dt}\right|_B \quad &\text{(the mass distribution is fixed in SB: constant tensor)} \\
> &= \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\alpha_{B0} \quad &\text{(the derivative of omega is the same in SB and S0, Notes Eq. 3.9)} \\
> \left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 &= \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\alpha_{B0} + \boldsymbol\omega_{B0} \times \left(\overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0}\right) \quad &\text{(Eq. 12.21)} \\
> \left.\frac{d\overline{\overline{\mathcal I}}_A}{dt}\right|_0 \cdot \boldsymbol\omega_{B0} &= \boldsymbol\omega_{B0} \times \left(\overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0}\right) \quad &\text{(Eq. 12.19 compared with Eq. 12.21: Eq. 12.22)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 = \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\alpha_{B0} + \boldsymbol\omega_{B0} \times \left(\overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0}\right)}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]$ in both terms
> **Meaning:** a body-fixed basis is the natural one: the tensor has constant components there, and the change of direction of the angular momentum appears as the gyroscopic term.

### 6.2 Euler's equations in principal axes

The basis $B_B$, with unit vectors $\mathbf e_1$, $\mathbf e_2$, $\mathbf e_3$, is now chosen along the principal axes of inertia at $A$ (Notes Sec. 10.7.1), with principal moments $I_1$, $I_2$, $I_3$. The components of the angular velocity and of the angular acceleration in this basis are written $\omega_i$ and $\alpha_i$.

![[attachments/EM-T/t7-principal-axes.svg]]

> [!derivation] Euler's equations
> **Law:** Eq. 12.21 written in components in the principal basis (Eqs. 10.42 and 10.43)
> **Source:** Notes.pdf, Eq. 12.23; Notes.pdf, Eq. 10.42; [Lecture 10, Slide 14]
>
> $$\begin{aligned}
> \left[\overline{\overline{\mathcal I}}_A\right]_{BB} &= \operatorname{diag}\left(I_1, I_2, I_3\right) \quad &\text{(principal basis: diagonal matrix, Notes Eq. 10.42)} \\
> \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\alpha_{B0} &= I_1\alpha_1\,\mathbf e_1 + I_2\alpha_2\,\mathbf e_2 + I_3\alpha_3\,\mathbf e_3 \quad &\text{(product of the diagonal matrix by the column of alpha)} \\
> \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0} &= I_1\omega_1\,\mathbf e_1 + I_2\omega_2\,\mathbf e_2 + I_3\omega_3\,\mathbf e_3 \quad &\text{(same product with omega)} \\
> \boldsymbol\omega_{B0} \times \left(\overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0}\right) &= \left(\omega_2 I_3\omega_3 - \omega_3 I_2\omega_2\right)\mathbf e_1 + \left(\omega_3 I_1\omega_1 - \omega_1 I_3\omega_3\right)\mathbf e_2 + \left(\omega_1 I_2\omega_2 - \omega_2 I_1\omega_1\right)\mathbf e_3 \quad &\text{(vector product in the right-handed basis BB, cofactors of the rows e, omega, I omega)} \\
> &= \left(I_3 - I_2\right)\omega_2\omega_3\,\mathbf e_1 + \left(I_1 - I_3\right)\omega_3\omega_1\,\mathbf e_2 + \left(I_2 - I_1\right)\omega_1\omega_2\,\mathbf e_3 \quad &\text{(expansion along the first row)} \\
> \left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 \cdot \mathbf e_1 &= I_1\alpha_1 + \left(I_3 - I_2\right)\omega_2\omega_3 = I_1\alpha_1 - \left(I_2 - I_3\right)\omega_2\omega_3 \quad &\text{(Eq. 12.21 projected on e1)} \\
> \left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 \cdot \mathbf e_2 &= I_2\alpha_2 - \left(I_3 - I_1\right)\omega_3\omega_1 \quad &\text{(projected on e2)} \\
> \left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 \cdot \mathbf e_3 &= I_3\alpha_3 - \left(I_1 - I_2\right)\omega_1\omega_2 \quad &\text{(projected on e3)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \left.\dfrac{d\mathbf H_{A,0}}{dt}\right|_0 \cdot \mathbf e_1 = I_1\alpha_1 - (I_2 - I_3)\,\omega_2\omega_3 \\ \left.\dfrac{d\mathbf H_{A,0}}{dt}\right|_0 \cdot \mathbf e_2 = I_2\alpha_2 - (I_3 - I_1)\,\omega_3\omega_1 \\ \left.\dfrac{d\mathbf H_{A,0}}{dt}\right|_0 \cdot \mathbf e_3 = I_3\alpha_3 - (I_1 - I_2)\,\omega_1\omega_2 \end{array}}$$
>
> **Units:** $[\mathrm{M\,L^2}]\,[\mathrm{T^{-2}}] = [\mathrm{M\,L^2\,T^{-2}}]$ in every term
> **Meaning:** these are Euler's equations in the principal axes of inertia; the cyclic order 1, 2, 3 of the indices reflects the right-handed basis.

> [!derivation] Euler's equations with the applied moment
> **Law:** rotational equation (A is G or a fixed body point) projected on the principal basis
> **Source:** [Lecture 10, Slide 13]; [Lecture 10, Slide 14]; Notes.pdf, Eq. 12.23
>
> $$\begin{aligned}
> \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\alpha_{B0} + \boldsymbol\omega_{B0} \times \left(\overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0}\right) &= \mathbf M_A \quad &\text{(Eq. 12.21 equal to the moment, Section 5.1)} \\
> \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\alpha_{B0} &= \mathbf M_A - \boldsymbol\omega_{B0} \times \left(\overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0}\right) \quad &\text{(Euler's equation in vector form, Lecture 10 Slide 13)} \\
> I_1\alpha_1 &= M_1 - \left(I_3 - I_2\right)\omega_2\omega_3 = M_1 + \left(I_2 - I_3\right)\omega_2\omega_3 \quad &\text{(component e1 of the previous box)}
> \end{aligned}$$
>
> $$\boxed{I_1\alpha_1 = M_1 + (I_2 - I_3)\,\omega_2\omega_3, \qquad I_2\alpha_2 = M_2 + (I_3 - I_1)\,\omega_3\omega_1, \qquad I_3\alpha_3 = M_3 + (I_1 - I_2)\,\omega_1\omega_2}$$
>
> **Units:** N m in every term
> **Meaning:** $M_i$ and $\omega_i$ are components in the body-fixed principal basis; the products of angular velocities couple the three rotations.

The notes add that the principal axes of an asymmetric body are laborious to find, and that the orientation of $B_B$ also affects how easily $\boldsymbol\omega_{B0}$ and $\boldsymbol\alpha_{B0}$ are written. The body-fixed basis is therefore chosen for overall convenience, and Eqs. 12.23 are used only when it is principal.

> [!example] Slides: clean and dirty rotations of a block
> Lecture 10 shows a rectangular block with centre of mass $G$ and principal axes $\mathbf e_1$, $\mathbf e_2$, $\mathbf e_3$, all principal moments different [Lecture 10, Slide 15] [Lecture 10, Slide 16]. In the clean rotation the angular velocity lies along a principal axis and the angular momentum about $G$ is parallel to it. In the dirty rotation the angular velocity has components on two principal axes and the angular momentum is no longer parallel to it. The boxes below derive both pictures from Euler's equations, taking moments about $G$.

> [!derivation] Clean rotation about a principal axis
> **Law:** Eq. 11.12 and Euler's equations with two components of omega equal to zero
> **Source:** [Lecture 10, Slide 14]; [Lecture 10, Slide 15]; Notes.pdf, Eq. 11.12
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0} &= \omega_3\,\mathbf e_3, \quad \omega_1 = \omega_2 = 0 \quad &\text{(rotation about the principal axis 3)} \\
> \mathbf H_{G,0} &= I_1 \cdot 0\,\mathbf e_1 + I_2 \cdot 0\,\mathbf e_2 + I_3\omega_3\,\mathbf e_3 = I_3\,\boldsymbol\omega_{B0} \quad &\text{(Eq. 11.12 in the principal basis)} \\
> \boldsymbol\omega_{B0} \times \mathbf H_{G,0} &= \omega_3\,\mathbf e_3 \times I_3\omega_3\,\mathbf e_3 = \mathbf 0 \quad &\text{(parallel vectors)} \\
> I_1\alpha_1 &= M_1, \quad I_2\alpha_2 = M_2, \quad I_3\alpha_3 = M_3 \quad &\text{(Euler's equations: every product of omegas contains a zero)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{G,0} \parallel \boldsymbol\omega_{B0}, \qquad \mathbf M_G = \mathbf 0 \;\Rightarrow\; \boldsymbol\alpha_{B0} = \mathbf 0}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-1}}]$ for the angular momentum; N m for the moments
> **Meaning:** the three equations are decoupled; without moment the block keeps spinning steadily about the same principal axis.

> [!derivation] Dirty rotation: angular velocity off the principal axes
> **Law:** Eq. 11.12 and Euler's equations with two non-zero components of omega
> **Source:** [Lecture 10, Slide 14]; [Lecture 10, Slide 16]; Notes.pdf, Eq. 11.12
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0} &= \omega_1\,\mathbf e_1 + \omega_3\,\mathbf e_3, \quad \omega_2 = 0 \quad &\text{(angular velocity in the plane of e1 and e3)} \\
> \mathbf H_{G,0} &= I_1\omega_1\,\mathbf e_1 + I_3\omega_3\,\mathbf e_3 \quad &\text{(Eq. 11.12 in the principal basis)} \\
> \boldsymbol\omega_{B0} \times \mathbf H_{G,0} &= \left(0 \cdot I_3\omega_3 - \omega_3 \cdot 0\right)\mathbf e_1 + \left(\omega_3 I_1\omega_1 - \omega_1 I_3\omega_3\right)\mathbf e_2 + \left(\omega_1 \cdot 0 - 0 \cdot I_1\omega_1\right)\mathbf e_3 = \left(\omega_3 I_1\omega_1 - \omega_1 I_3\omega_3\right)\mathbf e_2 \quad &\text{(cofactor expansion; only the e2 term survives)} \\
> &= \left(I_1 - I_3\right)\omega_1\omega_3\,\mathbf e_2 \neq \mathbf 0 \quad &\text{(different principal moments)} \\
> I_2\alpha_2 &= M_2 + \left(I_3 - I_1\right)\omega_3\omega_1 \quad &\text{(second Euler equation)} \\
> M_2 &= \left(I_1 - I_3\right)\omega_1\omega_3 \quad &\text{(moment needed to keep omega constant, alpha2 = 0)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{G,0} \nparallel \boldsymbol\omega_{B0}, \qquad \mathbf M_G = (I_1 - I_3)\,\omega_1\omega_3\,\mathbf e_2 \text{ to keep } \boldsymbol\omega_{B0} \text{ constant}}$$
>
> **Units:** $[\mathrm{M\,L^2}]\,[\mathrm{T^{-2}}] = [\mathrm{M\,L^2\,T^{-2}}]$, N m
> **Meaning:** the rotations about the principal axes are coupled; a body spun off its principal axes needs a moment (supplied by its bearings, for instance) just to keep its angular velocity constant.

## 7. Equilibrium of a rigid body

> [!derivation] Equilibrium conditions
> **Law:** Eqs. 12.8 and 12.13 with the body at rest for all times
> **Source:** Notes.pdf, Eq. 12.24; Notes.pdf, Eq. 12.25; [Lecture 10, Slide 19]
>
> $$\begin{aligned}
> \mathbf v_0^G &= \mathbf 0, \quad \boldsymbol\omega_{B0} = \mathbf 0 \quad \forall t \quad &\text{(a body at rest at t = 0 must remain at rest)} \\
> \mathbf a_0^G &= \mathbf 0, \quad \boldsymbol\alpha_{B0} = \mathbf 0 \quad &\text{(time derivatives of quantities that are zero for all t)} \\
> \mathbf F &= m\,\mathbf a_0^G = \mathbf 0 \quad &\text{(Eq. 12.8: Eq. 12.24)} \\
> \mathbf M_G &= \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\alpha_{B0} + \boldsymbol\omega_{B0} \times \left(\overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0}\right) = \mathbf 0 \quad &\text{(Eq. 12.21 about G)} \\
> \mathbf M_A &= \mathbf M_G + \mathbf F \times \overrightarrow{GA} = \mathbf 0 \quad &\text{(Eq. 12.15 with zero resultant: Eq. 12.25 at every point)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F = \mathbf 0, \qquad \mathbf M_A = \mathbf 0}$$
>
> **Units:** N and N m
> **Meaning:** a configuration is an equilibrium if and only if the resultant force and the resultant moment about one point vanish there; a body in equilibrium under a system of forces is also in equilibrium under any equivalent system.

The definition of stability carries over from the particle [Lecture 10, Slide 19]. Taking a body point $C$ and 3-1-3 Euler angles, the configuration with $C$ at $\mathbf r_0^*$ and angles $\psi_0$, $\theta_0$, $\varphi_0$ is stable when small perturbations stay small:

| Condition | Statement |
| :--- | :--- |
| for all tolerances | $\forall\,\varepsilon_r, \varepsilon_v, \varepsilon_a, \varepsilon_\omega \gt 0$ there exist $\delta_r, \delta_v, \delta_a, \delta_\omega \gt 0$ such that |
| initial perturbation | $\lvert\mathbf r_0^C - \mathbf r_0^*\rvert \lt \delta_r$, $\lvert\mathbf v_0^C\rvert \lt \delta_v$, $\lvert\psi - \psi_0\rvert, \lvert\theta - \theta_0\rvert, \lvert\varphi - \varphi_0\rvert \lt \delta_a$, $\lvert\boldsymbol\omega_{B0}\rvert \lt \delta_\omega$ |
| implies, for all $t \gt 0$ | $\lvert\mathbf r_0^C - \mathbf r_0^*\rvert \lt \varepsilon_r$, $\lvert\mathbf v_0^C\rvert \lt \varepsilon_v$, $\lvert\psi - \psi_0\rvert, \lvert\theta - \theta_0\rvert, \lvert\varphi - \varphi_0\rvert \lt \varepsilon_a$, $\lvert\boldsymbol\omega_{B0}\rvert \lt \varepsilon_\omega$ |

## 8. Work, power and conservation of mechanical energy

### 8.1 Power of a system of forces and torques

> [!derivation] Power of the external forces and torques
> **Law:** power of each force at its point of application (Eq. 4.10) plus the power of each torque
> **Source:** Notes.pdf, Eq. 12.26; Notes.pdf, Eq. 12.27; Notes.pdf, Eq. 12.28; Notes.pdf, Eq. 12.29; [Lecture 10, Slide 11]; [Lecture 10, Slide 12]
>
> $$\begin{aligned}
> \dot W_0 &= \sum_{i=1}^{N} \mathbf F^{P_i} \cdot \mathbf v_0^{P_i} + \sum_{k=1}^{M} \mathbf Q_k \cdot \boldsymbol\omega_{B0} \quad &\text{(internal forces do no work in a rigid body: Eq. 12.26)} \\
> \mathbf v_0^{P_i} &= \mathbf v_0^A + \boldsymbol\omega_{B0} \times \mathbf r_A^{P_i} \quad &\text{(velocity field from the body point A, Eq. 12.27)} \\
> \sum_{i} \mathbf F^{P_i} \cdot \mathbf v_0^{P_i} &= \sum_{i} \mathbf F^{P_i} \cdot \mathbf v_0^A + \sum_{i} \mathbf F^{P_i} \cdot \left(\boldsymbol\omega_{B0} \times \mathbf r_A^{P_i}\right) \quad &\text{(distributive property)} \\
> \mathbf F^{P_i} \cdot \left(\boldsymbol\omega_{B0} \times \mathbf r_A^{P_i}\right) &= \boldsymbol\omega_{B0} \cdot \left(\mathbf r_A^{P_i} \times \mathbf F^{P_i}\right) \quad &\text{(cyclic property of the scalar triple product)} \\
> \sum_{i} \mathbf F^{P_i} \cdot \mathbf v_0^{P_i} &= \left(\sum_i \mathbf F^{P_i}\right) \cdot \mathbf v_0^A + \left(\sum_i \mathbf r_A^{P_i} \times \mathbf F^{P_i}\right) \cdot \boldsymbol\omega_{B0} \quad &\text{(common factors out of the sums: Eq. 12.28)} \\
> \dot W_0 &= \mathbf F \cdot \mathbf v_0^A + \left(\sum_i \mathbf r_A^{P_i} \times \mathbf F^{P_i} + \sum_k \mathbf Q_k\right) \cdot \boldsymbol\omega_{B0} \quad &\text{(torque terms added)} \\
> &= \mathbf F \cdot \mathbf v_0^A + \mathbf M_A \cdot \boldsymbol\omega_{B0} \quad &\text{(Eq. 12.14: Eq. 12.29)}
> \end{aligned}$$
>
> $$\boxed{\dot W_0 = \mathbf F \cdot \mathbf v_0^A + \mathbf M_A \cdot \boldsymbol\omega_{B0}}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}]\,[\mathrm{L\,T^{-1}}] = [\mathrm{M\,L^2\,T^{-3}}]$ and $[\mathrm{M\,L^2\,T^{-2}}]\,[\mathrm{T^{-1}}] = [\mathrm{M\,L^2\,T^{-3}}]$, W
> **Meaning:** the power of a load system equals the power of its reduction at any body point $A$, so two equivalent systems do the same work [Lecture 10, Slide 11].

Two remarks of [Lecture 10, Slide 17]: an external force perpendicular to the velocity of its point of application (of any point on its line of action) does no work, and an external torque perpendicular to $\boldsymbol\omega_{B0}$ does no work.

### 8.2 Work and energy theorem

> [!derivation] Work and energy theorem for a rigid body
> **Law:** power as the rate of the kinetic energy (chain rule) integrated with Barrow's rule
> **Source:** Notes.pdf, Eq. 12.30; Notes.pdf, Eq. 12.31; Notes.pdf, Eq. 12.32; [Lecture 10, Slide 17]; [Lecture 10, Slide 18]
>
> $$\begin{aligned}
> \dot W_0 &= \sum_{i=1}^{N} m^{P_i}\left.\frac{d\mathbf v_0^{P_i}}{dt}\right|_0 \cdot \mathbf v_0^{P_i} \quad &\text{(second law for each particle, internal power zero)} \\
> &= \sum_{i=1}^{N} \frac{1}{2}m^{P_i}\,\frac{d\left(\mathbf v_0^{P_i} \cdot \mathbf v_0^{P_i}\right)}{dt} \quad &\text{(product rule: the derivative of v dot v is twice v dot its derivative)} \\
> &= \frac{d}{dt}\left[\sum_{i=1}^{N} \frac{1}{2}m^{P_i}\left(v_0^{P_i}\right)^2\right] = \frac{dT_0}{dt} \quad &\text{(constant masses; definition of T)} \\
> W_0(t_1, t_2) &= \int_{t_1}^{t_2} \dot W_0\,dt = \int_{t_1}^{t_2} \frac{dT_0}{dt}\,dt \quad &\text{(work as time integral of the power)} \\
> &= \Big[T_0\Big]_{t_1}^{t_2} = T_{0,2} - T_{0,1} \quad &\text{(antiderivative T, Barrow's rule: Eq. 12.30)} \\
> T_0 &= \frac{1}{2}\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0} \quad &\text{(A fixed body point, Eq. 11.32: Eq. 12.31)} \\
> T_0 &= \frac{1}{2}m\left(v_0^G\right)^2 + \frac{1}{2}\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0} \quad &\text{(always, Eq. 11.31: Eq. 12.32)}
> \end{aligned}$$
>
> $$\boxed{W_0(t_1, t_2) = \int_{t_1}^{t_2} \dot W_0\,dt = T_{0,2} - T_{0,1}}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-3}}]\,[\mathrm{T}] = [\mathrm{M\,L^2\,T^{-2}}]$, J
> **Meaning:** the work of all external forces and torques between two instants equals the change of the kinetic energy of the body.

> [!derivation] Conservation of mechanical energy
> **Law:** work of conservative loads as minus the change of a potential (Eq. 4.14)
> **Source:** Notes.pdf, Eq. 12.33; [Lecture 10, Slide 18]
>
> $$\begin{aligned}
> W_0(t_1, t_2) &= V_{0,1} - V_{0,2} \quad &\text{(all loads that do work derive from a potential)} \\
> T_{0,2} - T_{0,1} &= V_{0,1} - V_{0,2} \quad &\text{(Eq. 12.30)} \\
> T_{0,2} + V_{0,2} &= T_{0,1} + V_{0,1} \quad &\text{(terms of each instant on one side)}
> \end{aligned}$$
>
> $$\boxed{T_0 + V_0 = T_{0,2} + V_{0,2} = T_{0,1} + V_{0,1} = E_0}$$
>
> **Units:** J in every term
> **Meaning:** the mechanical energy is conserved when every force or torque that does work is conservative; non-conservative forces may act if they are always perpendicular to the velocity of their point, and non-conservative torques if they are always perpendicular to the angular velocity.

> [!derivation] Potential energy of the weight of a rigid body
> **Law:** potential of the weight of each element (Eq. 4.14) summed over the body; definition of the centre of mass
> **Source:** Notes.pdf, Eq. 12.34; Notes.pdf, Eq. 4.14; [Lecture 10, Slide 18]
>
> $$\begin{aligned}
> d\mathbf F_g &= -g\,\mathbf k_0\,dm \quad &\text{(weight of an element, k0 vertical upwards)} \\
> dV_0 &= -\int \left(-g\,\mathbf k_0\,dm\right) \cdot d\mathbf r_0^P = g\,dm \int dz_0^P = g\,z_0^P\,dm \quad &\text{(Notes Eq. 4.14; reference at zero height)} \\
> V_0 &= \int_{\mathcal D} g\,z_0^P\,dm = g\int_{\mathcal D} z_0^P\,dm \quad &\text{(sum over the elements, g uniform)} \\
> &= g\,m\,z_0^G \quad &\text{(vertical component of Notes Eq. 10.8)}
> \end{aligned}$$
>
> $$\boxed{V_0 = m\,g\,z_0^G}$$
>
> **Units:** $[\mathrm{M}]\,[\mathrm{L\,T^{-2}}]\,[\mathrm{L}] = [\mathrm{M\,L^2\,T^{-2}}]$, J
> **Meaning:** the weight is conservative and its potential is that of the whole mass at the height of $G$; as the slides warn, such potentials are integrals over the body.

### 8.3 Translational and rotational work

> [!derivation] Work of the resultant force and translational energy
> **Law:** Eq. 12.8 dotted with the velocity of G; chain rule; Barrow's rule
> **Source:** Notes.pdf, Eq. 12.35; Notes.pdf, Eq. 12.8
>
> $$\begin{aligned}
> \mathbf F \cdot \mathbf v_0^G &= m\,\mathbf a_0^G \cdot \mathbf v_0^G = m\left.\frac{d\mathbf v_0^G}{dt}\right|_0 \cdot \mathbf v_0^G \quad &\text{(Eq. 12.8)} \\
> &= \frac{d}{dt}\left[\frac{1}{2}m\left(v_0^G\right)^2\right] \quad &\text{(product rule on v dot v)} \\
> \int_{t_1}^{t_2} \mathbf F \cdot \mathbf v_0^G\,dt &= \Big[\tfrac{1}{2}m\left(v_0^G\right)^2\Big]_{t_1}^{t_2} \quad &\text{(antiderivative, Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\int_{t_1}^{t_2} \mathbf F \cdot \mathbf v_0^G\,dt = \frac{1}{2}m\left(v_0^G\right)^2\Big|_2 - \frac{1}{2}m\left(v_0^G\right)^2\Big|_1}$$
>
> **Units:** J on both sides
> **Meaning:** the resultant force, applied at $G$, changes only the translational part of the kinetic energy (first term of Eq. 12.32).

> [!derivation] Work of the moment about G and rotational energy
> **Law:** power reduced at G (Eq. 12.29), energy theorem (Eq. 12.30) and the previous box
> **Source:** Notes.pdf, Eq. 12.36; Notes.pdf, Eq. 12.29; Notes.pdf, Eq. 12.32
>
> $$\begin{aligned}
> \frac{dT_0}{dt} &= \mathbf F \cdot \mathbf v_0^G + \mathbf M_G \cdot \boldsymbol\omega_{B0} \quad &\text{(Eq. 12.29 with A = G, and dT/dt equal to the power)} \\
> \frac{d}{dt}\left[\frac{1}{2}m\left(v_0^G\right)^2\right] + \frac{d}{dt}\left[\frac{1}{2}\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0}\right] &= \mathbf F \cdot \mathbf v_0^G + \mathbf M_G \cdot \boldsymbol\omega_{B0} \quad &\text{(Eq. 12.32 differentiated)} \\
> \frac{d}{dt}\left[\frac{1}{2}\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0}\right] &= \mathbf M_G \cdot \boldsymbol\omega_{B0} \quad &\text{(the translational terms are equal, previous box)} \\
> \int_{t_1}^{t_2} \mathbf M_G \cdot \boldsymbol\omega_{B0}\,dt &= \Big[\tfrac{1}{2}\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0}\Big]_{t_1}^{t_2} \quad &\text{(antiderivative, Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\int_{t_1}^{t_2} \mathbf M_G \cdot \boldsymbol\omega_{B0}\,dt = \frac{1}{2}\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0}\Big|_2 - \frac{1}{2}\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0}\Big|_1}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]\,[\mathrm{T^{-1}}]\,[\mathrm{T}] = [\mathrm{M\,L^2\,T^{-2}}]$, J
> **Meaning:** the moment about $G$ changes only the rotational kinetic energy (second term of Eq. 12.32): translation and rotation can be treated separately.

## 9. Planar dynamics of a rigid body

> [!info] Extension: plane motion
> The notes and the slides treat the general three-dimensional motion only. The particular cases below (translation, rotation about a fixed axis and general plane motion) are obtained from Eqs. 12.8, 12.13 and 12.21 and are marked as an extension; they introduce no new law.

In a plane motion every point of the body moves parallel to the fixed plane spanned by $\mathbf i_0$ and $\mathbf j_0$, and $\mathbf k_0$ points out of the paper (⊙) in the figures. The body frame $S_1\{G; \mathbf i_1, \mathbf j_1, \mathbf k_1\}$ keeps $\mathbf k_1$ along $\mathbf k_0$ and turns by the angle $\theta$ measured from $\mathbf i_0$ to $\mathbf i_1$, counterclockwise about $\mathbf k_0$.

| Symbol | Meaning |
| :--- | :--- |
| $\theta$ | angle from $\mathbf i_0$ to $\mathbf i_1$, positive counterclockwise about $\mathbf k_0$ (right-hand rule, ⊙) |
| $\omega$, $\alpha$ | scalar angular velocity and angular acceleration about $\mathbf k_0$ (rad/s, rad/s$^2$) |
| $I_{13}$, $I_{23}$, $I_{33}$ | components of the third column of the matrix of the tensor of inertia about $G$ in $B_1$ (kg m$^2$) |
| $\rho$, $\mathbf e_t$, $\mathbf e_n$ | radius of curvature and intrinsic unit vectors of the path of $G$ (Notes Eq. 2.17) |

![[attachments/EM-T/t7-planar-motion.svg]]

> [!derivation] Basis change and angular velocity of a plane motion (extension)
> **Law:** rotation about the axis k0; right-hand rule; Poisson derivative of the unit vectors
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 3.9
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0 \quad &\text{(right triangle: hypotenuse 1, adjacent leg on i0 is cos, opposite leg on j0 is sin)} \\
> \mathbf j_1 &= -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0 \quad &\text{(i1 turned 90 degrees counterclockwise about k0 out of the paper: its i0 component is negative)} \\
> \left[{}_0 R_1\right] &= \left[\mathbf i_1 \mid \mathbf j_1 \mid \mathbf k_1\right]_{B_0}, \quad R_{11} = R_{22} = \cos\theta,\ R_{21} = -R_{12} = \sin\theta,\ R_{33} = 1,\ \text{others } 0 \quad &\text{(columns: components of i1, j1, k1 in B0, Notes Eq. 9.16 with psi = theta)} \\
> \det\left[{}_0 R_1\right] &= \cos^2\theta + \sin^2\theta = 1 \quad &\text{(expansion along the third row)} \\
> \left(R R^T\right)_{11} &= \cos^2\theta + \sin^2\theta = 1, \quad \left(R R^T\right)_{12} = \cos\theta\sin\theta - \sin\theta\cos\theta = 0, \quad \left(R R^T\right)_{22} = \sin^2\theta + \cos^2\theta = 1 \quad &\text{(orthogonality check, row times row; third row and column trivial: R R transposed is the identity)} \\
> \boldsymbol\omega_{B0} &= \dot\theta\,\mathbf k_0 = \omega\,\mathbf k_0 \quad &\text{(single rotation about k0)} \\
> \boldsymbol\alpha_{B0} &= \left.\frac{d}{dt}\left(\omega\,\mathbf k_0\right)\right|_0 = \dot\omega\,\mathbf k_0 + \omega \cdot \mathbf 0 = \alpha\,\mathbf k_0 \quad &\text{(product rule; k0 is fixed in S0)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{B0} = \dot\theta\,\mathbf k_0, \qquad \boldsymbol\alpha_{B0} = \ddot\theta\,\mathbf k_0}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ and $[\mathrm{T^{-2}}]$; the matrix is dimensionless
> **Meaning:** in a plane motion the angular velocity and the angular acceleration are always normal to the plane of motion.

> [!derivation] Moment equation about G in a plane motion (extension)
> **Law:** Eq. 12.21 about G with omega and alpha along the body axis k1
> **Source:** Notes.pdf, Eq. 12.21; Notes.pdf, Eq. 12.16
>
> $$\begin{aligned}
> \overline{\overline{\mathcal I}}_G \cdot \mathbf k_1 &= I_{13}\,\mathbf i_1 + I_{23}\,\mathbf j_1 + I_{33}\,\mathbf k_1 \quad &\text{(third column of the matrix in B1)} \\
> \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\alpha_{B0} &= \alpha\left(I_{13}\,\mathbf i_1 + I_{23}\,\mathbf j_1 + I_{33}\,\mathbf k_1\right) \quad &\text{(alpha along k1)} \\
> \boldsymbol\omega_{B0} \times \left(\overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0}\right) &= \omega\,\mathbf k_1 \times \omega\left(I_{13}\,\mathbf i_1 + I_{23}\,\mathbf j_1 + I_{33}\,\mathbf k_1\right) = \omega^2\left(I_{13}\,\mathbf j_1 - I_{23}\,\mathbf i_1\right) \quad &\text{(k1 cross i1 is j1, k1 cross j1 is minus i1)} \\
> \mathbf M_G &= \left(I_{13}\,\alpha - I_{23}\,\omega^2\right)\mathbf i_1 + \left(I_{23}\,\alpha + I_{13}\,\omega^2\right)\mathbf j_1 + I_{33}\,\alpha\,\mathbf k_1 \quad &\text{(Eq. 12.21 equal to the moment about G)} \\
> I_{13} &= I_{23} = 0 \quad &\text{(if the plane of motion through G is a plane of symmetry)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M_G \cdot \mathbf k_0 = I_{33}\,\alpha, \qquad \mathbf F = m\,\mathbf a_0^G}$$
>
> **Units:** N m and N
> **Meaning:** only the component normal to the plane governs the rotation; the in-plane components of the moment are those the supports must provide when the body is not symmetric about the plane.

> [!derivation] Particular plane motions (extension)
> **Law:** Eqs. 12.8, 12.13 and the acceleration field (Eq. 9.4) in each case
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 9.4; Notes.pdf, Eq. 2.17
>
> $$\begin{aligned}
> \omega &= 0, \quad \mathbf a_0^G = \ddot s\,\mathbf e_t \quad &\text{(rectilinear translation: the path of G is a straight line)} \\
> \mathbf F &= m\,\ddot s\,\mathbf e_t, \quad \mathbf M_G = \mathbf 0 \quad &\text{(Eq. 12.8; Eq. 12.21 with zero omega and alpha)} \\
> \mathbf a_0^G &= \ddot s\,\mathbf e_t + \frac{\dot s^2}{\rho}\,\mathbf e_n \quad &\text{(curvilinear translation: intrinsic acceleration, Notes Eq. 2.17)} \\
> \mathbf F &= m\,\ddot s\,\mathbf e_t + m\,\frac{\dot s^2}{\rho}\,\mathbf e_n, \quad \mathbf M_G = \mathbf 0 \quad &\text{(same equations, every point has the same path shape)} \\
> \mathbf a_0^G &= \alpha\,\mathbf k_0 \times \mathbf r_O^G + \omega\,\mathbf k_0 \times \left(\omega\,\mathbf k_0 \times \mathbf r_O^G\right) = \alpha\,\mathbf k_0 \times \mathbf r_O^G - \omega^2\,\mathbf r_O^G \quad &\text{(rotation about a fixed axis through O: Eq. 9.4 from O, r in the plane)} \\
> \mathbf M_O \cdot \mathbf k_0 &= I_{O,33}\,\alpha \quad &\text{(Eq. 12.13 about the fixed body point O, as the previous box)} \\
> \mathbf F &= m\,\mathbf a_0^G, \quad \mathbf M_G \cdot \mathbf k_0 = I_{33}\,\alpha \quad &\text{(general plane motion: three scalar equations)}
> \end{aligned}$$
>
> $$\boxed{\text{translation: } \mathbf F = m\,\mathbf a_0^G,\ \mathbf M_G = \mathbf 0; \quad \text{fixed axis: } \mathbf M_O \cdot \mathbf k_0 = I_{O,33}\,\alpha; \quad \text{general: } \mathbf F = m\,\mathbf a_0^G,\ \mathbf M_G \cdot \mathbf k_0 = I_{33}\,\alpha}$$
>
> **Units:** N and N m
> **Meaning:** a body in translation needs no moment about $G$; a body turning about a fixed axis is governed by one scalar equation about that axis, and the reactions there follow from the force equation.

> [!example] Extension example: compound pendulum
> A slender uniform rod $OA$ of length $L$ and mass $m$ turns in a vertical plane about a frictionless pin at its end $O$, under its own weight. In $S_0$ the unit vector $\mathbf i_0$ points vertically down, $\mathbf j_0$ horizontally to the right, and $\mathbf k_0$ out of the paper (⊙). The body frame $S_1$ has $\mathbf i_1$ along the rod from $O$ to $A$, and $\theta$ is the angle from $\mathbf i_0$ to $\mathbf i_1$. The example is not in the slides; it applies the rotation about a fixed axis, the reaction at the pin and the energy equation of this topic. The figure shows the deduction of the position of $G$ and the free-body diagram.

![[attachments/EM-T/t7-compound-pendulum.svg]]

> [!derivation] Kinematics of the rod
> **Law:** position vector of G and Poisson derivatives of the body basis
> **Source:** Notes.pdf, Eq. 3.8; Notes.pdf, Eq. 9.4
>
> $$\begin{aligned}
> \mathbf r_O^G &= \frac{L}{2}\,\mathbf i_1 = \frac{L}{2}\left(\cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0\right) \quad &\text{(G at mid-length; right triangle with hypotenuse L/2, vertical leg cos, horizontal leg sin)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \dot\theta\,\mathbf k_0 \times \mathbf i_1 = \dot\theta\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \dot\theta\,\mathbf k_0 \times \mathbf j_1 = -\dot\theta\,\mathbf i_1 \quad &\text{(Notes Eq. 3.8 with constant components in S1)} \\
> \mathbf v_0^G &= \frac{L}{2}\,\dot\theta\,\mathbf j_1 \quad &\text{(derivative of the position, L constant)} \\
> \mathbf a_0^G &= \frac{L}{2}\,\ddot\theta\,\mathbf j_1 + \frac{L}{2}\,\dot\theta\left(-\dot\theta\,\mathbf i_1\right) = \frac{L}{2}\,\ddot\theta\,\mathbf j_1 - \frac{L}{2}\,\dot\theta^2\,\mathbf i_1 \quad &\text{(product rule on theta dot times j1)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^G = \frac{L}{2}\,\dot\theta\,\mathbf j_1, \qquad \mathbf a_0^G = -\frac{L}{2}\,\dot\theta^2\,\mathbf i_1 + \frac{L}{2}\,\ddot\theta\,\mathbf j_1}$$
>
> **Units:** $[\mathrm{L}]\,[\mathrm{T^{-1}}]$ and $[\mathrm{L}]\,[\mathrm{T^{-2}}]$
> **Meaning:** $G$ moves on a circle of radius $L/2$: tangential acceleration along $\mathbf j_1$, centripetal acceleration towards $O$.

> [!derivation] Moment of inertia of the rod about the pin
> **Law:** moment of inertia as the integral of the squared distance (Eq. 10.11) for a slender rod
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.38
>
> $$\begin{aligned}
> dm &= \lambda\,dx_1, \quad \lambda = \frac{m}{L} \quad &\text{(uniform linear density; element of length dx1 at distance x1 from O)} \\
> I_{O,33} &= \int_{\mathcal D} \left(x_1^2 + y_1^2\right) dm = \int_0^L x_1^2\,\lambda\,dx_1 \quad &\text{(slender rod: y1 and z1 are zero on it)} \\
> &= \lambda\left[\frac{x_1^3}{3}\right]_0^L = \lambda\left(\frac{L^3}{3} - 0\right) \quad &\text{(antiderivative of x squared, Barrow's rule)} \\
> &= \frac{m}{L}\,\frac{L^3}{3} = \frac{1}{3}m L^2 \quad &\text{(substitution of lambda)} \\
> I_{O,13} &= -\int_{\mathcal D} x_1 z_1\,dm = 0, \quad I_{O,23} = -\int_{\mathcal D} y_1 z_1\,dm = 0 \quad &\text{(products of inertia with z1 vanish, Notes Eq. 10.38)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{O,0} = \overline{\overline{\mathcal I}}_O \cdot \boldsymbol\omega_{B0} = \frac{1}{3}m L^2\,\dot\theta\,\mathbf k_1}$$
>
> **Units:** $[\mathrm{M}]\,[\mathrm{L^2}]\,[\mathrm{T^{-1}}] = [\mathrm{M\,L^2\,T^{-1}}]$
> **Meaning:** $O$ is a fixed body point, so Eq. 11.13 applies, and the angular momentum is parallel to the angular velocity.

> [!derivation] Equation of motion from the moment about the pin
> **Law:** Eq. 12.13 about the fixed body point O; weight reduced at G
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 12.15
>
> $$\begin{aligned}
> \mathbf i_0 &= \cos\theta\,\mathbf i_1 - \sin\theta\,\mathbf j_1 \quad &\text{(first row of the transpose of the rotation matrix)} \\
> \mathbf M_O &= \mathbf r_O^G \times m g\,\mathbf i_0 + \mathbf r_O^O \times \mathbf R = \frac{L}{2}\,\mathbf i_1 \times m g\left(\cos\theta\,\mathbf i_1 - \sin\theta\,\mathbf j_1\right) + \mathbf 0 \quad &\text{(weight at G; the pin reaction has no arm)} \\
> &= -\frac{L}{2}\,m g\sin\theta\,\mathbf k_1 \quad &\text{(i1 cross i1 is zero, i1 cross j1 is k1)} \\
> \left.\frac{d\mathbf H_{O,0}}{dt}\right|_0 &= \frac{1}{3}m L^2\,\ddot\theta\,\mathbf k_1 + \frac{1}{3}m L^2\,\dot\theta \cdot \mathbf 0 \quad &\text{(product rule; k1 is fixed in S0)} \\
> \frac{1}{3}m L^2\,\ddot\theta &= -\frac{L}{2}\,m g\sin\theta \quad &\text{(component k1 of Eq. 12.13)}
> \end{aligned}$$
>
> $$\boxed{\ddot\theta + \frac{3g}{2L}\sin\theta = 0}$$
>
> **Units:** $[\mathrm{T^{-2}}]$ and $[\mathrm{L\,T^{-2}}]/[\mathrm{L}] = [\mathrm{T^{-2}}]$
> **Meaning:** for small angles the rod oscillates with angular frequency the square root of three g over two L, like a simple pendulum (Notes Eq. 4.38) of length two thirds of $L$.

> [!derivation] Reaction at the pin
> **Law:** Eq. 12.8 projected on the body basis B1
> **Source:** Notes.pdf, Eq. 12.8
>
> $$\begin{aligned}
> \mathbf R + m g\,\mathbf i_0 &= m\,\mathbf a_0^G \quad &\text{(resultant force: pin reaction and weight)} \\
> R_1 + m g\cos\theta &= -m\,\frac{L}{2}\,\dot\theta^2 \quad &\text{(component i1)} \\
> R_2 - m g\sin\theta &= m\,\frac{L}{2}\,\ddot\theta = m\,\frac{L}{2}\left(-\frac{3g}{2L}\sin\theta\right) \quad &\text{(component j1, equation of motion substituted)} \\
> R_2 &= m g\sin\theta - \frac{3}{4}m g\sin\theta = \frac{1}{4}m g\sin\theta \quad &\text{(solved for R2)}
> \end{aligned}$$
>
> $$\boxed{\mathbf R = -m\left(g\cos\theta + \frac{L}{2}\,\dot\theta^2\right)\mathbf i_1 + \frac{1}{4}m g\sin\theta\,\mathbf j_1}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}]$ in each term, N
> **Meaning:** at the lowest point the pin pulls up with the weight plus the centripetal force; the reaction never enters the moment equation about $O$.

> [!derivation] Energy check of the compound pendulum
> **Law:** Eqs. 12.31, 12.34 and 12.33
> **Source:** Notes.pdf, Eq. 12.31; Notes.pdf, Eq. 12.34; Notes.pdf, Eq. 12.33
>
> $$\begin{aligned}
> T_0 &= \frac{1}{2}\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_O \cdot \boldsymbol\omega_{B0} = \frac{1}{2}\,\frac{1}{3}m L^2\,\dot\theta^2 \quad &\text{(Eq. 12.31 about the fixed point O)} \\
> V_0 &= m g\left(-\frac{L}{2}\cos\theta\right) \quad &\text{(Eq. 12.34: G is L/2 cos theta below O)} \\
> \frac{d}{dt}\left(T_0 + V_0\right) &= \frac{1}{3}m L^2\,\dot\theta\,\ddot\theta + m g\,\frac{L}{2}\sin\theta\,\dot\theta \quad &\text{(chain rule on theta dot squared and on cos theta)} \\
> &= \frac{1}{3}m L^2\,\dot\theta\left(\ddot\theta + \frac{3g}{2L}\sin\theta\right) = 0 \quad &\text{(equation of motion)}
> \end{aligned}$$
>
> $$\boxed{\frac{1}{6}m L^2\,\dot\theta^2 - \frac{1}{2}m g L\cos\theta = E_0}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]$, J, in both terms
> **Meaning:** the pin reaction does no work (its point does not move) and the weight is conservative, so the energy integral is consistent with the equation of motion.

## 10. Practical formulary

| Quantity | Result | Source |
| :--- | :--- | :--- |
| Linear momentum | $\mathbf p_0 = \int_{\mathcal D} \mathbf v_0^P\,dm = m\,\mathbf v_0^G$ | Eqs. 11.1, 11.3 |
| Angular momentum about $A$ | $\mathbf H_{A,0} = \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0} + m\,\mathbf r_A^G \times \mathbf v_0^{A(B)}$ | Eq. 11.11 |
| About $G$ or a fixed body point | $\mathbf H_{G,0} = \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0}$, $\mathbf H_{A,0} = \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0}$ | Eqs. 11.12, 11.13 |
| Change of pole | $\mathbf H_{A,0} = \mathbf H_{G,0} + m\,\mathbf r_A^G \times \mathbf v_0^G$, $\mathbf H_{G,G} \equiv \mathbf H_{G,0}$ | Eqs. 11.19, 11.20, 11.21 |
| Kinetic energy | $T_0 = \tfrac12\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0} + \tfrac12 m (v_0^{A(B)})^2 + m(\boldsymbol\omega_{B0} \times \mathbf r_A^G) \cdot \mathbf v_0^{A(B)}$ | Eq. 11.30 |
| About $G$; fixed point | $T_0 = \tfrac12\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0} + \tfrac12 m (v_0^G)^2$; $T_0 = \tfrac12\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0}$ | Eqs. 11.31, 11.32 |
| Koenig | $T_0 = T_G + \tfrac12 m (v_0^G)^2$ | Eq. 11.37 |
| Axis of rotation (extension) | $T_0 = \tfrac12 I_\ell\,\omega^2$, $I_\ell = \mathbf e_\omega \cdot \overline{\overline{\mathcal I}}_A \cdot \mathbf e_\omega = I_{\ell G} + m d^2$ | Eqs. 10.39, 10.48 |
| Force equation | $\left.\dfrac{d\mathbf p_0}{dt}\right\vert_0 = \mathbf F = m\,\mathbf a_0^G$ | Eq. 12.8 |
| Moment equation | $\left.\dfrac{d\mathbf H_{A,0}}{dt}\right\vert_0 = \mathbf M_A - m\,\mathbf v_0^A \times \mathbf v_0^G$ | Eq. 12.13 |
| Resultant moment with torques | $\mathbf M_A = \sum_i \mathbf r_A^{P_i} \times \mathbf F^{P_i} + \sum_k \mathbf Q_k$ | Eq. 12.14 |
| Change of reduction point | $\mathbf M_B = \mathbf M_A + \mathbf F \times \overrightarrow{AB}$; $\mathbf M_G = \mathbf M_C - \overrightarrow{CG} \times \mathbf F$ | Eqs. 12.15, 12.16 |
| Weight (extension) | $\{m\,\mathbf g; \mathbf 0\}$ at $G$ | Eq. 10.44 |
| Rotational equation in $S_B$ | $\left.\dfrac{d\mathbf H_{A,0}}{dt}\right\vert_0 = \overline{\overline{\mathcal I}}_A \cdot \boldsymbol\alpha_{B0} + \boldsymbol\omega_{B0} \times (\overline{\overline{\mathcal I}}_A \cdot \boldsymbol\omega_{B0})$ | Eq. 12.21 |
| Euler's equations | $I_1\alpha_1 - (I_2 - I_3)\omega_2\omega_3 = M_1$ and cyclic | Eq. 12.23 |
| Equilibrium | $\mathbf F = \mathbf 0$, $\mathbf M_A = \mathbf 0$ | Eqs. 12.24, 12.25 |
| Power | $\dot W_0 = \mathbf F \cdot \mathbf v_0^A + \mathbf M_A \cdot \boldsymbol\omega_{B0}$ | Eq. 12.29 |
| Work and energy | $W_0(t_1, t_2) = T_{0,2} - T_{0,1}$; $T_0 + V_0 = E_0$ | Eqs. 12.30, 12.33 |
| Weight potential | $V_0 = m g z_0^G$ | Eq. 12.34 |
| Split of the work | $\int \mathbf F \cdot \mathbf v_0^G\,dt = \Delta(\tfrac12 m (v_0^G)^2)$; $\int \mathbf M_G \cdot \boldsymbol\omega_{B0}\,dt = \Delta(\tfrac12\boldsymbol\omega_{B0} \cdot \overline{\overline{\mathcal I}}_G \cdot \boldsymbol\omega_{B0})$ | Eqs. 12.35, 12.36 |
| Plane motion (extension) | $\mathbf F = m\,\mathbf a_0^G$, $\mathbf M_G \cdot \mathbf k_0 = I_{33}\,\alpha$; fixed axis $\mathbf M_O \cdot \mathbf k_0 = I_{O,33}\,\alpha$ | Eqs. 12.8, 12.21 |

**Back to:** [[Engineering Mechanics MOC]]
