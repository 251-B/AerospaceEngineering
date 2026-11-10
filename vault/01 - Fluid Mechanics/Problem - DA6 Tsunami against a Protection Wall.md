---
materia: Fluid Mechanics
tema: "Topic 6: Dimensional Analysis"
tags:
  - problema-examen
  - analisis-dimensional
  - teorema-pi
  - semejanza-fisica
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-06-dimensional-analysis/problemas/DA6.pdf"
id: "da6"
pill: "DA6: Tsunami wall"
sheets:
  - 6
tags_html:
  - "Π theorem"
  - "Froude similarity"
  - "Re ≫ 1"
---

# Problem DA6: Tsunami against a Protection Wall

> Official dimensional-analysis sheet of the course (exam of 28-06-2010), statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 6 - Dimensional Analysis]].
> Method: Π theorem (Notes.pdf, Eq. 6.25), the limit of negligible viscosity (Eq. 6.55) and Froude similarity (Eqs. 6.57-6.59).

## Statement

A protection wall against *tsunamis* is to be built at the coast. An experiment is to be conducted to evaluate the impact force that the tsunami, assumed to be of height $h$, may exert on the wall, of height $H$. To guide the design and analysis of the experiment, follow these steps:

- Use the Π theorem to simplify the parametric dependence of the *tsunami* velocity $U$. (2 points)
- Use the Π theorem to simplify the parametric dependence of the impact force **per unit width of wall** $F$. (2 points)
- Simplify the above relationships assuming that the viscosity has a negligible effect. Indicate the condition that needs to be satisfied. (1 point)

The real wall has a height $H = 3$ m and is to be designed to withstand *tsunamis* of height $h = 2$ m. If the laboratory model has a height $H' = 0.3$ m:

- Determine the laboratory value of the tsunami height $h'$ necessary to guarantee physical similarity. (2 points)
- For that value, the laboratory measurements provide $F' = 1500$ N/m and $U' = 2$ m/s. Determine the values of $F$ and $U$ for the real tsunami. (2 points)
- Verify the hypotheses of negligible viscosity for the model and for the real tsunami. (1 point)

![[attachments/FM-T6/da6-statement.svg]]
*Statement figure (redrawn from DA6.pdf): a tsunami of height h travelling with velocity U towards a coastal protection wall of height H; the unknowns are U and the impact force per unit width of wall F*

Source: DA6.pdf (page 1, exam of 28-06-2010, statement and handwritten key). Notes.pdf, Chapter 6: Π theorem, Eq. 6.25; limits, Eq. 6.55; physical similarity, Eqs. 6.57-6.59.

## Hypotheses, Data and Dimensional Table

- The tsunami is a gravity wave: the free surface is far from flat, so $g$ is essential (Notes.pdf, p. 66).
- The velocity of the wave is set by the wave itself, before it meets the wall: $U$ depends on $\rho$, $g$, $h$, $\mu$ but not on $H$. The force on the wall depends on the wall height too.
- Same liquid (water) in the model and in the sea: $\nu \simeq 10^{-6}$ m$^2$/s; same $g$. The coastal geometry is reproduced to scale.

| Parameter | Dimensions |
| :--- | :--- |
| $U$ (unknown) | $LT^{-1}$ |
| $F$ per unit width (unknown) | $MT^{-2}$ |
| $\rho$ | $ML^{-3}$ |
| $g$ | $LT^{-2}$ |
| $h$, $H$ | $L$ |
| $\mu$ | $ML^{-1}T^{-1}$ |

## Application of the Π Theorem

### Tsunami velocity

$$ U = U(\rho, g, h, \mu) $$

$n = 4$. The key takes $(\rho, g, h)$: rows $\rho(-3, 1, 0)$, $g(1, 0, -2)$, $h(1, 0, 0)$, $\det = -3(0) - 1\cdot(1\cdot 0 - (-2)\cdot 1) + 0 = -2 \neq 0$, so $k = 3$ and one group remains.

**Velocity.** $[U] = [g]^b[h]^c$: $T:\; -1 = -2b$; $L:\; 1 = b + c$; so $b = c = 1/2$, the scale $\sqrt{gh}$.

**Viscosity.** $[\mu] = [\rho]^a[g]^b[h]^c$: $M:\; 1 = a$; $T:\; -1 = -2b$, $b = 1/2$; $L:\; -1 = -3 + \tfrac{1}{2} + c$, $c = 3/2$; the group $\mu/(\rho g^{1/2}h^{3/2})$.

$$ \frac{U}{\sqrt{g h}} = f_1\left(\frac{\mu}{\rho g^{1/2}h^{3/2}}\right) $$

### Force per unit width

$$ F = F(\rho, g, h, H, \mu) $$

$n = 5$, $k = 3$ with the same set. **Force.** $[F] = MT^{-2} = [\rho]^a[g]^b[h]^c$: $M:\; 1 = a$; $T:\; -2 = -2b$, $b = 1$; $L:\; 0 = -3 + 1 + c$, $c = 2$: the scale $\rho g h^2$ (the hydrostatic force per unit width on a height $h$, up to the factor $1/2$). The wall gives $H/h$.

$$ \frac{F}{\rho g h^2} = f_2\left(\frac{\mu}{\rho g^{1/2}h^{3/2}}, \frac{H}{h}\right) $$

### Negligible viscosity

The group $\mu/(\rho g^{1/2}h^{3/2}) = \nu/(g^{1/2}h^{3/2})$ is the inverse of a Reynolds number built with the velocity $\sqrt{gh}$ and the length $h$. If

$$ \frac{\mu}{\rho g^{1/2}h^{3/2}} \ll 1 $$

viscosity has a negligible effect and the group drops out (Notes.pdf, Eq. 6.55):

$$ \frac{U}{\sqrt{g h}} = f_1 = \text{constant}, \qquad \frac{F}{\rho g h^2} = f_2\left(\frac{H}{h}\right) $$

## Physical Similarity

Without viscosity only $H/h$ must be matched:

$$ \frac{H}{h} = \frac{H'}{h'} \;\Longrightarrow\; h' = \frac{H'}{H}\,h = \frac{0.3}{3}\times 2 = 0.2\ \text{m} $$

Then $U/\sqrt{gh}$ and $F/(\rho g h^2)$ are the same in the model and in the sea (same $\rho$ and $g$):

$$ \frac{U}{\sqrt{g h}} = \frac{U'}{\sqrt{g h'}} \;\Longrightarrow\; U = \sqrt{\frac{h}{h'}}\,U' = \sqrt{10}\times 2 = 6.32\ \text{m/s} $$

$$ \frac{F}{\rho g h^2} = \frac{F'}{\rho g h'^2} \;\Longrightarrow\; F = \left(\frac{h}{h'}\right)^2 F' = 100\times 1500 = 1.5\times 10^{5}\ \text{N/m} = 150\ \text{kN/m} $$

## Check of Negligible Viscosity

With $\nu = 10^{-6}$ m$^2$/s and $g = 9.81$ m/s$^2$ ($g^{1/2} = 3.13$ m$^{1/2}$/s):

$$ \text{real: } \frac{\nu}{g^{1/2}h^{3/2}} = \frac{10^{-6}}{3.13\times 2^{3/2}} = \frac{10^{-6}}{3.13\times 2.83} = 1.1\times 10^{-7} \ll 1 $$

$$ \text{model: } \frac{\nu}{g^{1/2}h'^{3/2}} = \frac{10^{-6}}{3.13\times 0.2^{3/2}} = \frac{10^{-6}}{3.13\times 0.0894} = 3.6\times 10^{-6} \ll 1 $$

Both are very small: neglecting viscosity is justified in both, which is what makes the Froude model valid even though the two "Reynolds numbers" differ by a factor 30.

## Answers and Checks

- $U/\sqrt{gh} = f_1\left(\mu/(\rho g^{1/2}h^{3/2})\right)$ and $F/(\rho g h^2) = f_2\left(\mu/(\rho g^{1/2}h^{3/2}),\, H/h\right)$.
- With $\mu/(\rho g^{1/2}h^{3/2}) \ll 1$: $U/\sqrt{gh}$ constant and $F/(\rho g h^2) = f_2(H/h)$.
- Model wave height $h' = 0.2$ m; real tsunami $U = 6.32$ m/s and $F = 150$ kN/m.
- Viscosity groups: $1.1\times 10^{-7}$ (real) and $3.6\times 10^{-6}$ (model), both $\ll 1$.
- Dimensions: $\rho g h^2$ is $ML^{-3}\cdot LT^{-2}\cdot L^2 = MT^{-2}$, a force per unit width.
- Order of magnitude: the hydrostatic force of a 2 m column is $\rho g h^2/2 = 2\times 10^4$ N/m; the impact force is about 7 times larger, reasonable for a breaking wave.
- Check against the official key: DA6.pdf gives $h' = 0.2$ m, $U = 6.32$ m/s, $F = 150\,000$ N/m and the viscosity groups $\simeq 10^{-7}$ and $\simeq 3\times 10^{-6}$, the same results. The key writes the force as $F(\rho g, h, H, \mu)$; since the viscosity group needs $\rho$ and $g$ separately, the list is $(\rho, g, h, H, \mu)$, as used above.
