# Lab 1: Particle Connected to a Spool
**Course:** Mechanics Applied to Aerospace Engineering (UC3M)  
**Group:** LA  
**Authors:**  
- Aimar Álvarez Iglesias  
- Héctor Gonzalez Rodriguez  
- Santiago Hernández Bejarano  

---

## 1. Submission Package for Aula Global

As specified in Section 3.5 of the Laboratory Guidelines, the official deliverable is:
- **`Group_LA_Alvarez_Gonzalez_Hernandez.zip`**

This ZIP contains:
1. `Report_LA_Alvarez_Gonzalez_Hernandez.pdf` (The 9-page academic report in official UC3M format).
2. `code_LA_Alvarez_Gonzalez_Hernandez/main.m` (The MATLAB script ready to run).

---

## 2. Running the MATLAB Code

Simply run `main.m` in MATLAB:
```matlab
main
```

### Script Characteristics:
- Strictly and exclusively uses **`ode45`** for numerical integration (first-order state system).
- Work done by the spool ($W = \int a\omega T\,\mathrm{d}t$) is integrated directly as the 3rd state variable inside `diffeq`.
- Collision ($\xi = 0$) and slack string ($T = 0$) conditions are handled cleanly via event detection in `stopfun`.
- Automatically pops up all 4 figures on screen with LaTeX formatting:
  - **Figure 1:** 5x3 grid of $\phi(t)$, $\xi(t)$, and $T(t)$ across Cases 1--5.
  - **Figure 2:** Trajectories of the particle $P$ in the $Oxy$ plane with the spool circle.
  - **Figure 3:** Mechanical energy $E(t)$ and numerical conservation drift ($|E-E_0|/|E_0| < 10^{-9}$).
  - **Figure 4:** Case 3 asymptotic angular velocity singularity ($\propto (t_f - t)^{-1/2}$) and Case 5 work-energy balance ($E - E_0 = W$).

---

## 3. Report Summary (`Report_LA_Alvarez_Gonzalez_Hernandez.pdf`)

- **Total length:** Exactly 9 pages (respecting the strict $\le 10$ page limit).
- **Page Layout & Flow:**
  - **Page 1:** Official UC3M Cover Page with Department header, logo, title, and authors.
  - **Page 2:** Table of Contents (synchronized page numbers).
  - **Page 3:** Section 1 (Introduction) + Section 2 (Methodology: 2.1 Geometry & Degrees of Freedom) + Figure 1 (TikZ sketch).
  - **Page 4:** 2.1 continued (Velocity & Acceleration) + 2.2 (Forces & Equations of Motion) + 2.3 (Mechanical Energy).
  - **Page 5:** 2.4 (Numerical Method & Table 1) + Section 3 (Results: 3.1 Case 1 & 3.2 Case 2).
  - **Page 6:** Figure 2 (State Grid) + 3.3 (Case 3 Singularity & Collision) + 3.4 (Case 4 String Slackening).
  - **Page 7:** Figure 3 (Trajectories) + 3.5 (Case 5 Rotary Winding) + 3.6 (Energy Conservation & Work).
  - **Page 8:** Figure 4 (Energy Evolution & Drift) + Section 4 (Discussion: Ballistic Flight Modeling with `ode45`).
  - **Page 9:** Figure 5 (Singularity Slope & Work Check) + Section 5 (Conclusions) + References.
