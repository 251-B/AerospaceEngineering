"""MCP bridge exposing Antigravity CLI (agy.exe) as a delegatable teammate to Claude Code."""

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

mcp = FastMCP("antigravity-bridge")

_MODE_MAP = {
    "read_only": "",
    "plan": "plan",
    "edit": "accept-edits",
    "auto": "accept-edits",
}

_READ_ONLY_PREFIX = (
    "[READ-ONLY MODE: Do not create, modify, or delete any files or run mutating commands. "
    "Only inspect, analyze, and answer directly.]\n\n"
)


def _json_out(data: dict) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False)


async def _run_quick_cmd(args: list[str], timeout: float = 5.0) -> tuple[int, str, str]:
    proc = None
    try:
        proc = await asyncio.create_subprocess_exec(
            *args,
            stdin=asyncio.subprocess.DEVNULL,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            creationflags=bc.subprocess_creation_flags(),
        )
        out_b, err_b = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        return (
            int(proc.returncode or 0),
            out_b.decode("utf-8", errors="replace").strip(),
            err_b.decode("utf-8", errors="replace").strip(),
        )
    except asyncio.TimeoutError:
        if proc is not None and proc.returncode is None:
            try:
                proc.kill()
                await proc.wait()
            except ProcessLookupError:
                pass
        return -1, "", f"Timed out after {timeout}s"
    except Exception as exc:
        return -1, "", str(exc)


@mcp.tool()
async def antigravity_delegate(
    prompt: str,
    cwd: str = "",
    role: str = "worker",
    model: str = "",
    effort: str = "",
    mode: str = "read_only",
    conversation_id: str = "",
    timeout_sec: int = 300,
) -> str:
    """Delegate a bounded task or cross-review to Antigravity (agy CLI) in headless JSON mode.

    Args:
        prompt: Clear, self-contained task instruction.
        cwd: Working directory for Antigravity (defaults to current directory).
        role: Team role preset: 'fast', 'worker', 'reviewer', or 'architect'.
        model: Optional explicit model ID (leave blank to use agy default / config.json role preset).
        effort: Optional reasoning effort override ('low', 'medium', 'high', 'max'; omitted when model slug already carries an effort suffix).
        mode: Execution permission mode: 'read_only' (default, read-only default mode), 'plan' (creates implementation_plan.md), 'edit' (accept-edits), or 'auto' (mapped to accept-edits).
        conversation_id: Optional conversation_id returned from a previous call to resume context.
        timeout_sec: Max wall-clock seconds before terminating the subprocess (default 300).
    """
    allowed, depth, max_depth = bc.check_recursion_guard()
    if not allowed:
        return _json_out(
            {
                "status": "recursion_blocked",
                "provider": "antigravity",
                "depth": depth,
                "max_recursion_depth": max_depth,
                "error": "Delegation blocked to prevent recursive agent loops. Complete this task locally.",
            }
        )

    if mode not in _MODE_MAP:
        return _json_out(
            {
                "status": "invalid_argument",
                "provider": "antigravity",
                "error": f"Unsupported mode '{mode}'. Allowed values: {list(_MODE_MAP.keys())}.",
            }
        )

    cfg = bc.load_config()
    agy_cfg = cfg.get("antigravity", {})
    exe = bc.resolve_executable(str(agy_cfg.get("executable", "")), "agy")
    if not exe:
        return _json_out(
            {
                "status": "not_installed",
                "provider": "antigravity",
                "error": "agy.exe not found. Install via PowerShell: irm https://antigravity.google/cli/install.ps1 | iex",
            }
        )

    target_cwd = cwd.strip() or os.getcwd()
    if not os.path.isdir(target_cwd):
        return _json_out(
            {
                "status": "invalid_argument",
                "provider": "antigravity",
                "error": f"Working directory does not exist: {target_cwd}",
            }
        )

    roles = agy_cfg.get("roles", {})
    role_key = role if role in roles else "worker"
    role_cfg = roles.get(role_key, {"model": "", "effort": "medium"})
    eff_model = model.strip() or str(role_cfg.get("model", "")).strip()
    eff_effort = effort.strip() or str(role_cfg.get("effort", "medium")).strip()
    agy_mode = _MODE_MAP[mode]

    cooldown_active, remaining_mins, until_iso = bc.is_in_cooldown("antigravity")

    temp_prompt_path: Path | None = None
    effective_prompt = f"{_READ_ONLY_PREFIX}{prompt}" if mode == "read_only" else prompt
    if len(effective_prompt) > 25000:
        bc.TMP_DIR.mkdir(parents=True, exist_ok=True)
        fd, tmp_name = tempfile.mkstemp(dir=str(bc.TMP_DIR), prefix="agy_prompt_", suffix=".txt")
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(effective_prompt)
        temp_prompt_path = Path(tmp_name)
        effective_prompt = (
            f"Read the complete task specification from `{temp_prompt_path}` and execute it exactly."
        )

    effective_timeout = max(5, int(timeout_sec or cfg.get("default_timeout_sec", 300)))
    argv = [
        exe,
        "-p",
        effective_prompt,
        "--output-format",
        "json",
        "--print-timeout",
        f"{effective_timeout}s",
    ]
    if agy_mode:
        argv.extend(["--mode", agy_mode])
    if eff_effort and not bc.model_has_effort_suffix(eff_model):
        argv.extend(["--effort", eff_effort])
    if eff_model:
        argv.extend(["--model", eff_model])
    if conversation_id.strip():
        argv.extend(["--conversation", conversation_id.strip()])

    proc = None
    try:
        proc = await asyncio.create_subprocess_exec(
            *argv,
            cwd=target_cwd,
            env=bc.child_env("antigravity"),
            stdin=asyncio.subprocess.DEVNULL,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            creationflags=bc.subprocess_creation_flags(),
        )
        stdout_b, stderr_b = await asyncio.wait_for(
            proc.communicate(), timeout=effective_timeout + 15
        )
    except asyncio.TimeoutError:
        if proc is not None and proc.returncode is None:
            try:
                proc.kill()
                await proc.wait()
            except ProcessLookupError:
                pass
        bc.record_call(
            "antigravity", role_key, eff_model or "default", "timeout", None, f"Timed out after {effective_timeout}s"
        )
        return _json_out(
            {
                "status": "timeout",
                "provider": "antigravity",
                "role": role_key,
                "model": eff_model or "default",
                "error": f"Antigravity subprocess exceeded timeout of {effective_timeout}s.",
            }
        )
    except Exception as exc:
        bc.record_call("antigravity", role_key, eff_model or "default", "error", None, str(exc))
        return _json_out(
            {
                "status": "error",
                "provider": "antigravity",
                "role": role_key,
                "model": eff_model or "default",
                "error": f"Failed executing agy subprocess: {exc}",
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
        agy_status = str(envelope.get("status") or "").upper()
        resp_txt = str(envelope.get("response") or "")
        err_txt = str(envelope.get("error") or "")
        conv_out = str(envelope.get("conversation_id") or conversation_id or "")
        usage = envelope.get("usage") if isinstance(envelope.get("usage"), dict) else {}
        duration_sec = envelope.get("duration_seconds")
        num_turns = envelope.get("num_turns")
        denied_actions = envelope.get("denied_actions") or []
        combined_err = "\n".join(x for x in (err_txt, stderr_txt) if x).strip()

        # Only a failed run can be an auth failure; a reply that merely mentions the phrase is not.
        if agy_status != "SUCCESS" and "authentication required" in combined_err.lower():
            bc.record_call("antigravity", role_key, eff_model or "default", "auth_required", usage, combined_err)
            return _json_out(
                {
                    "status": "auth_required",
                    "provider": "antigravity",
                    "role": role_key,
                    "error": combined_err or "Authentication required for agy CLI.",
                    "instruction": "Run 'agy' once in PowerShell to sign in interactively.",
                }
            )

        is_failed = (agy_status and agy_status != "SUCCESS") or proc.returncode != 0 or bool(err_txt)
        if is_failed and bc.detect_quota_error(f"{err_txt}\n{resp_txt}\n{stderr_txt}"):
            bc.record_call(
                "antigravity",
                role_key,
                eff_model or "default",
                "quota_exceeded",
                usage,
                combined_err or "Quota/rate limit",
            )
            return _json_out(
                {
                    "status": "quota_exceeded",
                    "provider": "antigravity",
                    "role": role_key,
                    "model": eff_model or "default",
                    "conversation_id": conv_out,
                    "error": combined_err or resp_txt or "Antigravity hit usage/rate limit.",
                    "usage": usage,
                    "recommendation": "Antigravity hit rate/quota limit. Continue locally in Claude Code or save handoff via bridge_handoff.",
                }
            )

        if is_failed:
            bc.record_call(
                "antigravity",
                role_key,
                eff_model or "default",
                "error",
                usage,
                combined_err or f"agy status={agy_status} rc={proc.returncode}",
            )
            return _json_out(
                {
                    "status": "error",
                    "provider": "antigravity",
                    "role": role_key,
                    "model": eff_model or "default",
                    "conversation_id": conv_out,
                    "agy_status": agy_status,
                    "returncode": proc.returncode,
                    "error": combined_err or f"agy failed with status={agy_status}, rc={proc.returncode}",
                    "response": resp_txt,
                    "usage": usage,
                }
            )

        if resp_txt.strip() == "":
            err_summary = bc.summarize_empty_error("agy", denied_actions, warnings, stderr_txt)
            bc.record_call("antigravity", role_key, eff_model or "default", "empty", usage, err_summary)
            return _json_out(
                {
                    "status": "empty",
                    "provider": "antigravity",
                    "role": role_key,
                    "model": eff_model or "default",
                    "mode": mode,
                    "conversation_id": conv_out,
                    "duration_seconds": duration_sec,
                    "num_turns": num_turns,
                    "denied_actions": denied_actions,
                    "warnings": warnings,
                    "stderr": stderr_txt[:1500],
                    "usage": usage,
                    "error": err_summary,
                    "recommendation": "Headless agy returned an empty response (often caused by auto-denied tool permissions). Check denied_actions/stderr and ~/.gemini/antigravity-cli/settings.json before retrying.",
                }
            )

        bc.record_call("antigravity", role_key, eff_model or "default", "ok", usage)
        out = {
            "status": "ok",
            "provider": "antigravity",
            "role": role_key,
            "model": eff_model or "default",
            "effort": eff_effort,
            "mode": mode,
            "conversation_id": conv_out,
            "duration_seconds": duration_sec,
            "num_turns": num_turns,
            "response": resp_txt,
            "usage": usage,
        }
        if warnings:
            out["warnings"] = warnings
        if denied_actions:
            out["denied_actions"] = denied_actions
        if cooldown_active:
            out["note"] = f"Ran while prior cooldown was scheduled until {until_iso} ({remaining_mins}m left); succeeded so cooldown cleared."
        return _json_out(out)

    combined = "\n".join(x for x in (stdout_txt.strip(), stderr_txt) if x).strip()
    if "authentication required" in combined.lower():
        bc.record_call("antigravity", role_key, eff_model or "default", "auth_required", None, combined)
        return _json_out(
            {
                "status": "auth_required",
                "provider": "antigravity",
                "error": combined[:1000],
                "instruction": "Run 'agy' once in PowerShell to sign in interactively.",
            }
        )

    if bc.detect_quota_error(combined):
        bc.record_call("antigravity", role_key, eff_model or "default", "quota_exceeded", None, combined)
        return _json_out(
            {
                "status": "quota_exceeded",
                "provider": "antigravity",
                "role": role_key,
                "model": eff_model or "default",
                "error": combined[:1000],
                "recommendation": "Antigravity hit rate/quota limit. Continue locally in Claude Code or save handoff via bridge_handoff.",
            }
        )

    if proc.returncode != 0:
        bc.record_call("antigravity", role_key, eff_model or "default", "error", None, combined or f"rc={proc.returncode}")
        return _json_out(
            {
                "status": "error",
                "provider": "antigravity",
                "role": role_key,
                "model": eff_model or "default",
                "returncode": proc.returncode,
                "error": combined[:1500] or f"agy exited with code {proc.returncode}.",
            }
        )

    if stdout_txt.strip() == "":
        err_summary = bc.summarize_empty_error("agy", None, warnings, stderr_txt)
        bc.record_call("antigravity", role_key, eff_model or "default", "empty", None, err_summary)
        return _json_out(
            {
                "status": "empty",
                "provider": "antigravity",
                "role": role_key,
                "model": eff_model or "default",
                "mode": mode,
                "conversation_id": conversation_id,
                "denied_actions": [],
                "warnings": warnings,
                "stderr": stderr_txt[:1500],
                "error": err_summary,
                "recommendation": "Headless agy returned an empty response. Check stderr and ~/.gemini/antigravity-cli/settings.json before retrying.",
            }
        )

    bc.record_call("antigravity", role_key, eff_model or "default", "ok", None)
    return _json_out(
        {
            "status": "ok",
            "provider": "antigravity",
            "role": role_key,
            "model": eff_model or "default",
            "response": stdout_txt.strip(),
        }
    )


@mcp.tool()
async def antigravity_status() -> str:
    """Return agy CLI status/version/models, cooldowns, today's shared bridge telemetry, and active handoff."""
    cfg = bc.load_config()
    state = bc.load_state()
    agy_exe = bc.resolve_executable(str(cfg.get("antigravity", {}).get("executable", "")), "agy")
    claude_exe = bc.resolve_executable(str(cfg.get("claude", {}).get("executable", "")), "claude")

    agy_info: dict = {"available": bool(agy_exe), "path": agy_exe or ""}
    if agy_exe:
        rc_v, out_v, err_v = await _run_quick_cmd([agy_exe, "--version"], timeout=5.0)
        agy_info["version"] = out_v if rc_v == 0 else (err_v or f"rc={rc_v}")
        rc_m, out_m, err_m = await _run_quick_cmd([agy_exe, "models"], timeout=6.0)
        if rc_m == 0:
            agy_info["authenticated"] = True
            agy_info["models_output"] = out_m
        else:
            msg = err_m or out_m
            agy_info["authenticated"] = "authentication required" not in msg.lower()
            agy_info["models_status"] = msg[:500]

    c_cool, c_mins, c_until = bc.is_in_cooldown("claude")
    a_cool, a_mins, a_until = bc.is_in_cooldown("antigravity")

    return _json_out(
        {
            "executables": {
                "antigravity": agy_info,
                "claude": {"available": bool(claude_exe), "path": claude_exe or ""},
            },
            "cooldowns": {
                "antigravity": {"active": a_cool, "remaining_minutes": a_mins, "until": a_until},
                "claude": {"active": c_cool, "remaining_minutes": c_mins, "until": c_until},
            },
            "today_telemetry": state,
            "roles": {
                "antigravity": cfg.get("antigravity", {}).get("roles", {}),
                "claude": cfg.get("claude", {}).get("roles", {}),
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
            from_agent="claude",
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
