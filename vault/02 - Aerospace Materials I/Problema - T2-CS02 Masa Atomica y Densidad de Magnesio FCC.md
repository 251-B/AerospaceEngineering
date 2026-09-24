---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 2"
dificultad: baja
tags:
  - problema-oficial
  - resuelto
  - atomic-mass
  - density
  - fcc
  - magnesium
---

# ✏️ Problema: T2-CS02 — Masa Atómica y Densidad de Magnesio FCC

## 📄 Enunciado Oficial
> **2. Determine the atomic mass of a metal element with FCC structure, density of $1.74\text{ g/cm}^3$ and lattice constant of $4.527\text{ \AA}$. Find the element with these characteristics.**  
> *(Solution: $M = 24.3\text{ g/mol}$; $\text{Mg}$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Datos de Entrada:
* Estructura cristalina: Cúbica Centrada en las Caras (FCC) $\implies n = 4\text{ átomos/celda}$.
* Parámetro de red: $a = 4.527\text{ \AA} = 4.527 \times 10^{-8}\text{ cm} = 0.4527\text{ nm}$.
* Densidad volumétrica macroscópica: $\rho = 1.74\text{ g/cm}^3 = 1740\text{ kg/m}^3$.
* Constante de Avogadro: $N_A = 6.022 \times 10^{23}\text{ átomos/mol}$.

### Hipótesis de Partida:
1. El metal es un monocristal puro libre de vacantes o defectos que alteren significativamente la densidad aparente.
2. La celda unitaria cúbica satisface $V_C = a^3$.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

Citando los fundamentos teóricos del curso [Session 4 Slide 7, 15]:
* La densidad volumétrica teórica de un sólido cristalino se define por la razón entre la masa de la celda y su volumen:
  $$\rho = \frac{m_{\text{celda}}}{V_C} = \frac{n \cdot M}{a^3 \cdot N_A}$$
* Despejando algebraicamente la masa atómica molar $M$:
  $$M = \frac{\rho \cdot a^3 \cdot N_A}{n}$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

1. **Cálculo del volumen de la celda unitaria ($V_C$):**
   $$a = 4.527 \times 10^{-8}\text{ cm}$$
   $$V_C = a^3 = (4.527 \times 10^{-8}\text{ cm})^3 = 9.2778 \times 10^{-23}\text{ cm}^3$$

2. **Cálculo de la masa molar ($M$):**
   $$M = \frac{(1.74\text{ g/cm}^3) \times (9.2778 \times 10^{-23}\text{ cm}^3) \times (6.02214 \times 10^{23}\text{ mol}^{-1})}{4}$$
   $$M = \frac{1.6143 \times 10^{-22} \times 6.02214 \times 10^{23}}{4} = \frac{97.218}{4} = \mathbf{24.305\text{ g/mol}}$$

3. **Identificación en la Tabla Periódica:**
   Consultando los pesos atómicos estándar de los elementos:
   * Sodio ($\text{Na}$): $22.99\text{ g/mol}$
   * **Magnesio ($\text{Mg}$):** $24.305\text{ g/mol}$ (coincidencia exacta).
   * Aluminio ($\text{Al}$): $26.98\text{ g/mol}$

   Por tanto, el elemento con estas características físicas y masa atómica es el **Magnesio ($\text{Mg}$)**.

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

* **Análisis Cristalográfico:** A temperatura y presión ambiente, el magnesio puro cristaliza habitualmente en la estructura **HCP** ($c/a \approx 1.624$) con densidad $1.738\text{ g/cm}^3$. Sin embargo, en películas delgadas, estados metaestables epitaxiales o como fase polimórfica teórica, puede adoptar la configuración cúbica FCC manteniendo la misma densidad atómica masiva.
* **Consistencia Dimensional:**
  $$[M] = \frac{[\text{g/cm}^3] \cdot [\text{cm}^3] \cdot [\text{mol}^{-1}]}{[\text{adimensional}]} = \text{g/mol} \quad \checkmark$$

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
