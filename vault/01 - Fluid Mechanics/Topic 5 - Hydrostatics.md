---
materia: Fluid Mechanics
tema: "Topic 5: Hydrostatics"
fuentes:
  - "Notes.pdf (Sánchez & Rodríguez-Rodríguez, UC3M), Chapter 5, pp. 51-56 (PDF pages 60-65)"
tags:
  - moc-topic
  - fluid-mechanics
  - hydrostatics
  - second-year
dificultad: medium
---

# Topic 5: Hydrostatics

> **Central idea.** When the fluid is at rest in some reference frame, the convective and viscous terms of the Navier-Stokes equations vanish and momentum conservation reduces to a balance between the pressure gradient and the mass forces, $-\nabla p + \rho\vec{f}_m = 0$. For a liquid under gravity this gives $p + \rho g z = p_a$; integrating that pressure over a surface gives the forces on gates, walls and submerged bodies (Archimedes' principle), and for a gas it gives the pressure distribution of the standard atmosphere.

---

## 1. The Equilibrium Equations

### Fluid at rest

A fluid is at rest with respect to a reference frame when $\vec{v} = 0$ at every point. Putting $\vec{v} = 0$ in the continuity, momentum and energy equations of Chapter 4 cancels every convective term, every viscous stress and the viscous dissipation, and leaves (Notes.pdf, Eqs. 5.1-5.3):

$$ \frac{\partial \rho}{\partial t} = 0 \tag{5.1} $$

$$ -\nabla p + \rho\vec{f}_m = 0 \tag{5.2} $$

$$ \rho\frac{\partial e}{\partial t} = \nabla\cdot(k\nabla T) + Q_r + Q_c \tag{5.3} $$

- (5.1): in a fluid at rest the density cannot change in time, although it may change from point to point.
- (5.2): with no motion, the net pressure force on each fluid particle, $-\nabla p\,dV$, balances the mass force $\rho\vec{f}_m\,dV$. This is the equation used in the whole chapter.
- (5.3): the internal energy changes only by heat conduction, radiation and chemical reaction.

### Mass forces in a non-inertial frame

If the fluid is at rest in a frame that moves with acceleration $\vec{a}_o$ and angular velocity $\vec{\Omega}$, the mass force includes the inertial forces of that frame (Notes.pdf, Eq. 5.4):

$$ \vec{f}_m(\vec{x},t) = \vec{g} - \vec{a}_o - \vec{\Omega}\times(\vec{\Omega}\times\vec{x}) - \frac{d\vec{\Omega}}{dt}\times\vec{x} \tag{5.4} $$

The Coriolis force $-2\vec{\Omega}\times\vec{v}$ does not appear because $\vec{v} = 0$ in this frame.

### Initial, boundary and interface conditions

The only initial velocity compatible with equilibrium is $\vec{v} = 0$, and the no-slip condition then requires every solid boundary to be at rest. Integrating (5.1) gives $\rho(\vec{x},t) = \rho_i(\vec{x})$, the initial distribution. With surface tension neglected, mechanical equilibrium at the interface between two immiscible fluids requires **equal pressure on both sides**, and thermodynamic equilibrium requires equal temperature (Notes.pdf, p. 52).

---

## 2. Hydrostatics of Liquids

### Only conservative mass forces allow equilibrium

For a perfect liquid ($\rho$ constant), (5.1) holds identically and (5.2) can be divided by $\rho$ (Notes.pdf, Eq. 5.5):

$$ -\nabla\left(\frac{p}{\rho}\right) + \vec{f}_m = 0 \tag{5.5} $$

The first term is a gradient, so $\vec{f}_m$ must be a gradient too: equilibrium is possible only if the mass force derives from a potential $U$,

$$ \vec{f}_m = -\nabla U \tag{5.6} $$

The first three terms of (5.4) do derive from a potential (Notes.pdf, Eq. 5.7):

$$ U = -\vec{g}\cdot\vec{x} + \vec{a}_o\cdot\vec{x} - \frac{(\vec{\Omega}\times\vec{x})\cdot(\vec{\Omega}\times\vec{x})}{2} \tag{5.7} $$

Each term can be checked by taking its gradient: $\nabla(-\vec{g}\cdot\vec{x}) = -\vec{g}$ and $\nabla(\vec{a}_o\cdot\vec{x}) = \vec{a}_o$ because $\nabla(\vec{c}\cdot\vec{x}) = \vec{c}$ for a constant vector; and for $\vec{\Omega} = \Omega\vec{e}_z$, $\lvert\vec{\Omega}\times\vec{x}\rvert^2 = \Omega^2(x^2+y^2) = \Omega^2 r^2$, whose gradient is $2\Omega^2 r\,\vec{e}_r$, so $-\nabla(\Omega^2 r^2/2) = -\Omega^2 r\,\vec{e}_r$ and $\vec{f}_m = -\nabla U$ contains $+\Omega^2 r\,\vec{e}_r = -\vec{\Omega}\times(\vec{\Omega}\times\vec{x})$, the centrifugal force. The last term of (5.4), $-(d\vec{\Omega}/dt)\times\vec{x}$, has a non-zero curl ($\nabla\times(\dot{\vec{\Omega}}\times\vec{x}) = 2\dot{\vec{\Omega}}$), so it is not conservative: **a liquid can be at rest in a rotating frame only if $\vec{\Omega}$ is constant**.

### The pressure field

Substituting (5.6) in (5.5) gives $\nabla(p/\rho + U) = 0$; with $\rho$ constant, $\nabla(p + \rho U) = 0$, so $p + \rho U$ does not depend on position (Notes.pdf, Eq. 5.8):

$$ p + \rho U = C(t) \tag{5.8} $$

where $C(t)$ is the value of $p + \rho U$ at any point where the pressure is known, usually a free surface. The temperature follows from (5.3); with no radiation or reaction and constant $k$, it is the heat equation $\partial T/\partial t = \alpha\nabla^2 T$, $\alpha = k/(\rho c_p)$ (Notes.pdf, Eq. 5.9).

### Worked consequences of (5.7) and (5.8)

These two examples are applications of Eqs. (5.7)-(5.8), written out here; they are not worked in the notes.

- **Uniform horizontal acceleration** $\vec{a}_o = a\vec{e}_x$, gravity $-g\vec{e}_z$: $U = gz + ax$, so $p = C - \rho(gz + ax)$. The free surface is the isobar $p = p_a$: $gz + ax = \text{const}$, a plane with slope $dz/dx = -a/g$. Its angle with the horizontal is $\beta = \arctan(a/g)$: in the right triangle formed by a horizontal run $\Delta x$ and the drop $\Delta z$, the leg opposite to $\beta$ is $\Delta z = (a/g)\Delta x$ and the adjacent leg is $\Delta x$, so $\tan\beta = a/g$.
- **Rigid-body rotation** $\vec{\Omega} = \Omega\vec{e}_z$ (constant): $U = gz - \Omega^2r^2/2$, so $p = C - \rho g z + \rho\Omega^2 r^2/2$. The free surface $p = p_a$ is the paraboloid $z = z_0 + \Omega^2 r^2/(2g)$, where $z_0$ is its height on the axis.

---

## 3. A Liquid at Rest under Gravity

### The hydrostatic law

Under gravity alone, $U = gz$ with $z$ the vertical coordinate pointing up ($\vec{g} = -g\vec{e}_z$). If the liquid is bounded by a gas at pressure $p_a$ and $z$ is measured from that free surface ($z = 0$ on it, $z < 0$ in the liquid), (5.8) evaluated on the surface gives $C = p_a$ and (Notes.pdf, Eq. 5.10):

$$ p + \rho g z = p_a \tag{5.10} $$

so $p = p_a + \rho g(-z)$: the pressure grows linearly with the depth $-z$, at the rate $\rho g \approx 9.81\times10^{3}$ Pa/m for water. The gas pressure itself is uniform over heights of a few metres, because the density of a gas is about a thousand times smaller (Section 7).

### Several immiscible liquids

Layers of different densities stack with the heaviest at the bottom, each layer obeys (5.10) with its own $\rho_i$, and the pressure is continuous across every interface (Section 1). The walking rule below is a direct consequence of (5.10) and the interface condition, written out here (it is not stated in the notes). Walking from a point where $p$ is known to another point, each vertical step adds $+\rho_i g\,\Delta d$ when going **down** a depth $\Delta d$ in liquid $i$ and $-\rho_i g\,\Delta d$ when going **up**; horizontal steps inside one connected liquid add nothing.

### Manometers

The manometer is not in Chapter 5 of the notes: this subsection is an **extension**, a direct use of (5.10) and of the walking rule.

![[attachments/FM-T5/t5-manometer.svg]]

For the U-tube of the figure, walking from the point $A$ of the pipe down the column $h_1$ of the pipe liquid, then up the level difference $h_2$ of the manometric liquid, and ending at the open level where $p = p_a$:

$$ p_A + \rho g h_1 - \rho_m g h_2 = p_a \quad\Longrightarrow\quad p_A - p_a = \rho_m g h_2 - \rho g h_1 $$

Check: with the same liquid in both ($\rho_m = \rho$) and $h_1 = h_2$, the pipe point is at the open level and $p_A = p_a$, as it must.

---

## 4. Forces and Moments on a Surface

### The general expressions

The pressure force on a surface element $d\sigma$ of unit normal $\vec{n}$ **oriented towards the fluid** is $-p\vec{n}\,d\sigma$: it pushes the wall away from the fluid. Adding over a surface $\Sigma$ gives the force and the moment about a point $\vec{x}_o$ (Notes.pdf, Eq. 5.11):

$$ \vec{F} = -\int_\Sigma p\,\vec{n}\,d\sigma, \qquad \vec{M} = -\int_\Sigma (\vec{x}-\vec{x}_o)\times p\,\vec{n}\,d\sigma \tag{5.11} $$

With (5.10), $p = p_a - \rho g z$ and the two integrals split into the contribution of the gas pressure and the weight of the liquid column above each element (Notes.pdf, Eqs. 5.12-5.13):

$$ \vec{F} = -\int_\Sigma p_a\vec{n}\,d\sigma + \rho g\int_\Sigma z\,\vec{n}\,d\sigma \tag{5.12} $$

$$ \vec{M} = -\int_\Sigma (\vec{x}-\vec{x}_o)\times p_a\vec{n}\,d\sigma + \rho g\int_\Sigma (\vec{x}-\vec{x}_o)\times z\,\vec{n}\,d\sigma \tag{5.13} $$

When the gas pressure $p_a$ also acts on the other side of the wall (a gate with air behind it), the first terms cancel against the gas side, and only the **gauge pressure** $p - p_a = -\rho g z = \rho g\times\text{depth}$ counts.

### Projection rule

The component of the force along a fixed unit vector $\vec{m}$ is (Notes.pdf, Eq. 5.14):

$$ F_m = \vec{F}\cdot\vec{m} = -\int_\Sigma (p_a - \rho g z)\,\vec{n}\cdot\vec{m}\,d\sigma = -\int_{\Sigma_m}(p_a - \rho g z)\,d\sigma_m \tag{5.14} $$

where $d\sigma_m = \vec{n}\cdot\vec{m}\,d\sigma$ is the projection of $d\sigma$ on a plane normal to $\vec{m}$. Two consequences are used in every problem:

- **Horizontal component**: with $\vec{m}$ horizontal, every element keeps its depth $-z$ when projected horizontally, so the horizontal force on any surface equals the force on its **projection on a vertical plane**.
- **Vertical component**: with $\vec{m} = \vec{e}_z$, $d\sigma_z$ is the horizontal footprint of the element, and $-\rho g z\,d\sigma_z$ is the weight of the liquid column of height $-z$ above it. The vertical force equals the **weight of the liquid (real or virtual) between the surface and the free surface**, downward when the liquid is above the surface and upward when it is below.

### 4.1 Plane surfaces: resultant and centre of pressure

![[attachments/FM-T5/t5-plane-surface.svg]]

Chapter 5 of the notes stops at the general expressions (5.11)-(5.14). This subsection is an **extension**: it evaluates (5.11) for a plane surface, which is what the problem sheets need.

**Coordinates.** Let a plane surface of area $A$ make an angle $\theta$ with the horizontal free surface. Its plane cuts the free surface along a horizontal line through $O$; take $s$ as the distance from that line measured down the plane, and $x$ along the line. A point at distance $s$ is at depth $s\sin\theta$: in the right triangle with the hypotenuse $s$ along the plate and one leg vertical, the vertical leg is opposite to the angle $\theta$, so it equals $s\sin\theta$ (the horizontal leg, adjacent to $\theta$, is $s\cos\theta$).

**Element.** The strip between $s$ and $s + ds$ has width $w(s)$ and area $dA = w(s)\,ds$; its gauge pressure is $p - p_a = \rho g s\sin\theta$ and its normal is the same for the whole plate, so all the elementary forces are parallel:

$$ dF = \rho g\sin\theta\, s\, dA $$

**Resultant.** Integrating over the plate, with $\theta$ constant and the definition of the centroid, $\int_A s\,dA = s_C A$:

$$ F_R = \rho g\sin\theta\int_A s\,dA = \rho g\sin\theta\, s_C A = (p_C - p_a)\,A $$

The resultant equals the gauge pressure **at the centroid** times the area; it is normal to the plate.

**Centre of pressure.** The moment of the elementary forces about the line $O$ is $\int_A s\,dF = \rho g\sin\theta\int_A s^2\,dA = \rho g\sin\theta\, I_O$, with $I_O$ the second moment of area about the line through $O$. The resultant gives the same moment when applied at $s_{CP}$, so $F_R\,s_{CP} = \rho g\sin\theta\, I_O$ and

$$ s_{CP} = \frac{I_O}{s_C A} $$

Steiner's theorem relates $I_O$ to the second moment $I_C$ about the parallel axis through the centroid: writing $s = s_C + \xi$ with $\int_A \xi\,dA = 0$,

$$ I_O = \int_A (s_C + \xi)^2 dA = s_C^2 A + 2s_C\int_A\xi\,dA + \int_A \xi^2 dA = I_C + s_C^2 A $$

and therefore

$$ s_{CP} = s_C + \frac{I_C}{s_C A} $$

The centre of pressure is always **below** the centroid (the deeper half of the plate carries more pressure), and it approaches the centroid as the plate goes deeper ($s_C\to\infty$). For a shape symmetric about the line $x = x_C$, the lateral position is $x_{CP} = x_C$.

**Moment about the centroidal axis.** The moment of the pressure about the horizontal axis through $C$ is $F_R(s_{CP} - s_C) = \rho g\sin\theta\, s_C A\cdot I_C/(s_C A) = \rho g\sin\theta\, I_C$: it **does not depend on the depth**. A gate pivoting about its own centroidal axis needs the same holding moment at any water level (problem FS4).

| Shape (lower edge horizontal) | $A$ | Centroid from the lower edge | $I_C$ about the horizontal centroidal axis |
| :--- | :--- | :--- | :--- |
| Rectangle $b\times L$ ($L$ along $s$) | $bL$ | $L/2$ | $bL^3/12$ |
| Triangle, base $b$ at the bottom, height $L$ | $bL/2$ | $L/3$ | $bL^3/36$ |
| Circle of diameter $D$ | $\pi D^2/4$ | $D/2$ | $\pi D^4/64$ |

These three second moments are computed with $I_C = \int \xi^2\,dA$ in `tools/fluids_fs/verify_fluid_statics.py`.

### 4.2 Curved surfaces

![[attachments/FM-T5/t5-curved-surface.svg]]

On a curved surface the elementary forces change direction from point to point, so the force is found component by component: by direct integration or by the projection rule (5.14). This subsection is an **extension** with worked examples of (5.11) and (5.14); the examples are not in the notes. Both methods are shown on the quarter-cylinder gate of the figure: radius $R$, width $b$, centre $O$ on the free surface, liquid above the arc and air at $p_a$ below it.

**Direct integration.** Measure $\theta$ from the horizontal radius $OB$ down to the radius of the element. In the right triangle with hypotenuse $R$ (the radius), the vertical leg is opposite to $\theta$ and the horizontal leg is adjacent: the element is at $x = R\cos\theta$, depth $R\sin\theta$. The arc length of the element is $R\,d\theta$ and its area is $d\sigma = bR\,d\theta$. The normal towards the liquid points from the arc to $O$, $\vec{n} = -(\cos\theta\,\vec{e}_x - \sin\theta\,\vec{e}_z)$, so with the gauge pressure $\rho g R\sin\theta$:

$$ d\vec{F} = -(p - p_a)\vec{n}\,d\sigma = \rho g R\sin\theta\,(\cos\theta\,\vec{e}_x - \sin\theta\,\vec{e}_z)\,bR\,d\theta $$

Horizontal component, with $\int\sin\theta\cos\theta\,d\theta = \sin^2\theta/2$ (substitution $u = \sin\theta$, $du = \cos\theta\,d\theta$) and Barrow's rule:

$$ F_H = \rho g b R^2\int_0^{\pi/2}\sin\theta\cos\theta\,d\theta = \rho g b R^2\left[\frac{\sin^2\theta}{2}\right]_0^{\pi/2} = \rho g b R^2\left(\frac{1}{2} - 0\right) = \frac{\rho g b R^2}{2} $$

Vertical component, with $\sin^2\theta = (1 - \cos 2\theta)/2$ and $\int\cos 2\theta\,d\theta = \sin 2\theta/2$:

$$ F_V = -\rho g b R^2\int_0^{\pi/2}\sin^2\theta\,d\theta = -\rho g b R^2\left[\frac{\theta}{2} - \frac{\sin 2\theta}{4}\right]_0^{\pi/2} = -\rho g b R^2\left(\frac{\pi}{4} - 0\right) = -\frac{\pi\rho g b R^2}{4} $$

**Projection method.** The vertical projection of the arc is a rectangle of height $R$ and width $b$ with its centroid at depth $R/2$, so $F_H = \rho g (R/2)(bR) = \rho g b R^2/2$, applied at $2R/3$ below the surface (the centre of pressure of a rectangle starting at the surface, from Section 4.1). The liquid above the arc is a quarter disc of area $\pi R^2/4$, so $F_V$ is its weight, $\rho g b\pi R^2/4$, downward, through its centroid at $4R/(3\pi)$ from $O$. Both methods agree.

**Line of action.** Every $d\vec{F}$ is radial, so it passes through $O$; the resultant of forces through one point passes through that point. The magnitude is $\rho g b R^2\sqrt{1/4 + \pi^2/16}$ (Pythagoras on the two components). The angle $\gamma$ below the horizontal comes from the right triangle of the force components: the leg opposite to $\gamma$ is $\lvert F_V\rvert = \pi\rho g b R^2/4$, the adjacent leg is $F_H = \rho g b R^2/2$, so $\tan\gamma = (\pi/4)/(1/2) = \pi/2$ and $\gamma \approx 57.5^\circ$.

**Areas made of a sector and a triangle.** When the free surface cuts a circular wall at a general height, the area that gives $F_V$ is a circular sector plus or minus a right triangle. For a circle of radius $R$ resting on the floor with the liquid up to height $h$ on one side, call $\beta$ the angle at the centre between the downward vertical and the radius to the waterline point, so $R - h = R\cos\beta$ (adjacent leg of the right triangle with hypotenuse $R$). The wetted half-disc area below the waterline is

$$ A(h) = \frac{R^2\beta}{2} - \frac{1}{2}(R - h)\,R\sin\beta $$

the sector of angle $\beta$ minus the triangle with legs $R - h$ and $R\sin\beta$ (for $h > R$ the leg $R - h$ is negative and the triangle is added). The same result follows by integration: a horizontal strip at the height $y = R - R\cos u$ has the half-width $R\sin u$ and the thickness $dy = R\sin u\,du$, so, with $\sin^2 u = (1 - \cos 2u)/2$ and Barrow's rule,

$$ A = R^2\int_0^\beta \sin^2 u\,du = R^2\left[\frac{u}{2} - \frac{\sin 2u}{4}\right]_0^\beta = \frac{R^2\beta}{2} - \frac{R^2\sin\beta\cos\beta}{2} = \frac{R^2\beta}{2} - \frac{1}{2}(R - h)\,R\sin\beta $$

using $\sin 2\beta = 2\sin\beta\cos\beta$ and $R\cos\beta = R - h$ (checked in `verify_fluid_statics.py`). Problem FS10 and its simulator use this decomposition.

---

## 5. Archimedes' Principle

![[attachments/FM-T5/t5-archimedes.svg]]

For a **closed** surface $\Sigma$ enclosing a submerged body of volume $V$, the pressure on the body is the one the liquid would have if it filled $V$, so the Gauss formula $\oint_\Sigma f\vec{n}\,d\sigma = \int_V \nabla f\,dV$ can be applied to (5.12). With $\nabla p_a = 0$ and $\nabla(\rho g z) = \rho g\,\vec{e}_z$ (Notes.pdf, Eq. 5.15):

$$ \vec{F} = -\int_V \nabla p_a\,dV + \rho g\int_V \nabla z\,dV = \rho g V\,\vec{e}_z \tag{5.15} $$

The moment follows from $\oint_\Sigma \vec{n}\times\vec{A}\,d\sigma = \int_V\nabla\times\vec{A}\,dV$ with $\vec{A} = p(\vec{x}-\vec{x}_o)$. Since $-(\vec{x}-\vec{x}_o)\times p\vec{n} = \vec{n}\times p(\vec{x}-\vec{x}_o)$ and $\nabla\times[p(\vec{x}-\vec{x}_o)] = \nabla p\times(\vec{x}-\vec{x}_o) + p\,\nabla\times\vec{x}$ with $\nabla\times\vec{x} = 0$ and $\nabla p = -\rho g\,\vec{e}_z$ (Notes.pdf, Eq. 5.16):

$$ \vec{M} = -\rho g\,\vec{e}_z\times\int_V(\vec{x}-\vec{x}_o)\,dV = (\vec{x}_g - \vec{x}_o)\times\rho g V\,\vec{e}_z \tag{5.16} $$

where $\vec{x}_g = V^{-1}\int_V\vec{x}\,dV$ is the centroid of the displaced liquid. Equations (5.15) and (5.16) are **Archimedes' principle**: the buoyancy force on a submerged body equals the weight of the displaced liquid and acts at the centroid of the displaced volume (also called the centre of buoyancy), which in general is not the centre of gravity of the body.

The two consequences below are an **extension** of (5.15), used in the problem sheets.

- **Floating bodies.** For a body that floats, the same argument applies to the submerged part, closed by the waterline plane where $p = p_a$: the buoyancy is the weight of the liquid displaced below the waterline (problems FS1, FS3, FS6).
- **Trapped gas.** When a gas pocket inside an open-bottom body is part of the floating system, the displaced volume includes the gas below the free surface (problems FS3 and FS6).

---

## 6. Stability of Submerged and Floating Bodies

![[attachments/FM-T5/t5-stability.svg]]

A body in equilibrium is **stable** if, after a small perturbation, the forces bring it back. For a submerged body (Notes.pdf, p. 53, and Fig. 5.1 on p. 54), the buoyancy $\rho g V\vec{e}_z$ acts at the centroid $A$ of the displaced liquid and the weight $-W\vec{e}_z$ at the centre of gravity $B$ of the body; in equilibrium $W = \rho g V$ and $A$, $B$ are on the same vertical. If the body is tilted, $A$ and $B$ turn with it (the displaced volume is the body itself): with $A$ above $B$ the pair of forces is a restoring torque, with $B$ above $A$ it turns the body over. **A submerged body is stable when the centre of buoyancy lies above the centre of gravity**, so the centre of gravity should be as low as possible.

**Floating bodies and the metacentre (extension).** For a floating body the displaced volume changes shape when it heels, so the centre of buoyancy moves sideways, from $B$ to $B'$, towards the side that goes down. The vertical through $B'$ cuts the symmetry line of the body at the **metacentre** $M$. For a small heel angle $\alpha$, the wedge of volume that emerges on one side and sinks on the other moves the centre of buoyancy by $BB' = I_{wl}\,\alpha/V$, where $I_{wl}$ is the second moment of the waterline area about the heel axis, so the metacentric radius is

$$ BM = \frac{BB'}{\alpha} = \frac{I_{wl}}{V}, \qquad GM = BM - BG $$

The body is stable when $M$ is above the centre of gravity $G$ ($GM > 0$): then the buoyancy at $B'$ and the weight at $G$ form a restoring torque even if $G$ is above $B$. This is why ships can carry their centre of gravity above the centre of buoyancy, while submarines cannot. Notation: the notes call the centroid $A$ and the centre of gravity $B$; ship stability uses $B$ for the centre of buoyancy and $G$ for the centre of gravity.

---

## 7. Gases at Rest: the Standard Atmosphere

### Hydrostatics of a gas

For a gas in equilibrium under gravity, (5.2) gives $\partial p/\partial x = \partial p/\partial y = 0$ and (Notes.pdf, Eq. 5.17):

$$ \frac{dp}{dz} = -\rho g \tag{5.17} $$

Because the density of air is small, $dp/dz$ is only about $12$ Pa per metre at sea level ($\rho_0 g = 1.225\times 9.81$, computed here), so over heights of a few metres the pressure of a gas at rest can be taken as uniform. Appreciable changes appear over kilometres, across the atmosphere. Air is a mixture of about 78 % N$_2$, 21 % O$_2$ and 1 % Ar, well mixed by turbulence, with $W_{air} = 0.029$ kg/mol and $R_g = R/W = 287$ J/(kg K) in the equation of state (Notes.pdf, Eq. 5.18):

$$ p = \rho R_g T \tag{5.18} $$

Solving (5.18) for $\rho$ and substituting in (5.17) (Notes.pdf, Eq. 5.19):

$$ \frac{dp}{dz} = -\frac{p\,g}{R_g T} \quad\Longleftrightarrow\quad \frac{dp}{p} + \frac{g}{R_g T}\,dz = 0 \tag{5.19} $$

The temperature profile $T(z)$ must be given before integrating.

### Temperature model

The standard atmosphere uses a linear decrease of temperature in the troposphere and a constant temperature in the stratosphere (Notes.pdf, Eq. 5.20):

$$ T = \begin{cases} T_0 - \lambda z, & 0 < z < 11000\ \text{m (troposphere)} \\ T_{11} = T_0 - 11000\,\lambda, & 11000 < z < 20000\ \text{m (stratosphere)} \end{cases} \tag{5.20} $$

with the internationally accepted values $T_0 = 288.16$ K and $\lambda = 6.5\times10^{-3}$ K/m. The notes call the temperature gradient $\alpha$; here it is $\lambda$, because $\alpha$ already denotes the thermal diffusivity in (5.9). Then $T_{11} = 288.16 - 6.5\times 11 = 216.66$ K.

### Troposphere

With $T = T_0 - \lambda z$, (5.19) becomes (Notes.pdf, Eq. 5.21)

$$ \frac{dp}{p} = -\frac{g}{R_g}\frac{dz}{T_0 - \lambda z} \tag{5.21} $$

The left side integrates to $\ln p$. On the right, substitute $u = T_0 - \lambda z$, $du = -\lambda\,dz$, so $dz/(T_0 - \lambda z) = -du/(\lambda u)$ and $\int dz/(T_0 - \lambda z) = -\ln(T_0 - \lambda z)/\lambda$. Hence (Notes.pdf, Eq. 5.22)

$$ \ln p - \frac{g}{R_g\lambda}\ln(T_0 - \lambda z) = C \tag{5.22} $$

At sea level, $z = 0$ and $p = p_a = 1$ atm, so (Notes.pdf, Eq. 5.23) $C = \ln p_a - (g/(R_g\lambda))\ln T_0$. Substituting $C$ and grouping the logarithms, $\ln(p/p_a) = (g/(R_g\lambda))\ln[(T_0 - \lambda z)/T_0]$, and taking exponentials (Notes.pdf, Eq. 5.24):

$$ p = p_a\left(1 - \frac{\lambda z}{T_0}\right)^{g/(R_g\lambda)}, \qquad 0 < z < 11000\ \text{m} \tag{5.24} $$

The exponent is $g/(R_g\lambda) = 9.81/(287\times6.5\times10^{-3}) = 5.2586$ (dimensionless: $[\text{m s}^{-2}]/([\text{J kg}^{-1}\text{K}^{-1}][\text{K m}^{-1}]) = [\text{m s}^{-2}]/[\text{m s}^{-2}]$). At $z = 11$ km it gives $p_{11} = p_a(T_{11}/T_0)^{g/(R_g\lambda)} = 0.2232\,p_a \approx 22.6$ kPa.

### Stratosphere

With $T = T_{11}$ constant, (5.19) integrates directly between $11000$ m, where $p = p_{11}$, and $z$: $[\ln p]_{p_{11}}^{p} = -\frac{g}{R_g T_{11}}[z]_{11000}^{z}$, that is (Notes.pdf, Eq. 5.25)

$$ p = p_{11}\exp\left[-\frac{g\,(z - 11000)}{R_g T_{11}}\right], \qquad 11000 < z < 20000\ \text{m} \tag{5.25} $$

an exponential decay with the scale height $R_g T_{11}/g \approx 6.34$ km. At 20 km, $p \approx 0.054\,p_a \approx 5.5$ kPa.

![[attachments/FM-T5/t5-atmosphere.svg]]

The density follows from (5.18), $\rho/\rho_0 = (p/p_a)(T_0/T)$, with $\rho_0 = p_a/(R_g T_0) = 1.225$ kg/m$^3$. The values below are computed from (5.20), (5.24), (5.25) and (5.18); the four places are those marked in Fig. 5.2 of the notes.

| Place | $z$ (m) | $T$ (K) | $p/p_a$ | $\rho/\rho_0$ |
| :--- | ---: | ---: | ---: | ---: |
| Madrid | 650 | 283.94 | 0.925 | 0.94 |
| Navacerrada | 1780 | 276.59 | 0.806 | 0.84 |
| Teide | 3718 | 263.99 | 0.631 | 0.69 |
| Everest | 8848 | 230.65 | 0.310 | 0.39 |
| Tropopause | 11000 | 216.66 | 0.223 | 0.30 |
| Top of the model | 20000 | 216.66 | 0.054 | 0.07 |

At the top of Everest the density is only 39 % of its sea-level value (Notes.pdf, p. 56).

---

## 8. Practical Formulary of Topic 5

| Situation | Result | Source |
| :--- | :--- | :--- |
| Fluid at rest | $-\nabla p + \rho\vec{f}_m = 0$ | Eq. (5.2) |
| Liquid, conservative mass force | $p + \rho U = C(t)$, $U = -\vec{g}\cdot\vec{x} + \vec{a}_o\cdot\vec{x} - \lvert\vec{\Omega}\times\vec{x}\rvert^2/2$ | Eqs. (5.7)-(5.8) |
| Liquid under gravity, $z$ up from the free surface | $p = p_a - \rho g z$ | Eq. (5.10) |
| Walking through layers | $+\rho_i g\,\Delta d$ going down, $-\rho_i g\,\Delta d$ going up | Eq. (5.10) |
| Force and moment on a surface ($\vec{n}$ towards the fluid) | $\vec{F} = -\int p\vec{n}\,d\sigma$, $\vec{M} = -\int(\vec{x}-\vec{x}_o)\times p\vec{n}\,d\sigma$ | Eq. (5.11) |
| Plane surface | $F_R = (p_C - p_a)A = \rho g\sin\theta\,s_C A$, normal to the plate | Section 4.1 (extension of Eq. 5.11) |
| Centre of pressure | $s_{CP} = s_C + I_C/(s_C A)$; moment about $C$: $\rho g\sin\theta\,I_C$ | Section 4.1 (extension, Steiner) |
| Curved surface, horizontal | force on the vertical projection | Eq. (5.14) |
| Curved surface, vertical | weight of the real or virtual column above it | Eq. (5.14) |
| Submerged body | $\vec{F} = \rho g V\vec{e}_z$ at the centroid $\vec{x}_g$ of the displaced volume | Eqs. (5.15)-(5.16) |
| Stability, submerged | centre of buoyancy above the centre of gravity | Notes p. 53, Fig. 5.1 |
| Stability, floating (extension) | $GM = I_{wl}/V - BG > 0$ | Section 6 |
| Gas at rest | $dp/dz = -\rho g$, $p = \rho R_g T$ | Eqs. (5.17)-(5.18) |
| Troposphere | $p = p_a(1 - \lambda z/T_0)^{g/(R_g\lambda)}$, exponent 5.2586 | Eq. (5.24) |
| Stratosphere | $p = p_{11}\exp[-g(z - 11000)/(R_g T_{11})]$ | Eq. (5.25) |
| Isothermal gas pocket (problems FS3, FS6) | $p\,V = p_a V_0$ (constant temperature) | extension: Eq. (5.18) at constant mass and $T$ |

**Back to:** [[01 - Fluid Mechanics/Fluid Mechanics MOC|Fluid Mechanics MOC]]
