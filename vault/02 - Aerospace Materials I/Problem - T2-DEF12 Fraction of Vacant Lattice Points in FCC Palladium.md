---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 12"
dificultad: medium
tags:
  - official-problem
  - solved
  - palladium
  - fcc
  - vacant-lattice-points
  - density-deficit
---

# ✏️ Problem: T2-DEF12 — Fraction of Vacant Lattice Points in FCC Palladium

## 📄 Official Statement
> **12. The density of a sample of FCC palladium is $11.98\text{ g/cm}^3$, and its lattice parameter is $3.8902\text{ \AA}$. Calculate:**  
> **a)** The fraction of the lattice points that contain vacancies. *(Solution: $0.00204$)*  
> **b)** The total number of vacancies in a cubic centimeter of $\text{Pd}$. *(Solution: $1.39 \times 10^{20}\text{ vacancies/cm}^3$)*  
> **Data:** $M_{\text{Pd}} = 106.4\text{ g/mol}$; $N_A = 6.022 \times 10^{23}\text{ atoms/mol}$.

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Input Data:
* Material: Metallic palladium ($\text{Pd}$).
* Crystal structure: Face-Centred Cubic (FCC) $\implies n_{\text{sitios}} = 4\text{ lattice sites/cell}$.
* Measured lattice parameter: $a = 3.8902\text{ \AA} = 3.8902 \times 10^{-8}\text{ cm}$.
* Measured real density: $\rho_{\text{real}} = 11.98\text{ g/cm}^3$.
* Molar atomic mass: $M_{\text{Pd}} = 106.4\text{ g/mol}$.
* Avogadro number: $N_A = 6.022 \times 10^{23}\text{ átomos/mol}$.

---

## 🧠 2. Phase 2: Frames and Change of Basis

1. **Ideal Theoretical Density of the Perfect Crystal ($\rho_{\text{ideal}}$) [Session 4 Slide 7, 15]:**
   If all lattice points were occupied by palladium atoms with no vacancies at all:
   $$\rho_{\text{ideal}} = \frac{n \cdot M_{\text{Pd}}}{a^3 \cdot N_A} = \frac{4 \cdot M_{\text{Pd}}}{a^3 \cdot N_A}$$
2. **Fraction of Vacant Lattice Points ($f_v$):**
   The existence of vacancies reduces the mass contained in the cell without appreciably altering its lattice parameter $a$. The vacancy fraction is the relative density deficit:
   $$f_v = \frac{\rho_{\text{ideal}} - \rho_{\text{real}}}{\rho_{\text{ideal}}} = 1 - \frac{\rho_{\text{real}}}{\rho_{\text{ideal}}}$$
3. **Total Number of Vacancies per Cubic Centimetre ($n_v$):**
   The total number density of lattice points per cubic centimetre is:
   $$N = \frac{n_{\text{sitios}}}{V_C} = \frac{4}{a^3}$$
   The absolute number of vacancies per cubic centimetre is:
   $$n_v = f_v \cdot N$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Ideal Theoretical Density ($\rho_{\text{ideal}}$):
* Unit cell volume:
  $$V_C = a^3 = (3.8902 \times 10^{-8}\text{ cm})^3 = 5.88729 \times 10^{-23}\text{ cm}^3$$
* Theoretical mass of the perfect unit cell:
  $$m_{\text{celda}} = \frac{4 \times 106.4\text{ g/mol}}{6.022 \times 10^{23}\text{ mol}^{-1}} = \frac{425.6}{6.022 \times 10^{23}} = 7.06742 \times 10^{-22}\text{ g}$$
* Theoretical density:
  $$\rho_{\text{ideal}} = \frac{7.06742 \times 10^{-22}\text{ g}}{5.88729 \times 10^{-23}\text{ cm}^3} = \mathbf{12.0045\text{ g/cm}^3}$$

---

### 2. Part a: Fraction of Vacant Lattice Points ($f_v$):
$$f_v = \frac{\rho_{\text{ideal}} - \rho_{\text{real}}}{\rho_{\text{ideal}}} = \frac{12.0045 - 11.9800}{12.0045} = \frac{0.0245}{12.0045}$$
$$f_v = \mathbf{0.00204} \quad (\approx 0.204\%)$$

---

### 3. Part b: Number of Vacancies per Cubic Centimetre ($n_v$):
* Total concentration of lattice points ($N$):
  $$N = \frac{4}{a^3} = \frac{4}{5.88729 \times 10^{-23}\text{ cm}^3} = 6.7943 \times 10^{22}\text{ sitios/cm}^3$$
* Volumetric vacancy concentration:
  $$n_v = f_v \cdot N = (0.002043) \times (6.7943 \times 10^{22}\text{ cm}^{-3}) = \mathbf{1.388 \times 10^{20}\text{ vacantes/cm}^3} \approx \mathbf{1.39 \times 10^{20}\text{ vac/cm}^3}$$
  The unrounded fraction $f_v = 0.0020432$ gives $n_v = 1.388 \times 10^{20}\text{ cm}^{-3}$; both results agree with the official $0.00204$ and $1.39 \times 10^{20}\text{ cm}^{-3}$.

---

## 🎯 4. Phase 4: Units and Limits

* **Pycnometric and Dilatometric Detection:** This problem reflects the classic Simmons and Balluffi method: by comparing the lattice-parameter variation obtained by X-ray diffraction ($\Delta a / a$) with the macroscopic dimensional variation from dilatometry ($\Delta L / L$), or by contrasting the hydrostatic density with the X-ray theoretical one, the absolute concentration of thermal vacancies in noble metals such as palladium, platinum and gold is measured non-destructively.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
