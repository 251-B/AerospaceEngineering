---
subject: "Repository"
tags:
  - repository
  - tool
  - web
  - engineering-mechanics
source: "assets/js/mechanics-3d-sim.js"
---

# Tool - mechanics-3d-sim

## Purpose

Geometry simulator of the Engineering Mechanics problem cards: `assets/js/mechanics-3d-sim.js` and `assets/css/mechanics-3d-sim.css`. It follows the rule "Exercise simulators (SVG only)" of [[Rules - AGENTS.md]]: inline SVG inside the problem card, no canvas, no WebGL, no storage, controls hidden in print (the PDF shows the default view), every text in the page's own text colour. Related: [[Tool - build_mech_problems]], [[Rules - EM Mission Progress]].

One figure with the view box 760 by 360:

- **Left, orbitable axonometric view.** Camera azimuth and elevation by dragging, arrow keys or two sliders, and five quick views: `3D Isometric`, `Top XY`, `Front XZ`, `Side YZ`, `Plane normal to ω` (the camera looks along the active rotation axis). World axes: i0 = x, j0 = y, k0 = z (up).
- **Right, fold-down view.** The plane normal to the active rotation axis, with the symbol of the axis (out of or into the paper), the fixed pair of axes in grey, the rotated pair in blue, the arc of the angle, the shaded right triangle (L cos, L sin) and the live matrix (columns: the rotated unit vectors written in the fixed basis, the matrix written [0R1] in `Notes.pdf`, chapter 1).

## How a problem connects to it

In the solution of the problem (Solution Set note), where the simulator must appear:

```
> [!example] Interactive simulator
> sim: {"archetype": "rb-rolling-contact", "params": {"surface": "plane", "r": 0.3, "beta": 20}, "defaults": {"s": 0.5}, "readouts": [{"label": "Spin angle", "expr": "deg(-s/r)", "unit": "deg", "digits": 1}]}
```

The JSON object is on one line. Keys:

| Key | Meaning |
| :--- | :--- |
| `archetype` | one of the eight names below |
| `params` | constants of the problem (numbers in SI units, or the option words of the archetype); anything left out takes the default of the archetype |
| `defaults` | initial value of each slider, by slider id; angles in degrees. **The default state must be the configuration drawn or stated in the problem** |
| `sliders` | optional, per slider id: `min`, `max`, `step`, `label` |
| `readouts` | optional list of `{label, expr, unit, digits}`: **the formulas of the solution**, written as arithmetic over the variables below |
| `vectors` | optional list of `{label, at: [x, y, z], comp: [x, y, z], scale, cls}`: extra arrows (forces, reactions); every entry of `at` and `comp` is an expression string in world axes; `cls` is `m3-w` (pink, forces), `m3-v` (green), `m3-acc` (orange) or `m3-b1` (blue) |
| `view` | optional initial view: `iso`, `top`, `front`, `side` |
| `title`, `intro` | optional texts of the simulator |

Expressions: numbers, `+ - * / ^`, parentheses, `pi`, the functions `sin cos tan asin acos atan atan2 sqrt abs exp log min max pow sign deg rad` (`deg(x)` turns radians into degrees) and the variables: every numeric `param`, every slider id (angles in **radians**) and the variables of the archetype. Anything else gives no value; nothing is evaluated as code. Symbolic problems (no numbers in the statement) use unit values (1 m, 1 kg, 1 rad/s) and say so in the label, e.g. `"label": "v / (R Omega)"`.

## Archetypes

Sliders are given as `id (meaning, range)`; "vars" are the variables an expression can use besides params and sliders.

### `curvilinear-3d`: particle on a space curve

- params: `curve` = `helix` (R, b: z = b θ) | `circle` (R) | `ellipse` (a, b) | `spiral` (ρ = a + c θ) | `logspiral` (ρ = a e^{cθ}) | `conical` (ρ = c θ, z = b θ) | `cardioid` (ρ = a(1 + cos θ)) | `cycloid` (R, in the plane xz) | `parabola` (z = k x², plane xz) | `sine` (z = a sin(k x), plane xz) | `astroid` (x = a cos³θ, y = a sin³θ) | `line` (x0, y0, z0, vx, vy, vz) | `projectile` (v0, elev in degrees, g); `rate` (du/dt, default 1), `accel` (d²u/dt², default 0), `umin`, `umax` (range of the parameter: degrees for angular curves, metres or seconds for `parabola`, `sine`, `line`, `projectile`), `extent` (half-size of the view in metres).
- slider: `u` (the parameter: angle θ, abscissa x or time t).
- drawn: fixed basis, path, r, intrinsic basis (e_t, e_n, e_b), cylindrical basis (e_ρ, e_θ) and its triangle.
- vars: `u, x, y, z, rho, theta, v, at, an, rhoc`.

### `rotating-wire-groove`: particle on a wire fixed to a frame turning about k0

- params: `wire` = `line` (through the axis, elevation `beta` degrees, height `hgt`) | `horizontal` (arm at height `hgt`) | `hoop` (circle of radius R in the rotating vertical plane, centre at distance `e` from the axis and height `hgt`; θ measured from the lowest point) | `parabola` (z = k ρ²) | `chord` (horizontal groove at distance `d` from the axis); `Omega` (spin rate), `qdot` (rate of the coordinate), `qmin`, `qmax`, `extent`.
- sliders: `psi` (frame angle Ωt, degrees), `q` (coordinate along the wire in metres; for `hoop` the angle θ in degrees).
- drawn: B0, B1, wire, r, relative velocity, drag velocity, Coriolis acceleration, the triangle of the horizontal projection.
- vars: `psi, q, rho, x1, y1, z1, x, y, z, vrel, vdrag, acor`.

### `oscillator-phase`: oscillator and its rotating phasor

- params: `mode` = `free` | `forced`; `wn` (natural frequency), `zeta`, `r` (ω/ω_n), `x0`, `v0`, `delta` (static deflection F0/k), `tmax`, `extent`.
- sliders: `t`, `zeta`, and `r` when forced.
- drawn: spring and mass, the trace x(t), the phasor (A or X) with its projection.
- vars: `t, zeta, r, x, wd, A, M, psi, X`.

### `rb-euler-kinematics`: rigid body with Euler angles

- params: `sequence` = `313` (precession, nutation, spin) | `321` (yaw, pitch, roll); `shape` = `box` (a, b, c) | `plate` (a, b) | `disk` (R) | `cylinder` (R, h) | `cone` (R, h) | `sphere` (R) | `rod` (L); `psidot`, `thetadot`, `phidot` (rates); `px, py, pz` (a body point Q); `extent`.
- sliders: `psi`, `theta`, `phi` (degrees).
- drawn: B0, the body basis B3, the line of nodes, the body, ω, the instantaneous axis of rotation, the velocity of Q. The rotation selector shows each elementary rotation and its matrix.
- vars: `psi, theta, phi, w, wx, wy, wz` (ω in B0), `w1, w2, w3` (ω in the body basis), `vQ`.

### `rb-inertia-principal`: inertia tensor, rotation of axes, Steiner, principal axes

- params: `shape` = `rod` (L, along x) | `plate` (a along x, b along y) | `disk` (R) | `cylinder` (R, h, axis z) | `cone` (R, h, axis z) | `sphere` (R) | `shell` (R) | `box` (a, b, c) | `rects` (thin plate made of rectangles: `"rects": [[x, y, w, h], ...]`, lower-left corner and size; letters T, I, C, L); or `tensor` (a 3 by 3 array computed in the solution); `m`; `dx, dy, dz` (vector from the reference point O to... the centre of mass is drawn at −(dx, dy, dz): the tensor is taken about the point displaced (dx, dy, dz) from G); `axis` = `x` | `y` | `z` (axis of the rotation of axes); `extent`.
- slider: `alpha` (degrees).
- drawn: fixed and rotated axes, the body, G, the three principal axes.
- vars: `alpha, Ixx, Iyy, Izz, Ixy, Ixz, Iyz` (entries of the tensor in the rotated axes; the off-diagonal entries are minus the products of inertia), `I1, I2, I3` (principal moments, ascending), `alphap` (principal angle), `xG, yG, zG`.

### `rb-planar-dynamics`: planar body about a pivot (motion in the plane xy, k0 out of the paper)

- params: `shape` = `bar` (L) | `disk` (R) | `rect` (a, b) | `triangle` (legs a, b); `px, py` (pivot A in body axes with the origin at G; default: the end of the bar or the rim); `zero` = `down` | `up` | `horizontal` (direction of A→G when θ = 0); `thetadot`; `slide` (half-range in metres if the pivot slides along i0, 0 if fixed); `gx, gy` (direction of the weight, default (0, −1)); `extent`.
- sliders: `theta` (degrees), `x` (only with `slide`).
- drawn: B0, the body, its basis at G, r from A to G with its triangle, the velocity of G, the weight.
- vars: `theta, x, xG, yG, d, vG, thetadot`.

### `rb-rolling-contact`: body rolling on a plane or on a cylinder (plane xy)

- params: `surface` = `plane` (inclined `beta` degrees, positive s downhill) | `outer` (on a fixed cylinder of radius R) | `inner` (inside a cylinder of radius R); `shape` = `disk` | `hoop` | `sphere`; `r`; `e` (distance from the centre to the centre of mass, for a cavity or an eccentric mass); `sdot`; `slip` (1 frees the spin angle); `smin`, `smax`; `extent`.
- sliders: `s` (distance on the plane in metres, or the position angle θ in degrees on a cylinder), `phi` (only with `slip`).
- drawn: the surface, the body with a mark, contact point K, centre C, G, the velocity field about K. Rolling: r φ = −s (plane), r φ = (R + r) θ (outer), r φ = −(R − r) θ (inner).
- vars: `s, theta, phi, xC, yC, xG, yG, xK, yK, r, vC`.

### `rb-gyro-multibody`: rotor on an axle with precession, nutation and spin

- params: `L` (distance from the fixed point O to the centre of the rotor along the axle), `a` (radius of the rotor), `arm` (length of a horizontal arm that carries the pivot, 0 for none), `floor` (1: the rim touches the floor, as in a coin or disk rolling on the ground), `psidot`, `thetadot`, `phidot`, `I3`, `I1` (axial and transverse moments, in any common unit), `extent`.
- sliders: `psi`, `theta`, `phi` (degrees; sequence 3-1-3).
- drawn: B0, the basis B2 of the axle, the rotor, ω, the instantaneous axis, the angular momentum H, the triangle of the axle.
- vars: `psi, theta, phi, w, w3, wt, H, xG, yG, zG`.

## Choosing an archetype

| Problem | Archetype |
| :--- | :--- |
| Particle on a given trajectory, intrinsic or cylindrical coordinates, central force orbit | `curvilinear-3d` |
| Particle on a wire, groove, hoop or arm that turns; relative motion | `rotating-wire-groove` |
| Small oscillations, linearized equilibrium, forced or damped oscillation | `oscillator-phase` |
| Angular velocity from Euler angles, velocity field, instantaneous axis | `rb-euler-kinematics` |
| Moments and products of inertia, Steiner, principal axes | `rb-inertia-principal` |
| Plate, bar or disk moving in a plane about a pivot or hanging from a point | `rb-planar-dynamics` |
| Disk, hoop, sphere or cylinder that rolls (with or without slip) | `rb-rolling-contact` |
| Top, gyroscope, rotor on a fork or arm, coin on the floor, spacecraft with a wheel | `rb-gyro-multibody` |

A problem takes the archetype closest to its geometry; the readouts carry what is specific to it.

## Tests

`tools/tests/test_mechanics_sim.py` with the harness `tools/tests/mechanics_sim_harness.html`: every archetype renders, the matrices stay orthonormal after every control is moved, the default state equals the configuration, the readout parser only does arithmetic, nothing is written to storage, no canvas, and every text is AAA under the six reading palettes.
