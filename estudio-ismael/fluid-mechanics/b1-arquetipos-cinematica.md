# B1 Cinemática: problemas arquetipo para el hilo socrático

Hecho el 2026-10-31. Fuentes revisadas: enunciados de `vault/01 - Fluid Mechanics/Problem - K1..K10.md`, `FLUIDS_FIRSTPARTIAL_2011..2025.pdf` (2013_QUIZ y 2014_QUIZ leídos como imagen). NotebookLM no se pudo consultar (el conector `gemini-notebook` falla en este entorno), así que la selección no está cruzada con `[PROGRESO TEORÍA - BLOQUE 1]`.

## Lista ordenada (de más sencillo a más completo)

1. **K2 Couette plano.** Flujo estacionario y unidireccional: corriente = trayectoria, vorticidad, circulación en un rectángulo, tensor gradiente, tensor de deformación, **direcciones y velocidades principales de deformación** (autovalores), evolución de un elemento cuadrado.
2. **Parcial 2025, Short Questions Ej. 1 (Couette).** Mismo flujo que K2: **flujos convectivos de masa, cantidad de movimiento y energía cinética** a través de una sección + explicarlo en palabras. Pregunta real de Parte 1.
3. **K10 = QUIZ 2013 (es el mismo enunciado).** Campo cartesiano lineal con amplitud que crece en el tiempo: dilatación, **condición de irrotacionalidad para hallar B**, corriente en un instante, trayectoria (integrar con t), potencial y función de corriente, tensor de deformación, deformación pura de un cuadrado.
4. **K1 Pared porosa oscilante.** Arquetipo **no estacionario**: trayectoria distinta de línea de corriente, línea fluida, caudal Q(t) a través de un plano y su promedio, caudal saliente de una esfera (divergencia), circulación en un cuadrado directa y por Stokes.
5. **QUIZ 2014 (polares).** Todo el paquete en **coordenadas polares**: puntos de remanso, divergencia y rotacional en polares, corriente, trayectoria, línea fluida, potencial, función de corriente, **aceleración (a_r, a_θ)**, circulación a lo largo de una recta. No tiene nota en el vault; el PDF trae respuestas a mano parciales.
6. **K9 Flujo polar oscilante.** Polares **no estacionario**: aceleración con término local, existencia de potencial y función de corriente, línea fluida en θ = 0.
7. **K4 Cuerpo de Rankine.** **Superposición** (corriente uniforme + fuente) a partir de un potencial: velocidades en cartesianas y polares, línea de corriente divisoria, puntos de remanso y flujo local cerca de ellos.
8. **K6 Vórtice de Burgers + Parcial 2024 Ej. 2 (tornado).** **3D cilíndricas**: condición de incompresibilidad, corriente y trayectorias en 3D; tornado: circulación con datos numéricos, comprobar irrotacionalidad y usar Bernoulli entre líneas de corriente (Bernoulli se ve formalmente en T3; aquí solo se aplica).
9. **Parcial 2024 Ej. 1, apartado 1 (capa límite).** Mini-cálculo de Parte 1: **obtener v_y con la continuidad** dado v_x. Los apartados 2-3 (esfuerzos viscosos en la pared) van a B4.

## Descartados por equivalentes (reserva)

- **K7** (remanso hiperbólico lineal): mismo arquetipo que K10 y el QUIZ 2014.
- **K5** (dipolo oscilante): mismo arquetipo que K9 (dipolo polar no estacionario); usar solo si sobra tiempo para practicar aceleración de una partícula concreta.
- **K8** (potencial 3D pulsante) y **K3** (fuente 3D, observador móvil, superficies fluidas): nunca han caído en un parcial; extensión opcional. K3 es el único que trabaja el cambio de observador.

## Fuera de B1

Parcial 2021 Ej. 2 (∇·τ' = μ∇²v) y 2022 Ej. 2 (ecuación de T_m) son de NS y energía: B4/B5/B6. El resto de los parciales 2011-2025 son problemas CL o NS.
