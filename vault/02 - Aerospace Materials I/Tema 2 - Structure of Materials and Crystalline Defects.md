---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 3 T2 Structure of Materials I_2025.pdf, Session 4 T2 Structure of Materials II_2025.pdf, Problems T2_CrystStruct.pdf, Problems T2 defects.pdf"
tags:
  - teoria
  - moc-tema
  - crystal-structure
  - crystalline-defects
  - miller-indices
  - dislocations
  - x-ray-diffraction
dificultad: media
prerrequisitos:
  - "[[Tema 1 - Bonding in Solids and Material Properties]]"
---

# 🌐 Tema 2: Structure of Materials and Crystalline Defects

> **Idea Central del Tema:** La disposición geométrica tridimensional de los átomos en redes cristalinas periódicas (cristalografía) y, de forma aún más determinante, la presencia y comportamiento de las **imperfecciones o defectos cristalinos** (puntuales, lineales, planares y volumétricos) gobiernan de forma absoluta las propiedades mecánicas reales, la deformabilidad plástica, la resistencia a la fractura y la respuesta térmica de los materiales metálicos y cerámicos aeroespaciales [Session 3 Slide 2, Session 4 Slide 11].

$$\text{Estructura Cristalina (Bravais)} + \text{Defectos (0D, 1D, 2D)} \implies \text{Propiedades Mecánicas y Aeroespaciales}$$

---

## 🗺️ 1. Mapa Conceptual de Sesiones UC3M

```
TEMA 2: ESTRUCTURA DE MATERIALES Y DEFECTOS CRISTALINOS
│
├── 🏛️ PARTE I: CRISTALOGRAFÍA Y REDES DE BRAVAIS (Sesión 3)
│   ├── Parámetros de Red y 7 Sistemas Cristalinos (Cúbico, Tetragonal, Ortorrómbico, Romboédrico, Hexagonal, Monoclínico, Triclínico)
│   ├── Las 14 Redes de Bravais (P, I, F, C) [Auguste Bravais, 1848]
│   ├── Estructuras Metálicas Fundamentales: BCC (n=2, APF=0.68), FCC (n=4, APF=0.74), HCP (n=6, APF=0.74)
│   ├── Apilamiento Compacto: ABABAB... (HCP) vs ABCABC... (FCC) y relación ideal c/a = √(8/3) ≈ 1.633
│   ├── Huecos Intersticiales: Tetraédricos (2n) y Octaédricos (n) en FCC, BCC y HCP
│   ├── Índices de Miller para Direcciones [uvw] y Planos (hkl) en Sistemas Cúbicos
│   ├── Índices de Miller-Bravais de 4 ejes para Redes Hexagonales (hkil) y [uvtw]
│   └── Difracción de Rayos X (XRD), Espaciados Interplanares dhkl y Ley de Bragg (λ = 2d·sin θ)
│
└── 🔬 PARTE II: DENSIDADES, DEFECTOS RETICULARES Y POLIMORFISMO (Sesión 4)
    ├── Cálculos de Densidad en Redes: Volumétrica (ρv), Lineal (ρl) y Planar (ρp)
    ├── Defectos Puntuales (0D): Vacantes térmicas (nv/N = exp(-ΔHv/RT)), autointersticiales
    ├── Cristales Iónicos: Pares de Schottky (ns = N·exp(-ΔHs/2RT)) y Frenkel (nF = √(N·Ni)·exp(-ΔHF/2RT))
    ├── Soluciones Sólidas: Sustitucionales vs Intersticiales, Reglas de Hume-Rothery (4 criterios)
    ├── Compensación de Carga Eléctrica en Cerámicos (3Mg²⁺ ↔ 2Al³⁺ + 1 vacante catiónica)
    ├── Fenómeno de Orden-Desorden en Aleaciones (Cu-Au a T = 390 °C)
    ├── Defectos Lineales / Dislocaciones (1D): Borde (Taylor, b ⊥ t), Tornillo (Burgers, b || t) y Mixtas
    ├── Vector de Burgers b, Circuito de Burgers y Energía Elástica Almacenada (E ∝ |b|²)
    ├── Sistemas de Deslizamiento: Planos compactos + Direcciones compactas (FCC: 12, BCC: 12, HCP: 3)
    ├── Defectos Planares (2D): Límites de grano (2-5 distancias atómicas, alta energía interfacial)
    ├── Ecuación de Hall-Petch para Refinamiento de Grano: σy = σ0 + ky·d^(-1/2)
    ├── Maclas de Deformación y Recocido, Fallas de Apilamiento (ABCABABC) y Superficies Libres
    └── Polimorfismo y Alotropía: Carbono (Diamante vs Grafito), Circonia (ZrO2) y Alotropía del Hierro (α-Fe → γ-Fe → δ-Fe)
```

---

## 📐 2. Relaciones Matemáticas Fundamentales

### 1. Parámetros de Red y Geometría Atómica:
* **BCC:** $a = \frac{4R}{\sqrt{3}}, \quad n = 2, \quad \text{NC} = 8, \quad \text{APF} = \frac{\pi\sqrt{3}}{8} \approx 0.6802$
* **FCC:** $a = 2\sqrt{2}R, \quad n = 4, \quad \text{NC} = 12, \quad \text{APF} = \frac{\pi\sqrt{2}}{6} \approx 0.7405$
* **HCP:** $a = 2R, \quad c = a\sqrt{\frac{8}{3}} \approx 1.633 a, \quad n = 6, \quad \text{NC} = 12, \quad \text{APF} = 0.7405$

### 2. Huecos Intersticiales y Radios Críticos:
* **FCC:** $N_{\text{tet}} = 8$ a $\frac{a\sqrt{3}}{4}$ con $r_{\text{tet}} = (\sqrt{3/2}-1)r \approx 0.225r$; $N_{\text{oct}} = 4$ con $r_{\text{oct}} = (\sqrt{2}-1)r \approx 0.414r$.
* **BCC:** $N_{\text{tet}} = 12$ en caras con $r_{\text{tet}} = (\sqrt{5/3}-1)r \approx 0.291r$; $N_{\text{oct}} = 6$ en centros de caras y aristas con $r_{\text{oct}} = (\frac{2}{\sqrt{3}}-1)r \approx 0.155r$.

### 3. Densidades Cristalográficas:
* **Volumétrica:** $\rho_v = \frac{n \cdot M}{V_C \cdot N_A}$
* **Lineal:** $\rho_l = \frac{N_{\text{átomos centrados}}}{L_{[uvw]}}$
* **Planar:** $\rho_p = \frac{N_{\text{átomos plano}}}{A_{(hkl)}}$
* **Relación con espaciado:** $\rho_v = \frac{\rho_p(hkl)}{d_{hkl}}$

### 4. Espaciado Interplanar y Ley de Bragg:
* **Cúbica:** $d_{hkl} = \frac{a}{\sqrt{h^2+k^2+l^2}}$
* **Ortorrómbica:** $\frac{1}{d_{hkl}^2} = \frac{h^2}{a^2} + \frac{k^2}{b^2} + \frac{l^2}{c^2}$
* **Ley de Bragg:** $\lambda = 2d_{hkl}\sin\theta$

### 5. Termodinámica de Defectos y Deslizamiento:
* **Vacantes térmicas en metales:** $\frac{n_v}{N} = \exp\left(-\frac{\Delta H_v}{RT}\right), \quad N = \frac{\rho N_A}{M}$
* **Defectos de Schottky (Iónicos):** $n_s = N \exp\left(-\frac{\Delta H_s}{2RT}\right)$
* **Defectos de Frenkel (Iónicos):** $n_F = \sqrt{N N_i} \exp\left(-\frac{\Delta H_F}{2RT}\right)$
* **Energía elástica de dislocación:** $E \propto |\vec{b}|^2$
* **Ecuación de Hall-Petch:** $\sigma_y = \sigma_0 + k_y \cdot d^{-1/2}$

---

## 📚 3. Índice de Notas Conceptuales Atómicas

1. `[[Concepto - Sistemas Cristalinos y Redes de Bravais]]` — 7 sistemas cristalinos, 4 tipos de celda (P, I, F, C) y deducción de las 14 redes de Bravais.
2. `[[Concepto - Estructuras Metalicas FCC BCC HCP y Factor de Empaquetamiento]]` — Deducciones de $a(R)$, volúmenes de celda, APF, números de coordinación y secuencias de apilamiento $ABAB\dots$ vs $ABCABC\dots$.
3. `[[Concepto - Huecos Intersticiales Tetraedricos y Octaedricos]]` — Multiplicidad $2n$ y $n$, posiciones espaciales y radios de huecos en FCC, BCC y HCP.
4. `[[Concepto - Notacion de Miller para Direcciones y Planos Cubicos y Hexagonales]]` — Índices $[uvw]$, $(hkl)$, perpendicularidad en cúbicas y sistema Miller-Bravais $(hkil)$ y $[uvtw]$.
5. `[[Concepto - Densidad Volumetrica Lineal y Planar en Redes Cristalinas]]` — Definición física, cálculos paso a paso y relación con el espaciado interplanar.
6. `[[Concepto - Difraccion de Rayos X y Ley de Bragg]]` — Interferencia constructiva, cálculo de espaciados interplanares y caracterización estructural.
7. `[[Concepto - Defectos Puntuales Vacantes Termicas Schottky y Frenkel]]` — Termodinámica estadística ($\Delta G = \Delta H - T\Delta S$), concentraciones de equilibrio y tabla de entalpías.
8. `[[Concepto - Soluciones Solidas Sustitucionales e Intersticiales Reglas de Hume-Rothery]]` — 4 reglas de solubilidad, compensación de carga en cerámicos y orden-desorden a $390^\circ\text{C}$ en Cu-Au.
9. `[[Concepto - Dislocaciones Vector de Burgers y Deslizamiento en Metales]]` — Dislocaciones Taylor, Burgers y mixtas, energía $E \propto |\vec{b}|^2$ y sistemas de deslizamiento en metales.
10. `[[Concepto - Defectos Planares Limites de Grano Maclas y Ecuacion de Hall-Petch]]` — Límites de grano, ecuación de Hall-Petch, maclas, fallas de apilamiento y energía superficial.
11. `[[Concepto - Polimorfismo y Alotropia en Metales y Ceramicos]]` — Carbono (diamante/grafito), $\text{ZrO}_2$ y tenacificación martensítica, transformaciones del hierro ($\alpha \to \gamma \to \delta$).

---

## ✏️ 4. Colección Oficial de los 26 Problemas Resueltos

### Bloque 1: Estructuras Cristalinas e Índices de Miller (`Problems T2_CrystStruct.pdf`)
* `[[Problema - T2-CS01 Indices de Miller y Densidades en FCC]]` — Índices de Miller de planos en figuras I, II, III y densidades lineal, planar y volumétrica en FCC.
* `[[Problema - T2-CS02 Masa Atomica y Densidad de Magnesio FCC]]` — Determinación de la masa atómica $M=24.31\text{ g/mol}$ e identificación de Magnesio en red FCC.
* `[[Problema - T2-CS03 Trazado de Planos Cristalinos en Cubica]]` — Determinación analítica y esquemas de 10 planos de Miller cúbicos con traslaciones de origen.
* `[[Problema - T2-CS04 Densidades Planares y Lineales en Red BCC]]` — Densidades superficiales de $(100), (110), (111)$, densidad lineal en $[100]$ y volumétrica en BCC.
* `[[Problema - T2-CS05 Densidades Planares Lineales y Masa de Barra de Aluminio]]` — Densidades en Al FCC y masa de barra cilíndrica de $\varnothing 20\text{ mm} \times 1\text{ m}$ ($m = 855\text{ g}$).
* `[[Problema - T2-CS06 Densidades Lineales y Planares en Direccion 111 de Fe y Ni]]` — Análisis comparativo de densidad lineal $[111]$ y planar $(111)$ en Hierro BCC vs Níquel FCC.
* `[[Problema - T2-CS07 Celda Ortorrombica y Densidades de Material Hipotetico]]` — Deducción de celda ortorrómbica centrada en las caras, masa molar de Plata y densidades planares.
* `[[Problema - T2-CS08 Fraccion de Empaquetamiento Planar en Planos FCC]]` — Cálculo de la fracción de área atómica en planos $(111), (200), (220), (222), (400), (420)$ en FCC.
* `[[Problema - T2-CS09 Cambio Volumetrico en Transformacion Polimorfica BCC a FCC]]` — Cálculo del salto volumétrico del $+5.7\%$ a partir de $d_{321}$ en BCC y $\rho_{(002)}$ en FCC a $910^\circ\text{C}$.
* `[[Problema - T2-CS10 Identificacion de Galio en Celda Ortorrombica y Direcciones Compactas]]` — Celda ortorrómbica centrada en bases, identificación de Galio ($M=69.76\text{ g/mol}$) y direcciones densas.
* `[[Problema - T2-CS11 Parametro de Red y Densidades en Aluminio desde Densidad Lineal]]` — Obtención de $a=4.04\text{ \AA}$ a partir de $\rho_{[111]}$ y cálculo de densidades volumétrica y planar.
* `[[Problema - T2-CS12 Trazado de Direcciones Vectoriales en Celdas Cubicas]]` — Representación vectorial de 12 direcciones cristalográficas cúbicas con traslaciones de origen.
* `[[Problema - T2-CS13 Caracterizacion de Metal Ortorrombico Plano 220 y Direccion 101]]` — Red ortorrómbica centrada en las caras, APF, distancias interplanares y masa de un monocristal de $1\text{ cm}^3$.
* `[[Problema - T2-CS14 Difraccion XRD y Espaciados Interplanares en Fe BCC y FCC]]` — Espaciados $d_{020}$ y distancias entre planos más compactos de Ferrita BCC y Austenita FCC.

### Bloque 2: Defectos Cristalinos y Soluciones Sólidas (`Problems T2 defects.pdf`)
* `[[Problema - T2-DEF01 Fraccion de Vacantes en Aluminio cerca de Fusion]]` — Cálculo de la fracción de vacantes en Al a $660^\circ\text{C}$ ($n_v/N = 4.53 \times 10^{-4}$) desde datos a $400^\circ\text{C}$.
* `[[Problema - T2-DEF02 Concentracion de Equilibrio de Defectos Schottky y Frenkel]]` — Concentración de defectos de Schottky ($3.03 \times 10^{-3}$) y Frenkel ($8.39 \times 10^{-11}$) a $1000\text{ K}$.
* `[[Problema - T2-DEF03 Vacantes Cationicas en MgO por Disolucion de Al2O3 y TiO2]]` — Cuantificación de vacantes catiónicas por neutralidad de carga tras disolver $\text{Al}_2\text{O}_3$ y $\text{TiO}_2$ en $\text{MgO}$.
* `[[Problema - T2-DEF04 Ordenamiento de Solubilidad en Hierro por Reglas de Hume-Rothery]]` — Justificación rigurosa del orden de solubilidad en Hierro: $\text{Mo} > \text{Ni} > \text{Mn}$.
* `[[Problema - T2-DEF05 Defectos de No Estequiometria y Disminucion de Densidad en FeO]]` — Cálculo de vacantes catiónicas ($0.033\text{ mol/mol}$) y disminución de densidad ($-2.56\%$) en $\text{FeO}$ no estequiométrico.
* `[[Problema - T2-DEF06 Magnitud del Vector de Burgers en Alfa-Fe y Al]]` — Deducción analítica de $|\vec{b}|$ para $\alpha\text{-Fe}$ (BCC: $\frac{a\sqrt{3}}{2}$) y Aluminio (FCC: $\frac{a}{\sqrt{2}}$).
* `[[Problema - T2-DEF07 Demostracion de Energia de Dislocaciones en FCC Direcciones 100 vs 110]]` — Demostración teórica formal de la relación de energías elásticas $E_1/E_2 = 2$.
* `[[Problema - T2-DEF08 Determinacion del Vector de Burgers de Dislocacion de Borde en FCC]]` — Determinación de magnitud ($2.553 \times 10^{-10}\text{ m}$) y dirección $[\bar{1}10]$ en plano $(110)$.
* `[[Problema - T2-DEF09 Espaciado Interplanar y Modulo de Burgers en Sistema de Deslizamiento de Tantalo]]` — Análisis del sistema real $(110)[1\bar{1}1]$ vs hipotético $(111)[1\bar{1}0]$ en Tántalo BCC ($a=3.3026\text{ \AA}$).
* `[[Problema - T2-DEF10 Solucion Solida MgO Al2O3 Vacantes y Variacion de Densidad]]` — Cálculo de $0.088\text{ vacantes/átomo Mg}$ y variación porcentual de densidad de $-3\%$ para proporción 15:85.
* `[[Problema - T2-DEF11 Concentracion de Vacantes en Cobre Proximo a Fusion]]` — Cálculo de vacantes por centímetro cúbico en Cobre a $1080^\circ\text{C}$ ($4.98 \times 10^{19}\text{ vacantes/cm}^3$).
* `[[Problema - T2-DEF12 Fraccion de Puntos de Red Vacantes en Paladio FCC]]` — Fracción de puntos vacantes ($0.00204$) y vacantes por $\text{cm}^3$ ($1.39 \times 10^{20}$) en Paladio FCC.

---
*Retorno:* `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|⬅️ Volver a Materiales Aeroespaciales I MOC]]` | `[[00 - Indice Central/Indice Maestro|🗺️ Índice Maestro]]`
