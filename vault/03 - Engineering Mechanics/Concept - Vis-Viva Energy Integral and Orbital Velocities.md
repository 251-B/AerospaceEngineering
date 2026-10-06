---
subject: Mechanics Applied to Aerospace Engineering
topic: 4 - Angular Momentum and Central Forces
concept: Vis-Viva Energy Integral and Orbital Velocities
tags:
  - concept
  - vis-viva
  - orbital-energy
  - circular-velocity
  - escape-velocity
  - kepler-third-law
---

# Concept: Vis-Viva Energy Integral and Orbital Velocities

## 1. Kepler's Third Law (Harmonic Law) (Slide 15)
Integrating the constant areal velocity $dA/dt = h/2$ over an elliptical orbital period $\tau$:
$$ \frac{h}{2}\tau = A_{\text{ellipse}} = \pi a b = \pi a^2\sqrt{1 - e^2} $$
Using $h = \sqrt{\mu a(1 - e^2)}$:
$$ \tau = \frac{2\pi a^2\sqrt{1 - e^2}}{\sqrt{\mu a(1 - e^2)}} = 2\pi\sqrt{\frac{a^3}{\mu}} \implies \tau^2 = \frac{4\pi^2}{\mu} a^3 $$
The period depends strictly on semi-major axis $a$ and gravitational parameter $\mu$, completely independent of eccentricity $e$.

---

## 2. Vis-Viva Equation (Slides 11, 16, Notes 8.5)
The mass-specific mechanical energy in a Newtonian gravitational field is:
$$ \xi = \frac{1}{2}v^2 - \frac{\mu}{r} = \text{constant} $$

Evaluating $\xi$ at pericenter $r_p = a(1 - e)$ where $v_p = \sqrt{\frac{\mu}{a}\frac{1+e}{1-e}}$:
$$ \xi = -\frac{\mu}{2a} $$
Equating both expressions yields the **Vis-Viva equation**:
$$ v^2 = \mu\left(\frac{2}{r} - \frac{1}{a}\right) $$

### Energy Sign and Orbit Type:
* **$\xi < 0$ ($a > 0$):** Elliptic orbit (bound).
* **$\xi = 0$ ($a \to \infty$):** Parabolic orbit (escape threshold).
* **$\xi > 0$ ($a < 0$):** Hyperbolic orbit (unbound, excess speed $v_\infty = \sqrt{-\mu/a}$).

---

## 3. Fundamental Orbital Velocities (Slide 16)

* **Circular Velocity ($r = a$):**
  $$ v_c = \sqrt{\frac{\mu}{r}} $$
* **Escape Velocity ($a \to \infty$):**
  $$ v_e = \sqrt{\frac{2\mu}{r}} = \sqrt{2}\,v_c $$
* **Periapsis Velocity ($r = r_p = a(1-e)$):**
  $$ v_p = \sqrt{\frac{\mu}{a}\left(\frac{1+e}{1-e}\right)} $$
* **Apoapsis Velocity ($r = r_a = a(1+e)$):**
  $$ v_a = \sqrt{\frac{\mu}{a}\left(\frac{1-e}{1+e}\right)} $$
* **Apsidal Ratio:**
  $$ \frac{v_p}{v_a} = \frac{1+e}{1-e} = \frac{r_a}{r_p} $$
