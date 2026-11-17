---
materia: "Aerospace Materials I"
tema: "Topic 9: Polymers"
origen: "Problems T9_Polymers.pdf, Problem 6"
dificultad: easy
badge: "Crystallinity from density · modulus against T"
tags:
  - official-problem
  - solved
  - crystallinity
  - density
  - polypropylene
  - modulus-temperature
---

# ✏️ Problem: T9-06 — Degree of Crystallinity of Polypropylene from Its Density

## 📄 Official Statement
> 6. Determine the degree of crystallinity of polypropylene with density 0.853g/cm³, given that the densities of amorphous and totally crystalline polypropylene are 0.83 and 0.947 g/cm³ respectively. Represent the change in the elastic modulus with temperature for this polymer, a completely amorphous polymer and a completely crystalline polymer.
>
> *(Solution: 21.8%)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Two-phase sample.** The polypropylene is a mixture of crystalline regions of density $\rho_c$ and amorphous regions of density $\rho_a$ [Session 19 Slide 24], and the degree of crystallinity is the mass fraction of crystalline polymer, given by the formula of Session 19 Slide 25 (its derivation from the additive volumes is in [[Topic 9 - Polymers|the theory note, Section 10.3]]).
2. **Modulus curves.** The modulus against temperature for 100 % amorphous, 50 % / 50 % and 100 % crystalline polymers is the figure of Session 19 Slide 45.
3. **Temperatures of polypropylene.** $T_g = -20$ °C (table of Session 19 Slide 29; the panel of the same slide prints $-15$ °C) and $T_m = 165$ – $177$ °C [Session 20 Slide 8].

### Data
| Quantity | Symbol | Value |
| :--- | :--- | ---: |
| Density of the sample | $\rho_s$ | 0.853 g/cm³ |
| Density of amorphous PP | $\rho_a$ | 0.83 g/cm³ |
| Density of totally crystalline PP | $\rho_c$ | 0.947 g/cm³ |

**Unknowns:** the degree of crystallinity, and the modulus-temperature curves of this PP, of an amorphous polymer and of a crystalline polymer.

---

## 🧠 2. Model and Strategy

[Session 19 Slide 25]:

$$\%\ \text{crystallinity} = \frac{\rho_c(\rho_s - \rho_a)}{\rho_s(\rho_c - \rho_a)} \times 100$$

The sample density lies between $\rho_a$ and $\rho_c$, and the formula places it on the scale between the two in terms of mass.

**Strategy.**
1. Check that $\rho_a < \rho_s < \rho_c$.
2. Evaluate the numerator and the denominator separately and divide.
3. Place the result among the curves of Slide 45.

---

## 🔢 3. Step-by-Step Derivation

### 1. Order of the densities
$$\rho_a = 0.83 < \rho_s = 0.853 < \rho_c = 0.947\ \text{g/cm}^3$$

so the result must lie between 0 and 100 %, and since $\rho_s$ is much closer to $\rho_a$, near the amorphous end.

### 2. Numerator and denominator
$$\rho_c(\rho_s - \rho_a) = 0.947\ \text{g/cm}^3\times(0.853 - 0.83)\ \text{g/cm}^3 = 0.947\times0.023 = 0.021781\ (\text{g/cm}^3)^2$$

$$\rho_s(\rho_c - \rho_a) = 0.853\ \text{g/cm}^3\times(0.947 - 0.83)\ \text{g/cm}^3 = 0.853\times0.117 = 0.099801\ (\text{g/cm}^3)^2$$

### 3. Degree of crystallinity
$$\%\ \text{crystallinity} = \frac{0.021781}{0.099801}\times100 = 21.824 \approx \mathbf{21.8\ \%}$$

### 4. Modulus against temperature [Session 19 Slide 45]
![[attachments/T9/s19-modulus-vs-temperature-crystallinity.png]]

- **Completely amorphous polymer:** high glassy modulus below $T_g$, a drop of several decades at $T_g$, a short plateau and the fall to flow; there is no $T_m$.
- **Completely crystalline polymer:** no glass transition; the modulus stays high and falls only at $T_m$.
- **This polypropylene, 21.8 % crystalline:** its curve lies between the amorphous curve and the 50 % / 50 % curve of the slide. At $T_g$ (about $-20$ °C) it drops, but less than the amorphous polymer, because 21.8 % of its mass stays crystalline; between $T_g$ and $T_m$ it keeps an intermediate plateau held by the crystallites; at $T_m$ (165 – 177 °C) the crystals melt and the modulus falls to the flow region.

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** Numerator and denominator are both products of two densities, $(\text{g/cm}^3)^2$, so the ratio is dimensionless.
- **Limits.** $\rho_s = \rho_a$ gives $0$ and $\rho_s = \rho_c$ gives $\rho_c(\rho_c - \rho_a)/[\rho_c(\rho_c - \rho_a)] = 1$, that is 100 %.
- **Mass against volume fraction.** The volume fraction would be $(\rho_s - \rho_a)/(\rho_c - \rho_a) = 0.023/0.117 = 19.7\ \%$; the mass fraction is larger, $\times\rho_c/\rho_s = 0.947/0.853 = 1.110$, because the crystalline regions are denser (extension).

### Interpretation
Only about one fifth of this polypropylene is crystalline. Room temperature lies above its $T_g$, so the amorphous four fifths are rubbery and the stiffness at room temperature comes from the crystalline fifth: a polymer with this low crystallinity is soft and tough rather than stiff. A more crystalline grade (isotactic PP, slowly cooled) would have a higher density and a higher plateau, closer to the crystalline curve.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Degree of crystallinity | 21.8 % | 21.824 % | agrees |
| Modulus curves | not printed on the sheet | between the amorphous and the 50 % / 50 % curves of Slide 45 | consistent with Session 19 Slide 45 |

## 🔗 Related Links
* [[Topic 9 - Polymers]]
* [[Problem - T9-09 Densities of Crystalline and Amorphous Polypropylene|Problem T9-09]]
