"""Read a problem note of the vault back into the problem dict that build.py renders.

The notes are the source of truth: each note holds the frontmatter (id, short name, tags) and the statement,
the source line and the four phases in the markdown layout written by build.note_md. Block types are recovered
from that layout: "### " heading (h4), "- " list (ul), "| " table, "> [!kind]" callout (note), "$$ ... $$" line
(m), the bold label + "$$" + caption + table block (bal), otherwise paragraph (p).
"""
import json
import pathlib
import re

CAPTION = "Each surface integral, surface by surface (the vertical line drawn under each integral in class):"


def _scalar(value):
    value = value.strip()
    return json.loads(value) if value.startswith('"') else value


def _frontmatter(lines):
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        raise ValueError("the frontmatter must open and close with '---'")
    end = lines.index("---", 1)
    fm, key = {}, None
    for line in lines[1:end]:
        m = re.match(r"^([A-Za-z_][\w-]*):(?: (.*))?$", line)
        if m:
            key = m.group(1)
            fm[key] = [] if m.group(2) is None else _scalar(m.group(2))
        elif line.startswith("  - ") and key is not None:
            fm[key].append(_scalar(line[4:]))
    return fm, end + 1


def _chunks(lines):
    """Runs of non-empty lines: each block of the note is one run (a bal block is several)."""
    out, cur = [], []
    for line in lines:
        if line.strip():
            cur.append(line)
        elif cur:
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def _check_table(chunk):
    """A table is a header row, a separator row and the body, with no blank line inside."""
    if len(chunk) < 2 or not re.match(r"^\|(\s*:?-+:?\s*\|)+$", chunk[1].strip()):
        raise ValueError(f"table without header or separator row (a blank line inside a table?) near: {chunk[0][:60]}")


def _cells(line):
    return [c.strip() for c in line.strip()[1:-1].split("|")]


def _is_bal(chunks, i):
    return (i + 2 < len(chunks) and len(chunks[i]) == 1 and chunks[i][0].startswith("**") and chunks[i][0].endswith("**")
            and len(chunks[i + 1]) == 1 and chunks[i + 1][0].startswith("$$ ") and chunks[i + 2][0] == CAPTION)


def _bal(chunks, i):
    label, eq = chunks[i][0][2:-2], chunks[i + 1][0][3:-3]
    table = chunks[i + 3]
    _check_table(table)
    cols = [c[1:-1] for c in _cells(table[0])[1:]]
    rows = []
    for line in table[2:]:
        cells = _cells(line)
        first = cells[0]
        wall = first.startswith("**")
        inner = first[2:first.index("** (boxed)")] if wall else first
        rows.append((inner[1:-1], cells[1:], wall))
    j, wall = i + 4, None
    if not chunks[j][0].startswith("$$ "):
        wall = "\n".join(chunks[j])
        j += 1
    result = chunks[j][0][3:-3]
    bal = {"label": label, "eq": eq, "cols": cols, "rows": rows, "result": result}
    if wall is not None:
        bal["wall"] = wall
    return bal, j + 1


def _is_figure(ch):
    """An embedded figure and its caption: placed by build.py from the figure registry, not part of the content."""
    return len(ch) == 2 and ch[0].startswith("![[attachments/FM-T3/") and ch[0].endswith("]]") and ch[1].startswith("*")


def _blocks(lines):
    chunks, blocks, i = _chunks(lines), [], 0
    while i < len(chunks):
        ch = chunks[i]
        if _is_figure(ch):
            i += 1
            continue
        if _is_bal(chunks, i):
            bal, i = _bal(chunks, i)
            blocks.append(("bal", bal))
            continue
        if len(ch) == 1 and ch[0].startswith("### "):
            blocks.append(("h4", ch[0][4:]))
        elif all(line.startswith("- ") for line in ch):
            blocks.append(("ul", [line[2:] for line in ch]))
        elif ch[0].startswith("> [!"):
            kind_title = re.match(r"^> \[!\w+\] (.*)$", ch[0])
            blocks.append(("note", kind_title.group(1), ch[1][2:] if len(ch) > 1 else ""))
        elif ch[0].startswith("| "):
            _check_table(ch)
            blocks.append(("table", _cells(ch[0]), [_cells(line) for line in ch[2:]]))
        elif len(ch) == 1 and ch[0].startswith("$$ ") and ch[0].endswith(" $$"):
            blocks.append(("m", ch[0][3:-3]))
        else:
            blocks.append(("p", "\n".join(ch)))
        i += 1
    return blocks


def read_problem(path):
    """The problem dict of one note; a malformed note raises ValueError naming the file."""
    path = pathlib.Path(path)
    try:
        return _read(path)
    except ValueError as err:
        raise ValueError(f"{path.name}: {err}") from None


def _read(path):
    lines = path.read_text(encoding="utf-8").split("\n")
    fm, body_at = _frontmatter(lines)
    for key in ("id", "pill", "tags", "tags_html"):
        if key not in fm:
            raise ValueError(f"the frontmatter lacks '{key}'")
    body = lines[body_at:]
    heading = next((re.match(r"^# Problem (CL\d+): (.*)$", l) for l in body if l.startswith("# Problem ")), None)
    if heading is None:
        raise ValueError("missing the '# Problem CLn: title' heading")
    num, title = heading.groups()

    sections, name = [], None
    for line in body:
        if line.startswith("## "):
            name = line[3:]
            sections.append((name, []))
        elif name is not None:
            sections[-1][1].append(line)
    lines_of = dict(sections)
    if "Statement" not in lines_of:
        raise ValueError("missing the '## Statement' section")

    statement_chunks = _chunks(lines_of["Statement"])
    source_line = "\n".join(statement_chunks[-1]) if statement_chunks else ""
    if not source_line.startswith("Source: "):
        raise ValueError("the statement must end with the 'Source: ...' line")
    statement = _blocks(lines_of["Statement"][:lines_of["Statement"].index(statement_chunks[-1][0])])

    phases = []
    for name, body_lines in sections:
        if name.startswith("Phase "):
            badge, head = name.split(": ", 1)
            phases.append((badge, head, _blocks(body_lines)))

    problem = {"id": fm["id"], "pill": fm["pill"], "title": title, "note_title": path.stem,
               "tags_md": fm["tags"], "tags_html": fm["tags_html"], "statement": statement,
               "source_line": source_line, "phases": phases}
    if "dificultad" in fm and fm["dificultad"] != "media":
        problem["difficulty"] = fm["dificultad"]
    return problem


def read_all(vault_dir):
    """Every problem note of the subject, in problem order."""
    notes = sorted(pathlib.Path(vault_dir).glob("Problem - CL*.md"), key=lambda p: int(re.search(r"CL(\d+)", p.name).group(1)))
    return [read_problem(p) for p in notes]
