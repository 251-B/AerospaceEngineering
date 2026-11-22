# Skill Evolution — Continuous Observation & Auto-Skill Creation

- **Pinned shared observation workspace (Antigravity + Claude Code):** `{{HOME}}/.agent-bridge/skill-observations/` (log dir: `{{HOME}}/.agent-bridge/skill-observations/observation-log/`).
- **Session start:** Invoke `task-observer` at the start of each main session (subagents skip it).
- **Helper script (Windows):** `python "{{HOME}}/.gemini/config/plugins/skill-evolution/scripts/new_observation.py" <kebab-slug> --title "..." --area "..." --context "..." [--skill s1,s2] [--proposes new-skill]`

## Behaviour during multi-step tasks and corrections

1. **Observe silently while working:** Watch for recurring user requests, explicit user corrections ("hazlo siempre así", "no hagas X, haz Y"), repeated multi-step procedures not yet captured by an existing skill, or gaps/friction in an active skill.
2. **Avoid duplicates:** Before logging a new observation, scan the YAML frontmatter headers in `{{HOME}}/.agent-bridge/skill-observations/observation-log/*.md`. If an open entry already captures the same pattern or `proposes_skill`, extend that entry instead of creating a duplicate.
3. **Log durable, generalisable patterns:** Create an entry using `new_observation.py` (following `task-observer` format: **Issue** -> **Suggested improvement** -> **Principle**). Do **not** log trivial one-off Q&A or ephemeral facts.
4. **Auto-create or evolve skills & register router rule:**
   - When the same pattern or `proposes_skill` candidate reaches **2 or more** occurrences/observations, OR when the user explicitly states a standing workflow ("siempre hago esto así", "cada vez que te pida X..."), proactively propose or draft the reusable skill using `skill-creator` + `writing-skills` conventions.
   - Save project-agnostic or domain skills inside the matching plugin under `{{HOME}}/.gemini/config/plugins/<domain>/skills/<skill-name>/SKILL.md` (or ask a single concise confirmation line first if the plugin destination or scope is ambiguous).
   - **Mandatory router rule:** Every newly installed or created skill MUST receive a matching rule in `~/.claude/skill_rules.json` (global) or `<repo>/.claude/skill_rules.json` (project) so it fires automatically in both Claude Code and Antigravity.
5. **Periodic review:** When the user asks for a review, or when `last-review-date.txt` is 7 or more days old and open observations exist, summarize the pending clusters concisely and offer to promote ready patterns into skills.
6. **Keep responses clean:** Add at most one brief end-of-response note—and only when an observation was actually logged or a recurring skill candidate reached the threshold to be turned into a skill.
