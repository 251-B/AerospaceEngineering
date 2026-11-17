---
materia: "Aerospace Materials I"
tema: "Topic 10: Composite Materials"
origen: "Problems T10_CompositeMaterials.pdf, Problem 3"
dificultad: hard
badge: "Hybrid composite · specific modulus and strength"
tags:
  - official-problem
  - solved
  - rule-of-mixtures
  - hybrid-composite
  - specific-properties
  - weight-fraction
---

# ✏️ Problem: T10-03 — Graphite-Epoxy and Graphite-Kevlar Hybrid Composite

## 📄 Official Statement
> 3. A composite material has a 69.5% in weight of unidirectional graphite-HM fibers in an epoxy matrix.
> a) Estimate the density and elastic modulus of the composite.
> b) If a 50% of the graphite fibers are replaced with Kevlar fibers, estimate the specific elastic modulus and the specific tensile strength in the longitudinal direction in this new hybrid composite.
> c) Calculate the minimum volumetric fraction of the graphite-HM fibers so that the initial composite has more strength than the hybrid composite of section b).
> d) Do the same calculations as in (c) considering Kevlar fibers.
>
> Data:
>
> | Material | Density g/cm³ | Elastic modulus GPa | Tensile strength MPa |
> | :--- | ---: | ---: | ---: |
> | Epoxy resin | 1.23 | 3.5 | 70 |
> | Graphite-HM fiber | 1.86 | 390 | 2400 |
> | Kevlar-49 fiber | 1.44 | 131 | 3700 |
>
> *(Solution: a) 1.61 g/cm³, 235.4 GPa; b) 106.5×10⁶ m²/s², 1.24×10⁶ m²/s²; c) 0.77; d) 0.49)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Weight to volume.** The composition is given by weight. In 1 g of composite each phase occupies $w_i/\rho_i$; the sum of these volumes is $1/\rho_c$, and $V_i = (w_i/\rho_i)/\sum_j (w_j/\rho_j)$ (definition of density).
2. **Rule of mixtures** along the fibres, for the modulus, the strength and the density, extended term by term to three phases: $P_{CM} = \sum_i f_i p_i$ [Session 22 Slide 27]; isostrain modulus [Session 22 Slide 22]; strength $\sigma_C = \sigma_f V_f + \sigma_m(1 - V_f)$ [Session 22 Slide 26], with the tabulated matrix strength as the matrix term.
3. **Hybrid of part b).** Half of the graphite **volume** is replaced by the same volume of Kevlar, so $V_{gr} = V_K = V_f/2$ and $V_m$ is unchanged.
4. **Specific property** = property / density [Session 21 Slide 43]; in SI, Pa/(kg/m³) = m²/s².
5. **Parts c) and d).** "Initial composite" means the two-phase composite fibre + epoxy with the fibre of each part; its strength must exceed that of the hybrid.

### Data
| Constituent | $\rho$ (g/cm³) | $E$ (GPa) | $\sigma$ (MPa) |
| :--- | ---: | ---: | ---: |
| Epoxy (m) | 1.23 | 3.5 | 70 |
| Graphite-HM (gr) | 1.86 | 390 | 2400 |
| Kevlar 49 (K) | 1.44 | 131 | 3700 |

$w_{gr} = 0.695$, $w_m = 0.305$.

**Unknowns:** (a) $\rho_c$, $E_{1C}$; (b) $E/\rho$ and $\sigma/\rho$ of the hybrid; (c) minimum $V_{gr}$; (d) minimum $V_K$.

---

## 🧠 2. Model and Strategy

[Session 22 Slides 22, 26, 27]:

$$V_i = \frac{w_i/\rho_i}{\sum_j w_j/\rho_j} \qquad \rho_c = \sum_i V_i\rho_i \qquad E_{1C} = \sum_i V_i E_i \qquad \sigma_{1C} = \sum_i V_i\sigma_i$$

**Strategy.**
1. Convert the weight fractions to volume fractions; then density and modulus (a).
2. Split the fibre volume in two halves; density, modulus and strength of the hybrid; divide by the density (b).
3. Set the strength of a two-phase composite equal to the hybrid strength and solve for $V_f$ (c, d).

---

## 🔢 3. Step-by-Step Derivation

### 1. a) Volume fractions, density and modulus [Session 22 Slides 22, 27]
Volumes of the phases in 1 g of composite:

$$\frac{w_{gr}}{\rho_{gr}} = \frac{0.695\ \text{g}}{1.86\ \text{g/cm}^3} = 0.37366\ \text{cm}^3 \qquad \frac{w_m}{\rho_m} = \frac{0.305\ \text{g}}{1.23\ \text{g/cm}^3} = 0.24797\ \text{cm}^3$$

Total volume $0.62163\ \text{cm}^3$, so

$$V_{gr} = \frac{0.37366}{0.62163} = 0.6011 \qquad V_m = 0.3989 \qquad \rho_c = \frac{1\ \text{g}}{0.62163\ \text{cm}^3} = \mathbf{1.609\ g/cm^3}$$

Isostrain modulus:

$$E_{1C} = 0.6011 \times 390\ \text{GPa} + 0.3989 \times 3.5\ \text{GPa} = 234.43 + 1.40 = \mathbf{235.8\ GPa}$$

### 2. b) The hybrid composite [Session 22 Slides 22, 26, 27]
$V_{gr} = V_K = 0.6011/2 = 0.30055$, $V_m = 0.3989$.

$$\rho_h = 0.30055 \times 1.86 + 0.30055 \times 1.44 + 0.3989 \times 1.23 = 0.5590 + 0.4328 + 0.4906 = 1.4825\ \text{g/cm}^3$$

$$E_h = 0.30055 \times 390 + 0.30055 \times 131 + 0.3989 \times 3.5 = 117.21 + 39.37 + 1.40 = 157.98\ \text{GPa}$$

$$\sigma_h = 0.30055 \times 2400 + 0.30055 \times 3700 + 0.3989 \times 70 = 721.3 + 1112.0 + 27.9 = 1861.3\ \text{MPa}$$

Specific values, with $\rho_h = 1482.5\ \text{kg/m}^3$:

$$\frac{E_h}{\rho_h} = \frac{157.98\times10^9\ \text{Pa}}{1482.5\ \text{kg/m}^3} = \mathbf{106.6\times10^6\ m^2/s^2} \qquad \frac{\sigma_h}{\rho_h} = \frac{1861.3\times10^6\ \text{Pa}}{1482.5\ \text{kg/m}^3} = \mathbf{1.26\times10^6\ m^2/s^2}$$

### 3. c) Minimum graphite fraction [Session 22 Slide 26]
Strength of a graphite-epoxy composite with fraction $V$, set greater than the hybrid strength:

$$2400\,V + 70\,(1 - V) > 1861.3 \ \Rightarrow\ 2330\,V > 1791.3 \ \Rightarrow\ V > \frac{1791.3}{2330} = 0.769$$

**$V_{gr,min} = 0.77$.** The initial composite of part a), with $V_{gr} = 0.60$, has $2400 \times 0.6011 + 70 \times 0.3989 = 1470.6$ MPa, weaker than the hybrid.

### 4. d) Minimum Kevlar fraction [Session 22 Slide 26]

$$3700\,V + 70\,(1 - V) > 1861.3 \ \Rightarrow\ 3630\,V > 1791.3 \ \Rightarrow\ V > \frac{1791.3}{3630} = 0.493$$

**$V_{K,min} = 0.49$.**

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $\text{Pa}/(\text{kg/m}^3) = (\text{kg}\,\text{m}^{-1}\text{s}^{-2})/(\text{kg}\,\text{m}^{-3}) = \text{m}^2/\text{s}^2$, the unit of the key.
- **Fractions.** $0.30055 + 0.30055 + 0.3989 = 1.0000$.
- **Trends.** Kevlar is lighter, stronger and less stiff than graphite, so the hybrid is lighter (1.48 against 1.61 g/cm³), less stiff (158 against 236 GPa) and stronger (1861 against 1471 MPa) than the initial composite.
- **c) against d).** Kevlar is the stronger fibre, so it needs a smaller fraction (0.49) than graphite (0.77) to beat the hybrid; both are below 1, so both are possible in principle.

### Interpretation
A hybrid trades stiffness for strength and lower density: replacing half the graphite by Kevlar lowers the specific modulus from $235.8\times10^9/1609 = 146.6\times10^6$ to $106.6\times10^6$ m²/s² but raises the strength by 27 %. To match the hybrid strength with graphite alone, more than 77 vol% of fibre would be needed, above the 50 to 60 % of typical fibre composites [Session 22 Slide 22].

> [!warning] Discrepancy with the official solution
> The key gives $1.24\times10^6$ m²/s² for the specific strength of part b); the rule of mixtures gives $1.861\times10^9/1482.5 = 1.26\times10^6$ m²/s² (with $V_f$ rounded to 0.60: $1858/1.482 = 1.25\times10^6$). The key value is reproduced only if the matrix term is dropped, $(0.30055 \times 6100)/1482.5 = 1.24\times10^6$ m²/s², but parts c) and d) of the same key (0.77, 0.49) need the full hybrid strength of about 1860 MPa, so the computed $1.26\times10^6$ m²/s² is kept. The other key values agree after rounding ($E_{1C} = 235.4$ GPa is the result for $V_f = 0.60$).

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) $\rho_c$ | 1.61 g/cm³ | 1.609 g/cm³ | agrees |
| a) $E_{1C}$ | 235.4 GPa | 235.8 GPa | agrees within rounding (key uses $V_f = 0.60$) |
| b) $E/\rho$ | 106.5×10⁶ m²/s² | 106.6×10⁶ m²/s² | agrees |
| b) $\sigma/\rho$ | 1.24×10⁶ m²/s² | 1.26×10⁶ m²/s² | differs (see the warning) |
| c) $V_{gr,min}$ | 0.77 | 0.769 | agrees |
| d) $V_{K,min}$ | 0.49 | 0.493 | agrees |

## 🔗 Related Links
* [[Topic 10 - Composite Materials|Topic 10: Composite Materials]]
* [[Problem - T10-04 Modulus Strength and Load Fraction of a Kevlar 49-Epoxy Composite|Problem T10-04]]
