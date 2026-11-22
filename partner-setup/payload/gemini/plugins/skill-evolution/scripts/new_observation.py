#!/usr/bin/env python3
"""Create a new observation markdown file in skill-observations/observation-log/.

Windows-safe replacement for task-observer's bash id-derivation and archival snippet:
1. Archives resolved observations (actioned|declined|superseded with resolved < today).
2. Computes next_id = max(max_active, max_archive, .id-floor) + 1.
3. Creates NNNN-<slug>.md atomically with exclusive creation ('x') and valid YAML frontmatter.
4. Updates archive/.id-floor and prints the created absolute file path.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path

DEFAULT_OBS_ROOT = Path(r"{{HOME}}/.agent-bridge/skill-observations")
RESOLVED_STATUSES = {"actioned", "declined", "superseded"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_PREFIX_RE = re.compile(r"^(\d+)-.*\.md$")


def yaml_quote(text: str) -> str:
    escaped = text.replace("\\", "\\\\").replace('"', '\\"').replace("\r", " ").replace("\n", " ")
    return f'"{escaped}"'


def yaml_list(items: list[str]) -> str:
    if not items:
        return "[]"
    rendered = []
    for item in items:
        item = item.strip()
        if not item:
            continue
        if ":" in item or any(ch in item for ch in ('"', "'", "[", "]", "{", "}", "#", " ")):
            rendered.append(yaml_quote(item))
        else:
            rendered.append(item)
    return "[" + ", ".join(rendered) + "]"


def parse_status_and_resolved(path: Path) -> tuple[str, str]:
    status = ""
    resolved = ""
    try:
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            first = fh.readline()
            if not re.match(r"^---\s*$", first):
                return status, resolved
            for line in fh:
                if re.match(r"^---\s*$", line):
                    break
                m_st = re.match(r"^status:\s*(\S+)", line)
                if m_st:
                    status = m_st.group(1).strip().strip('"\'').lower()
                m_res = re.match(r"^resolved:\s*(\S+)", line)
                if m_res:
                    resolved = m_res.group(1).strip().strip('"\'')
    except OSError:
        pass
    return status, resolved


def archive_stale_resolved(log_dir: Path, archive_dir: Path, today_str: str) -> None:
    for md_file in sorted(log_dir.glob("*.md")):
        if not md_file.is_file():
            continue
        status, resolved = parse_status_and_resolved(md_file)
        if status in RESOLVED_STATUSES and DATE_RE.match(resolved) and resolved < today_str:
            dest = archive_dir / md_file.name
            if not dest.exists():
                shutil.move(str(md_file), str(dest))


def read_id_floor(floor_file: Path) -> int:
    if not floor_file.is_file():
        return 0
    raw = floor_file.read_text(encoding="utf-8", errors="replace")
    digits = re.sub(r"[^0-9]", "", raw)
    return int(digits) if digits else 0


def max_file_id(directory: Path) -> int:
    hi = 0
    if not directory.is_dir():
        return hi
    for entry in directory.iterdir():
        if not entry.is_file():
            continue
        m = ID_PREFIX_RE.match(entry.name)
        if m:
            hi = max(hi, int(m.group(1), 10))
    return hi


def normalize_slug(raw: str) -> str:
    slug = re.sub(r"[^a-z0-9-]+", "-", raw.strip().lower())
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    if not slug:
        raise ValueError(f"Invalid slug: {raw!r}")
    return slug


def parse_csv(raw: str | None) -> list[str]:
    if not raw:
        return []
    return [part.strip() for part in raw.split(",") if part.strip()]


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Atomically archive stale resolved observations and create a new NNNN-slug.md observation file."
    )
    parser.add_argument("slug", help="Kebab-case slug for the observation filename (e.g. 'pdf-crop-dpi-check').")
    parser.add_argument("--title", required=True, help="Short descriptive title for the observation.")
    parser.add_argument("--area", required=True, help="Which part of the skill or workflow this concerns.")
    parser.add_argument("--context", required=True, help="Task or session context where this was observed.")
    parser.add_argument("--skill", default="", help="Comma-separated existing skill names this improves.")
    parser.add_argument("--proposes", default="", help="Comma-separated proposed new skill names.")
    parser.add_argument("--target-file", default="", help="Comma-separated non-skill target file paths.")
    parser.add_argument("--siblings", default="none", help="Siblings checked verdict (defaults to 'none').")
    parser.add_argument(
        "--type",
        dest="obs_type",
        choices=("internal", "open-source"),
        default="internal",
        help="Observation confidentiality type (default: internal).",
    )
    parser.add_argument("--issue", default="[Describe what happened with specific evidence.]", help="Issue body text.")
    parser.add_argument(
        "--improvement",
        default="[Describe concrete skill/workflow change or proposed skill scope.]",
        help="Suggested improvement body text.",
    )
    parser.add_argument(
        "--principle",
        default="[State the generalisable takeaway.]",
        help="Generalisable principle body text.",
    )
    parser.add_argument("--reference", default="", help="Optional path to saved evidence.")
    parser.add_argument(
        "--obs-root",
        default=str(DEFAULT_OBS_ROOT),
        help="Root directory of skill-observations (default: global Antigravity store).",
    )
    return parser


def main() -> int:
    parser = build_arg_parser()
    args = parser.parse_args()

    slug = normalize_slug(args.slug)
    obs_root = Path(args.obs_root)
    log_dir = obs_root / "observation-log"
    archive_dir = log_dir / "archive"
    floor_file = archive_dir / ".id-floor"

    log_dir.mkdir(parents=True, exist_ok=True)
    archive_dir.mkdir(parents=True, exist_ok=True)

    today_str = dt.date.today().isoformat()
    archive_stale_resolved(log_dir, archive_dir, today_str)

    floor = read_id_floor(floor_file)
    hi = max(max_file_id(log_dir), max_file_id(archive_dir))
    next_id = max(hi, floor) + 1
    prefix = f"{next_id:04d}-"

    existing_collisions = [
        p for p in (*log_dir.glob(f"{prefix}*.md"), *archive_dir.glob(f"{prefix}*.md")) if p.is_file()
    ]
    if existing_collisions:
        print(f"ERROR: ID collision for prefix {prefix}: {existing_collisions[0]}", file=sys.stderr)
        return 1

    target_path = log_dir / f"{prefix}{slug}.md"

    skills = parse_csv(args.skill)
    proposes = parse_csv(args.proposes)
    targets = parse_csv(args.target_file)

    lines = [
        "---",
        f"id: {next_id}",
        f"title: {yaml_quote(args.title)}",
        "status: open",
        f"type: {args.obs_type}",
        f"skill: {yaml_list(skills)}",
        f"proposes_skill: {yaml_list(proposes)}",
        f"target_file: {yaml_list(targets)}",
        f"siblings_checked: {yaml_quote(args.siblings)}",
        f"area: {yaml_quote(args.area)}",
        f"date: {today_str}",
        f"session_context: {yaml_quote(args.context)}",
        "parked_until:",
        "resolved:",
        "resolution:",
        f"reference: {yaml_quote(args.reference) if args.reference else ''}".rstrip(),
        "commands_verified: none",
        "---",
        "",
        f"**Issue:** {args.issue}",
        "",
        f"**Suggested improvement:** {args.improvement}",
        "",
        f"**Principle:** {args.principle}",
        "",
    ]
    content = "\n".join(lines)

    with target_path.open("x", encoding="utf-8", newline="\n") as fh:
        fh.write(content)

    floor_file.write_text(f"{next_id}\n", encoding="utf-8")
    print(str(target_path.resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
