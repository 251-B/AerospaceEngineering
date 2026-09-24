---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 7"
dificultad: alta
tags:
  - problema-oficial
  - resuelto
  - orthorhombic
  - face-centered-orthorhombic
  - planar-density
  - silver
---

# ✏️ Problema: T2-CS07 — Celda Ortorrómbica y Densidades de un Material Hipotético

## 📄 Enunciado Oficial
> **7. The figure below shows the crystallographic directions of a hypothetical material with orthogonal structure.**  
> **$[010] = 5\text{ \AA}$, $[110] = 6.4\text{ \AA}$, $[101] = 7.21\text{ \AA}$**  
> *(The figure illustrates that atoms are in contact along $[110]$ and $[101]$, containing 2 atoms in the segment, while $[010]$ contains 1 atom).*  
> **a)** Draw the unit cell. To which crystalline lattice does it belong?  
> **b)** Calculate the atomic weight given that the density is $5.97\text{ g/cm}^3$.  
> **c)** Calculate the planar density in $\text{atoms/mm}^2$ in the planes $(100)$ and $(110)$, and compare them with each other.  
> *(Solution: a) face centered orthorhombic lattice; b) $M = 107.87\text{ g/mol}$; c) $\rho_{(100)} = 6.66 \times 10^{12}\text{ at/mm}^2$; $\rho_{(110)} = 5.2 \times 10^{12}\text{ at/mm}^2$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Datos de Entrada:
* Estructura ortogonal: $\alpha = \beta = \gamma = 90^\circ$.
* Longitudes dadas:
  * $L_{[010]} = b = 5\text{ \AA} = 5.0 \times 10^{-8}\text{ cm}$.
  * $L_{[110]} = \sqrt{a^2 + b^2} = 6.4\text{ \AA}$.
  * $L_{[101]} = \sqrt{a^2 + c^2} = 7.21\text{ \AA}$.
* Densidad volumétrica: $\rho = 5.97\text{ g/cm}^3$.
* Número de Avogadro: $N_A = 6.022 \times 10^{23}\text{ átomos/mol}$.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

1. **Determinación de los Parámetros de Red ($a, b, c$):**
   Conociendo la métrica ortogonal $L_{[uvw]} = \sqrt{(ua)^2 + (vb)^2 + (wc)^2}$, se despejan sucesivamente $a$ y $c$.
2. **Identificación de la Red de Bravais [Session 3 Slides 9, 12]:**
   Si las diagonales de cara $[110]$ y $[101]$ son direcciones de contacto atómico continuo con átomos en sus puntos medios, la celda presenta átomos centrados en todas las caras $\implies$ **Red Ortorrómbica Centrada en las Caras ($F$)** con $n = 4$ átomos equivalentes.
3. **Masa Atómica Molar:**
   $$M = \frac{\rho \cdot (a \cdot b \cdot c) \cdot N_A}{n}$$
4. **Densidades Planares:**
   $$\rho_{(100)} = \frac{N_{\text{átomos}(100)}}{b \cdot c}, \quad \rho_{(110)} = \frac{N_{\text{átomos}(110)}}{\sqrt{a^2 + b^2} \cdot c}$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Apartado a: Deducción de Parámetros y Tipo de Red
* A partir de $L_{[110]}$ y $b = 5.0\text{ \AA}$:
  $$a^2 + b^2 = 6.4^2 \implies a^2 + 5.0^2 = 40.96 \implies a^2 = 40.96 - 25 = 15.96\text{ \AA}^2$$
  $$a = \sqrt{15.96} \approx 3.995\text{ \AA} \approx \mathbf{4.0\text{ \AA}}$$
* A partir de $L_{[101]}$ y $a^2 = 15.96$:
  $$a^2 + c^2 = 7.21^2 \implies 15.96 + c^2 = 51.984 \implies c^2 = 51.984 - 15.96 = 36.024\text{ \AA}^2$$
  $$c = \sqrt{36.024} \approx \mathbf{6.0\text{ \AA}}$$
* Como $a \neq b \neq c$ ($a \approx 4.0\text{ \AA}$, $b = 5.0\text{ \AA}$, $c = 6.0\text{ \AA}$) y los tres ángulos son de $90^\circ$, el sistema es **Ortorrómbico**.
* Como existen átomos en los centros de todas las caras por donde pasan las direcciones compactas, pertenece a la **red ortorrómbica centrada en las caras (Face-Centered Orthorhombic, $F$)** con $n = 4$ átomos/celda.

---

### 2. Apartado b: Cálculo del Peso Atómico ($M$)
* **Volumen de la celda unitaria:**
  $$V_C = a \cdot b \cdot c = (3.995 \times 10^{-8}\text{ cm}) \times (5.0 \times 10^{-8}\text{ cm}) \times (6.0 \times 10^{-8}\text{ cm}) = 1.1985 \times 10^{-22}\text{ cm}^3$$
* **Masa atómica molar:**
  $$M = \frac{\rho \cdot V_C \cdot N_A}{n} = \frac{(5.97\text{ g/cm}^3) \times (1.1985 \times 10^{-22}\text{ cm}^3) \times (6.022 \times 10^{23}\text{ mol}^{-1})}{4}$$
  $$M = \frac{7.155 \times 10^{-22} \times 6.022 \times 10^{23}}{4} = \frac{430.87}{4} = \mathbf{107.72\text{ g/mol}} \approx \mathbf{107.87\text{ g/mol}}$$
  *(Corresponde a la Plata, $\text{Ag}$, con $M_{\text{tabulada}} = 107.868\text{ g/mol}$).*

---

### 3. Apartado c: Cálculo de las Densidades Planares

1. **Plano $(100)$:**
   * Es la cara delimitada por las aristas $b$ y $c$.
   * Dimensiones: $b = 5.0\text{ \AA} = 5.0 \times 10^{-7}\text{ mm}$; $c = 6.0\text{ \AA} = 6.0 \times 10^{-7}\text{ mm}$.
   * Área: $A_{(100)} = b \cdot c = 30.0\text{ \AA}^2 = 3.0 \times 10^{-13}\text{ mm}^2$.
   * Átomos contenidos en la cara centrada: 4 vértices $\times \frac{1}{4} + 1\text{ centro de cara} = 2\text{ átomos}$.
   $$\rho_{(100)} = \frac{2\text{ at}}{3.0 \times 10^{-13}\text{ mm}^2} = \mathbf{6.66 \times 10^{12}\text{ at/mm}^2}$$

2. **Plano $(110)$:**
   * Plano rectangular diagonal de base $L_{[110]} = 6.4\text{ \AA} = 6.4 \times 10^{-7}\text{ mm}$ y altura $c = 6.0\text{ \AA} = 6.0 \times 10^{-7}\text{ mm}$.
   * Área: $A_{(110)} = 6.4 \times 6.0 = 38.4\text{ \AA}^2 = 3.84 \times 10^{-13}\text{ mm}^2$.
   * Átomos contenidos: 4 vértices $\times \frac{1}{4} + 2\text{ centros en aristas de base} \times \frac{1}{2} = 1 + 1 = 2\text{ átomos}$.
   $$\rho_{(110)} = \frac{2\text{ at}}{3.84 \times 10^{-13}\text{ mm}^2} = \mathbf{5.21 \times 10^{12}\text{ at/mm}^2}$$

3. **Comparación:**
   $$\rho_{(100)} = 6.66 \times 10^{12}\text{ at/mm}^2 > \rho_{(110)} = 5.21 \times 10^{12}\text{ at/mm}^2$$
   El plano $(100)$ tiene un **$28\%$ mayor densidad atómica** que el plano $(110)$.

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

* **Geometría Anisótropa:** A diferencia del sistema cúbico donde $\{100\}$ tiene menor densidad que $\{110\}$, en este cristal ortorrómbico con $a < b < c$, el plano $(100)$ posee una superficie pequeña ($bc = 30\text{ \AA}^2$) conteniendo 2 átomos, resultando más denso que el plano $(110)$ de mayor superficie ($38.4\text{ \AA}^2$), demostrando la fuerte anisotropía de las redes ortorrómbicas.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
