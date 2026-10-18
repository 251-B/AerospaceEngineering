# Engineering Mechanics, Midterm 1: blueprint (working draft)

Status: Phases 1 and 2 (audit and exam DNA). Nothing here is published on the portal yet.
Sources read: `sources/cuatrimestre-1/03-engineering-mechanics/examenes/MECHANICS_FIRSTPARTIAL_{2011,2013,2015,2016,2017,2018,2019,2019_V2,2024}.pdf` (text layer, full); `..._2022.pdf` is a scan (no text layer, not read yet); finals and second partials were only skimmed by statement headers.

## 1. Scope of Midterm 1 = point-particle mechanics (units 1 to 5)

Every Midterm 1 paper from 2011 to 2024 is about **particles, not rigid bodies**. Rigid-body kinematics, inertia tensors, Steiner, rolling without slipping, instantaneous centre and Euler angles appear only in the **second partial** (2011 triangle, 2015 wooden piece, 2017 coin, 2018 asteroid, 2019 twin wheels). So the rigid-body content in the request belongs to a future Midterm 2 bank, and the Midterm 1 bank must be particle problems.

Syllabus (Notes.pdf chapters; slide decks `unit-01` to `unit-05`):

| Unit | Content evaluated |
| :--- | :--- |
| 1 | Vector bases, rotation matrices, derivative of a vector, coordinates (Cartesian, cylindrical, spherical), Frenet intrinsic frame, arc length |
| 2 | Newton's laws, equations of motion, work, power, potential, mechanical energy, equilibrium, 1D potential wells, harmonic oscillator, damping, forced oscillation |
| 3 | Degrees of freedom, holonomic/rheonomic/unilateral constraints, smooth curves and surfaces, normal reaction, Coulomb friction, strings and pulleys |
| 4 | Angular momentum and torque, central forces, planar motion, Binet, Kepler, vis-viva |
| 5 | Moving reference frames, Coriolis theorem, relative velocity and acceleration, inertia forces (centrifugal, Coriolis, translational) |

## 2. Common structure of the real paper

- One problem, 10 points, 5 to 7 parts (2011 had two problems). Duration is not printed on any Midterm 1 paper; the 60 minutes comes from the 2015 Quiz 2 (second partial) and is an assumption here.
- Weights: 1 to 3 points per part; the heavy parts are "write the equations of motion" (2 to 3 pts) and "kinematics of P and Q" (2 to 3 pts).
- Fixed question ladder, repeated almost verbatim:
  1. Degrees of freedom / define bases (1 pt).
  2. Position, velocity, acceleration of each particle in the stated frame, with unit vectors defined first (1.5 to 3 pts).
  3. All forces: weight, spring, string tension, normal reaction, plus inertia forces if the analysis is in a moving frame (2 to 3 pts).
  4. Equations of motion, then a reduced set free of reactions by projecting on directions perpendicular to the constraint (2 to 3 pts).
  5. A first integral: mechanical energy (own or of the system, tension doing no net work), or angular momentum about an axis (1 to 2 pts).
  6. A particular case: equilibrium, horizontal circular motion, linearisation about equilibrium, reduction to quadratures, or "is the string ever compressed?" (1 to 2 pts).
- Conceptual traps that recur: the energy of one particle is not conserved when tension acts on it but the system energy is; reaction multipliers are eliminated by projecting on tangent vectors; centrifugal force is conservative in a uniformly rotating frame (adds a potential); a string cannot push (check T >= 0); the constraint force direction must be justified from the gradient.

## 3. Mechanism typology found in the papers

| Archetype | Papers |
| :--- | :--- |
| Two particles on a string through a hole or ring (plane + vertical line, spherical coordinates) | 2011, 2024 |
| Particle on a string wound on a rotating spool or cylinder (variable free length) | 2016, 2017 |
| Particle on a rotating curve or surface (cone, loop, ring, hoop), analysed in the rotating frame | 2018, 2019, finals 2011/2012 |
| Particle on a moving track (translating, h(t) given), engine force | 2015 |
| Particle on a fixed curve with spring and extra linear drag | 2013 |
| Skater towed by a vehicle on a circle, rotating frame, string/bar tension | 2011 |
| Finals: 1D potential V(x) true/false, Frenet frame of a 3D trajectory, damped forced oscillator, particle on a rotating planet | 2013 to 2019 |

Questions are symbolic (letters, no numbers) except for a few numeric checks (angle, ratio). Figures are mechanism sketches with the inertial frame and the moving basis drawn.

## 4. Gaps to confirm before writing the bank

1. The 2022 first partial is a scan: read it as an image.
2. Whether Midterm 1 also covers unit 6 (particle systems) is not shown: no papers use it, and `unit-06` has no slides.
3. Official duration and point split of Midterm 1 are not printed on any Midterm 1 paper (the 60 minutes is from the 2015 Quiz 2). `exam-blueprint.json` carries a provenance note until confirmed; 2013 prints no marks and 2011 has two problems.
4. Final-exam problems from the Midterm 1 scope (1D potentials, Frenet, forced oscillator, particle on a planet) still need a full read; only headers were skimmed.
