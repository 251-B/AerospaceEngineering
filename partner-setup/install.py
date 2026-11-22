#!/usr/bin/env python3
"""Reproduce the owner's Claude Code + Antigravity setup on this computer.

Stdlib only, Python 3.10+. Run from the repository root:

    python partner-setup/install.py plan      # show every action, change nothing
    python partner-setup/install.py apply     # back up, then install
    python partner-setup/install.py check     # verify; exit 1 on any failure

Options: --skip-cli (files only: no claude/agy/npx commands), --install-deps
(pip install the Python package `mcp` if missing), --home DIR (target another
home folder, used by the tests). Every file it replaces is first copied to
~/.ae-setup-backup/<timestamp>/. Nothing personal is read from or sent anywhere.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAYLOAD = HERE / "payload"
REPO = HERE.parent
M = json.loads((HERE / "manifest.json").read_text(encoding="utf-8"))
MARK_START = "<!-- AE-PARTNER-SETUP:START (managed by partner-setup/install.py) -->"
MARK_END = "<!-- AE-PARTNER-SETUP:END -->"
TAGS = ("{{HOME}}", "{{PYTHON}}", "{{REPO}}", "{{CLAUDE_EXE}}", "{{AGY_EXE}}")


class Ctx:
    def __init__(self, home: Path, dry: bool, skip_cli: bool):
        self.home, self.dry, self.skip_cli = home, dry, skip_cli
        self.backup = home / ".ae-setup-backup" / time.strftime("%Y%m%d-%H%M%S")
        claude = shutil.which("claude") or str(home / ".local/bin/claude.exe")
        agy = shutil.which("agy") or str(home / "AppData/Local/agy/bin/agy.exe")
        self.values = {
            "{{HOME}}": home.as_posix(),
            "{{PYTHON}}": Path(sys.executable).as_posix(),
            "{{REPO}}": REPO.as_posix(),
            "{{CLAUDE_EXE}}": Path(claude).as_posix(),
            "{{AGY_EXE}}": Path(agy).as_posix(),
        }
        self.claude, self.agy = claude, agy

    # -- helpers -------------------------------------------------------------
    def say(self, msg: str) -> None:
        print(("[plan] " if self.dry else "") + msg)

    def fill(self, text: str) -> str:
        for tag, value in self.values.items():
            text = text.replace(tag, value)
        return text

    def save(self, target: Path) -> None:
        """Copy an existing file or folder to the backup folder before it changes."""
        if self.dry or not target.exists():
            return
        dst = self.backup / target.relative_to(self.home)
        if dst.exists():
            return
        dst.parent.mkdir(parents=True, exist_ok=True)
        (shutil.copytree if target.is_dir() else shutil.copy2)(target, dst)

    def write(self, target: Path, text: str) -> None:
        if target.exists() and target.read_text(encoding="utf-8", errors="replace") == text:
            return
        self.say(f"write {target}")
        if self.dry:
            return
        self.save(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8", newline="")

    def tree(self, src: Path, dst: Path) -> None:
        """Replace dst with a filled-in copy of src (backed up first)."""
        self.say(f"install folder {dst}")
        if self.dry:
            return
        self.save(dst)
        if dst.exists():
            shutil.rmtree(dst)
        for f in sorted(src.rglob("*")):
            if not f.is_file() or "__pycache__" in f.parts:
                continue
            out = dst / f.relative_to(src)
            out.parent.mkdir(parents=True, exist_ok=True)
            try:
                out.write_text(self.fill(f.read_text(encoding="utf-8")), encoding="utf-8", newline="")
            except UnicodeDecodeError:
                shutil.copyfile(f, out)

    def edit_json(self, target: Path, change) -> None:
        data = json.loads(target.read_text(encoding="utf-8")) if target.exists() else {}
        new = json.loads(json.dumps(data))
        change(new)
        if new != data:
            self.write(target, json.dumps(new, indent=2, ensure_ascii=False) + "\n")

    def run(self, args: list[str], ok_codes=(0,), quiet=False) -> subprocess.CompletedProcess | None:
        self.say("run " + " ".join(args))
        if self.dry or self.skip_cli:
            return None
        # A CLI installed during this session may not be on this process's PATH yet.
        exe = shutil.which(args[0]) or {"claude": self.claude, "agy": self.agy}.get(args[0], args[0])
        try:
            p = subprocess.run([exe, *args[1:]], capture_output=True, text=True, encoding="utf-8", errors="replace")
        except FileNotFoundError:
            print(f"  ! command not found: {args[0]} (install it, open a new terminal, run apply again)")
            return None
        if p.returncode not in ok_codes and not quiet:
            print(f"  ! exit {p.returncode}: {(p.stderr or p.stdout).strip()[:400]}")
        return p


def newest_version(base: Path) -> Path | None:
    """Highest version folder under a plugin cache (e.g. .../superpowers/6.4.2)."""
    def key(p: Path):  # 13.34.2 ranks above 13.34.2-beta.1
        core = p.name.split("-")[0]
        return ([int(x) if x.isdigit() else 0 for x in core.split(".")], 0 if "-" in p.name else 1)
    dirs = [d for d in base.glob("*") if d.is_dir() and (d / "skills").is_dir() and not (d / ".orphaned_at").exists()]
    return max(dirs, key=key) if dirs else None


# -- install steps -------------------------------------------------------------
def claude_files(c: Ctx) -> None:
    for rel, target in M["claude"]["files"].items():
        text = c.fill((PAYLOAD / rel).read_text(encoding="utf-8"))
        dst = c.home / target
        if rel.endswith("CLAUDE.md"):  # keep the partner's own global instructions
            old = dst.read_text(encoding="utf-8") if dst.exists() else ""
            block = f"{MARK_START}\n{text.rstrip()}\n{MARK_END}\n"
            if MARK_START in old:
                text = re.sub(re.escape(MARK_START) + r".*?" + re.escape(MARK_END) + r"\n?", lambda _: block, old, flags=re.S)
            else:
                text = (old.rstrip() + "\n\n" if old.strip() else "") + block
        c.write(dst, text)
    for name in M["claude"]["vendored_skills"]:
        c.tree(PAYLOAD / "claude/skills" / name, c.home / ".claude/skills" / name)


def claude_settings(c: Ctx) -> None:
    cfg = M["claude"]

    def change(s: dict) -> None:
        hooks = s.setdefault("hooks", {})
        for event, cmd in cfg["hooks"].items():
            groups = [g for g in hooks.get(event, []) if not any("skill_router.py" in h.get("command", "") for h in g.get("hooks", []))]
            groups.append({"hooks": [{"type": "command", "command": c.fill(cmd)}]})
            hooks[event] = groups
        for pid in cfg["plugins"]:
            s.setdefault("enabledPlugins", {})[pid] = True
        for mk in cfg["marketplaces"]:
            s.setdefault("extraKnownMarketplaces", {})[mk["name"]] = {"source": mk["settings"]}

    c.edit_json(c.home / ".claude/settings.json", change)


def claude_cli(c: Ctx) -> None:
    cfg = M["claude"]
    listed = c.run(["claude", "plugin", "marketplace", "list"], quiet=True)
    for mk in cfg["marketplaces"]:
        if not listed or mk["name"] not in listed.stdout:
            c.run(["claude", "plugin", "marketplace", "add", mk["source"]])
    installed = c.run(["claude", "plugin", "list"], quiet=True)
    for pid in cfg["plugins"]:
        if not installed or pid not in installed.stdout:
            c.run(["claude", "plugin", "install", pid, "--scope", "user"])
    for srv in cfg["mcp"]:
        c.run(["claude", "mcp", "remove", srv["name"], "-s", "user"], quiet=True)
        c.run(["claude", "mcp", "add", "-s", "user", srv["name"], "--", c.fill(srv["command"]), *map(c.fill, srv["args"])])
    for up in cfg["upstream_skills"]:
        c.run(["npx", "-y", cfg["skills_cli"], "add", up["repo"], "-g", "-a", "claude-code", "-s", *up["skills"], "-y", "--copy"])


def enable_invocation(c: Ctx) -> None:
    for name in M["claude"]["enable_model_invocation"]:
        f = c.home / ".claude/skills" / name / "SKILL.md"
        if f.exists():
            text = f.read_text(encoding="utf-8")
            c.write(f, text.replace("disable-model-invocation: true", "disable-model-invocation: false"))


def gemini_plugins(c: Ctx) -> None:
    g = M["gemini"]
    plugins = c.home / ".gemini/config/plugins"
    for name in g["vendored_plugins"]:
        c.tree(PAYLOAD / "gemini/plugins" / name, plugins / name)
    for name, spec in g["built_plugins"].items():
        src_root = c.home / spec["from"]
        if spec["from"].endswith("skills"):
            skills_root = src_root
        else:
            ver = newest_version(src_root)
            skills_root = ver / "skills" if ver else None
        c.tree(PAYLOAD / "gemini/plugins" / name, plugins / name)
        for skill in spec["skills"]:
            src = skills_root / skill if skills_root else None
            if not src or not src.is_dir():
                c.say(f"  ! {name}: skill {skill} not found under {src_root} (install the Claude plugin/skills first)")
                continue
            dst = plugins / name / "skills" / skill
            c.say(f"copy skill {skill} -> {dst}")
            if not c.dry:
                shutil.copytree(src, dst, dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__"))

    def change(cfg: dict) -> None:
        for name in [*g["vendored_plugins"], *g["built_plugins"]]:
            cfg.setdefault("plugins", {}).setdefault(name, {})["enabled"] = True
        cfg.setdefault("userSettings", {}).update(g["user_settings"])

    c.edit_json(c.home / ".gemini/config/config.json", change)
    for pid in g["marketplace_plugins"]:
        c.run(["agy", "plugin", "install", pid])


DRIVELESS = re.compile(r"^(read_file|write_file)\(/[^:]*\)$")  # breaks agy's sandbox on Windows


def cli_permissions(home: Path) -> tuple[list[str], list[str]]:
    repo, h = REPO.as_posix(), home.as_posix()  # absolute, with drive letter on Windows
    allow = [f"read_file({repo})", f"write_file({repo})",
             f"read_file({h}/.agent-bridge)", f"write_file({h}/.agent-bridge)",
             "mcp(agent-bridge_claude-bridge/*)", "mcp(claude-bridge/*)",
             "mcp(claude-mem_claude-mem/*)", "mcp(claude-mem/*)",
             r"command(regex:^(git|python|py|node|npm|npx|echo|dir|ls|Get-ChildItem|Get-Content|Test-Path)\b.*)"]
    deny = [r"command(regex:.*(rm -rf|Remove-Item.*-Recurse|git push --force|git reset --hard).*)"]
    return allow, deny


def gemini_cli_settings(c: Ctx) -> None:
    allow, deny = cli_permissions(c.home)

    def change(s: dict) -> None:
        perms = s.setdefault("permissions", {})
        if os.name == "nt":
            perms["allow"] = [x for x in perms.get("allow", []) if not DRIVELESS.match(x)]
        for key, items in (("allow", allow), ("deny", deny)):
            lst = perms.setdefault(key, [])
            lst += [x for x in items if x not in lst]
        trusted = s.setdefault("trustedWorkspaces", [])
        if str(REPO) not in trusted:
            trusted.append(str(REPO))

    c.edit_json(c.home / ".gemini/antigravity-cli/settings.json", change)


def agent_bridge(c: Ctx) -> None:
    root = c.home / ".agent-bridge"
    for d in ("tmp", "skill-observations/observation-log/archive", "skill-observations/reviews"):
        if not (root / d).exists():
            c.say(f"mkdir {root / d}")
            if not c.dry:
                (root / d).mkdir(parents=True, exist_ok=True)
    obs = root / "skill-observations"
    if not (obs / "last-review-date.txt").exists():
        c.write(obs / "last-review-date.txt", "never\n")
    if not (obs / "cross-cutting-principles.md").exists():
        c.write(obs / "cross-cutting-principles.md", "# Cross-Cutting Principles\n\nPrinciples that apply to all skills. Read as a mandatory checklist during\nany skill creation or regeneration.\n\n---\n\n## Active Principles\n")
    for rel, target in M["agent_bridge"]["files"].items():
        c.write(c.home / target, c.fill((PAYLOAD / rel).read_text(encoding="utf-8")))


def python_deps(c: Ctx, install: bool) -> None:
    try:
        import mcp  # noqa: F401
        return
    except ImportError:
        pass
    if install:
        c.run([sys.executable, "-m", "pip", "install", "--user", "mcp"])
    else:
        c.say(f"  ! Python package 'mcp' missing: run  {sys.executable} -m pip install --user mcp")


def apply(c: Ctx, install_deps: bool) -> None:
    python_deps(c, install_deps)
    claude_files(c)
    claude_settings(c)
    claude_cli(c)
    enable_invocation(c)
    agent_bridge(c)
    gemini_plugins(c)
    gemini_cli_settings(c)
    if not c.dry and c.backup.exists():
        print(f"backup of replaced files: {c.backup}")


# -- check -----------------------------------------------------------------------
def check(c: Ctx) -> int:
    rows: list[tuple[str, bool, str]] = []

    def add(name: str, ok: bool, detail: str = "") -> None:
        rows.append((name, ok, detail))

    for rel, target in M["claude"]["files"].items():
        want = c.fill((PAYLOAD / rel).read_text(encoding="utf-8"))
        dst = c.home / target
        have = dst.read_text(encoding="utf-8") if dst.exists() else ""
        ok = want.rstrip() in have if rel.endswith("CLAUDE.md") else have == want
        add(f"file ~/{target}", ok, "" if ok else "missing or different from payload")
    for name in M["claude"]["vendored_skills"]:
        add(f"skill {name}", (c.home / ".claude/skills" / name / "SKILL.md").exists())
    settings = c.home / ".claude/settings.json"
    s = json.loads(settings.read_text(encoding="utf-8")) if settings.exists() else {}
    for event, cmd in M["claude"]["hooks"].items():
        cmds = [h.get("command") for g in s.get("hooks", {}).get(event, []) for h in g.get("hooks", [])]
        add(f"hook {event}", c.fill(cmd) in cmds)

    leftovers = []
    for base in (c.home / ".claude/hooks", c.home / ".gemini/config/plugins", c.home / ".agent-bridge"):
        for f in base.rglob("*") if base.exists() else []:
            if f.is_file() and f.suffix in {".py", ".json", ".md"}:
                try:
                    t = f.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    continue
                if any(tag in t for tag in TAGS):
                    leftovers.append(str(f))
    add("no unfilled placeholders", not leftovers, ", ".join(leftovers[:3]))

    env = {**os.environ, "CLAUDE_PROJECT_DIR": str(REPO), "USERPROFILE": str(c.home), "HOME": str(c.home)}
    router = c.home / ".claude/hooks/skill_router.py"
    n_rules = len(json.loads((PAYLOAD / "claude/skill_rules.json").read_text(encoding="utf-8"))["rules"])
    n_rules += len(json.loads((REPO / ".claude/skill_rules.json").read_text(encoding="utf-8"))["rules"])
    if router.exists():
        p = subprocess.run([sys.executable, str(router), "--selftest"], capture_output=True, text=True, env=env)
        add("router selftest", p.returncode == 0 and f"{n_rules} rules" in p.stdout, p.stdout.strip() or p.stderr.strip()[:200])
        p = subprocess.run([sys.executable, str(router)], input=json.dumps({"prompt": "la página da un 404"}), capture_output=True, text=True, env=env, encoding="utf-8")
        add("router note on '404'", "systematic-debugging" in p.stdout)
        p = subprocess.run([sys.executable, str(router)], input=json.dumps({"prompt": "hola"}), capture_output=True, text=True, env=env, encoding="utf-8")
        add("router silent on 'hola'", p.stdout.strip() == "")
    else:
        add("router selftest", False, "skill_router.py missing")
    agy_router = c.home / ".gemini/config/plugins/agent-bridge/hooks/agy_skill_router.py"
    if agy_router.exists():
        payload = {"lastUserInput": "la página da un 404", "conversationId": f"check-{time.time_ns()}", "cwd": str(REPO)}
        p = subprocess.run([sys.executable, str(agy_router)], input=json.dumps(payload), capture_output=True, text=True,
                           env=env, encoding="utf-8")
        add("Antigravity router note", "systematic-debugging" in p.stdout, (p.stderr or "").strip()[:200])
        p = subprocess.run([sys.executable, str(agy_router), "--selftest"], capture_output=True, text=True, env=env, encoding="utf-8")
        add("Antigravity router selftest", p.returncode == 0, (p.stdout or p.stderr).strip()[:120])
    else:
        add("Antigravity router note", False, "agy_skill_router.py missing")
    for name in M["claude"]["enable_model_invocation"]:
        f = c.home / ".claude/skills" / name / "SKILL.md"
        if f.exists():
            add(f"{name} invocable", "disable-model-invocation: true" not in f.read_text(encoding="utf-8"))
    cli = c.home / ".gemini/antigravity-cli/settings.json"
    cs = json.loads(cli.read_text(encoding="utf-8")) if cli.exists() else {}
    have = cs.get("permissions", {}).get("allow", [])
    want, _ = cli_permissions(c.home)
    add("Antigravity CLI permissions", all(x in have for x in want) and not any(DRIVELESS.match(x) for x in have),
        "" if cli.exists() else "settings.json missing")
    add("Antigravity trusted workspace", str(REPO) in cs.get("trustedWorkspaces", []))

    plugins = c.home / ".gemini/config/plugins"
    for name in M["gemini"]["vendored_plugins"]:
        add(f"Antigravity plugin {name}", (plugins / name / "plugin.json").exists())
    for name, spec in M["gemini"]["built_plugins"].items():
        missing = [k for k in spec["skills"] if not (plugins / name / "skills" / k / "SKILL.md").exists()]
        add(f"Antigravity plugin {name}", not missing, ("missing: " + ", ".join(missing[:4])) if missing else "")
    cfg = c.home / ".gemini/config/config.json"
    g = json.loads(cfg.read_text(encoding="utf-8")) if cfg.exists() else {}
    off = [n for n in [*M["gemini"]["vendored_plugins"], *M["gemini"]["built_plugins"]] if not g.get("plugins", {}).get(n, {}).get("enabled")]
    add("Antigravity config.json plugins", not off, ", ".join(off))
    for f in M["agent_bridge"]["files"].values():
        add(f"file ~/{f}", (c.home / f).exists())
    add("observation log folder", (c.home / ".agent-bridge/skill-observations/observation-log").is_dir())
    try:
        import mcp  # noqa: F401
        add("Python package mcp", True)
    except ImportError:
        add("Python package mcp", False, f"{sys.executable} -m pip install --user mcp")

    if not c.skip_cli:
        cache = c.home / ".claude/plugins"
        mem = list(cache.glob("cache/thedotmack/claude-mem/*/scripts/mcp-server.cjs")) + list(cache.glob("marketplaces/thedotmack/plugin/scripts/mcp-server.cjs"))
        add("claude-mem MCP server for Antigravity", bool(mem), "" if mem else "install the Claude plugin claude-mem first")
        for pid in M["gemini"]["marketplace_plugins"]:
            name = pid.split("@")[0]
            add(f"Antigravity plugin {name}", (plugins / name).is_dir(), "agy plugin install " + pid)
        for tool in ("claude", "agy", "npx", "node", "git"):
            add(f"command {tool}", bool(shutil.which(tool)) or (tool in ("claude", "agy") and Path(getattr(c, tool)).exists()))
        lp = subprocess.run([c.claude, "plugin", "list"], capture_output=True, text=True, encoding="utf-8", errors="replace") if Path(c.claude).exists() or shutil.which("claude") else None
        for pid in M["claude"]["plugins"]:
            add(f"Claude plugin {pid}", bool(lp) and pid in lp.stdout)
        ml = subprocess.run([c.claude, "mcp", "list"], capture_output=True, text=True, encoding="utf-8", errors="replace") if lp else None
        for srv in M["claude"]["mcp"]:
            add(f"Claude MCP {srv['name']}", bool(ml) and srv["name"] in ml.stdout)
        for up in M["claude"]["upstream_skills"]:
            miss = [k for k in up["skills"] if not (c.home / ".claude/skills" / k / "SKILL.md").exists()]
            add(f"skills from {up['repo']}", not miss, ", ".join(miss[:4]))

    width = max(len(r[0]) for r in rows)
    for name, ok, detail in rows:
        print(f"{'OK  ' if ok else 'FAIL'}  {name.ljust(width)}  {detail}")
    failed = sum(1 for r in rows if not r[1])
    print(f"\n{len(rows) - failed}/{len(rows)} checks passed")
    return 1 if failed else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("action", choices=["plan", "apply", "check"])
    ap.add_argument("--home", type=Path, default=Path.home())
    ap.add_argument("--skip-cli", action="store_true", help="no claude/agy/npx commands")
    ap.add_argument("--install-deps", action="store_true", help="pip install the Python package mcp")
    a = ap.parse_args()
    c = Ctx(a.home.resolve(), dry=a.action == "plan", skip_cli=a.skip_cli)
    if a.action == "check":
        return check(c)
    apply(c, a.install_deps)
    print("\nNext: python partner-setup/install.py check" if a.action == "apply" else "\n(plan only: nothing was changed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
