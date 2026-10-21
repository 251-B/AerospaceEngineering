# Lab 2: Particle on Oscillating Loop
**Course:** Mechanics Applied to Aerospace Engineering (UC3M)  
**Group:** LA  
**Authors:**  
- Aimar Álvarez Iglesias  
- Héctor Gonzalez Rodriguez  
- Santiago Hernández Bejarano  

---

## 1. Submission Package for Aula Global

As specified in the Laboratory Guidelines (Section 2, Deliverables), the official deliverable is:
- **`Group_LA_Alvarez_Gonzalez_Hernandez.zip`**

This ZIP contains:
1. `Report_LA_Alvarez_Gonzalez_Hernandez.pdf` (the 10-page report, cover included).
2. `code_LA_Alvarez_Gonzalez_Hernandez/main.m` (the MATLAB script, ready to run).
3. `trajectory_P.avi` (animation of the trajectory in the fixed frame, the optional extra of item 6).

---

## 2. Running the MATLAB Code

Run `main.m` in MATLAB from its folder:
```matlab
main
```
It takes about 2.5 minutes (most of it writing the video) and needs no input.

### Script characteristics
- Integrates only with **`ode45`**, with the state of item 4, `X = [phi; dphi]`, in `diffeq(t,X,g,w,R,A)`; the linearized equation of item 8 is `diffeqlin`.
- Forces, energies and the work of the wire (trapezoidal rule) are computed from the stored solution with the same equations as the report.
- Prints the numerical checks: `ddphi(0) = -g/R`, `Nr = -3mg` at the bottom, `E - E0 = W`, energy conservation for `A = 0`, the analytical criterion of item 7 against the numerical result, and the linear solution against its closed form.
- Saves `Fig_2.png` to `Fig_6.png` (Figures 2 to 6 of the report; Figure 1 is the TikZ sketch) and `trajectory_P.avi`.
- Item 8 initial conditions: the statement gives none, so the particle starts at rest at the bottom, `delta(0) = 0`, `ddelta(0) = 0` (stated in the report, Section 2.5).

---

## 3. Report Summary (`Report_LA_Alvarez_Gonzalez_Hernandez.pdf`)

- **Length:** 10 pages including the cover (limit: 10).
- **Source:** `latex_source/report.tex` (same template as Lab 1), figures in `latex_source/figures/`.
- **Structure:**
  - 1 Introduction (problem, aims, plan of the report).
  - 2 Methodology: kinematics and degree of freedom (rotation matrix, all cross products), forces and equation of motion, mechanical energy, criterion to go over the top of a fixed loop, linearized equation with its closed-form solution, numerical method.
  - 3 Results: oscillating loop (angle, reactions, inertia forces), energy, trajectory and animation, phase portrait, linearized vs full equation; each discussed next to its figure.
  - 4 Discussion and 5 Conclusions.
