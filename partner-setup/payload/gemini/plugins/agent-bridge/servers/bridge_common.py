"""Shared helpers for Antigravity <-> Claude Code MCP bridge servers."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

BRIDGE_HOME = Path.home() / ".agent-bridge"
CONFIG_PATH = BRIDGE_HOME / "config.json"
STATE_PATH = BRIDGE_HOME / "state.json"
HANDOFF_PATH = BRIDGE_HOME / "handoff.json"
TMP_DIR = BRIDGE_HOME / "tmp"

DEFAULT_CONFIG: dict[str, Any] = {
    "max_recursion_depth": 1,
    "quota_cooldown_minutes": 45,
    "default_timeout_sec": 300,
    "claude": {
        "executable": str(Path.home() / ".local" / "bin" / "claude.exe"),
        "roles": {
            "fast": {"model": "haiku", "effort": "low"},
            "worker": {"model": "sonnet", "effort": "medium"},
            "reviewer": {"model": "opus", "effort": "high"},
            "architect": {"model": "opus", "effort": "high"},
        },
    },
    "antigravity": {
        "executable": str(
            Path(os.environ.get("LOCALAPPDATA", str(Path.home() / "AppData" / "Local")))
            / "agy"
            / "bin"
            / "agy.exe"
        ),
        "roles": {
            "fast": {"model": "", "effort": "low"},
            "worker": {"model": "", "effort": "medium"},
            "reviewer": {"model": "", "effort": "high"},
            "architect": {"model": "", "effort": "high"},
        },
    },
}

_QUOTA_PATTERNS = [
    re.compile(p, re.IGNORECASE)
    for p in (
        r"rate.?limit",
        r"usage.?limit",
        r"hit your limit",
        r"quota",
        r"\b429\b",
        r"too many requests",
        r"overloaded",
        r"capacity",
        r"credit.?exhausted",
        r"out of credits",
        r"resets at",
    )
]


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def utc_now_iso() -> str:
    return utc_now().replace(microsecond=0).isoformat().replace("+00:00", "Z")


def today_utc_str() -> str:
    return utc_now().strftime("%Y-%m-%d")


def _atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(dir=str(path.parent), prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def load_config() -> dict[str, Any]:
    cfg = json.loads(json.dumps(DEFAULT_CONFIG))
    if CONFIG_PATH.is_file():
        try:
            with CONFIG_PATH.open("r", encoding="utf-8") as f:
                user_cfg = json.load(f)
            if isinstance(user_cfg, dict):
                for k in ("max_recursion_depth", "quota_cooldown_minutes", "default_timeout_sec"):
                    if k in user_cfg:
                        cfg[k] = user_cfg[k]
                for prov in ("claude", "antigravity"):
                    if isinstance(user_cfg.get(prov), dict):
                        if "executable" in user_cfg[prov]:
                            cfg[prov]["executable"] = user_cfg[prov]["executable"]
                        if isinstance(user_cfg[prov].get("roles"), dict):
                            cfg[prov]["roles"].update(user_cfg[prov]["roles"])
        except Exception as exc:
            print(f"[agent-bridge] warning: failed reading {CONFIG_PATH}: {exc}", file=sys.stderr)
    return cfg


def _empty_provider_state(date_str: str) -> dict[str, Any]:
    return {
        "date": date_str,
        "calls": 0,
        "errors": 0,
        "quota_hits": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "total_tokens": 0,
        "last_call_at": "",
        "last_role": "",
        "last_model": "",
        "last_error": "",
        "quota_limited_until": "",
    }


def load_state() -> dict[str, Any]:
    today = today_utc_str()
    state: dict[str, Any] = {
        "claude": _empty_provider_state(today),
        "antigravity": _empty_provider_state(today),
    }
    if STATE_PATH.is_file():
        try:
            with STATE_PATH.open("r", encoding="utf-8") as f:
                raw = json.load(f)
            if isinstance(raw, dict):
                for prov in ("claude", "antigravity"):
                    p = raw.get(prov)
                    if isinstance(p, dict):
                        merged = _empty_provider_state(today)
                        if p.get("date") == today:
                            merged.update(p)
                        else:
                            # Reset daily counters on date rollover while preserving active cooldown/last_error
                            merged["last_call_at"] = p.get("last_call_at", "")
                            merged["last_error"] = p.get("last_error", "")
                            merged["quota_limited_until"] = p.get("quota_limited_until", "")
                        state[prov] = merged
        except Exception as exc:
            print(f"[agent-bridge] warning: failed reading {STATE_PATH}: {exc}", file=sys.stderr)
    return state


def _extract_tokens(usage: dict[str, Any] | None) -> tuple[int, int, int]:
    if not isinstance(usage, dict):
        return 0, 0, 0
    inp = int(usage.get("input_tokens") or 0)
    inp += int(usage.get("cache_read_input_tokens") or usage.get("cache_read_tokens") or 0)
    inp += int(usage.get("cache_creation_input_tokens") or 0)
    out = int(usage.get("output_tokens") or 0) + int(usage.get("thinking_tokens") or 0)
    tot = int(usage.get("total_tokens") or (inp + out))
    return inp, out, tot


def record_call(
    provider: str,
    role: str,
    model: str,
    status: str,
    usage_dict: dict[str, Any] | None = None,
    error_msg: str = "",
) -> dict[str, Any]:
    cfg = load_config()
    state = load_state()
    ps = state.setdefault(provider, _empty_provider_state(today_utc_str()))
    ps["calls"] = int(ps.get("calls", 0)) + 1
    ps["last_call_at"] = utc_now_iso()
    ps["last_role"] = role
    ps["last_model"] = model

    inp, out, tot = _extract_tokens(usage_dict)
    ps["input_tokens"] = int(ps.get("input_tokens", 0)) + inp
    ps["output_tokens"] = int(ps.get("output_tokens", 0)) + out
    ps["total_tokens"] = int(ps.get("total_tokens", 0)) + tot

    if status == "quota_exceeded":
        ps["errors"] = int(ps.get("errors", 0)) + 1
        ps["quota_hits"] = int(ps.get("quota_hits", 0)) + 1
        ps["last_error"] = error_msg[:500]
        cooldown_mins = int(cfg.get("quota_cooldown_minutes", 45))
        until = utc_now() + timedelta(minutes=cooldown_mins)
        ps["quota_limited_until"] = until.replace(microsecond=0).isoformat().replace("+00:00", "Z")
    elif status != "ok":
        ps["errors"] = int(ps.get("errors", 0)) + 1
        ps["last_error"] = error_msg[:500]
    else:
        ps["last_error"] = ""
        ps["quota_limited_until"] = ""

    _atomic_write_json(STATE_PATH, state)
    return ps


def is_in_cooldown(provider: str) -> tuple[bool, int, str]:
    state = load_state()
    until_iso = str(state.get(provider, {}).get("quota_limited_until") or "").strip()
    if not until_iso:
        return False, 0, ""
    try:
        until_dt = datetime.fromisoformat(until_iso.replace("Z", "+00:00"))
        now = utc_now()
        if until_dt > now:
            remaining = max(1, int((until_dt - now).total_seconds() // 60) + 1)
            return True, remaining, until_iso
    except ValueError:
        pass
    return False, 0, ""


def detect_quota_error(text: str) -> bool:
    if not text:
        return False
    return any(p.search(text) for p in _QUOTA_PATTERNS)


def extract_warnings(stderr_text: str) -> list[str]:
    """Extract unique warning or permission-denial lines from subprocess stderr."""
    if not stderr_text:
        return []
    markers = ("warning:", "jetski:", "auto-denied", "not available", "denied")
    seen: list[str] = []
    for raw_line in stderr_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        low = line.lower()
        if any(m in low for m in markers) and line not in seen:
            seen.append(line)
            if len(seen) >= 10:
                break
    return seen


def model_has_effort_suffix(model_name: str) -> bool:
    """Return True if a model slug already encodes a thinking/effort tier suffix."""
    return bool(re.search(r"-(low|medium|high|xhigh|max)$", (model_name or "").strip(), re.IGNORECASE))


def summarize_empty_error(
    provider: str,
    denials: list[Any] | None,
    warnings: list[str],
    stderr_txt: str,
) -> str:
    """Build a concise error description for an empty headless response."""
    parts: list[str] = []
    if denials:
        actions: list[str] = []
        for item in denials:
            if isinstance(item, dict):
                act = str(item.get("action") or item.get("tool_name") or item.get("display_name") or "").strip()
                if act:
                    actions.append(act)
            elif item:
                actions.append(str(item))
        if actions:
            parts.append(f"denied actions: {', '.join(actions)}")
    if warnings:
        parts.append(" | ".join(warnings[:3]))
    elif stderr_txt:
        parts.append(stderr_txt[:300])
    if not parts:
        return f"Empty response returned by {provider}"
    return f"Empty response returned by {provider} ({'; '.join(parts)})"


def check_recursion_guard() -> tuple[bool, int, int]:
    cfg = load_config()
    max_depth = int(cfg.get("max_recursion_depth", 1))
    try:
        depth = int(os.environ.get("AGENT_BRIDGE_DEPTH", "0"))
    except ValueError:
        depth = 0
    return depth < max_depth, depth, max_depth


def child_env(provider: str) -> dict[str, str]:
    env = os.environ.copy()
    try:
        depth = int(env.get("AGENT_BRIDGE_DEPTH", "0"))
    except ValueError:
        depth = 0
    env["AGENT_BRIDGE_DEPTH"] = str(depth + 1)
    if provider == "claude":
        # Allow Antigravity (or nested bridge invocation up to max_recursion_depth)
        # without tripping Claude Code's nested terminal guard; AGENT_BRIDGE_DEPTH governs loops.
        env.pop("CLAUDECODE", None)
    return env


def resolve_executable(configured_path: str, fallback_cmd: str) -> str | None:
    if configured_path and os.path.isfile(configured_path):
        return configured_path
    found = shutil.which(fallback_cmd)
    if found and os.path.isfile(found):
        return found
    return None


def parse_last_json_object(stdout_text: str) -> dict[str, Any] | None:
    text = (stdout_text or "").strip()
    if not text:
        return None
    try:
        parsed = json.loads(text)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass

    # Fallback: scan lines from the end for a standalone JSON object or trailing block
    lines = text.splitlines()
    for idx in range(len(lines) - 1, -1, -1):
        line = lines[idx].strip()
        if line.startswith("{"):
            candidate = "\n".join(lines[idx:]).strip()
            try:
                parsed = json.loads(candidate)
                if isinstance(parsed, dict):
                    return parsed
            except json.JSONDecodeError:
                try:
                    parsed = json.loads(line)
                    if isinstance(parsed, dict):
                        return parsed
                except json.JSONDecodeError:
                    continue
    return None


def subprocess_creation_flags() -> int:
    if sys.platform == "win32":
        return getattr(subprocess, "CREATE_NO_WINDOW", 0)
    return 0


def handoff_read() -> dict[str, Any]:
    if not HANDOFF_PATH.is_file():
        return {"exists": False, "message": "No active handoff recorded yet."}
    try:
        with HANDOFF_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            data.setdefault("exists", True)
            return data
    except Exception as exc:
        return {"exists": False, "error": f"Failed reading handoff: {exc}"}
    return {"exists": False, "message": "Empty handoff file."}


def handoff_write(
    project_cwd: str,
    from_agent: str,
    summary: str,
    completed: str,
    next_steps: str,
    files_touched: str,
    blocker_or_reason: str,
    write_project_md: bool = False,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "exists": True,
        "updated_at": utc_now_iso(),
        "from_agent": from_agent,
        "project_cwd": project_cwd,
        "summary": summary,
        "completed": completed,
        "next_steps": next_steps,
        "files_touched": files_touched,
        "blocker_or_reason": blocker_or_reason,
    }
    _atomic_write_json(HANDOFF_PATH, payload)

    project_md_path = ""
    if write_project_md and project_cwd and os.path.isdir(project_cwd):
        md_dir = Path(project_cwd) / ".agents"
        md_dir.mkdir(parents=True, exist_ok=True)
        md_file = md_dir / "HANDOFF.md"
        md_body = (
            "# Dual-Agent Handoff\n\n"
            f"- **Updated:** {payload['updated_at']}\n"
            f"- **From:** {from_agent}\n"
            f"- **Workspace:** `{project_cwd}`\n"
            f"- **Reason / Blocker:** {blocker_or_reason or 'Manual handoff'}\n\n"
            f"## Summary\n{summary}\n\n"
            f"## Completed\n{completed or '_None specified_'}\n\n"
            f"## Next Steps\n{next_steps or '_None specified_'}\n\n"
            f"## Files Touched\n{files_touched or '_None specified_'}\n"
        )
        md_file.write_text(md_body, encoding="utf-8")
        project_md_path = str(md_file)

    if project_md_path:
        payload["project_md_path"] = project_md_path
    return payload
