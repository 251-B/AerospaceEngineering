# Prompts de arranque tras la limpieza de herramientas (2026-11-22)

Dos prompts para pegar tal cual. El primero, en una **sesión nueva de Claude Code** en este repo. El segundo, en **Antigravity**.

---

## 1. Sesión nueva de Claude Code (verificación)

```text
Verifica que la nueva configuración de herramientas funciona en esta sesión limpia. Contexto: el 22-nov hicimos una limpieza y montamos un router automático de skills; todo está en docs/plans/2026-11-22-tooling-cleanup.md y en la sección "Skill router and learning loop" de CLAUDE.md. No cambies nada fuera de lo que diga abajo.

1. Arranque: confirma que NO aparece el aviso de GSD ni el timeout del MCP "rea", y que SÍ llegó la nota "Learning loop (skill router)" del hook SessionStart. Invoca task-observer como dice esa nota y comprueba que su log queda en ~/.agent-bridge/skill-observations/ (y no en el repo).
2. Router: ejecuta `python ~/.claude/hooks/skill_router.py --selftest` con CLAUDE_PROJECT_DIR apuntando al repo (debe cargar 51 reglas) y prueba estos mensajes pasándolos por stdin como {"prompt": "..."}: "la página da un 404", "resuelve el problema 12 de mecánica", "anima el botón en el móvil", "hola". Los tres primeros deben dar nota y el último nada.
3. Inventario: `claude plugin list` debe mostrar solo superpowers, claude-mem, claude-code-setup, ponytail y figma. En ~/.claude.json los MCP deben ser solo playwright y antigravity-bridge. Cuenta las skills de la lista de sesión y compáralas con las ~260 de antes.
4. Limpieza pendiente: borra ~/.claude/plugins/cache/context-mode (la sesión anterior la tenía bloqueada).
5. Puente: llama a antigravity_status del MCP antigravity-bridge y dime si responde.
6. Repo: `python tools/vault_lint.py` y `python tools/audit_portal.py` a 0 errores.

Termina con una tabla OK/FALLA por punto. Si algo falla, arregla la causa (no el síntoma), vuelve a probar y haz commit y push solo de los archivos del repo que hayas tocado.
```

---

## 2. Antigravity (ponerse al día y copiar la configuración)

```text
Ponte al día de la reorganización de herramientas que hizo Claude Code el 22-nov-2026 y deja tu configuración equivalente a la suya, para que los dos trabajéis igual y el puente funcione bien. Lee primero, sin cambiar nada:

- AerospaceEngineering/docs/plans/2026-11-22-tooling-cleanup.md (decisiones y lo que se ejecutó)
- AerospaceEngineering/CLAUDE.md, sección "Skill router and learning loop" y la línea de task-observer
- ~/.claude/CLAUDE.md (reglas globales de Claude), ~/.claude/hooks/skill_router.py, ~/.claude/skill_rules.json (reglas globales) y AerospaceEngineering/.claude/skill_rules.json (reglas del proyecto)
- ~/.agent-bridge/TEAM_PROTOCOL.md

Criterio del dueño (obligatorio): conservar todas las herramientas útiles; cuando dos hacen lo mismo, quedarse con la más completa; y que TODO se active solo según el trabajo, sin que él tenga que acordarse de ninguna skill. Las skills que crean o mejoran skills deben ejecutarse automáticamente a medida que se aprende de él.

Después, haz esto y explícame cada cambio antes de aplicar los que borren algo:

1. Paridad de plugins con Claude. Claude quitó context-mode, bm/GSD, headroom (MCP), rea (MCP; la skill reverse-engineer-anything se mantiene y se conecta sola cuando hace falta), las skills trader-* y graphify. Quita o desactiva en ~/.gemini/config/plugins lo equivalente (context-mode; trading-research si contiene esas mismas skills de trading) y conserva lo que Claude conserva: superpowers, claude-mem (memoria compartida), figma, agent-bridge, las skills de diseño y animación, reverse-engineer-anything y aerospace-study-workflows. Si tienes duplicados entre tus plugins (por ejemplo skill-evolution frente a skill-creator, o ui-design-craft frente a las skills de diseño), quédate con la versión más completa y dime cuál y por qué.
2. Skill creator: Claude usa anthropic-skills:skill-creator y borró la copia de .agents/skills/skill-creator. Usa tu mejor equivalente (skill-evolution, si cubre crear, evaluar y mejorar skills) y apúntalo en GEMINI.md.
3. Aprendizaje compartido: task-observer tiene ahora UN solo log para los dos agentes en ~/.agent-bridge/skill-observations/ (ya copié ahí lo que había en ~/.gemini/skill-observations). Fija ahí el workspace de tu task-observer, ejecútalo al inicio de cada sesión principal y, cuando toque revisión, propón skills nuevas o mejoradas; cada skill nueva debe recibir una regla en el skill_rules.json correspondiente.
4. Activación automática: monta tu equivalente del router de Claude. Si Antigravity tiene hooks al enviar un mensaje, reutiliza el mismo script (python ~/.claude/hooks/skill_router.py, con el JSON {"prompt": ...} por stdin) y las mismas dos tablas de reglas, traduciendo los nombres de skill o agente a los tuyos. Si no tiene hooks, crea una regla o workflow global de Antigravity que lea esas tablas y aplique las skills al empezar cada tarea. No dupliques las reglas: las dos tablas JSON son la única fuente.
5. Skills del proyecto: .agents/skills debe quedar idéntica a .claude/skills (aerospace-study-team, claude-agents, humanizer, review-ultrareview) más task-observer, que en Claude ahora vive en ~/.claude/skills. Comprueba con un diff que coinciden.
6. Puente: comprueba los dos sentidos (claude_status desde ti y antigravity_status desde Claude), escribe un bridge_handoff con el resumen de lo que has cambiado y guarda en claude-mem una observación corta (menos de 100 tokens) con las decisiones.
7. Si tocas archivos del repo, sigue AGENTS.md: solo tus archivos, commit tipo "chore(gemini): ..." y push a main.

Termina con una tabla de paridad Claude ↔ Antigravity (plugins, MCP, skills, hooks/reglas, memoria, log de task-observer) marcando OK o diferencia y su motivo.
```
