"""Skill router: makes installed skills, plugins and agents fire without being remembered.

Hooks (registered in ~/.claude/settings.json):
  UserPromptSubmit  -> python skill_router.py            (match the prompt against the rules)
  SessionStart      -> python skill_router.py --session  (start the learning loop)

Rules are data, merged from two files (project rules first):
  $CLAUDE_PROJECT_DIR/.claude/skill_rules.json   project-specific (committed with the repo)
  ~/.claude/skill_rules.json                     global, every project
Each rule: {"match": "<regex on the prompt, lower-case, accents removed>", "use": ["skill" | "agent:name"]}.
A prompt that matches nothing gets nothing, so ordinary prompts cost no tokens.
"""
import json
import os
import re
import sys
import unicodedata

HOME_RULES = os.path.join(os.path.expanduser("~"), ".claude", "skill_rules.json")
MAX_HITS = 5

SESSION_NOTE = (
    "Learning loop (skill router): in the main session, invoke the task-observer skill before your "
    "first tool call; subagents skip it. Its workspace is pinned to ~/.agent-bridge/skill-observations/ "
    "(one log shared by every project and by Antigravity). Run adaptive-agent:skill-review when task-observer says a review is due. When task-observer finds a repeated pattern, a correction "
    "from the user or a review that is due, propose the skill or the change to an existing skill; "
    "build it with anthropic-skills:skill-creator (and superpowers:writing-skills), then add a rule "
    "for it to skill_rules.json (project rules in <repo>/.claude/skill_rules.json, the rest in "
    "~/.claude/skill_rules.json) so it fires automatically from then on. "
    "When a prompt names a skill in a 'Skill router' note, invoke it before acting unless it is "
    "plainly irrelevant; if two match, run the process skill (debugging, brainstorming, plans) first."
)


def plain(text):
    text = unicodedata.normalize("NFKD", text.lower())
    return "".join(c for c in text if not unicodedata.combining(c))


def load_rules():
    files = []
    proj = os.environ.get("CLAUDE_PROJECT_DIR")
    if proj:
        files.append(os.path.join(proj, ".claude", "skill_rules.json"))
    files.append(HOME_RULES)
    rules = []
    for f in files:
        try:
            with open(f, encoding="utf-8") as fh:
                rules += json.load(fh).get("rules", [])
        except (OSError, ValueError):
            continue  # a missing or broken rules file must never block the prompt
    return rules


def route(prompt, rules):
    p = plain(prompt)
    if p.lstrip().startswith("/"):
        return []  # an explicit slash command already chose its skill
    hits = []
    for r in rules:
        try:
            if re.search(r["match"], p):
                hits += [u for u in r["use"] if u not in hits]
        except (re.error, KeyError, TypeError):
            continue
    return hits[:MAX_HITS]


def note(hits):
    skills = [h for h in hits if not h.startswith("agent:")]
    agents = [h[6:] for h in hits if h.startswith("agent:")]
    parts = []
    if skills:
        parts.append("invoke with the Skill tool: " + ", ".join(skills))
    if agents:
        parts.append("delegate to the subagent: " + ", ".join(agents))
    return "Skill router: this prompt matches; " + "; ".join(parts) + ". Do it before acting, unless plainly irrelevant."


def emit(event, text):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": text}}))


def selftest():
    rules = [{"match": r"\b(error|404)\b", "use": ["superpowers:systematic-debugging"]},
             {"match": r"\bdisena\b", "use": ["superpowers:brainstorming", "agent:subject-web-builder"]}]
    assert route("La página da un 404", rules) == ["superpowers:systematic-debugging"]
    assert route("Diseña una página", rules) == ["superpowers:brainstorming", "agent:subject-web-builder"]
    assert route("/review error", rules) == []
    assert route("Resuelve el problema 3", rules) == []
    assert "subagent: subject-web-builder" in note(route("Diseña", rules))
    assert route("x", [{"match": "(", "use": ["bad"]}]) == []  # broken regex is skipped
    for r in load_rules():
        re.compile(r["match"])
    print("selftest ok,", len(load_rules()), "rules loaded")


def main():
    if "--selftest" in sys.argv:
        return selftest()
    if "--session" in sys.argv:
        return emit("SessionStart", SESSION_NOTE)
    try:
        data = json.loads(sys.stdin.buffer.read().decode("utf-8", "ignore") or "{}")
    except ValueError:
        return
    hits = route(data.get("prompt", ""), load_rules())
    if hits:
        emit("UserPromptSubmit", note(hits))


if __name__ == "__main__":
    main()
