---
materia: Fluid Mechanics
tema: "Topic 6: Dimensional Analysis"
fuentes:
  - "Notes.pdf (Sánchez & Rodríguez-Rodríguez, UC3M), Chapter 6, pp. 57-71 (PDF pages 66-80)"
tags:
  - moc-topic
  - fluid-mechanics
  - dimensional-analysis
  - second-year
dificultad: medium
---

# Topic 6: Dimensional Analysis

> **Central idea.** A physical law cannot depend on the units chosen to measure its quantities. If an unknown $a_0$ depends on $n$ governing parameters, of which $k$ have independent dimensions, the $\Pi$ theorem reduces the law to a relation between $n-k+1$ dimensionless groups, $\Pi_0 = F(\Pi_1,\dots,\Pi_{n-k})$. In fluid mechanics the list of parameters is read from the conservation equations and their boundary conditions; the limits $\mathrm{Re}\gg 1$ and $\mathrm{Re}\ll 1$ remove one more parameter; and equal dimensionless groups in a model and in the real system (physical similarity) let a laboratory test predict the full-scale result.

---

## 1. Dimensions of a Physical Magnitude

### The falling body

The chapter opens with a mass $m$ released from rest at a height $h$ under gravity $g$ (Notes.pdf, p. 57, Fig. 6.1). The unknowns are the collision time $t_c$ and the collision velocity $v_c$.

![[attachments/FM-T6/t6-falling-mass.svg]]

The exact solution is quick, and it will be used to check the dimensional result. Newton's second law $m\,d^2z/dt^2 = -mg$ with $z = h$ and $dz/dt = 0$ at $t = 0$ is integrated once, from $0$ to $t$, using Barrow's rule:

$$ \frac{dz}{dt}(t) - \frac{dz}{dt}(0) = \int_0^t (-g)\,dt' = \big[-g t'\big]_0^t = -g t \quad\Longrightarrow\quad \frac{dz}{dt} = -g t $$

and once more:

$$ z(t) - z(0) = \int_0^t (-g t')\,dt' = \left[-\frac{g t'^2}{2}\right]_0^t = -\frac{g t^2}{2} \quad\Longrightarrow\quad z = h - \frac{g t^2}{2} $$

Setting $z(t_c) = 0$ gives $t_c = \sqrt{2h/g}$, and then $v_c = g t_c = \sqrt{2gh}$ (Notes.pdf, p. 57).

### What we would guess before solving

Before any integration, one guesses which quantities can influence the answer: the mass, the height and gravity (Notes.pdf, Eq. 6.1):

$$ t_c = t_c(m, h, g), \qquad v_c = v_c(m, h, g) \tag{6.1} $$

### Units and dimensions

The numbers $t_c$, $v_c$, $h$, $m$, $g$ are the result of comparing each quantity with a unit. If the unit of length is made $L$ times smaller, the unit of time $T$ times smaller and the unit of mass $M$ times smaller, the numbers $h$, $t_c$ and $m$ grow by the factors $L$, $T$ and $M$, the velocity $v_c$ by $LT^{-1}$ and the acceleration $g$ by $LT^{-2}$. These factors are the **dimensions** of the quantities:

$$ [h] = L, \qquad [t_c] = T, \qquad [m] = M, \qquad [v_c] = LT^{-1}, \qquad [g] = LT^{-2} $$

The dimensions are always power-law monomials $L^{\alpha}T^{\beta}M^{\gamma}$, with $\alpha$, $\beta$, $\gamma$ rational numbers (Notes.pdf, p. 58).

### The two dimensionless ratios

Changing the units of length and time changes $(h/g)^{1/2}$ by a factor $T$ and $(gh)^{1/2}$ by a factor $LT^{-1}$; check: $[(h/g)^{1/2}] = (L\cdot L^{-1}T^{2})^{1/2} = T$ and $[(gh)^{1/2}] = (LT^{-2}\cdot L)^{1/2} = LT^{-1}$. Hence the ratios (Notes.pdf, Eqs. 6.2-6.3)

$$ \Pi_1 = \frac{t_c}{(h/g)^{1/2}} \tag{6.2} $$

$$ \Pi_2 = \frac{v_c}{(gh)^{1/2}} \tag{6.3} $$

have dimension $[\Pi_1] = [\Pi_2] = 1$: their value is the same in every system of units. With (6.1) they become (Notes.pdf, Eqs. 6.4-6.5)

$$ \Pi_1 = \frac{t_c(m,h,g)}{(h/g)^{1/2}} = \Pi_1(m, h, g) \tag{6.4} $$

$$ \Pi_2 = \frac{v_c(m,h,g)}{(gh)^{1/2}} = \Pi_2(m, h, g) \tag{6.5} $$

### Removing the parameters one by one

The key argument of the whole chapter (Notes.pdf, p. 59):

1. Change **only the unit of mass**. The number $m$ changes arbitrarily while $h$ and $g$ stay fixed, and $\Pi_1$, $\Pi_2$ (dimensionless) cannot change. So $\Pi_1$ and $\Pi_2$ do not depend on $m$: $\Pi_1 = \Pi_1(h, g)$, $\Pi_2 = \Pi_2(h, g)$.
2. Change **only the unit of time**. The number $g$ is multiplied by $T^{-2}$ while $h$ stays fixed; again $\Pi_1$, $\Pi_2$ do not change, so they do not depend on $g$.
3. Change **the unit of length**. $h$ changes arbitrarily and the $\Pi$'s do not, so they do not depend on $h$ either.

What is left is (Notes.pdf, Eqs. 6.6-6.7)

$$ \frac{t_c}{(h/g)^{1/2}} = C_1 \tag{6.6} $$

$$ \frac{v_c}{(gh)^{1/2}} = C_2 \tag{6.7} $$

Dimensional analysis gives the form of the law, not the constants. The integration above gives $C_1 = C_2 = \sqrt{2}$; a **single experiment** (drop one object, measure $t_c$ and $v_c$) would give them too, and then (6.6)-(6.7) hold for any mass, any height and any planet.

---

## 2. Physical Quantities with Independent Dimensions

### How many fundamental units

A geometric problem needs one unit (length), a kinematic problem two (length, time), mechanics three (mass, length, time); thermal problems add temperature $\Theta$, electromagnetic ones electric charge. The chapter works with mechanical problems, $[a] = L^{\alpha}T^{\beta}M^{\gamma}$ (Notes.pdf, p. 60).

### Definition

The quantities $a_1,\dots,a_k$ have **independent dimensions** when the dimension of none of them can be written as a product of powers of the dimensions of the other $k-1$.

### Example: $\rho$, $U$, $\mu$

Take $[\rho] = ML^{-3}$, $[U] = LT^{-1}$, $[\mu] = ML^{-1}T^{-1}$. Assume the opposite: that two numbers $x$, $y$ exist with $[\rho] = [U]^x[\mu]^y$ (Notes.pdf, Eq. 6.8). Written with the exponents of $(L, M, T)$:

$$ L^{-3}M^{1}T^{0} = \left(L^{1}M^{0}T^{-1}\right)^{x}\left(L^{-1}M^{1}T^{-1}\right)^{y} \tag{6.8} $$

Equating the exponents of $L$, $M$ and $T$ (Notes.pdf, Eq. 6.9):

$$ -3 = x - y, \qquad 1 = y, \qquad 0 = -x - y \tag{6.9} $$

The second equation gives $y = 1$; the first then gives $x = -3 + 1 = -2$; the third requires $0 = -x - y = 2 - 1 = 1$, which is false. No pair $(x, y)$ exists, so $\rho$, $U$, $\mu$ have independent dimensions. By contrast, $p$, $\rho$, $U$ do not: $[\rho][U]^2 = ML^{-3}\cdot L^{2}T^{-2} = ML^{-1}T^{-2} = [p]$, that is $x = 1$, $y = 2$.

### The rank test

The equations (6.9) say that the exponent vector of $\rho$ is a combination of those of $U$ and $\mu$ (Notes.pdf, Eq. 6.10):

$$ (-3, 1, 0) = x\,(1, 0, -1) + y\,(-1, 1, -1) \tag{6.10} $$

so $a_1,\dots,a_k$ have independent dimensions if and only if **the rank of the matrix of exponents equals $k$**. Rows $\rho$, $U$, $\mu$; columns $L$, $M$, $T$ (Notes.pdf, Eq. 6.11):

$$ \begin{pmatrix} -3 & 1 & 0 \\ 1 & 0 & -1 \\ -1 & 1 & -1 \end{pmatrix} \tag{6.11} $$

Expanding along the first row: $\det = -3\,[0\cdot(-1) - (-1)\cdot 1] - 1\,[1\cdot(-1) - (-1)\cdot(-1)] + 0 = -3(1) - 1(-2) = -1 \neq 0$, so the rank is 3. For $\rho$, $U$, $p$ (Notes.pdf, Eq. 6.12):

$$ \begin{pmatrix} -3 & 1 & 0 \\ 1 & 0 & -1 \\ -1 & 1 & -2 \end{pmatrix} \tag{6.12} $$

$\det = -3\,[0\cdot(-2) - (-1)\cdot 1] - 1\,[1\cdot(-2) - (-1)\cdot(-1)] = -3(1) - 1(-3) = 0$, and the first two rows are clearly not proportional, so the rank is 2: the three quantities are not independent.

> [!tip] Exam practice
> With three fundamental units the matrix has three columns, so **at most three** quantities can have independent dimensions. To find $k$, look for the largest set of rows with a non-zero determinant (a $3\times 3$ minor first; if all vanish, a $2\times 2$ one).

---

## 3. The Π Theorem (Vaschy-Buckingham Theorem)

### The general problem

We look for an unknown quantity $a_0$ that depends on $n$ governing parameters (Notes.pdf, Eq. 6.13):

$$ a_0 = f(a_1,\dots,a_k,a_{k+1},\dots,a_n) \tag{6.13} $$

Let $k \le n$ be the largest number of parameters with independent dimensions, and $a_1,\dots,a_k$ one such set. The dimensions of every other parameter are products of powers of theirs (Notes.pdf, Eq. 6.14):

$$ [a_{k+1}] = [a_1]^{\alpha_{k+1}}\cdots[a_k]^{\gamma_{k+1}}, \quad [a_{k+2}] = [a_1]^{\alpha_{k+2}}\cdots[a_k]^{\gamma_{k+2}}, \quad \dots, \quad [a_n] = [a_1]^{\alpha_{n}}\cdots[a_k]^{\gamma_{n}} \tag{6.14} $$

In general $0 < k < n$; $k = n$ happens in the falling body. The same holds for the unknown (Notes.pdf, Eq. 6.15):

$$ [a_0] = [a_1]^{\alpha_0}\cdots[a_k]^{\gamma_0} \tag{6.15} $$

> [!note] Two typing slips in the notes (p. 61)
> In (6.14) the notes print the exponent of $[a_k]$ in the second line as $\gamma_{k+1}$; it must be $\gamma_{k+2}$, as written above. The sentence after (6.14) reads "or $k = n$, as occurs if all parameters $a_1,\dots,a_n$ are dimensionless"; for dimensionless parameters no unit can change them, so the intended case is $k = 0$.

### The dimensionless groups

Dividing each quantity by the product of powers with its own dimensions gives $n - k + 1$ dimensionless numbers (Notes.pdf, Eq. 6.16):

$$ \Pi_0 = \frac{a_0}{a_1^{\alpha_0}\cdots a_k^{\gamma_0}}, \quad \Pi_1 = \frac{a_{k+1}}{a_1^{\alpha_{k+1}}\cdots a_k^{\gamma_{k+1}}}, \quad \Pi_2 = \frac{a_{k+2}}{a_1^{\alpha_{k+2}}\cdots a_k^{\gamma_{k+2}}}, \quad \dots, \quad \Pi_{n-k} = \frac{a_n}{a_1^{\alpha_n}\cdots a_k^{\gamma_n}} \tag{6.16} $$

Dividing (6.13) by $a_1^{\alpha_0}\cdots a_k^{\gamma_0}$ and writing $a_{k+1},\dots,a_n$ through the $\Pi$'s, $a_{k+j} = \Pi_j\,a_1^{\alpha_{k+j}}\cdots a_k^{\gamma_{k+j}}$ (Notes.pdf, Eq. 6.17):

$$ \Pi_0 = \frac{f(a_1,\dots,a_k,a_{k+1},\dots,a_n)}{a_1^{\alpha_0}\cdots a_k^{\gamma_0}} = \frac{f\left(a_1,\dots,a_k,\Pi_1 a_1^{\alpha_{k+1}}\cdots a_k^{\gamma_{k+1}},\dots,\Pi_{n-k}a_1^{\alpha_n}\cdots a_k^{\gamma_n}\right)}{a_1^{\alpha_0}\cdots a_k^{\gamma_0}} \tag{6.17} $$

that is, $\Pi_0$ is a function of $a_1,\dots,a_k$ and of the $\Pi$'s (Notes.pdf, Eq. 6.18):

$$ \Pi_0 = \Pi_0(a_1,\dots,a_k,\Pi_1,\dots,\Pi_{n-k}) \tag{6.18} $$

### Worked example: pressure loss in a pipe

The pressure loss per unit length of a liquid flowing along a long circular pipe depends on the volume flux $Q$, the diameter $D$, the density $\rho$ and the viscosity $\mu$ (Notes.pdf, Eq. 6.19):

$$ P_l = -\frac{\partial p}{\partial x} = f(Q, D, \rho, \mu) \tag{6.19} $$

Here $n = 4$. Dimensions: $[Q] = L^3T^{-1}$, $[D] = L$, $[\rho] = ML^{-3}$, $[\mu] = ML^{-1}T^{-1}$, $[P_l] = [p]/L = ML^{-2}T^{-2}$. The set $(Q, D, \rho)$ is independent: $\rho$ is the only one with $M$, $Q$ the only one with $T$, and $D$ adds $L$; so $k = 3$.

**Exponents of $\mu$.** Write $[\mu] = [Q]^{a}[D]^{b}[\rho]^{c}$ and equate exponents:

$$ M:\; 1 = c, \qquad T:\; -1 = -a, \qquad L:\; -1 = 3a + b - 3c $$

so $c = 1$, $a = 1$ and $b = -1 - 3(1) + 3(1) = -1$ (Notes.pdf, Eq. 6.20):

$$ [\mu] = [Q]^{1}[D]^{-1}[\rho]^{1} \tag{6.20} $$

**Exponents of $P_l$.** With $[P_l] = [Q]^{a}[D]^{b}[\rho]^{c}$:

$$ M:\; 1 = c, \qquad T:\; -2 = -a, \qquad L:\; -2 = 3a + b - 3c $$

so $c = 1$, $a = 2$ and $b = -2 - 6 + 3 = -5$ (Notes.pdf, Eq. 6.21):

$$ [P_l] = [Q]^{2}[D]^{-5}[\rho]^{1} \tag{6.21} $$

The two dimensionless groups are (Notes.pdf, Eq. 6.22)

$$ \Pi_0 = \frac{P_l}{\rho Q^2/D^5} \qquad\text{and}\qquad \Pi_1 = \frac{\mu}{\rho Q/D} \tag{6.22} $$

and substituting $\mu = \Pi_1\,\rho Q/D$ into (6.19) gives the form (6.18) (Notes.pdf, Eq. 6.23):

$$ \Pi_0 = \frac{f(Q, D, \rho, \Pi_1\rho Q/D)}{\rho Q^2/D^5} = F(Q, D, \rho, \Pi_1) \tag{6.23} $$

Now the argument of Section 1, repeated:

1. Make the unit of mass $M$ times smaller: $\rho$ grows by $M$, while $\Pi_0$, $\Pi_1$, $Q$, $D$ do not change. So $F$ does not depend on $\rho$: $\Pi_0 = F(Q, D, \Pi_1)$.
2. Make the unit of time $T$ times smaller: the number $Q$ changes by the factor $T^{-1}$ (since $[Q] = L^3T^{-1}$), while $D$, $\Pi_0$, $\Pi_1$ do not change: $\Pi_0 = F(D, \Pi_1)$.
3. Change the unit of length: $\Pi_0 = F(\Pi_1)$.

The result (Notes.pdf, Eq. 6.24):

$$ \frac{P_l}{\rho Q^2/D^5} = F\left(\frac{\mu}{\rho Q/D}\right) \tag{6.24} $$

### The theorem

Repeating the argument on (6.18): a change of units can always modify $a_1$ alone, leaving $a_2,\dots,a_k$ and all the $\Pi$'s fixed, so $\Pi_0$ does not depend on $a_1$; one by one, it does not depend on $a_2,\dots,a_k$ either (Notes.pdf, Eq. 6.25):

$$ \Pi_0 = F(\Pi_1,\dots,\Pi_{n-k}) \tag{6.25} $$

> [!info] The Π theorem (Notes.pdf, p. 62)
> If an unknown $a_0$ depends on $n$ governing parameters $a_1,\dots,a_n$, the number of parameters can always be reduced to $n - k$, where $k$ is the number of governing parameters with independent dimensions. The $k$ quantities with independent dimensions are used to write the other $n-k$ parameters and the unknown in dimensionless form, which gives (6.25).

### Why it matters: fewer experiments

For the pipe, the theorem reduces four parameters to one. A single series of experiments in one pipe with one fluid, varying $Q$ and measuring $P_l$, plotted as $\Pi_0$ against $\Pi_1$, gives the law for **any fluid in any pipe**. For a new case ($Q^*$, $\rho^*$, $\mu^*$, $D^*$): compute $\Pi_1^* = \mu^*/(\rho^*Q^*/D^*)$, read $\Pi_0^*$ on the curve, and solve $P_l^* = \Pi_0^*\,\rho^*(Q^*)^2/(D^*)^5$ (Notes.pdf, p. 63).

---

## 4. Taylor's Analysis of a Nuclear Explosion

### Governing parameters

An atomic explosion releases a large energy $E$ almost instantaneously at one point; a strong spherical shock of radius $r_o$ grows with time $t$. In the first stages the pressure $p_o$ behind the shock is thousands of times the ambient pressure, so the ambient pressure does not enter, and (6.13) becomes (Notes.pdf, Eq. 6.26):

$$ r_o = f_1(E, \rho_a, t) \qquad\text{and}\qquad p_o = f_2(E, \rho_a, t) \tag{6.26} $$

### Rank

Rows $E$, $\rho_a$, $t$; columns $L$, $M$, $T$, from $[E] = ML^2T^{-2}$, $[\rho_a] = ML^{-3}$, $[t] = T$ (Notes.pdf, Eq. 6.27):

$$ \begin{pmatrix} 2 & 1 & -2 \\ -3 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \tag{6.27} $$

Expanding along the third row: $\det = 1\cdot(2\cdot 1 - 1\cdot(-3)) = 5 \neq 0$. So $k = 3 = n$ and **no governing parameter is left**: $n - k = 0$.

### The exponents

**Radius.** $[r_o] = L = [E]^{a}[\rho_a]^{b}[t]^{c}$:

$$ M:\; 0 = a + b, \qquad L:\; 1 = 2a - 3b, \qquad T:\; 0 = -2a + c $$

From the first, $b = -a$; the second becomes $1 = 2a + 3a = 5a$, so $a = 1/5$, $b = -1/5$; the third gives $c = 2a = 2/5$.

**Pressure.** $[p_o] = ML^{-1}T^{-2} = [E]^{a}[\rho_a]^{b}[t]^{c}$:

$$ M:\; 1 = a + b, \qquad L:\; -1 = 2a - 3b, \qquad T:\; -2 = -2a + c $$

With $b = 1 - a$: $-1 = 2a - 3 + 3a$, so $a = 2/5$, $b = 3/5$, and $c = -2 + 2a = -6/5$.

The solution is therefore (Notes.pdf, Eqs. 6.28-6.29)

$$ \frac{r_o}{E^{1/5}\rho_a^{-1/5}t^{2/5}} = C_1 \qquad\text{and}\qquad \frac{p_o}{E^{2/5}\rho_a^{3/5}t^{-6/5}} = C_2 \tag{6.28} $$

$$ r_o = C_1 E^{1/5}\rho_a^{-1/5}t^{2/5} \qquad\text{and}\qquad p_o = C_2 E^{2/5}\rho_a^{3/5}t^{-6/5} \tag{6.29} $$

$C_1$ and $C_2$ come from integrating the compressible-flow equations, or from measurements.

### The shock slows down, and when the law stops holding

The shock speed is the time derivative of (6.29), with the power rule $\frac{d}{dt}t^{2/5} = \frac{2}{5}t^{2/5-1} = \frac{2}{5}t^{-3/5}$:

$$ \frac{dr_o}{dt} = \frac{2}{5}\,C_1 E^{1/5}\rho_a^{-1/5}t^{-3/5} $$

Both the speed and $p_o$ decrease with time. The law fails when $p_o$ falls to the order of the ambient pressure $p_a$. Setting $E^{2/5}\rho_a^{3/5}t^{-6/5} \sim p_a$ and solving for $t$: $t^{6/5} \sim E^{2/5}\rho_a^{3/5}/p_a$, and raising to $5/6$,

$$ t \sim \frac{E^{1/3}\rho_a^{1/2}}{p_a^{5/6}} $$

(Notes.pdf, p. 64). The same reasoning applies to the cylindrical shock of a lightning stroke, with $E$ the energy per unit length, $[E] = MLT^{-2}$.

---

## 5. Parametric Dependence of the Solution

### The hard step is the list of parameters

Missing an important parameter, or adding spurious ones, gives a wrong result. In fluid mechanics the list need not be a guess: **write the conservation equations with their initial and boundary conditions**, and read the parameters from them (Notes.pdf, p. 64).

![[attachments/FM-T6/t6-sphere.svg]]

### A first guess for the sphere

A sphere of radius $R$ moves with constant velocity $U$ in a stagnant liquid of density $\rho$ and viscosity $\mu$; far away the pressure is hydrostatic, $p + \rho g z = P_\infty$. A first guess for the drag (Notes.pdf, Eq. 6.30):

$$ F_x = F_x(R, U, \rho, \mu, P_\infty, g) \tag{6.30} $$

Exponent matrix, rows $R$, $U$, $\rho$, $\mu$, $P_\infty$, $g$; columns $L$, $M$, $T$ (Notes.pdf, Eq. 6.31):

$$ \begin{pmatrix} 1 & 0 & 0 \\ 1 & 0 & -1 \\ -3 & 1 & 0 \\ -1 & 1 & -1 \\ -1 & 1 & -2 \\ 1 & 0 & -2 \end{pmatrix} \tag{6.31} $$

The rank of a $6\times 3$ matrix is at most 3, and the first three rows give $\det = 1\cdot(0\cdot 0 - (-1)\cdot 1) - 0 + 0 = 1 \neq 0$, so $k = 3$ with $(R, U, \rho)$. Since $[F_x] = MLT^{-2} = [\rho][U]^2[R]^2$, the dimensionless force is (Notes.pdf, Eq. 6.32)

$$ \Pi_0 = \frac{F_x}{\rho U^2 R^2} \tag{6.32} $$

Check the other three: $[\rho][U][R] = ML^{-3}\cdot LT^{-1}\cdot L = ML^{-1}T^{-1} = [\mu]$; $[\rho][U]^2 = ML^{-1}T^{-2} = [P_\infty]$; $[U]^2[R]^{-1} = LT^{-2} = [g]$. So (Notes.pdf, Eq. 6.33)

$$ \Pi_1 = \frac{\mu}{\rho U R}, \qquad \Pi_2 = \frac{P_\infty}{\rho U^2}, \qquad \Pi_3 = \frac{g}{U^2/R} \tag{6.33} $$

and the theorem gives (Notes.pdf, Eq. 6.34)

$$ \frac{F_x}{\rho U^2 R^2} = f\left(\frac{\mu}{\rho U R}, \frac{P_\infty}{\rho U^2}, \frac{g}{U^2/R}\right) \tag{6.34} $$

Six parameters became three, but **(6.34) is wrong**: $P_\infty$ and $g$ do not influence the drag. With the correct list $F_x = F_x(R, U, \rho, \mu)$ the result is (Notes.pdf, Eq. 6.35)

$$ \frac{F_x}{\rho U^2 R^2} = f\left(\frac{\mu}{\rho U R}\right) \tag{6.35} $$

### Reading the parameters from the equations

In the frame of the sphere the liquid satisfies (Notes.pdf, Eq. 6.36)

$$ \nabla\cdot\bar{v} = 0, \quad \rho\,\bar{v}\cdot\nabla\bar{v} = -\nabla p + \mu\nabla^2\bar{v} - \rho g\,\bar{e}_z; \qquad \lvert\bar{x}\rvert\to\infty:\; p = P_\infty - \rho g z,\; \bar{v} = U\bar{e}_x; \qquad \lvert\bar{x}\rvert = R:\; \bar{v} = 0 \tag{6.36} $$

and the force on the sphere is the integral of the pressure and of the viscous stress $\bar{\bar{\tau}}' = \mu(\nabla\bar{v} + \nabla\bar{v}^T)$ over its surface (Notes.pdf, Eqs. 6.37-6.38):

$$ \bar{F} = -\int_{\lvert\bar{x}\rvert = R} p\,\bar{n}\,d\sigma + \int_{\lvert\bar{x}\rvert = R}\mu(\nabla\bar{v} + \nabla\bar{v}^T)\cdot\bar{n}\,d\sigma \tag{6.37} $$

$$ F_x = \bar{F}\cdot\bar{e}_x = -\int_{\lvert\bar{x}\rvert = R} p\,n_x\,d\sigma + \int_{\lvert\bar{x}\rvert = R}\mu\left[(\nabla\bar{v} + \nabla\bar{v}^T)\cdot\bar{n}\right]\cdot\bar{e}_x\,d\sigma \tag{6.38} $$

At first sight $P_\infty$ and $g$ do appear. Two observations remove them:

1. Gravity is a gradient, $-\nabla p - \rho g\bar{e}_z = -\nabla(p + \rho g z)$, so it can be absorbed in the **reduced pressure**.
2. Only pressure differences move the fluid; the level $P_\infty$ does not matter.

Both suggest $P' = p + \rho g z - P_\infty$. In terms of $P'$ (Notes.pdf, Eq. 6.39):

$$ \nabla\cdot\bar{v} = 0, \quad \rho\,\bar{v}\cdot\nabla\bar{v} = -\nabla P' + \mu\nabla^2\bar{v}; \qquad \lvert\bar{x}\rvert\to\infty:\; P' = 0,\; \bar{v} = U\bar{e}_x; \qquad \lvert\bar{x}\rvert = R:\; \bar{v} = 0 \tag{6.39} $$

Neither $P_\infty$ nor $g$ appears, so $P'(\bar{x})$ and $\bar{v}(\bar{x})$ do not depend on them. Substituting $p = P' + P_\infty - \rho g z$ in (6.37), and using $\int P_\infty\bar{n}\,d\sigma = 0$ (a constant pressure on a closed surface gives no force) (Notes.pdf, Eq. 6.40):

$$ \bar{F} = -\int_{\lvert\bar{x}\rvert = R} P'\,\bar{n}\,d\sigma + \int_{\lvert\bar{x}\rvert = R}\mu(\nabla\bar{v} + \nabla\bar{v}^T)\cdot\bar{n}\,d\sigma + \int_{\lvert\bar{x}\rvert = R}\rho g z\,\bar{n}\,d\sigma \tag{6.40} $$

The last term is Archimedes' buoyancy. By the Gauss theorem over the volume $V$ of the sphere ($\bar{n}$ pointing out of the sphere) and $\nabla(\rho g z) = \rho g\,\bar{e}_z$ (Notes.pdf, Eq. 6.41):

$$ \int_{\lvert\bar{x}\rvert = R}\rho g z\,\bar{n}\,d\sigma = \int_V \nabla(\rho g z)\,dV = \rho g\,\frac{4}{3}\pi R^3\,\bar{e}_z \tag{6.41} $$

It is vertical, so it does not contribute to the drag (Notes.pdf, Eq. 6.42):

$$ F_x = \bar{F}\cdot\bar{e}_x = -\int_{\lvert\bar{x}\rvert = R} P'\,n_x\,d\sigma + \int_{\lvert\bar{x}\rvert = R}\mu\left[(\nabla\bar{v} + \nabla\bar{v}^T)\cdot\bar{n}\right]\cdot\bar{e}_x\,d\sigma \tag{6.42} $$

This proves that $F_x = F_x(R, U, \rho, \mu)$ and that (6.35), not (6.34), is the right result.

### When pressure level and gravity do matter

- **Gases**: the absolute pressure enters through the equation of state $p = \rho R_g T$.
- **Liquids with a free surface that is not flat** (waves): the condition $p = p_a$ on the unknown surface $z_s(x, y)$ brings $g$ back. A sphere moving at a depth of order $R$ below the surface feels a drag that depends on $g$ and on the depth, and the reduced pressure no longer removes $g$ (Notes.pdf, p. 66). This is why $g$ appears in the ship, tsunami and wave-maker problems (DA1, DA6, DA11).

### The repeating set is not unique

Choosing $(U, R, \mu)$ instead of $(U, R, \rho)$ gives (Notes.pdf, Eq. 6.43)

$$ \frac{F_x}{\mu U R} = f\left(\frac{\rho U R}{\mu}\right) \tag{6.43} $$

Both (6.35) and (6.43) are valid. In both, the dimensionless force depends on the **Reynolds number** (Notes.pdf, Eq. 6.44):

$$ \mathrm{Re} = \frac{\rho U R}{\mu} \tag{6.44} $$

---

## 6. Nondimensionalization of the Navier-Stokes Equations

### Scales from the boundary conditions

Instead of the $\Pi$ theorem, the problem itself can be written in dimensionless variables. For the sphere, the boundary conditions give the velocity scale $U$ and the length scale $R$: $\bar{v}^* = \bar{v}/U$, $\bar{x}^* = \bar{x}/R$, hence $\nabla^* = R\nabla$ and $d\sigma^* = R^{-2}d\sigma$ (Notes.pdf, p. 67). The scale $\Delta p$ of $P'$ is not obvious: it depends on the kind of motion.

### Order of magnitude of each term

Velocities are of order $U$ and change by $O(U)$ over distances $O(R)$, so $O(\nabla\bar{v}) \sim U/R$ and $O(\nabla^2\bar{v}) \sim U/R^2$ (Notes.pdf, Eq. 6.45):

$$ \underbrace{\rho\,\bar{v}\cdot\nabla\bar{v}}_{\rho U^2/R} = \underbrace{-\nabla P'}_{\Delta p/R} + \underbrace{\mu\nabla^2\bar{v}}_{\mu U/R^2} \tag{6.45} $$

The pressure gradient is almost always essential: without it, (6.39) would have three unknowns (the velocity components) and four equations (continuity and three momentum components). The ratio of the other two terms is (Notes.pdf, Eq. 6.46)

$$ \frac{O(\rho\,\bar{v}\cdot\nabla\bar{v})}{O(\mu\nabla^2\bar{v})} = \frac{\rho U^2/R}{\mu U/R^2} = \frac{\rho U R}{\mu} \tag{6.46} $$

the Reynolds number (6.44). Three regimes (Notes.pdf, p. 67):

| Regime | Balance in (6.45) | Pressure scale |
| :--- | :--- | :--- |
| $\mathrm{Re}\sim 1$ | all three terms | either estimate |
| $\mathrm{Re}\gg 1$ | $\rho\,\bar{v}\cdot\nabla\bar{v} = -\nabla P'$ (viscosity negligible) | $\Delta p \sim \rho U^2$ |
| $\mathrm{Re}\ll 1$ | $0 = -\nabla P' + \mu\nabla^2\bar{v}$ (acceleration negligible) | $\Delta p \sim \mu U/R$ |

### Scaling for $\mathrm{Re}\gtrsim 1$

With $p^* = (p + \rho g z - P_\infty)/(\rho U^2)$, substitute $\bar{v} = U\bar{v}^*$, $\bar{x} = R\bar{x}^*$, $\nabla = \nabla^*/R$, $P' = \rho U^2 p^*$ in each term of (6.39):

$$ \rho\,\bar{v}\cdot\nabla\bar{v} = \frac{\rho U^2}{R}\,\bar{v}^*\cdot\nabla^*\bar{v}^*, \qquad \nabla P' = \frac{\rho U^2}{R}\nabla^* p^*, \qquad \mu\nabla^2\bar{v} = \frac{\mu U}{R^2}\nabla^{*2}\bar{v}^* $$

Dividing by $\rho U^2/R$, the viscous term carries $\mu U/R^2 \div \rho U^2/R = \mu/(\rho U R) = 1/\mathrm{Re}$. The problem (6.39) becomes (Notes.pdf, Eq. 6.47)

$$ \nabla^*\cdot\bar{v}^* = 0, \quad \bar{v}^*\cdot\nabla^*\bar{v}^* = -\nabla^* p^* + \frac{1}{\mathrm{Re}}\nabla^{*2}\bar{v}^*; \qquad \lvert\bar{x}^*\rvert\to\infty:\; p^* = 0,\; \bar{v}^* = \bar{e}_x; \qquad \lvert\bar{x}^*\rvert = 1:\; \bar{v}^* = 0 \tag{6.47} $$

In the force (6.42), $P'\,d\sigma = \rho U^2 R^2\,p^*\,d\sigma^*$ and the viscous stress is $\mu(U/R)(\nabla^*\bar{v}^* + \nabla^*\bar{v}^{*T})$, which times $d\sigma = R^2 d\sigma^*$ gives $\mu U R\,(\dots)\,d\sigma^*$. Dividing by $\rho U^2 R^2$ (Notes.pdf, Eq. 6.48):

$$ \frac{F_x}{\rho U^2 R^2} = -\int_{\lvert\bar{x}^*\rvert = 1} p^*\,\bar{n}\cdot\bar{e}_x\,d\sigma^* + \frac{1}{\mathrm{Re}}\int_{\lvert\bar{x}^*\rvert = 1}\left[(\nabla^*\bar{v}^* + \nabla^*\bar{v}^{*T})\cdot\bar{n}\right]\cdot\bar{e}_x\,d\sigma^* \tag{6.48} $$

The only parameter left is $\mathrm{Re}$: $F_x/(\rho U^2R^2)$ is a function of $\mathrm{Re}$ alone, exactly (6.35).

> [!note] Reference in the notes (p. 68)
> The notes say that this scaling reduces "(6.40)"; the problem being scaled is the system (6.39) (the field equations and boundary conditions), while the force is (6.42). The same applies to the sentence before (6.49).

### Scaling for $\mathrm{Re}\lesssim 1$

With $p^* = (p + \rho g z - P_\infty)/(\mu U/R)$, now $\nabla P' = (\mu U/R^2)\nabla^* p^*$; dividing every term by $\mu U/R^2$, the convective term carries $\rho U^2/R \div \mu U/R^2 = \mathrm{Re}$ (Notes.pdf, Eq. 6.49):

$$ \nabla^*\cdot\bar{v}^* = 0, \quad \mathrm{Re}\,\bar{v}^*\cdot\nabla^*\bar{v}^* = -\nabla^* p^* + \nabla^{*2}\bar{v}^*; \qquad \lvert\bar{x}^*\rvert\to\infty:\; p^* = 0,\; \bar{v}^* = \bar{e}_x; \qquad \lvert\bar{x}^*\rvert = 1:\; \bar{v}^* = 0 \tag{6.49} $$

and the force, divided by $\mu U R$ (Notes.pdf, Eq. 6.50):

$$ \frac{F_x}{\mu U R} = -\int_{\lvert\bar{x}^*\rvert = 1} p^*\,\bar{n}\cdot\bar{e}_x\,d\sigma^* + \int_{\lvert\bar{x}^*\rvert = 1}\left[(\nabla^*\bar{v}^* + \nabla^*\bar{v}^{*T})\cdot\bar{n}\right]\cdot\bar{e}_x\,d\sigma^* \tag{6.50} $$

so $F_x/(\mu U R)$ is a function of $\mathrm{Re}$ only, the result (6.43).

> [!tip] Π theorem or nondimensional equations?
> Both give the same groups, but the equations tell you **which parameters really enter** (no spurious $P_\infty$ or $g$) and **which terms are small** in each limit. The $\Pi$ theorem alone cannot do either. Problem DA14 compares the two methods on the rotating cavity.

---

## 7. Selection of Parameters with Independent Dimensions

### The rule

The set $a_1,\dots,a_k$ should contain parameters with a **significant influence** for the flow considered (Notes.pdf, p. 68). For the sphere, $R$ and $U$ obviously matter. The third one:

- if viscosity is important, $\mu$, which leads to (6.43);
- if viscosity is not expected to matter, $\rho$, which leads to (6.35).

Evaluate $\mathrm{Re} = \rho U_c L_c/\mu$ with the characteristic velocity and size: $\mathrm{Re}\lesssim 1$ suggests $(U_c, L_c, \mu)$; $\mathrm{Re}\gtrsim 1$ suggests $(U_c, L_c, \rho)$.

### The two extreme limits

For $\mathrm{Re}\gg 1$ the $1/\mathrm{Re}$ term of (6.47)-(6.48) disappears, so the dimensionless force no longer depends on $\mathrm{Re}$ (Notes.pdf, Eq. 6.51):

$$ \lim_{\mathrm{Re}\gg 1}\frac{F_x}{\rho U^2 R^2} = C_1 \tag{6.51} $$

For $\mathrm{Re}\ll 1$ the $\mathrm{Re}$ term of (6.49) disappears (Notes.pdf, Eq. 6.52):

$$ \lim_{\mathrm{Re}\ll 1}\frac{F_x}{\mu U R} = C_2 \tag{6.52} $$

With the "wrong" set, the limit still depends on $\mathrm{Re}$. Since $\frac{F_x}{\rho U^2R^2} = \frac{F_x}{\mu U R}\cdot\frac{\mu U R}{\rho U^2 R^2} = \frac{F_x}{\mu U R}\cdot\frac{1}{\mathrm{Re}}$, (6.52) gives (Notes.pdf, Eq. 6.53)

$$ \lim_{\mathrm{Re}\ll 1}\frac{F_x}{\rho U^2 R^2} = C_2\,\mathrm{Re}^{-1} \tag{6.53} $$

and, since $\frac{F_x}{\mu U R} = \frac{F_x}{\rho U^2R^2}\cdot\mathrm{Re}$, (6.51) gives (Notes.pdf, Eq. 6.54)

$$ \lim_{\mathrm{Re}\gg 1}\frac{F_x}{\mu U R} = C_1\,\mathrm{Re} \tag{6.54} $$

![[attachments/FM-T6/t6-drag-limits.svg]]

In dimensional terms: for $\mathrm{Re}\ll 1$, $F_x = C_2\,\mu U R$ (drag linear in $U$, independent of $\rho$); for $\mathrm{Re}\gg 1$, $F_x = C_1\,\rho U^2 R^2$ (drag quadratic in $U$, independent of $\mu$).

> [!note] Typing slip in the notes (p. 69)
> Before (6.51) the notes write "$F_x/(\rho U R^2)$ becomes independent of $Re$"; the quantity is $F_x/(\rho U^2 R^2)$, as in (6.51).

### General form of the limits

When one group of (6.25) takes extreme values, say $\Pi_1\gg 1$, two things can happen (Notes.pdf, Eqs. 6.55-6.56):

$$ \lim_{\Pi_1\gg 1}\Pi_0(\Pi_1,\dots,\Pi_{n-k}) = f(\Pi_2,\dots,\Pi_{n-k}) \tag{6.55} $$

$$ \lim_{\Pi_1\gg 1}\Pi_0(\Pi_1,\dots,\Pi_{n-k}) = \Pi_1^{\lambda}\,f(\Pi_2,\dots,\Pi_{n-k}) \tag{6.56} $$

In (6.55) one parameter disappears; in (6.56) it survives only as a power, with $\lambda$ to be found. A good choice of $a_1,\dots,a_k$ usually gives the simpler form (6.55).

> [!tip] Exam practice
> In the problems, "simplify assuming the viscosity has a negligible effect" means: use $\rho$ (not $\mu$) in the repeating set, then drop the group that contains $\mu$. Always finish by **checking** the assumption with numbers: $\mathrm{Re}\gg 1$ for both the model and the real system (DA1, DA6, DA12).

---

## 8. Physical Similarity

### Designing an experiment

A full-scale phenomenon often cannot be reproduced in the laboratory. Example of the notes: the drag $F_1$ on a sphere of radius $R_1$ moving at $U_1$ in an oil ($\rho_1$, $\mu_1$), to be measured in a water tunnel ($\rho_2$, $\mu_2$) with the only available spheres, of radius $R_2 \neq R_1$ (Notes.pdf, p. 70).

By (6.35), $F_x/(\rho U^2R^2)$ depends only on $\mathrm{Re}$. If the experiment has the same Reynolds number, $\rho_2U_2R_2/\mu_2 = \rho_1U_1R_1/\mu_1$, solving for $U_2$ (Notes.pdf, Eq. 6.57):

$$ U_2 = \frac{\mu_2}{\mu_1}\,\frac{\rho_1}{\rho_2}\,\frac{R_1}{R_2}\,U_1 \tag{6.57} $$

Then the dimensionless forces are equal (Notes.pdf, Eq. 6.58):

$$ \frac{F_1}{\rho_1U_1^2R_1^2} = \frac{F_2}{\rho_2U_2^2R_2^2} \tag{6.58} $$

and the measured $F_2$ gives the real force (Notes.pdf, Eq. 6.59):

$$ F_1 = \frac{\rho_1U_1^2R_1^2}{\rho_2U_2^2R_2^2}\,F_2 \tag{6.59} $$

### The general rule

For $\Pi_0 = F(\Pi_1,\dots,\Pi_{n-k})$, the model does not have to reproduce $a_1,\dots,a_n$. It is **physically similar** to the real system when every governing group $\Pi_1,\dots,\Pi_{n-k}$ takes the same value in both; then $\Pi_0$ is equal too, and the measured $a_0$ is converted to the real one by equating $\Pi_0$ (Notes.pdf, p. 71).

When not all groups can be matched, similarity is **partial**: match the groups that dominate the problem and accept different values of the secondary ones (Notes.pdf, p. 71).

### Extension: why Reynolds and Froude cannot both be matched with the same fluid

This subsection is an **extension** used in problems DA1 and DA3. A ship or a stirred free surface depends on $\mathrm{Re} = UL/\nu$ (with $\nu = \mu/\rho$) and on the Froude number $\mathrm{Fr} = U/\sqrt{gL}$. Model $m$, prototype $p$, scale $\lambda = L_m/L_p$, same $g$:

$$ \mathrm{Fr}_m = \mathrm{Fr}_p \;\Longrightarrow\; \frac{U_m}{U_p} = \sqrt{\frac{L_m}{L_p}} = \lambda^{1/2}, \qquad \mathrm{Re}_m = \mathrm{Re}_p \;\Longrightarrow\; \frac{U_m}{U_p} = \frac{\nu_m}{\nu_p}\,\frac{L_p}{L_m} = \frac{\nu_m}{\nu_p}\,\lambda^{-1} $$

Equating both velocity ratios: $\nu_m/\nu_p = \lambda^{3/2}$. With the same fluid ($\nu_m = \nu_p$) this forces $\lambda = 1$: no scaled model can match both. The two ways out are those of the problems:

- **neglect viscosity** when $\mathrm{Re}\gg 1$ in model and prototype, and match only Froude (DA1, DA6, DA11);
- **change the fluid** so that $\nu_m = \lambda^{3/2}\nu_p$ (DA3, tar replaced by water).

---

## 9. Practical Formulary of Topic 6

### Dimensions in $[M, L, T, \Theta]$

| Quantity | Symbol | Dimensions |
| :--- | :--- | :--- |
| Velocity | $U$ | $LT^{-1}$ |
| Acceleration, gravity | $g$ | $LT^{-2}$ |
| Angular velocity, frequency | $\Omega$, $f$ | $T^{-1}$ |
| Volume flux (3-D); per unit width (2-D) | $Q$; $q$ | $L^3T^{-1}$; $L^2T^{-1}$ |
| Density | $\rho$ | $ML^{-3}$ |
| Dynamic viscosity | $\mu$ | $ML^{-1}T^{-1}$ |
| Kinematic viscosity | $\nu = \mu/\rho$ | $L^2T^{-1}$ |
| Pressure, stress | $p$, $\tau$ | $ML^{-1}T^{-2}$ |
| Pressure gradient | $P_l = -\partial p/\partial x$ | $ML^{-2}T^{-2}$ |
| Force; force per unit length | $F$; $F/L$ | $MLT^{-2}$; $MT^{-2}$ |
| Energy, torque | $E$, $M$ | $ML^2T^{-2}$ |
| Power | $W$ | $ML^2T^{-3}$ |
| Speed of sound | $c$ | $LT^{-1}$ |
| Temperature (extension) | $T$ | $\Theta$ |
| Thermal conductivity (extension) | $k$ | $MLT^{-3}\Theta^{-1}$ |
| Specific heat (extension) | $c_p$ | $L^2T^{-2}\Theta^{-1}$ |

### Dimensionless numbers

Only the Reynolds number is defined in Chapter 6; the others are **extensions**, given here because the problems use them.

| Number | Definition | Measures | Where |
| :--- | :--- | :--- | :--- |
| Reynolds | $\mathrm{Re} = \rho U L/\mu = UL/\nu$ | convection / viscous forces | Eq. (6.44), (6.46) |
| Froude (extension) | $\mathrm{Fr} = U/\sqrt{gL}$ | inertia / gravity | DA1, DA3, DA6, DA11, DA13 |
| Mach (extension) | $\mathrm{Ma} = U/c$ | flow speed / speed of sound | DA9, DA12 |
| Strouhal (extension) | $\mathrm{St} = fL/U$ | unsteadiness / convection | DA2 (shedding period) |
| Euler (extension) | $\mathrm{Eu} = \Delta p/(\rho U^2)$ | pressure differences / dynamic pressure | scaling of (6.47) |
| Prandtl (extension) | $\mathrm{Pr} = \mu c_p/k$ | momentum / heat diffusion | energy equation |
| Eckert (extension) | $\mathrm{Ec} = U^2/(c_p\,\Delta T)$ | kinetic energy / enthalpy differences | energy equation |

### Key results

| Situation | Result | Source |
| :--- | :--- | :--- |
| Independent dimensions | rank of the exponent matrix $= k$ | Eqs. (6.10)-(6.12) |
| Π theorem | $a_0 = f(a_1,\dots,a_n) \;\Rightarrow\; \Pi_0 = F(\Pi_1,\dots,\Pi_{n-k})$ | Eqs. (6.13)-(6.25) |
| $k = n$ (no group left) | $\Pi_0 = C$, constant | Eqs. (6.6)-(6.7), (6.28) |
| Pipe flow | $P_l D^5/(\rho Q^2) = F\left(\mu D/(\rho Q)\right)$ | Eq. (6.24) |
| Strong explosion | $r_o = C_1E^{1/5}\rho_a^{-1/5}t^{2/5}$, $p_o = C_2E^{2/5}\rho_a^{3/5}t^{-6/5}$ | Eq. (6.29) |
| Reduced pressure removes $g$ and $P_\infty$ | $P' = p + \rho g z - P_\infty$ (not with a free surface) | Eq. (6.39) |
| Sphere drag | $F_x/(\rho U^2R^2) = f(\mathrm{Re})$, or $F_x/(\mu UR) = f(\mathrm{Re})$ | Eqs. (6.35), (6.43) |
| $\mathrm{Re}\gg 1$ | $F_x = C_1\rho U^2R^2$; pressure scale $\rho U^2$ | Eqs. (6.47), (6.51) |
| $\mathrm{Re}\ll 1$ | $F_x = C_2\mu UR$; pressure scale $\mu U/R$ | Eqs. (6.49), (6.52) |
| Similarity | equal $\Pi_1,\dots,\Pi_{n-k}$ $\Rightarrow$ equal $\Pi_0$ | Eqs. (6.57)-(6.59) |
| Re and Fr with the same $g$ (extension) | needs $\nu_m/\nu_p = (L_m/L_p)^{3/2}$ | Section 8 |

### Exam recipe

1. **List the parameters.** Write the unknown $a_0$ and everything it depends on. In doubt, write the equations and boundary conditions: geometry, velocities or rotation rates imposed at the boundaries, fluid properties that appear ($\rho$, $\mu$; $c$ for a gas at high speed; $g$ only with a free surface or a weight). Count $n$.
2. **Build the exponent matrix** (rows: parameters; columns: $M$, $L$, $T$) and find $k$ with a non-zero determinant.
3. **Choose the repeating set** of $k$ parameters: those that clearly matter. Use $\rho$ if viscosity is expected to be negligible ($\mathrm{Re}\gg 1$), $\mu$ if inertia is ($\mathrm{Re}\ll 1$). Never put the unknown in the set.
4. **Form each Π** by solving the system of exponents, one equation per fundamental unit, and check that each group is dimensionless.
5. **Simplify with the limits** stated in the problem: drop the group that contains the negligible parameter (6.55), or keep it as a power (6.56) when the set was not the natural one.
6. **Similarity.** Equate every remaining governing group between model and prototype to get the test conditions (velocity, rotation rate, fluid, mass). Equate $\Pi_0$ to convert the measurement. If two groups cannot both be matched, match the dominant one and check numerically that the neglected group is extreme in both systems.
7. **Tables of measurements.** Each row of a model table maps to a prototype row through the same scale factors (one for the independent variable, one for the unknown).
8. **Check** the dimensions of the final formula and its limits.

**Back to:** [[01 - Fluid Mechanics/Fluid Mechanics MOC|Fluid Mechanics MOC]]
