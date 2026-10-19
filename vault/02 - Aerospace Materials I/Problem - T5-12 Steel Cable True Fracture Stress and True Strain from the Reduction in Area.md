---
materia: "Aerospace Materials I"
tema: "Topic 5: Mechanical Properties"
origen: "Problems T5_MechanicalProperties.pdf, Problem 12"
dificultad: medium
badge: "True stress · true strain"
tags:
  - official-problem
  - solved
  - true-stress
  - true-strain
  - reduction-in-area
  - ductility
---

# ✏️ Problem: T5-12 — Steel Cable: True Fracture Stress and True Strain from the Reduction in Area

## 📄 Official Statement
> 12. A steel cable has fracture strength of 300 MPa. Its ductility is 77% measured as a reduction in area. Calculate the real fracture strength. Considering that strain is uniform until fracture, what is the real strain?
>
> *(Solution: $\varepsilon_{real} = 1.47$)*

---

## 📊 1. Phase 1: Hypotheses and Parameters

### Hypotheses
1. **Fracture strength = engineering stress at fracture.** The "fracture strength of 300 MPa" is the load at fracture divided by the *initial* area, $\sigma_f = F_f/A_0$, as in the engineering curve of the tensile test [Session 11 Slide 9]. The true fracture stress is that load divided by the area at fracture, $A_f$ [Session 11 Slide 37].
2. **Ductility as reduction in area.** $RA\,(\%) = \dfrac{A_0 - A_f}{A_0}\times100$ is measured after fracture [Session 11 Slide 33], so $RA = 77\,\%$ means $A_f = 0.23\,A_0$.
3. **Uniform deformation.** The statement asks to take the strain as uniform until fracture, so the volume of the wire is constant, $l_0A_0 = l_fA_f$ (the necking is not modelled) [Session 11 Slide 38].
4. **Real strain by integration.** $\varepsilon_r = \int_{l_0}^{l}dl/l = \ln(l/l_0)$ [Session 11 Slide 37].

### Data
| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Engineering fracture strength | $\sigma_f$ | 300 MPa | $300\times10^{6}$ Pa |
| Reduction in area | $RA$ | 77 % | 0.77 (dimensionless) |

**Unknowns:** the true fracture stress $\sigma_{f,r}$ and the true strain at fracture $\varepsilon_{r}$.

---

## 🧠 2. Phase 2: Frames and Strategy

One direction (the axis of the wire); no change of basis.

**Strategy.**
1. The reduction in area gives the ratio $A_f/A_0 = 1 - RA$.
2. The load at fracture is the same in both definitions of stress, $F_f = \sigma_f A_0 = \sigma_{f,r}A_f$, so $\sigma_{f,r} = \sigma_f\,A_0/A_f$ (the true stress is larger than the engineering one because the area has decreased) [Session 11 Slide 38].
3. With constant volume, the length ratio is the inverse of the area ratio, and the true strain follows from $\ln(l/l_0) = \ln(A_0/A_f)$.
4. The result is verified with the other route, $\sigma_r = \sigma(1+\varepsilon)$ and $\varepsilon_r = \ln(1+\varepsilon)$, through the engineering strain.

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Area ratio at fracture
$$\frac{A_f}{A_0} = 1 - \frac{RA}{100} = 1 - 0.77 = 0.23$$

### 2. True fracture stress
The load at fracture is $F_f = \sigma_f A_0$. Dividing by the area at fracture instead of the initial one:

$$\sigma_{f,r} = \frac{F_f}{A_f} = \frac{\sigma_f A_0}{A_f} = \frac{\sigma_f}{A_f/A_0} = \frac{300\ \text{MPa}}{0.23} = \mathbf{1304.3\ MPa}$$

($\sigma_{f,r}/\sigma_f = 4.348$: the true stress is more than four times the engineering one.)

### 3. True strain at fracture
With the volume constant, $l_0A_0 = l_fA_f$, so

$$\frac{l_f}{l_0} = \frac{A_0}{A_f} = \frac{1}{0.23} = 4.348$$

and the integral of the definition of the real strain, with the substitution $u = l$, $du = dl$, and Barrow's rule between $l_0$ and $l_f$, is

$$\varepsilon_r = \int_{l_0}^{l_f}\frac{dl}{l} = \big[\ln l\big]_{l_0}^{l_f} = \ln l_f - \ln l_0 = \ln\frac{l_f}{l_0} = \ln\frac{A_0}{A_f} = \ln\frac{1}{0.23} = \mathbf{1.4697}$$

Equivalently, in terms of the diameters of the wire, $\varepsilon_r = 2\ln(D_0/D_f)$ [Session 11 Slide 38], with $D_f/D_0 = \sqrt{A_f/A_0} = \sqrt{0.23} = 0.4796$: $2\ln(1/0.4796) = 1.4697$.

### 4. Check through the engineering strain
The engineering strain at fracture is $\varepsilon = l_f/l_0 - 1 = 4.348 - 1 = 3.348$ (that is, 334.8 %). Then

$$\sigma_{f,r} = \sigma_f\,(1 + \varepsilon) = 300\times4.348 = 1304.3\ \text{MPa} \qquad \varepsilon_r = \ln(1 + \varepsilon) = \ln4.348 = 1.4697$$

in agreement with the two results above.

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** Stress in MPa; $A_f/A_0$ and the strains are dimensionless; the argument of the logarithm is a ratio of areas.
- **Limits.** If $RA \to 0$ (no necking) then $A_f \to A_0$, $\sigma_{f,r} \to \sigma_f$ and $\varepsilon_r \to 0$. As $RA \to 100\,\%$, both $\sigma_{f,r}$ and $\varepsilon_r$ grow without bound.
- **Ordering.** $\sigma_{f,r} > \sigma_f$ and $\varepsilon_r < \varepsilon$ ($1.4697 < 3.348$), as stated in [Session 11 Slide 37].

### Interpretation
The steel cable breaks when the material that is left carries 1304 MPa, not 300 MPa: the engineering value hides the reduction of the section. The true strain, 1.47, is the natural measure of such a large deformation, because the integral adds up the increments $dl/l$ over the changing length.

> [!note] Limitation of the uniform-strain hypothesis
> A real cable necks before fracture, and most of the strain is concentrated in the neck. The mean strain along the whole length, obtained here, is therefore a lower bound of the local strain at the fracture section. The statement asks explicitly for the uniform strain, so that is the value reported.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| true fracture stress | not given | 1304.3 MPa | asked by the statement, absent from the key |
| true strain | 1.47 | 1.4697 | agrees |

> [!warning] Discrepancy with the official solution: the key omits the true stress
> The key only prints "$\varepsilon_{real} = 1.47$", although the statement asks for the real fracture strength first. The value computed here, $\sigma_{f,r} = 1304.3$ MPa, is not contradicted by the key: it is the first half of the answer that the key leaves out.

## 🔗 Related Links
* [[Topic 5 - Mechanical Properties]]
* [[Concept - True Stress and True Strain]]
* [[Concept - Ductility - Percent Elongation and Reduction in Area]]
