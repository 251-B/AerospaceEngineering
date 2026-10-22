---
materia: "Advanced Mathematics"
tema: "Tema 1: Introduction, Modeling and Classification of ODEs"
tags:
  - guia-tema
  - bloque-1
  - edos
  - modelado
  - clasificacion
dificultad: media
fuentes:
  - "Notes.pdf (class notes 'Diff Eq', p. 2), sources/cuatrimestre-1/04-advanced-maths/teoria/Notes.pdf"
  - "Robinson (2004), An Introduction to Ordinary Differential Equations, Ch. 3, Sec. 5.3, Ch. 8"
  - "definition_linear_ODE.pdf (lecture note, Sep 9)"
  - "ProblemsCh1.pdf (Department of Mathematics, UC3M)"
---

# Topic 1: Introduction, Modeling and Classification of ODEs

> **Key takeaway:** a differential equation is an equation for an unknown function and its derivatives. We classify it (ODE or PDE, order, linear or nonlinear, single equation or system) and meet the first two models of the course: exponential population growth or decay, and free fall under Newton's second law.

This note follows page 2 of the class notes (`Notes.pdf`) item by item and in the same order. Robinson (2004) is used to formalise and extend each step; anything that is not in the class notes is labelled **Complement (Robinson)** or **extension**. The web page is `subjects/advanced-maths/teoria/topic-1.html`, sections 1 to 6.

---

## 1. Differential equations, ODEs and PDEs [Notes, p. 2; Robinson, Sec. 3.1, pp. 11-12]

**Definition (class notes).** A *differential equation* is an equation involving an unknown function (of one or more independent variables) and its derivatives.

- **ODE.** A differential equation in which the unknown function depends on **only one** independent variable. Example from the notes:
  $$x'(t) = x(t),$$
  where $x$ is the dependent variable and $t$ the independent one. The function $x(t) = e^t$ is a solution, because $\frac{d}{dt}e^t = e^t$.
- **PDE.** A differential equation in which the unknown function depends on **more than one** variable. Example from the notes, the heat equation for $u(x,t)$:
  $$\frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2}.$$
  (The notes write the derivatives with $d$; with two independent variables they are partial derivatives.)

**Complement (Robinson).** Robinson's examples: $dy/dx = f(x)$, Newton's law $m\ddot{\mathbf x} = \mathbf f(t)$, the Schrodinger equation (ODEs), the heat equation and the Navier-Stokes equations (PDEs), Eqs. (3.1)-(3.3), p. 12. Robinson writes $\dot z = dz/dt$ and $y' = dy/dx$; the class notes use primes for time derivatives too ($x'(t)$).

## 2. Order [Notes, p. 2; Robinson, Sec. 3.2, p. 13]

The **order** of an ODE is the order of the highest derivative in it. $x' = x$ is first order, the heat equation is second order in $x$, Newton's law $m\ddot y = F$ is second order. Formally an $n$th-order ODE is $F(y^{(n)}, \dots, y', y, t) = 0$ with $y^{(n)}$ really present (Robinson Eq. 3.4).

The definition of an **autonomous** equation ($t$ absent from the right-hand side) appears in the class notes on p. 3, with the stability of first-order equations; see [[04 - Advanced Maths/Topic 2 - First-Order ODEs and Qualitative Dynamics|Topic 2]].

## 3. Linear and nonlinear ODEs [Notes, p. 2; definition_linear_ODE.pdf; Robinson, Sec. 3.3, p. 14]

### 3.1 The linear form

The margin of p. 2 gives the form of a linear ODE of order $n$:
$$a_0(x)\,y^{(n)}(x) + a_1(x)\,y^{(n-1)}(x) + \dots + a_n(x)\,y(x) = b(x). \tag{L}$$
The coefficients $a_i$ and the right-hand side $b$ are functions of the independent variable only. The lecture note `definition_linear_ODE.pdf` writes the same form with the indices in the opposite order ($a_n$ multiplying $y^{(n)}$); Robinson writes it with $t$ and $f(t)$ (Eq. 3.5). The equation is **homogeneous** when $b \equiv 0$.

Writing $L[y] = a_0 y^{(n)} + a_1 y^{(n-1)} + \dots + a_n y$, the equation is $L[y] = b$.

### 3.2 The superposition criterion of the class notes

> **Criterion [Notes, p. 2].** Consider $u_1$ and $u_2$, two solutions of an ODE. The ODE is **linear** if, for all $\alpha, \beta \in \mathbb R$, the combination $\alpha u_1 + \beta u_2$ is also a solution. If not, the ODE is **nonlinear**.

> [!note] Scope of the criterion
> The property "every combination $\alpha u_1 + \beta u_2$ of solutions is a solution" is exactly the superposition principle of **homogeneous** linear equations. An inhomogeneous linear equation such as $x' - x = 1$ is of form (L) but fails the test as stated: with $\alpha = \beta = 0$ the zero function would have to be a solution, and $0 - 0 \neq 1$. For $b \not\equiv 0$ apply the test to the homogeneous part $L[y] = 0$. The two examples of the notes are tested exactly as written there.

### 3.3 Demonstration 1: a homogeneous linear equation passes the test

Let $L[u_1] = 0$ and $L[u_2] = 0$, and set $v = \alpha u_1 + \beta u_2$.

1. Differentiation is linear: for each $k$, $v^{(k)} = \frac{d^k}{dx^k}(\alpha u_1 + \beta u_2) = \alpha u_1^{(k)} + \beta u_2^{(k)}$.
2. Substitute into $L$ and regroup the sum:
$$L[v] = \sum_{j=0}^{n} a_j\big(\alpha u_1^{(n-j)} + \beta u_2^{(n-j)}\big) = \alpha\sum_{j=0}^{n} a_j u_1^{(n-j)} + \beta\sum_{j=0}^{n} a_j u_2^{(n-j)} = \alpha L[u_1] + \beta L[u_2] = \alpha\cdot 0 + \beta\cdot 0 = 0.$$

So $v$ is a solution for every $\alpha, \beta$.

**Example of the notes: $u' = u$.** Let $u_1' = u_1$ and $u_2' = u_2$, and call $u = \alpha u_1 + \beta u_2$. Then
$$u' = \alpha u_1' + \beta u_2' = \alpha u_1 + \beta u_2 = u,$$
so $u$ solves the equation: **linear**. In form (L): $n = 1$, $a_0 = 1$, $a_1 = -1$, $b = 0$.

### 3.4 Demonstration 2: $u'' = (u')^2 + 1$ fails the test

Let $u_1'' = (u_1')^2 + 1$ and $u_2'' = (u_2')^2 + 1$, and set $v = \alpha u_1 + \beta u_2$. By linearity of differentiation,
$$v' = \alpha u_1' + \beta u_2', \qquad v'' = \alpha u_1'' + \beta u_2''.$$
For $v$ to be a solution we need $v'' = (v')^2 + 1$.

- Left side, using the equations of $u_1$ and $u_2$:
$$v'' = \alpha\big((u_1')^2 + 1\big) + \beta\big((u_2')^2 + 1\big) = \alpha (u_1')^2 + \beta (u_2')^2 + \alpha + \beta.$$
- Right side, expanding the square $(a + b)^2 = a^2 + 2ab + b^2$:
$$(v')^2 + 1 = \alpha^2 (u_1')^2 + 2\alpha\beta\, u_1' u_2' + \beta^2 (u_2')^2 + 1.$$

The two sides do not agree for all $\alpha, \beta$: the left side has $\alpha$ where the right side has $\alpha^2$, $\beta$ where it has $\beta^2$, no cross term $2\alpha\beta\,u_1'u_2'$, and the constant $\alpha + \beta$ instead of $1$. The equation is **nonlinear** [Notes, p. 2].

**Extension: the failure is caused by the square, not by the "+1".** For an inhomogeneous linear equation, combinations with $\alpha + \beta = 1$ are still solutions. Here they are not. Put $\beta = 1 - \alpha$ and subtract the two sides:
$$v'' - \big((v')^2 + 1\big) = \alpha(1 - \alpha)(u_1')^2 + \beta(1 - \beta)(u_2')^2 - 2\alpha\beta\,u_1'u_2' = \alpha(1 - \alpha)\big(u_1' - u_2'\big)^2,$$
because $\beta(1 - \beta) = (1 - \alpha)\alpha$ and $2\alpha\beta = 2\alpha(1 - \alpha)$. This is non-zero whenever $0 < \alpha < 1$ and $u_1' \neq u_2'$. Explicit solutions exist: $w = u'$ satisfies $w' = w^2 + 1$, solved by $w = \tan(t + c)$ (since $\frac{d}{dt}\tan s = \sec^2 s = \tan^2 s + 1$), so $u = -\ln\cos(t + c) + d$. Take $u_1 = -\ln\cos t$ and $u_2 = -\ln\cos(t - \pi/4)$ on $-\pi/4 < t < \pi/2$ and $\alpha = \beta = \tfrac12$. At $t = 0$: $u_1' = 0$, $u_2' = -1$, $u_1'' = 1$, $u_2'' = 2$, so $v'' = \tfrac32$ while $(v')^2 + 1 = \tfrac14 + 1 = \tfrac54$. The difference $\tfrac14 = \tfrac12\cdot\tfrac12\cdot(0 - (-1))^2$ matches the formula.

### 3.5 Practical reading of form (L)

An equation is linear exactly when every term is either a function of the independent variable alone (it goes into $b$) or such a function times $y$ or one derivative $y^{(k)}$ to the first power. Powers such as $y^2$ or $(y')^2$, products such as $y\,y'$, and functions such as $\sin y$ make it nonlinear. Nonlinearity in the independent variable is irrelevant: $y' = 4y^2 + x^2$ is nonlinear because of $y^2$, not because of $x^2$ (third example of the Sep 9 lecture note).

**Complement (Robinson, Sec. 3.4).** What "solving" can mean: explicit, explicit with an integral, implicit, qualitative, numerical.

## 4. Systems of ODEs [Notes, p. 2; Robinson, Eq. 3.9 and Ch. 25]

**Definition (class notes).** A *system of ODEs* has two or more dependent variables (sharing one independent variable). Example of the notes:
$$\begin{cases} x'(t) = 2x(t) - y(t),\\ y'(t) = -x(t) + 3y(t). \end{cases}$$
It is first order, linear, homogeneous, with constant coefficients and autonomous. In matrix form $\begin{pmatrix}x\\y\end{pmatrix}' = \begin{pmatrix}2 & -1\\ -1 & 3\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}$. If $(x_1, y_1)$ and $(x_2, y_2)$ are solutions, so is $\alpha(x_1, y_1) + \beta(x_2, y_2)$: each right-hand side is a linear combination of $x$ and $y$, so the computation of 3.3 applies equation by equation.

**Preview of Topic 4 (Notes, p. 9): elimination.** From the first equation $y = 2x - x'$, so $y' = 2x' - x''$. Substituting both into the second equation:
$$2x' - x'' = -x + 3(2x - x') = 5x - 3x' \quad\Longrightarrow\quad x'' - 5x' + 5x = 0,$$
in agreement with the general rule $x'' - (a + d)x' + (ad - bc)x = 0$ for $a = 2$, $b = -1$, $c = -1$, $d = 3$ ($a + d = 5$, $ad - bc = 6 - 1 = 5$).

**Complement (Robinson, Eq. 3.9).** The nonlinear system $\dot x = x(4 - 2x - y)$, $\dot y = y(9 - 3x - 3y)$ of two competing species, with its four equilibria $(0,0)$, $(0,3)$, $(2,0)$, $(1,2)$ and its phase portrait (every solution with $x, y > 0$ tends to $(1,2)$).

## 5. Example 1: population growth and decay [Notes, p. 2; Robinson, Secs. 8.2-8.3]

**Model (class notes).** $x(t)$ is the population at time $t$, with $x(t) > 0$ for all $t$. The rate of change of $x$ is proportional to $x$ itself, with proportionality constant $k \in \mathbb R$:
$$x'(t) = k\,x(t), \qquad x(0) = x_0 > 0.$$
First order, linear (form (L) with $a_0 = 1$, $a_1 = -k$, $b = 0$). Robinson derives the same law from a birth-death balance, $\Delta x \approx (\beta - \delta)x\,\Delta t$, so $k = \beta - \delta$ (Sec. 8.3, Eq. 8.5). Units: $[k] = \text{s}^{-1}$ (per unit time), so $kt$ is dimensionless.

**Solution, route 1 (notes).** Divide by $x > 0$ and integrate from $0$ to $t$. On the left, substitute $u = x(\tau)$, $du = x'(\tau)\,d\tau$; the limits $\tau = 0$ and $\tau = t$ become $u = x_0$ and $u = x(t)$:
$$\int_0^t \frac{x'(\tau)}{x(\tau)}\,d\tau = \int_{x_0}^{x(t)} \frac{du}{u} = \big[\ln u\big]_{x_0}^{x(t)} = \ln x(t) - \ln x_0 = \ln\frac{x(t)}{x_0},$$
$$\int_0^t k\,d\tau = \big[k\tau\big]_0^t = kt - 0 = kt.$$
(The notes write this as $\frac{dx}{dt} = kx \Rightarrow \int_0^t \frac{dx}{x} = \int_0^t k\,dt$.)

**Solution, route 2 (notes).** Recognise the left-hand side as a derivative. By the chain rule, with $x(\tau) > 0$,
$$\frac{d}{d\tau}\ln\big(x(\tau)\big) = \frac{1}{x(\tau)}\,x'(\tau),$$
so by Barrow's rule
$$\int_0^t \big(\ln x(\tau)\big)'\,d\tau = \ln x(t) - \ln x(0) = \int_0^t k\,d\tau = kt.$$

Both routes give $\ln\frac{x}{x_0} = kt$; exponentiating, $\frac{x}{x_0} = e^{kt}$ and
$$\boxed{x(t) = x_0\,e^{kt}}.$$
Check: $x'(t) = k x_0 e^{kt} = k\,x(t)$ and $x(0) = x_0 e^0 = x_0$.

**Discussion (notes).**
- $k > 0$: the population grows; $x(t) \to \infty$ as $t \to \infty$; doubling time $\ln 2/k$.
- $k < 0$: the population decays; $x(t) \to 0$ as $t \to \infty$; half-life $\ln 2/|k|$ (radioactive decay, [[04 - Advanced Maths/Problem - Ch1-P3 Plutonium 239 Radioactive Decay|Problem 1.3]]).
- $k = 0$: $x(t) \equiv x_0$.

"In reality, population doesn't grow exponentially forever, but reaches a flat max" [Notes, p. 2]: this motivates the **logistic correction** $x' = kx(1 - x/M)$, whose equilibria, stability and explicit solution are studied with the first-order methods of the class notes, p. 3 ([[04 - Advanced Maths/Concept - Logistic Equation and Carrying Capacity|Logistic Equation]]).

**Complement (Robinson, Sec. 8.2).** For a general start $x(t_0) = x_0$ of either sign, uniqueness shows that $x(t)$ never crosses $0$, and the same computation gives $x(t) = x_0 e^{k(t - t_0)}$. **Complement (Robinson, Sec. 8.3).** Census test of the model for Great Britain and Ireland (1801, 1851, 1901): $k = 0.01043\ \text{yr}^{-1}$ fits the first century but overestimates 2001 by a factor of two.

## 6. Example 2: Newton's second law, free fall [Notes, p. 2; Robinson, Sec. 5.3]

**Model (class notes).** Free fall of an object under gravity $g$, with $y(t)$ its height (axis pointing up). The only force is the weight $-mg$, so Newton's law $F = ma$ reads
$$-mg = m\,y''(t) \quad\Longrightarrow\quad \frac{d^2y}{dt^2} = -g,$$
a second-order linear ODE (form (L) with $a_0 = 1$, $a_1 = a_2 = 0$, $b = -g$). The mass cancels.

**Integration.** Integrate twice from $0$ to $t$, with the antiderivatives stated:
1. An antiderivative of $-g$ is $-g\tau$, so $y'(t) - y'(0) = \int_0^t (-g)\,d\tau = \big[-g\tau\big]_0^t = -gt$, i.e. $y'(t) = v_0 - gt$ with $v_0 = y'(0)$.
2. An antiderivative of $v_0 - g\tau$ is $v_0\tau - \tfrac12 g\tau^2$, so $y(t) - y(0) = \big[v_0\tau - \tfrac12 g\tau^2\big]_0^t = v_0t - \tfrac12 g t^2$.

General solution: $y(t) = y_0 + v_0 t - \tfrac12 g t^2$, with two constants $y_0 = y(0)$, $v_0 = y'(0)$, as expected for a second-order equation. The notes take the object released from rest at the origin ($y_0 = v_0 = 0$):
$$\boxed{y(t) = -\iint g\,dt\,dt = -\tfrac12 g t^2}.$$
Dimensions: $[g t^2] = \text{m s}^{-2}\cdot\text{s}^2 = \text{m}$.

**Complement (Robinson, Sec. 5.3 and Exercise 5.6).** $F = ma$ from the momentum balance $dp/dt = F$ with the product rule; release from height $h$: impact time $\sqrt{2h/g}$ and speed $\sqrt{2gh}$ (energy check $\tfrac12 m v^2 = mgh$); Example 5.4, a braking car; free fall with quadratic drag $m\dot v = mg - kv|v|$ (Sec. 7.5.2), terminal velocity $\sqrt{mg/k}$ and $v(t) = w_T\tanh(gt/w_T)$ (Exercise 8.6).

---

## 7. Initial value problems and Picard's theorem

In the class notes the IVP and Picard's theorem open p. 3, together with autonomous equations. See [[04 - Advanced Maths/Concept - Well-Posed Problems and Picard Theorem|Well-Posed Problems and Picard Theorem]] and [[04 - Advanced Maths/Topic 2 - First-Order ODEs and Qualitative Dynamics|Topic 2]].

## Concept notes

- [[04 - Advanced Maths/Concept - Linearity and Order of Differential Equations|Linearity and Order of Differential Equations]]
- [[04 - Advanced Maths/Concept - First-Order Physical Models|First-Order Physical Models]]
- [[04 - Advanced Maths/Concept - Logistic Equation and Carrying Capacity|Logistic Equation and Carrying Capacity]]
- [[04 - Advanced Maths/Concept - Well-Posed Problems and Picard Theorem|Well-Posed Problems and Picard Theorem]]
- [[04 - Advanced Maths/Concept - Navier-Stokes Poiseuille Flow Reduction|Navier-Stokes Poiseuille Flow Reduction]]

## Solved problems (ProblemsCh1.pdf)

| Problem | Title | Key result |
| :--- | :--- | :--- |
| [[04 - Advanced Maths/Problem - Ch1-P1 Classification of Differential Equations\|Problem 1.1]] | Classification of ODEs and PDEs | Linearity, order, variables |
| [[04 - Advanced Maths/Problem - Ch1-P2 Malthusian Population Dynamics\|Problem 1.2]] | Malthusian population dynamics | $x(t) = x_0e^{kt}$, doubling time $\ln 2/k$ |
| [[04 - Advanced Maths/Problem - Ch1-P3 Plutonium 239 Radioactive Decay\|Problem 1.3]] | Plutonium-239 decay | $k = \ln 2/24\,000\ \text{yr}^{-1}$ |
| [[04 - Advanced Maths/Problem - Ch1-P4 Newton Law of Cooling Modeling\|Problem 1.4]] | Newton's law of cooling | $\frac{dT}{dt} = -k(T - T_A(t))$ |
| [[04 - Advanced Maths/Problem - Ch1-P5 Forensic Time of Death Estimation\|Problem 1.5]] | Time of death | $k = \ln 1.4\ \text{h}^{-1}$ |
| [[04 - Advanced Maths/Problem - Ch1-P6 Saline Mixing Tank Dynamics\|Problem 1.6]] | Mixing tank | $x(t) = s + (0.01 - s)e^{-t/100}$ |
| [[04 - Advanced Maths/Problem - Ch1-P7 Free Fall Motion under Gravity\|Problem 1.7]] | Free fall | $y(t) = y_0 - \tfrac12 g t^2$ |
| [[04 - Advanced Maths/Problem - Ch1-P8 Simple Pendulum Equation of Motion\|Problem 1.8]] | Pendulum | $\ddot\theta + \frac{g}{l}\sin\theta = 0$ |
| [[04 - Advanced Maths/Problem - Ch1-P9 Logistic Population Growth Model\|Problem 1.9]] | Logistic growth | $p(t) = \frac{Mp_0}{p_0 + (M - p_0)e^{-k(t - t_0)}}$ |
| [[04 - Advanced Maths/Problem - Ch1-P10 Laminar Viscous Poiseuille Flow\|Problem 1.10]] | Poiseuille flow | $V(r) = \frac{P}{4}(a^2 - r^2)$ |

## Navigation

- [[04 - Advanced Maths/Advanced Maths MOC|Advanced Mathematics MOC]]
- [[00 - Indice Central/Master Index|Central Master Index]]
