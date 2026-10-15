#!/usr/bin/env python3
"""Build the Business Management problem bank (subjects/business-management/data/problems.json) from its vault notes.

Every note in vault/05 - Business Management/Problem Bank/ named "Problem - Bank <ID> - <title>.md" is one bank item:
Pnn are 4-point Extra Practice problems, Cnn are 2-point short theory cases. The note carries its metadata in the YAML
frontmatter (bank_id, title, category, archetype or theme, unit, difficulty, points, time_minutes, tags, origen, official,
page) and its content in "## " sections:

    ## Statement                       -> statement_html
    ## Setup                           -> setup_html (optional: data, hypotheses, definitions)
    ## (a) <prompt> [1.5 pts]          -> one subquestion; text under the heading is part of the prompt
    ### Hint / ### Checkpoint / ### Solution   -> hint_html, checkpoint_html, solution_html of that subquestion
    ## Interpretation                  -> interpretation_html (optional)

"#### " headings become step titles. A line "![[Note#Heading]]" (Obsidian heading embed) is replaced by that section of
the named note, so the bank cards of the official exercises reuse their solved notes instead of copying them. Everything
after the "**Back to:**" line is ignored.

The tool also checks the content: subquestion points add up to the item's points, categories and points agree, every
subquestion has its hint, checkpoint and solution, and every balance-sheet row that carries both "Total assets" and
"Total liabilities and equity" shows the same figure on both sides.

It writes problems.json and problems.js (the same data as window.AE_BM_BANK, for pages opened from disk).

Usage:
    python tools/build_problem_bank.py            # rewrite problems.json and problems.js
    python tools/build_problem_bank.py --check    # exit 1 if they are stale or a note is invalid
"""
import argparse
import html
import json
import pathlib
import re
import sys

TOOLS = pathlib.Path(__file__).resolve().parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import build_topic_pages as bt  # noqa: E402

VAULT = REPO / "vault" / "05 - Business Management"
BANK = VAULT / "Problem Bank"
OUT_DIR = REPO / "subjects" / "business-management" / "data"
INDEX_NOTE = "Problem Set - Business Management Problem Bank"  # must link every bank note

CATEGORIES = {"short_theory_case": 2.0, "extra_practice_problem": 4.0}
ARCHETYPES = {
    "unordered-items": "Unordered items",
    "reverse-engineering-ratios": "Reverse engineering & ratios",
    "narrative-case": "Narrative case",
    "year-on-year-cash": "Year-on-year & cash",
    "financing-leverage": "Financing & leverage",
}
UNITS = {1: "Topic 1 · The firm", 2: "Topic 2 · Value creation", 3: "Topic 3 · Financial management (I)"}
REQUIRED = ("bank_id", "title", "category", "unit", "difficulty", "points", "time_minutes", "tags", "origen")
_NAME = re.compile(r"Problem - Bank ([PC]\d{2}) - .+\.md$")
_SUB = re.compile(r"\(([a-z])\)\s+(.*?)\s*\[(\d+(?:\.\d+)?)\s*pts?\]\s*$")
_EMBED = re.compile(r"^!\[\[([^\]#|]+)#([^\]|]+)\]\]\s*$")
_NUM = re.compile(r"\(?-?\d[\d,]*(?:\.\d+)?\)?")


class BankError(ValueError):
    pass


# --------------------------------------------------------------------------- frontmatter
def frontmatter(md, where):
    if not md.startswith("---"):
        raise BankError(f"{where}: no YAML frontmatter")
    head, body = md.split("---", 2)[1:]
    meta, key = {}, None
    for line in head.strip("\n").split("\n"):
        if not line.strip():
            continue
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            meta[key] = [] if val == "" else _scalar(val)
        elif re.match(r"^\s+-\s+", line) and key is not None and isinstance(meta[key], list):
            meta[key].append(_scalar(re.sub(r"^\s+-\s+", "", line)))
        else:
            raise BankError(f"{where}: unreadable frontmatter line {line!r}")
    return meta, body


def _scalar(val):
    if len(val) >= 2 and val[0] == val[-1] == '"':
        return val[1:-1]
    if val in ("true", "false"):
        return val == "true"
    if re.fullmatch(r"-?\d+", val):
        return int(val)
    if re.fullmatch(r"-?\d+\.\d+", val):
        return float(val)
    return val


# --------------------------------------------------------------------------- embeds and rendering
def heading_section(note, heading, where):
    path = next(iter(sorted(VAULT.rglob(f"{note}.md"))), None)
    if path is None:
        raise BankError(f"{where}: embed of unknown note {note!r}")
    lines = bt.strip_frontmatter(path.read_text(encoding="utf-8")).split("\n")
    for i, line in enumerate(lines):
        m = re.match(r"^(#{2,4}) (.*)$", line)
        if m and m.group(2).strip() == heading.strip():
            level, out = len(m.group(1)), []
            for nxt in lines[i + 1:]:
                h = re.match(r"^(#{1,4}) ", nxt)
                if (h and len(h.group(1)) <= level) or nxt.startswith("**Back to:**"):
                    break
                out.append(nxt)
            # an embedded step keeps its title; sub-headings of an embedded section become step titles
            body = [re.sub(r"^#{3,4} ", "#### ", x) for x in out]
            return ([f"#### {heading.strip()}"] if level >= 3 else []) + body
    raise BankError(f"{where}: note {note!r} has no heading {heading!r}")


def expand(lines, where):
    out = []
    for line in lines:
        m = _EMBED.match(line.strip())
        out.extend(heading_section(m.group(1), m.group(2), where) if m else [line])
    return out


def render(lines, where):
    lines = expand(lines, where)
    while lines and not lines[-1].strip():
        lines.pop()
    check_balances(lines, where)
    out, chunk = [], []
    for line in lines + ["#### \x00"]:
        if line.startswith("#### "):
            if any(x.strip() for x in chunk):
                out.append(bt.blocks(chunk))
            chunk = []
            title = line[5:].strip()
            if title != "\x00":
                out.append(f'<h4 class="step-title">{bt.inline(title)}</h4>')
        else:
            chunk.append(line)
    return "\n".join(out)


_EU = {"on": False}  # set per note: frontmatter "number_format: eu" means 1.500,25 (dot thousands, comma decimals)
_NUM_EU = re.compile(r"\(?-?\d[\d.]*(?:,\d+)?\)?")


def _amount(cell):
    cell = re.sub(r"[*$]", "", cell).strip()
    if not (_NUM_EU if _EU["on"] else _NUM).fullmatch(cell):
        return None
    neg = cell.startswith("(") or cell.startswith("-")
    digits = cell.replace(".", "").replace(",", ".") if _EU["on"] else cell.replace(",", "")
    value = float(re.sub(r"[()]", "", digits).lstrip("-"))
    return -value if neg else value


def check_balances(lines, where):
    for line in lines:
        if line.startswith("|") and "Total assets" in line and "Total liabilities and equity" in line:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            nums = [v for v in (_amount(c) for c in cells) if v is not None]
            if len(nums) != 2 or abs(nums[0] - nums[1]) > 0.005:
                raise BankError(f"{where}: balance sheet does not balance: {line.strip()}")


# --------------------------------------------------------------------------- one note
def parse_note(path):
    where = path.name
    m = _NAME.match(path.name)
    if not m:
        raise BankError(f"{where}: name must be 'Problem - Bank Pnn|Cnn - <title>.md'")
    meta, body = frontmatter(path.read_text(encoding="utf-8"), where)
    _EU["on"] = meta.get("number_format") == "eu"
    try:
        return _parse(path, where, meta, body)
    finally:
        _EU["on"] = False


def _parse(path, where, meta, body):
    missing = [k for k in REQUIRED if k not in meta]
    if missing:
        raise BankError(f"{where}: frontmatter lacks {', '.join(missing)}")
    if meta["bank_id"] != _NAME.match(path.name).group(1):
        raise BankError(f"{where}: bank_id {meta['bank_id']} does not match the file name")
    category = meta["category"]
    if category not in CATEGORIES:
        raise BankError(f"{where}: unknown category {category!r}")
    points = float(meta["points"])
    if points != CATEGORIES[category]:
        raise BankError(f"{where}: a {category} is worth {CATEGORIES[category]} points, not {points}")
    if (category == "extra_practice_problem") != meta["bank_id"].startswith("P"):
        raise BankError(f"{where}: P ids are problems, C ids are theory cases")
    archetype = meta.get("archetype")
    if category == "extra_practice_problem" and archetype not in ARCHETYPES:
        raise BankError(f"{where}: unknown archetype {archetype!r}")
    if meta["unit"] not in UNITS or meta["difficulty"] not in (1, 2, 3):
        raise BankError(f"{where}: unit must be 1-3 and difficulty 1-3")
    if category == "short_theory_case" and not meta.get("theme"):
        raise BankError(f"{where}: a theory case needs a theme (the simulator never puts two cases of one theme together)")

    body = body.split("**Back to:**")[0]
    parts = re.split(r"\n## ", "\n" + body)
    item = {
        "id": meta["bank_id"], "category": category, "archetype": archetype if category == "extra_practice_problem" else "theory-case",
        "theme": meta.get("theme") or archetype,
        "unit": meta["unit"], "title": meta["title"], "difficulty": meta["difficulty"], "points": points,
        "time_minutes": meta["time_minutes"], "tags": [t for t in meta["tags"] if t != "problem-bank"],
        "official": bool(meta.get("official", False)), "source": meta["origen"],
        "vault_note": path.relative_to(REPO).as_posix() if path.is_relative_to(REPO) else path.name,
        "page": meta.get("page"),
        "statement_html": None, "setup_html": None, "subquestions": [], "interpretation_html": None,
    }
    for part in parts[1:]:
        head, _, rest = part.partition("\n")
        head = head.strip()
        lines = rest.split("\n")
        if head == "Statement":
            item["statement_html"] = render(lines, where)
        elif head == "Setup":
            item["setup_html"] = render(lines, where)
        elif head == "Interpretation":
            item["interpretation_html"] = render(lines, where)
        elif _SUB.match(head):
            item["subquestions"].append(subquestion(head, rest, where))
        else:
            raise BankError(f"{where}: unexpected section '## {head}'")
    if not item["statement_html"]:
        raise BankError(f"{where}: no '## Statement' section")
    if not item["subquestions"]:
        raise BankError(f"{where}: no subquestions")
    labels = [s["label"] for s in item["subquestions"]]
    if labels != [chr(ord("a") + i) for i in range(len(labels))]:
        raise BankError(f"{where}: subquestions must be (a), (b), ... in order, got {labels}")
    total = round(sum(s["points"] for s in item["subquestions"]), 4)
    if total != points:
        raise BankError(f"{where}: subquestion points add up to {total}, not {points}")
    if item["page"] and not (REPO / item["page"].split("#")[0]).is_file():
        raise BankError(f"{where}: page {item['page']} does not exist")
    return item


def subquestion(head, rest, where):
    label, prompt, pts = _SUB.match(head).groups()
    blocks = re.split(r"\n### ", "\n" + rest)
    sub = {"label": label, "points": float(pts), "prompt_html": None,
           "hint_html": None, "checkpoint_html": None, "solution_html": None}
    intro = blocks[0].split("\n")
    sub["prompt_html"] = f"<p>{bt.inline(prompt)}</p>" + ("\n" + render(intro, where) if any(x.strip() for x in intro) else "")
    for block in blocks[1:]:
        name, _, text = block.partition("\n")
        key = {"Hint": "hint_html", "Checkpoint": "checkpoint_html", "Solution": "solution_html"}.get(name.strip())
        if key is None:
            raise BankError(f"{where}: ({label}) has an unexpected '### {name.strip()}'")
        sub[key] = render(text.split("\n"), f"{where} ({label})")
    for key in ("hint_html", "checkpoint_html", "solution_html"):
        if not sub[key]:
            raise BankError(f"{where}: ({label}) lacks its {key.split('_')[0]}")
    return sub


# --------------------------------------------------------------------------- whole bank
def build(bank_dir=None):
    bank_dir = pathlib.Path(bank_dir or BANK)
    items = [parse_note(p) for p in sorted(bank_dir.glob("Problem - Bank *.md"))]
    ids = [i["id"] for i in items]
    dup = sorted({x for x in ids if ids.count(x) > 1})
    if dup:
        raise BankError(f"duplicate bank ids: {', '.join(dup)}")
    index = bank_dir / f"{INDEX_NOTE}.md"
    if index.is_file():
        listed = index.read_text(encoding="utf-8")
        unlisted = [p.stem for p in sorted(bank_dir.glob("Problem - Bank *.md")) if f"[[{p.stem}" not in listed]
        if unlisted:
            raise BankError(f"{INDEX_NOTE} does not list: {', '.join(unlisted)}")
    items.sort(key=lambda i: (i["id"][0] != "C", int(i["id"][1:])))
    data = {
        "_comment": "Generated by tools/build_problem_bank.py from vault/05 - Business Management/Problem Bank/. Do not edit by hand.",
        "subject": "business-management",
        "categories": {"short_theory_case": {"label": "Short theory cases", "points": 2.0},
                       "extra_practice_problem": {"label": "Extra Practice problems", "points": 4.0}},
        "archetypes": ARCHETYPES,
        "units": {str(k): v for k, v in UNITS.items()},
        "counts": {"short_theory_case": sum(i["category"] == "short_theory_case" for i in items),
                   "extra_practice_problem": sum(i["category"] == "extra_practice_problem" for i in items)},
        "items": items,
    }
    text = json.dumps(data, indent=1, ensure_ascii=False) + "\n"
    js = ("/* Generated by tools/build_problem_bank.py (same data as problems.json). Do not edit by hand. */\n"
          f"window.AE_BM_BANK = {json.dumps(data, ensure_ascii=False)};\n")
    return {OUT_DIR / "problems.json": text, OUT_DIR / "problems.js": js}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    try:
        outputs = build()
    except BankError as exc:
        print(f"build_problem_bank: {exc}")
        return 1
    stale = 0
    for path, content in outputs.items():
        current = path.read_bytes().decode("utf-8").replace("\r\n", "\n") if path.exists() else None
        if current != content:
            stale += 1
            if args.check:
                print("stale", path.relative_to(REPO).as_posix())
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content.encode("utf-8"))
                print("wrote", path.relative_to(REPO).as_posix())
    data = json.loads(outputs[OUT_DIR / "problems.json"])
    print(f"build_problem_bank: {data['counts']['extra_practice_problem']} problems, "
          f"{data['counts']['short_theory_case']} theory cases")
    return 1 if (args.check and stale) else 0


if __name__ == "__main__":
    sys.exit(main())
