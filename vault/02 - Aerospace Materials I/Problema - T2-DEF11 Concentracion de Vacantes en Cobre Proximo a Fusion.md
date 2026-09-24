---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 11"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - copper
  - fcc
  - vacancies-concentration
  - arrhenius
  - high-temperature
---

# ✏️ Problema: T2-DEF11 — Concentración de Vacantes en Cobre Próximo a la Fusión

## 📄 Enunciado Oficial
> **11. Calculate the number of vacancies per $\text{cm}^3$ expected in copper at $1080^\circ\text{C}$ (just below the melting temperature). The energy for vacancy formation is $20000\text{ cal/mol}$.**  
> *(Solution: $4.98 \times 10^{19}\text{ vacancies/cm}^3$)*  
> **Data:** Copper has an FCC crystal structure and a lattice parameter of $3.6151\text{ \AA}$; $R = 1.987\text{ cal/(mol}\cdot\text{K)}$.

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Datos de Entrada:
* Material: Cobre puro ($\text{Cu}$, red FCC con $n = 4\text{ átomos/celda}$).
* Parámetro reticular: $a = 3.6151\text{ \AA} = 3.6151 \times 10^{-8}\text{ cm}$.
* Temperatura: $T = 1080^\circ\text{C} = 1080 + 273.15 = 1353.15\text{ K}$ (punto de fusión del cobre puro: $T_m = 1084.6^\circ\text{C}$).
* Energía de formación de vacantes: $\Delta H_v = 20000\text{ cal/mol}$.
* Constante universal de los gases: $R = 1.987\text{ cal/(mol}\cdot\text{K)}$.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

1. **Número Total de Sitios Reticulares por Unidad de Volumen ($N$):**
   En una celda unitaria cúbica FCC de volumen $V_C = a^3$, existen $4$ puntos de red equivalentes [Session 4 Slide 15]:
   $$N = \frac{n}{V_C} = \frac{4}{a^3} \quad [\text{sitios/cm}^3]$$
2. **Ecuación Termodinámica de Boltzmann para Vacantes [Session 4 Slide 15]:**
   $$n_v = N \cdot \exp\left(-\frac{\Delta H_v}{R \cdot T}\right)$$
   donde $n_v$ representa el número de vacantes en equilibrio térmico por centímetro cúbico.

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Cálculo del Número de Posiciones de Red ($N$):
* Volumen de la celda unitaria cúbica:
  $$V_C = a^3 = (3.6151 \times 10^{-8}\text{ cm})^3 = 4.72457 \times 10^{-23}\text{ cm}^3$$
* Concentración total de nudos de red:
  $$N = \frac{4}{4.72457 \times 10^{-23}\text{ cm}^3} = \mathbf{8.46638 \times 10^{22}\text{ sitios/cm}^3}$$

---

### 2. Cálculo del Factor de Boltzmann ($\exp(-\Delta H_v / RT)$):
* Denominador térmico:
  $$R \cdot T = (1.987\text{ cal/mol}\cdot\text{K}) \times (1353.15\text{ K}) = 2688.71\text{ cal/mol}$$
* Exponente adimensional:
  $$-\frac{\Delta H_v}{R \cdot T} = -\frac{20000\text{ cal/mol}}{2688.71\text{ cal/mol}} = -7.43851$$
* Fracción de vacantes en equilibrio térmico:
  $$\frac{n_v}{N} = \exp(-7.43851) = \mathbf{5.88166 \times 10^{-4}}$$
  *(Nótese que $\approx 0.059\%$, perfectamente coherente con el orden de magnitud de $10^{-4}$ cerca de la fusión [Slide 15]).*

---

### 3. Cálculo de las Vacantes por Centímetro Cúbico ($n_v$):
$$n_v = N \times \left(\frac{n_v}{N}\right) = (8.46638 \times 10^{22}\text{ cm}^{-3}) \times (5.88166 \times 10^{-4})$$
$$n_v = 4.9796 \times 10^{19} \approx \mathbf{4.98 \times 10^{19}\text{ vacancies / cm}^3}$$

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

* **Magnitud Macroscópica:** Aunque la fracción porcentual parece reducida ($0.059\%$), un solo centímetro cúbico de cobre caliente a $1080^\circ\text{C}$ alberga la ingente cantidad de casi **$50$ trillones de vacantes** ($4.98 \times 10^{19}\text{ vacantes}$).
* **Papel en la Difusión y la Fluencia (Creep):** Esta colosal densidad de vacantes permite que los átomos de cobre salten continuamente a posiciones vacías adyacentes a frecuencias del orden de $10^{10}\text{ saltos/s}$, lo que explica por qué a temperaturas superiores a $0.5\, T_m$ los metales experimentan deformación por fluencia térmica (creep) y las dislocaciones pueden ascender (*dislocation climb*) eludiendo obstáculos.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
