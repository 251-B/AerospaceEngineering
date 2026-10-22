---
materia: "Advanced Maths"
tema: "Tema 3: Second-Order Linear ODEs General Theory and Constant Coefficients"
tags:
  - moc-tema
  - advanced-maths
  - segundo-curso
  - edos-segundo-orden
  - coeficientes-constantes
  - wronskiano
dificultad: media
fuentes:
  - "Notes.pdf (class notes 'Diff Eq', pp. 5-8), sources/cuatrimestre-1/04-advanced-maths/teoria/Notes.pdf"
  - "Robinson (2004), An Introduction to Ordinary Differential Equations, Ch. 11-18"
  - "Lecture schedule: Sep 22 - Oct 1"
---

# Topic 3: Second-Order Linear ODEs

> **Key takeaway:** the solutions of $x'' + p(t)x' + q(t)x = 0$ form a two-dimensional space, spanned by any two solutions with non-zero Wronskian. With constant coefficients they come from the roots of $k^2 + pk + q = 0$; an inhomogeneous equation adds one particular solution, found by an educated guess or by variation of constants.

This note follows pages 5 to 8 of the class notes (`Notes.pdf`) in their order. Robinson (2004) formalises and extends each step; material that is not in the notes is labelled **Complement (Robinson)**. Four slips of the notes are corrected with a check. The web page is `subjects/advanced-maths/teoria/topic-3.html`; sections 1-10 below match its sections.

---

## 1. Second-order linear ODEs [Notes, p. 5; Robinson, Sec. 11.1]

$$x''(t) + p(t)\,x'(t) + q(t)\,x(t) = f(t).$$
For a spring: $p$ is the friction, $q$ the spring constant and $f$ the forcing ($m x'' = -\mu x' - kx + F$ divided by $m$).

**Theorem [Notes, p. 5; Robinson, Thm 11.1].** Given $\ddot x = f(\dot x, x, t)$, if $f$, $\partial f/\partial x$, $\partial f/\partial\dot x$ are continuous in a cube $(a_1, a_2)\times(b_1, b_2)\times(t_1, t_2)$, the IVP $x(t_0) = x_0$, $\dot x(t_0) = y_0$ has a unique solution when $t_0 \in (t_1, t_2)$, $x_0 \in (a_1, a_2)$, $y_0 \in (b_1, b_2)$. (Complement, Robinson Sec. 11.1: two integrations of $\ddot x = f(t)$ show why two data are needed.)

## 2. Superposition, independence, general solution [Notes, p. 5; Robinson, Secs. 11.2-11.3]

- **Superposition:** if $x_1$, $x_2$ solve $x'' + px' + qx = 0$, so does $\alpha x_1 + \beta x_2$. Remark: $f = 0$ homogeneous, $f \neq 0$ inhomogeneous.
- **Linear independence:** $\alpha_1x_1 + \dots + \alpha_nx_n = 0$ on $I$ only for $\alpha_1 = \dots = \alpha_n = 0$.
- **Theorem:** every solution is $x = C_1x_1 + C_2x_2$ with $x_1$, $x_2$ independent solutions; Picard gives two such solutions.
- **Example of the notes:** matching $x(t_0) = x_0$, $x'(t_0) = y_0$ gives
$$\begin{pmatrix} x_1(t_0) & x_2(t_0) \\ x_1'(t_0) & x_2'(t_0)\end{pmatrix}\begin{pmatrix} C_1 \\ C_2\end{pmatrix} = \begin{pmatrix} x_0 \\ y_0\end{pmatrix},$$
solvable for all data only if the determinant (the Wronskian) is non-zero.

## 3. The Wronskian [Notes, p. 5; Robinson, Sec. 11.4, Ex. 11.2]

$W(x_1, x_2) = x_1x_2' - x_2x_1'$. Product rule: $W' = x_1x_2'' - x_2x_1''$. With $x_j'' = -px_j' - qx_j$:
$$W' = -p\,x_1x_2' + p\,x_2x_1' = -p\,W \quad\Longrightarrow\quad W(t) = Ce^{-\int p\,dt}.$$
So $W \equiv 0$ or $W$ never vanishes.

> [!warning] Discrepancy with the class notes (p. 5)
> The notes box $W' = p\,W$; their own previous line is $-p\,x_1x_2' + p\,x_2x_1' = -pW$, and their solution $W = Ce^{-\int p}$ solves $W' = -pW$. Check: $x'' + x' - 6x = 0$, $x_1 = e^{-3t}$, $x_2 = e^{2t}$: $W = 5e^{-t}$, $W' = -5e^{-t} = -W$.

**Complement (Robinson).** Wronskian test (non-zero at one point gives independence, for any differentiable functions); $t^2|t|$ and $t^3$ are independent with $W \equiv 0$ (Exercise 11.3).

## 4. Homogeneous equations with constant coefficients [Notes, p. 5; Robinson, Ch. 12]

$x = e^{kt}$ in $x'' + px' + qx = 0$ gives $(k^2 + pk + q)e^{kt} = 0$, so $k^2 + pk + q = 0$, $k = \frac{-p \pm \sqrt{p^2 - 4q}}{2}$.

| Case [Notes] | Roots | General solution | Wronskian |
| :--- | :--- | :--- | :--- |
| 01 | $k_1 \neq k_2$ real | $C_1e^{k_1t} + C_2e^{k_2t}$ | $(k_2 - k_1)e^{(k_1 + k_2)t}$ |
| 02 | $k = -p/2$ double | $C_1e^{kt} + C_2te^{kt}$ | $e^{2kt}$ |
| 03 | $\rho \pm \omega i$ | $e^{\rho t}(A\cos\omega t + B\sin\omega t)$ | $\omega e^{2\rho t}$ |

- Case 02 check: $(te^{kt})'' + p(te^{kt})' + qte^{kt} = [(k^2 + pk + q)t + (2k + p)]e^{kt} = 0$.
- Case 03 [Notes]: $\rho = -p/2$, $\omega = \sqrt{4q - p^2}/2$; $C_1e^{(\rho + \omega i)t} + C_2e^{(\rho - \omega i)t} = (C_1 + C_2)e^{\rho t}\cos\omega t + i(C_1 - C_2)e^{\rho t}\sin\omega t$ (Euler); with $C_1 = \tfrac12(A - iB)$, $C_2 = \overline{C_1}$ this is $e^{\rho t}(A\cos\omega t + B\sin\omega t)$.

**Complement (Robinson).** Examples 12.1, 12.3, 12.4; higher order (Sec. 16.1).

## 5. Complement: the mass-spring-damper [Robinson, Ch. 13]

$\ddot x + \lambda\dot x + \omega^2x = 0$: over-, critically and under-damped regimes; the Millennium Bridge; landing gear.

## 6. Inhomogeneous equations with constant coefficients [Notes, p. 6; Robinson, Ch. 14]

$x'' + px' + qx = f$: $x = x_H + x_N$. Proof: $\Phi = x - x_N$ gives $\Phi'' + p\Phi' + q\Phi = f - f = 0$, so $\Phi = x_H$ and $x = x_H + x_N$.

> [!warning] Discrepancy with the class notes (p. 6)
> The proof ends with $x = x_H - x_N$ (and writes $q(x - x_N')$ for $q(x - x_N)$). Solving $x_H = x - x_N$ gives $x = x_H + x_N$. Check with $f = 12$: $x = 2$ gives $-12 \neq 12$; $x = -2$ gives $12$.

**Educated guess [Notes, p. 6]:** polynomial of order $n$ $\to$ full polynomial; $Ce^{\alpha t}$ $\to$ $Ae^{\alpha t}$ (Case 1, $\alpha$ not a root) or $Ate^{\alpha t}$ (Case 2, $\alpha$ a root; $At^2e^{\alpha t}$ for a double root, Robinson Sec. 14.5); $\alpha\cos\omega t + \beta\sin\omega t$ $\to$ $A\cos\omega t + B\sin\omega t$, times $t$ if already in $x_H$; sums by decomposition; the same for higher order.

**Example [Notes, p. 6]:** $x'' + x' - 6x = f$. $k^2 + k - 6 = (k + 3)(k - 2)$, $x_H = C_1e^{-3t} + C_2e^{2t}$.
- $f = 12$: $x_N = C$, $-6C = 12$, $x_N = -2$.
- $f = 36t$: $x_N = a_1t + a_0$; $a_1 - 6(a_1t + a_0) = 36t$; $-6a_1 = 36 \Rightarrow a_1 = -6$; $a_1 - 6a_0 = 0 \Rightarrow a_0 = -1$; $x_N = -6t - 1$. (The notes write $6C_1t = 36t$; the coefficient is $-6C_1$, the value $-6$ is right.)
- $f = 4e^{-2t}$: $-2$ is not a root; $x_N = Ae^{-2t}$, $(4 - 2 - 6)A = 4$, $A = -1$, $x_N = -e^{-2t}$.
- Decomposition (portal check, not in the notes, which only state the rule): $f = 12 + 36t + 4e^{-2t}$ gives $x_N = -6t - 3 - e^{-2t}$.

**Complement (Robinson).** Guess table and rule of thumb (Sec. 14.5); Examples 14.4, 14.8, 14.10, 14.11.

## 7. Complement: forced vibrations and resonance [Robinson, Ch. 15]

Beats, resonance $x_p = \frac{a}{2\omega}t\sin\omega t$, damped response $R(\alpha) = a/\sqrt{(\omega^2 - \alpha^2)^2 + \lambda^2\alpha^2}$.

## 8. Variable coefficients: reduction of order [Notes, p. 7; Robinson, Ch. 17]

In general not all solutions can be found; two strategies. **Reduction of order:** knowing a solution $u$ of $x'' + px' + qx = 0$, set $x = yu$. Then $x' = y'u + yu'$, $x'' = y''u + 2y'u' + yu''$ and
$$\big[u'' + pu' + qu\big]y + \big[2u' + pu\big]y' + uy'' = 0,$$
the first bracket being $0$. With $z = y'$: $uz' + (2u' + pu)z = 0$, a first-order equation; the notes stop here. Complement (Robinson Ex. 17.7): it is separable, $z = Ae^{-\int p}/u^2$, $x_2 = u\int e^{-\int p}/u^2\,dt$ (Robinson Exercise 17.7). With $u = e^{kt}$ and a double root this gives $z = A$, $x = (At + B)e^{kt}$: Case 02.

**Complement (Robinson).** Examples 17.1 and 17.2 ($t^2\ddot x - 2t\dot x - 4x = 0$, $x_2 = t^4$).

## 9. Variation of constants [Notes, p. 8; Robinson, Ch. 18]

$x = u_1x_1 + u_2x_2$. $x' = u_1'x_1 + u_1x_1' + u_2'x_2 + u_2x_2'$. Impose $u_1'x_1 + u_2'x_2 = 0$, so $u_1' = -u_2'x_2/x_1$ $(\ast)$ and $x' = u_1x_1' + u_2x_2'$. Then $x'' = u_1'x_1' + u_1x_1'' + u_2'x_2' + u_2x_2''$; substituting, the brackets $x_j'' + px_j' + qx_j$ vanish and $u_1'x_1' + u_2'x_2' = f$. With $(\ast)$: $u_2'(x_1x_2' - x_2x_1')/x_1 = f$, so
$$u_2' = \frac{f\,x_1}{W}, \qquad u_1' = -\frac{f\,x_2}{W}, \qquad W = x_1x_2' - x_2x_1'.$$

> [!warning] Discrepancy with the class notes (p. 8)
> The notes write $u_1' = f x_2/W$ and $u_1 = \int x_2 f/W$ without the minus sign; $(\ast)$ gives $-fx_2/W$, as Robinson's (18.8). Check with $f = 12$, $x_1 = e^{-3t}$, $x_2 = e^{2t}$, $W = 5e^{-t}$: $u_1 = -\frac45e^{3t}$, $u_2 = -\frac65e^{-2t}$, $x_N = -\frac45 - \frac65 = -2$ (Section 6). With the notes' sign $x_N = -\frac25$, which gives $L[x_N] = \frac{12}{5} \neq 12$.

**Complement (Robinson).** Cramer's rule (no division by $x_1$); Examples 18.1 ($5e^{-3t}$, with the p. 166 erratum) and 18.2 ($\ddot x + x = \tan t$, $x_p = -\cos t\ln|\sec t + \tan t|$).

## 10. Summary

| Result | Notes | Robinson |
| :--- | :--- | :--- |
| Existence and uniqueness in a cube | p. 5 | Thm 11.1 |
| Superposition, $x = C_1x_1 + C_2x_2$ | p. 5 | Secs. 11.2-11.3 |
| Wronskian, $W' = -pW$ | p. 5 | Sec. 11.4 |
| Cases 01-03 | p. 5 | Ch. 12 |
| $x = x_H + x_N$, educated guess, $x'' + x' - 6x = f$ | p. 6 | Ch. 14 |
| Reduction of order | p. 7 | Ch. 17 |
| Variation of constants | p. 8 | Ch. 18 |

---

## Concept notes

1. [[04 - Advanced Maths/Concept - Existence and Uniqueness Theorem for Second-Order ODEs|Existence and Uniqueness Theorem for Second-Order ODEs]]
2. [[04 - Advanced Maths/Concept - Linear Operator and the Superposition Principle|Linear Operator and the Superposition Principle]]
3. [[04 - Advanced Maths/Concept - Linear Independence of Functions and the Wronskian Determinant|Linear Independence of Functions and the Wronskian Determinant]]
4. [[04 - Advanced Maths/Concept - Abel's Identity and Properties of the Wronskian|Abel's Identity and Properties of the Wronskian]]
5. [[04 - Advanced Maths/Concept - Homogeneous Equations with Constant Coefficients and the Characteristic Equation|Homogeneous Equations with Constant Coefficients and the Characteristic Equation]]

## Aerospace connections

- **Landing gear:** oleo-pneumatic struts are designed near critical damping (Case 02) to absorb the impact without rebound.
- **Flutter:** when aerodynamic forces reduce the effective damping, the wing moves from Case 03 with $\rho < 0$ to $\rho > 0$.
- **Attitude control:** $I\ddot\theta + c\dot\theta + k\theta = T_c(t)$, with gains chosen for a target damping ratio.

## Navigation

- [[04 - Advanced Maths/Advanced Maths MOC|Advanced Mathematics MOC]]
- Previous: [[04 - Advanced Maths/Topic 2 - First-Order ODEs and Qualitative Dynamics|Topic 2]]
- [[00 - Indice Central/Master Index|Central Master Index]]
