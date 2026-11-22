#!/usr/bin/env python3
"""Refresh partner-setup/payload/ from the owner's live Claude Code + Antigravity setup.

Run on the owner's computer only (stdlib, Python 3.10+):

    python partner-setup/export.py           # rewrite payload/
    python partner-setup/export.py --check   # exit 1 if payload/ is stale

Every text file is templated: the owner's paths become {{PYTHON}}, {{CLAUDE_EXE}},
{{AGY_EXE}}, {{REPO}} and {{HOME}}. The export refuses to finish if a personal
value (name, e-mail, machine name) is left in the payload.
"""
from __future__ import annotations

import argparse
import filecmp
import json
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = json.loads((HERE / "manifest.json").read_text(encoding="utf-8"))
HOME = Path.home()
REPO = HERE.parent

# Owner-specific absolute paths, most specific first.
BASES = [
    ("{{PYTHON}}", sys.executable),
    ("{{CLAUDE_EXE}}", str(HOME / ".local/bin/claude.exe")),
    ("{{AGY_EXE}}", str(HOME / "AppData/Local/agy/bin/agy.exe")),
    ("{{REPO}}", str(REPO)),
    ("{{HOME}}", str(HOME)),
]
# Any other user's clone of this repo (e.g. a path a teammate's note left behind).
OTHER_REPO = re.compile(r"[A-Za-z]:[\\/]{1,2}Users[\\/]{1,2}[^\\/\s\"'`)]+(?:[\\/]{1,2}[^\\/\s\"'`)]+)*?[\\/]{1,2}AerospaceEngineering")
# Any absolute user-profile path left after templating is a leak.
USER_PATH = re.compile(r"[A-Za-z]:[\\/]{1,2}Users[\\/]{1,2}\w", re.I)
SKIP_DIRS = {"__pycache__", ".git"}


def personal_markers() -> list[str]:
    """Owner-specific values the payload must not contain; nothing personal is written in this file."""
    marks = [HOME.name, platform.node()]
    try:
        marks.append(subprocess.run(["git", "config", "user.email"], capture_output=True, text=True, cwd=REPO).stdout)
    except OSError:
        pass
    private = HOME / ".agent-bridge" / "export-private.json"  # optional, never committed
    if private.exists():
        marks += json.loads(private.read_text(encoding="utf-8")).get("personal", [])
    return sorted({m.strip().lower() for m in marks if len(m.strip()) >= 4})


def variants(path: str) -> list[str]:
    """Spellings of one Windows path: backslash, JSON-escaped, forward slash, git-bash."""
    win = path.replace("/", "\\")
    fwd = win.replace("\\", "/")
    out = [win.replace("\\", "\\\\"), win, fwd]
    if len(win) > 2 and win[1] == ":":
        out.append("/" + win[0].lower() + fwd[2:])
    out += [v[0].lower() + v[1:] if v[1:2] == ":" else v for v in out]
    return sorted(set(out), key=len, reverse=True)


REPLACEMENTS = [(v, tag) for tag, base in BASES for v in variants(base)]


TAIL = re.compile(r"(\{\{(?:HOME|REPO|PYTHON|CLAUDE_EXE|AGY_EXE)\}\})([^\s\"'`)\]]*)")


def template(text: str) -> str:
    for old, tag in REPLACEMENTS:
        text = text.replace(old, tag)
    text = OTHER_REPO.sub("{{REPO}}", text)
    # Forward slashes after a placeholder, so the installed path is valid on any OS.
    return TAIL.sub(lambda m: m[1] + m[2].replace("\\\\", "/").replace("\\", "/"), text)


def copy_file(src: Path, dst: Path, fix=None) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    try:
        text = src.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        shutil.copyfile(src, dst)
        return
    text = template(text)
    if fix:
        text = fix(text)
    dst.write_text(text, encoding="utf-8", newline="")


def copy_tree(src: Path, dst: Path) -> None:
    for f in sorted(src.rglob("*")):
        if f.is_file() and not SKIP_DIRS.intersection(f.relative_to(src).parts) and ".bak" not in f.name:
            copy_file(f, dst / f.relative_to(src))


def quote_python(text: str) -> str:
    # A bare `python` or a Python path with spaces breaks a hook command on Windows.
    for bare in ('"command": "{{PYTHON}} ', '"command": "python '):
        text = text.replace(bare, '"command": "\\"{{PYTHON}}\\" ')
    return text


def drop_backup_line(text: str) -> str:
    return "".join(l for l in text.splitlines(True) if "claude-config-backup" not in l)


def router_rules(text: str) -> str:
    """Drop rules that only route to skills the partner does not get; refuse a broken regex."""
    data = json.loads(text)
    excluded = set(MANIFEST["claude"]["router_rules_excluded"])
    bad = [r["match"][:40] for r in data["rules"] if any(ord(ch) < 32 for ch in r["match"])]
    if bad:
        raise SystemExit(f"export: control character in a router regex (write \\\\b, not \\b in JSON): {bad}")
    data["rules"] = [r for r in data["rules"] if not set(r["use"]) <= excluded]
    return json.dumps(data, indent=1, ensure_ascii=False) + "\n"


def built_plugin_file(name: str):
    description = MANIFEST["gemini"]["built_plugins"][name].get("description")

    def fix(text: str) -> str:
        if description and text.lstrip().startswith("{") and '"description"' in text:
            data = json.loads(text)
            if "name" in data:
                data["description"] = description
                return json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        return text
    return fix


def build(out: Path) -> None:
    c, g = MANIFEST["claude"], MANIFEST["gemini"]
    fixes = {"claude/CLAUDE.md": drop_backup_line, "claude/skill_rules.json": router_rules}
    for rel, live in c["files"].items():
        copy_file(HOME / live, out / rel, fixes.get(rel))
    for name in c["vendored_skills"]:
        copy_tree(HOME / ".claude/skills" / name, out / "claude/skills" / name)
    plugins = HOME / ".gemini/config/plugins"
    for name in g["vendored_plugins"]:
        src = plugins / name
        copy_tree(src, out / "gemini/plugins" / name)
        hooks = out / "gemini/plugins" / name / "hooks.json"
        if hooks.exists():
            hooks.write_text(quote_python(hooks.read_text(encoding="utf-8")), encoding="utf-8", newline="")
    for name in g["built_plugins"]:  # only the plugin's own files; skills come from the partner's caches
        for f in sorted((plugins / name).iterdir()):
            if f.is_file():
                copy_file(f, out / "gemini/plugins" / name / f.name, built_plugin_file(name))
    for rel, live in MANIFEST["agent_bridge"]["files"].items():
        copy_file(HOME / live, out / rel)


def personal_hits(root: Path) -> list[str]:
    marks, hits = personal_markers(), []
    for f in sorted(root.rglob("*")):
        if not f.is_file():
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        low = text.lower()
        hits += [f"{f.relative_to(root)}: personal value #{i}" for i, p in enumerate(marks) if p in low]
        hits += [f"{f.relative_to(root)}: absolute user path {m[0]!r}" for m in USER_PATH.finditer(text)]
    return hits


def same_tree(a: Path, b: Path) -> list[str]:
    fa = {p.relative_to(a) for p in a.rglob("*") if p.is_file()}
    fb = {p.relative_to(b) for p in b.rglob("*") if p.is_file()}
    diff = sorted(str(p) for p in fa ^ fb)
    diff += sorted(str(p) for p in fa & fb if not filecmp.cmp(a / p, b / p, shallow=False))
    return diff


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="fail if payload/ is stale")
    args = ap.parse_args()
    payload = HERE / "payload"
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "payload"
        build(out)
        hits = personal_hits(out)
        if hits:
            print("export: personal values left in the payload:\n  " + "\n  ".join(hits))
            return 1
        if args.check:
            diff = same_tree(out, payload) if payload.exists() else ["payload/ missing"]
            if diff:
                print("export --check: payload is stale:\n  " + "\n  ".join(diff[:40]))
                return 1
            print("export --check: payload up to date")
            return 0
        if payload.exists():
            shutil.rmtree(payload)
        shutil.copytree(out, payload)
    n = sum(1 for p in payload.rglob("*") if p.is_file())
    print(f"export: wrote {n} files to {payload.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
