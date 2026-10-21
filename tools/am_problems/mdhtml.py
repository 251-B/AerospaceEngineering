"""Markdown (vault note dialect of the Advanced Maths problem sheets) -> HTML blocks.  Pure stdlib.

Dialect: paragraphs, `#### step headings`, `- bullets`, `1. numbered`, pipe tables, `$...$` and `$$...$$` maths
(display maths on one line or between two `$$` lines), `> [!kind] Title` callouts (kind: info, warning, result),
figures `![[attachments/AM-PS/name.svg]]` followed by an italic caption line, `**bold**`, `*italic*`, `code`.
"""
import html
import json
import re

MATH = re.compile(r"\$\$.+?\$\$|\$[^$\n]+?\$", re.S)


def inline(text, wikilinks=True):
    """Inline Markdown -> HTML; maths is protected and passed through (HTML-escaped)."""
    store = []

    def keep(m):
        store.append(html.escape(m.group(0), quote=False))
        return f"\x00{len(store) - 1}\x00"

    t = MATH.sub(keep, text)
    t = html.escape(t, quote=False)
    if wikilinks:
        t = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", t)
        t = re.sub(r"\[\[([^\]]+)\]\]", lambda m: m.group(1).split("/")[-1], t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    return re.sub(r"\x00(\d+)\x00", lambda m: store[int(m.group(1))], t)


def parse(text):
    """Block list: ('h', level, text) ('p', text) ('math', tex) ('ul', [..]) ('ol', [..]) ('table', head, rows)
    ('callout', kind, title, blocks) ('fig', name, caption)."""
    lines = text.split("\n")
    i, out = 0, []
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            i += 1
        elif s.startswith("$$"):
            buf = s
            while not (len(buf) > 2 and buf.endswith("$$")) and i + 1 < len(lines):
                i += 1
                buf += " " + lines[i].strip()
            out.append(("math", buf[2:-2].strip()))
            i += 1
        elif re.match(r"#{2,6} ", s):
            level = len(s) - len(s.lstrip("#"))
            out.append(("h", level, s[level:].strip()))
            i += 1
        elif s.startswith("> "[:1]) and not s.startswith("![["):
            body = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                body.append(re.sub(r"^\s*> ?", "", lines[i]))
                i += 1
            head = re.match(r"\[!(\w+)\]\s*(.*)", body[0]) if body else None
            if head:
                out.append(("callout", head.group(1), head.group(2).strip(), parse("\n".join(body[1:]))))
            else:
                out.append(("quote", parse("\n".join(body))))
        elif s.startswith("![["):
            m = re.match(r"!\[\[([^\]]+)\]\]", s)
            cap = ""
            if i + 1 < len(lines) and lines[i + 1].strip().startswith("*") and lines[i + 1].strip().endswith("*"):
                cap = lines[i + 1].strip().strip("*").strip()
                i += 1
            name = m.group(1).rsplit("/", 1)[-1].rsplit(".", 1)[0]
            out.append(("fig", name, cap))
            i += 1
        elif s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append(("table", rows[0], [r for r in rows[2:]]))
        elif re.match(r"- ", s):
            items = []
            while i < len(lines) and (lines[i].startswith("- ") or lines[i].startswith("  ")) and lines[i].strip():
                if lines[i].startswith("- "):
                    items.append(lines[i][2:].strip())
                else:
                    items[-1] += " " + lines[i].strip()
                i += 1
            out.append(("ul", items))
        elif re.match(r"\d+\. ", s):
            items = []
            while i < len(lines) and (re.match(r"\d+\. ", lines[i]) or lines[i].startswith("   ")) and lines[i].strip():
                if re.match(r"\d+\. ", lines[i]):
                    items.append(re.sub(r"^\d+\. ", "", lines[i]).strip())
                else:
                    items[-1] += " " + lines[i].strip()
                i += 1
            out.append(("ol", items))
        else:
            buf = [s]
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"(#{2,6} |\$\$|> |!\[\[|\||- |\d+\. )", lines[i].strip()):
                buf.append(lines[i].strip())
                i += 1
            out.append(("p", " ".join(buf)))
    return out


def render(blocks, figure_html):
    """HTML of a block list.  `figure_html(name, caption)` returns the markup of a figure."""
    out, i = [], 0
    while i < len(blocks):
        b = blocks[i]
        k = b[0]
        if k == "fig":
            group = []
            while i < len(blocks) and blocks[i][0] == "fig":
                group.append(figure_html(blocks[i][1], blocks[i][2]))
                i += 1
            out.append('<div class="diagram-row">' + "".join(group) + "</div>" if len(group) > 1 else group[0])
            continue
        i += 1
        if k == "p":
            out.append(f"<p>{inline(b[1])}</p>")
        elif k == "math":
            out.append(f'<p>$$ {html.escape(b[1], quote=False)} $$</p>')
        elif k == "h":
            out.append(f'<h4 class="step-heading">{inline(b[2])}</h4>')
        elif k == "ul":
            out.append('<ul class="bullet-list">' + "".join(f"<li>{inline(x)}</li>" for x in b[1]) + "</ul>")
        elif k == "ol":
            out.append('<ol class="num-list">' + "".join(f"<li>{inline(x)}</li>" for x in b[1]) + "</ol>")
        elif k == "table":
            head = "".join(f"<th>{inline(h)}</th>" for h in b[1])
            rows = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in b[2])
            out.append(f'<div class="table-container"><table class="data-table"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>')
        elif k == "callout":
            kind = {"warning": "warning", "result": "result"}.get(b[1], "note")
            inner = render(b[3], figure_html)
            out.append(f'<div class="{kind}-box"><div class="{kind}-box-title">{inline(b[2])}</div>{inner}</div>')
        elif k == "quote":
            out.append("")
        else:
            raise ValueError(k)
    return "".join(out)


def split_note(text):
    """(front matter dict, title, statement markdown, [(phase number, heading, markdown)]) of an exercise note."""
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    fm, tags = {}, []
    for ln in m.group(1).split("\n"):
        if ln.startswith("  - "):
            tags.append(ln[4:].strip())
        elif ":" in ln and not ln.startswith(" "):
            key, val = ln.split(":", 1)
            val = val.strip()
            if val.startswith('"') and val.endswith('"'):
                try:
                    val = json.loads(val)
                except ValueError:
                    val = val[1:-1]
            fm[key.strip()] = val
    fm["tags"] = tags
    body = text[m.end():]
    title = re.search(r"^# (.+)$", body, re.M).group(1)
    parts = re.split(r"^## ", body, flags=re.M)[1:]
    statement, phases = "", []
    for part in parts:
        head, _, rest = part.partition("\n")
        pm = re.match(r"Phase (\d+): (.*)", head)
        if head.strip() == "Statement":
            statement = rest
        elif pm:
            phases.append((int(pm.group(1)), pm.group(2).strip(), rest))
    return fm, title, statement, phases
