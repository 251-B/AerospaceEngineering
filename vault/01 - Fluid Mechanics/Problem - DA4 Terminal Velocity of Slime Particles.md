---
materia: Fluid Mechanics
tema: "Topic 6: Dimensional Analysis"
tags:
  - problema-examen
  - analisis-dimensional
  - teorema-pi
  - semejanza-fisica
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-06-dimensional-analysis/problemas/DA4.pdf"
id: "da4"
pill: "DA4: Settling particles"
sheets:
  - 4
tags_html:
  - "Π theorem"
  - "Change of fluid"
  - "Terminal velocity"
---

# Problem DA4: Terminal Velocity of Slime Particles

> Official dimensional-analysis sheet of the course, statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 6 - Dimensional Analysis]].
> Method: Π theorem (Notes.pdf, Eq. 6.25) and physical similarity with a different liquid (Eqs. 6.57-6.59).

## Statement

Chemical and hydraulic engineers are often interested in computing the settling velocity of a suspension of particulates in a given liquid. For dilute suspensions, a variable that is directly related with this settling velocity is the so-called terminal velocity, $u_t$, which is the constant falling velocity of an isolated particle moving in an infinite fluid under the action of gravity. For the particular case of slime sedimentation in a river, the slime particles are spheres of average diameter $D_s = 30\ \mu$m and average mass $m_s = 0.2\ \mu$g, much too small to be handled in the lab. To guide the design of an experiment to determine $u_t$, the following steps are suggested:

1. Use the Π theorem to reduce the parametric dependence of the terminal velocity.

2. To enable the use of larger particles in the experiment, explore the replacement of water with glicerine ($\nu_g/\nu_w = 680$, $\rho_g/\rho_w = 1.25$) and find the corresponding values of the diameter $D_e$ and mass $m_e$ for the resulting experimental particle.

3. For this particle, the experimental measurements give $u_e = 10^{-3}$ m/s. Obtain the terminal velocity for an average slime particle.

Source: DA4.pdf (page 1, statement and handwritten key). Notes.pdf, Chapter 6: Π theorem, Eq. 6.25; physical similarity, Eqs. 6.57-6.59.

## Hypotheses, Data and Dimensional Table

- At terminal velocity the particle does not accelerate: its weight, the buoyancy and the drag balance. The weight enters through $m g$, the buoyancy through $\rho g$ times the volume ($\propto D^3$), the drag through $\rho$, $\mu$, $D$ and $u_t$.
- The particle is a sphere in an unbounded liquid: no free surface, no walls.

| Parameter | Meaning | Dimensions |
| :--- | :--- | :--- |
| $u_t$ | terminal velocity (unknown) | $LT^{-1}$ |
| $D$ | particle diameter | $L$ |
| $m$ | particle mass | $M$ |
| $g$ | gravity | $LT^{-2}$ |
| $\rho$ | liquid density | $ML^{-3}$ |
| $\mu$ | liquid viscosity | $ML^{-1}T^{-1}$ |

## Application of the Π Theorem

$$ u_t = u_t(D, m, g, \rho, \mu) $$

$n = 5$. The key takes $(D, g, \rho)$: rows $D(1, 0, 0)$, $g(1, 0, -2)$, $\rho(-3, 1, 0)$ in $(L, M, T)$, with $\det = 1\cdot(0\cdot 0 - (-2)\cdot 1) - 0 + 0 = 2 \neq 0$, so $k = 3$ and two groups remain.

**Velocity.** $[u_t] = [D]^a[g]^b$: $T:\; -1 = -2b$, so $b = 1/2$; $L:\; 1 = a + b$, so $a = 1/2$: the scale $\sqrt{gD}$.

**Mass.** $[m] = [\rho][D]^3$: the group $m/(\rho D^3)$, the ratio of the particle density to the liquid density up to the factor $\pi/6$.

**Viscosity.** $[\mu] = [\rho]^a[g]^b[D]^c$: $M:\; 1 = a$; $T:\; -1 = -2b$, so $b = 1/2$; $L:\; -1 = -3a + b + c = -3 + \tfrac{1}{2} + c$, so $c = 3/2$: the group $\mu/(\rho g^{1/2}D^{3/2}) = \nu/(g^{1/2}D^{3/2})$.

$$ \frac{u_t}{\sqrt{g D}} = f\left(\frac{m}{\rho D^3}, \frac{\mu}{\rho g^{1/2} D^{3/2}}\right) $$

## Physical Similarity in Glycerine

Subscript $s$ for the slime particle in water ($\rho_w$, $\nu_w$), $e$ for the experiment in glycerine ($\rho_g$, $\nu_g$); same $g$. Both groups must be equal.

**Viscosity group:**

$$ \frac{\nu_w}{g^{1/2}D_s^{3/2}} = \frac{\nu_g}{g^{1/2}D_e^{3/2}} \;\Longrightarrow\; \left(\frac{D_e}{D_s}\right)^{3/2} = \frac{\nu_g}{\nu_w} \;\Longrightarrow\; D_e = \left(\frac{\nu_g}{\nu_w}\right)^{2/3}D_s $$

$680^{2/3} = \exp\left(\tfrac{2}{3}\ln 680\right) = \exp(4.348) = 77.33$, so

$$ D_e = 77.33\times 30\ \mu\text{m} = 2320\ \mu\text{m} = 2.32\ \text{mm} $$

**Mass group:**

$$ \frac{m_s}{\rho_w D_s^3} = \frac{m_e}{\rho_g D_e^3} \;\Longrightarrow\; m_e = \frac{\rho_g}{\rho_w}\left(\frac{D_e}{D_s}\right)^3 m_s = 1.25\times 77.33^3\times 0.2\ \mu\text{g} $$

$77.33^3 = 4.624\times 10^{5}$, so $m_e = 1.25\times 4.624\times 10^{5}\times 0.2\ \mu\text{g} = 1.156\times 10^{5}\ \mu\text{g} = 0.116$ g. The experimental particle is a sphere of 2.3 mm and about 0.12 g, easy to handle.

## Terminal Velocity of the Slime

With both groups equal, the dimensionless velocity is equal:

$$ \frac{u_t}{\sqrt{g D_s}} = \frac{u_e}{\sqrt{g D_e}} \;\Longrightarrow\; u_t = \left(\frac{D_s}{D_e}\right)^{1/2}u_e = \left(\frac{1}{77.33}\right)^{1/2}\times 10^{-3}\ \text{m/s} $$

$$ u_t = 0.1137\times 10^{-3}\ \text{m/s} = 0.1137\ \text{mm/s} $$

## Answers and Checks

- Reduced law: $u_t/\sqrt{gD} = f\left(m/(\rho D^3),\, \mu/(\rho g^{1/2}D^{3/2})\right)$.
- Experimental particle: $D_e = 2.32$ mm, $m_e = 0.116$ g.
- Slime terminal velocity: $u_t = 0.114$ mm/s.
- Dimensions: $\nu/(g^{1/2}D^{3/2})$ is $L^2T^{-1}/(L^{1/2}T^{-1}\cdot L^{3/2}) = 1$.
- Consistency: equal $m/(\rho D^3)$ means the particle-to-liquid density ratio is the same in both systems, so the net weight per unit volume scales with the liquid density, as it must for the same balance of weight, buoyancy and drag.
- Check against the official key: DA4.pdf gives $D_e = 2.32$ mm and $u_t = 0.1137$ mm/s; the key writes $m_e = (\rho_g/\rho_w)(D_e/D_s)^3 m_s$ without the number, which is 0.116 g.
