#!/usr/bin/env python3
"""Rename vault notes and rewrite every wikilink that points at them.

    python tools/vault_rename.py map.json            # dry run: print what would change
    python tools/vault_rename.py map.json --apply    # rename files and rewrite links

map.json: {"Old note name": "New note name", ...} (names without .md). Links such as
[[Old]], [[Old|alias]], [[Old#Heading]], ![[Old]] are rewritten; fenced code is left alone.
Refuses to run if a new name already exists or two notes would share a name.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
_LINK = re.compile(r"(!?\[\[)([^\]\|#\n]+)((?:#[^\]\|\n]*)?(?:\|[^\]\n]*)?\]\])")
_FENCE = re.compile(r"^(```|~~~)")


def rewrite_links(text: str, mapping: dict[str, str]) -> tuple[str, int]:
    count = 0
    out, marker = [], None  # marker: the fence opener ("```" or "~~~") while inside a code block
    for line in text.splitlines(keepends=True):
        m = _FENCE.match(line.lstrip())
        if m and marker is None:
            marker = m.group(1)
            out.append(line)
            continue
        if marker is not None:
            if m and m.group(1) == marker and line.strip().startswith(marker) and not line.strip().strip(marker[0]):
                marker = None
            out.append(line)
            continue

        def sub(m):
            nonlocal count
            target = m.group(2).strip()
            head, sep, leaf = target.rpartition("/")
            suffix = ".md" if leaf.endswith(".md") else ""
            name = leaf[: -len(suffix)] if suffix else leaf
            if name in mapping:
                count += 1
                return m.group(1) + head + sep + mapping[name] + suffix + m.group(3)
            return m.group(0)

        out.append(_LINK.sub(sub, line))
    return "".join(out), count


def plan(vault: pathlib.Path, mapping: dict[str, str]):
    notes = {p.stem: p for p in vault.rglob("*.md")}
    errors = []
    for old, new in mapping.items():
        if old not in notes:
            errors.append(f"missing source note: {old}")
        if new in notes and new != old:
            errors.append(f"target already exists: {new}")
        if re.search(r'[:?"/\\|*<>]', new):
            errors.append(f"illegal character in new name: {new}")
    if len(set(mapping.values())) != len(mapping):
        errors.append("two notes map to the same new name")
    return notes, errors


def apply(vault: pathlib.Path, mapping: dict[str, str], do_it: bool, links_only: bool = False):
    notes, errors = plan(vault, mapping) if not links_only else ({}, [])
    if errors:
        for e in errors:
            print("ERROR:", e)
        return 1
    rewritten = links = 0
    for path in vault.rglob("*.md"):
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            continue
        new_text, n = rewrite_links(text, mapping)
        if n:
            rewritten += 1
            links += n
            if do_it:
                path.write_bytes(new_text.encode("utf-8"))
    if not links_only:
        for old, new in mapping.items():
            src = notes[old]
            if do_it:
                src.rename(src.with_name(new + ".md"))
    verb = ("rewrote links only" if links_only else "renamed") if do_it else "would rename"
    print(f"{verb} {len(mapping)} notes; rewrote {links} links in {rewritten} files")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("map")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--links-only", action="store_true", help="only rewrite links (notes were already renamed)")
    ap.add_argument("--vault", default=str(REPO / "vault"))
    args = ap.parse_args(argv)
    mapping = json.loads(pathlib.Path(args.map).read_text(encoding="utf-8"))
    return apply(pathlib.Path(args.vault), mapping, args.apply, args.links_only)


if __name__ == "__main__":
    sys.exit(main())
