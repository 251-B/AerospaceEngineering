---
subject: Mechanics Applied to Aerospace Engineering
topic: 4 - Angular Momentum and Central Forces
concept: Kepler Laws and Barycentric Two-Body Reduction
tags:
  - concept
  - kepler-laws
  - two-body-problem
  - barycenter
  - gravitational-parameter
---

# Concept: Kepler Laws and Barycentric Two-Body Reduction

## 1. Empirical Kepler's Laws (Slide 8)
1. **1st Law (Law of Ellipses):** The orbits of planets are ellipses with the primary mass (Sun) at one of the two foci.
2. **2nd Law (Law of Equal Areas):** The radius vector joining the planet to the Sun sweeps out equal areas in equal intervals of time ($dA/dt = \text{const}$).
3. **3rd Law (Harmonic Law):** The square of the orbital period $\tau$ is proportional to the cube of the semi-major axis $a$:
   $$ \tau^2 \propto a^3 $$

---

## 2. Barycentric Frame & Two-Body Reduction (Slides 9–11)
Newtonian gravitational interaction between two masses $m^P$ (satellite/planet) and $m^S$ (Earth/Sun):
$$ m^P \ddot{\mathbf{r}}_0^P = -\frac{G m^P m^S}{\|\mathbf{r}_0^P - \mathbf{r}_0^S\|^3}(\mathbf{r}_0^P - \mathbf{r}_0^S), \qquad m^S \ddot{\mathbf{r}}_0^S = +\frac{G m^P m^S}{\|\mathbf{r}_0^P - \mathbf{r}_0^S\|^3}(\mathbf{r}_0^P - \mathbf{r}_0^S) $$

Summing both equations (the internal forces cancel) shows that the center of mass (barycenter $G$, $\mathbf{r}_0^G = (m^P\mathbf{r}_0^P + m^S\mathbf{r}_0^S)/(m^S + m^P)$) has zero acceleration:
$$ (m^S + m^P)\ddot{\mathbf{r}}_0^G = \mathbf{0} \implies \mathbf{r}_0^G(t) = \mathbf{r}_0^G(0) + \mathbf{v}_0^G t \implies \text{Frame } S_G \text{ is inertial} $$

### Relative Coordinate Equation:
Defining relative position $\mathbf{r} \equiv \mathbf{r}_0^P - \mathbf{r}_0^S$:
$$ \frac{d^2\mathbf{r}}{dt^2} = -\frac{G(m^S + m^P)}{r^3}\mathbf{r} = -\frac{\mu}{r^3}\mathbf{r} $$
where $\mu \equiv G(m^S + m^P)$ is the **standard gravitational parameter**. The step is: divide the first equation by $m^P$, the second by $m^S$, and subtract.

### Reduced Mass:
Multiplying by $m_{\text{red}} = \dfrac{m^P m^S}{m^P + m^S}$ gives $m_{\text{red}}\ddot{\mathbf{r}} = -\dfrac{G m^P m^S}{r^2}\mathbf{e}_r$: the relative vector moves like one particle of mass $m_{\text{red}}$ around a fixed center. The individual bodies are $\mathbf{r}_0^P = \mathbf{r}_0^G + \frac{m^S}{m^S + m^P}\mathbf{r}$ and $\mathbf{r}_0^S = \mathbf{r}_0^G - \frac{m^P}{m^S + m^P}\mathbf{r}$.

In orbital mechanics where $m^S \gg m^P$:
$$ \mu \approx G m^S $$
For Earth: $\mu_\oplus = G M_\oplus \approx 3.986 \times 10^{14}\,\text{m}^3/\text{s}^2$.

---

## 3. Specific Angular Momentum & Kepler's 2nd Law (Slide 12)
In polar coordinates $(r, \theta)$:
$$ \mathbf{a} = (\ddot{r} - r\dot{\theta}^2)\mathbf{e}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\mathbf{e}_\theta = -\frac{\mu}{r^2}\mathbf{e}_r $$
Transverse projection:
$$ r\ddot{\theta} + 2\dot{r}\dot{\theta} = \frac{1}{r}\frac{d}{dt}(r^2\dot{\theta}) = 0 \implies h \equiv r^2\dot{\theta} = \text{constant} $$
The areal velocity is constant:
$$ \frac{dA}{dt} = \frac{1}{2}r^2\dot{\theta} = \frac{h}{2} = \text{constant} \quad \text{(Kepler's 2nd Law)} $$
