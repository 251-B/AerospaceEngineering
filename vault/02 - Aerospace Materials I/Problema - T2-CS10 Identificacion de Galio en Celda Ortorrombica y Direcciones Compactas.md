---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 10"
dificultad: alta
tags:
  - problema-oficial
  - resuelto
  - gallium
  - base-centered-orthorhombic
  - close-packed-directions
  - close-packed-planes
---

# ✏️ Problema: T2-CS10 — Identificación de Galio en Celda Ortorrómbica y Direcciones Compactas

## 📄 Enunciado Oficial
> **10. Three distinct crystallographic planes in the unit cell of a hypothetic metal are shown below. The circles represent atoms.**  
> * **Plane $(110)$:** Rectangle with dimensions $4.88\text{ \AA}$ (diagonal) and $3.32\text{ \AA}$ (vertical edge). Atoms at the 4 corners and 2 in the center of the base edges.
> * **Plane $(101)$:** Rectangle with dimensions $4.64\text{ \AA}$ and $3.65\text{ \AA}$. Atoms only at the 4 corners.
> * **Plane $(020)$:** Rectangle with dimensions $3.24\text{ \AA}$ and $3.32\text{ \AA}$. Atoms at the 4 corners.
> 
> **a)** To which crystalline structure does this unit cell belong?  
> **b)** Given that the density of this metal is $5.9\text{ g/cm}^3$, determine the atomic mass. Which specific metal is it referred to?  
> **c)** Identify the directions and planes of maximum packing.  
> *(Solution: a) Base centered orthorhombic lattice; b) $M = 69.76\text{ g/mol}$, Gallium; c) $[110], [\bar{1}10], [\bar{1}\bar{1}0], [1\bar{1}0], (001)$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Datos de Entrada:
* Dimensiones extraídas de los planos:
  * Del plano $(020)$: arista $a = 3.24\text{ \AA}$, arista $c = 3.32\text{ \AA}$.
  * Del plano $(110)$: arista vertical $c = 3.32\text{ \AA}$, diagonal de base $\sqrt{a^2 + b^2} = 4.88\text{ \AA}$.
  * Del plano $(101)$: diagonal $\sqrt{a^2 + c^2} = \sqrt{3.24^2 + 3.32^2} = \sqrt{10.50 + 11.02} = \sqrt{21.52} \approx 4.64\text{ \AA}$, y arista $b = 3.65\text{ \AA}$.
* Densidad volumétrica: $\rho = 5.9\text{ g/cm}^3$.
* Número de Avogadro: $N_A = 6.022 \times 10^{23}\text{ átomos/mol}$.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

1. **Parámetros de Red ($a, b, c$):**
   * $a = 3.24\text{ \AA}$
   * $b = 3.65\text{ \AA}$ (verificación: $\sqrt{3.24^2 + 3.65^2} = \sqrt{10.50 + 13.32} = \sqrt{23.82} = 4.88\text{ \AA}$, coincidencia exacta).
   * $c = 3.32\text{ \AA}$
   * Como $a \neq b \neq c$ y los planos forman ángulos de $90^\circ$, el sistema es **Ortorrómbico** [Session 3 Slide 12].
2. **Tipo de Centrado de Celda (Bravais) [Session 3 Slide 9, 12]:**
   El plano $(110)$ contiene átomos en el centro de las aristas inferior y superior de base, lo que revela que la cara basal $(001)$ tiene un átomo centrado. Por el contrario, los planos $(101)$ y $(020)$ no contienen átomos centrados en sus caras. Por tanto, únicamente las dos bases $(001)$ están centradas $\implies$ **Red Ortorrómbica Centrada en las Bases (Base-Centered Orthorhombic, $C$)**.
3. **Número de Átomos por Celda:**
   $$n = 8 \times \left(\frac{1}{8}\right)_{\text{vértices}} + 2 \times \left(\frac{1}{2}\right)_{\text{bases}} = 1 + 1 = 2\text{ átomos/celda}$$
4. **Masa Atómica Molar:**
   $$M = \frac{\rho \cdot (a \cdot b \cdot c) \cdot N_A}{n}$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Apartado a: Identificación de la Red Cristalina
* Aristas: $a = 3.24\text{ \AA}$, $b = 3.65\text{ \AA}$, $c = 3.32\text{ \AA}$ ($a \neq b \neq c$).
* Ángulos: $\alpha = \beta = \gamma = 90^\circ$.
* Disposición de átomos: Átomos en los 8 vértices y en los baricentros de las dos caras basales opuestas $z=0$ y $z=c$.
* Estructura: **Red Ortorrómbica Centrada en las Bases (Base-centered Orthorhombic)**.

---

### 2. Apartado b: Cálculo de la Masa Atómica e Identificación
* **Volumen de la celda unitaria:**
  $$V_C = a \cdot b \cdot c = (3.24 \times 10^{-8}\text{ cm}) \times (3.65 \times 10^{-8}\text{ cm}) \times (3.32 \times 10^{-8}\text{ cm}) = 3.926 \times 10^{-23}\text{ cm}^3$$
* **Masa atómica ($M$):**
  $$M = \frac{\rho \cdot V_C \cdot N_A}{n} = \frac{(5.9\text{ g/cm}^3) \times (3.926 \times 10^{-23}\text{ cm}^3) \times (6.022 \times 10^{23}\text{ mol}^{-1})}{2}$$
  $$M = \frac{2.3163 \times 10^{-22} \times 6.022 \times 10^{23}}{2} = \frac{139.49}{2} = \mathbf{69.745\text{ g/mol}} \approx \mathbf{69.76\text{ g/mol}}$$
* **Identificación del Metal:**
  El elemento químico con masa molar de $69.72\text{--}69.76\text{ g/mol}$ y densidad $\approx 5.9\text{ g/cm}^3$ es el **Galio ($\text{Ga}$)**.

---

### 3. Apartado c: Direcciones y Planos de Máximo Empaquetamiento
* **Plano de Máximo Empaquetamiento:**
  * En la celda ortorrómbica centrada en bases, la cara basal $(001)$ contiene el átomo centrado y los 4 de los vértices en un área $a \cdot b = 3.24 \times 3.65 = 11.83\text{ \AA}^2$.
  * Densidad planar de $(001)$: $\rho_{(001)} = \frac{2}{11.83 \times 10^{-16}\text{ cm}^2} = 1.69 \times 10^{15}\text{ at/cm}^2$.
  * Por tanto, el plano más compacto es el **$(001)$** (o plano basal).
* **Direcciones de Máximo Empaquetamiento:**
  * En el plano $(001)$, los átomos de los vértices y el átomo central están alineados en las diagonales de la cara basal:
    $$\mathbf{[110], \quad [\bar{1}10], \quad [\bar{1}\bar{1}0], \quad [1\bar{1}0]}$$
  * En estas 4 direcciones diagonales coplanares, los átomos están en contacto mutuo continuo.

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

* **Física del Galio:** El Galio puro es un elemento sumamente singular en ciencia de materiales aeroespaciales y optoelectrónica ($\text{GaAs}, \text{GaN}$). Posee una temperatura de fusión sumamente baja ($T_m = 29.76^\circ\text{C}$), fundiéndose con el calor de la mano humana, y cristaliza a temperatura ambiente en una red ortorrómbica ligeramente distorsionada donde los átomos forman dímeros casi moleculares $\text{Ga}_2$ orientados a lo largo de las direcciones densas del plano $(001)$.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
