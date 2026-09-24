---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 4 T2 Structure of Materials II_2025.pdf, Slides 12-18"
tags:
  - teoria
  - concepto-fundamental
  - defectos-puntuales
  - vacantes
  - schottky
  - frenkel
  - termodinamica-defectos
dificultad: alta
prerrequisitos:
  - "[[Concepto - Difraccion de Rayos X y Ley de Bragg]]"
---

# 🔘 Concepto: Defectos Puntuales, Vacantes Térmicas, Schottky y Frenkel

> **Principio Termodinámico:** Un cristal perfecto libre de defectos solo puede existir en el cero absoluto ($T = 0\text{ K}$). A cualquier temperatura $T > 0\text{ K}$, la introducción espontánea de defectos de dimensión cero (**defectos puntuales**) aumenta la entalpía del cristal ($\Delta H > 0$), pero genera un incremento extraordinario en la **entropía configuracional** ($\Delta S_{\text{conf}} > 0$). Por tanto, la variación de energía libre de Gibbs $\Delta G = \Delta H - T\Delta S$ alcanza un mínimo estable a una concentración finita de equilibrio de defectos [Slides 11, 15].

---

## 🌡️ 1. Termodinámica de la Formación de Vacantes en Metales

Una **vacante** es la ausencia de un átomo o ion en un nudo regular de la red [Slide 15].

### Deducción de la Concentración de Equilibrio ($n_v/N$):
Sea un cristal metálico con $N$ posiciones reticulares y $n_v$ vacantes. El número de formas microscópicas indistinguibles de distribuir $n_v$ vacantes en $N$ posiciones viene dado por la combinatoria:
$$W = \frac{N!}{(N - n_v)! \, n_v!}$$

La entropía configuracional según la ecuación de Boltzmann es:
$$S = k_B \ln W = k_B \left[ \ln N! - \ln(N - n_v)! - \ln n_v! \right]$$

Aplicando la aproximación de Stirling ($\ln x! \approx x\ln x - x$):
$$S \approx k_B \left[ N\ln N - (N - n_v)\ln(N - n_v) - n_v \ln n_v \right]$$

El cambio en la energía libre de Gibbs para formar $n_v$ vacantes con entalpía de formación $\Delta H_v$ por mol es:
$$\Delta G(n_v) = n_v \Delta H_v - T \Delta S$$

En el equilibrio termodinámico a temperatura constante $T$, la energía libre se minimiza:
$$\left( \frac{\partial \Delta G}{\partial n_v} \right)_T = \Delta H_v - k_B T \ln\left( \frac{N - n_v}{n_v} \right) = 0$$

Dado que $n_v \ll N$ ($n_v/N \sim 10^{-4}$ cerca del punto de fusión [Slide 15]):
$$\ln\left(\frac{N}{n_v}\right) = \frac{\Delta H_v}{k_B T} \implies \frac{n_v}{N} = \exp\left(-\frac{\Delta H_v}{k_B T}\right) = \exp\left(-\frac{\Delta H_v}{RT}\right)$$

### Parámetros de la Ecuación:
* $n_v$: número de vacantes en equilibrio por unidad de volumen ($\text{vacantes/cm}^3$).
* $N$: densidad numérica de posiciones de red ($\text{sitios/cm}^3$):
  $$N = \frac{\rho \cdot N_A}{M} = \frac{n_{\text{átomos celda}}}{V_C}$$
* $\Delta H_v$: entalpía o energía molar de formación de una vacante ($\text{J/mol}$ o $\text{cal/mol}$, o $E_v$ en $\text{eV/átomo}$).
* $R = 8.314\text{ J/mol}\cdot\text{K} = 1.987\text{ cal/mol}\cdot\text{K}$ (o constante de Boltzmann $k_B = 8.62 \times 10^{-5}\text{ eV/K}$).
* Fracción de vacantes máxima: En la mayoría de los metales cerca de la temperatura de fusión $T_m$, la fracción alcanza $n_v/N \approx 10^{-4}\text{--}10^{-3}$ [Slide 15].

---

## ⚡ 2. Defectos Puntuales en Cristales Iónicos (Schottky y Frenkel)

En los cerámicos iónicos, cualquier defecto debe preservar de manera estricta la **electroneutralidad macroscópica** del cristal [Slide 16].

### a) Defecto de Schottky (Par de Vacantes Catión-Anión) [Slide 16]
* **Mecanismo:** Un catión y un anión abandonan simultáneamente sus posiciones reticulares regulares y migran a la superficie exterior del cristal.
* Se crea un **par estequiométrico de vacantes** ($1\text{ vacante catiónica} + 1\text{ vacante aniónica}$ en un compuesto $MX$).
* La densidad volumétrica del cristal **disminuye**.
* **Concentración de equilibrio:**
  $$n_s = N \exp\left(-\frac{\Delta H_s}{2RT}\right)$$
  *(El factor 2 en el denominador refleja que la formación de cada defecto implica la creación simultánea de dos vacantes independientes).*

### b) Defecto de Frenkel (Par Vacante-Intersticial) [Slide 16]
* **Mecanismo:** Un ion (generalmente el catión, al ser de menor radio atómico) salta de su posición reticular normal hacia un hueco intersticial cercano.
* Se forma un par asociado: **1 vacante catiónica + 1 catión intersticial**.
* La densidad volumétrica macroscópica **se mantiene prácticamente constante**.
* **Concentración de equilibrio:**
  $$n_F = \sqrt{N N_i} \exp\left(-\frac{\Delta H_F}{2RT}\right)$$
  donde $N$ es el número de posiciones regulares y $N_i$ es el número de posiciones intersticiales disponibles.

---

## 📊 3. Entalpías Oficiales de Formación de Defectos (Smart & Moore)

En cualquier cristal iónico real, $\Delta H_s \neq \Delta H_F$. **El defecto que predomina es siempre aquel con la menor entalpía de formación $\Delta H$** [Slides 16-17]:

| Compuesto | Tipo de Defecto Dominante | Entalpía de Formación ($\Delta H$) | Concentración a $300\text{ K}$ | Concentración a $1000\text{ K}$ |
| :--- | :--- | :--- | :--- | :--- |
| **$\text{NaCl}$** | **Schottky** | $3.69 \times 10^{-19}\text{ J}$ ($2.30\text{ eV}$) | $n_s = 2.64 \times 10^{4}\text{ vac/mol}$ | $n_s = 9.38 \times 10^{17}\text{ vac/mol}$ |
| **$\text{MgO}$** | **Schottky** | $10.57 \times 10^{-19}\text{ J}$ ($6.60\text{ eV}$) | $n_s = 2.12 \times 10^{-32}\text{ vac/mol}$ | $n_s = 1.39 \times 10^{7}\text{ vac/mol}$ |
| **$\text{CaO}$** | **Schottky** | $\approx 9.8 \times 10^{-19}\text{ J}$ | Despreciable | Baja |
| **$\text{LiF}$** | **Schottky** | $\approx 4.3 \times 10^{-19}\text{ J}$ | Muy baja | Moderada |
| **$\text{AgCl}$** | **Frenkel (catiónico)** | $\approx 2.56 \times 10^{-19}\text{ J}$ ($1.60\text{ eV}$) | Apreciable | Alta |

> [!NOTE]
> Debido a que la carga de los iones en $\text{MgO}$ ($\text{Mg}^{2+}, \text{O}^{2-}$) es el doble que en $\text{NaCl}$ ($\text{Na}^{+}, \text{Cl}^{-}$), la atracción electrostática de Coulomb es unas 4 veces superior. Por tanto, la entalpía de formación de Schottky en $\text{MgO}$ ($10.57 \times 10^{-19}\text{ J}$) es casi el triple que en $\text{NaCl}$, haciendo extraordinariamente más difícil generar vacantes térmicas en $\text{MgO}$ [Slide 17].

---
*Enlaces Bidireccionales:*
* `[[Concepto - Difraccion de Rayos X y Ley de Bragg|⬅️ Anterior: Difracción de Rayos X]]`
* `[[Concepto - Soluciones Solidas Sustitucionales e Intersticiales Reglas de Hume-Rothery|Siguiente: Soluciones Sólidas y Hume-Rothery ➡️]]`
