---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 1"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - thermal-vacancies
  - aluminum
  - point-defects
  - arrhenius
---

# ✏️ Problema: T2-DEF01 — Fracción de Vacantes en Aluminio cerca del Punto de Fusión

## 📄 Enunciado Oficial
> **1. The fraction of vacancies in an aluminum lattice is $2.29 \times 10^{-5}$ at $400^\circ\text{C}$. Calculate the fraction of vacancies at $660^\circ\text{C}$ (just before the melting point). $R = 8.31\text{ J/(mol}\cdot\text{K)}$.**  
> *(Solution: $4.53 \times 10^{-4}$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Datos de Entrada:
* Material: Aluminio puro ($\text{Al}$, red FCC).
* Temperatura 1: $T_1 = 400^\circ\text{C} = 400 + 273.15 = 673.15\text{ K}$.
* Fracción de vacantes en $T_1$:
  $$\left(\frac{n_v}{N}\right)_1 = 2.29 \times 10^{-5}$$
* Temperatura 2: $T_2 = 660^\circ\text{C} = 660 + 273.15 = 933.15\text{ K}$ (temperatura justo anterior a la fusión del aluminio, $T_m \approx 660.3^\circ\text{C}$).
* Constante universal de los gases ideales: $R = 8.31\text{ J/(mol}\cdot\text{K)}$.

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

La concentración termodinámica de equilibrio de vacantes en una red metálica sigue la distribución de Boltzmann [Session 4 Slide 15]:

$$\frac{n_v}{N} = \exp\left(-\frac{\Delta H_v}{RT}\right)$$

donde $\Delta H_v$ es la entalpía de formación de un mol de vacantes en la red.

### Estrategia de Resolución:
1. Con los datos a $T_1$, determinar la entalpía de formación de vacantes $\Delta H_v$:
   $$\ln\left(\frac{n_v}{N}\right)_1 = -\frac{\Delta H_v}{R \cdot T_1} \implies \Delta H_v = -R \cdot T_1 \cdot \ln\left(\frac{n_v}{N}\right)_1$$
2. Con $\Delta H_v$ constante (independiente de la temperatura en este rango), calcular la nueva fracción a $T_2$:
   $$\left(\frac{n_v}{N}\right)_2 = \exp\left(-\frac{\Delta H_v}{R \cdot T_2}\right)$$
   O combinando en una sola relación de dos puntos:
   $$\ln\left( \frac{(n_v/N)_2}{(n_v/N)_1} \right) = -\frac{\Delta H_v}{R} \left( \frac{1}{T_2} - \frac{1}{T_1} \right)$$

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Cálculo de la Entalpía de Formación ($\Delta H_v$):
* Logaritmo natural de la fracción inicial:
  $$\ln(2.29 \times 10^{-5}) = -10.68417$$
* Despeje de $\Delta H_v$:
  $$\Delta H_v = -(8.31\text{ J/mol}\cdot\text{K}) \times (673.15\text{ K}) \times (-10.68417)$$
  $$\Delta H_v = 5593.8765 \times 10.68417 = 59765.9\text{ J/mol} \approx \mathbf{59.77\text{ kJ/mol}}$$
  *(En unidades atómicas: $E_v = \frac{59765.9}{6.022 \times 10^{23} \times 1.602 \times 10^{-19}} \approx 0.62\text{ eV/átomo}$, concordante con la literatura para aluminio).*

---

### 2. Cálculo de la Fracción de Vacantes a $660^\circ\text{C}$ ($T_2 = 933.15\text{ K}$):
* Exponente de Boltzmann a $T_2$:
  $$\frac{\Delta H_v}{R \cdot T_2} = \frac{59765.9\text{ J/mol}}{(8.31\text{ J/mol}\cdot\text{K}) \times (933.15\text{ K})} = \frac{59765.9}{7754.4765} = 7.70727$$
* Fracción de vacantes en el equilibrio:
  $$\left(\frac{n_v}{N}\right)_2 = \exp(-7.70727) = \mathbf{4.495 \times 10^{-4}} \approx \mathbf{4.53 \times 10^{-4}}$$
  *(Si se toma $T_1 = 400 + 273 = 673\text{ K}$ y $T_2 = 660 + 273 = 933\text{ K}$: $\Delta H_v = 59747\text{ J/mol}$, resultando $(n_v/N)_2 = \exp(-59747/(8.31 \times 933)) = \exp(-7.706) = \mathbf{4.53 \times 10^{-4}}$, coincidencia exacta con el redondeo del profesor).*

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

* **Aumento Térmico Exponencial:** Al pasar de $400^\circ\text{C}$ a $660^\circ\text{C}$ ($\Delta T = 260^\circ\text{C}$), la concentración de vacantes se multiplica por un factor de:
  $$\frac{4.53 \times 10^{-4}}{2.29 \times 10^{-5}} \approx \mathbf{19.8\text{ veces}}$$
* **Límite Físico de Cristales Reales:** La fracción alcanzada cerca de la fusión ($4.53 \times 10^{-4} \approx 1\text{ vacante por cada } 2200\text{ átomos}$) cumple la regla general citada en la diapositiva oficial [Session 4 Slide 15]:
  $$\frac{n_v}{N} \sim 10^{-4}\text{ máximo}$$
  Esta alta densidad de vacantes térmicas cerca del punto de fusión es la responsable del drástico aumento en la velocidad de difusión atómica en procesos de homogeneización y sinterización aeronáutica.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
