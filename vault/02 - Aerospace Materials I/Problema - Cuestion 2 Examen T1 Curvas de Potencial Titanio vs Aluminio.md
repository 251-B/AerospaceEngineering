---
materia: "Aerospace Materials I"
tema: "Tema 1: Bonding in Solids"
origen: "Session 2 T1 Bonding_2025.pdf, Slide 39, Question 2"
dificultad: alta
tags:
  - problema-examen
  - resuelto
  - potential-well
  - titanium
  - aluminum
  - young-modulus
  - thermal-expansion
---

# ✏️ Problema: Cuestión 2 Examen T1 — Curvas de Potencial Titanio vs Aluminio

## 📄 Enunciado Oficial [Slide 39]
> **Titanium is stiffer than aluminum, has a lower thermal expansion coefficient than aluminum, and has a higher melting temperature than aluminum. On the same graph, carefully and schematically draw the potential well curves for both metals and showing how the physical properties are manifested in these curves.**

---

## 📊 1. Fase 1: Planteamiento Físico, Datos e Hipótesis

### Datos Comparativos de Ingeniería Aeroespacial:
| Physical Property | Symbol | Titanium ($\text{Ti}$, $Z=22$) | Aluminum ($\text{Al}$, $Z=13$) | Comparative Relation |
| :--- | :--- | :--- | :--- | :--- |
| **Young's Modulus (Stiffness)** | $E$ | $\approx 115\text{ GPa}$ | $\approx 69\text{ GPa}$ | $E_{\text{Ti}} > E_{\text{Al}}$ (Stiffer) |
| **Melting Temperature** | $T_m$ | $1668^\circ\text{C}$ ($1941\text{ K}$) | $660^\circ\text{C}$ ($933\text{ K}$) | $T_{m,\text{Ti}} \gg T_{m,\text{Al}}$ |
| **Thermal Expansion Coeff.** | $\alpha$ | $\approx 8.6 \times 10^{-6}\text{ K}^{-1}$ | $\approx 23.1 \times 10^{-6}\text{ K}^{-1}$ | $\alpha_{\text{Ti}} \ll \alpha_{\text{Al}}$ |
| **Equilibrium Interatomic Spacing** | $r_0$ | $\approx 0.289\text{ nm}$ | $\approx 0.286\text{ nm}$ | $r_{0,\text{Ti}} \approx r_{0,\text{Al}}$ (very close) |

### Hipótesis de Partida:
1. Both metals are treated at the interatomic level through their effective pairwise potential energy function $E_{\text{net}}(r) = E_{\text{att}}(r) + E_{\text{rep}}(r)$.
2. Titanium is an early $3d$ transition metal ($[\text{Ar}]\,3d^2 4s^2$) with partially filled $d$-orbitals creating strong localized hybridization, whereas Aluminum is a simple $s$-$p$ post-transition metal ($[\text{Ne}]\,3s^2 3p^1$).

---

## 🧠 2. Fase 2: Formulación Fundamental y Vinculación Matemática

### Justificación Teórica Previa:
To draw the curves correctly, each of the three macroscopic engineering properties must be explicitly mapped to a precise geometric feature of the potential well $E(r)$ [Slides 8, 10, 12, 13]:

1. **Melting Temperature ($T_m$) $\longleftrightarrow$ Depth of the Potential Well ($E_0$):**
   * Melting requires thermal energy $k_B T$ sufficient to overcome the cohesive binding energy holding atoms in their lattice sites:
     $$k_B T_m \propto E_0 = |E(r_0)|$$
   * Because $T_{m,\text{Ti}} (1668^\circ\text{C}) > T_{m,\text{Al}} (660^\circ\text{C})$, **the potential well for Titanium must be significantly deeper** than that for Aluminum:
     $$E_{0,\text{Ti}} \gg E_{0,\text{Al}}$$

2. **Young's Modulus ($E$) $\longleftrightarrow$ Curvature at the Minimum ($d^2E/dr^2|_{r_0}$):**
   * The elastic modulus is directly proportional to the second derivative (curvature) of the potential curve evaluated at the equilibrium distance $r_0$:
     $$E = \frac{1}{r_0}\left.\frac{d^2 E}{dr^2}\right|_{r = r_0}$$
   * Because Titanium is stiffer ($E_{\text{Ti}} > E_{\text{Al}}$), **the bottom of Titanium's potential well must be noticeably narrower and sharper (higher curvature)**, representing a stiffer atomic spring constant.

3. **Coefficient of Thermal Expansion ($\alpha$) $\longleftrightarrow$ Well Asymmetry (Anharmonicity):**
   * The expansion coefficient reflects the shift of the average interatomic distance $\bar{r}(T)$ as thermal energy $k_B T$ increases:
     $$\alpha = \frac{1}{r_0}\frac{d\bar{r}}{dT}$$
   * Because Aluminum has a much higher thermal expansion coefficient ($\alpha_{\text{Al}} \approx 2.7 \times \alpha_{\text{Ti}}$), **Aluminum's potential well must be significantly broader, shallower, and much more asymmetric (anharmonic)** on its attractive branch ($r > r_0$) than Titanium's.

---

## 🔢 3. Fase 3: Representación Gráfica y Análisis Geométrico Detallado

```
Energy E(r)
   ▲
   │                              Repulsive Branch (Steep Pauli Repulsion)
   │                           \   \
   │                            \   \
 0 ┼─────────────────────────────\───\──────────────────────────────────► Distance r
   │                              \   \
   │                               \   \      Attractive Branch (Coulombic/Covalent)
   │                                \   \
-E₀(Al) ├────────────────────────────*───\────  Aluminum (Shallower, Broader, Asymmetric)
   │                                / \   \
   │                               /   \   \
   │                              /     \   \
   │                             /       \   \
-E₀(Ti) ├────────────────────────*────────\─── Titanium (Deeper, Narrower, Sharper)
   │                            r₀(Ti) ≈ r₀(Al)
   ▼
```

### Manifestación Gráfica Explícita de las Propiedades:
1. **Vertical Trough Depth ($E_0$):**
   * Titanium's minimum is positioned much lower along the vertical energy axis:
     $$|E_0(\text{Ti})| \approx 470\text{ kJ/mol} \quad \text{vs} \quad |E_0(\text{Al})| \approx 326\text{ kJ/mol}$$
   * *Manifestation:* Proves why Titanium retains solid structural integrity up to $1668^\circ\text{C}$, whereas Aluminum melts at $660^\circ\text{C}$.
2. **Bottom Curvature ($d^2E/dr^2$):**
   * The trough of the Titanium curve has a very small radius of curvature (steep parabolic opening $U(r) \approx -E_0 + \frac{1}{2} k_{\text{Ti}} (r-r_0)^2$), whereas Aluminum opens broadly.
   * *Manifestation:* Explains why Titanium exhibits $E = 115\text{ GPa}$ compared to Aluminum's $E = 69\text{ GPa}$.
3. **Width and Asymmetry at High Thermal Levels:**
   * At an energy level corresponding to room temperature or elevated operational temperatures ($\Delta E = k_B T$), draw a horizontal chord across each well connecting $r_{\text{min}}$ and $r_{\text{max}}$.
   * For Aluminum, the midpoint $\bar{r}_{\text{Al}} = \frac{r_{\text{min}} + r_{\text{max}}}{2}$ shifts substantially to the right of $r_0$ because the attractive wall flares out widely.
   * For Titanium, the deep well confines the vibrational excursion to a steep, nearly symmetric region, so $\bar{r}_{\text{Ti}}$ shifts only slightly.
   * *Manifestation:* Demonstrates why $\alpha_{\text{Al}} = 23 \times 10^{-6}\text{ K}^{-1}$ is nearly triple $\alpha_{\text{Ti}} = 8.6 \times 10^{-6}\text{ K}^{-1}$.

---

## 🎯 4. Fase 4: Interpretación Física y Conclusiones Aeroespaciales

* **Electronic Origin:** In Aluminum, bonding is sustained purely by $3s^2 3p^1$ valence electrons forming a relatively compliant electron sea. In Titanium ($[Ar]\,3d^2 4s^2$), the partially filled $3d$ electron orbitals participate actively in bonding through localized covalent-like directional hybridization superimposed onto the metallic electron sea.
* **Engineering Impact:** In supersonic aircraft structures and compressor stages of jet engines (e.g., Eurofighter Typhoon, CFM LEAP engines), aerodynamic skin friction heats components to $200\text{--}450^\circ\text{C}$. Aluminum rapidly loses its stiffness and expands excessively above $150^\circ\text{C}$, whereas Titanium retains superior stiffness ($E$), resists creep, and maintains tight aerodynamic clearances due to its low $\alpha$.

---
*Retorno:* `[[Tema 1 - Bonding in Solids and Material Properties|⬅️ Volver a Tema 1]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
