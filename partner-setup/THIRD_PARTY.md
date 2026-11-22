# Third-party material in partner-setup

Most third-party tools are **not copied** into this repository: `install.py` downloads them from their authors (Claude plugin marketplaces, `npx skills add`, the Antigravity marketplace) or copies them from the partner's own Claude install. Only the items below are included in `payload/`, under their own licences.

| Item | Path in `payload/` | Author | Licence |
| :--- | :--- | :--- | :--- |
| task-observer ("One Skill to Rule Them All") v3.5.0 | `claude/skills/task-observer/` (unmodified copy); `gemini/plugins/skill-evolution/skills/task-observer/` (copy adapted for Antigravity: paths and line endings) | Eoghan Henn and contributors, https://github.com/rebelytics/one-skill-to-rule-them-all | CC BY 4.0, https://creativecommons.org/licenses/by/4.0/ |
| skill-creator | `gemini/plugins/skill-evolution/skills/skill-creator/` (licence text in its `LICENSE.txt`) | Anthropic | Apache-2.0 |
| humanizer v3.0.0 | `gemini/plugins/aerospace-study-workflows/skills/humanizer/` (same skill as `.claude/skills/humanizer/` in this repo) | Based on Wikipedia's "Signs of AI writing" guide, extended for this repo; the upstream author is not recorded in the skill | MIT (declared in its frontmatter). If the upstream author is identified, add their copyright line and the MIT text here |

Downloaded at install time, not stored here:

| Source | What |
| :--- | :--- |
| `obra/superpowers-marketplace` | superpowers (Claude plugin; its skills are copied into the Antigravity plugin on the partner's machine) |
| `thedotmack/claude-mem` | claude-mem (Claude plugin; four of its skills are copied into the Antigravity plugin on the partner's machine) |
| `DietrichGebert/ponytail` | ponytail (Claude plugin) |
| `anthropics/claude-plugins-official` | claude-code-setup, figma (Claude plugins) |
| `emilkowalski/skills`, `pbakaus/impeccable`, `Leonxlnx/taste-skill` | Design and animation skills, via `npx skills add` |
| `antigravity-plugins-official` | chrome-devtools-plugin (Antigravity) |

Never included: Anthropic's docx, pdf, pptx and xlsx skills (proprietary terms forbid redistribution), and anything personal (memory database, observation logs, account tokens).

Everything else in `payload/` (the skill router, the agent bridge, dual-agent-team, skill-evolution's wrapper scripts, aerospace-study-workflows, TEAM_PROTOCOL.md) was written for this repository.
