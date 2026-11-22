"""MCP bridge exposing Claude Code (claude.exe) as a delegatable teammate to Antigravity."""

from __future__ import annotations

import asyncio
import json
import os
import sys
import tempfile
from pathlib import Path

from mcp.server.fastmcp import FastMCP

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bridge_common as bc  # noqa: E402

mcp = FastMCP("claude-bridge")

_MODE_MAP = {
    "read_only": "plan",
    "edit": "acceptEdits",
    "auto": "auto",
}


def _json_out(data: dict) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False)


@mcp.tool()
async def claude_delegate(
    prompt: str,
    cwd: str = "",
    role: str = "worker",
    model: str = "",
    effort: str = "",
    mode: str = "read_only",
    session_id: str = "",
    timeout_sec: int = 300,
) -> str:
    """Delegate a bounded task or cross-review to Claude Code in headless JSON mode.

    Args:
        prompt: Clear, self-contained task instruction.
        cwd: Working directory for Claude Code (defaults to current directory).
        role: Team role preset: 'fast' (haiku), 'worker' (sonnet), 'reviewer' (opus), or 'architect' (opus).
        model: Optional explicit model override (e.g. 'haiku', 'sonnet', 'opus').
        effort: Optional explicit reasoning effort override ('low', 'medium', 'high', 'max').
        mode: Execution permission mode: 'read_only' (default, plan mode), 'edit' (acceptEdits), or 'auto'.
        session_id: Optional Claude session_id returned from a previous call to resume context.
        timeout_sec: Max wall-clock seconds before terminating the subprocess (minimum and default 300 due to Claude Code cold-start overhead).
    """
    allowed, depth, max_depth = bc.check_recursion_guard()
    if not allowed:
        return _json_out(
            {
                "status": "recursion_blocked",
                "provider": "claude",
                "depth": depth,
                "max_recursion_depth": max_depth,
                "error": "Delegation blocked to prevent recursive agent loops. Complete this task locally.",
            }
        )

    if mode not in _MODE_MAP:
        return _json_out(
            {
                "status": "invalid_argument",
                "provider": "claude",
                "error": f"Unsupported mode '{mode}'. Allowed values: {list(_MODE_MAP.keys())}.",
            }
        )

    cfg = bc.load_config()
    claude_cfg = cfg.get("claude", {})
    exe = bc.resolve_executable(str(claude_cfg.get("executable", "")), "claude")
    if not exe:
        return _json_out(
            {
                "status": "not_installed",
                "provider": "claude",
                "error": "claude.exe not found. Verify ~/.local/bin/claude.exe or PATH.",
            }
        )

    target_cwd = cwd.strip() or os.getcwd()
    if not os.path.isdir(target_cwd):
        return _json_out(
            {
                "status": "invalid_argument",
                "provider": "claude",
                "error": f"Working directory does not exist: {target_cwd}",
            }
        )

    roles = claude_cfg.get("roles", {})
    role_key = role if role in roles else "worker"
    role_cfg = roles.get(role_key, {"model": "sonnet", "effort": "medium"})
    eff_model = model.strip() or str(role_cfg.get("model", "sonnet"))
    eff_effort = effort.strip() or str(role_cfg.get("effort", "medium"))
    perm_mode = _MODE_MAP[mode]

    cooldown_active, remaining_mins, until_iso = bc.is_in_cooldown("claude")

    temp_prompt_path: Path | None = None
    effective_prompt = prompt
    if len(prompt) > 25000:
        bc.TMP_DIR.mkdir(parents=True, exist_ok=True)
        fd, tmp_name = tempfile.mkstemp(dir=str(bc.TMP_DIR), prefix="claude_prompt_", suffix=".txt")
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(prompt)
        temp_prompt_path = Path(tmp_name)
        effective_prompt = (
            f"Read the complete task specification from `{temp_prompt_path}` and execute it exactly."
        )

    argv = [
        exe,
        "-p",
        effective_prompt,
        "--output-format",
        "json",
        "--permission-mode",
        perm_mode,
        "--model",
        eff_model,
        "--effort",
        eff_effort,
    ]
    if session_id.strip():
        argv.extend(["--resume", session_id.strip()])

    min_timeout = int(cfg.get("default_timeout_sec", 300))
    effective_timeout = max(min_timeout, int(timeout_sec or min_timeout))
    proc = None
    try:
        proc = await asyncio.create_subprocess_exec(
            *argv,
            cwd=target_cwd,
            env=bc.child_env("claude"),
            stdin=asyncio.subprocess.DEVNULL,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            creationflags=bc.subprocess_creation_flags(),
        )
        stdout_b, stderr_b = await asyncio.wait_for(proc.communicate(), timeout=effective_timeout)
    except asyncio.TimeoutError:
        if proc is not None and proc.returncode is None:
            try:
                proc.kill()
                await proc.wait()
            except ProcessLookupError:
                pass
        bc.record_call("claude", role_key, eff_model, "timeout", None, f"Timed out after {effective_timeout}s")
        return _json_out(
            {
                "status": "timeout",
                "provider": "claude",
                "role": role_key,
                "model": eff_model,
                "error": f"Claude subprocess exceeded timeout of {effective_timeout}s.",
            }
        )
    except Exception as exc:
        bc.record_call("claude", role_key, eff_model, "error", None, str(exc))
        return _json_out(
            {
                "status": "error",
                "provider": "claude",
                "role": role_key,
                "model": eff_model,
                "error": f"Failed executing Claude subprocess: {exc}",
            }
        )
    finally:
        if temp_prompt_path is not None:
            try:
                temp_prompt_path.unlink(missing_ok=True)
            except OSError:
                pass

    stdout_txt = stdout_b.decode("utf-8", errors="replace")
    stderr_txt = stderr_b.decode("utf-8", errors="replace").strip()
    warnings = bc.extract_warnings(stderr_txt)
    envelope = bc.parse_last_json_object(stdout_txt)

    if envelope is not None:
        is_err = bool(envelope.get("is_error"))
        result_txt = str(envelope.get("result") or "")
        sess_out = str(envelope.get("session_id") or session_id or "")
        usage = envelope.get("usage") if isinstance(envelope.get("usage"), dict) else {}
        cost_usd = envelope.get("total_cost_usd")
        num_turns = envelope.get("num_turns")
        permission_denials = envelope.get("permission_denials") or []
        combined_err = "\n".join(x for x in (result_txt if is_err else "", stderr_txt) if x).strip()

        if (is_err or proc.returncode != 0) and bc.detect_quota_error(f"{result_txt}\n{stderr_txt}"):
            bc.record_call("claude", role_key, eff_model, "quota_exceeded", usage, combined_err or "Quota/rate limit")
            return _json_out(
                {
                    "status": "quota_exceeded",
                    "provider": "claude",
                    "role": role_key,
                    "model": eff_model,
                    "session_id": sess_out,
                    "error": combined_err or "Claude Code hit usage/rate limit.",
                    "usage": usage,
                    "recommendation": "Claude hit rate/quota limit. Handle locally in Antigravity or save handoff via bridge_handoff.",
                }
            )

        if is_err or proc.returncode != 0:
            bc.record_call("claude", role_key, eff_model, "error", usage, combined_err or f"Exit code {proc.returncode}")
            return _json_out(
                {
                    "status": "error",
                    "provider": "claude",
                    "role": role_key,
                    "model": eff_model,
                    "session_id": sess_out,
                    "returncode": proc.returncode,
                    "error": combined_err or f"Claude exited with code {proc.returncode}.",
                    "response": result_txt,
                    "usage": usage,
                }
            )

        if result_txt.strip() == "":
            err_summary = bc.summarize_empty_error("claude", permission_denials, warnings, stderr_txt)
            bc.record_call("claude", role_key, eff_model, "empty", usage, err_summary)
            return _json_out(
                {
                    "status": "empty",
                    "provider": "claude",
                    "role": role_key,
                    "model": eff_model,
                    "mode": mode,
                    "session_id": sess_out,
                    "num_turns": num_turns,
                    "permission_denials": permission_denials,
                    "warnings": warnings,
                    "stderr": stderr_txt[:1500],
                    "usage": usage,
                    "error": err_summary,
                    "recommendation": "Claude returned an empty response. Check permission_denials/stderr before retrying.",
                }
            )

        bc.record_call("claude", role_key, eff_model, "ok", usage)
        out = {
            "status": "ok",
            "provider": "claude",
            "role": role_key,
            "model": eff_model,
            "effort": eff_effort,
            "mode": mode,
            "session_id": sess_out,
            "num_turns": num_turns,
            "response": result_txt,
            "usage": usage,
            "total_cost_usd": cost_usd,
        }
        if permission_denials:
            out["permission_denials"] = permission_denials
        if warnings:
            out["warnings"] = warnings
        if cooldown_active:
            out["note"] = f"Ran while prior cooldown was scheduled until {until_iso} ({remaining_mins}m left); succeeded so cooldown cleared."
        return _json_out(out)

    # Non-JSON output fallback
    combined = "\n".join(x for x in (stdout_txt.strip(), stderr_txt) if x).strip()
    if bc.detect_quota_error(combined):
        bc.record_call("claude", role_key, eff_model, "quota_exceeded", None, combined)
        return _json_out(
            {
                "status": "quota_exceeded",
                "provider": "claude",
                "role": role_key,
                "model": eff_model,
                "error": combined[:1000],
                "recommendation": "Claude hit rate/quota limit. Handle locally in Antigravity or save handoff via bridge_handoff.",
            }
        )

    if proc.returncode != 0:
        bc.record_call("claude", role_key, eff_model, "error", None, combined or f"Exit code {proc.returncode}")
        return _json_out(
            {
                "status": "error",
                "provider": "claude",
                "role": role_key,
                "model": eff_model,
                "returncode": proc.returncode,
                "error": combined[:1500] or f"Claude exited with code {proc.returncode}.",
            }
        )

    if stdout_txt.strip() == "":
        err_summary = bc.summarize_empty_error("claude", None, warnings, stderr_txt)
        bc.record_call("claude", role_key, eff_model, "empty", None, err_summary)
        return _json_out(
            {
                "status": "empty",
                "provider": "claude",
                "role": role_key,
                "model": eff_model,
                "mode": mode,
                "session_id": session_id,
                "permission_denials": [],
                "warnings": warnings,
                "stderr": stderr_txt[:1500],
                "error": err_summary,
                "recommendation": "Claude returned an empty response. Check stderr before retrying.",
            }
        )

    bc.record_call("claude", role_key, eff_model, "ok", None)
    return _json_out(
        {
            "status": "ok",
            "provider": "claude",
            "role": role_key,
            "model": eff_model,
            "response": stdout_txt.strip(),
        }
    )


@mcp.tool()
async def claude_status() -> str:
    """Return Claude & Antigravity availability, cooldowns, today's bridge token telemetry, role mapping, and active handoff."""
    cfg = bc.load_config()
    state = bc.load_state()
    claude_exe = bc.resolve_executable(str(cfg.get("claude", {}).get("executable", "")), "claude")
    agy_exe = bc.resolve_executable(str(cfg.get("antigravity", {}).get("executable", "")), "agy")

    c_cool, c_mins, c_until = bc.is_in_cooldown("claude")
    a_cool, a_mins, a_until = bc.is_in_cooldown("antigravity")

    return _json_out(
        {
            "executables": {
                "claude": {"available": bool(claude_exe), "path": claude_exe or ""},
                "antigravity": {"available": bool(agy_exe), "path": agy_exe or ""},
            },
            "cooldowns": {
                "claude": {"active": c_cool, "remaining_minutes": c_mins, "until": c_until},
                "antigravity": {"active": a_cool, "remaining_minutes": a_mins, "until": a_until},
            },
            "today_telemetry": state,
            "roles": {
                "claude": cfg.get("claude", {}).get("roles", {}),
                "antigravity": cfg.get("antigravity", {}).get("roles", {}),
            },
            "handoff": bc.handoff_read(),
        }
    )


@mcp.tool()
async def bridge_handoff(
    action: str = "read",
    project_cwd: str = "",
    summary: str = "",
    completed: str = "",
    next_steps: str = "",
    files_touched: str = "",
    blocker_or_reason: str = "",
    write_project_md: bool = False,
) -> str:
    """Read or write the shared cross-agent handoff state (~/.agent-bridge/handoff.json).

    Args:
        action: 'read' (default) to inspect the latest handoff, or 'write' to save state for the other agent.
        project_cwd: Workspace root path for the task being handed off.
        summary: Concise context summary for the receiving agent.
        completed: What has already been verified/finished.
        next_steps: Exact next actions for the receiving agent.
        files_touched: Comma-separated or bulleted list of modified/relevant files.
        blocker_or_reason: Why handing off (e.g. 'quota_exceeded', 'cross_review', 'manual_switch').
        write_project_md: When True and project_cwd exists, also writes <project_cwd>/.agents/HANDOFF.md.
    """
    act = (action or "read").strip().lower()
    if act == "read":
        return _json_out(bc.handoff_read())
    if act == "write":
        res = bc.handoff_write(
            project_cwd=project_cwd.strip() or os.getcwd(),
            from_agent="antigravity",
            summary=summary,
            completed=completed,
            next_steps=next_steps,
            files_touched=files_touched,
            blocker_or_reason=blocker_or_reason,
            write_project_md=write_project_md,
        )
        return _json_out(res)
    return _json_out({"status": "invalid_argument", "error": f"Unknown action '{action}'. Use 'read' or 'write'."})


if __name__ == "__main__":
    mcp.run(transport="stdio")
