---
subject: "Repository"
tags:
  - repository
  - rules
source: "CLAUDE.md"
---

# Rules - CLAUDE.md

## Scope

`CLAUDE.md` at the repository root, read by Claude Code. It imports `AGENTS.md` with an `@AGENTS.md` line, so the shared rules apply too, and it adds the Claude-specific framework and settings.

## Sections

Claude Code operating framework (triggering pipeline and decision matrix) and Claude Code specifics.

## Operative rules

- The five-stage pipeline runs before any edit: classify the request, check memory and context, route to a plugin or agent, close with the gate, then store the key findings.
- The decision matrix maps trigger words (errors, new pages, theory, problem sets, web styling, reviews, skills) to a workflow, a role and an expected deliverable.
- The closing gate is REVIEW for a single task and ULTRAREVIEW for a milestone or exam.
- Subagents live in `.claude/agents/`. Delegate when a task matches a role, and work directly when it is small.
- Agent teams have 3 to 5 members with 5 to 6 tasks each, and are shut down as soon as they finish.
- `.claude/settings.json` enables agent teams and the plugins superpowers, skill-creator, bm, context-mode, claude-mem, humanizer and claude-code-setup.
- Instructions to use `define_subagent` or `manage_subagents` belong to the Gemini setup and are ignored here.
- An optional, per-machine token-compression proxy is described. It is not part of the gate.
- The `task-observer` skill is bundled in `.claude/skills/` and `.agents/skills/`, and both copies must match.

## Related

[[Agent - aerospace-pedagogue]] · [[Agent - problem-step-mentor]] · [[Agent - source-researcher]] · [[Agent - subject-web-builder]] · [[Agent - web-qa-reviewer]] · [[Rules - AGENTS.md]] · [[Rules - GEMINI.md]] · [[Tool - vault_lint]] · [[Tool - audit_portal]] · [[Repository MOC]]
