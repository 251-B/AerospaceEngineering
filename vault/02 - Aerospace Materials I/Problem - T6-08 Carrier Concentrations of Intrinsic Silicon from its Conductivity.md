---
materia: "Aerospace Materials I"
tema: "Topic 6: Electrical Properties"
origen: "Problems T6andT7_Electric and Magnetic Properties.pdf, Problem 8"
dificultad: easy
badge: "Intrinsic carriers · electrons and holes"
tags:
  - official-problem
  - solved
  - intrinsic-semiconductor
  - carrier-concentration
  - mobility
---

# ✏️ Problem: T6-08 — Carrier Concentrations of Intrinsic Silicon from its Conductivity

## 📄 Official Statement
> 8. The electrical conductivity of intrinsic Si at room temperature is $4\cdot10^{-4}$ Ω⁻¹m⁻¹, and the mobilities of electrons and holes are 0.14 y 0.048 m²/(V·s) respectively. Calculate the concentration of holes and electrons.
>
> *(Solution: $1.32\times10^{16}$ m⁻³)*

The statement is transcribed as printed: "y" is the Spanish "and".

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Two carrier types.** In an intrinsic semiconductor each excitation creates one electron in the conduction band and one hole in the valence band, so both carry current: $\sigma=n|q_e|\mu_e+p|q_e|\mu_h$ [Session 13 Slides 27-28].
2. **Equal numbers.** Because the carriers are created in pairs, $n=p=n_i$ and the charge of the hole has the same magnitude as that of the electron, $|q_h|=|q_e|$ [Session 13 Slide 28].
3. **Room temperature,** all values are those of the statement. The charge is $1.602\times10^{-19}$ C (the value that reproduces the key).

### Data
| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Conductivity | $\sigma$ | $4\times10^{-4}$ Ω⁻¹m⁻¹ | same |
| Electron mobility | $\mu_e$ | 0.14 m²/(V·s) | same |
| Hole mobility | $\mu_h$ | 0.048 m²/(V·s) | same |
| Charge | $\lvert q_e\rvert$ | $1.602\times10^{-19}$ C | same |

**Unknown:** the hole concentration $p$ and the electron concentration $n$.

---

## 🧠 2. Model and Strategy

The two carriers add their currents. As their numbers are equal, the conductivity is the carrier concentration times the charge times the sum of the two mobilities, and that one equation has one unknown. The figure shows the excitation of pairs and the way the conductivity splits between the carriers.

![[attachments/T6/t6-p8-carriers.svg]]

**Strategy.**
1. Write the conductivity with both carriers and impose $n=p$.
2. Solve for the concentration.
3. Evaluate with SI values, then compute the share of each carrier.
4. Compare with the intrinsic concentration of silicon tabulated on Slide 31.

---

## 🔢 3. Step-by-Step Derivation

### 1. Conductivity with both carriers [Session 13 Slides 27-28]
$$\sigma=n\,|q_e|\,\mu_e+p\,|q_e|\,\mu_h$$

### 2. Condition of pairs and solution for the concentration
Substitution of $n=p=n_i$ and extraction of the common factor:

$$\sigma=n_i\,|q_e|\,\mu_e+n_i\,|q_e|\,\mu_h=n_i\,|q_e|\,(\mu_e+\mu_h)$$

Division by $|q_e|(\mu_e+\mu_h)$:

$$n_i=\frac{\sigma}{|q_e|\,(\mu_e+\mu_h)}$$

### 3. Numerical evaluation, one operation per block
Sum of the mobilities:

$$\mu_e+\mu_h=0.14\ \frac{\text{m}^2}{\text{V}\,\text{s}}+0.048\ \frac{\text{m}^2}{\text{V}\,\text{s}}=0.188\ \frac{\text{m}^2}{\text{V}\,\text{s}}$$

Denominator:

$$|q_e|\,(\mu_e+\mu_h)=1.602\times10^{-19}\ \text{C}\times0.188\ \frac{\text{m}^2}{\text{V}\,\text{s}}=3.01176\times10^{-20}\ \frac{\text{C}\,\text{m}^2}{\text{V}\,\text{s}}$$

Quotient:

$$n_i=\frac{4\times10^{-4}\ \Omega^{-1}\text{m}^{-1}}{3.01176\times10^{-20}\ \text{C}\,\text{m}^2\text{V}^{-1}\text{s}^{-1}}=1.3281\times10^{16}\ \frac{\Omega^{-1}\text{m}^{-1}\ \text{V}\,\text{s}}{\text{C}\,\text{m}^2}$$

Reduction of the units, with $\Omega^{-1}=\text{A}/\text{V}$ and $\text{A}\,\text{s}=\text{C}$:

$$\frac{\Omega^{-1}\text{m}^{-1}\,\text{V}\,\text{s}}{\text{C}\,\text{m}^2}=\frac{\text{A}\,\text{V}\,\text{s}}{\text{V}\,\text{C}\,\text{m}^3}=\frac{\text{C}}{\text{C}\,\text{m}^3}=\text{m}^{-3}$$

$$\mathbf{n=p=n_i=1.328\times10^{16}\ m^{-3}}$$

### 4. Share of each carrier in the conductivity
Electron and hole conductivities:

$$\sigma_e=n\,|q_e|\,\mu_e=1.3281\times10^{16}\times1.602\times10^{-19}\times0.14\ \Omega^{-1}\text{m}^{-1}=2.979\times10^{-4}\ \Omega^{-1}\text{m}^{-1}$$

$$\sigma_h=p\,|q_e|\,\mu_h=1.3281\times10^{16}\times1.602\times10^{-19}\times0.048\ \Omega^{-1}\text{m}^{-1}=1.021\times10^{-4}\ \Omega^{-1}\text{m}^{-1}$$

Shares (they equal the mobility ratios because $n=p$):

$$\frac{\sigma_e}{\sigma}=\frac{0.14}{0.188}=0.7447\qquad\frac{\sigma_h}{\sigma}=\frac{0.048}{0.188}=0.2553$$

Sum:

$$\sigma_e+\sigma_h=2.979\times10^{-4}+1.021\times10^{-4}=4.000\times10^{-4}\ \Omega^{-1}\text{m}^{-1}$$

### 5. Comparison with the table of Slide 31
Slide 31 gives for silicon $n_i=1.5\times10^{16}$ m⁻³, $\mu_e=0.135$ and $\mu_h=0.048$ m²/(V·s):

$$\sigma=1.5\times10^{16}\times1.602\times10^{-19}\times(0.135+0.048)\ \Omega^{-1}\text{m}^{-1}=4.40\times10^{-4}\ \Omega^{-1}\text{m}^{-1}$$

$$\frac{1.328\times10^{16}}{1.5\times10^{16}}=0.885$$

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $\sigma/(|q|\mu)$ has units of $\text{m}^{-3}$ (step 3).
- **Reconstruction.** The two partial conductivities add up to the given $4\times10^{-4}$ Ω⁻¹m⁻¹ (step 4).
- **Order of magnitude.** Relative difference of the computed concentration from the tabulated $1.5\times10^{16}$ m⁻³; it comes from the rounded conductivity of the statement ($4\times10^{-4}$, with $\mu_e=0.14$) against the $4.4\times10^{-4}$ that the table values give:

$$\frac{1.328\times10^{16}-1.5\times10^{16}}{1.5\times10^{16}}=-0.115$$

- **Concentration against atom density.** With $N_{\text{Si}}=4.995\times10^{28}$ atoms/m³ (from $\rho_mN_A/M$, Problem T6-09):

$$\frac{N_{\text{Si}}}{n_i}=\frac{4.995\times10^{28}\ \text{m}^{-3}}{1.328\times10^{16}\ \text{m}^{-3}}=3.76\times10^{12}$$

one carrier pair per $3.8\times10^{12}$ atoms, which is why intrinsic silicon is such a poor conductor.

### Interpretation
Silicon at room temperature has $1.3\times10^{16}$ electrons and the same number of holes per cubic metre, and three quarters of the current is carried by the electrons because they move almost three times faster. If the holes had the mobility of the electrons the two shares would be equal; if the number of electrons exceeded that of the holes (doping) the material would no longer be intrinsic.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Concentration of holes and electrons | $1.32\times10^{16}$ m⁻³ | $1.328\times10^{16}$ m⁻³ for each | agrees to 0.6 %, see the warning |

> [!warning] Discrepancy with the official solution
> The key prints $1.32\times10^{16}$ m⁻³. Our exact value is $1.3281\times10^{16}$ m⁻³, which rounds to $1.33\times10^{16}$: the key appears to truncate instead of rounding. With the rounded charge $1.6\times10^{-19}$ C the result would be $1.330\times10^{16}$ m⁻³. We keep the computed value.

## 🔗 Related Links
* [[Topic 6 - Electrical Properties]]
* [[Concept - Metallic Bonding and Energy Band Theory]]
* [[Problem - T6-07 Conductivity of Intrinsic Germanium at 75 C]]
