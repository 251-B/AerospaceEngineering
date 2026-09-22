---
name: aerospace-study-team
description: >-
  Orquestación del equipo de 5 subagentes especializados y gestión de la bóveda de Obsidian para el portal de estudio de 2º de Ingeniería Aeroespacial.
---

# Equipo de Estudio de Ingeniería Aeroespacial (Subagentes)

Esta habilidad permite al agente orquestador coordinar el desarrollo de material docente, ejercicios, simuladores y páginas web de las 5 materias de 2º curso.

## Subagentes Disponibles

1. **`notebook_researcher`**: Ingesta y consulta de cuadernos NotebookLM vía MCP (`gemini-notebook`). Extrae temario, fórmulas y problemas.
2. **`aerospace_pedagogue`**: Razonamiento analítico profundo (`pro`). Redacta teoría rigurosa y resuelve problemas paso a paso en LaTeX.
3. **`simulator_engineer`**: Crea simuladores y widgets interactivos (Canvas 2D, SVG, Chart.js).
4. **`subject_web_builder`**: Implementa páginas web en `subjects/` con KaTeX, temas oscuro/claro y diseño responsive.
5. **`web_qa_reviewer`**: Audita enlaces relativos, valida sintaxis de fórmulas LaTeX y evita conflictos de Git.

## Bóveda de Obsidian (`vault/`)
* **Ubicación:** `AerospaceEngineering/vault/`
* **Notas MOC:** Consultar `vault/00 - Indice Central/Indice Maestro.md` para navegar por la jerarquía.
* **Plantillas:** En `vault/Templates/` para conceptos, problemas de examen y formularios.
