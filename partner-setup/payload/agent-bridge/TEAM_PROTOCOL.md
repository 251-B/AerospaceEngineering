# Protocolo de Equipo Dual: Antigravity ↔ Claude Code

Manual operativo compartido entre **Antigravity (Gemini)** y **Claude Code (Claude)** en esta máquina. Ambos agentes comparten memoria persistente (`claude-mem`), canal de relevo (`~/.agent-bridge/handoff.json`), contadores de uso (`~/.agent-bridge/state.json`), las tablas de auto-activación (`~/.claude/skill_rules.json` + `<repo>/.claude/skill_rules.json`) y el log compartido de `task-observer` (`~/.agent-bridge/skill-observations/`).

---

## 1. Jerarquía de Modelos y Enrutado Basado en Benchmarks (Nov 2026)

Lineup activo: **Gemini 4 Hydrogen & Neon** (Antigravity) + **Claude Haiku 5.5, Sonnet 5.5 & Opus 5.5** (Claude Code). Quedan descartados `gemini-3.8-flash` y `argon`.

| Rol (`role`) | Antigravity (`agy`) | Claude Code (`claude`) | Cuándo usarlo (evidencia de benchmarks) |
| :--- | :--- | :--- | :--- |
| **`architect`** | `gemini-4-neon-high` *(opcional `xhigh`)* | `opus` (`high`) | **Neon**: diseño UI/UX, matemáticas/STEM (RiemannBench 84%), PDFs multimodales e ingesta barata de 1M tokens (caché -95%). **Opus 5.5**: sesiones largas (20+ turnos), refactors complejos y arquitectura crítica. |
| **`reviewer`** | `gemini-4-neon-high` | `opus` (`high`) | **Revisión cruzada**: auditar `git diff` y derivaciones del otro agente (`mode="read_only"`). Neutraliza el exceso de confianza de Gemini y los puntos ciegos de Claude. |
| **`worker`** | `gemini-4-hydrogen-high` | `sonnet` (`medium`) | **Enjambre de implementación paralela**: **Hydrogen `high`** es el punto dulce para swarms/código multiarchivo (-24% cuota, -19% tiempo); **Sonnet 5.5 `medium`** lidera Terminal-Bench 4.0 (70.6%) en CLI, PRs, tests y redacción (GDPval-AA 1,844 Elo). *Evitar `Sonnet max` por defecto* (dispara tokens de salida). |
| **`fast`** | `gemini-4-hydrogen-medium` | `haiku` (`medium`) | **Exploración y micro-tareas atómicas** (1–2 pasos, búsqueda, logs, extracción, checks): **Haiku `medium`** (<100k tokens) cuesta ~20x menos con precisión equivalente a Sonnet en tareas cerradas; **Hydrogen `medium`** digiere contexto largo barato. |

### Regla del Reintento Cero
- **Nunca uses `low` para generar o editar código multiarchivo.** Un subagente barato que falla o se detiene pronto y obliga al orquestador caro a corregir su diff cuesta más tokens y tiempo que asignar `Hydrogen high` o `Sonnet medium` a la primera.
- Pasa a cada subagente **solo los 2–5 archivos relevantes** (y mantén los prompts de Haiku <100k tokens; por encima de 100k su tarifa sube 5x).
- Todo subagente que edita código debe ejecutar un check determinista (test, lint o build) antes de cerrar.

---

## 2. Reglas de Delegación y Revisión Cruzada

1. **Modo seguro por defecto (`mode="read_only"`):**
   - Toda consulta, análisis, planificación o auditoría cruzada se delega en `read_only` (`plan`).
   - Usa `mode="edit"` solo cuando delegues una implementación concreta con archivos/objetivo bien acotados.
2. **Patrón Implementador + Auditor Cruzado:**
   - Un agente implementa la solución (o parte de ella) y el otro la audita en `read_only` con `role="reviewer"`.
3. **Trabajo en paralelo sin pisarse:**
   - Nunca hagas que ambos agentes editen los mismos archivos simultáneamente en la misma copia de trabajo. Si van a implementar en paralelo, aísla cada rama con `git worktree` (skill `using-git-worktrees`).
4. **Regla anti-bucle (`AGENT_BRIDGE_DEPTH`):**
   - El puente limita la delegación a **1 salto** (`max_recursion_depth = 1`). El agente delegado ejecuta su subtarea y devuelve el resultado directamente; nunca vuelve a llamar al agente llamador.
5. **Tiempo límite y respuesta vacía:**
   - Delega siempre con `timeout_sec` ≥ 300 (el valor por defecto del puente). Claude Code tarda más de 90 s en arrancar en frío (plugins, hook `SessionStart`, `claude-mem`): el 22-nov una delegación con 90 s acabó en timeout.
   - Un `status: ok` con `response` vacía no es un éxito: comprueba en disco si el delegado hizo el trabajo antes de darlo por hecho. En modo sin pantalla `agy` no tiene `--mode auto` en esta cuenta (vuelve al modo por defecto) y una tarea con comandos o MCP puede terminar sin hacer nada; no la reintentes en bucle.

---

## 3. Gestión de Cuotas y Relevo Automático (Failover)

1. **Consulta previa antes de bloques grandes:**
   - Antes de delegar una tarea pesada, consulta `claude_status` (desde Antigravity) o `antigravity_status` (desde Claude) para ver el consumo del día y si alguno está en cooldown.
2. **Ante `status: "quota_exceeded"`:**
   - El puente registra automáticamente un cooldown (45 min por defecto) en `~/.agent-bridge/state.json`.
   - **Prohibido reintentar en bucle.** El agente activo asume el trabajo restante localmente o guarda el contexto con `bridge_handoff(action="write", ...)` para continuar en el otro cliente sin perder el hilo.
3. **Relevo manual entre sesiones:**
   - Guarda estado con `bridge_handoff(action="write", summary=..., completed=..., next_steps=..., files_touched=..., write_project_md=True)`.
   - En el otro cliente: *"Lee el último handoff con `bridge_handoff` / `mem-search` y continúa desde ahí"*.

---

## 4. Memoria y Aprendizaje Compartido

- **Memoria (`claude-mem`):** ambos clientes comparten `~/.claude-mem/claude-mem.db`. Guarda hitos verificados en <100 tokens.
- **Observaciones (`task-observer`):** ambos escriben y revisan en **`~/.agent-bridge/skill-observations/`**. Toda skill nueva que nazca de una observación debe recibir su regla en `~/.claude/skill_rules.json` (global) o `<repo>/.claude/skill_rules.json` (proyecto).

---

## 5. Actualización de Benchmarks y Modelos

Cuando salgan modelos nuevos o quieras recalibrar el enrutado:
1. Lista los modelos reales disponibles con `agy models` (y `claude --help` / modelos de Claude).
2. Busca benchmarks independientes actualizados (Artificial Analysis, Terminal-Bench, SWE-bench / SWE-sweep, costes por nivel de esfuerzo) y consenso real en desarrollo.
3. Propón y aplica el diff en `~/.agent-bridge/config.json` y en la tabla de la Sección 1 de este archivo.
