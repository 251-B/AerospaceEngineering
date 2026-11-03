---
materia: Fluid Mechanics
tema: "Topic 5: Hydrostatics"
tags:
  - problema-examen
  - hidrostatica
  - superficie-inclinada
  - momentos
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-05-hydrostatics/problemas/fluid_statics_7.pdf"
id: "fs7"
pill: "FS7: Wedge on its vertex"
sheets:
  - 7
tags_html:
  - "Inclined surfaces"
  - "Two liquids"
  - "Force and moment"
  - "Virtual column"
---

# Problem FS7: Wedge between Two Liquids

> Official hydrostatics sheet of the course, statement translated from the Spanish original. Part of [[Topic 5 - Hydrostatics]].
> Method: force and moment of the pressure on each inclined face by direct integration (Notes.pdf, Eq. 5.11), with the element, its normal and its arm deduced from the right triangle of the face; checked with the projection rule (Eq. 5.14).

## Statement

A two-dimensional wedge of angle $2\alpha$ and weight $W$ per unit length rests on its lower vertex in the position shown in the figure. The wedge separates two liquids of densities $\rho_1$ and $\rho_2 > \rho_1$. The levels of the two liquids are $h_1$ and $h_2$ respectively. Find:

1. The reaction force exerted on the wedge at the support point $O$.

2. The relation that must hold between $h_1$ and $h_2$ for the equilibrium position shown in the figure to be possible.

Translated from the Spanish original.

![[attachments/FM-T5/fs7-statement.svg]]
*Statement figure (redrawn from fluid_statics_7.pdf, p. 1): wedge of angle $2\alpha$ and weight $W$ per unit length resting on its vertex $O$; liquid $\rho_1$ of depth $h_1$ on the left and $\rho_2 > \rho_1$ of depth $h_2$ on the right*

Source: fluid_statics_7.pdf (pages 1-2, sheet of 05-09-07, problem P5). Notes.pdf, Chapter 5: Eqs. 5.10, 5.11 and 5.14.

## Hypotheses, Data and Unknowns

- Both liquids at rest, incompressible; air at $p_a$ above them and on the top face of the wedge, so the $p_a$ contributions cancel over the closed surface and only gauge pressures count.
- Planar problem: forces and moments per unit length normal to the paper.
- The wedge is symmetric about the vertical through $O$, each face making the angle $\alpha$ with that vertical; its centre of gravity lies on that vertical, so $W$ has no moment about $O$.
- At $O$ the wedge rests on the floor; the reaction $\vec{R} = R_x\vec{e}_x + R_y\vec{e}_y$ acts at $O$ (no moment at a point support).
- Data: $\alpha$, $W$, $\rho_1$, $\rho_2$, $h_1$, $h_2$, $g$. Unknowns: $R_x$, $R_y$ and the relation between $h_1$ and $h_2$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $\alpha$ | half-angle of the wedge | rad |
| $W$ | weight per unit length | N/m |
| $h_1$, $h_2$ | liquid levels above $O$ | m |
| $R_x$, $R_y$ | reaction at $O$ per unit length | N/m |

## Coordinates, Element and Normal of Each Face

Origin at the vertex $O$, $x$ horizontal to the right, $y$ vertical and up. A point of the left face at the height $y$ is at $x = -y\tan\alpha$: in the right triangle with the vertical leg $y$ (adjacent to $\alpha$) and the horizontal leg (opposite), the horizontal leg is $y\tan\alpha$, and the hypotenuse, the distance from $O$ along the face, is $l = y/\cos\alpha$.

The element of the face between $y$ and $y + dy$ is the hypotenuse of the small right triangle with the legs $dy$ and $dy\tan\alpha$, so $dl = dy/\cos\alpha$.

The face makes the angle $\alpha$ with the vertical, so its unit normal makes the angle $\alpha$ with the horizontal. Liquid 1 is on the left and below the face, so the normal towards liquid 1 is

$$ \vec{n}_1 = -\cos\alpha\,\vec{e}_x - \sin\alpha\,\vec{e}_y, \qquad \vec{n}_2 = \cos\alpha\,\vec{e}_x - \sin\alpha\,\vec{e}_y $$

($\vec{n}_2$ by mirror symmetry for the right face). Check: $\vec{n}_1$ is perpendicular to the face direction $(-\sin\alpha, \cos\alpha)$, since $\sin\alpha\cos\alpha - \sin\alpha\cos\alpha = 0$.

![[attachments/FM-T5/fs7-geometry.svg]]
*Left face of the wedge, making the angle $\alpha$ with the vertical. The element $dl$ is the hypotenuse of the right triangle with the vertical leg $dy$ (adjacent to $\alpha$) and the horizontal leg $dy\tan\alpha$ (opposite), so $dl = dy/\cos\alpha$; for the same reason the distance from $O$ along the face is $l = y/\cos\alpha$. The unit normal towards liquid 1 is $\vec{n}_1 = -\cos\alpha\,\vec{e}_x - \sin\alpha\,\vec{e}_y$ and the force on the wedge is $-p\vec{n}_1\,dl$*

By (5.10), the gauge pressures are $p_1 - p_a = \rho_1 g (h_1 - y)$ for $0 \leq y \leq h_1$ and $p_2 - p_a = \rho_2 g (h_2 - y)$ for $0 \leq y \leq h_2$.

## Forces on the Faces

On the left face, $d\vec{F}_1 = -(p_1 - p_a)\vec{n}_1\,dl = \rho_1 g (h_1 - y)(\cos\alpha\,\vec{e}_x + \sin\alpha\,\vec{e}_y)\,\dfrac{dy}{\cos\alpha}$, so

$$ \vec{F}_1 = \rho_1 g\,(\vec{e}_x + \tan\alpha\,\vec{e}_y)\int_0^{h_1}(h_1 - y)\,dy = \rho_1 g\,(\vec{e}_x + \tan\alpha\,\vec{e}_y)\left[h_1 y - \frac{y^2}{2}\right]_0^{h_1} = \frac{\rho_1 g h_1^2}{2}\,(\vec{e}_x + \tan\alpha\,\vec{e}_y) $$

and in the same way on the right face, with $-\vec{n}_2 = -\cos\alpha\,\vec{e}_x + \sin\alpha\,\vec{e}_y$:

$$ \vec{F}_2 = \frac{\rho_2 g h_2^2}{2}\,(-\vec{e}_x + \tan\alpha\,\vec{e}_y) $$

**Check with the projection rule (5.14).** The horizontal component of $\vec{F}_1$ is the force on the vertical projection of the face, a rectangle of height $h_1$ and unit width: $\rho_1 g h_1^2/2$. The vertical component is upward and equals the weight of the **virtual** column of liquid 1 above the face, the triangle with the vertical side $h_1$ and the horizontal side $h_1\tan\alpha$: $\rho_1 g\cdot\tfrac{1}{2}h_1\cdot h_1\tan\alpha$. Both agree.

## 1. The Reaction at O

![[attachments/FM-T5/fs7-fbd.svg]]
*Free-body diagram of the wedge (per unit length): $F_1$ and $F_2$ normal to the faces, applied at the centres of pressure, at the distances $h_1/(3\cos\alpha)$ and $h_2/(3\cos\alpha)$ from $O$ along the faces; the weight $W$ on the symmetry line through $O$; the reaction $R$ at $O$*

Force balance of the wedge, $\vec{F}_1 + \vec{F}_2 - W\vec{e}_y + \vec{R} = 0$, component by component:

$$ R_x = -\frac{\rho_1 g h_1^2}{2} + \frac{\rho_2 g h_2^2}{2}, \qquad R_y = W - \frac{\rho_1 g h_1^2}{2}\tan\alpha - \frac{\rho_2 g h_2^2}{2}\tan\alpha $$

## 2. The Moment about O and the Condition on the Levels

Every $d\vec{F}_1$ is normal to the face, so its arm about $O$ is the distance along the face, $l = y/\cos\alpha$, and it turns the wedge clockwise (towards liquid 2). Its moment is

$$ M_1 = \int_0^{h_1}(p_1 - p_a)\,l\,dl = \int_0^{h_1}\rho_1 g (h_1 - y)\,\frac{y}{\cos\alpha}\,\frac{dy}{\cos\alpha} = \frac{\rho_1 g}{\cos^2\alpha}\left[\frac{h_1 y^2}{2} - \frac{y^3}{3}\right]_0^{h_1} = \frac{\rho_1 g h_1^3}{6\cos^2\alpha} $$

The same follows from the cross product $\vec{r}\times d\vec{F}_1$ with $\vec{r} = (-y\tan\alpha, y)$: $M_z = x\,dF_y - y\,dF_x = -\rho_1 g (h_1 - y)\,y\,(\sin^2\alpha + \cos^2\alpha)\,dy/\cos^2\alpha$, clockwise, with $\sin^2\alpha + \cos^2\alpha = 1$. By symmetry, liquid 2 gives the counterclockwise moment $M_2 = \rho_2 g h_2^3/(6\cos^2\alpha)$. The weight and the reaction pass through $O$. Moment balance about $O$:

$$ \frac{\rho_1 g h_1^3}{6\cos^2\alpha} = \frac{\rho_2 g h_2^3}{6\cos^2\alpha} \quad\Longrightarrow\quad \rho_1 h_1^3 = \rho_2 h_2^3 \quad\Longrightarrow\quad \frac{h_1}{h_2} = \left(\frac{\rho_2}{\rho_1}\right)^{1/3} $$

## Answers and Checks

- $R_x = \tfrac{g}{2}(\rho_2 h_2^2 - \rho_1 h_1^2)$, $R_y = W - \tfrac{g}{2}(\rho_1 h_1^2 + \rho_2 h_2^2)\tan\alpha$.
- $h_1/h_2 = (\rho_2/\rho_1)^{1/3}$: the lighter liquid must stand higher ($h_1 > h_2$, as drawn). The angle $\alpha$ does not appear.
- **Support conditions (extension, not asked in the key)**: a vertex resting on the floor can only push up, so the position is possible only if $R_y \geq 0$, that is $W \geq \tfrac{g}{2}(\rho_1 h_1^2 + \rho_2 h_2^2)\tan\alpha$, and only if the support can supply the horizontal force $R_x$ (friction or a notch at $O$).
- With the levels in that relation, $\rho_2 h_2^2 = \rho_1 h_1^2\,(h_1/h_2) > \rho_1 h_1^2$, so $R_x > 0$: the net push of the liquids is towards liquid 1 and the floor holds the vertex back.
- **Limiting case** $\rho_1 = \rho_2$: $h_1 = h_2$, $R_x = 0$ and $R_y = W - \rho g h^2\tan\alpha$, the weight minus the buoyancy of the submerged triangle of area $h^2\tan\alpha$ (Archimedes' principle, with the vertex as the only support).
- **Dimensions**: $\rho g h^2$ is (kg m$^{-3}$)(m s$^{-2}$)(m$^2$) = N/m, like $W$; $\rho g h^3$ is N m/m.
- **Check against the official key**: fluid_statics_7.pdf gives $\vec{F}_1 = \rho_1 g h_1^2(\vec{e}_x + \tan\alpha\,\vec{e}_y)/2$, $\vec{F}_2 = \rho_2 g h_2^2(-\vec{e}_x + \tan\alpha\,\vec{e}_y)/2$, the same $R_x$ and $R_y$, $M_1 = \rho_1 g h_1^3/(6\cos^2\alpha)$ and $h_1/h_2 = (\rho_2/\rho_1)^{1/3}$, the same results. The key writes the normals pointing into the wedge, the opposite of the convention of Eq. 5.11; the forces are the same.
