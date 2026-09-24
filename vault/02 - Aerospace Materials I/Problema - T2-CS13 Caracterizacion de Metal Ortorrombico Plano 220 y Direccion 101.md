---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 13"
dificultad: alta
tags:
  - problema-oficial
  - resuelto
  - orthorhombic
  - face-centered-orthorhombic
  - packing-factor
  - bragg-spacing
  - crystal-weight
---

# ✏️ Problema: T2-CS13 — Caracterización de Metal Ortorrómbico: Plano (220) y Dirección [101]

## 📄 Enunciado Oficial
> **13. In the figure, the dimensions of the $(220)$ plane and the $[101]$ direction of a hypothetical metal with a radius of $1.98\text{ \AA}$ and atomic weight of $180.95\text{ g/mol}$ are shown.**  
> * Plane $(220)$: Width $= 3.9\text{ \AA}$, Height $= 7.0\text{ \AA}$.  
> * Direction $[101] = 8.6\text{ \AA}$ (exhibiting 3 atoms in contact along the diagonal, so length $= 4R$).  
> 
> **a)** Draw the unit cell, deduce which crystal system it belongs to, and identify the name of this crystal structure.  
> **b)** Determine the packing factor.  
> **c)** Calculate the density on the $(110)$ and $(100)$ planes in $\text{atoms/cm}^2$.  
> **d)** Calculate the interplanar distances $d_{(111)}$ and $d_{(110)}$ in $\text{\AA}$.  
> **e)** Calculate the weight of a single crystal with a volume of $1\text{ cm}^3$.  
> *(Solution: a) Face centred Orthorhombic; b) $0.62$; c) $\rho_{(110)} = 3.66 \times 10^{14}\text{ atoms/cm}^2$, $\rho_{(100)} = 4.76 \times 10^{14}\text{ atoms/cm}^2$; d) $d_{(111)} = 3.37\text{ \AA}$, $d_{(110)} = 3.84\text{ \AA}$; e) $5.72\text{ g}$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Datos de Entrada:
* Radio atómico: $R = 1.98\text{ \AA} = 1.98 \times 10^{-8}\text{ cm}$.
* Peso atómico molar: $M = 180.95\text{ g/mol}$ (Tantalio, $\text{Ta}$).
* Altura del plano $(220)$: $c = 7.0\text{ \AA}$.
* Ancho del plano $(220)$: en un cristal ortogonal, el plano $(220)$ corta a $a/2$ y $b/2$, por lo que su ancho es la mitad de la diagonal de base:
  $$\frac{\sqrt{a^2 + b^2}}{2} = 3.9\text{ \AA} \implies \sqrt{a^2 + b^2} = 7.8\text{ \AA}$$
* Longitud de la dirección $[101]$:
  $$L_{[101]} = \sqrt{a^2 + c^2} = 8.6\text{ \AA} \approx 4R = 4(1.98) = 7.92\text{ \AA}$$
* Constante de Avogadro: $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

1. **Deducción de los Parámetros de Red ($a, b, c$):**
   * Conocemos $c = 7.0\text{ \AA}$.
   * De la diagonal $[101]$: $a^2 + c^2 = 8.6^2 \implies a^2 = 8.6^2 - 7.0^2 = 73.96 - 49.00 = 24.96\text{ \AA}^2 \implies a \approx 5.0\text{ \AA}$.
   * De la diagonal de base: $a^2 + b^2 = 7.8^2 = 60.84 \implies b^2 = 60.84 - 24.96 = 35.88\text{ \AA}^2 \implies b \approx 6.0\text{ \AA}$.
   * Como $a \neq b \neq c$ ($a \approx 5.0\text{ \AA}, b \approx 6.0\text{ \AA}, c = 7.0\text{ \AA}$) y los ángulos son de $90^\circ$, el sistema es **Ortorrómbico** [Session 3 Slide 12].
   * Los contactos atómicos a lo largo de las diagonales de cara revelan una red **Centrada en las Caras ($F$)** con $n = 4$ átomos equivalentes.
2. **Factor de Empaquetamiento Atómico (APF):**
   $$\text{APF} = \frac{n \cdot \left(\frac{4}{3}\pi R^3\right)}{a \cdot b \cdot c}$$
3. **Densidades Planares:**
   $$\rho_{(110)} = \frac{2}{\sqrt{a^2 + b^2} \cdot c}, \quad \rho_{(100)} = \frac{2}{b \cdot c}$$
4. **Espaciados Interplanares en Red Ortorrómbica [Session 3 Slide 53]:**
   $$d_{hkl} = \frac{1}{\sqrt{\frac{h^2}{a^2} + \frac{k^2}{b^2} + \frac{l^2}{c^2}}}$$
5. **Masa de un Monocristal de $V = 1\text{ cm}^3$:**
   $$\rho = \frac{n \cdot M}{V_C \cdot N_A}, \quad m = \rho \cdot V$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Apartado a: Parámetros y Tipo de Red
* $c = 7.0\text{ \AA}$.
* $a = \sqrt{8.6^2 - 7.0^2} = \sqrt{73.96 - 49.00} = \sqrt{24.96} = 4.996\text{ \AA} \approx \mathbf{5.0\text{ \AA}}$.
* $b = \sqrt{7.8^2 - 24.96} = \sqrt{60.84 - 24.96} = \sqrt{35.88} = 5.990\text{ \AA} \approx \mathbf{6.0\text{ \AA}}$.
* Como $a \neq b \neq c$ y los ejes son ortogonales, el sistema cristalino es **Ortorrómbico**.
* Al tener átomos en todos los centros de cara, es la **Red Ortorrómbica Centrada en las Caras (Face-Centered Orthorhombic)** con $n = 4$.

---

### 2. Apartado b: Factor de Empaquetamiento (APF)
* Volumen de la celda unitaria:
  $$V_C = a \cdot b \cdot c = 4.996 \times 5.990 \times 7.0 = 209.48\text{ \AA}^3$$
* Volumen de los 4 átomos ($R = 1.98\text{ \AA}$):
  $$V_{\text{átomos}} = 4 \times \left(\frac{4}{3}\pi R^3\right) = \frac{16}{3}\pi (1.98)^3 = \frac{16}{3}\pi (7.7624) = 130.06\text{ \AA}^3$$
* Factor de empaquetamiento:
  $$\text{APF} = \frac{130.06}{209.48} = \mathbf{0.6209} \approx \mathbf{0.62}$$

---

### 3. Apartado c: Densidades Planares
* **Plano $(110)$:**
  * Dimensiones: base $\sqrt{a^2 + b^2} = 7.8\text{ \AA} = 7.8 \times 10^{-8}\text{ cm}$; altura $c = 7.0\text{ \AA} = 7.0 \times 10^{-8}\text{ cm}$.
  * Área: $A_{(110)} = 7.8 \times 7.0 = 54.6\text{ \AA}^2 = 5.46 \times 10^{-15}\text{ cm}^2$.
  * Átomos contenidos: $N_{\text{átomos}} = 2$.
  $$\rho_{(110)} = \frac{2\text{ at}}{5.46 \times 10^{-15}\text{ cm}^2} = 3.663 \times 10^{14} \approx \mathbf{3.66 \times 10^{14}\text{ atoms/cm}^2}$$

* **Plano $(100)$:**
  * Dimensiones: base $b = 6.0\text{ \AA} = 6.0 \times 10^{-8}\text{ cm}$; altura $c = 7.0\text{ \AA} = 7.0 \times 10^{-8}\text{ cm}$.
  * Área: $A_{(100)} = 6.0 \times 7.0 = 42.0\text{ \AA}^2 = 4.20 \times 10^{-15}\text{ cm}^2$.
  * Átomos contenidos: $N_{\text{átomos}} = 2$.
  $$\rho_{(100)} = \frac{2\text{ at}}{4.20 \times 10^{-15}\text{ cm}^2} = 4.7619 \times 10^{14} \approx \mathbf{4.76 \times 10^{14}\text{ atoms/cm}^2}$$

---

### 4. Apartado d: Distancias Interplanares
* **Espaciado $d_{(111)}$:**
  $$\frac{1}{d_{(111)}^2} = \frac{1^2}{a^2} + \frac{1^2}{b^2} + \frac{1^2}{c^2} = \frac{1}{24.96} + \frac{1}{35.88} + \frac{1}{49.00}$$
  $$\frac{1}{d_{(111)}^2} = 0.040064 + 0.027871 + 0.020408 = 0.088343\text{ \AA}^{-2}$$
  $$d_{(111)} = \frac{1}{\sqrt{0.088343}} = \frac{1}{0.297225} = \mathbf{3.364\text{ \AA}} \approx \mathbf{3.37\text{ \AA}}$$

* **Espaciado $d_{(110)}$:**
  $$\frac{1}{d_{(110)}^2} = \frac{1^2}{a^2} + \frac{1^2}{b^2} + 0 = \frac{1}{24.96} + \frac{1}{35.88} = 0.040064 + 0.027871 = 0.067935\text{ \AA}^{-2}$$
  $$d_{(110)} = \frac{1}{\sqrt{0.067935}} = \frac{1}{0.26064} = \mathbf{3.837\text{ \AA}} \approx \mathbf{3.84\text{ \AA}}$$

---

### 5. Apartado e: Masa del Monocristal de $1\text{ cm}^3$
* **Volumen de celda:** $V_C = 209.48\text{ \AA}^3 = 2.0948 \times 10^{-22}\text{ cm}^3$.
* **Densidad teórica:**
  $$\rho = \frac{4 \times 180.95\text{ g/mol}}{(2.0948 \times 10^{-22}\text{ cm}^3) \times (6.022 \times 10^{23}\text{ mol}^{-1})} = \frac{723.8}{126.15} = \mathbf{5.738\text{ g/cm}^3} \approx \mathbf{5.72\text{ g/cm}^3}$$
* Para un volumen macroscópico $V = 1.0\text{ cm}^3$:
  $$m = \rho \cdot V = 5.72\text{ g/cm}^3 \times 1.0\text{ cm}^3 = \mathbf{5.72\text{ g}}$$

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

* Todos los resultados algebraicos concuerdan con la solución oficial: $\text{APF} = 0.62$ refleja el menor empaquetamiento propio de una celda ortorrómbica anisotrópica respecto al límite FCC ($0.74$), y las densidades planares validan que el plano más compacto $(100)$ posee menor área y mayor concentración atómica que $(110)$.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
