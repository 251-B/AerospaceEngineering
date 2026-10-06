---
subject: Mechanics Applied to Aerospace Engineering
topic: 4 - Angular Momentum and Central Forces
concept: Binet Equation and Conic Section Trajectories
tags:
  - concept
  - binet-equation
  - conic-sections
  - kepler-first-law
  - orbital-eccentricity
---

# Concept: Binet Equation and Conic Section Trajectories

## 1. Binet Coordinate Transformation (Slide 13, Notes 8.4)
To eliminate time $t$ in favor of polar angle $\theta$, define the reciprocal radius:
$$ u(\theta) \equiv \frac{1}{r(\theta)} $$
Using $h = r^2\dot{\theta} \implies \dot{\theta} = h u^2$:
$$ \dot{r} = \frac{dr}{d\theta}\dot{\theta} = -h\frac{du}{d\theta} = -h u' $$
$$ \ddot{r} = \frac{d}{dt}(-h u') = -h u'' \dot{\theta} = -h^2 u^2 u'' $$

Substituting into the radial equation of motion $\ddot{r} - r\dot{\theta}^2 = -\mu u^2$:
$$ -h^2 u^2 u'' - h^2 u^3 = -\mu u^2 \implies \frac{d^2u}{d\theta^2} + u = \frac{\mu}{h^2} $$
This is the **Binet Equation** for an inverse-square central force field.

---

## 2. General Analytical Solution (Kepler's 1st Law)
The Binet ODE has the general solution of a forced harmonic oscillator:
$$ u(\theta) = \frac{\mu}{h^2}\left[1 + e\cos(\theta - \omega)\right] $$
Aligning $\theta = 0$ with pericenter ($\omega = 0$):
$$ r(\theta) = \frac{p}{1 + e\cos\theta} = \frac{h^2/\mu}{1 + e\cos\theta} $$
where $p = h^2/\mu$ is the **semi-latus rectum** and $e \ge 0$ is the **eccentricity**. This is the polar equation of a conic section with focus at origin $O$.

---

## 3. Geometric Classification of Conic Sections (Slide 14)

| Eccentricity | Semi-Major Axis $a$ | Geometric Curve | Orbital Boundness |
| :---: | :---: | :---: | :---: |
| $e = 0$ | $a = p > 0$ | Circle | Bound |
| $0 < e < 1$ | $a > 0$ | Ellipse | Bound (Planets, Satellites) |
| $e = 1$ | $a \to \infty$ | Parabola | Critical escape trajectory |
| $e > 1$ | $a < 0$ | Hyperbola | Unbound (Interplanetary flyby) |

### Ellipse Apsides:
* **Pericenter (Periapsis):** $r_p = a(1 - e) = \frac{p}{1 + e}$ at $\theta = 0$.
* **Apocenter (Apoapsis):** $r_a = a(1 + e) = \frac{p}{1 - e}$ at $\theta = \pi$.
* **Semi-Major Axis:** $2a = r_p + r_a \implies a = \frac{p}{1 - e^2}$.
* **Semi-Minor Axis:** $b = a\sqrt{1 - e^2} = \sqrt{a p}$.
