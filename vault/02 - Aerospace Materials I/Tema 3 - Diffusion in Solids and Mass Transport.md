---
materia: "Aerospace Materials I"
tema: "Tema 3: Diffusion in Solids and Mass Transport"
fuentes: "Session 5 T3  Difussion_2025.pdf, Problems T3_Diffusion.pdf"
tags:
  - teoria
  - moc-tema
  - diffusion
  - ficks-laws
  - steady-state
  - non-steady-state
  - error-function
  - arrhenius
  - case-hardening
dificultad: media
prerrequisitos:
  - "[[Tema 2 - Structure of Materials and Crystalline Defects]]"
---

# 🌐 Tema 3: Diffusion in Solids and Mass Transport

> **Idea Central del Tema:** La **difusión en sólidos** es el fenómeno de transporte de materia en el que átomos, iones o moléculas migran a través de la red cristalina mediante vibraciones térmicamente activadas, impulsados fundamentalmente por un **gradiente de concentración** ($\nabla C$). Rige desde los tratamientos termoquímicos de endurecimiento superficial en engranajes aeronáuticos hasta la fabricación de circuitos integrados en obleas de silicio, la sinterización de álabes cerámicos y la soldadura por difusión en turbofanes de última generación [Session 5 Slides 2, 29-35].

$$\text{Gradiente de Concentración } (\nabla C) + \text{Activación Térmica } (T > 0\text{ K}) \implies \text{Transporte de Masa } (J = -D \nabla C)$$

---

## 🗺️ 1. Mapa Conceptual de la Sesión Oficial UC3M (Sesión 5)

```
TEMA 3: DIFUSIÓN EN SÓLIDOS Y TRANSPORTE DE MASA
│
├── ⚛️ 1. CONCEPTOS FUNDAMENTALES Y MECANISMOS ATÓMICOS (Slides 2-13)
│   ├── Definición: Transporte de materia en sólidos mediante vibración térmica activada
│   ├── Fuerza Impulsora: Gradiente de composición (tendencia a homogenizar)
│   ├── Requisitos: Sitio adyacente vacante (empty site) + Energía térmica ≥ Energía de activación (Ea)
│   ├── Mecanismo por Vacantes (Sustitucional):
│   │   ├── Auto-difusión (Self-diffusion): Intercambio atómico en metal puro (Eself = Ev + Em)
│   │   ├── Correlación con Tm: Mayor punto de fusión ⟹ mayor energía de enlace ⟹ mayor Ea
│   │   └── Interdifusión: Movimiento en aleaciones sustitucionales (Reglas de Hume-Rothery, par Cu-Ni)
│   └── Mecanismo Intersticial:
│       ├── Migración de solutos pequeños (C, H, N, O, B) entre intersticios sin deformar permanentemente la matriz
│       └── Ventajas cinéticas: Ei ≪ Ev, abundancia de huecos libres, Dintersticial es 10⁴-10⁶ veces más rápido
│
├── 📏 2. LEYES DE FICK DE LA DIFUSIÓN (Slides 15-21)
│   ├── Densidad de Flujo Difusional: J = M / (A · t) [mol/(cm²·s) o kg/(m²·s)]
│   ├── Primera Ley de Fick — Estado Estacionario (∂C/∂t = 0, ∂J/∂t = 0):
│   │   ├── Ecuación fundamental: J = -D · (∂C/∂x) ≈ -D · (ΔC / Δx)
│   │   └── Perfil de concentración estrictamente lineal en membranas planas (Δx = D · ΔC / J)
│   └── Segunda Ley de Fick — Estado No Estacionario / Transitorio (∂C/∂t ≠ 0):
│       ├── Ecuación diferencial general: ∂Cx/∂t = D · (∂²Cx/∂x²) (para D ≠ f(C))
│       ├── Geometría de Sólido Semi-Infinito (x = 0 a ∞): C(x,0) = C₀, C(0,t) = Cs, C(∞,t) = C₀
│       ├── Solución analítica con Función Error: (Cx - C₀)/(Cs - C₀) = 1 - erf(x / (2√Dt))
│       └── Propiedades de erf(z), tabla oficial de valores (z = 0 a 2.0) e interpolación lineal
│
├── 🌡️ 3. FACTORES QUE GOBIERNAN LA DIFUSIVIDAD (Slides 23-27)
│   ├── Ecuación de Arrhenius: D = D₀ · exp(-ED / RT)
│   ├── Linealización logarítmica: ln D = ln D₀ - (ED / R) · (1/T) (gráfico de pendiente -ED/R)
│   ├── Formulación de dos temperaturas: ln(D₂/D₁) = (ED / R) · (1/T₁ - 1/T₂)
│   └── Factores moduladores de D:
│       ├── Mecanismo atómico (Intersticial vs Vacantes: DC ≫ DFe)
│       ├── Estructura cristalina de la matriz (Red abierta BCC > Red compacta FCC)
│       ├── Defectos cristalinos y cortocircuitos: Dsuperficie > Dlímite de grano > Dvolumen
│       └── Concentración de soluto y temperatura homóloga T/Tm
│
└── ⚙️ 4. APLICACIONES INDUSTRIALES Y AEROESPACIALES (Slides 29-35)
    ├── Cementación superficial de aceros (Case hardening, CH₄-H₂, tensiones de compresión, engranajes)
    ├── Purificación de hidrógeno gaseoso con membranas de Paladio (Pd)
    ├── Sinterización de cerámicos y metales (densificación y eliminación de porosidad)
    ├── Soldadura por difusión y conformado superplástico (DB/SPF, álabes Rolls-Royce Trent 500)
    ├── Dopaje de obleas de Silicio en microelectrónica y nitruración de polvo de Si (Si₃N₄)
    └── Barrera de permeación en films poliméricos frente a O₂ y humedad
```

---

## 📐 2. Ecuaciones y Relaciones Matemáticas Fundamentales

### 1. Flujo Difusional y Primera Ley de Fick (Estado Estacionario):
$$J = \frac{M}{A \cdot t} \quad \left[\frac{\text{kg}}{\text{m}^2\cdot\text{s}}\right] \quad \text{o} \quad \left[\frac{\text{mol}}{\text{cm}^2\cdot\text{s}}\right]$$
$$J = -D \frac{\partial C}{\partial x} \approx -D \frac{\Delta C}{\Delta x} = D \frac{C_{\text{alta}} - C_{\text{baja}}}{\Delta x}$$

### 2. Segunda Ley de Fick y Solución en Sólido Semi-Infinito:
$$\frac{\partial C_x}{\partial t} = D \frac{\partial^2 C_x}{\partial x^2}$$
$$\frac{C_x - C_0}{C_s - C_0} = 1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right) \iff \frac{C_s - C_x}{C_s - C_0} = \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right) = \text{erf}(z)$$

donde $z \equiv \frac{x}{2\sqrt{Dt}}$, permitiendo despejar el tiempo:
$$t = \frac{x^2}{4 \cdot z^2 \cdot D}$$

### 3. Ecuación de Arrhenius para la Difusividad Térmica:
$$D = D_0 \exp\left(-\frac{E_D}{RT}\right)$$
$$\ln D = \ln D_0 - \left(\frac{E_D}{R}\right) \frac{1}{T}$$
$$\ln\left(\frac{D_2}{D_1}\right) = \frac{E_D}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) \implies E_D = \frac{R \cdot \ln(D_2 / D_1)}{\frac{1}{T_1} - \frac{1}{T_2}}$$

### 4. Jerarquía de Difusividades por Defectos y Estructura:
$$D_{\text{superficie}} > D_{\text{límite de grano}} > D_{\text{volumen (red)}}$$
$$D_{\text{intersticial}} \gg D_{\text{vacantes}} \quad (\text{factor de } 10^4\text{--}10^6)$$
$$D_{\text{BCC}} > D_{\text{FCC}} \quad (\text{para igual soluto e igual } T)$$

---

## 📚 3. Índice de Notas Conceptuales Atómicas (5 Conceptos)

1. `[[Concepto - Mecanismos de Difusion Vacantes e Intersticios]]`  
   *Definición de transporte térmico, fuerza impulsora por gradiente de potencial químico, auto-difusión e interdifusión con reglas de Hume-Rothery, correlación $E_a\text{--}T_m$ y cinética acelerada de solutos intersticiales ($\text{C}, \text{H}, \text{N}$).*
2. `[[Concepto - Primera Ley de Fick Difusion en Estado Estacionario]]`  
   *Definición de flujo difusional $J$, condiciones de estado estacionario ($\partial C/\partial t = 0$), signo negativo del gradiente, perfiles lineales en membranas planas y formulación del transporte másico.*
3. `[[Concepto - Segunda Ley de Fick Difusion en Estado No Estacionario y Funcion Error]]`  
   *Deducción por continuidad diferencial, hipótesis $D \neq f(C)$, sólido semi-infinito con $C_s$ y $C_0$, definición de $\text{erf}(z)$, tabla oficial completa de $z = 0$ a $2.0$ y algoritmo de interpolación lineal.*
4. `[[Concepto - Ecuacion de Arrhenius y Factores que Influyen en la Difusividad]]`  
   *Dependencia térmica $D(T)$, linealización logarítmica y método de dos temperaturas, factores moduladores (tamaño atómico, red abierta BCC vs compacta FCC, difusión en cortocircuito en grano y superficie).*
5. `[[Concepto - Cementacion y Aplicaciones Industriales de la Difusion]]`  
   *Tratamiento termoquímico de cementación gaseosa (*case hardening*) en aceros para engranajes, membranas de paladio para $\text{H}_2$, sinterización de cerámicos, soldadura por difusión DB/SPF en álabes Rolls-Royce Trent 500 y barreras poliméricas.*

---

## ✏️ 4. Colección de Problemas Oficiales Resueltos (6 Problemas)

| Código | Título del Problema | Tema y Fenómeno Físico | Resultado Oficial |
| :---: | :--- | :--- | :---: |
| **T3-01** | `[[Problema - T3-01 Carburacion de Engranaje de Acero 1018]]` | Fick 2 · Sólido Semi-infinito · Interpolación $\text{erf}(z)$ | $t = 6636\text{ s} = 1.84\text{ h}$ |
| **T3-02** | `[[Problema - T3-02 Difusion de Aluminio en Silicio Monocristalino]]` | Arrhenius inverso · Dopaje semiconductor | $T = 1566\text{ K} = 1293^\circ\text{C}$ |
| **T3-03** | `[[Problema - T3-03 Energia de Activacion y Difusividad de Carbono en Acero]]` | Método 2 temperaturas · $E_D$ y extrapolación $D(1000^\circ\text{C})$ | $E_D = 36\text{ kcal/mol}$, $D = 3.23 \times 10^{-11}\text{ m}^2/\text{s}$ |
| **T3-04** | `[[Problema - T3-04 Transporte Ionico de Niquel a Traves de Placa de MgO]]` | Fick 1 · Transporte iónico en cerámico · Red FCC $\text{Ni}$ | $t = 309\text{ h}$ |
| **T3-05** | `[[Problema - T3-05 Temperatura de Cementacion de Acero 1010 en 8 Horas]]` | Acoplamiento Fick 2 + Arrhenius · Diseño térmico | $T = 1175\text{ K} = 902^\circ\text{C}$ |
| **T3-06** | `[[Problema - T3-06 Purificacion de Hidrogeno con Membrana de Paladio]]` | Fick 1 · Permeación en membrana $\text{Pd}$ · Flujo másico | $\Delta x = 5\text{ mm}$ |

---

## 🔗 Navegación y Retorno
* `[[Materiales Aeroespaciales I MOC|⬅️ Volver al MOC de Asignatura]]`
* `[[00 - Indice Central/Indice Maestro|🗺️ Índice Maestro de la Bóveda]]`
* Portal Web de Teoría: `subjects/aerospace-materials-1/teoria/topic-3-diffusion.html`
* Portal Web de Problemas: `subjects/aerospace-materials-1/problemas/topic-3-diffusion.html`
