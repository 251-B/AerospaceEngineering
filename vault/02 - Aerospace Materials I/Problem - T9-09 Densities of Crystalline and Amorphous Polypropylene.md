---
materia: "Aerospace Materials I"
tema: "Topic 9: Polymers"
origen: "Problems T9_Polymers.pdf, Problem 9"
dificultad: medium
badge: "Two samples · crystalline and amorphous densities"
tags:
  - official-problem
  - solved
  - crystallinity
  - density
  - polypropylene
  - tacticity
---

# ✏️ Problem: T9-09 — Densities of Crystalline and Amorphous Polypropylene from Two Samples

## 📄 Official Statement
> 9.- The densities of amorphous and totally crystalline polypropylene are given in the table below.
> a) Write the formula of polypropylene and justify whether it can present tacticity.
> b) Calculate the density of completely crystalline and completely amorphous polypropylene.
> c) Deterrmine the density of a sample that is 74.6% crystalline.
>
> ![[attachments/T9/t9-p9-density-crystallinity-table.png]]
>
> *(Solution: b) ρa = 0.84 g/cm³, ρc = 0.946 g/cm³; c) ρ = 0.917 g/cm³)*

The sheet prints "Deterrmine". The first sentence says that the table gives the densities of amorphous and totally crystalline polypropylene, but the table gives the density and the crystallinity of two samples, and part b) asks for the two densities: they are the unknowns.

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Same polypropylene.** Both samples are the same polymer, so they share the same $\rho_c$ and $\rho_a$ and differ only in their degree of crystallinity.
2. **Crystallinity formula.** The degree of crystallinity (mass fraction) is $X_c = \rho_c(\rho_s - \rho_a)/[\rho_s(\rho_c - \rho_a)]$ [Session 19 Slide 25].
3. **Repeat unit.** Polypropylene is $\mathrm{-[CH_2{-}CH(CH_3)]_n-}$ [Session 19 Slide 50].

### Data
| Sample | $\rho_s$ (g/cm³) | $X_c$ |
| :--- | ---: | ---: |
| 1 | 0.904 | 0.628 |
| 2 | 0.895 | 0.544 |
| 3 (part c) | unknown | 0.746 |

**Unknowns:** (a) the formula and its tacticity; (b) $\rho_c$ and $\rho_a$; (c) $\rho_s$ for $X_c = 0.746$.

---

## 🧠 2. Model and Strategy

The formula of Slide 25 has two unknowns, $\rho_c$ and $\rho_a$, and each sample gives one equation, so two samples fix both. The formula is not linear in the densities, but it becomes linear in the specific volumes $1/\rho$. Multiply both sides by $\rho_s(\rho_c - \rho_a)$ and divide by $\rho_s\rho_c\rho_a$:

$$X_c\left(\frac{1}{\rho_a} - \frac{1}{\rho_c}\right) = \frac{1}{\rho_a} - \frac{1}{\rho_s} \quad\Rightarrow\quad \frac{1}{\rho_s} = \frac{X_c}{\rho_c} + \frac{1 - X_c}{\rho_a}$$

which says that the specific volume of the sample is the mass-weighted mean of the specific volumes of its crystalline and amorphous parts. With $u = 1/\rho_c$ and $v = 1/\rho_a$ each sample gives a linear equation.

**Strategy.**
1. Write the formula of polypropylene and look at its asymmetric carbon.
2. Write the two linear equations in $u$ and $v$ and solve them.
3. Use the same relation with $X_c = 0.746$.

---

## 🔢 3. Step-by-Step Derivation

### 1. a) Formula and tacticity [Session 19 Slides 18-19]
$$\mathrm{-[CH_2{-}CH(CH_3)]_n-}$$

Every second carbon of the chain carries a $\mathrm{CH_3}$ side group and an H, so it has four different neighbours (H, $\mathrm{CH_3}$ and the two chain segments). The $\mathrm{CH_3}$ group can be placed on one side or the other of the chain each time a unit is added: polypropylene is a vinyl polymer $\mathrm{H_2C{=}CH{-}R}$ with R = $\mathrm{CH_3}$, so **it can present tacticity**: isotactic, syndiotactic or atactic, as drawn on Slide 19.

### 2. b) Densities of crystalline and amorphous polypropylene
Specific volumes of the samples:

$$\frac{1}{\rho_1} = \frac{1}{0.904\ \text{g/cm}^3} = 1.106195\ \text{cm}^3/\text{g} \qquad \frac{1}{\rho_2} = \frac{1}{0.895\ \text{g/cm}^3} = 1.117318\ \text{cm}^3/\text{g}$$

The two equations:

$$0.628\,u + 0.372\,v = 1.106195\ \text{cm}^3/\text{g} \qquad 0.544\,u + 0.456\,v = 1.117318\ \text{cm}^3/\text{g}$$

Subtracting the second from the first:

$$0.084\,u - 0.084\,v = -0.011124\ \text{cm}^3/\text{g} \quad\Rightarrow\quad v = u + 0.132426\ \text{cm}^3/\text{g}$$

Substituting in the first:

$$0.628\,u + 0.372\,(u + 0.132426) = u + 0.049262 = 1.106195 \quad\Rightarrow\quad u = 1.056932\ \text{cm}^3/\text{g}$$

$$v = 1.056932 + 0.132426 = 1.189358\ \text{cm}^3/\text{g}$$

Densities:

$$\rho_c = \frac{1}{u} = \frac{1}{1.056932\ \text{cm}^3/\text{g}} = \mathbf{0.9461\ g/cm^3} \qquad \rho_a = \frac{1}{v} = \frac{1}{1.189358\ \text{cm}^3/\text{g}} = \mathbf{0.8408\ g/cm^3}$$

### 3. c) Density of a 74.6 % crystalline sample
$$\frac{1}{\rho_s} = 0.746\,u + 0.254\,v = 0.746(1.056932) + 0.254(1.189358) = 0.788471 + 0.302097 = 1.090568\ \text{cm}^3/\text{g}$$

$$\rho_s = \frac{1}{1.090568\ \text{cm}^3/\text{g}} = \mathbf{0.917\ g/cm^3}$$

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Back-substitution in the formula of Slide 25.** With $\rho_c = 0.94613$ and $\rho_a = 0.84079$ g/cm³: sample 1, $0.94613(0.904 - 0.84079)/[0.904(0.94613 - 0.84079)] = 0.628$; sample 2, $0.544$. Both data are recovered.
- **Order.** $\rho_a = 0.841 < 0.895 < 0.904 < 0.917 < \rho_c = 0.946$ g/cm³: the samples lie between the two limits, and the more crystalline the sample, the denser it is [Session 19 Slide 24].
- **Units.** $u$ and $v$ are specific volumes in cm³/g, the coefficients $X_c$ are dimensionless, and every term of the equations is in cm³/g.
- **Comparison with Problem T9-06.** That problem gives $\rho_a = 0.83$ and $\rho_c = 0.947$ g/cm³ for polypropylene; the values found here are close to them.

### Interpretation
Two density measurements of samples of known crystallinity are enough to find the densities of the pure phases, which cannot be measured directly (a fully crystalline polypropylene cannot be made). The crystalline phase is about 12.5 % denser than the amorphous one, because the folded chains of the lamellae pack more closely than the random coils. Once $\rho_c$ and $\rho_a$ are known, the density of any sample gives its crystallinity, which is how the crystallinity of a polymer part is checked in practice.

> [!note] Sensitivity of the result to rounding
> The key rounds the densities to $\rho_a = 0.84$ and $\rho_c = 0.946$ g/cm³. Putting these rounded values back into the formula of Slide 25 gives 63.2 % and 54.8 % instead of the 62.8 % and 54.4 % of the table. This is not an error of the key: the two samples are close in density, so the system is ill-conditioned (determinant $0.628\times0.456 - 0.372\times0.544 = 0.084$), and the change of $0.0008$ g/cm³ in $\rho_a$ alone moves the crystallinity of sample 1 by 0.3 points (from 62.8 % to 63.1 %). With the unrounded $\rho_a = 0.8408$ g/cm³ the table is recovered exactly, and the density of part c) is 0.917 g/cm³ with either set.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) Tacticity | not printed on the sheet | yes: asymmetric CH carbon with a $\mathrm{CH_3}$ group | consistent with Session 19 Slides 18-19 |
| b) $\rho_a$ | 0.84 g/cm³ | 0.8408 g/cm³ | agrees after rounding |
| b) $\rho_c$ | 0.946 g/cm³ | 0.9461 g/cm³ | agrees |
| c) $\rho$ | 0.917 g/cm³ | 0.917 g/cm³ | agrees |

## 🔗 Related Links
* [[Topic 9 - Polymers]]
* [[Problem - T9-06 Degree of Crystallinity of Polypropylene from Its Density|Problem T9-06]]
