---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 12"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - palladium
  - fcc
  - vacant-lattice-points
  - density-deficit
---

# ✏️ Problema: T2-DEF12 — Fracción de Puntos de Red Vacantes en Paladio FCC

## 📄 Enunciado Oficial
> **12. The density of a sample of FCC palladium is $11.98\text{ g/cm}^3$, and its lattice parameter is $3.8902\text{ \AA}$. Calculate:**  
> **a)** The fraction of the lattice points that contain vacancies. *(Solution: $0.00204$)*  
> **b)** The total number of vacancies in a cubic centimeter of $\text{Pd}$. *(Solution: $1.39 \times 10^{20}\text{ vacancies/cm}^3$)*  
> **Data:** $M_{\text{Pd}} = 106.4\text{ g/mol}$; $N_A = 6.022 \times 10^{23}\text{ atoms/mol}$.

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Datos de Entrada:
* Material: Paladio metálico ($\text{Pd}$).
* Estructura cristalina: Cúbica Centrada en las Caras (FCC) $\implies n_{\text{sitios}} = 4\text{ sitios reticulares/celda}$.
* Parámetro reticular medido: $a = 3.8902\text{ \AA} = 3.8902 \times 10^{-8}\text{ cm}$.
* Densidad real medida: $\rho_{\text{real}} = 11.98\text{ g/cm}^3$.
* Masa atómica molar: $M_{\text{Pd}} = 106.4\text{ g/mol}$.
* Número de Avogadro: $N_A = 6.022 \times 10^{23}\text{ átomos/mol}$.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

1. **Densidad Teórica Ideal del Cristal Perfecto ($\rho_{\text{ideal}}$) [Session 4 Slide 7, 15]:**
   Si todos los puntos de la red estuvieran ocupados por átomos de paladio sin vacante alguna:
   $$\rho_{\text{ideal}} = \frac{n \cdot M_{\text{Pd}}}{a^3 \cdot N_A} = \frac{4 \cdot M_{\text{Pd}}}{a^3 \cdot N_A}$$
2. **Fracción de Puntos de Red Vacantes ($f_v$):**
   La existencia de vacantes reduce la masa contenida en la celda sin alterar apreciablemente su parámetro reticular $a$. La fracción de vacantes es el déficit relativo de densidad:
   $$f_v = \frac{\rho_{\text{ideal}} - \rho_{\text{real}}}{\rho_{\text{ideal}}} = 1 - \frac{\rho_{\text{real}}}{\rho_{\text{ideal}}}$$
3. **Número Total de Vacantes por Centímetro Cúbico ($n_v$):**
   La densidad numérica total de puntos de red por centímetro cúbico es:
   $$N = \frac{n_{\text{sitios}}}{V_C} = \frac{4}{a^3}$$
   El número absoluto de vacantes por centímetro cúbico es:
   $$n_v = f_v \cdot N$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Cálculo de la Densidad Ideal Teórica ($\rho_{\text{ideal}}$):
* Volumen de la celda unitaria:
  $$V_C = a^3 = (3.8902 \times 10^{-8}\text{ cm})^3 = 5.88722 \times 10^{-23}\text{ cm}^3$$
* Masa teórica de la celda unitaria perfecta:
  $$m_{\text{celda}} = \frac{4 \times 106.4\text{ g/mol}}{6.022 \times 10^{23}\text{ mol}^{-1}} = \frac{425.6}{6.022 \times 10^{23}} = 7.06742 \times 10^{-22}\text{ g}$$
* Densidad teórica:
  $$\rho_{\text{ideal}} = \frac{7.06742 \times 10^{-22}\text{ g}}{5.88722 \times 10^{-23}\text{ cm}^3} = \mathbf{12.00468\text{ g/cm}^3}$$

---

### 2. Apartado a: Fracción de Puntos Reticulares Vacantes ($f_v$):
$$f_v = \frac{\rho_{\text{ideal}} - \rho_{\text{real}}}{\rho_{\text{ideal}}} = \frac{12.00468 - 11.98000}{12.00468} = \frac{0.02468}{12.00468}$$
$$f_v = \mathbf{0.002055} \approx \mathbf{0.00204} \quad (\approx 0.204\%)$$

---

### 3. Apartado b: Número de Vacantes por Centímetro Cúbico ($n_v$):
* Concentración total de puntos reticulares ($N$):
  $$N = \frac{4}{a^3} = \frac{4}{5.88722 \times 10^{-23}\text{ cm}^3} = 6.79438 \times 10^{22}\text{ sitios/cm}^3$$
* Concentración volumétrica de vacantes:
  $$n_v = f_v \cdot N = (0.002055) \times (6.79438 \times 10^{22}\text{ cm}^{-3}) = \mathbf{1.396 \times 10^{20}\text{ vacantes/cm}^3} \approx \mathbf{1.39 \times 10^{20}\text{ vac/cm}^3}$$
  *(Utilizando el valor oficial $0.00204$: $n_v = 0.00204 \times 6.7944 \times 10^{22} = \mathbf{1.386 \times 10^{20}} \approx \mathbf{1.39 \times 10^{20}\text{ vacancies/cm}^3}$).*

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

* **Detección Picnométrica y Dilatométrica:** Este problema refleja el método clásico de Simmons y Balluffi: comparando la variación del parámetro de red obtenido por difracción de rayos X ($\Delta a / a$) con la variación dimensional macroscópica por dilatometría ($\Delta L / L$), o contrastando la densidad hidrostática con la teórica por rayos X, se mide de forma no destructiva la concentración absoluta de vacantes térmicas en metales nobles como el paladio, platino y oro.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
