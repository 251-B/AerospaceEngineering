---
subject: Mechanics Applied to Aerospace Engineering
topic: Laboratory 1 - Particle Connected to a Spool
course_code: "251-14165"
tags:
  - laboratory
  - numerical-methods
  - ode45
  - event-detection
  - kinematics
  - rheonomic
  - energy-conservation
difficulty: hard
sources:
  - "[[mechanics_labs.pdf]]"
  - "[[Lab1_notes.pptx]]"
  - "AnaliticSolutionLab1Mech2ndTry.pdf"
---

# 🌀 Laboratory 1: Particle Connected to a Spool

> **Primary Course Reference:** *Mechanics Applied to Aerospace Engineering (MAAE) — UC3M*  
> **Source Documents:** [[mechanics_labs.pdf]] (pp. 14–16) | [[Lab1_notes.pptx]] | `AnaliticSolutionLab1Mech2ndTry.pdf` (official handwritten derivation)  
> **Theoretical Prerequisites:** [[Topic 1 - Fundamentals and Particle Kinematics]], [[Topic 2 - Point Particle Dynamics]], [[Topic 3 - Constraints and Reaction Forces]]  
> **Navigation:** [[Lab - Guidelines and Scientific Report Standards|Guidelines]] | [[Engineering Mechanics MOC|⬅️ Mechanics MOC]]

---

## 📌 1. Physical System Description

A heavy particle $P$ of mass $m$ hangs from a thin, massless, inextensible string of total length $l$. The other end of the string is anchored at a point $A$ of a cylindrical spool of radius $a$ and centre $O$, which rotates counterclockwise at a constant rate $\omega$ (`mechanics_labs.pdf`, p. 14).

* $B$: tangency point between the straight segment $BP$ and the spool, at angle $\phi$ from $Ox$.
* $\xi$: length of the straight (unspooled) segment $BP$.
* The wrapped part of the string runs from $B$ **counterclockwise** to the anchor $A$; the free segment leaves $B$ along $-\hat e_\phi$.
* Gravity: $\vec g = -g\,\hat\jmath$.

---

## 🧮 2. Kinematic Formulation

### 2.1 Degrees of Freedom & Constraint (item 1)
The wrapped arc $BA$ has length $a(\theta_A - \phi)$ with $\theta_A(t) = \theta_{A0} + \omega t$. Inextensibility, $a(\theta_A - \phi) + \xi = l$, gives (handwritten solution, "constraint"):
$$\xi(t,\phi) = \xi_0 - a(\omega t - \phi), \qquad \dot\xi = a\dot\phi - a\omega$$
* $\phi$ increasing (B moves CCW) **unwinds** string; the spool rotating CCW **winds** it.
* Holonomic and rheonomic (explicit $t$). **C.D.O.F. $= 2 - 1 = 1$**, parametrised by $\phi$.

### 2.2 Basis and change-of-basis matrix
$$\hat e_r = \cos\phi\,\hat\imath + \sin\phi\,\hat\jmath, \qquad \hat e_\phi = -\sin\phi\,\hat\imath + \cos\phi\,\hat\jmath$$
$$\begin{pmatrix}\hat e_r\\ \hat e_\phi\end{pmatrix} = \begin{pmatrix}\cos\phi & \sin\phi\\ -\sin\phi & \cos\phi\end{pmatrix}\begin{pmatrix}\hat\imath\\ \hat\jmath\end{pmatrix}, \qquad \det R = 1,\; RR^T = I$$
Chain rule: $\dot{\hat e}_r = \frac{d\hat e_r}{d\phi}\dot\phi = \dot\phi\,\hat e_\phi$, $\quad \dot{\hat e}_\phi = -\dot\phi\,\hat e_r$.

### 2.3 Position, Velocity, Acceleration (item 2)
$$\vec r_P = a\hat e_r - \xi\hat e_\phi \;\Longleftrightarrow\; x_P = a\cos\phi + \xi\sin\phi,\quad y_P = a\sin\phi - \xi\cos\phi$$
$$\vec v_P = a\dot\phi\,\hat e_\phi - (a\dot\phi - a\omega)\hat e_\phi + \xi\dot\phi\,\hat e_r = \boxed{\xi\dot\phi\,\hat e_r + a\omega\,\hat e_\phi}$$
(the $a\dot\phi\,\hat e_\phi$ terms cancel; $a\omega$ is the reel-in speed along the string).
$$\vec a_P = (\dot\xi\dot\phi + \xi\ddot\phi)\hat e_r + \xi\dot\phi^2\hat e_\phi - a\omega\dot\phi\,\hat e_r = \boxed{\left(a\dot\phi^2 + \xi\ddot\phi - 2a\omega\dot\phi\right)\hat e_r + \xi\dot\phi^2\,\hat e_\phi}$$

---

## ⚖️ 3. Forces & Equations of Motion

### 3.1 Forces (item 3)
$$\vec T = T\,\hat e_\phi \;(T \ge 0), \qquad m\vec g = -mg\,\hat\jmath = -mg\left(\sin\phi\,\hat e_r + \cos\phi\,\hat e_\phi\right)$$

### 3.2 Newton's law projected (item 4)
$$\hat e_r:\; m\left(a\dot\phi^2 + \xi\ddot\phi - 2a\omega\dot\phi\right) = -mg\sin\phi \qquad \hat e_\phi:\; m\xi\dot\phi^2 = T - mg\cos\phi$$
$$\boxed{\ddot\phi = \frac{-g\sin\phi - a\dot\phi^2 + 2a\omega\dot\phi}{\xi_0 - a(\omega t - \phi)}} \qquad \boxed{T = m\xi\dot\phi^2 + mg\cos\phi}$$
Dimensional check: numerator in m/s², divided by m → s⁻² ✓; $m\xi\dot\phi^2$ in N ✓.

---

## ⚙️ 4. State-Space Formulation & Event Detection (`ode45`)

$$\vec X = [\phi,\ \dot\phi]^T, \qquad \dot{\vec X} = \begin{bmatrix} X_2 \\ \dfrac{-g\sin X_1 - aX_2^2 + 2a\omega X_2}{\xi_0 - a(\omega t - X_1)} \end{bmatrix}$$

```matlab
function [value, isterminal, direction] = stopfun(t, X, g, omega, a, xi0, m, xi_tol)
    xi = xi0 - a*(omega*t - X(1));
    T  = m*xi*X(2)^2 + m*g*cos(X(1));
    value      = [xi - xi_tol; T];   % spool contact / slack string
    isterminal = [1; 1];
    direction  = [-1; -1];
end
```
* `xi_tol = 1e-6` m is needed: near contact $\xi \simeq \sqrt{2av_c(t_c - t)}$ (infinite slope), so `ode45` cannot step onto $\xi = 0$ and aborts without firing the event if `xi_tol = 0`.
* Initial condition: $\dot x_P(0) = \xi_0\dot\phi_0$ at $\phi_0 = 0$ ⇒ $\dot\phi_0 = \dot x_P(0)/\xi_0$; $\dot y_P(0) = a\omega$ is imposed by the spool.

---

## 📊 5. Study Cases & Validated Results

Parameters: $g = 9.81$ m/s², $m = 0.1$ kg, $a = 0.2$ m, $\phi(0) = 0$, $\xi(0) = 1$ m. `RelTol = AbsTol = 1e-8`.

| Case | $\omega$ (rad/s) | $\dot x_P(0)$ (m/s) | $E_0$ (J) | End | Outcome |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | 0.1 | 0 | −0.98098 | $\xi = 0$ at 50.00 s, $P = (0.2, 0)$ | Exact winch solution $\phi \equiv 0$, $T = mg$, $E = E_0 + mga\omega t$ |
| **2** | 0 | −1 | −0.93100 | none (10 s simulated) | Pendulum with variable length $\xi = 1 + 0.2\phi \in [0.934, 1.063]$ m, period 2.018 s |
| **3** | 0 | −10 | 4.01900 | $\xi = 0$ at 0.270947 s, $P = (0.0567, 0.1918)$ m | Wraps 5 rad; $\dot\phi \simeq -v_c/\xi$, $v_c = 8.753$ m/s |
| **4** | 0 | +4 | −0.18100 | $T = 0$ at 1.69347 s, $P = (-0.6858, -0.1897)$ m | Slack on the **left** swing, just above the horizontal through $B$ |
| **5** | 0.1 | +1 | −0.93098 | $\xi = 0$ at 35.509 s, $P = (0.0243, -0.1985)$ m | Oscillation + winding; $\min T = 0.455$ N > 0 |

---

## 🔍 6. Answers & Critical Discussion

### Mechanical energy (item 9)
$$E = \tfrac12 m(\xi^2\dot\phi^2 + a^2\omega^2) + mg(a\sin\phi - \xi\cos\phi), \qquad \frac{dE}{dt} = \vec T\cdot\vec v_P = Ta\omega$$
* Conserved **iff** $\omega = 0$ (cases 2–4): $\vec T \perp \vec v_P$.
* Strictly increasing for $\omega > 0$ (cases 1, 5): the spool reels the string in at speed $a\omega$ against $T > 0$.

### Critical events (item 10)
* **Case 3:** $|\vec v_P| = \xi|\dot\phi|$ stays bounded (energy conservation) ⇒ $\dot\phi = \mathcal O(1/\xi)$, $T \simeq mv_c^2/\xi$, both diverge; $\phi$ reaches the finite value $-\xi_0/a = -5$ rad.
* **Case 4:** $T = 0$ needs $\cos\phi < 0$ (segment $BP$ above the horizontal through $B$). On the right swing $\phi_{max} = 1.267$ rad $< \pi/2$ ⇒ no slack; on the left, the wrapped string lowers $B$ to $y \simeq -0.2$ m and $P$ rises above it.
* **Case 5:** stops by spool contact, $\omega t - \phi = \xi_0/a = 5$ rad, reached 14.5 s earlier than the pure winch because a leftward swing wraps extra string.

### Transition after tension loss (item 11, discussion only: the guide asks what would change in the code, not to implement it)
1. Switch to 2-DoF free flight $\ddot x = 0$, $\ddot y = -g$ with a new state $[x_P, y_P, \dot x_P, \dot y_P]$ and a new derivative function.
2. Start the flight from $\vec r_P(t_s)$, $\vec v_P(t_s)$ (continuous at $t_s$).
3. New event: string taut again when $|\vec r_P - \vec r_B(\phi_s)| = \xi_s$ (with $\omega = 0$ the wrapped part does not move); a second event $|\vec r_P| = a$ detects contact with the spool.
4. At re-tension an impulse removes the velocity component along the string; restart `diffeq` + `stopfun` with $\dot\phi = \vec v_P\cdot\hat e_r/\xi$ and alternate the two models in a loop.

---

## 📁 7. Deliverables & Validated Code Repository

Location: `sources/cuatrimestre-1/03-engineering-mechanics/laboratorios/lab-1/Lab1-Ismael/deliverable/`
* `code_LB_Martin_Martin_Ranz/main.m`: single self-contained script (no user input; prints results, exports figures to `figures/`). Only what the guide asks for: integration of the 5 cases, one figure per case ($\phi$, $\xi$, $T$, trajectory), $E(t)$ for each case and $|\dot\phi|$ near contact in case 3. `diffeq`, `stopfun` and the plotting helpers are local functions at the end of the file, as in the professor's `example1.m`.
* `Overleaf_Lab1_ReportFinished.zip`: Overleaf project for the report (`main.tex`, `references.bib`, `figures/`, `exercise.jpeg`).
