---
materia: "Aerospace Materials I"
tema: "Tema 1: Bonding in Solids"
fuentes: "Session 2 T1 Bonding_2025.pdf, Slides 7-13, 20-21, 24, 39"
tags:
  - teoria
  - concepto-clave
  - potential-well
  - young-modulus
  - thermal-expansion
  - melting-point
dificultad: media
prerrequisitos:
  - "Cálculo diferencial e integral básico"
---

# 📖 Concepto: Curvas de Energía Potencial Interatómica y Propiedades Macroscópicas

> **Key Idea in One Sentence:** The interatomic potential energy curve $E(r)$—specifically its minimum location $r_0$, trough depth $E_0$, local curvature $(d^2E/dr^2)_{r_0}$, and asymmetric anharmonicity—serves as the universal microscopic blueprint that directly dictates the macroscopic equilibrium volume, melting point ($T_m$), Young's elastic modulus ($E$), and coefficient of thermal expansion ($\alpha$) of aerospace structural materials.

---

## 🎯 1. Anatomy of the Interatomic Potential Energy Curve $E(r)$

The interaction between two isolated atoms or ions as a function of separation distance $r$ is described by a net potential energy $E_{\text{net}}(r)$ comprising an attractive term $E_{\text{att}}(r)$ and a repulsive term $E_{\text{rep}}(r)$ [Slides 7-8]:

$$E_{\text{net}}(r) = E_{\text{att}}(r) + E_{\text{rep}}(r) = -\frac{A}{r^m} + \frac{B}{r^n} \quad (n > m)$$

```
Energy E(r)
   ▲
   │                           E_rep(r) = +B / rⁿ
   │            \             /
   │             \           /
 0 ┼──────────────\─────────/──────────────────────────► Distance r
   │               \       /     E_att(r) = -A / rᵐ
   │                \     /
   │                 \   /
-E₀├───────────────────*  (r₀, -E₀)  <--- Equilibrium Point
   │                 Equilibrium
   │                 Distance r₀
   ▼
```

### 1.1 Key Geometric Features:
1. **Equilibrium Separation ($r_0$):**
   * The distance where attractive and repulsive forces exactly balance.
   * Net interatomic force:
     $$F_{\text{net}}(r) = -\frac{dE_{\text{net}}}{dr}$$
     $$\left.F_{\text{net}}\right|_{r = r_0} = -\left.\frac{dE_{\text{net}}}{dr}\right|_{r = r_0} = 0$$
   * $r_0$ determines the equilibrium lattice parameter and macroscopic mass density $\rho$.
2. **Binding Energy / Well Depth ($E_0$):**
   * The energy required to separate the bonded atoms from equilibrium $r_0$ to infinite distance ($r \to \infty$):
     $$E_0 = -E_{\text{net}}(r_0)$$
   * Represents the cohesive bond strength of the solid.

---

## 🏗️ 2. Young's Modulus ($E$) from Potential Well Curvature [Slide 13]

### 2.1 Derivation from First Principles
When a macroscopic tensile stress $\sigma$ is applied to an elastic material, it stretches the interatomic bonds by a small displacement $\Delta r$ away from equilibrium $r_0$. The strain is:

$$\varepsilon = \frac{\Delta r}{r_0} = \frac{r - r_0}{r_0}$$

Expanding the net interatomic force $F(r)$ in a Taylor series about $r = r_0$:

$$F(r) = F(r_0) + \left.\frac{dF}{dr}\right|_{r_0}(r - r_0) + \mathcal{O}((r - r_0)^2)$$

Since $F(r_0) = 0$:

$$F(r) \approx \left.\frac{dF}{dr}\right|_{r_0}\Delta r$$

The microscopic atomic stiffness / spring constant $S_0$ is defined as:

$$S_0 = \left.\frac{dF}{dr}\right|_{r_0} = -\left.\frac{d^2 E_{\text{net}}}{dr^2}\right|_{r_0}$$

*(Note: Depending on sign conventions for force, with $F_{\text{net}} = -\nabla E$, the restorative slope $dF/dr$ relates to the positive curvature $\left.\frac{d^2 E}{dr^2}\right|_{r_0} > 0$).*

Relating microscopic atomic force to macroscopic stress ($\sigma = F/r_0^2$) and strain ($\varepsilon = \Delta r/r_0$):

$$\sigma = \frac{F}{r_0^2} = \frac{S_0 \Delta r}{r_0^2} = \left(\frac{S_0}{r_0}\right)\left(\frac{\Delta r}{r_0}\right) = \left(\frac{S_0}{r_0}\right)\varepsilon$$

Comparing with Hooke's Law ($\sigma = E \varepsilon$):

$$E_{\text{Young}} = \frac{S_0}{r_0} = \frac{1}{r_0}\left.\frac{d^2 E_{\text{net}}}{dr^2}\right|_{r = r_0}$$

### 2.2 Physical Meaning [Slide 13]:
* **Steep, Deep Well:** A steep potential well possesses a large second derivative (sharp curvature). A very high external mechanical force is required to pull atoms away from $r_0$. Thus, **materials with deep, narrow wells exhibit high Young's modulus ($E$)**.
* **Shallow, Broad Well:** Possesses low curvature, yielding a compliant material with low elastic modulus (e.g., lead or un-crosslinked polymers).

---

## 🌡️ 3. Thermal Expansion ($\alpha$) and Anharmonic Asymmetry [Slide 12]

### 3.1 The Origin of Thermal Expansion
At absolute zero ($T = 0\text{ K}$), atoms reside at the bottom of the well ($r = r_0$). As temperature increases, thermal energy $k_B T$ excites lattice vibrations (phonons). The atoms oscillate back and forth between the inner repulsive wall $r_{\text{min}}(T)$ and the outer attractive wall $r_{\text{max}}(T)$.

```
Energy
  ▲
  │              \
  │               \       T₃   r_min ───●───────●─── r_max  --> Mean r̄(T₃) > r₀
  │                \      T₂      r_min ──●───●── r_max     --> Mean r̄(T₂) > r₀
  │                 \     T₁        r_min ●─● r_max         --> Mean r̄(T₁) > r₀
  │                  \   /                ▲
0 ┼───────────────────\_/─────────────────┼────────────────────────► r
                                          r₀
```

* **Ideal Harmonic (Symmetric) Potential Well:**
  If the potential well were a pure parabola $E(r) = \frac{1}{2}k(r-r_0)^2$, the oscillation would be completely symmetric around $r_0$. The mean atomic position would be:
  $$\bar{r}(T) = \frac{r_{\text{min}}(T) + r_{\text{max}}(T)}{2} = r_0 = \text{constant}$$
  **In a perfectly harmonic material, the thermal expansion coefficient would be zero ($\alpha = 0$)!**
* **Real Anharmonic (Asymmetric) Potential Well:**
  Real atomic interactions are fundamentally **anharmonic**:
  * At $r < r_0$, the Pauli electron cloud repulsion is extremely steep ($n \approx 5\text{--}12$).
  * At $r > r_0$, the electrostatic/covalent attraction decays much more gradually ($m \approx 1\text{--}6$).
  * Because the attractive branch is flatter than the repulsive branch, as thermal energy increases, $r_{\text{max}}$ extends much farther than $r_{\text{min}}$ contracts.
  * Consequently, the average interatomic spacing $\bar{r}(T)$ **shifts progressively to larger values with rising temperature**:
    $$\frac{d\bar{r}}{dT} > 0 \implies \alpha = \frac{1}{r_0}\frac{d\bar{r}}{dT} > 0$$

### 3.2 Correlation with Well Depth [Slide 12]:
* **Strong Bonds (Deep, Narrow Well):** High binding energy $E_0$ restricts vibration amplitudes and forces the trough to be more symmetric near the bottom. Hence, materials with strong bonds have **very low coefficients of thermal expansion ($\alpha$)**.
* **Weak Bonds (Shallow, Asymmetric Well):** Flatter trough promotes massive vibrational asymmetry, leading to **high thermal expansion ($\alpha$)**.

---

## 🔥 4. Melting Temperature ($T_m$) [Slide 10]

Melting occurs when the average thermal vibrational energy of the crystal lattice approaches the depth of the cohesive potential well:

$$k_B T_m \propto E_0$$

Where $k_B = 1.38 \times 10^{-23}\text{ J/K}$ is Boltzmann's constant.
* Materials with deep potential wells (e.g., transition metals like Tungsten, covalent networks like Diamond, divalent ceramics like $\text{MgO}$) require immense thermal agitation to overcome the binding energy $E_0$, exhibiting **high melting temperatures ($T_m > 1500\text{--}3500^\circ\text{C}$)**.
* Materials with shallow wells (e.g., alkali metals like Potassium, molecular solids) melt at very low temperatures ($T_m < 100^\circ\text{C}$).

---

## 📈 5. Synthesis: Interatomic Well Diagnostic Matrix

| Property | Symbol | Potential Curve Metric | Strong / Deep Well ($E_0 \uparrow$) | Weak / Shallow Well ($E_0 \downarrow$) |
| :--- | :--- | :--- | :--- | :--- |
| **Melting Point** | $T_m$ | Well depth $E_0$ | **Very High** | **Low** |
| **Young's Modulus** | $E$ | Well curvature $\left.\frac{d^2E}{dr^2}\right\|_{r_0}$ | **High (Stiff)** | **Low (Compliant)** |
| **Thermal Expansion** | $\alpha$ | Well asymmetry (anharmonicity) | **Low ($\alpha \downarrow$)** | **High ($\alpha \uparrow$)** |
| **Hardness (Mohs)** | $H$ | Curvature + depth + bond density | **High (Scratch-resistant)** | **Low (Soft)** |

---

## 🔗 Related Notes
* `[[Tema 1 - Bonding in Solids and Material Properties]]`
* `[[Concepto - Enlace Ionico y Energia Reticular de Born-Lande]]`
* `[[Concepto - Enlace Metalico y Teoria de Bandas de Energia]]`
* `[[Problema - Cuestion 2 Examen T1 Curvas de Potencial Titanio vs Aluminio]]`
* `[[Problema - Cuestion 3 Examen T1 Modulo de Elasticidad MgO vs Mg]]`
* `[[Problema - Cuestion 4 Examen T1 Modulo de Elasticidad Aluminio vs Silicio]]`
