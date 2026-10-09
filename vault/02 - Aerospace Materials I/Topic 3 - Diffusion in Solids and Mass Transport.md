---
materia: "Aerospace Materials I"
tema: "Topic 3: Diffusion in Solids and Mass Transport"
fuentes: "Session 5 T3  Difussion_2025.pdf, Problems T3_Diffusion.pdf"
tags:
  - theory
  - topic-moc
  - diffusion
  - ficks-laws
  - steady-state
  - non-steady-state
  - error-function
  - arrhenius
  - case-hardening
dificultad: medium
prerrequisitos:
  - "[[Topic 2 - Structure of Materials and Crystalline Defects]]"
---

# 🌐 Topic 3: Diffusion in Solids and Mass Transport

> **Central Idea of the Topic:** **Diffusion in solids** is the mass-transport phenomenon in which atoms, ions or molecules migrate through the crystal lattice by thermally activated vibrations, driven fundamentally by a **concentration gradient** ($\nabla C$). It governs everything from the thermochemical surface-hardening treatments of aeronautical gears to the manufacture of integrated circuits on silicon wafers, the sintering of ceramic blades and diffusion bonding in state-of-the-art turbofans [Session 5 Slides 2, 29-35].

$$\text{Concentration Gradient } (\nabla C) + \text{Thermal Activation } (T > 0\text{ K}) \implies \text{Mass Transport } (J = -D \nabla C)$$

---

## 🗺️ 1. Concept Map of the Official UC3M Session (Session 5)

```
TOPIC 3: DIFFUSION IN SOLIDS AND MASS TRANSPORT
│
├── ⚛️ 1. FUNDAMENTAL CONCEPTS AND ATOMIC MECHANISMS (Slides 2-13)
│   ├── Definition: Mass transport in solids by activated thermal vibration
│   ├── Driving Force: Composition gradient (tendency to homogenize)
│   ├── Requirements: Adjacent vacant site (empty site) + Thermal energy ≥ Activation energy (Ea)
│   ├── Vacancy Mechanism (Substitutional):
│   │   ├── Self-diffusion: Atomic exchange in a pure metal (Eself = Ev + Em)
│   │   ├── Correlation with Tm: Higher melting point ⟹ higher bond energy ⟹ higher Ea
│   │   └── Interdiffusion: Motion in substitutional alloys (Hume-Rothery rules, Cu-Ni couple)
│   └── Interstitial Mechanism:
│       ├── Migration of small solutes (C, H, N, O, B) between interstitial sites without permanently deforming the matrix
│       └── Kinetic advantages: Ei ≪ Ev, abundance of free sites, Dinterstitial is 10⁴-10⁶ times faster
│
├── 📏 2. FICK'S LAWS OF DIFFUSION (Slides 15-21)
│   ├── Diffusional Flux Density: J = M / (A · t) [mol/(cm²·s) or kg/(m²·s)]
│   ├── Fick's First Law — Steady State (∂C/∂t = 0, ∂J/∂t = 0):
│   │   ├── Fundamental equation: J = -D · (∂C/∂x) ≈ -D · (ΔC / Δx)
│   │   └── Strictly linear concentration profile in flat membranes (Δx = D · ΔC / J)
│   └── Fick's Second Law — Non-Steady State / Transient (∂C/∂t ≠ 0):
│       ├── General differential equation: ∂Cx/∂t = D · (∂²Cx/∂x²) (for D ≠ f(C))
│       ├── Semi-Infinite Solid Geometry (x = 0 to ∞): C(x,0) = C₀, C(0,t) = Cs, C(∞,t) = C₀
│       ├── Analytical solution with the Error Function: (Cx - C₀)/(Cs - C₀) = 1 - erf(x / (2√Dt))
│       └── Properties of erf(z), official table of values (z = 0 to 2.0) and linear interpolation
│
├── 🌡️ 3. FACTORS GOVERNING DIFFUSIVITY (Slides 23-27)
│   ├── Arrhenius Equation: D = D₀ · exp(-ED / RT)
│   ├── Logarithmic linearization: ln D = ln D₀ - (ED / R) · (1/T) (plot with slope -ED/R)
│   ├── Two-temperature formulation: ln(D₂/D₁) = (ED / R) · (1/T₁ - 1/T₂)
│   └── Factors that modulate D:
│       ├── Atomic mechanism (Interstitial vs Vacancy: DC ≫ DFe)
│       ├── Crystal structure of the matrix (Open BCC lattice > Close-packed FCC lattice)
│       ├── Crystal defects and short circuits: Dsurface > Dgrain boundary > Dvolume
│       └── Solute concentration and homologous temperature T/Tm
│
└── ⚙️ 4. INDUSTRIAL AND AEROSPACE APPLICATIONS (Slides 29-35)
    ├── Surface carburizing of steels (Case hardening, CH₄-H₂, compressive stresses, gears)
    ├── Hydrogen gas purification with Palladium (Pd) membranes
    ├── Sintering of ceramics and metals (densification and elimination of porosity)
    ├── Diffusion bonding and superplastic forming (DB/SPF, Rolls-Royce Trent 500 blades)
    ├── Doping of Silicon wafers in microelectronics and nitriding of Si powder (Si₃N₄)
    └── Permeation barrier in polymer films against O₂ and moisture
```

---

## 📐 2. Fundamental Equations and Mathematical Relations

### 1. Diffusional Flux and Fick's First Law (Steady State):
$$J = \frac{M}{A \cdot t} \quad \left[\frac{\text{kg}}{\text{m}^2\cdot\text{s}}\right] \quad \text{or} \quad \left[\frac{\text{mol}}{\text{cm}^2\cdot\text{s}}\right]$$
$$J = -D \frac{\partial C}{\partial x} \approx -D \frac{\Delta C}{\Delta x} = D \frac{C_{\text{high}} - C_{\text{low}}}{\Delta x}$$

### 2. Fick's Second Law and Solution in a Semi-Infinite Solid:
$$\frac{\partial C_x}{\partial t} = D \frac{\partial^2 C_x}{\partial x^2}$$
$$\frac{C_x - C_0}{C_s - C_0} = 1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right) \iff \frac{C_s - C_x}{C_s - C_0} = \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right) = \text{erf}(z)$$

where $z \equiv \frac{x}{2\sqrt{Dt}}$, allowing the time to be solved for:
$$t = \frac{x^2}{4 \cdot z^2 \cdot D}$$

### 3. Arrhenius Equation for Thermal Diffusivity:
$$D = D_0 \exp\left(-\frac{E_D}{RT}\right)$$
$$\ln D = \ln D_0 - \left(\frac{E_D}{R}\right) \frac{1}{T}$$
$$\ln\left(\frac{D_2}{D_1}\right) = \frac{E_D}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) \implies E_D = \frac{R \cdot \ln(D_2 / D_1)}{\frac{1}{T_1} - \frac{1}{T_2}}$$

### 4. Hierarchy of Diffusivities by Defects and Structure:
$$D_{\text{surface}} > D_{\text{grain boundary}} > D_{\text{volume (lattice)}}$$
$$D_{\text{interstitial}} \gg D_{\text{vacancy}} \quad (\text{factor of } 10^4\text{--}10^6)$$
$$D_{\text{BCC}} > D_{\text{FCC}} \quad (\text{for the same solute and the same } T)$$

---

## 📚 3. Index of Atomic Concept Notes (5 Concepts)

1. [[Concept - Diffusion Mechanisms, Vacancies and Interstitials]]  
   *Definition of thermal transport, driving force from the chemical potential gradient, self-diffusion and interdiffusion with Hume-Rothery rules, $E_a\text{--}T_m$ correlation and accelerated kinetics of interstitial solutes ($\text{C}, \text{H}, \text{N}$).*
2. [[Concept - Fick's First Law, Steady-State Diffusion]]  
   *Definition of the diffusional flux $J$, steady-state conditions ($\partial C/\partial t = 0$), negative sign of the gradient, linear profiles in flat membranes and formulation of mass transport.*
3. [[Concept - Fick's Second Law, Non-Steady-State Diffusion and the Error Function]]  
   *Derivation by differential continuity, hypothesis $D \neq f(C)$, semi-infinite solid with $C_s$ and $C_0$, definition of $\text{erf}(z)$, complete official table from $z = 0$ to $2.0$ and linear interpolation algorithm.*
4. [[Concept - The Arrhenius Equation and Factors Influencing Diffusivity]]  
   *Thermal dependence $D(T)$, logarithmic linearization and the two-temperature method, modulating factors (atomic size, open BCC vs close-packed FCC lattice, short-circuit diffusion at grain boundaries and surfaces).*
5. [[Concept - Carburizing and Industrial Applications of Diffusion]]  
   *Gas carburizing thermochemical treatment (*case hardening*) in gear steels, palladium membranes for $\text{H}_2$, sintering of ceramics, DB/SPF diffusion bonding in Rolls-Royce Trent 500 blades and polymer barriers.*

---

## ✏️ 4. Collection of Official Solved Problems (6 Problems)

| Code | Problem Title | Topic and Physical Phenomenon | Official Result |
| :---: | :--- | :--- | :---: |
| **T3-01** | [[Problem - T3-01 Carburisation of a 1018 Steel Gear]] | Fick 2 · Semi-infinite solid · $\text{erf}(z)$ interpolation | $t = 6638\text{ s} = 1.84\text{ h}$ (official $6636\text{ s}$) |
| **T3-02** | [[Problem - T3-02 Diffusion of Aluminium in Single-Crystal Silicon]] | Inverse Arrhenius · Semiconductor doping | $T = 1566\text{ K} = 1293^\circ\text{C}$ |
| **T3-03** | [[Problem - T3-03 Activation Energy and Diffusivity of Carbon in Steel]] | Two-temperature method · $E_D$ and extrapolation $D(1000^\circ\text{C})$ | $E_D = 36\text{ kcal/mol}$, $D = 3.23 \times 10^{-11}\text{ m}^2/\text{s}$ |
| **T3-04** | [[Problem - T3-04 Ionic Transport of Nickel through an MgO Plate]] | Fick 1 · Ionic transport in a ceramic · FCC $\text{Ni}$ lattice | $t = 309\text{ h}$ |
| **T3-05** | [[Problem - T3-05 Carburising Temperature of 1010 Steel in 8 Hours]] | Coupling of Fick 2 + Arrhenius · Thermal design | $T = 1175\text{ K} = 902^\circ\text{C}$ |
| **T3-06** | [[Problem - T3-06 Hydrogen Purification with a Palladium Membrane]] | Fick 1 · Permeation through a $\text{Pd}$ membrane · Mass flow | $\Delta x = 5\text{ mm}$ |

---

## 🔗 Navigation and Return
* [[Aerospace Materials I MOC|⬅️ Back to the Subject MOC]]
* [[00 - Indice Central/Master Index|🗺️ Master Index of the Vault]]
* Theory Web Portal: `subjects/aerospace-materials-1/teoria/topic-3-diffusion.html`
* Problems Web Portal: `subjects/aerospace-materials-1/problemas/topic-3-diffusion.html`
