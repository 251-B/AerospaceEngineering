# Limpieza de skills, plugins, hooks y MCP (2026-11-22)

Plan para revisar juntos. **Nada se ha borrado todavía.**

## Decisiones tomadas (22-nov)

- `trader-*`: **borrar**.
- **Se conservan** (anula lo que dicen las tablas de abajo): `superpowers`, `task-observer`, `figma`, `dual-agent-team` y el puente con Gemini, y **todas** las skills de diseño y animación.
- `rea`: se quita el MCP y se mantiene la skill `reverse-engineer-anything`.
- **Siguen en la lista para borrar:** `bm`, `context-mode` (y su hook), `claude-code-setup`, el plugin `skill-creator` y todas las copias de `skill-creator` salvo la integrada, `humanizer@synced`, `headroom`, `graphify` y las copias globales de `aerospace-study-team`, de `claude-agents` y de los 5 agentes.
- Por tanto, la Fase 5 solo quita de `CLAUDE.md` y `AGENTS.md` las menciones a `bm`, `context-mode` y `headroom`. Las de `superpowers` y las skills de diseño se quedan.

## Cómo se ha medido

- Inventario de `~/.claude/settings.json`, `.claude/settings.json`, `installed_plugins.json`, `~/.claude/skills/`, `.claude/skills/`, `.claude/agents/`, `~/.claude.json` (MCP) y los `hooks.json` de cada plugin.
- Uso real: escaneo de **369 transcripciones** de todos los proyectos (`~/.claude/projects/*/*.jsonl`), contando llamadas a `Skill`, `Agent`, herramientas MCP y slash commands, con la fecha del último uso.

### Lo que se usa de verdad

| Qué | Llamadas | Último uso |
| :-- | --: | :-- |
| Browser integrado (`Claude_Browser`) | 407 | 21-nov |
| `playwright` (MCP) | 222 | 21-nov |
| `computer-use` | 163 | 22-nov |
| `/model` | 123 | 21-nov |
| `/ponytail` | 37 | 21-nov |
| `claude-mem` (búsqueda MCP) | 23 | 20-nov |
| Subagentes propios (`problem-step-mentor` 16, `source-researcher` 12, `web-qa-reviewer` 7, `task-runner` 2, `aerospace-pedagogue` 2) | 39 | 20-nov |
| `review-ultrareview` | 13 | 21-nov |
| `humanizer` | 8 | 22-nov |
| `reverse-engineer-anything` | 4 | 13-oct |
| `task-observer` | 3 | 14-nov |
| `impeccable`, `review-animations` | 2 + 2 | 21-nov |

### Lo que nunca se ha usado (0 llamadas en 369 sesiones)

`bm` (GSD, ~100 skills y 34 agentes), `superpowers` (14 skills), `context-mode` (1 llamada en total), `figma`, `claude-code-setup`, `skill-creator` (en ninguna de sus 4 copias), `graphify`, las 11 `trader-*`, `headroom` (MCP), `gemini-notebook` (MCP), `design-taste-frontend` y 12 de las 15 skills de animación/diseño.

## Problemas concretos encontrados (bugs, no gustos)

1. **`.claude/settings.local.json` es JSON inválido** (coma final en la línea 5). Tus permisos locales se ignoran.
2. **Cada plugin está instalado tres veces**: una a nivel usuario y dos a nivel proyecto con la ruta escrita `c:\` y `C:\` (mismo proyecto). Además están activados en `~/.claude/settings.json` y otra vez en `.claude/settings.json`.
3. **`skill-creator` existe en 4 sitios**: plugin oficial, `~/.claude/skills/`, `.claude/skills/` (+ copia `.agents/skills/`) y la skill integrada `anthropic-skills:skill-creator`.
4. **`humanizer` dos veces**: skill del proyecto y plugin `humanizer@synced`.
5. **`aerospace-study-team` y `claude-agents` duplicadas** en `~/.claude/skills/` (global) y en `.claude/skills/` (proyecto).
6. **MCP `rea` falla al conectar en cada sesión** (timeout 30 s) y solo se usó en octubre.
7. **Aviso de GSD desactualizado** en cada arranque (plugin de 59 días que no usas).
8. **Hook propio `context-mode-cache-heal.mjs`**: existe solo para parchear `context-mode`.
9. Restos: `plugins/cache/temp_git_*`, `installed_plugins.json.bak-20261009`.
10. **Apareció `~/.claude/skills/dual-agent-team` durante esta sesión**, lo instaló el puente de Gemini (`~/.gemini/config/plugins/agent-bridge`). Si no lo usas, es ruido.

## Coste del ruido

- **Hooks en cada llamada a herramienta**: `bm` registra 18 entradas (5 PreToolUse, 6 PostToolUse…), `context-mode` 13 (8 PreToolUse), `claude-mem` 9. Cada `Bash`/`Read` pasa por varios procesos de Node antes de ejecutarse.
- **Contexto al arrancar**: la lista de skills de esta sesión tiene ~260 entradas; `superpowers` inyecta su skill completa, `context-mode` un bloque de reglas, `claude-mem` 50 observaciones, `bm` el aviso. Todo eso se paga en tokens en cada sesión y empeora la elección de skill (más candidatas parecidas = más falsos positivos).

## Veredicto por componente

### Plugins

| Plugin | Veredicto | Motivo |
| :-- | :-- | :-- |
| `bm` (GSD) | **Eliminar** | 0 usos, 18 hooks, ~130 skills/agentes, aviso diario. Su flujo de fases (`.planning/`) no se usa en este repo. |
| `superpowers` | **Eliminar** | 0 invocaciones. Inyecta texto en cada sesión que obliga a invocar skills "con un 1 % de probabilidad", lo que choca con ponytail y con tus reglas. Lo útil (depuración sistemática, verificación antes de cerrar) ya está escrito en `AGENTS.md`. |
| `context-mode` | **Eliminar** | 1 uso en total, 13 hooks que interceptan cada Bash/Read y un hook propio para arreglarlo. Su función (no volcar salidas grandes) ya la cubren los subagentes `Explore`/`source-researcher` y tu regla de economía de tokens. |
| `figma` | **Eliminar** (o desactivar) | Instalado el 19-nov, 0 usos; el portal no parte de diseños Figma. Reinstalar es un comando. |
| `claude-code-setup` | **Eliminar** | Herramienta de una sola vez (recomendador), 0 usos. |
| `skill-creator` (plugin) | **Eliminar** | Ya tienes `anthropic-skills:skill-creator` integrada. |
| `humanizer@synced` | **Desactivar en el proyecto** | Duplica la skill `humanizer` del repo (la que tiene tu huella de voz). Quedarse con una. |
| `claude-mem` | **Mantener, vigilar** | 23 búsquedas y el resumen al arrancar sí te ha servido (sesiones de labs). Sus 22 skills sobran, pero vienen en el paquete. |
| `ponytail` | **Mantener** | Lo usas a diario (37 veces). |

### MCP

| Servidor | Veredicto | Motivo |
| :-- | :-- | :-- |
| `playwright` | **Mantener** | 222 usos; lo pide tu flujo de diseño (375/768/1440 px). |
| Browser integrado / `computer-use` | **Mantener** | Los más usados; no son configurables, vienen con la app. |
| `rea` | **Quitar de `~/.claude.json`** | Falla en cada arranque; reactivar solo cuando hagas ingeniería inversa. |
| `headroom` | **Quitar** | 0 usos; el proxy de compresión no se ha usado nunca. Quitar también la mención en `CLAUDE.md`. |
| `gemini-notebook`, Gmail, Drive, Calendar | **Revisar en claude.ai → Connectors** | Conectores de cuenta, no de este PC. Drive se usó 6 veces; NotebookLM y Calendar, 0. |

### Skills globales (`~/.claude/skills/`, se cargan en todos los proyectos)

| Skill | Veredicto |
| :-- | :-- |
| `trader-*` (11) | **Mover a un proyecto de trading** (o borrar). 0 usos, nada que ver con este repo y ocupan contexto en todas las sesiones. |
| `aerospace-study-team`, `claude-agents` | **Borrar la copia global**; ya están en el proyecto. |
| `skill-creator` | **Borrar** (duplicado). |
| `graphify` | **Borrar** salvo que la uses en otro repo (0 usos). Quitar el bloque de `~/.claude/CLAUDE.md`. |
| `reverse-engineer-anything` | **Mantener** si piensas repetir; si no, archivar junto con `rea`. |
| `dual-agent-team` | **Borrar** si no coordinas con Gemini (lo vuelve a instalar el puente; desactivar el puente en Gemini). |
| `impeccable`, `design-taste-frontend`, `emil-design-eng`, `animate`, `review-animations` | **Mantener**: son las que nombra tu flujo de diseño en `CLAUDE.md`. |
| `animate-expo`, `write-swift`, `ask-sonner`, `apple-design`, `pick-ui-library`, `prototype`, `learn-taste`, `ask-emil` | **Borrar**: React Native, Swift, librería React o de arranque de proyecto; el portal es HTML estático. |
| `animation-vocabulary`, `animation-performance`, `choreograph`, `gestures`, `mobile-native`, `break-ui`, `find-animation-opportunities`, `improve-animations`, `remove-animations` | **Reducir**: quedarse con 2–3 (propuesta: `mobile-native`, `break-ui`, `animation-performance`) y borrar el resto; `CLAUDE.md` nombra varias, habría que actualizar esa lista. |

### Skills del proyecto (`.claude/skills/` = `.agents/skills/`)

| Skill | Veredicto |
| :-- | :-- |
| `review-ultrareview` | **Mantener** (la más usada). |
| `humanizer` | **Mantener** (8 usos). |
| `aerospace-study-team` y `claude-agents` | **Fusionar en una** o borrar: 0 usos y repiten lo que ya dice `CLAUDE.md`/`AGENTS.md`. |
| `skill-creator` | **Borrar** (duplicado de la integrada). |
| `task-observer` | **Decidir**: 3 usos, pero su descripción exige invocarla antes de la primera herramienta de *cada* sesión. Si no revisas sus observaciones, borrar. |

### Subagentes (`.claude/agents/`)

Se usan todos menos con poca frecuencia `aerospace-pedagogue` (2). **Mantener los 6.** Las copias de 5 de ellos en `~/.claude/agents/` son **duplicados globales**: borrar o confirmar que son idénticas. `general-purpose` se usa 192 veces frente a 39 de los propios: tu tabla de enrutado por modelo se aplica poco.

## Plan de acción (por orden de riesgo, de menor a mayor)

**Fase 0 — Copia de seguridad** (1 min)
- Copiar `~/.claude/settings.json`, `~/.claude.json`, `~/.claude/skills/`, `~/.claude/agents/` y `installed_plugins.json` a una carpeta fechada.

**Fase 1 — Arreglos sin discusión**
1. Corregir la coma de `.claude/settings.local.json`.
2. Quitar los registros de plugins a nivel proyecto duplicados (`c:\` y `C:\`) con `/plugin` y dejar solo los de usuario.
3. Borrar `plugins/cache/temp_git_*` y el `.bak`.
4. Quitar `rea` y `headroom` de `~/.claude.json`.

**Fase 2 — Duplicados**
5. Borrar copias globales de `aerospace-study-team`, `claude-agents`, `skill-creator` y de los 5 agentes (tras comprobar que el proyecto tiene la versión buena).
6. Desinstalar el plugin `skill-creator`; borrar `skill-creator` de `.claude/skills/` y `.agents/skills/`.
7. Desactivar `humanizer@synced` en `.claude/settings.json`.

**Fase 3 — Plugins sin uso** (lo de mayor impacto en velocidad y contexto)
8. Desinstalar `bm`, `context-mode` (+ hook `context-mode-cache-heal.mjs`), `superpowers`, `claude-code-setup`, `figma`, y quitar sus marketplaces si quedan vacíos.

**Fase 4 — Skills globales**
9. Mover o borrar `trader-*`, `graphify`, `dual-agent-team` y las skills de diseño marcadas para borrar.

**Fase 5 — Documentación del repo** (commit y push)
10. Reescribir en `CLAUDE.md` el pipeline de 5 etapas y la matriz de decisión sin `superpowers`, `bm` ni `context-mode`; quitar `headroom`; actualizar la lista de skills de diseño y la de plugins de `.claude/settings.json`.
11. Igual en `AGENTS.md` (tabla Routing, "Token economy and memory") y en `vault/06 - Repository/`.
12. Actualizar `~/.claude/CLAUDE.md` (bloque `graphify`).

**Fase 6 — Verificación**
13. Abrir sesión nueva: sin avisos de GSD ni timeouts de `rea`; contar cuántas skills aparecen (objetivo: < 80 frente a ~260).
14. Pasar `python -m unittest discover -s tools/tests` y `audit_portal` para confirmar que ninguna herramienta del repo dependía de lo eliminado.

## Preguntas para decidir antes de ejecutar

1. ¿Las `trader-*` las usas en otro sitio (otra carpeta, otra máquina)? → moverlas o borrarlas.
2. ¿Quieres conservar `superpowers` por sus skills de proceso aunque no se invoquen, o fuera?
3. ¿`task-observer`: lo revisas o fuera?
4. ¿`figma`: lo vas a usar con algún enlace de diseño pronto?
5. ¿Coordinas con Gemini (`dual-agent-team`, puente) o se desactiva?

## Fuera de alcance / no comprobado

- Conectores de cuenta de claude.ai (Gmail, Drive, Calendar, NotebookLM, `anthropic-skills`, `adaptive-agent`, `claude-memory`): se gestionan desde la web, no desde este PC.
- Disco (caché de plugins): `claude-mem` 488 MB, `context-mode` 140 MB, `bm` 22 MB, `ponytail` 13 MB, oficiales 12 MB. Skills globales: `design-taste-frontend` 39 MB (sus checkers de Chrome), `impeccable` 2,4 MB. Las fases 3 y 4 liberan unos 165 MB; `claude-mem` puede tener versiones antiguas en caché que conviene purgar.
- Las transcripciones no registran cuántas veces una skill guio la respuesta sin invocarse, así que "0 usos" significa 0 invocaciones explícitas.
