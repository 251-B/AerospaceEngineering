# Plan del segundo parcial de Mecánica de Fluidos (Temas 4-7)

Creado el 2026-11-23. Fuente: `sources/cuatrimestre-1/01-fluid-mechanics/examenes/FLUIDS_SECONDPARTIAL_*.pdf` (13 convocatorias, 2011-2025) y las hojas NS, FS, DA y VF.
Pendiente de confirmar: fecha del examen, horas disponibles, formato 2026 y qué problemas se han hecho en clase de los Temas 5-7.

## 1. Qué ha caído (segundos parciales)

| Año | Problema largo | Ejercicio corto / otros |
| :--- | :--- | :--- |
| 2011 | NS: película en plano inclinado + temperatura + balance de energía (= NS7) | - |
| 2013 (prefinal) | NS: anillo entre cilindros con giro y arrastre axial; VF: pared que arrastra líquido por una ranura, h(t) (= VF18) | DA: misil supersónico (= DA12); CL: codo de mezcla |
| 2014 | VF: cuerpo que cae sobre una capa de líquido (squeeze film), órdenes de magnitud, h(t) | DA: cetáceos con tabla de datos; CL: caudalímetro |
| 2015 | NS: cilindro poroso con succión que se mueve axialmente (= NS8) + T | DA: viscosímetro con tabla de datos; CL: unión de tuberías |
| 2016 | VF: descarga de depósito por tubo, criterios, H(t), tiempo de descarga | DA + Stokes: microorganismo, Pi + NS adimensional con Re -> 0 + arrastre de la esfera |
| 2016 retake | NS: cavidad entre cilindros porosos, campo de presión, velocidades, fuerza, T (≈ NS13) | CL: aspersor |
| 2017 | VF: pistón con conducto (apartado 1 es hidrostática: fuerza sobre el pistón en reposo) | - |
| 2017 retake | NS: dos líquidos concéntricos en tubería vertical + T | - |
| 2018 retake | NS: cilindros porosos (igual que 2016 retake) | CL: aspersor |
| 2021 | VF: canal de altura variable con paredes móviles (lubricación, Reynolds), 70 min | DA + VF: contracción, Pi + estimaciones de flujo esbelto, 25 min |
| 2021 retake | NS: cilindro poroso que gira con inyección, v_r, v_θ ∝ r^n, p(r), T (no hay solución estacionaria) | - |
| 2022 | VF + DA: tubo con hilo concéntrico, Pi + Poiseuille anular + Q, 75 min | VF: capa de Stokes por pared oscilante (= VF2), 20 min |
| 2025 | VF: canal con 2 líquidos entre depósitos, l(t), tiempo, fuerza y momento sobre la placa (≈ VF5), 65 min (70 %) | DA: bomba centrífuga, semejanza física, curvas Δp-ω y Δp-Q, 25 min (30 %) |

Nota: hasta 2018 el segundo parcial incluía también un problema de leyes de conservación integrales (CL); desde 2021 ya no.

## 2. Patrones

- **Formato actual (2021, 2022, 2025):** 1 problema largo (65-75 min, ~70 %) + 1 ejercicio corto (20-25 min, ~30 %).
- **Problema largo = flujo viscoso (Tema 7) casi siempre:** flujo esbelto dominado por viscosidad, cuasi estacionario. Siempre empieza con **órdenes de magnitud** (V_L, Δp, t_0, criterio Re·h/L << 1 y criterio de no estacionariedad), luego perfil de velocidad u(y) o w(r) en función del gradiente de presión reducida, caudal Q, distribución p(x), y al final una **ecuación de evolución** (h(t), H(t), l(t)) o fuerzas/momentos/potencia.
- **Ejercicio corto = análisis dimensional (Tema 6)** en 2021 y 2025 (Pi + simplificar un límite + semejanza con datos), o una **capa de Stokes** (2022).
- **DA aparece en 9 de 13 convocatorias.** Dos sabores: (a) Pi + límite + uso de tabla/curva para otro tamaño o velocidad (semejanza); (b) Pi combinado con estimaciones de VF.
- **NS exacto (Tema 4):** cilindros porosos/rotatorios en coordenadas cilíndricas, con v_r de continuidad, p de la ecuación radial, v_θ o v_z por ODE tipo r^n, y casi siempre la **temperatura**. Era el problema largo hasta 2021 retake; en 2022 y 2025 no ha salido como tal, pero las herramientas son las mismas que VF.
- **Hidrostática (Tema 5):** nunca como problema propio. Solo aparece dentro de otro: fuerza sobre un pistón en reposo (2017), fuerza y momento de la presión sobre una placa articulada (2025). Peso bajo, pero hay que saber integrar presión y momento.

## 3. Bloques y tiempos (unas 30 h en total)

| Bloque | Contenido | Peso en examen | Horas | Problemas prioritarios (en orden) |
| :--- | :--- | :--- | :--- | :--- |
| **C1** NS exacto en cilíndricas | Continuidad -> v_r, NS radial -> p, ODE en r^n, T con disipación | ~20 % | 5 h | NS13, NS8, NS2, NS14, NS4 (Couette con calor). Examen: 2021 retake |
| **C2** Análisis dimensional | Teorema Pi, límites (Re grande/pequeño), semejanza con tablas y curvas | ~25-30 % | 5 h | DA1, DA5 o DA9 (potencia, semejanza), DA12, DA4 (Stokes), DA3. Exámenes: 2025 corto, 2015 P3, 2014 P1 |
| **C3** VF I: flujos paralelos, no estacionarios y descargas | Poiseuille/Couette en canal y tubo, capa de Stokes, criterios, descargas cuasi estacionarias h(t) | ~25 % | 7 h | VF2, VF5, VF6, VF7, VF4, VF3. Exámenes: 2022 corto, 2016 P1, 2022 P1 |
| **C4** VF II: lubricación y películas delgadas | Ecuación de Reynolds, canal de altura variable, squeeze film, fuerzas, potencia y rendimiento | ~25 % | 7 h | VF16, VF8, VF12, VF11, VF15, VF18. Exámenes: 2021 P1, 2014 P2, 2017 |
| **C5** Hidrostática (ligero) | Fuerza y momento de presión sobre compuertas y placas | ~5 % | 2 h | FS10 (de clase), FS4, FS9 |
| **C6** Simulacros con tiempo | 70/30, 90 min, con Notes.pdf | - | 5 h | 2025 completo, 2022 completo, 2021 completo; si sobra, 2021 retake |

Si el tiempo aprieta, recorta en este orden: C5, luego los NS opcionales (NS2, NS14, NS4), luego VF3/VF4. No recortes C2 ni C6.

## 4. Ecuaciones de Notes.pdf que hay que tener localizadas

- Cap. 4: continuidad y NS incompresible en cartesianas y cilíndricas, ecuación de la energía, esfuerzos viscosos.
- Cap. 5: hidrostática (Eqs. 5.1-5.25).
- Cap. 6: teorema Pi y semejanza (Eqs. 6.1-6.59).
- Cap. 7: Couette y Poiseuille, capas de Stokes, películas esbeltas y efecto cuña, criterios 7.40/7.41 (Eqs. 7.1-7.76).

## 5. Convención de hilos

Un hilo por bloque (C1 ... C6). Cada hilo arranca con esta lista, va directo al primer problema y sigue el estilo guiado (paso a paso, término a término, un apartado por mensaje).
