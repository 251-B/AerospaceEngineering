---
name: claude-agents
description: Orquestación avanzada de subagentes y equipos de agentes (Agent Teams) en Claude Code para Aerospace Engineering. Úsalo para coordinar tareas paralelas, debates analíticos, ingesta de fuentes oficiales locales, desarrollo pedagógico, resolución de problemas paso a paso sin saltos algebraicos, y ejecución de auditorías de cierre (review / ultrareview) con estricta economía de tokens y caché.
---

# Orquestación de Equipos y Agentes en Claude Code (Aerospace Engineering)

Esta skill define la guía operativa y los estándares para coordinar múltiples instancias y subagentes de Claude Code en el repositorio `AerospaceEngineering`. Permite estructurar flujos de trabajo paralelos, debates analíticos, revisión exhaustiva, ejecución de la arquitectura dual (Obsidian Vault + Portal Web), y auditorías de cierre (`review` y `ultrareview`) con máxima eficiencia en el consumo de tokens y optimización de caché.

---

## 1. Subagentes vs. Equipos de Agentes (Agent Teams)

Antes de lanzar compañeros de equipo, selecciona la arquitectura adecuada según la naturaleza del trabajo:

| Criterio | Subagentes (`Subagents`) | Equipos de Agentes (`Agent Teams`) |
| :--- | :--- | :--- |
| **Contexto** | Ventana propia; el resultado final retorna al llamador | Ventana propia independiente; se comunican entre sí |
| **Comunicación** | Devuelven un resumen al agente principal | Envío directo de mensajes punto a punto (`SendMessage`) |
| **Coordinación** | Gestionada centralmente por el líder | Auto-coordinación y lista de tareas compartida (`TaskCreate`, `TaskUpdate`) |
| **Consumo Tokens** | Menor (solo el resumen entra al hilo principal) | Mayor (múltiples sesiones completas concurrentes) |
| **Casos Ideales** | Consultas puntuales, lecturas de PDFs en `sources/`, cálculos acotados | Debates con hipótesis competidoras, módulos independientes en paralelo, revisión cruzada QA |

* **Regla de decisión:**
  - Usa **Subagentes** para tareas enfocadas donde solo importa el informe final (ej. `source-researcher` extrayendo las ecuaciones de un PDF).
  - Usa **Agent Teams** cuando los compañeros deban colaborar activamente, cuestionar hipótesis o desarrollar simultáneamente teoría y problemas sin pisar archivos comunes.

---

## 2. Requisitos y Configuración del Entorno

Los equipos de agentes requieren habilitación explícita en `.claude/settings.json` a nivel de proyecto:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  },
  "teammateMode": "in-process"
}
```

* **Modos de visualización (`teammateMode`):**
  - `"in-process"` (predeterminado): Todos los agentes corren en la terminal principal. Navega con flechas `Arriba`/`Abajo`, pulsa `Enter` para inspeccionar la transcripción de un compañero y hablarle directamente. `Esc` para volver.
  - `"auto"` / `"tmux"`: Habilita paneles divididos si estás en una sesión de tmux o iTerm2.

---

## 3. Catálogo de Roles Especializados (`.claude/agents/`)

En este repositorio existen 5 roles clave definidos en `.claude/agents/*.md`, reutilizables como subagentes o compañeros de equipo:

1. **`source-researcher`**:
   - **Misión:** Documentalista e ingestor de fuentes oficiales locales (`sources/`).
   - **Permisos:** Solo lectura (`Read`, `Grep`, `Glob`).
   - **Salida:** Enunciados exactos, fórmulas en KaTeX, condiciones de contorno y datos numéricos sin alucinaciones.

2. **`aerospace-pedagogue`**:
   - **Misión:** Ingeniero Aeroespacial & Pedagogo Mayor (Modelo `opus` o `sonnet` con alto esfuerzo).
   - **Permisos:** Solo lectura / razonamiento profundo.
   - **Salida:** Deducción de ecuaciones desde primeros principios con trazabilidad a fuentes oficiales y explicaciones analíticas en inglés.

3. **`problem-step-mentor`**:
   - **Misión:** Mentor Pedagógico de Problemas & Auditor de Rigor Analítico.
   - **Metodología Obligatoria de 4 Fases:**
     1. Planteamiento físico/matemático, grados de libertad, ligaduras e hipótesis.
     2. Sistemas de coordenadas, bases vectoriales ($\mathcal{B}_0, \mathcal{B}_C$) y matrices de cambio de base $[{}_0 R_1]$.
     3. Desarrollo algebraico y cálculo paso a paso sin omisiones. Justificación previa de cada fórmula. Derivadas explícitas (regla de la cadena) e integrales completas (cambio de variable, diferencial, Barrow).
     4. Interpretación física, órdenes de magnitud y verificación dimensional en unidades SI.

4. **`subject-web-builder`**:
   - **Misión:** Desarrollador Frontend del Portal (`subjects/`) y Bóveda Obsidian (`vault/`).
   - **Herramientas:** Edición y creación (`Read`, `Write`, `Edit`, `Glob`, `Grep`).
   - **Estándares:** KaTeX CDN, modo oscuro/claro con `localStorage('ae_theme')`, enlace estricto de retorno `../../../index.html`, diseño responsive.

5. **`web-qa-reviewer`**:
   - **Misión:** Auditor de Calidad, Revisor Técnico y Git Manager.
   - **Herramientas:** Lectura, ejecución y edición.
   - **Auditoría:** Enlaces relativos, balance de delimitadores KaTeX ($...$ y $$...$$), ausencia de simuladores innecesarios, integridad de insignias en `index.html`.

---

## 4. Protocolo de Spawning y Asignación de Tareas

### A. Sintaxis de Generación
Para invocar compañeros de equipo basados en las definiciones del proyecto, especifica el rol, el modelo y el alcance:

```text
Spawn 3 teammates to analyze Chapter 4 of Advanced Maths:
- One teammate using the source-researcher agent type to index all PDE problems in sources/cuatrimestre-1/04-advanced-maths/.
- One teammate using the aerospace-pedagogue agent type to structure the analytical theory.
- One teammate using the problem-step-mentor agent type to draft the step-by-step resolution.
Have them populate the shared task list and coordinate findings.
```

### B. Tamaño de Equipo y Granularidad de Tareas
- Mantener equipos estrictamente entre **3 y 5 compañeros** para evitar explosión de tokens.
- Desglosar el trabajo en unidades autocontenidas de **5 a 6 tareas por compañero**.
- Cada tarea debe tener un entregable claro (ej. una nota de Obsidian, un problema resuelto, una página web validada).

### C. Aislamiento de Archivos para Evitar Conflictos
- **Regla estricta:** Ningún par de compañeros debe editar el mismo archivo simultáneamente.
- Asignar dominios de trabajo separados:
  - Agente A: `vault/04 - Advanced Maths/`
  - Agente B: `subjects/04-advanced-maths/teoria/`
  - Agente C: `subjects/04-advanced-maths/problemas/`

---

## 5. Comunicación y Puertas de Calidad (Quality Gates)

1. **Mensajería entre Agentes:**
   - Los compañeros usan `SendMessage` para transferir hipótesis, validar resultados o alertar de inconsistencias.
   - Si un revisor detecta un salto algebraico o una fórmula sin justificar, envía un mensaje al autor requiriendo el desglose explícito antes de dar por cerrada la tarea.

2. **Fase de Planificación Previa (`Plan Mode`):**
   - Para tareas complejas o refactorizaciones de gran calado, inicia la sesión en modo de planificación para que los compañeros generen su plan antes de modificar código o contenido.

3. **Apagado Ordenado Inmediato (`Graceful Shutdown`):**
   - Una vez completadas todas las tareas de la lista compartida y validadas por `web-qa-reviewer`, solicita al líder el apagado ordenado de cada compañero por su nombre para detener de inmediato el consumo de tokens:
     ```text
     Ask the source-researcher teammate to shut down.
     ```

---

## 6. Flujo de Trabajo en Aerospace Engineering: Obsidian First → Web Second

1. **Fase 1 (Ingesta y Bóveda):**
   `source-researcher` y `aerospace-pedagogue` estructuran primero las notas en `vault/<asignatura>/` usando las plantillas de `vault/Templates/` y actualizan los MOCs.
2. **Fase 2 (Resolución de Problemas):**
   `problem-step-mentor` desarrolla las soluciones completas paso a paso en inglés, asegurando la metodología de 4 fases y KaTeX impecable.
3. **Fase 3 (Construcción Web):**
   `subject-web-builder` genera las páginas en `subjects/<asignatura>/teoria/` y `problemas/` consumiendo la bóveda consolidada como única fuente de verdad.
4. **Fase 4 (Auditoría de Cierre):**
   Ejecutar `review` (tareas unitarias) o `ultrareview` (hitos completos) antes de consolidar los cambios.

---

## 7. Motor de Detección Automática y Sinergia con Plugins

El orquestador no espera órdenes manuales sobre qué plugin o rol invocar. Aplica la siguiente matriz de detección sobre el prompt del usuario:

| Intención Detectada | Plugin Involucrado | Rol / Subagente Activado | Acción Automática |
| :--- | :--- | :--- | :--- |
| **Nuevo módulo / Refactorización** | `superpowers:brainstorming` + `bm:plan-phase` | `aerospace-pedagogue` | Cuestionamiento socrático y diseño de arquitectura antes de tocar código. |
| **Fallo de renderizado / Bug KaTeX / Enlace roto** | `superpowers:systematic-debugging` | `web-qa-reviewer` | Reproducción, hipótesis falsificable, arreglo de causa raíz y test de verificación. |
| **Inspección de múltiples archivos o logs** | `context-mode` (`ctx_execute`, `ctx_search`) | `source-researcher` | Ejecución en sandbox para parsear y resumir sin saturar la ventana de contexto. |
| **Desarrollo de problemas o exámenes** | Ninguno (Rigor analítico puro) | `problem-step-mentor` | Desglose estricto en 4 fases, derivadas e integrales explícitas en KaTeX. |
| **Hitos de larga duración / Sprints temáticos** | `bm` (`/bm:plan-phase`, `/bm:execute-phase`) | Agent Teams (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) | Lanzamiento coordinado de 3–5 compañeros con lista de tareas compartida. |
| **Cierre de tarea puntual** | `review-ultrareview` (Modo: `review`) | `web-qa-reviewer` | Checklist rápido: KaTeX delimitadores, link `../../../index.html`, idioma y YAML. |
| **Cierre de capítulo o examen** | `review-ultrareview` (Modo: `ultrareview`) | Equipo Completo (Adversarial) | Auditoría 4D: comprobación algebraica sin saltos, Barrow, SI, fuentes oficiales. |
| **Diseño o ajuste de nuevas skills** | `skill-creator` + `superpowers:writing-skills` | Meta-skill | Pruebas de disparo con `run_eval.py` y optimización con `improve_description.py`. |
| **Continuidad entre sesiones** | `claude-mem` | Auto-Memory | Recuperación de decisiones previas y estado consolidado de la asignatura. |

---

## 8. Protocolos de Cierre Obligatorios: `review` y `ultrareview`

Cada compañero de equipo y el líder deben someter los entregables a la auditoría correspondiente:

* **`review` (Por tarea unitaria):**
  - Delimitadores KaTeX (`$...$` y `$$...$$`) balanceados.
  - Enlace de retorno `../../../index.html` verificado.
  - Idioma estrictamente en inglés.
  - Frontmatter YAML en Obsidian completo.
* **`ultrareview` (Por capítulo, tema, hoja o examen completo):**
  - **Dimensión 1 (Matemática):** Ningún paso omitido. Regla de la cadena temporal explícita $\frac{d}{dt}f(u) = \frac{df}{du}\dot{u}$, integrales con diferencial explícita y límites de Barrow calculados. Matriz $[{}_0 R_1]$ con ortonormalidad verificada. Análisis dimensional SI de cada término. Casos límite evaluados.
  - **Dimensión 2 (Fuentes Oficiales):** Concordancia estricta con PDFs de `sources/`. Cero alucinaciones.
  - **Dimensión 3 (Frontend):** Sin errores en consola KaTeX, tema oscuro/claro persistente (`localStorage('ae_theme')`).
  - **Dimensión 4 (Memoria y Token Economy):** Registro de fórmulas maestras en `claude-mem` y eliminación de archivos temporales.

---

## 9. Directrices de Eficiencia de Tokens, Memoria y Optimización de Caché

1. **Prompt Caching Invariable:** Las directivas de sistema y encabezados de agentes deben permanecer idénticos entre llamadas para reutilizar el caché de prefijo de la API. Prohibido insertar timestamps o datos dinámicos en los prefijos.
2. **Context Shielding (`context-mode`):** Nunca volcar contenidos masivos de PDFs o logs a la conversación. Emplear `ctx_execute` para procesar y filtrar datos en sandbox.
3. **Persistencia en Memoria (`claude-mem`):** Almacenar decisiones consolidadas en `claude-mem` para que al reanudar sesiones se carguen en <100 tokens, evitando releer transcripciones enteras.
4. **Respuestas Concisas:** No duplicar en la respuesta de texto el contenido íntegro de los archivos guardados en disco. Compartir enlaces markdown, resúmenes de cambios y pruebas de verificación.
