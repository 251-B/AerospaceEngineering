---
materia: "Aerospace Materials I"
tema: "Topic 6: Electrical Properties"
origen: "Problems T6andT7_Electric and Magnetic Properties.pdf, Problem 6"
dificultad: easy
badge: "n-type silicon · conductivity"
tags:
  - official-problem
  - solved
  - extrinsic-semiconductor
  - conductivity
  - mobility
---

# ✏️ Problem: T6-06 — Phosphorus-Doped Silicon: Type and Conductivity

## 📄 Official Statement
> 6. P is added to high purity silicon in order to introduce a concentration of $10^{+23}$ m⁻³ of charge carriers at room temperature.
>
> - a) What type of semiconductor is this material?
> - b) What is the conductivity of this semiconductor at room temperature? Assume that the mobility of the e⁻ in the material is 0.14 m²/(V·s)
>
> *(Solution: b) 2243 Ω⁻¹m⁻¹)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **P is a donor.** Phosphorus (group 15, 5 valence electrons) replaces silicon (4 valence electrons) and gives one electron to the conduction band, so the extrinsic silicon is n-type [Session 13 Slide 36].
2. **Electrons carry the current.** In n-type material $n_e\gg n_H$ and the conductivity is $\sigma\approx n_e|q_e|\mu_e$ [Session 13 Slide 36]. The "concentration of charge carriers" of the statement is the electron concentration $n_e$.
3. **Holes are negligible.** The holes of the intrinsic silicon are at most $n_i=1.5\times10^{16}$ m⁻³ [Session 13 Slide 31], far fewer than the donor electrons; this is checked in step 5.
4. **Constant of the electron charge.** $|q_e|=1.602\times10^{-19}$ C. Slide 10 prints $1.6\times10^{-19}$ C; the key of the sheet (2243) is reproduced with $1.602\times10^{-19}$ C.

### Data
| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Electron (carrier) concentration | $n_e$ | $10^{23}$ m⁻³ | $10^{23}$ m⁻³ |
| Electron mobility | $\mu_e$ | 0.14 m²/(V·s) | 0.14 m²/(V·s) |
| Electron charge | $\lvert q_e\rvert$ | $1.602\times10^{-19}$ C | same |

**Unknowns:** (a) the type of semiconductor; (b) the conductivity $\sigma$.

---

## 🧠 2. Model and Strategy

Every donor atom adds one free electron, so the electron concentration equals the carrier concentration given by the statement. The current density follows from the drift velocity $v_d=\mu_eE$, and the conductivity is the proportionality constant between $J$ and $E$ (Ohm's law of the microscopic form, Slide 12). The figure shows the bar.

![[attachments/T6/t6-p6-n-type-bar.svg]]

**Strategy.**
1. Classify the semiconductor from the group of P.
2. Write the current density from the drift velocity and read off the conductivity.
3. Evaluate the product in SI units, checking that the units reduce to Ω⁻¹m⁻¹.
4. Check that the hole contribution is negligible.

---

## 🔢 3. Step-by-Step Derivation

### 1. Type of the semiconductor (a) [Session 13 Slide 36]
Valence electrons of the dopant against the host:

$$Z_{\text{P}}-Z_{\text{Si}}=5-4=+1\ \Rightarrow\ \text{donor}\ \Rightarrow\ \mathbf{n\text{-}type\ extrinsic\ semiconductor}$$

### 2. Conductivity from the drift velocity [Session 13 Slides 11-12, 36]
Drift velocity and current density of $n_e$ electrons of charge $|q_e|$, and Ohm's law $J=\sigma E$:

$$v_d=\mu_e\,E\qquad J=n_e\,|q_e|\,v_d=n_e\,|q_e|\,\mu_e\,E\qquad J=\sigma E$$

Comparing the last two expressions of the current density:

$$\sigma=n_e\,|q_e|\,\mu_e$$

### 3. Numerical evaluation (b)
Charge density of the free electrons, one operation at a time:

$$n_e\,|q_e|=10^{23}\ \text{m}^{-3}\times1.602\times10^{-19}\ \text{C}=1.602\times10^{4}\ \frac{\text{C}}{\text{m}^3}=16\,020\ \frac{\text{C}}{\text{m}^3}$$

Multiplication by the mobility:

$$\sigma=16\,020\ \frac{\text{C}}{\text{m}^3}\times0.14\ \frac{\text{m}^2}{\text{V}\,\text{s}}=2242.8\ \frac{\text{C}}{\text{V}\,\text{s}\,\text{m}}$$

Reduction of the units, with $1\ \text{C}/\text{s}=1\ \text{A}$ and $1\ \text{V}/\text{A}=1\ \Omega$:

$$\frac{\text{C}}{\text{V}\,\text{s}\,\text{m}}=\frac{\text{A}}{\text{V}\,\text{m}}=\frac{1}{\Omega\,\text{m}}=\Omega^{-1}\text{m}^{-1}$$

$$\sigma=\mathbf{2243\ \Omega^{-1}m^{-1}}$$

### 4. Resistivity (for comparison with the metals of Problem T6-01)
$$\rho=\frac{1}{\sigma}=\frac{1}{2242.8\ \Omega^{-1}\text{m}^{-1}}=4.459\times10^{-4}\ \Omega\,\text{m}$$

### 5. The holes are negligible
Upper bound of the hole contribution, if there were $n_i$ holes with the hole mobility of silicon (0.048 m²/(V·s) [Session 13 Slide 31]):

$$\sigma_h\le p\,|q_e|\,\mu_h=1.5\times10^{16}\ \text{m}^{-3}\times1.602\times10^{-19}\ \text{C}\times0.048\ \frac{\text{m}^2}{\text{V}\,\text{s}}=1.153\times10^{-4}\ \Omega^{-1}\text{m}^{-1}$$

$$\frac{\sigma_h}{\sigma}\le\frac{1.153\times10^{-4}}{2242.8}=5.1\times10^{-8}$$

### 6. Effect of the rounded charge
With the value of Slide 10:

$$\sigma=10^{23}\times1.6\times10^{-19}\times0.14\ \Omega^{-1}\text{m}^{-1}=2240\ \Omega^{-1}\text{m}^{-1}$$

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $[n_e|q_e|\mu_e]=\text{m}^{-3}\cdot\text{C}\cdot\text{m}^2\text{V}^{-1}\text{s}^{-1}=\Omega^{-1}\text{m}^{-1}$ (step 3).
- **Order of magnitude.** 2243 Ω⁻¹m⁻¹ lies inside the semiconductor range of Slide 5 ($10^{-6}$ to $10^{4}$ Ω⁻¹m⁻¹). Against the intrinsic value of silicon at room temperature, $4\times10^{-4}$ Ω⁻¹m⁻¹ (the value used in Problem 8 of the sheet and printed on Slide 33; Slide 21 prints $4.5\times10^{-4}$ Ω⁻¹m⁻¹):

$$\frac{\sigma}{\sigma_i}=\frac{2242.8\ \Omega^{-1}\text{m}^{-1}}{4\times10^{-4}\ \Omega^{-1}\text{m}^{-1}}=5.6\times10^{6}$$

- **Hole share.** Below $10^{-7}$ of the total.
- **Limit.** For $n_e\to n_i$ the formula would need both carriers and tend to the intrinsic value; for $n_e\to0$, $\sigma\to0$.

### Interpretation
The donors are a tiny fraction of the silicon atoms. The atom density follows from the density of Slide 31, the molar mass of silicon (28.09 g/mol, periodic table, not on the slides) and Avogadro's number:

$$N_{\text{Si}}=\frac{\rho_mN_A}{M}=\frac{2.33\times10^{6}\ \text{g/m}^3\times6.022\times10^{23}\ \text{mol}^{-1}}{28.09\ \text{g/mol}}=4.995\times10^{28}\ \text{m}^{-3}$$

and the fraction of donors is:

$$\frac{n_e}{N_{\text{Si}}}=\frac{10^{23}\ \text{m}^{-3}}{4.995\times10^{28}\ \text{m}^{-3}}=2.0\times10^{-6}$$

that is, two donors per million atoms, and yet they raise the conductivity by almost seven orders of magnitude. The mobility of 0.14 m²/(V·s) is the one of the electrons in this material; Slide 42 shows that it falls when the dopant concentration is higher.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) Type | not printed (the key lists b only) | n-type extrinsic | P is a group-15 donor, Slide 36 |
| b) Conductivity | 2243 Ω⁻¹m⁻¹ | 2243 Ω⁻¹m⁻¹ | agrees with $q=1.602\times10^{-19}$ C; with the rounded $1.6\times10^{-19}$ C of Slide 10 the result is 2240 |

## 🔗 Related Links
* [[Topic 6 - Electrical Properties]]
* [[Concept - Covalent Bonding and Polar Character]]
* [[Problem - T6-05 Extrinsic Type of Silicon Doped with Sb As and Ga]]
