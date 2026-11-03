---
materia: Fluid Mechanics
tema: "Topic 5: Hydrostatics"
tags:
  - problema-examen
  - hidrostatica
  - superficie-curva
  - coordenadas-esfericas
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-05-hydrostatics/problemas/fluid_statics_2.pdf"
id: "fs2"
pill: "FS2: Hemispherical station"
sheets:
  - 2
  - 8
tags_html:
  - "Curved surface"
  - "Spherical coordinates"
  - "Projection rule"
  - "Sheets FS2 and FS8"
---

# Problem FS2: Hemispherical Station on the Sea Floor

> Official hydrostatics sheet of the course, statement translated from the Spanish original (sheets fluid_statics_2.pdf and fluid_statics_8.pdf are two scans of the same problem). Part of [[Topic 5 - Hydrostatics]].
> Method: direct integration of $-(p - p_a)\vec{n}\,dS$ in spherical coordinates (Notes.pdf, Eq. 5.11), checked with the projection rule (Eq. 5.14).

## Statement

A hemispherical experimental station of radius $R$ is to be installed on the ocean floor at a depth $H$. Calculate the force, indicating its direction and sense, exerted on the walls of the station, knowing that the pressure inside is equal to the atmospheric pressure, $p_a$.

Translated from the Spanish original.

![[attachments/FM-T5/fs2-statement.svg]]
*Statement figure (redrawn from fluid_statics_2.pdf and fluid_statics_8.pdf, p. 1): hemispherical station of radius $R$ on the sea floor at depth $H$, atmospheric pressure $p_a$ inside, axis $z$ up from the floor*

Source: fluid_statics_2.pdf and fluid_statics_8.pdf (page 1, sheet of 29-01-01). Notes.pdf, Chapter 5: Eqs. 5.10, 5.11 and 5.14.

## Hypotheses, Data and Unknowns

- Sea water at rest, incompressible, density $\rho$; the free surface is at the atmospheric pressure $p_a$, the depth of the floor is $H > R$.
- The walls form a thin hemispherical shell of radius $R$ resting on the floor; inside, the air is at $p_a$. The force asked for is the net pressure force on the shell (water outside plus air inside); the floor of the station is not part of the walls.
- Data: $R$, $H$, $\rho$, $g$, $p_a$. Unknown: the force $\vec{F}$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $R$ | radius of the station | m |
| $H$ | depth of the sea floor | m |
| $\rho$ | density of sea water | kg/m$^3$ |

## Coordinates, Surface Element and Normal

Take the origin $O$ at the centre of the base of the hemisphere, $z$ vertical and pointing up, so the floor is $z = 0$ and the free surface $z = H$. A point of the shell is located by its **elevation** $\varphi$ above the floor plane ($0 \leq \varphi \leq \pi/2$) and its **azimuth** $\theta$ ($0 \leq \theta < 2\pi$). In the meridian section (right triangle with the radius $R$ as hypotenuse), the height $z = R\sin\varphi$ is the leg opposite to $\varphi$ and the distance to the axis $R\cos\varphi$ the adjacent leg.

The element of the sphere is a small rectangle with sides $R\,d\varphi$ (along the meridian) and $R\cos\varphi\,d\theta$ (along the parallel, a circle of radius $R\cos\varphi$):

$$ dS = R^2\cos\varphi\,d\theta\,d\varphi $$

The unit normal towards the water is the radial vector $\vec{e}_r = \cos\varphi\cos\theta\,\vec{e}_x + \cos\varphi\sin\theta\,\vec{e}_y + \sin\varphi\,\vec{e}_z$; its vertical component $n_z = \sin\varphi$ is the leg opposite to $\varphi$ of the unit right triangle.

![[attachments/FM-T5/fs2-geometry.svg]]
*Spherical coordinates of the station. Left: meridian section; the radius $R$ is the hypotenuse, $z = R\sin\varphi$ is the leg opposite to the elevation $\varphi$ and $R\cos\varphi$ the adjacent leg; the outward normal is $\vec{e}_r$, with $n_z = \sin\varphi$; the water pushes along $-\vec{e}_r$. Right: top view; at elevation $\varphi$ the parallel is a ring of radius $R\cos\varphi$, so the element is $dS = (R\cos\varphi\,d\theta)(R\,d\varphi)$*

## The Pressure and the Net Elementary Force

By (5.10), at the height $z$ (depth $H - z$): $p = p_a + \rho g (H - z) = p_a + \rho g (H - R\sin\varphi)$.

The water pushes the outer face with $-p\,\vec{e}_r\,dS$; the air pushes the inner face with $-p_a(-\vec{e}_r)\,dS$, since the normal towards the air is $-\vec{e}_r$. Their sum is

$$ d\vec{F} = -(p - p_a)\,\vec{e}_r\,dS = -\rho g (H - R\sin\varphi)\,\vec{e}_r\,R^2\cos\varphi\,d\theta\,d\varphi $$

## Integration

**Horizontal components.** $F_x$ contains $\int_0^{2\pi}\cos\theta\,d\theta = [\sin\theta]_0^{2\pi} = 0$, and $F_y$ contains $\int_0^{2\pi}\sin\theta\,d\theta = [-\cos\theta]_0^{2\pi} = 0$: by the axial symmetry the horizontal forces cancel.

**Vertical component.** With $n_z = \sin\varphi$, the $\theta$ integral of a function independent of $\theta$ gives $2\pi$:

$$ F_z = -\int_0^{\pi/2}\!\!\int_0^{2\pi}\rho g (H - R\sin\varphi)\sin\varphi\,R^2\cos\varphi\,d\theta\,d\varphi = -2\pi R^2\rho g\int_0^{\pi/2}\left(H\sin\varphi\cos\varphi - R\sin^2\varphi\cos\varphi\right)d\varphi $$

Both terms are integrated with the substitution $u = \sin\varphi$, $du = \cos\varphi\,d\varphi$, with $u = 0$ at $\varphi = 0$ and $u = 1$ at $\varphi = \pi/2$:

$$ \int_0^{\pi/2}\sin\varphi\cos\varphi\,d\varphi = \int_0^1 u\,du = \left[\frac{u^2}{2}\right]_0^1 = \frac{1}{2}, \qquad \int_0^{\pi/2}\sin^2\varphi\cos\varphi\,d\varphi = \int_0^1 u^2\,du = \left[\frac{u^3}{3}\right]_0^1 = \frac{1}{3} $$

Therefore

$$ F_z = -2\pi R^2\rho g\left(\frac{H}{2} - \frac{R}{3}\right) = -\pi R^2\rho g\left(H - \frac{2R}{3}\right) $$

## Check with the Projection Rule

![[attachments/FM-T5/fs2-column.svg]]
*Projection rule (Eq. 5.14): $F_z$ is the weight of the water that would stand above the hemisphere, the cylinder $\pi R^2 H$ minus the hemisphere $\tfrac{2}{3}\pi R^3$; it points down*

By (5.14), the vertical force on a surface with the water above it is the weight of the water column standing on it, down to the surface: the cylinder of radius $R$ and height $H$, $\pi R^2 H$, minus the volume of the hemisphere, $\tfrac{2}{3}\pi R^3$, which is not water:

$$ F_z = -\rho g\left(\pi R^2 H - \frac{2}{3}\pi R^3\right) = -\pi R^2\rho g\left(H - \frac{2R}{3}\right) $$

the same result. The air inside contributes nothing net because $p_a$ also acts at the top of the column.

## Answers and Checks

- $\vec{F} = -\pi R^2\rho g\,(H - 2R/3)\,\vec{e}_z$: vertical, downward (since $H > R > 2R/3$), pressing the station against the floor; no horizontal component.
- **Limiting case** of a small station, $R \ll H$: $F_z \approx -\rho g H\,\pi R^2$, the gauge pressure at the floor times the base area, as for a flat lid; the term $2R/3$ comes from the hemisphere volume, which is not water.
- **Physical reading**: the station is not lifted by Archimedes' principle, because no water reaches its base: the buoyancy formula (5.15) applies only to a surface closed by water.
- **Dimensions**: $\rho g R^2 H$ is (kg m$^{-3}$)(m s$^{-2}$)(m$^3$) = N.
- **Check against the official key**: fluid_statics_2.pdf (and its second scan fluid_statics_8.pdf) sets up the same integral, $F_z = -\int\!\!\int\rho g(H - R\sin\varphi)\sin\varphi\,R^2\cos\varphi\,d\theta\,d\varphi$, and reaches $-2\pi R^2\rho g[H\sin^2\varphi/2 - R\sin^3\varphi/3]_0^{\pi/2}$, which equals the result above.

> [!warning] Discrepancy with the official solution
> The handwritten last line reads $-\pi R^2\rho g\,[H - 2R/3]\,\vec{e}_z$ preceded by a mark that looks like a struck-out 4 (reading of handwriting). The previous line of the key, $-2\pi R^2\rho g\,[H\sin^2\varphi/2 - R\sin^3\varphi/3]_0^{\pi/2}$, evaluates to $-2\pi R^2\rho g\,(H/2 - R/3) = -\pi R^2\rho g\,(H - 2R/3)$, coefficient $\pi$, as above.
