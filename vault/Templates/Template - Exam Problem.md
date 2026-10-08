---
materia: ""
tema: ""
origen: "Final Exam January 2024" # Midterm / Problem sheet / Final Exam
dificultad: high # low | medium | high | challenge
tags:
  - exam-problem
  - solved
---

# ✏️ Problem: {{title}}

## 📄 Official Statement
> Complete, literal transcription of the statement, including dimensions, diagrams and imposed conditions. Cite the source page.

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Known Data (SI units):
* $ \rho = \dots\ [\mathrm{kg/m^3}] $
* $ v_1 = \dots\ [\mathrm{m/s}] $
* $ D = \dots\ [\mathrm{m}] $

### Unknowns:
1. $ p_2 = ? $
2. $ \dot{m} = ? $

### Justified Hypotheses:
* [x] Incompressible fluid.
* [x] Steady regime.
* [x] One-dimensional flow or section-averaged properties.

Count the degrees of freedom and the independent equations before computing anything.

---

## 🧠 2. Phase 2: Frames and Change of Basis
Define the reference frames and bases, and write the change-of-basis matrix $[{}_0R_1]$ when more than one basis is used (check $\det R = 1$ and $R R^T = I$). Then state, in words, why each tool is chosen before applying it:
1. Apply mass conservation between sections 1 and 2.
2. State the momentum equation or Bernoulli as appropriate.

---

## 🔢 3. Phase 3: Step-by-Step Derivation
No algebraic skips: show every chain rule $\frac{d}{dt}f(u) = \frac{df}{du}\dot{u}$, every substitution differential $du$, and the Barrow limits at both ends of each integral.

### Step 1: [Name of the step, e.g. Continuity]
$$ \dot{m} = \rho A_1 v_1 = \rho A_2 v_2 $$

Solving for $ v_2 $:
$$ v_2 = v_1 \frac{A_1}{A_2} = \dots $$

### Step 2: [Name of the step, e.g. Pressure Balance]
$$ p_1 + \frac{1}{2} \rho v_1^2 = p_2 + \frac{1}{2} \rho v_2^2 + \Delta p_{\mathrm{losses}} $$

---

## 🎯 4. Phase 4: Units and Limits
* **Numerical solution:** $ \mathbf{p_2 = 142.5\ \mathrm{kPa}} $
* **Unit check:** dimensional verification of every term.
* **Limiting cases:** does the result behave correctly as each parameter tends to $0$ or $\infty$?
* **Physical sense:** do the sign and the order of magnitude agree with physical intuition?
* **Official key:** compare with the official answer; if they differ, add a `> [!warning] Discrepancy with the official solution` callout and do not adjust data to match.
