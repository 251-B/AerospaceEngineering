#!/usr/bin/env python3
"""Rewrite the lists of the index note of the Midterm 2 bank from the notes on disk (titles from their frontmatter).

    python tools/materials_bank/update_index.py
"""
import pathlib
import re
import sys

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import build_materials_bank as bmb  # noqa: E402
import build_problem_bank as bpb  # noqa: E402


def main():
    index = bmb.BANK / f"{bmb.INDEX_NOTE}.md"
    text = index.read_text(encoding="utf-8")
    head = text.split("## Test blocks")[0]
    out = [head.rstrip("\n"), "", "## Test blocks (ten questions each)", ""]
    notes = {}
    for p in sorted(bmb.BANK.glob("Quiz - Bank *.md")) + sorted(bmb.BANK.glob("Problem - Bank *.md")):
        meta, _ = bpb.frontmatter(p.read_text(encoding="utf-8"), p.name)
        notes[p.stem] = meta
    for unit, label in bmb.UNITS.items():
        out += [f"### {label}", ""]
        out += [f"- [[{stem}|{m['bank_id']}]]: {m['title']}" for stem, m in notes.items()
                if m.get("category") == bmb.BLOCK_CATEGORY and m.get("unit") == unit]
        out.append("")
    out += ["## Part II problems", ""]
    for arch, label in bmb.ARCHETYPES.items():
        out += [f"### {label}", ""]
        out += [f"- [[{stem}|{m['bank_id']}]]: {m['title']}" for stem, m in notes.items()
                if m.get("category") == bmb.PROBLEM_CATEGORY and m.get("archetype") == arch]
        out.append("")
    out.append("**Back to:** [[Aerospace Materials I MOC]]")
    new = "\n".join(out) + "\n"
    if new != text:
        index.write_text(new, encoding="utf-8", newline="\n")
        print("wrote", index.relative_to(bmb.REPO).as_posix())
    return 0


if __name__ == "__main__":
    sys.exit(main())
