# Tutoring self-test (4 Nov 2026, 12:00): candidate doubts per block

How to use: cover the answer, try to answer in 30 s. Tick the ones you cannot -> ask the professor.
Equation numbers refer to `Notes.pdf`; where I am not sure of the exact number I write "(check)".

---

## B1 - Kinematics (Topic 2) - priority

1. **Streamline vs pathline vs streakline: when do they coincide, and how do you compute each?**
   - Coincide only in **steady** flow. Streamline: $dx/u = dy/v$ at fixed $t$. Pathline: $d\bar x/dt = \bar v(\bar x,t)$ integrated in time. Streakline: all particles that passed through a point $\bar x_0$; take pathline with $\bar x(\tau)=\bar x_0$ and eliminate $\tau$.
2. **In an unsteady flow, do you treat $t$ as a constant when integrating streamlines?** Yes (frozen time). For pathlines no.
3. **Material derivative of a field: write $D\bar v/Dt$ and name each term.** $\partial \bar v/\partial t$ (local) $+ (\bar v\cdot\nabla)\bar v$ (convective). A steady flow can have nonzero acceleration.
4. **Steady flow in one frame, unsteady in another?** Yes (e.g. body moving in still fluid is unsteady in the ground frame, steady in the body frame). Ask: which frame do they expect in exam problems?
5. **Decomposition of $\nabla\bar v$:** symmetric part = rate of strain $\bar{\bar\gamma}$ (deformation), antisymmetric part = rotation, $\bar\omega=\nabla\times\bar v$ (vorticity = 2x angular velocity).
6. **What does $\nabla\cdot\bar v$ mean physically?** Relative rate of change of volume of a fluid particle: $\frac{1}{V}\frac{DV}{Dt}=\nabla\cdot\bar v$. Incompressible: $\nabla\cdot\bar v=0$.
7. **Reynolds transport theorem: fixed CV vs moving CV, which velocity goes in the flux term?** Fixed: $\bar v\cdot\bar n$. Moving CV: relative velocity $(\bar v-\bar v_c)\cdot\bar n$. Classic mistake.
8. **Is irrotational the same as incompressible?** No, independent properties. Potential flow needs irrotational; $\nabla^2\phi=0$ needs both.
9. **Lagrangian <-> Eulerian:** given $\bar x(\bar x_0,t)$, invert for $\bar x_0$ and differentiate; given $\bar v(\bar x,t)$, integrate pathlines. Ask: do they expect the inversion explicitly in exam?

---

## B2 - Conservation laws, integral (Topic 3) - top priority (likely the long problem)

**Choosing the CV**
1. **Where do you cut the CV and why?** Through inlets/outlets where velocity and pressure are known (uniform profile, $p=p_a$ in free jets), and *through* the solid supports if you want the force on them.
2. **Fixed vs moving CV (e.g. moving cart or plate): what changes?** Mass flux uses relative velocity; in an inertial moving CV (constant velocity) momentum uses relative velocities as well. Accelerating CV adds fictitious force $-\int\rho \bar a_0\,dV$. Ask: does she want the inertial or non-inertial version in the sprinkler (2025) type?

**Pressure terms**
3. **Free jet in atmosphere: pressure in the jet?** $p=p_a$ (subsonic jet, straight streamlines).
4. **Why can you work with gauge pressure $p-p_a$?** $\oint p_a\bar n\,d\sigma=0$ over a closed surface. Only valid if $p_a$ acts on the **whole** closed surface. Ask: what about the part of the CV that cuts a solid wall (the reaction)?
5. **Force on the solid vs force by the fluid: sign.** Momentum gives the force the solid exerts on the fluid; force on the solid is its opposite. Most frequent sign error.

**Viscous term**
6. **When is the viscous integral negligible?** At inlets/outlets with uniform (or fully developed) flow, normal viscous stresses $\sim\mu\,\partial u/\partial x\approx 0$; on walls it is NOT zero but is part of the wall force you are computing.

**Angular momentum (sprinkler, pipe bends)**
7. **Torque balance: $\bar r\times$ of what?** $\int\rho(\bar r\times\bar v)(\bar v\cdot\bar n)\,d\sigma = \bar M$ on the fluid. Rotating sprinkler: absolute velocity of the jet = relative minus $\Omega R$ (watch sign). Free rotation (no friction): $M=0$ gives $\Omega$.

**Energy**
8. **Which energy equation: total, mechanical or internal?** Total energy (with heat $\dot Q$, work of pressure and of shafts); mechanical energy only if no heat/dissipation info is needed. Ask: in heated-jet problems (2024), is the viscous dissipation always neglected?
9. **Enthalpy appears where?** Flux of $(e+p/\rho+v^2/2)$ = flux of $(h+v^2/2)$; pressure work at inlets/outlets is absorbed into $h$.
10. **Unsteady term: when can't you drop it?** Tank filling/emptying, moving pistons (2021). $\frac{d}{dt}\int\rho\,dV$ ≠ 0 even if the flow at the outlet looks steady.

**Quick checks**
11. Mass balance done first? Units of each term (N, N m, W)? Limit $\theta\to0$ / $v\to0$ makes sense?

---

## B3 - Navier-Stokes (Topic 4) - light

1. **Which terms cancel in a fully developed flow (Couette/Poiseuille)?** $\partial u/\partial x=0$ by continuity -> $v=0$ -> convective term $=0$. Pressure gradient constant.
2. **Boundary conditions:** no-slip on walls; free surface: $p=p_a$ and $\mu\,\partial u/\partial y=0$ (no shear).
3. **Short-question pattern (2024, 2025): $v_y$ from continuity in a boundary layer / Couette with convection.** $v\sim U\delta/L$. Ask: how deep will short questions go in order-of-magnitude estimates?
4. **Viscous dissipation $\Phi_v$ in the energy equation:** when is it relevant? (Large $\mu U^2/(k\Delta T)$, Brinkman number.)

---

## B5 - Fluid statics (Topic 5) - new, only FS10 done in class

1. **Fundamental equation:** $-\nabla p+\rho\bar f_m=0$; with gravity $p+\rho g z=$ const (Eq. 5.10). Pressure grows downward.
2. **Two immiscible liquids:** $p$ continuous across the interface; $p+\rho_i g z$ const *within each* liquid.
3. **Force on a plane surface:** $F=\int p\,d\sigma = p_{\text{centroid}}A$ (gauge). Point of application (centre of pressure) is **below** the centroid. Note: centre of pressure is marked as an **extension** in the portal notes; ask the professor whether she expects $y_{cp}=y_c+I/(y_cA)$ or always direct integration of the moment.
4. **Horizontal force on a curved surface:** equals the force on its vertical projection (Eq. 5.14).
5. **Vertical force on a curved surface:** weight of the fluid (real or imaginary) between the surface and the free surface. Sign: fluid above -> downward; fluid below -> upward.
6. **Archimedes:** buoyancy = weight of displaced fluid, acting at the centroid of the displaced volume. Partially submerged in two fluids: sum both contributions.
7. **Trapped air (FS3/FS6):** isothermal ideal gas, $pV=$ const; air pressure = liquid pressure at the interface. Ask: is isothermal always the assumption unless stated?
8. **Stability:** fully submerged body stable if centre of buoyancy above centre of gravity. Floating body uses the metacentre (marked **extension** in the portal). Ask: does the metacentre enter the exam?
9. **Hinged gate (FS9):** moment of pressure forces about the hinge = moment of the weight/restraining force; integrate $\int p\,(\text{arm})\,d\sigma$.
10. **Rotating / accelerating containers:** $\bar f_m=-\bar g-\bar a$ (or $+\Omega^2 r$); free surface is a paraboloid $z=\Omega^2r^2/(2g)+$const. Ask: does rigid-body rotation/acceleration enter Topic 5 this year?
11. **Standard atmosphere:** $dp/dz=-\rho g$, $p=\rho R_gT$, $T=T_0-\alpha z$ up to 11 km: $p/p_0=(T/T_0)^{g/(R_g\alpha)}$; isothermal layer: $p\propto e^{-gz/(R_gT)}$.

---

## Logistics to ask the professor
- Exam duration and split (theory vs problem) for group 46.
- Can Topic 5 appear as the long problem or only as a short question?
- In theory part: derivations to reproduce from memory, or only concepts?
