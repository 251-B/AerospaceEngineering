---
materia: "Aerospace Materials I"
tema: "Topic 6: Electrical Properties"
origen: "Problems T6andT7_Electric and Magnetic Properties.pdf, Problem 10"
dificultad: medium
badge: "Ranking · band gap · donor and acceptor levels"
tags:
  - official-problem
  - solved
  - compound-semiconductor
  - band-gap
  - donor
  - acceptor
---

# ✏️ Problem: T6-10 — Ranking Semiconductors by Conductivity: Band Gap and Donor and Acceptor Levels

## 📄 Official Statement
> 10. Order the following semiconductors according to their conductivity (assume that the materials are always at the same temperature).
>
> - a) Gallium arsenide; aluminium phosphide; Indium antimonide.
> - b) Cadmium telluride; Indium antimonide.
> - c) Germanium with 1ppm of P; Germanium with 1 ppm of Sb.
> - d) Germanium with 1ppm of P; Silicon with 1 ppm of P.
> - e) Silicon with 10 ppm of B; Silicon with 10 ppm of In.
> - f) Germanium with 5ppm of As; Germanium with 5 ppm of Sb.

The sheet prints no solution for this problem. Slides 34 and 41 pose the same items (a, e and f) and ask to "explain the criterion you have followed".

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Intrinsic compounds (a, b).** Their conductivity is set by the band gap through $\sigma\propto\exp(-E_g/2k_BT)$ [Session 13 Slide 29]; a smaller $E_g$ gives more excited carriers. The trend of $E_g$ follows the bonding: as the covalent character decreases (the bond becomes more ionic) $E_g$ increases and $\sigma$ decreases [Session 13 Slide 32]; and within a group $E_g$ decreases as the atom size increases [Session 13 Slide 31].
2. **Extrinsic semiconductors (c to f).** The doping concentration is the same in each pair, so the carriers come from the ionisation of the dopants; the smaller the ionisation energy ($E_c-E_d$ for donors, $E_a-E_v$ for acceptors), the larger the fraction ionised and the higher the conductivity: $\sigma=\sigma_0\exp[-(E_c-E_d)/2k_BT]$ [Session 13 Slide 43]. The levels are those of Slide 40; for donors and acceptors "increasing $\sigma$" runs with increasing ionic radius for donors and decreasing ionic radius for acceptors (arrows of Slide 40).
3. **Host and mobility.** The mobility of the host matters when the two hosts differ (d): $\mu_e$ is 0.39 m²/(V·s) in germanium and 0.135 in silicon [Session 13 Slide 31], and in extrinsic material $\sigma$ is controlled by the number of carriers because the distortion by the doping is negligible [Session 13 Slide 42].
4. **Data outside the slides** are marked as an extension: AlP and CdTe are not tabulated on Slides 31 and 33.
5. $k_B=8.62\times10^{-5}$ eV/K and $T=300$ K, so $k_BT=0.02586$ eV.

### Data
| Item | Quantity | Value (eV) | Source |
| :--- | :--- | ---: | :--- |
| InSb | $E_g$ | 0.17 | Slide 33 |
| GaAs | $E_g$ | 1.42 | Slide 33 |
| GaP (for the trend) | $E_g$ | 2.25 | Slide 33 |
| AlP | $E_g$ | about 2.45 | literature, extension |
| CdTe | $E_g$ | about 1.5 | literature, extension |
| Ge:P, Ge:As, Ge:Sb | $E_d$ | 0.0120, 0.0127, 0.0096 | Slide 40 |
| Si:P, Si:As, Si:Sb | $E_d$ | 0.045, 0.049, 0.039 | Slide 40 |
| Si:B, Si:Al, Si:Ga, Si:In | $E_a$ | 0.045, 0.057, 0.065, 0.160 | Slide 40 |

**Unknown:** the order of the conductivities in each pair or triple.

---

## 🧠 2. Model and Strategy

Items a and b compare band gaps; items c to f compare ionisation energies. The figure puts the two kinds of quantity side by side, with the ranking found.

![[attachments/T6/t6-p10-ordering.svg]]

**Strategy.**
1. (a, b) Read the gaps of the tabulated compounds and place the others with the bonding trend of Slides 31-32.
2. (c to f) Read the donor or acceptor level of each dopant in its host from Slide 40 and apply the order of the exponential.
3. Quantify each comparison with the exponential of Slide 29 or 43 at 300 K, as an indication only: $\sigma_0$ is taken equal, and the real extrinsic conductivity saturates when all the dopants are ionised.

---

## 🔢 3. Step-by-Step Derivation

### a) GaAs, AlP and InSb [Session 13 Slides 31-33]
Law and the thermal factor at 300 K:

$$\sigma\propto\exp\!\left(-\frac{E_g}{2k_BT}\right)\qquad2k_BT=2\times8.62\times10^{-5}\ \frac{\text{eV}}{\text{K}}\times300\ \text{K}=0.05172\ \text{eV}$$

Exponents $E_g/2k_BT$ of the three materials:

$$\frac{0.17\ \text{eV}}{0.05172\ \text{eV}}=3.287\ (\text{InSb})\qquad\frac{1.42\ \text{eV}}{0.05172\ \text{eV}}=27.46\ (\text{GaAs})\qquad\frac{2.45\ \text{eV}}{0.05172\ \text{eV}}=47.37\ (\text{AlP, extension})$$

Relative factors:

$$e^{-3.287}=3.74\times10^{-2}\qquad e^{-27.46}=1.19\times10^{-12}\qquad e^{-47.37}=2.67\times10^{-21}$$

The three compounds are III-V (covalent with some ionic character); AlP has the smallest atoms of the three (Al and P are in the third period), InSb the largest (fifth period). Larger atoms mean a smaller gap (Slide 31) and the gap is smallest in InSb; on the tabulated side GaAs (1.42 eV) is below GaP (2.25 eV), and AlP, with smaller atoms than GaP, lies above it:

$$E_g(\text{InSb})<E_g(\text{GaAs})<E_g(\text{GaP})<E_g(\text{AlP})$$

$$\mathbf{\sigma(InSb)>\sigma(GaAs)>\sigma(AlP)}$$

### b) CdTe and InSb [Session 13 Slides 32-33]
CdTe is a II-VI compound, more ionic than the III-V InSb; a lower covalent character means a larger gap and a lower conductivity [Session 13 Slide 32]. With the literature value 1.5 eV (extension) and the 0.17 eV of Slide 33, ratio of the factors:

$$\frac{\sigma_{\text{InSb}}}{\sigma_{\text{CdTe}}}\sim\exp\!\left[\frac{(1.5-0.17)\ \text{eV}}{0.05172\ \text{eV}}\right]=\exp(25.72)=1.5\times10^{11}$$

$$\mathbf{\sigma(InSb)>\sigma(CdTe)}$$

### c) Germanium with P or Sb [Session 13 Slides 40-41, 43]
Same concentration, so the dopant with the lower donor level ionises more:

$$E_d(\text{Sb})=0.0096\ \text{eV}<E_d(\text{P})=0.0120\ \text{eV}$$

Indicative ratio, from the exponential of Slide 43 with $2k_BT=0.05172$ eV and equal $\sigma_0$:

$$\frac{\sigma_{\text{Sb}}}{\sigma_{\text{P}}}\sim\exp\!\left[\frac{(0.0120-0.0096)\ \text{eV}}{0.05172\ \text{eV}}\right]=\exp(0.0464)=1.047$$

$$\mathbf{\sigma(Ge{:}Sb)>\sigma(Ge{:}P)}$$

### d) Germanium or silicon with 1 ppm of P
The same dopant in two hosts: Ge has the lower donor level and the higher electron mobility:

$$E_d(\text{Ge})=0.0120\ \text{eV}<E_d(\text{Si})=0.045\ \text{eV}\qquad\mu_e(\text{Ge})=0.39\ \frac{\text{m}^2}{\text{V}\,\text{s}}>\mu_e(\text{Si})=0.135\ \frac{\text{m}^2}{\text{V}\,\text{s}}$$

Indicative ratio, the ionisation exponential times the mobility ratio:

$$\frac{\sigma_{\text{Ge}}}{\sigma_{\text{Si}}}\sim\exp\!\left[\frac{(0.045-0.0120)\ \text{eV}}{0.05172\ \text{eV}}\right]\times\frac{0.39}{0.135}=\exp(0.6380)\times2.889=1.893\times2.889=5.47$$

The same atomic fraction of 1 ppm is a slightly smaller number of donors per unit volume in germanium than in silicon, because germanium has fewer atoms per cubic metre ($N_{\text{Ge}}=4.411\times10^{28}$ m⁻³ and $N_{\text{Si}}=4.995\times10^{28}$ m⁻³, from the densities of Slide 31 as in Problem 9). Including that factor:

$$\frac{N_{\text{Ge}}}{N_{\text{Si}}}=\frac{4.411\times10^{28}\ \text{m}^{-3}}{4.995\times10^{28}\ \text{m}^{-3}}=0.8831\qquad\frac{\sigma_{\text{Ge}}}{\sigma_{\text{Si}}}\sim5.47\times0.8831=4.83$$

The order does not change.

$$\mathbf{\sigma(Ge{:}P)>\sigma(Si{:}P)}$$

### e) Silicon with 10 ppm of B or In
Same concentration of acceptors; the acceptor level of B is much closer to the valence band:

$$E_a(\text{B})=0.045\ \text{eV}<E_a(\text{In})=0.160\ \text{eV}$$

Indicative ratio:

$$\frac{\sigma_{\text{B}}}{\sigma_{\text{In}}}\sim\exp\!\left[\frac{(0.160-0.045)\ \text{eV}}{0.05172\ \text{eV}}\right]=\exp(2.224)=9.24$$

$$\mathbf{\sigma(Si{:}B)>\sigma(Si{:}In)}$$

### f) Germanium with 5 ppm of As or Sb
$$E_d(\text{Sb})=0.0096\ \text{eV}<E_d(\text{As})=0.0127\ \text{eV}$$

$$\frac{\sigma_{\text{Sb}}}{\sigma_{\text{As}}}\sim\exp\!\left[\frac{(0.0127-0.0096)\ \text{eV}}{0.05172\ \text{eV}}\right]=\exp(0.0599)=1.062$$

$$\mathbf{\sigma(Ge{:}Sb)>\sigma(Ge{:}As)}$$

### Result table
| Item | Ranking, highest conductivity first | Criterion |
| :--- | :--- | :--- |
| a | InSb > GaAs > AlP | smaller $E_g$ (larger atoms, more covalent) |
| b | InSb > CdTe | smaller $E_g$ (III-V less ionic than II-VI) |
| c | Ge:Sb > Ge:P | smaller $E_d$ |
| d | Ge:P > Si:P | smaller $E_d$ and larger $\mu_e$ |
| e | Si:B > Si:In | smaller $E_a$ |
| f | Ge:Sb > Ge:As | smaller $E_d$ |

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Dimensionless exponents.** Each exponent is an energy in eV divided by $2k_BT$ in eV, so it has no units; $[k_BT]=\text{eV}\,\text{K}^{-1}\cdot\text{K}=\text{eV}$.
- **Arrows of Slide 40.** Donors: Sb (largest ion) above P, in both hosts, and Ge above Si; acceptors: B (smallest ion) above In. All agree with the ranking found.
- **Scale of the indicative ratios.** The extrinsic ratios in c, d and f are of the order of 1 to 6 because the levels are all of the order of $k_BT$ or smaller and the dopants are almost fully ionised; the pair e differs by 9 because the 0.160 eV of In is several times $k_BT$ (0.02586 eV), and In remains largely un-ionised.
- **The intrinsic ratios are many orders of magnitude** because the gaps are between 3 and 47 times $2k_BT$ (exponents of step a); they are indicative only, since the mobility and the prefactor also change from compound to compound (the mobility of InSb is 7.7 m²/(V·s), the largest on Slide 33, which strengthens the ranking).

### Interpretation
Two rules cover the sheet: for intrinsic material the smaller gap wins, and the gap decreases with the size of the atoms and with the covalent character; for extrinsic material at the same concentration the dopant whose level is nearer to its band wins, with the host's mobility as a second factor. The values labelled "extension" (AlP, CdTe) affect only how far the intrinsic ratios go, not the order, which follows from the trend of Slides 31-32.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a to f | not printed on the sheet | table of the result | checked against the levels of Slide 40 and the gaps of Slide 33; the criterion is the one asked for on Slides 34 and 41 |

## 🔗 Related Links
* [[Topic 6 - Electrical Properties]]
* [[Problem - T6-05 Extrinsic Type of Silicon Doped with Sb As and Ga]]
* [[Problem - T6-09 Ranking Semiconductors by Conductivity Temperature Doping and Concentration]]
* [[Concept - Covalent Bonding and Polar Character]]
