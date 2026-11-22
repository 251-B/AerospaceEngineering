#!/usr/bin/env python3
"""Antigravity SessionStart hook for skill-evolution.

Scans frontmatter headers in the persistent skill-observations store and injects
concise awareness of open observations and proposed skill candidates.
Never prints anything to stdout other than a single valid JSON object.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

OBS_ROOT = Path(r"{{HOME}}/.agent-bridge/skill-observations")
LOG_DIR = OBS_ROOT / "observation-log"
LAST_REVIEW_FILE = OBS_ROOT / "last-review-date.txt"
NEW_OBS_SCRIPT = "{{HOME}}/.gemini/config/plugins/skill-evolution/scripts/new_observation.py"


def _unquote(val: str) -> str:
    val = val.strip()
    if len(val) >= 2 and ((val[0] == '"' and val[-1] == '"') or (val[0] == "'" and val[-1] == "'")):
        inner = val[1:-1]
        if val[0] == '"':
            inner = inner.replace('\\"', '"').replace("\\\\", "\\")
        else:
            inner = inner.replace("''", "'")
        return inner
    return val


def _parse_inline_list(val: str) -> list[str]:
    val = val.strip()
    if not (val.startswith("[") and val.endswith("]")):
        item = _unquote(val)
        return [item] if item else []
    inner = val[1:-1].strip()
    if not inner:
        return []
    items: list[str] = []
    # Split on commas outside quotes
    current: list[str] = []
    quote: str | None = None
    escaped = False
    for ch in inner:
        if escaped:
            current.append(ch)
            escaped = False
            continue
        if ch == "\\" and quote == '"':
            current.append(ch)
            escaped = True
            continue
        if ch in ('"', "'"):
            if quote is None:
                quote = ch
            elif quote == ch:
                quote = None
            current.append(ch)
            continue
        if ch == "," and quote is None:
            token = _unquote("".join(current))
            if token:
                items.append(token)
            current = []
            continue
        current.append(ch)
    token = _unquote("".join(current))
    if token:
        items.append(token)
    return items


def parse_frontmatter(path: Path) -> dict[str, object]:
    """Read only the YAML frontmatter block between the opening and closing --- lines."""
    fields: dict[str, object] = {}
    try:
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            first = fh.readline()
            if not re.match(r"^---\s*$", first):
                return fields
            active_list_key: str | None = None
            for line in fh:
                if re.match(r"^---\s*$", line):
                    break
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                if active_list_key and re.match(r"^-\s+", stripped):
                    item = _unquote(re.sub(r"^-\s+", "", stripped))
                    if item:
                        lst = fields.setdefault(active_list_key, [])
                        if isinstance(lst, list):
                            lst.append(item)
                    continue
                active_list_key = None
                m = re.match(r"^([a-zA-Z0-9_]+):\s*(.*)$", line.rstrip("\r\n"))
                if not m:
                    continue
                key = m.group(1)
                raw_val = m.group(2).strip()
                # Strip inline YAML comments outside quotes
                if raw_val and not raw_val.startswith(('"', "'", "[")):
                    raw_val = re.sub(r"\s+#.*$", "", raw_val).strip()
                if key in ("skill", "proposes_skill"):
                    if not raw_val:
                        fields[key] = []
                        active_list_key = key
                    else:
                        fields[key] = _parse_inline_list(raw_val)
                elif key in ("id", "status", "title"):
                    fields[key] = _unquote(raw_val)
    except OSError:
        return {}
    return fields


def main() -> None:
    try:
        try:
            raw_stdin = sys.stdin.read()
            if raw_stdin.strip():
                json.loads(raw_stdin)
        except Exception:
            pass

        last_review = "never"
        if LAST_REVIEW_FILE.is_file():
            txt = LAST_REVIEW_FILE.read_text(encoding="utf-8", errors="replace").strip()
            if txt:
                last_review = txt.splitlines()[0].strip()

        open_count = 0
        proposed_counter: Counter[str] = Counter()

        if LOG_DIR.is_dir():
            for md_file in sorted(LOG_DIR.glob("*.md")):
                if not md_file.is_file():
                    continue
                fm = parse_frontmatter(md_file)
                status = str(fm.get("status", "open") or "open").strip().lower()
                if status == "open":
                    open_count += 1
                    proposes = fm.get("proposes_skill", [])
                    if isinstance(proposes, list):
                        for cand in proposes:
                            cand_str = str(cand).strip()
                            if cand_str:
                                proposed_counter[cand_str] += 1

        if proposed_counter:
            proposed_str = ", ".join(
                f"{name} ({count})" if count > 1 else name
                for name, count in proposed_counter.most_common()
            )
        else:
            proposed_str = "none"

        msg = (
            f"[skill-evolution] Shared observation store: {{HOME}}/.agent-bridge/skill-observations/observation-log "
            f"({open_count} open observations; last review: {last_review}; proposed skills: {proposed_str}). "
            f"Invoke task-observer at the start of every main session (subagents skip it). Follow the Skill Evolution rule: "
            f"detect recurring requests, corrections, and reusable multi-step workflows; log observations with python \"{NEW_OBS_SCRIPT}\"; "
            f"and when a pattern repeats (>=2 occurrences), a review is due, or the user says 'siempre hago esto asi', "
            f"propose or build the reusable skill with skill-creator + writing-skills and add a matching rule in "
            f"~/.claude/skill_rules.json (or <repo>/.claude/skill_rules.json) so it fires automatically."
        )

        payload = {
            "injectSteps": [
                {
                    "systemMessage": {
                        "systemMessage": msg
                    }
                }
            ]
        }
        sys.stdout.write(json.dumps(payload, ensure_ascii=True))
    except Exception:
        sys.stdout.write("{}")


if __name__ == "__main__":
    main()
