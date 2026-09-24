---
materia: "Aerospace Materials I"
tema: "Tema 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 3 T2 Structure of Materials I_2025.pdf, Slide 53"
tags:
  - teoria
  - concepto-fundamental
  - difraccion-rayos-x
  - ley-de-bragg
  - espaciado-interplanar
  - caracterizacion-materiales
dificultad: media
prerrequisitos:
  - "[[Concepto - Notacion de Miller para Direcciones y Planos Cubicos y Hexagonales]]"
---

# ⚡ Concepto: Difracción de Rayos X y Ley de Bragg

> **Principio de Difracción:** Los rayos X poseen longitudes de onda del orden de las distancias interatómicas ($\lambda \sim 0.05\text{--}0.25\text{ nm} \sim 0.5\text{--}2.5\text{ \AA}$). Cuando un haz monocromático incide sobre un cristal periódico, las ondas dispersadas elásticamente por los electrones de planos atómicos paralelos interfieren constructivamente si la diferencia de camino óptico es un múltiplo entero de la longitud de onda [Slide 53].

---

## 📐 1. Ecuaciones del Espaciado Interplanar ($d_{hkl}$)

El espaciado interplanar $d_{hkl}$ es la distancia perpendicular más corta que separa dos planos cristalográficos adyacentes pertenecientes a la misma familia de Miller $(h\, k\, l)$ [Slide 53]:

### 1. Sistema Cúbico ($a = b = c$, $\alpha = \beta = \gamma = 90^\circ$):
$$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$

### 2. Sistema Ortorrómbico General ($a \neq b \neq c$, $\alpha = \beta = \gamma = 90^\circ$):
$$\frac{1}{d_{hkl}^2} = \frac{h^2}{a^2} + \frac{k^2}{b^2} + \frac{l^2}{c^2} \implies d_{hkl} = \frac{1}{\sqrt{\frac{h^2}{a^2} + \frac{k^2}{b^2} + \frac{l^2}{c^2}}}$$

### 3. Sistema Tetragonal ($a = b \neq c$, $\alpha = \beta = \gamma = 90^\circ$):
$$\frac{1}{d_{hkl}^2} = \frac{h^2 + k^2}{a^2} + \frac{l^2}{c^2}$$

### 4. Sistema Hexagonal ($a = b \neq c$, $\gamma = 120^\circ$):
$$\frac{1}{d_{hkl}^2} = \frac{4}{3}\left(\frac{h^2 + hk + k^2}{a^2}\right) + \frac{l^2}{c^2}$$

---

## 🌊 2. Deducción de la Ley de Bragg

Consideremos dos rayos incidentes paralelos con ángulo rasante $\theta$ (ángulo de Bragg) reflejados en dos planos atómicos paralelos adyacentes $(hkl)$ separados por una distancia $d_{hkl}$:

```
     Rayo 1 \         / Rayo difractado 1
             \   θ   /
 Plano 1 ─────●─────●───── (hkl)
             /|     |\
            / | d   | \
           /  |     |  \
     Rayo 2 \ |     | / Rayo difractado 2
             \|  θ  |/
 Plano 2 ─────●─────●───── (hkl)
              A     B
```

* El rayo 2 recorre una distancia adicional antes de reflejarse igual a $d_{hkl}\sin\theta$.
* Tras la reflexión, recorre otra distancia adicional idéntica igual a $d_{hkl}\sin\theta$.
* **Diferencia de camino óptico total:**
  $$\Delta = 2\, d_{hkl}\sin\theta$$
* **Condición de Interferencia Constructiva Máxima (Ley de Bragg) [Slide 53]:**
  $$n\lambda = 2\, d_{hkl}\sin\theta$$
  donde $n$ es el orden de difracción ($n = 1$ para difracción de primer orden, absorbiéndose órdenes superiores dentro de los índices de Miller: $d_{nh, nk, nl} = d_{hkl}/n$).

---

## 🔍 3. Reglas de Extinción Sistemática (Factor de Estructura $F_{hkl}$)

Debido a la interferencia destructiva de planos atómicos intermedios en celdas centradas, ciertas reflexiones $(hkl)$ no aparecen en el difractograma:

| Estructura Cristalina | Condición de Reflexión Permitida | Reflexiones Típicas Observadas | Reflexiones Prohibidas (Extintas) |
| :--- | :--- | :--- | :--- |
| **Cúbica Simple (SC)** | Cualquier combinación $(hkl)$ | $(100), (110), (111), (200), (210), (211)$ | Ninguna |
| **Cúbica Centrada en Cuerpo (BCC)** | $h + k + l = \text{par}$ | $(110), (200), (211), (220), (310), (222)$ | $(100), (111), (210), (300)$ |
| **Cúbica Centrada en Caras (FCC)** | $h, k, l$ todos pares o todos impares | $(111), (200), (220), (311), (222), (400)$ | $(100), (110), (210), (211)$ |

---

## 🔬 4. Aplicaciones en Ingeniería Aeroespacial

1. **Determinación Precisa de Parámetros de Red ($a, c$):**
   Midiendo con precisión los ángulos de pico $2\theta$, se calcula $d_{hkl}$ y se despeja el parámetro reticular $a$:
   $$a = \frac{\lambda \sqrt{h^2 + k^2 + l^2}}{2\sin\theta}$$
2. **Identificación de Fases y Polimorfismo:**
   Permite distinguir instantáneamente fases alotrópicas (p. ej., ferrita $\alpha\text{-Fe}$ BCC vs austenita $\gamma\text{-Fe}$ FCC; titanio $\alpha\text{-HCP}$ vs $\beta\text{-BCC}$).
3. **Análisis de Tensiones Residuales Macroscópicas:**
   La presencia de tensiones residuales de tracción o compresión (debidas a granallado, soldadura por fricción-agitación o mecanizado) altera el espaciado interplanar $\Delta d$, desplazando angularmente los picos de difracción ($\Delta \theta$).

---
*Enlaces Bidireccionales:*
* `[[Concepto - Densidad Volumetrica Lineal y Planar en Redes Cristalinas|⬅️ Anterior: Densidades Cristalográficas]]`
* `[[Concepto - Defectos Puntuales Vacantes Termicas Schottky y Frenkel|Siguiente: Defectos Puntuales ➡️]]`
