---
materia: "Advanced Maths"
tema: "Tema 2: First-Order ODEs and Qualitative Dynamics"
origen: "ProblemsCh2.pdf — Exercise 2.3"
dificultad: media
tags:
  - problema-resuelto
  - factor-integrante
  - edos-lineales
  - integracion-por-partes
  - comportamiento-asintotico
---

# ✏️ Problem 2.3: Integrating Factor Method and Asymptotics

## 📄 Enunciado (Problem Statement)

Use an integrating factor to solve the following differential equations:

(i) $\frac{dy}{dx} + \frac{y}{x} = x^2$ (find the general solution and the only solution that is finite when $x = 0$)  
(ii) $\frac{dx}{dt} + tx = 4t$ (find the solution with $x(0) = 2$)  
(iii) $\frac{dz}{dy} = z \tan y + \sin y$ (find the general solution)  
(iv) $y' + e^{-x} y = 1$ (find the solution when $y(0) = e$, leaving your answer as an integral)  
(v) $\dot{x} + x \tanh t = 3$ (find the general solution, and compare it to that for $\dot{x} + x = 3$)  
(vi) $y' + 2y \cot x = 5$ (find the solution with $y(\pi/2) = 1$)  
(vii) $\frac{dx}{dt} + 5x = t$ (find the general solution)  
(viii) With $a > 0$, find the solution of the equation $\frac{dx}{dt} + \left( a + \frac{1}{t} \right)x = b$ for a general initial condition $x(1) = x_0$, and show that $x(t) \to \frac{b}{a}$ as $t \to \infty$.

---

## 📊 1. Identificación de Datos e Hipótesis (Phase 1)

### Mathematical Structure:
All eight equations are first-order linear ODEs of the form:
$$ \frac{dx}{dt} + p(t) x = q(t) $$
The integrating factor is $\mu(t) = \exp\left( \int p(t) dt \right)$, yielding:
$$ x(t) = \frac{1}{\mu(t)} \left[ \int \mu(t) q(t) \, dt + C \right] $$

---

## 🧠 2. Estrategia y Planteamiento Físico (Phase 2)

1. For each equation, identify $p(t)$ and $q(t)$, verifying that the leading derivative coefficient is $1$.
2. Compute the antiderivative $\int p(t) dt$ and evaluate $\mu(t) = \exp(\int p dt)$ using trigonometric/hyperbolic identities where appropriate ($\int \tan y dy = -\ln|\cos y|$, $\int \cot x dx = \ln|\sin x|$, $\int \tanh t dt = \ln(\cosh t)$).
3. Integrate $\mu(t) q(t)$ using substitution or integration by parts.
4. Enforce boundary conditions, singularity restrictions ($x = 0$), and asymptotic limits ($t \to \infty$).

---

## 🔢 3. Resolución Matemática Paso a Paso (Phase 3)

### Part (i): $\frac{dy}{dx} + \frac{1}{x} y = x^2$
* Here $p(x) = \frac{1}{x}, q(x) = x^2$.
* Integrating factor: $\mu(x) = e^{\int \frac{1}{x} dx} = e^{\ln|x|} = x$ (for $x > 0$).
* Multiply the ODE by $x$:
  $$ \frac{d}{dx} [x y] = x \cdot x^2 = x^3 $$
* Integrate with respect to $x$:
  $$ x y = \int x^3 \, dx = \frac{x^4}{4} + C \implies \mathbf{y(x) = \frac{x^3}{4} + \frac{C}{x}} \tag{1} $$
* **Finiteness at $x = 0$:**
  $$ \lim_{x \to 0} y(x) = \lim_{x \to 0} \left( \frac{x^3}{4} + \frac{C}{x} \right) $$
  The term $\frac{C}{x}$ diverges to $\pm\infty$ as $x \to 0$ unless $C = 0$.
* Therefore, the **only finite solution** at the origin is:
  $$ \mathbf{y(x) = \frac{x^3}{4}} \tag{1b} $$

---

### Part (ii): $\frac{dx}{dt} + t x = 4t$, $x(0) = 2$
* Here $p(t) = t, q(t) = 4t$.
* Integrating factor: $\mu(t) = e^{\int t dt} = e^{t^2/2}$.
* Total derivative:
  $$ \frac{d}{dt} \left[ x e^{t^2/2} \right] = 4t e^{t^2/2} $$
* Integrate:
  $$ x(t) e^{t^2/2} = \int 4t e^{t^2/2} \, dt = 4 e^{t^2/2} + C $$
  $$ x(t) = 4 + C e^{-t^2/2} $$
* Apply $x(0) = 2$:
  $$ 2 = 4 + C e^0 \implies C = -2 $$
  $$ \mathbf{x(t) = 4 - 2 e^{-t^2/2}} \tag{2} $$

---

### Part (iii): $\frac{dz}{dy} = z \tan y + \sin y \implies \frac{dz}{dy} - (\tan y) z = \sin y$
* Here $p(y) = -\tan y, q(y) = \sin y$.
* Integrating factor:
  $$ \int -\tan y \, dy = -\int \frac{\sin y}{\cos y} \, dy = \ln|\cos y| \implies \mu(y) = e^{\ln|\cos y|} = \cos y $$
  (for $y \in (-\pi/2, \pi/2)$).
* Total derivative:
  $$ \frac{d}{dy} [z \cos y] = \sin y \cos y $$
* Integrate:
  $$ z \cos y = \int \sin y \cos y \, dy = \frac{1}{2} \sin^2 y + C $$
* Isolate $z(y)$:
  $$ \mathbf{z(y) = \frac{\sin^2 y}{2\cos y} + \frac{C}{\cos y} = \frac{1}{2}\sin y \tan y + C \sec y} \tag{3} $$

---

### Part (iv): $y' + e^{-x} y = 1$, $y(0) = e$
* Here $p(x) = e^{-x}, q(x) = 1$.
* Integrating factor with base point $0$:
  $$ \int_0^x e^{-s} \, ds = \left[ -e^{-s} \right]_0^x = 1 - e^{-x} \implies \mu(x) = e^{1 - e^{-x}} = e \cdot e^{-e^{-x}} $$
* Using $\mu(x) = e^{-e^{-x}}$:
  $$ \frac{d}{dx} \left[ y(x) e^{-e^{-x}} \right] = e^{-e^{-x}} $$
* Integrate from $0$ to $x$:
  $$ y(x) e^{-e^{-x}} - y(0) e^{-e^0} = \int_0^x e^{-e^{-s}} \, ds $$
  Since $y(0) = e$ and $e^0 = 1$, the initial term is $e \cdot e^{-1} = 1$:
  $$ y(x) e^{-e^{-x}} - 1 = \int_0^x e^{-e^{-s}} \, ds $$
  $$ \mathbf{y(x) = e^{e^{-x}} \left( 1 + \int_0^x e^{-e^{-s}} \, ds \right)} \tag{4} $$

---

### Part (v): $\dot{x} + x \tanh t = 3$
* Here $p(t) = \tanh t = \frac{\sinh t}{\cosh t}, q(t) = 3$.
* Integrating factor:
  $$ \mu(t) = \exp\left( \int \frac{\sinh t}{\cosh t} \, dt \right) = \exp(\ln(\cosh t)) = \cosh t $$
* Total derivative:
  $$ \frac{d}{dt} [x \cosh t] = 3 \cosh t $$
* Integrate:
  $$ x \cosh t = \int 3 \cosh t \, dt = 3 \sinh t + C $$
  $$ \mathbf{x(t) = 3 \frac{\sinh t}{\cosh t} + \frac{C}{\cosh t} = 3 \tanh t + C \operatorname{sech} t} \tag{5} $$

#### Comparison with $\dot{x} + x = 3$:
For $\dot{x} + x = 3$, the integrating factor is $e^t$, giving:
$$ x_{\text{comp}}(t) = 3 + C_2 e^{-t} $$
* **As $t \to +\infty$:** $\tanh t \to 1$ and $\operatorname{sech} t \to 0$. Thus $x(t) \to 3$. Similarly, $x_{\text{comp}}(t) \to 3$. Both converge to the identical steady-state attractor $x = 3$.
* **As $t \to -\infty$:** $\tanh t \to -1$ and $\operatorname{sech} t \to 0$. Thus $x(t) \to -3$. In contrast, $x_{\text{comp}}(t) \to \pm\infty$ exponentially.

---

### Part (vi): $y' + 2y \cot x = 5$, $y(\pi/2) = 1$
* Here $p(x) = 2\cot x = 2\frac{\cos x}{\sin x}, q(x) = 5$.
* Integrating factor:
  $$ \mu(x) = \exp\left( \int 2 \frac{\cos x}{\sin x} \, dx \right) = \exp(2\ln|\sin x|) = \sin^2 x $$
* Total derivative:
  $$ \frac{d}{dx} \left[ y \sin^2 x \right] = 5 \sin^2 x = 5 \left( \frac{1 - \cos 2x}{2} \right) $$
* Integrate:
  $$ y \sin^2 x = \frac{5}{2} \int (1 - \cos 2x) \, dx = \frac{5}{2} x - \frac{5}{4}\sin 2x + C $$
* Apply $y(\pi/2) = 1$:
  $$ 1 \cdot \sin^2(\pi/2) = \frac{5}{2}\left(\frac{\pi}{2}\right) - \frac{5}{4}\sin(\pi) + C $$
  $$ 1 = \frac{5\pi}{4} - 0 + C \implies C = 1 - \frac{5\pi}{4} $$
* Isolate $y(x)$:
  $$ \mathbf{y(x) = \frac{\frac{5}{2}x - \frac{5}{4}\sin(2x) + 1 - \frac{5\pi}{4}}{\sin^2 x}} \tag{6} $$

---

### Part (vii): $\frac{dx}{dt} + 5x = t$
* Here $p(t) = 5, q(t) = t$.
* Integrating factor: $\mu(t) = e^{5t}$.
* Total derivative:
  $$ \frac{d}{dt} [x e^{5t}] = t e^{5t} $$
* Integrate by parts ($\int u dv = uv - \int v du$ with $u = t, dv = e^{5t}dt$):
  $$ \int t e^{5t} \, dt = \frac{t e^{5t}}{5} - \int \frac{e^{5t}}{5} \, dt = \frac{t e^{5t}}{5} - \frac{e^{5t}}{25} + C $$
* Isolate $x(t)$:
  $$ \mathbf{x(t) = \frac{t}{5} - \frac{1}{25} + C e^{-5t}} \tag{7} $$

---

### Part (viii): $\frac{dx}{dt} + \left( a + \frac{1}{t} \right)x = b$, $a > 0$, $x(1) = x_0$
* Integrating factor for $t > 0$:
  $$ \int \left( a + \frac{1}{t} \right) dt = at + \ln t \implies \mu(t) = e^{at + \ln t} = t e^{at} $$
* Total derivative:
  $$ \frac{d}{dt} [x \cdot t e^{at}] = b t e^{at} $$
* Integrate by parts:
  $$ \int b t e^{at} \, dt = b \left[ \frac{t e^{at}}{a} - \int \frac{e^{at}}{a} \, dt \right] = \frac{b}{a} t e^{at} - \frac{b}{a^2} e^{at} + C $$
* Divide by $t e^{at}$:
  $$ x(t) = \frac{b}{a} - \frac{b}{a^2 t} + \frac{C}{t} e^{-at} \tag{8} $$
* Apply $x(1) = x_0$:
  $$ x_0 = \frac{b}{a} - \frac{b}{a^2} + C e^{-a} \implies C = e^a \left( x_0 - \frac{b}{a} + \frac{b}{a^2} \right) $$
* **Asymptotic limit as $t \to \infty$:**
  Since $a > 0$, $e^{-at} \to 0$ and $\frac{1}{t} \to 0$:
  $$ \lim_{t \to \infty} x(t) = \frac{b}{a} - \lim_{t \to \infty} \frac{b}{a^2 t} + C \lim_{t \to \infty} \frac{e^{-at}}{t} = \frac{b}{a} - 0 + 0 = \mathbf{\frac{b}{a}} \tag{8b} $$

---

## 🎯 4. Resultado Final y Análisis Físico (Phase 4)

### Master Solution Table:

| Part | Integrating Factor $\mu$ | Solution |
| :---: | :---: | :--- |
| **(i)** | $x$ | $y(x) = \frac{x^3}{4} + \frac{C}{x}$; finite at $x=0 \implies \mathbf{y = \frac{x^3}{4}}$ |
| **(ii)** | $e^{t^2/2}$ | $\mathbf{x(t) = 4 - 2 e^{-t^2/2}}$ |
| **(iii)** | $\cos y$ | $\mathbf{z(y) = \frac{1}{2}\sin y \tan y + C \sec y}$ |
| **(iv)** | $e^{-e^{-x}}$ | $\mathbf{y(x) = e^{e^{-x}}\left(1 + \int_0^x e^{-e^{-s}}ds\right)}$ |
| **(v)** | $\cosh t$ | $\mathbf{x(t) = 3\tanh t + C\operatorname{sech} t}$ ($\lim_{t\to\infty} x = 3, \lim_{t\to-\infty} x = -3$) |
| **(vi)** | $\sin^2 x$ | $\mathbf{y(x) = \frac{\frac{5}{2}x - \frac{5}{4}\sin(2x) + 1 - \frac{5\pi}{4}}{\sin^2 x}}$ |
| **(vii)** | $e^{5t}$ | $\mathbf{x(t) = \frac{t}{5} - \frac{1}{25} + C e^{-5t}}$ |
| **(viii)** | $t e^{at}$ | $\mathbf{x(t) = \frac{b}{a} - \frac{b}{a^2 t} + \frac{C}{t}e^{-at} \implies \lim_{t\to\infty} x(t) = \frac{b}{a}}$ |

---

## 🔗 Related Notes
* `[[04 - Advanced Maths/Concepto - Factor Integrante y Ecuaciones Lineales de Primer Orden|Integrating Factor Theory]]`
* `[[04 - Advanced Maths/Problema - Ch2-P10 Uniqueness via Integrating Transformation|Problem 2.10: Uniqueness Transformation]]`
