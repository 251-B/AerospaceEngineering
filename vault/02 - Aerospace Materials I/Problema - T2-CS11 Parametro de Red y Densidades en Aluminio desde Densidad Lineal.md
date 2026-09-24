---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 11"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - aluminum
  - fcc
  - linear-density
  - lattice-parameter
  - planar-density
---

# ✏️ Problema: T2-CS11 — Parámetro de Red y Densidades en Aluminio desde Densidad Lineal

## 📄 Enunciado Oficial
> **11. Aluminum has an FCC structure with atomic weight of $26.98\text{ g/mol}$. Given that its linear density in the direction $[111]$ is $1.43 \times 10^7\text{ at/cm}$, determine:**  
> **a)** The lattice parameter and the atomic radius for aluminum. *(Solution: $a = 4.04\text{ \AA}$, $r = 1.43\text{ \AA}$)*  
> **b)** Volume density in $(\text{g/cm}^3)$ and planar density in the plane $(101)$ in $(\text{at/cm}^2)$. *(Solution: $\rho = 2.71\text{ g/cm}^3$; $\rho_{(101)} = 8.66 \times 10^{14}\text{ at/cm}^2$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Datos de Entrada:
* Elemento: Aluminio puro ($\text{Al}$).
* Estructura: Cúbica Centrada en las Caras (FCC) $\implies n = 4\text{ átomos/celda}$.
* Masa atómica molar: $M = 26.98\text{ g/mol}$.
* Densidad lineal en la dirección $[111]$: $\rho_{[111]} = 1.43 \times 10^7\text{ at/cm}$.
* Número de Avogadro: $N_A = 6.022 \times 10^{23}\text{ átomos/mol}$.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

1. **Densidad Lineal en $[111]$ para FCC [Session 4 Slide 7]:**
   En una celda FCC, la diagonal principal $[111]$ tiene una longitud $L_{[111]} = a\sqrt{3}$. Atraviesa únicamente dos átomos situados en los vértices extremos opuestos, cada uno aportando $\frac{1}{2}$ átomo centrado:
   $$N_{\text{átomos}} = 2 \times \frac{1}{2} = 1\text{ átomo}$$
   $$\rho_{[111]} = \frac{1}{a\sqrt{3}} \implies a = \frac{1}{\sqrt{3} \cdot \rho_{[111]}}$$
2. **Radio Atómico en FCC [Session 3 Slide 20]:**
   $$4R = a\sqrt{2} \implies R = \frac{a\sqrt{2}}{4}$$
3. **Densidad Volumétrica ($\rho_v$):**
   $$\rho_v = \frac{n \cdot M}{a^3 \cdot N_A} = \frac{4 \cdot M}{a^3 \cdot N_A}$$
4. **Densidad Planar en el Plano $(101)$ [Session 4 Slide 8]:**
   En el sistema cúbico, el plano $(101)$ es cristalográficamente equivalente a $(110) \in \{110\}$.
   El plano $(101)$ corta la diagonal de la cara $x-z$ (longitud $a\sqrt{2}$) y la arista $y$ (longitud $a$).
   Área: $A_{(101)} = a\sqrt{2} \times a = a^2\sqrt{2}$.
   Átomos contenidos: $N_{\text{átomos}} = 4 \times \frac{1}{4} + 2 \times \frac{1}{2} = 2\text{ átomos}$.
   $$\rho_{(101)} = \frac{2}{\sqrt{2}a^2} = \frac{\sqrt{2}}{a^2}$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Apartado a: Parámetro de Red y Radio Atómico
* **Cálculo de $a$:**
  $$a = \frac{1}{\sqrt{3} \times (1.43 \times 10^7\text{ at/cm})} = \frac{1}{1.73205 \times 1.43 \times 10^7\text{ cm}^{-1}} = \frac{1}{2.4768 \times 10^7\text{ cm}^{-1}}$$
  $$a = 4.0374 \times 10^{-8}\text{ cm} \approx \mathbf{4.04\text{ \AA}}$$
* **Cálculo de $R$:**
  $$R = \frac{a\sqrt{2}}{4} = \frac{(4.0374 \times 10^{-8}\text{ cm}) \times 1.4142136}{4} = 1.4274 \times 10^{-8}\text{ cm} \approx \mathbf{1.43\text{ \AA}}$$

---

### 2. Apartado b: Densidad Volumétrica y Planar
* **Densidad Volumétrica ($\rho_v$):**
  $$V_C = a^3 = (4.0374 \times 10^{-8}\text{ cm})^3 = 6.5813 \times 10^{-23}\text{ cm}^3$$
  $$\rho_v = \frac{4 \times 26.98\text{ g/mol}}{(6.5813 \times 10^{-23}\text{ cm}^3) \times (6.022 \times 10^{23}\text{ mol}^{-1})} = \frac{107.92}{39.633} = \mathbf{2.72\text{ g/cm}^3} \approx \mathbf{2.71\text{ g/cm}^3}$$

* **Densidad Planar en el Plano $(101)$:**
  $$a^2 = (4.0374 \times 10^{-8}\text{ cm})^2 = 1.63006 \times 10^{-15}\text{ cm}^2$$
  $$\rho_{(101)} = \frac{\sqrt{2}}{a^2} = \frac{1.4142136}{1.63006 \times 10^{-15}\text{ cm}^2} = 8.6758 \times 10^{14} \approx \mathbf{8.66 \times 10^{14}\text{ at/cm}^2}$$

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

* **Validación Cruzada de Métodos:** En el problema T2-CS05 se obtuvo la densidad planar a partir del radio atómico conocido $R = 1.43\text{ \AA}$. Aquí, el procedimiento es inverso: midiendo la densidad lineal $\rho_{[111]}$ (accesible mediante microscopía electrónica de transmisión de alta resolución o difracción), se deriva con exactitud idéntica el parámetro reticular ($4.04\text{ \AA}$), el radio atómico ($1.43\text{ \AA}$), la densidad del sólido ($2.71\text{ g/cm}^3$) y la densidad planar de los planos de cizalladura.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
