---
name: review-ultrareview
description: Protocolos obligatorios de verificación estándar (review) y auditoría adversarial exhaustiva (ultrareview) para el portal de estudio, notas de Obsidian y resoluciones de Aerospace Engineering. Asegura rigor matemático sin saltos algebraicos, enlaces relativos, KaTeX impecable, memoria persistente (claude-mem) y máxima eficiencia en el consumo de tokens y caché.
---

# Protocolos de Cierre de Tareas: Review y Ultrareview

Este documento establece las dos fases de control de calidad y auditoría que la IA debe ejecutar al concluir cualquier tarea en el repositorio `AerospaceEngineering`: **`review`** (verificación estándar por tarea unitaria) y **`ultrareview`** (auditoría adversarial profunda de módulos, capítulos o exámenes).

Además, define las directrices obligatorias de **eficiencia de tokens, aprovechamiento de prompt caching y persistencia en memoria** para evitar consumo innecesario de contexto.

---

## 1. Cuándo Invocar `review` vs. `ultrareview`

```
                      ¿Qué trabajo se ha finalizado?
                                    │
               ┌────────────────────┴────────────────────┐
               ▼                                         ▼
      [ Tarea Unitaria ]                       [ Hito Completo / Examen / Fin ]
   • 1 problema resuelto                    • Capítulo o tema entero
   • 1 sección teórica redactada            • Hoja de problemas completa
   • 1 página web maquetada                 • Refactorización o reorganización
   • 1 corrección de bug puntual            • Petición explícita ("ultrareview")
               │                                         │
               ▼                                         ▼
        Ejecutar REVIEW                        Ejecutar ULTRAREVIEW
    (Rápido, determinista)                 (Adversarial, 4 dimensiones)
```

---

## 2. Protocolo de `review` (Verificación Estándar)

Se ejecuta **automáticamente** al finalizar cualquier tarea unitaria. Coste estimado: mínimo (<300 tokens).

### Lista de Comprobación de `review`:
1. **Sintaxis KaTeX:**
   - Delimitadores matemáticos perfectamente balanceados: `$...$` para inline y `$$...$$` para bloques.
   - Sin barras de escape erróneas ni caracteres raw no procesados.
2. **Navegación y Enlaces Relativos:**
   - Todo enlace de retorno en páginas de `subjects/` apunta exactamente a `../../../index.html`.
   - Los wikilinks de Obsidian (`[[...]]`) coinciden exactamente con notas existentes.
3. **Estándar Lingüístico:**
   - 100% redactado en **English** académico (directriz UC3M).
4. **Metadatos y Frontmatter (Obsidian First):**
   - Encabezado YAML presente en `vault/` con `materia`, `tema`, `tags`, `dificultad` y `fuentes`.
5. **Persistencia Sintética en Memoria:**
   - Registrar una síntesis de 2 líneas en `claude-mem` (o MOC) con la solución o estructura completada.

---

## 3. Protocolo de `ultrareview` (Auditoría Adversarial Profunda)

Se ejecuta al cerrar un hito mayor (capítulo completo, hoja de problemas, examen oficial) o ante la instrucción explícita del usuario (`ultrareview` o `/ultrareview`).

Se realiza una auditoría cruzada multi-rol y adversarial en **4 dimensiones**:

### Dimensión 1: Rigor Matemático y Analítico (`problem-step-mentor` + `aerospace-pedagogue`)
- [ ] **Cero Saltos Algebraicos:** Cada simplificación, factorización, cancelación de términos y sustitución intermedia está explícitamente escrita.
- [ ] **Derivación Explícita:** Se muestra la regla de la cadena temporal paso a paso:
  $$\frac{d}{dt}f(u(t)) = \frac{\partial f}{\partial u}\frac{du}{dt}$$
- [ ] **Integración Exhaustiva:** Se explicita el cambio de variable con su diferencial ($du = u'(t)dt$), la primitiva intermedia y los límites evaluados por la Regla de Barrow:
  $$\int_{a}^{b} f(t)\,dt = [F(t)]_{a}^{b} = F(b) - F(a)$$
- [ ] **Matrices de Cambio de Base:** Si intervienen giros o marcos de referencia, la matriz $[{}_0 R_1]$ está deducida y se verifica su ortonormalidad ($\det R = 1$, $R R^T = I$).
- [ ] **Análisis Dimensional Homogéneo:** Cada sumando de cada ecuación se verifica en unidades del SI.
- [ ] **Comportamiento Asintótico y Límites Físicos:** Se evalúan los casos límite ($t \to 0$, $t \to \infty$, o ángulos extremos $\theta = 0, \pi/2$) para certificar la coherencia física.

### Dimensión 2: Trazabilidad y Cero Alucinaciones (`source-researcher`)
- [ ] Todas las fórmulas, ecuaciones maestras, hipótesis y datos numéricos se cotejan contra los PDFs originales de `sources/`.
- [ ] Cita explícita de la fuente oficial (ej. *Lecture Notes Topic 3, Slide 14*, *Robinson Eq. 4.8*).

### Dimensión 3: Integridad Frontend y Web (`web-qa-reviewer` + `subject-web-builder`)
- [ ] KaTeX CDN renderiza sin errores en consola ni fórmulas desbordadas.
- [ ] Dark/light toggle works through `assets/js/theme.js` with persistence in `localStorage('ae_theme')` (no inline theme code, no other theme key).
- [ ] Diseño responsive adaptado a móvil, tablet y escritorio.
- [ ] Insignia de estado actualizada en el `index.html` raíz.

### Dimensión 4: Eficiencia de Tokens, Memoria y Caché
- [ ] Eliminación de archivos temporales de depuración (`scratch/`, `.tmp`).
- [ ] Consolidación de memoria: guardar decisiones clave en `claude-mem` para que sesiones futuras no requieran releer cientos de líneas.

---

## 4. Directrices Obligatorias de Eficiencia de Tokens, Memoria y Caché

Para garantizar respuestas rápidas, costes mínimos y evitar desbordar la ventana de contexto:

### A. Maximizar el Prompt Caching
1. **Prefijos Estables:** Mantener invariantes las instrucciones y frontmatter de las skills. Nunca insertar timestamps, fechas dinámicas o textos cambiantes al inicio de los prompts de sistema.
2. **Reutilización de Definiciones:** Utilizar los roles definidos en `.claude/agents/` en lugar de redefinir system prompts completos en cada mensaje.

### B. Blindaje de Contexto (`Context Shielding`)
1. **Prohibido el Volcado Masivo:** Nunca ejecutar lecturas completas de múltiples PDFs o archivos de código grandes en el hilo principal del chat.
2. **Uso de `context-mode`:**
   - Usar `ctx_execute` (Node/Python/PowerShell) para filtrar, contar o extraer líneas exactas en un entorno sandbox antes de llevarlas al contexto.
   - Usar `ctx_search` para búsquedas semánticas o de palabras clave en los materiales de estudio.
3. **Lecturas Precisas:** Emplear `view_file` con `StartLine` y `EndLine` delimitados, o `grep_search` específico.

### C. Persistencia en Memoria (`claude-mem`)
1. **Evitar Re-Ingestas:** Una vez extraídas las fórmulas maestras o resuelto un problema, registrar un resumen denso en `claude-mem`.
2. Al iniciar o reanudar una sesión, consultar `claude-mem` para obtener el estado consolidado en <100 tokens, en lugar de releer 10.000 tokens de notas previas.

### D. Respuestas Concisas y Sin Duplicación
1. Si un archivo ya ha sido modificado o creado en disco (`vault/` o `subjects/`), **NO** copiar y pegar su contenido íntegro en el mensaje de respuesta.
2. Proporcionar un enlace Markdown clickeable ([ejemplo](file:///c:/Users/hecto/OneDrive/Documentos/GitHub/AerospaceEngineering/CLAUDE.md)), un resumen ejecutivo de las decisiones adoptadas y las pruebas de validación realizadas.
3. Mantener los equipos de agentes (Agent Teams) acotados a **3–5 compañeros**, con **5–6 tareas** por compañero, y ejecutar **apagado ordenado** (`Graceful Shutdown`) tan pronto terminen su labor.
