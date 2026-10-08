---
name: aerospace-study-team
description: >-
  Orquestación del equipo de 5 subagentes especializados, protocolos de cierre (review/ultrareview), gestión de la bóveda de Obsidian y optimización estricta de tokens, memoria y caché para 2º de Grado en Ingeniería Aeroespacial UC3M.
---

# Equipo de Estudio de Ingeniería Aeroespacial (Subagentes, Agent Teams y Auditoría)

Esta habilidad coordina el desarrollo de material docente, teoría analítica, resolución exhaustiva de problemas paso a paso y páginas web de las materias activas de 2º curso bajo directrices estrictas de rigor y economía de tokens.

---

## 1. Subagentes y Roles Especializados (`.claude/agents/`)

1. **`source-researcher`**: Ingesta y consulta de fuentes oficiales locales (`sources/`). Extrae temario, fórmulas y problemas sin inventar datos.
2. **`aerospace-pedagogue`**: Razonamiento analítico profundo (`pro` / `opus`). Redacta teoría rigurosa desde primeros principios en inglés.
3. **`problem-step-mentor`**: Mentor Pedagógico de Problemas (`pro` / `opus`). Garantiza desarrollo exhaustivo paso a paso según la metodología de 4 fases:
   - Justificación pedagógica previa de cada ecuación o principio.
   - Matrices de cambio de base $[{}_0 R_1]$ y sistemas de coordenadas.
   - Cálculo explícito de derivadas (regla de la cadena temporal, implícitas) e integrales (sustitución, diferencial, Barrow) sin saltos algebraicos.
   - Verificación dimensional en unidades SI y casos límite.
4. **`subject-web-builder`**: Implementa páginas web en `subjects/` con KaTeX, temas oscuro/claro persistente (`localStorage('ae_theme')`) y notas en `vault/`.
5. **`web-qa-reviewer`**: Audita enlaces relativos (`../../../index.html`), valida sintaxis KaTeX y controla la calidad.

---

## 2. Bóveda de Obsidian (`vault/`) y Portal Web (`subjects/`)

* **Estrategia Dual (Obsidian First):** Toda materia debe documentarse **primero** en Obsidian (`vault/`) con YAML frontmatter y `[[Wikilinks]]`, y posteriormente maquetarse en la web (`subjects/`).
* **Notas MOC:** Consultar [Indice Maestro.md](file:///c:/Users/hecto/OneDrive/Documentos/GitHub/AerospaceEngineering/vault/00%20-%20Indice%20Central/Indice%20Maestro.md) para la navegación jerárquica.
* **Plantillas:** Ubicadas en `vault/Templates/`.

---

## 3. Protocolos de Cierre Obligatorios: `review` y `ultrareview`

Al finalizar cualquier actividad, se debe ejecutar el protocolo correspondiente:

* **`review` (Cierre de Tarea Unitaria):**
  - Verificación estándar: sintaxis KaTeX ($...$ y $$...$$), enlaces de retorno `../../../index.html`, idioma estricto en inglés y frontmatter YAML completo.
* **`ultrareview` (Cierre de Hito, Capítulo, Hoja de Problemas o Examen):**
  - Auditoría adversarial profunda en 4 dimensiones:
    1. *Rigor analítico:* Cero saltos algebraicos, derivadas e integrales desarrolladas paso a paso, comprobación dimensional de cada término en unidades SI.
    2. *Trazabilidad:* Cero alucinaciones con cita exacta a fuentes oficiales (`sources/`).
    3. *Frontend:* Comprobación de renderizado KaTeX y persistencia dark/light theme.
    4. *Memoria:* Síntesis compacta de fórmulas y decisiones guardada en `claude-mem`.

Consulta la skill [review-ultrareview](file:///c:/Users/hecto/OneDrive/Documentos/GitHub/AerospaceEngineering/.claude/skills/review-ultrareview/SKILL.md) para la lista completa de comprobación.

---

## 4. Eficiencia de Tokens, Memoria y Optimización de Caché

1. **Prompt Caching:** Instrucciones estables y estructuradas sin prefijos dinámicos volátiles.
2. **Blindaje de Contexto (`Context Shielding`):**
   - Prohibido volcar PDFs completos al chat.
   - Emplear `context-mode` (`ctx_execute`, `ctx_search`) para consultar y filtrar archivos en sandbox.
3. **Persistencia en Memoria (`claude-mem`):**
   - Guardar hallazgos y decisiones clave de diseño en `claude-mem` para que no sea necesario releer documentos enteros en sesiones futuras.
4. **Respuestas Concisas:**
   - No reproducir en el chat el contenido íntegro de notas o páginas HTML ya escritas en disco. Usar enlaces markdown, diffs y síntesis analítica.
