---
materia: "Aerospace Materials I"
tema: "Topic 6: Electrical Properties"
origen: "Problems T6andT7_Electric and Magnetic Properties.pdf, Problem 9"
dificultad: medium
badge: "Ranking · temperature · doping · concentration"
tags:
  - official-problem
  - solved
  - intrinsic-semiconductor
  - extrinsic-semiconductor
  - doping-level
---

# ✏️ Problem: T6-09 — Ranking Semiconductors by Conductivity: Temperature, Doping and Concentration

## 📄 Official Statement
> 9. Order the following semiconductors according to their conductivity (assume that the materials are always at room temperature, except when the opposite is specified).
>
> - a) Pure Germanium at 0 ºC; pure Germanium at 25 ºC; pure Germanium at 50 ºC.
> - b) Phosphor doped- silicon; pure silicon.
> - c) Germanium doped with 100 ppb of nitrogen; germanium doped with 1ppm of nitrogen.

The sheet prints no solution for this problem.

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Pure germanium is intrinsic** and obeys $\sigma=\sigma_0\exp(-E_g/2k_BT)$ [Session 13 Slide 29]; $\sigma_0$ does not change over 50 K, and $E_g=0.67$ eV [Session 13 Slide 31].
2. **Doped silicon is extrinsic.** Phosphorus is a group-15 donor, so $\sigma\approx n_e|q_e|\mu_e$ with $n_e$ equal to the number of P atoms [Session 13 Slide 36]. Extrinsic doping is "generally 100-1000 ppm" [Session 13 Slide 26]; a doping of 1 ppm, which is 100 times below the lowest value of the slide, is used so that the conclusion holds a fortiori for any realistic doping. The doping level is not given in the statement. A concentration in ppm is read as an atomic fraction (atoms of dopant per million atoms of host).
3. **Mobility of the doped silicon.** It lies between the value of low doping, 0.135 m²/(V·s) [Session 13 Slide 31], and a floor of 0.001 m²/(V·s), the bottom of the axis of the mobility chart of Slide 42, which the electron curve never reaches.
4. **Nitrogen is a donor** in the course model, because it is in group 15 (VA), like P, As and Sb [Session 13 Slides 35-36]. Extension caveat: in real germanium nitrogen is not a practical donor; the problem is answered within the rule of the course.
5. **Same mobility** for the two nitrogen levels, so $\sigma\propto n_e$: for extrinsic semiconductors the distortion of the lattice caused by the doping is negligible, and the conductivity is controlled by the number of charge carriers [Session 13 Slide 42].
6. **Room temperature** is 25 °C (298.15 K); $k_B=8.62\times10^{-5}$ eV/K; $|q_e|=1.602\times10^{-19}$ C. The atomic masses (Si 28.09 g/mol, Ge 72.63 g/mol) and Avogadro's number ($6.022\times10^{23}$ mol⁻¹) are standard data, not on the slides.

### Data
| Quantity | Value | Source |
| :--- | ---: | :--- |
| $E_g$ of Ge | 0.67 eV | Slide 31 |
| Density of Si, Ge | $2.33\times10^{6}$, $5.32\times10^{6}$ g/m³ | Slide 31 |
| Intrinsic conductivity of Si | $4\times10^{-4}$ Ω⁻¹m⁻¹ | Slides 31, 33 |
| Intrinsic carrier density of Ge | $2.4\times10^{19}$ m⁻³ | Slide 31 |
| $\mu_e$ of Si at low doping | 0.135 m²/(V·s) | Slide 31 |

**Unknown:** the order of the conductivities in each group.

---

## 🧠 2. Model and Strategy

Each group changes one variable: the temperature (a), the type of material (b) or the doping concentration (c). The figure collects the numerical results of the three groups.

![[attachments/T6/t6-p9-ordering.svg]]

**Strategy.**
1. (a) Compute the ratios of the intrinsic conductivity at the three temperatures from the exponential law.
2. (b) Compute the conductivity of the doped silicon at its lowest realistic doping and compare it with the intrinsic value.
3. (c) Convert both concentrations to carriers per cubic metre and compare them with each other and with the intrinsic density.

---

## 🔢 3. Step-by-Step Derivation

### a) Pure germanium at 0, 25 and 50 °C [Session 13 Slide 29]
Ratio between two temperatures (the derivation of Problem T6-07), and the temperatures in kelvin:

$$\frac{\sigma_B}{\sigma_A}=\exp\!\left[\frac{E_g}{2k_B}\left(\frac{1}{T_A}-\frac{1}{T_B}\right)\right]\qquad\frac{E_g}{2k_B}=\frac{0.67\ \text{eV}}{2\times8.62\times10^{-5}\ \text{eV/K}}=3886.3\ \text{K}$$

$$T_0=0+273.15=273.15\ \text{K}\qquad T_{25}=25+273.15=298.15\ \text{K}\qquad T_{50}=50+273.15=323.15\ \text{K}$$

Reciprocals:

$$\frac{1}{T_0}=3.66099\times10^{-3}\ \text{K}^{-1}\qquad\frac{1}{T_{25}}=3.35402\times10^{-3}\ \text{K}^{-1}\qquad\frac{1}{T_{50}}=3.09454\times10^{-3}\ \text{K}^{-1}$$

Exponents and ratios for 0 to 25 °C, 25 to 50 °C and 0 to 50 °C:

$$\frac{\sigma_{25}}{\sigma_0}=\exp\!\left[3886.3\ \text{K}\times(3.66099-3.35402)\times10^{-3}\ \text{K}^{-1}\right]=\exp(1.1930)=3.297$$

$$\frac{\sigma_{50}}{\sigma_{25}}=\exp\!\left[3886.3\ \text{K}\times(3.35402-3.09454)\times10^{-3}\ \text{K}^{-1}\right]=\exp(1.0084)=2.741$$

$$\frac{\sigma_{50}}{\sigma_0}=3.297\times2.741=9.038=\exp(2.2014)$$

$$\mathbf{\sigma(50\ {}^{\circ}C)>\sigma(25\ {}^{\circ}C)>\sigma(0\ {}^{\circ}C)}$$

### b) Phosphorus-doped silicon against pure silicon [Session 13 Slides 26, 31, 33, 36]
Atomic density of silicon, with $N=\rho_m N_A/M$:

$$N_{\text{Si}}=\frac{2.33\times10^{6}\ \text{g/m}^3\times6.022\times10^{23}\ \text{mol}^{-1}}{28.09\ \text{g/mol}}=\frac{1.4031\times10^{30}}{28.09}\ \text{m}^{-3}=4.995\times10^{28}\ \text{m}^{-3}$$

Conversion of 1 ppm (one atom in $10^6$) to a concentration of donors, one electron per P atom:

$$n_e=10^{-6}\times4.995\times10^{28}\ \text{m}^{-3}=4.995\times10^{22}\ \text{m}^{-3}$$

Charge density of the free electrons:

$$n_e\,|q_e|=4.995\times10^{22}\ \text{m}^{-3}\times1.602\times10^{-19}\ \text{C}=8.002\times10^{3}\ \frac{\text{C}}{\text{m}^3}$$

Conductivity, upper and lower bounds by the mobility ($\sigma=n_e|q_e|\mu_e$, units $\text{C}\,\text{m}^{-3}\cdot\text{m}^2\text{V}^{-1}\text{s}^{-1}=\Omega^{-1}\text{m}^{-1}$):

$$\sigma_{\max}=8.002\times10^{3}\times0.135\ \Omega^{-1}\text{m}^{-1}=1080\ \Omega^{-1}\text{m}^{-1}\qquad\sigma_{\min}=8.002\times10^{3}\times0.001\ \Omega^{-1}\text{m}^{-1}=8.0\ \Omega^{-1}\text{m}^{-1}$$

Comparison with the intrinsic silicon of Slide 33:

$$\frac{\sigma_{\min}}{\sigma_{\text{pure}}}=\frac{8.0}{4\times10^{-4}}=2.0\times10^{4}\qquad\frac{\sigma_{\max}}{\sigma_{\text{pure}}}=\frac{1080}{4\times10^{-4}}=2.7\times10^{6}$$

$$\mathbf{\sigma(\text{P-doped Si})>\sigma(\text{pure Si})}$$

A doping of 100 to 1000 ppm, as on Slide 26, is 100 to 1000 times the level used above, so $n_e$ is larger by the same factor and the gap widens further.

### c) Germanium with 100 ppb and with 1 ppm of nitrogen
Atomic density of germanium:

$$N_{\text{Ge}}=\frac{5.32\times10^{6}\ \text{g/m}^3\times6.022\times10^{23}\ \text{mol}^{-1}}{72.63\ \text{g/mol}}=\frac{3.2037\times10^{30}}{72.63}\ \text{m}^{-3}=4.411\times10^{28}\ \text{m}^{-3}$$

Conversion of the two concentrations (1 ppm is $10^{-6}$, 100 ppb is $10^{-7}$), one electron per N atom (hypothesis 4):

$$n_{1\,\text{ppm}}=10^{-6}\times4.411\times10^{28}\ \text{m}^{-3}=4.411\times10^{22}\ \text{m}^{-3}\qquad n_{100\,\text{ppb}}=10^{-7}\times4.411\times10^{28}\ \text{m}^{-3}=4.411\times10^{21}\ \text{m}^{-3}$$

Ratio of conductivities, with the same mobility:

$$\frac{\sigma_{1\,\text{ppm}}}{\sigma_{100\,\text{ppb}}}=\frac{n_{1\,\text{ppm}}\,|q_e|\,\mu_e}{n_{100\,\text{ppb}}\,|q_e|\,\mu_e}=\frac{4.411\times10^{22}}{4.411\times10^{21}}=10$$

Both are extrinsic, because both exceed the intrinsic density of Slide 31:

$$\frac{n_{100\,\text{ppb}}}{n_i}=\frac{4.411\times10^{21}}{2.4\times10^{19}}=183.8\qquad\frac{n_{1\,\text{ppm}}}{n_i}=\frac{4.411\times10^{22}}{2.4\times10^{19}}=1838$$

$$\mathbf{\sigma(1\ ppm\ N)>\sigma(100\ ppb\ N)}$$

### Result table
| Group | Ranking, highest conductivity first |
| :--- | :--- |
| a | Ge at 50 °C > Ge at 25 °C > Ge at 0 °C |
| b | P-doped Si > pure Si |
| c | Ge with 1 ppm N > Ge with 100 ppb N |

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Dimensionless exponents.** $[(E_g/2k_B)(1/T_A-1/T_B)]=\text{K}\cdot\text{K}^{-1}=1$.
- **Units of the atomic density.** $[\rho_mN_A/M]=\text{g}\,\text{m}^{-3}\cdot\text{mol}^{-1}/(\text{g}\,\text{mol}^{-1})=\text{m}^{-3}$.
- **Consistency.** The result of a for 25 to 50 °C (2.74) is the same exponential law as in Problem T6-07, where the 25 to 75 °C ratio is 6.50.
- **Doping against the intrinsic density of silicon** (Slide 31):

$$\frac{n_e}{n_i}=\frac{4.995\times10^{22}\ \text{m}^{-3}}{1.5\times10^{16}\ \text{m}^{-3}}=3.3\times10^{6}$$

so one part per million is already far above the intrinsic density.

### Interpretation
Heating creates carriers in the pure semiconductor, doping supplies them at room temperature, and the more dopant the more carriers, until the mobility starts to drop (Slide 42). Doping is by far the strongest lever: a one-in-a-million donor does more for the conductivity than a 50 K rise of the pure crystal. The ranking in c assumes that nitrogen behaves as a donor, as the course rule says for group 15; the ratio 10 is only the ratio of the concentrations and does not depend on that assumption except for the sign.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a | not printed on the sheet | 50 °C > 25 °C > 0 °C | exponential law of Slide 29 |
| b | not printed on the sheet | doped Si > pure Si | at least $2\times10^{4}$ times |
| c | not printed on the sheet | 1 ppm > 100 ppb | ratio 10 |

## 🔗 Related Links
* [[Topic 6 - Electrical Properties]]
* [[Problem - T6-07 Conductivity of Intrinsic Germanium at 75 C]]
* [[Problem - T6-06 Phosphorus-Doped Silicon Type and Conductivity]]
