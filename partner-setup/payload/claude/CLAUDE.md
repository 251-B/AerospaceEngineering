# Automatic tool use (every project)
- The owner does not want to remember skills, plugins, agents or MCP servers: they must fire on their own as the work comes up.
- `~/.claude/hooks/skill_router.py` (hooks `UserPromptSubmit` and `SessionStart` in `~/.claude/settings.json`) adds a "Skill router" note naming the skills or subagents that match the prompt. Invoke them before acting unless plainly irrelevant; process skills (debugging, brainstorming, plans) first.
- Rules: `~/.claude/skill_rules.json` (global) and `<repo>/.claude/skill_rules.json` (project). Every skill installed or created gets a rule there; a skill with `disable-model-invocation: true` gets `false` or no rule.
- Learning loop: `task-observer` at the start of each main session, workspace pinned to `~/.agent-bridge/skill-observations/` (shared with Antigravity); `adaptive-agent:skill-review` when a review is due; its proposals are built with `anthropic-skills:skill-creator` + `superpowers:writing-skills`, then routed. `learn-taste` turns design corrections into rules.

## Dual-Agent Team (Antigravity Bridge)
- Paired with **Antigravity** via MCP `antigravity-bridge` (`antigravity_delegate`, `antigravity_status`, `bridge_handoff`) and shared `claude-mem`.
- Read `~/.agent-bridge/TEAM_PROTOCOL.md` or use skill `dual-agent-team` before multi-agent delegation, cross-review, parallel `git worktree` work, or quota failover.
- Default to `mode="read_only"` for audits/analysis; never edit the same files concurrently without `git worktree`, and never loop back if `status == "quota_exceeded"`.

