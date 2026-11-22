---
name: dual-agent-team
description: Orchestrate collaborative work between Antigravity (Gemini) and Claude Code via the bidirectional MCP bridge (claude-bridge / antigravity-bridge), shared claude-mem SQLite memory, cross-review, git worktrees, benchmark-driven model routing, and quota failover/handoff. Use when splitting tasks across models, requesting cross-agent review, checking quota/cooldown status, updating model benchmarks, or handing off work between Antigravity and Claude Code.
---

# Dual-Agent Team Playbook (Antigravity ↔ Claude Code)

Usa este protocolo para coordinar trabajo entre **Antigravity** y **Claude Code** como un único equipo jerárquico, aprovechando los puntos fuertes medidos de **Gemini 4 Neon / Hydrogen** y **Claude Opus 5.5 / Sonnet 5.5 / Haiku 5.5**, y repartiendo carga para no agotar un solo límite de suscripción.

Manual completo en `~/.agent-bridge/TEAM_PROTOCOL.md`.

---

## 1. Herramientas disponibles según el lado desde el que trabajes

- **Desde Antigravity (`claude-bridge`):**
  - `claude_status()` → disponibilidad de Claude y `agy`, cooldowns activos, telemetría diaria y último handoff.
  - `claude_delegate(prompt, cwd, role, model, effort, mode, session_id, timeout_sec)` → delegar una subtarea a Claude Code (`role`: `fast` | `worker` | `reviewer` | `architect`; `mode`: `read_only` | `edit` | `auto`).
  - `bridge_handoff(action, ...)` → leer (`"read"`) o guardar (`"write"`) el relevo compartido en `~/.agent-bridge/handoff.json` (y opcionalmente `.agents/HANDOFF.md`).
- **Desde Claude Code (`antigravity-bridge`):**
  - `antigravity_status()` → versión/modelos de `agy`, cooldowns, telemetría diaria y último handoff.
  - `antigravity_delegate(prompt, cwd, role, model, effort, mode, conversation_id, timeout_sec)` → delegar una subtarea a Antigravity (`agy`).
  - `bridge_handoff(action, ...)` → el mismo buzón compartido de relevo.

---

## 2. Enrutado óptimo por rol (Regla del Reintento Cero)

Configurado en `~/.agent-bridge/config.json` (sin `gemini-3.8-flash` ni `argon`, y sin `low` para generar código):

- **`architect`** (`gemini-4-neon-high` / `opus high`):
  - Usa **Neon** para UI/UX frontend, matemáticas/STEM, PDFs multimodales y lectura/planificación barata de repos de 1M tokens (caché -95%).
  - Usa **Opus 5.5** para sesiones largas (20+ turnos), arquitectura crítica y código legado complejo.
- **`reviewer`** (`gemini-4-neon-high` / `opus high`, siempre `mode="read_only"`):
  - **Revisión cruzada**: audita el `git diff` o las derivaciones del otro agente (el auditor es el proveedor distinto al que implementó).
- **`worker`** (`gemini-4-hydrogen-high` / `sonnet medium`):
  - **Implementación paralela**: **Hydrogen `high`** es el punto dulce para swarms/código multiarchivo; **Sonnet 5.5 `medium`** lidera ejecución en terminal/CLI, PRs, tests y redacción profesional. Evita `Sonnet max` por defecto.
- **`fast`** (`gemini-4-hydrogen-medium` / `haiku medium`):
  - **Solo lectura, búsqueda y micro-tareas atómicas** (1–2 pasos). Mantén los prompts de Haiku **<100k tokens** (por encima sube 5x su coste). Nunca asignes tareas abiertas multiarchivo a `fast`.

---

## 3. Reglas de coordinación

1. **Comprueba estado antes de bloques grandes:** llama a `claude_status` o `antigravity_status`. Si un proveedor está en cooldown (`quota_limited_until`), no le delegues carga pesada.
2. **Contexto mínimo + verificación obligatoria:** pasa a cada subagente solo los 2–5 archivos necesarios y exige un check determinista (test, lint o build) antes de responder.
3. **Aislamiento de escritura:** usa `mode="read_only"` por defecto. Si ambos vais a editar código a la vez en el mismo repo, aísla cada uno en un `git worktree` (`using-git-worktrees`) y pasa el `cwd` del worktree al delegado.
4. **Reanudación de sesiones largas:** reutiliza `session_id` (Claude) o `conversation_id` (Antigravity) para evitar reenviar todo el contexto.
5. **Cero bucles:** `AGENT_BRIDGE_DEPTH` corta cualquier re-delegación recursiva.
6. **Failover limpio ante `quota_exceeded`:** NO reintentes en bucle. Asume el resto en local o guarda relevo con `bridge_handoff(action="write", ..., write_project_md=True)` + resumen <100 tokens en `claude-mem`.
7. **Resultado `empty` o sin efectos:** un `status: "empty"` del puente no es un éxito. Lee `denied_actions` y `stderr`, no reintentes en bucle (como mucho una vez, cambiando el modo o los permisos) y, tras delegar una edición, comprueba en disco que el cambio existe antes de darlo por hecho (`TEAM_PROTOCOL.md`, sección 2, punto 5).
8. **Desinstalar o purgar algo compartido:** antes de borrar un plugin, una caché o un MCP, busca su ruta en la configuración del otro agente (solo archivos de configuración, nunca sus conversaciones) y lista los procesos cuya línea de comandos la usa. Enseña ambas cosas al usuario y decide por agente: una ruta de instalación es una dependencia de todos los agentes que la lanzan.

---

## 4. Actualización de benchmarks y modelos

Cuando salgan modelos nuevos:
1. Comprueba modelos reales (`agy models` y modelos activos de Claude).
2. Busca benchmarks actualizados (Artificial Analysis, Terminal-Bench, SWE-bench/SWE-sweep, costes por nivel de esfuerzo) y opinión de desarrollo.
3. Actualiza `~/.agent-bridge/config.json` y `~/.agent-bridge/TEAM_PROTOCOL.md` (más ambas copias de esta skill).
