---
trigger: always_on
---
# Dual-Agent Team (Antigravity <-> Claude Code)

Estás emparejado con **Claude Code** a través del servidor MCP `claude-bridge` (`claude_delegate`, `claude_status`, `bridge_handoff`) y compartís memoria persistente en `claude-mem` (`~/.claude-mem/claude-mem.db`).

- Consulta `~/.agent-bridge/TEAM_PROTOCOL.md` o activa la skill `dual-agent-team` cuando vayas a repartir tareas entre modelos (`fast`/`worker`/`reviewer`/`architect`), hacer revisión cruzada, trabajar en paralelo con `git worktree` o relevar una sesión por límite de cuota.
- Usa `mode="read_only"` por defecto al delegar análisis o auditorías; usa `mode="edit"` solo en subtareas acotadas y nunca edites los mismos archivos que Claude simultáneamente sin `git worktree`.
- Si `claude_delegate` devuelve `status: "quota_exceeded"`, no reintentes en bucle: continúa localmente o guarda el estado con `bridge_handoff`.
