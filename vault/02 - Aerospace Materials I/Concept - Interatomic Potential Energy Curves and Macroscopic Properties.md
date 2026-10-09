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
   * For $E_{\text{net}}(r) = -A/r^m + B/r^n$ ($n > m$) the force is
     $$F_{\text{net}}(r) = -\frac{mA}{r^{m+1}} + \frac{nB}{r^{n+1}}$$
     and the integral relation with explicit limits is
     $$E_{\text{net}}(r) = -\int_\infty^r F_{\text{net}}(r')\,dr' = -\left[\frac{A}{r'^{\,m}} - \frac{B}{r'^{\,n}}\right]_{\infty}^{r} = -\frac{A}{r^m} + \frac{B}{r^n}$$
     The equilibrium condition is $mA/r_0^{m+1} = nB/r_0^{n+1}$.
   * $r_0$ determines the equilibrium lattice parameter and macroscopic mass density $\rho$.
2. **Binding Energy / Well Depth ($E_0$):**
   * The energy required to separate the bonded atoms from equilibrium $r_0$ to infinite distance ($r \to \infty$):
     $$E_0 = -E_{\text{net}}(r_0)$$
   * Represents the cohesive bond strength of the solid.

### 1.2 Closed Forms of $r_0$ and $E_0$ from $dE/dr = 0$ (added derivation)
Start from $E_{\text{net}}(r) = -A/r^m + B/r^n$ and differentiate term by term, using $\frac{d}{dr}r^{-m} = -m\,r^{-m-1}$:

$$\frac{dE_{\text{net}}}{dr} = \frac{mA}{r^{m+1}} - \frac{nB}{r^{n+1}}$$

Setting $dE_{\text{net}}/dr = 0$ at $r = r_0$ and multiplying by $r_0^{n+1}$:

$$mA\,r_0^{\,n-m} = nB \quad\Longrightarrow\quad r_0 = \left(\frac{nB}{mA}\right)^{1/(n-m)}, \qquad B = \frac{mA}{n}\,r_0^{\,n-m}$$

Eliminate $B$ from $E_{\text{net}}(r_0)$:

$$E_{\text{net}}(r_0) = -\frac{A}{r_0^m} + \frac{1}{r_0^n}\,\frac{mA}{n}\,r_0^{\,n-m} = -\frac{A}{r_0^m}\left(1 - \frac{m}{n}\right) \;\Longrightarrow\; \boxed{E_0 = \frac{A}{r_0^m}\left(1 - \frac{m}{n}\right) = \frac{A\,(n-m)}{n\,r_0^m}}$$

Check with the ionic pair ($m = 1$, $A = Z_1 Z_2 e^2/4\pi\varepsilon_0$): $E_0 = \frac{Z_1 Z_2 e^2}{4\pi\varepsilon_0 a_0}\left(1 - \frac{1}{n}\right)$, identical to the Born result of [[Concept - Ionic Bonding and Born-Lande Lattice Energy]]. Because $n > m$, $0 < E_0 < A/r_0^m$: the repulsion gives back a fraction $m/n$ of the attractive energy at equilibrium (about $1/n \approx 11\text{--}20\%$ for an ionic pair).

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

$$S_0 = -\left.\frac{dF}{dr}\right|_{r_0} = \left.\frac{d^2 E_{\text{net}}}{dr^2}\right|_{r_0} = \frac{m(n-m)A}{r_0^{m+2}} > 0$$

*(Note: with $F_{\text{net}} = -dE_{\text{net}}/dr$, the slope $dF/dr$ at $r_0$ is negative (restoring force, $F \approx -S_0\,\Delta r$), while the curvature $d^2E/dr^2|_{r_0}$ is positive; $S_0$ is defined as the positive quantity. The closed form follows from the equilibrium condition above.)*

Relating the magnitude of the microscopic restoring force to macroscopic stress ($\sigma = |F|/r_0^2$) and strain ($\varepsilon = \Delta r/r_0$):

$$\sigma = \frac{F}{r_0^2} = \frac{S_0 \Delta r}{r_0^2} = \left(\frac{S_0}{r_0}\right)\left(\frac{\Delta r}{r_0}\right) = \left(\frac{S_0}{r_0}\right)\varepsilon$$

Comparing with Hooke's Law ($\sigma = E \varepsilon$). *Note:* Slide 13 is qualitative (steep, narrow well gives high $E$); $E \propto S_0/r_0$ is an order-of-magnitude extension (for NaCl it gives about $255\text{ GPa}$ against about $40\text{ GPa}$ measured):

$$E_{\text{Young}} \sim \frac{S_0}{r_0} = \frac{1}{r_0}\left.\frac{d^2 E_{\text{net}}}{dr^2}\right|_{r = r_0}$$

### 2.2 Physical Meaning [Slide 13]:
* **Steep, Deep Well:** A steep potential well possesses a large second derivative (sharp curvature). A very high external mechanical force is required to pull atoms away from $r_0$. Thus, **materials with deep, narrow wells exhibit high Young's modulus ($E$)**.
* **Shallow, Broad Well:** Possesses low curvature, yielding a compliant material with low elastic modulus (e.g., lead or un-crosslinked polymers).

### 2.3 Explicit Stiffness of an Ionic Pair and a Caution (extension)
With $m = 1$ and $K \equiv Z_1 Z_2 e^2/4\pi\varepsilon_0$, $E_{\text{net}}(a) = -K/a + b/a^n$, and the equilibrium condition gives $b = K a_0^{\,n-1}/n$. Differentiating twice:

$$\frac{d^2E_{\text{net}}}{da^2} = -\frac{2K}{a^3} + \frac{n(n+1)\,b}{a^{n+2}} \;\Longrightarrow\; S_0 = -\frac{2K}{a_0^3} + \frac{(n+1)K}{a_0^3} = \frac{(n-1)\,K}{a_0^3}$$

which agrees with the general $S_0 = m(n-m)A/r_0^{m+2}$ for $m = 1$. Then $E_{\text{Young}} \sim S_0/a_0 = (n-1)K/a_0^4$.

Numerical check for NaCl ($a_0 = 2.82\ \text{\AA}$, $n = 8$, $K = 2.307\times10^{-28}\ \text{J}\cdot\text{m}$): $S_0 = 72\ \text{N/m}$ and $S_0/a_0 \approx 255\ \text{GPa}$. The measured $E_{\text{NaCl}}$ is about $40\ \text{GPa}$, so this single-pair estimate is only an order-of-magnitude indicator: it ignores the Madelung sum, the lattice geometry and the conversion from a bond stiffness to the stiffness of a given crystal direction. The qualitative conclusion of the slides is unchanged: a larger $K$ (higher valences) and a smaller $a_0$ give a larger curvature, hence a larger $E$.

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

### 3.3 Quantitative Link Between Well Depth and $\alpha$ (extension, beyond the slides)
Expand the well about $r_0$ with $x = r - r_0$ as $E(r) = -E_0 + c\,x^2 - g\,x^3$, where $c = \tfrac12 S_0$ and $g = -\tfrac16\,E^{(3)}(r_0)$. For the $(m, n)$ potential, differentiating the force expression once more gives $E^{(3)}(r_0) = -m(n-m)(m+n+3)A/r_0^{m+3}$, so $g = m(n-m)(m+n+3)A/(6\,r_0^{m+3})$.

The thermal mean displacement follows from the Boltzmann average $\langle x\rangle = \int x\,e^{-E/k_BT}dx \big/ \int e^{-E/k_BT}dx$. To first order in the small cubic term, $e^{g x^3/k_BT} \approx 1 + g x^3/k_BT$, and with the Gaussian moments $\langle x^2\rangle_0 = k_BT/(2c)$ and $\langle x^4\rangle_0 = 3\langle x^2\rangle_0^2$:

$$\langle x\rangle = \frac{g}{k_BT}\langle x^4\rangle_0 = \frac{g}{k_BT}\cdot 3\left(\frac{k_BT}{2c}\right)^2 = \frac{3g\,k_BT}{4c^2} = \frac{3g\,k_BT}{S_0^2}$$

so $\alpha = \dfrac{1}{r_0}\dfrac{d\langle x\rangle}{dT} = \dfrac{3g\,k_B}{r_0 S_0^2}$. Substituting $g$, $S_0$ and $A\,r_0^{-m} = nE_0/(n-m)$:

$$\boxed{\alpha = \frac{(m+n+3)\,k_B}{2\,m\,n\,E_0}}$$

Hence $\alpha \propto 1/E_0$ at fixed exponents: a deeper well gives a smaller expansion coefficient, in agreement with the slide statement. A symmetric well has $g = 0$ and therefore $\alpha = 0$, as argued above. Verification: for the Lennard-Jones case ($m = 6$, $n = 12$) a direct numerical Boltzmann average at $k_BT = 0.002E_0$ gives $\langle x\rangle = 3.286\times10^{-4}\,r_0$-units, against $3.274\times10^{-4}$ from $3gk_BT/S_0^2$ (0.4 percent difference), and the formula gives $\alpha\,E_0/k_B = 21/144 = 0.1458$. This is a one-dimensional classical model, so absolute values are only indicative.

---

## 🔥 4. Melting Temperature ($T_m$) [Slide 10]

Melting occurs when the average thermal vibrational energy of the crystal lattice approaches the depth of the cohesive potential well:

$$k_B T_m \propto E_0$$

Where $k_B = 1.38 \times 10^{-23}\text{ J/K}$ is Boltzmann's constant.
* Materials with deep potential wells (e.g., transition metals like Tungsten, covalent networks like Diamond, divalent ceramics like $\text{MgO}$) require immense thermal agitation to overcome the binding energy $E_0$, exhibiting **high melting temperatures ($T_m > 1500\text{--}3500^\circ\text{C}$)**.
* Materials with shallow wells (e.g., alkali metals like Potassium, molecular solids) melt at very low temperatures ($T_m < 100^\circ\text{C}$).

### 4.1 Why $T_m \propto E_0$ (Lindemann criterion, extension)
Lindemann's empirical criterion states that a crystal melts when the root-mean-square vibration amplitude reaches a fraction $\delta \approx 0.1$ of the spacing, $\sqrt{\langle x^2\rangle} = \delta\,r_0$. In the harmonic region the equipartition theorem gives $\tfrac12 S_0\langle x^2\rangle = \tfrac12 k_BT$, hence $\langle x^2\rangle = k_BT/S_0$ and

$$k_B T_m = S_0\,\delta^2 r_0^2$$

By dimensional analysis $S_0 r_0^2 \sim E_0$ times a constant of order unity fixed by $m$ and $n$ (from the closed forms above, $S_0 r_0^2 = m\,n\,E_0$), so $k_BT_m = m\,n\,\delta^2\,E_0$ and $T_m \propto E_0$, the slide statement. Check with $m = 6$, $n = 12$, $\delta = 0.1$: $k_BT_m \approx 0.7E_0$, which is of the right order of magnitude for simple solids (the estimate is crude).

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
* [[Topic 1 - Bonding in Solids and Material Properties]]
* [[Concept - Ionic Bonding and Born-Lande Lattice Energy]]
* [[Concept - Metallic Bonding and Energy Band Theory]]
* [[Problem - T1 Exam Question 2 Potential Curves Titanium vs Aluminium]]
* [[Problem - T1 Exam Question 3 Elastic Modulus MgO vs Mg]]
* [[Problem - T1 Exam Question 4 Elastic Modulus Aluminium vs Silicon]]
