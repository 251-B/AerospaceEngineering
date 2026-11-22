#!/usr/bin/env python3
"""Antigravity PreInvocation adapter reusing ~/.claude/hooks/skill_router.py and its JSON tables.

Reads Antigravity's camelCase PreInvocation JSON payload from stdin, resolves the project's
.claude/skill_rules.json + global ~/.claude/skill_rules.json (single source of truth),
deduplicates per (conversationId, lastUserInput) so it injects at most once per user message,
translates Claude skill/agent identifiers to Antigravity equivalents, and emits valid
Antigravity PreInvocation JSON on stdout.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import re
import sys
import tempfile
from pathlib import Path

CLAUDE_ROUTER_PATH = Path.home() / ".claude" / "hooks" / "skill_router.py"
SEEN_PATH = Path.home() / ".agent-bridge" / "tmp" / "router_seen.json"
MAX_SEEN_KEYS = 200

_STRIP_PREFIXES = ("superpowers:", "anthropic-skills:", "claude-mem:", "figma:")
_CLAUDE_ONLY_SKILLS = {
    "headroom:headroom",
    "adaptive-agent:skill-review",
    "adaptive-agent:build-user-profile",
    "update-config",
    "simplify",
    "dataviz",
}
_SKILL_REMAP = {
    "code-review": "requesting-code-review",
    "schedule": "schedule (slash command /schedule or schedule tool)",
}


def _load_claude_router():
    spec = importlib.util.spec_from_file_location("claude_skill_router", str(CLAUDE_ROUTER_PATH))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {CLAUDE_ROUTER_PATH}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _find_project_dir(cwd: str, workspace_paths: list[str] | None) -> str | None:
    candidates: list[Path] = []
    for raw in [cwd, *(workspace_paths or [])]:
        if isinstance(raw, str) and raw.strip():
            candidates.append(Path(raw.strip()))
    for start in candidates:
        cur = start
        for candidate in [cur, *cur.parents]:
            if (candidate / ".claude" / "skill_rules.json").is_file():
                return str(candidate)
    return None


def _seen_key(conv_id: str, prompt: str) -> str:
    digest = hashlib.sha256(prompt.encode("utf-8", errors="replace")).hexdigest()
    return f"{conv_id or 'default'}:{digest}"


def _already_seen_and_mark(key: str, seen_file: Path = SEEN_PATH) -> bool:
    seen: list[str] = []
    if seen_file.is_file():
        try:
            raw = json.loads(seen_file.read_text(encoding="utf-8"))
            if isinstance(raw, list):
                seen = [str(x) for x in raw]
        except Exception:
            seen = []
    if key in seen:
        return True
    seen.append(key)
    if len(seen) > MAX_SEEN_KEYS:
        seen = seen[-MAX_SEEN_KEYS:]
    seen_file.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(dir=str(seen_file.parent), prefix=".router_seen.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(seen, fh)
        os.replace(tmp_name, seen_file)
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
    return False


def translate_hits(raw_hits: list[str], plain_prompt: str) -> tuple[list[str], list[str]]:
    hits = list(raw_hits)
    if not plain_prompt.lstrip().startswith("/") and re.search(r"\bclaude\b", plain_prompt):
        if "dual-agent-team" not in hits:
            hits.append("dual-agent-team")

    skills: list[str] = []
    agents: list[str] = []
    for h in hits:
        if h.startswith("agent:"):
            ag = h[6:].strip()
            if ag and ag not in agents:
                agents.append(ag)
            continue
        if h in _CLAUDE_ONLY_SKILLS:
            continue
        mapped = h
        for pref in _STRIP_PREFIXES:
            if mapped.startswith(pref):
                mapped = mapped[len(pref):]
                break
        mapped = _SKILL_REMAP.get(mapped, mapped)
        if mapped and mapped not in skills:
            skills.append(mapped)
    return skills, agents


def build_message(skills: list[str], agents: list[str]) -> str | None:
    parts: list[str] = []
    if skills:
        parts.append("activate skills: " + ", ".join(skills))
    if agents:
        parts.append("delegate to subagent: " + ", ".join(agents))
    if not parts:
        return None
    return (
        "Skill router: this prompt matches; "
        + "; ".join(parts)
        + ". Do it before acting, unless plainly irrelevant."
    )


def selftest() -> int:
    cr = _load_claude_router()
    repo_proj = r"{{REPO}}"
    if Path(repo_proj, ".claude", "skill_rules.json").is_file():
        os.environ["CLAUDE_PROJECT_DIR"] = repo_proj
    rules = cr.load_rules()
    assert len(rules) >= 40, f"Expected >=40 rules, got {len(rules)}"
    for r in rules:
        re.compile(r["match"])

    def eval_prompt(text: str) -> tuple[list[str], list[str]]:
        raw = cr.route(text, rules)
        return translate_hits(raw, cr.plain(text))

    s1, a1 = eval_prompt("La página da un error 404")
    assert "systematic-debugging" in s1, f"404 failed: {s1}"

    s2, _ = eval_prompt("Diseña una interfaz bonita para la home")
    assert "brainstorming" in s2 and "impeccable" in s2 and "design-taste-frontend" in s2, f"UI failed: {s2}"

    _, a3 = eval_prompt("Resuelve el problema 3 de la hoja")
    assert "problem-step-mentor" in a3, f"Problem failed: {a3}"

    _, a4 = eval_prompt("Explica la teoría del tema 4")
    assert "aerospace-pedagogue" in a4, f"Theory failed: {a4}"

    s5, _ = eval_prompt("Crea una nueva skill y evalúa su descripción")
    assert "skill-creator" in s5 and "writing-skills" in s5, f"Skill creation failed: {s5}"

    s6, _ = eval_prompt("Pide a Claude que revise este código")
    assert "dual-agent-team" in s6, f"Claude bridge trigger failed: {s6}"

    s7, a7 = eval_prompt("/review error 404")
    assert s7 == [] and a7 == [], f"Slash command not skipped: {s7}, {a7}"

    # Verify deduplication using a temporary file
    with tempfile.TemporaryDirectory() as td:
        tmp_seen = Path(td) / "seen.json"
        k = _seen_key("conv-1", "hola mundo")
        assert _already_seen_and_mark(k, tmp_seen) is False
        assert _already_seen_and_mark(k, tmp_seen) is True

    print(f"agy_skill_router selftest ok, {len(rules)} rules loaded and compiled")
    return 0


def main() -> None:
    if "--selftest" in sys.argv:
        raise SystemExit(selftest())

    try:
        raw_stdin = sys.stdin.buffer.read().decode("utf-8", "ignore")
        payload = json.loads(raw_stdin or "{}")
    except Exception:
        sys.stdout.write("{}")
        return

    try:
        prompt = str(payload.get("lastUserInput") or "")
        if not prompt.strip() or prompt.lstrip().startswith("/"):
            sys.stdout.write("{}")
            return

        conv_id = str(payload.get("conversationId") or "default")
        if _already_seen_and_mark(_seen_key(conv_id, prompt)):
            sys.stdout.write("{}")
            return

        proj = _find_project_dir(
            str(payload.get("cwd") or ""),
            payload.get("workspacePaths") if isinstance(payload.get("workspacePaths"), list) else [],
        )
        if proj:
            os.environ["CLAUDE_PROJECT_DIR"] = proj
        else:
            os.environ.pop("CLAUDE_PROJECT_DIR", None)

        cr = _load_claude_router()
        rules = cr.load_rules()
        raw_hits = cr.route(prompt, rules)
        skills, agents = translate_hits(raw_hits, cr.plain(prompt))
        msg = build_message(skills, agents)
        if not msg:
            sys.stdout.write("{}")
            return

        out = {
            "injectSteps": [
                {
                    "systemMessage": {
                        "systemMessage": msg
                    }
                }
            ]
        }
        sys.stdout.write(json.dumps(out, ensure_ascii=True))
    except Exception:
        sys.stdout.write("{}")


if __name__ == "__main__":
    main()
