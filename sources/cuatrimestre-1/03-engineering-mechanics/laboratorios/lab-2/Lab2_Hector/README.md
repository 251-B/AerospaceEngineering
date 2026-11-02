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
- Forces and energies are computed from the stored solution with the same equations as the report.
- Prints the numerical checks: `ddphi(0) = -g/R`, `Nr = -3mg` at the bottom, energy conservation for `A = 0`, the analytical criterion of item 7 against the numerical result, the periods of the closed curves of the fixed loop, and the linear solution against its exact solution.
- Saves `Fig_2.png` to `Fig_7.png` (Figures 2 to 7 of the report; Figure 1 is the TikZ sketch) and `trajectory_P.avi`. The figures plot what items 5 to 8 ask for, plus a zoom of the first 10 s for the angle, the radial reaction and the energies (over 3T the 79 swings look like a solid band), following the plotting rules of the Laboratory Guidelines: magnitude and units on every axis, Script 6 style, one panel per magnitude when sizes differ by orders of magnitude, and a logarithmic axis for the percentage error of item 8. They are drawn at their printed size (17 cm wide) and exported at 600 dpi with `exportgraphics`. The animation is recorded with `getframe`, as the guidelines suggest; a frame of a different size is skipped instead of stopping the script.
- Item 8 initial conditions: the statement gives none, so the particle starts at rest at the bottom, `delta(0) = 0`, `deltadot(0) = 0` (stated in the report, Section 2.5).

---

## 3. Report Summary (`Report_LA_Alvarez_Gonzalez_Hernandez.pdf`)

- **Length:** 10 pages including the cover (limit: 10).
- **Source:** `latex_source/human.tex` (same template as Lab 1), figures in `latex_source/figures/`.
- **Structure:**
  - 1 Introduction (problem, aims, plan of the report).
  - 2 Methodology: kinematics and degree of freedom (rotation matrix, all cross products), forces and equation of motion, mechanical energy, criterion to go over the top of a fixed loop, linearized equation with its exact solution, numerical method.
  - 3 Results: oscillating loop (angle, reactions, inertia forces), energy, trajectory and animation, phase portrait, linearized vs full equation; each discussed next to its figure.
  - 4 Discussion and 5 Conclusions.
