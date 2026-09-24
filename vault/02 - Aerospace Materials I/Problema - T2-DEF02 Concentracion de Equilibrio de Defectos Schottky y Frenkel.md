---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 2"
dificultad: media
tags:
  - problema-oficial
  - resuelto
  - schottky
  - frenkel
  - ionic-defects
  - boltzmann-statistics
---

# ✏️ Problema: T2-DEF02 — Concentración de Equilibrio de Defectos Schottky y Frenkel

## 📄 Enunciado Oficial
> **2. Considering that the energies for Schottky and Frenkel defects formation in a specific material are $1\text{ eV}$ and $4\text{ eV}$ per atom, respectively. Determine the equilibrium concentrations of such defects at $1000\text{ K}$. $k = 8.62 \times 10^{-5}\text{ eV/K}$.**  
> *(Solution: $3.026 \times 10^{-3}$ and $8.386 \times 10^{-11}$)*

---

## 📊 1. Fase 1: Hipótesis y Parámetros

### Datos de Entrada:
* Energía de formación de defectos de Schottky: $\Delta H_s = 1.0\text{ eV/defecto}$.
* Energía de formación de defectos de Frenkel: $\Delta H_F = 4.0\text{ eV/defecto}$.
* Temperatura absoluta: $T = 1000\text{ K}$.
* Constante de Boltzmann: $k_B = 8.62 \times 10^{-5}\text{ eV/K}$.

### Hipótesis de Partida:
1. El material es un sólido iónico estequiométrico tipo $MX$.
2. Las concentraciones de defectos se expresan como fracciones respecto al número total de posiciones reticulares regulares $N$ (y asumiendo $N_i \approx N$ para el cálculo de concentración fraccionaria de Frenkel $n_F / \sqrt{N N_i} \approx n_F / N$).

---

## 🧠 2. Fase 2: Formulación y Justificación Pedagógica

Citando las formulaciones oficiales para cristales iónicos [Session 4 Slide 16]:

1. **Defectos de Schottky (Pares de Vacantes Anión-Catión):**
   La formación de un par de Schottky requiere la creación simultánea de dos vacantes de signo opuesto. Termodinámicamente, la fracción de equilibrio es:
   $$\frac{n_s}{N} = \exp\left(-\frac{\Delta H_s}{2\, k_B T}\right)$$

2. **Defectos de Frenkel (Pares Vacante-Intersticial):**
   La migración de un ion a una posición intersticial genera una vacante y un intersticial. La concentración fraccionaria de equilibrio es:
   $$\frac{n_F}{\sqrt{N N_i}} = \exp\left(-\frac{\Delta H_F}{2\, k_B T}\right)$$

> [!NOTE]
> El factor $2$ en el denominador del exponente es un rasgo termodinámico fundamental de los defectos iónicos: puesto que se generan dos especies de defectos simultáneamente para conservar la electroneutralidad, el producto de actividades de masas conduce a $\exp(-\Delta H / 2k_B T)$.

---

## 🔢 3. Fase 3: Desarrollo Matemático Paso a Paso

### 1. Concentración de Defectos de Schottky ($n_s / N$):
* Denominador térmico:
  $$2\, k_B T = 2 \times (8.62 \times 10^{-5}\text{ eV/K}) \times (1000\text{ K}) = 2 \times 0.0862\text{ eV} = 0.1724\text{ eV}$$
* Argumento de la exponencial:
  $$-\frac{\Delta H_s}{2\, k_B T} = -\frac{1.0\text{ eV}}{0.1724\text{ eV}} = -5.800464$$
* Concentración en equilibrio:
  $$\frac{n_s}{N} = \exp(-5.800464) = \mathbf{3.0262 \times 10^{-3}} \approx \mathbf{3.026 \times 10^{-3}}$$

---

### 2. Concentración de Defectos de Frenkel ($n_F / \sqrt{N N_i}$):
* Denominador térmico:
  $$2\, k_B T = 0.1724\text{ eV}$$
* Argumento de la exponencial:
  $$-\frac{\Delta H_F}{2\, k_B T} = -\frac{4.0\text{ eV}}{0.1724\text{ eV}} = -23.201856$$
* Concentración en equilibrio:
  $$\frac{n_F}{\sqrt{N N_i}} = \exp(-23.201856) = \mathbf{8.386 \times 10^{-11}}$$

---

## 🎯 4. Fase 4: Interpretación Física y Verificación

1. **Predominancia Termodinámica Absoluta:**
   Comparando ambas poblaciones a $1000\text{ K}$:
   $$\frac{n_s}{n_F} = \frac{3.026 \times 10^{-3}}{8.386 \times 10^{-11}} \approx \mathbf{3.6 \times 10^{7}}$$
   La concentración de defectos de Schottky es más de **36 millones de veces superior** a la de defectos de Frenkel.
2. **Correlación con la Diapositiva 16 [Session 4 Slide 16]:**
   Tal como establece textualmente la teoría oficial:
   $$\text{"In a crystal } \Delta H_s \neq \Delta H_F \implies \text{the defect with the lowest } \Delta H \text{ will form"}$$
   Dado que $\Delta H_s = 1\text{ eV} \ll \Delta H_F = 4\text{ eV}$, el cristal presentará de manera abrumadoramente dominante defectos de tipo Schottky, mientras que los defectos de Frenkel serán estadísticamente inexistentes.

---
*Retorno:* `[[Tema 2 - Structure of Materials and Crystalline Defects|⬅️ Volver a Tema 2]]` | `[[02 - Aerospace Materials I/Materiales Aeroespaciales I MOC|🔬 MOC Asignatura]]`
