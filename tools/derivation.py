#!/usr/bin/env python3
"""Derivation boxes of Engineering Mechanics (theory notes and worked solutions) and the `no-inline-calc` gate.

Every development (a time derivative, a vector product, an integral, a chain of equalities) lives inside one
self-contained box; the prose around the boxes only names things with atomic identifiers ($m$, $\\theta$,
$\\mathbf r_0^P$). In a vault note a box is an Obsidian callout:

    > [!derivation] Title of the step
    > **Law:** the principle invoked
    > **Source:** Notes.pdf, Eq. 3.5; [Lecture 3, Slide 12]
    >
    > Free lines: sentences, lists and $$ blocks. A development is written as
    > $$\\begin{aligned}
    > a &= b \\quad &\\text{(one operation, with its reason)} \\\\
    >   &= c \\quad &\\text{(the next operation)}
    > \\end{aligned}$$
    >
    > $$\\boxed{a = c}$$
    >
    > **Units:** $[\\mathrm{M\\,L\\,T^{-2}}]$, the check written out
    > **Meaning:** the physical reading of the result

Rules checked by `parse` (each returns a message, never raises):
  * a title, a **Law:** line, a **Source:** line with an official citation written outside $...$,
    a **Units:** line and a **Meaning:** line;
  * at least one $$ block, and at least one of them with \\boxed{...};
  * every row of every aligned block carries its reason, \\text{(...)}.

`render` gives the HTML (`<div class="derivation-box">`, styled by assets/css/derivation-box.css). `gate(html)` is the
`no-inline-calc` gate on a rendered fragment: outside the boxes no <p> or <li> may hold an equals sign inside maths,
\\dot, \\ddot, \\times, \\frac or \\int, and no display formula may stand on its own.
"""
import html as _html
import re

START = re.compile(r"^>\s*\[!derivation\]\s*(.*)$", re.I)
CITATION = re.compile(
    r"Notes\.pdf, (?:Eqs?\.|Sec\.|Ch\.|p\.) ?[\d.]+|\[Lecture \d+, Slides? \d+(?:[-\u2013]\d+)?\]|Problems\.pdf, pp?\. ?\d+"
    r"|weekly-planning-mechanics_G46\.pdf")
FIELD = re.compile(r"^\*\*(Law|Source|Units|Meaning):\*\*\s*(.*)$")
FIGURE = re.compile(r"^!\[\[attachments/([\w-]+)/([\w.-]+)\]\]$")
BANNED = re.compile(r"=|\\ddot(?![A-Za-z])|\\dot(?![A-Za-z])|\\times(?![A-Za-z])|\\[dt]?frac(?![A-Za-z])|\\i+nt(?![A-Za-z])|\\oint(?![A-Za-z])")
INLINE = re.compile(r"(?<![\\$])\$(?!\$)(.+?)(?<![\\$])\$(?!\$)", re.S)


def is_start(line):
    return bool(START.match(line))


def take(lines, i):
    """Lines of the callout that starts at lines[i] (without the '> ' prefix) and the index after it."""
    block = []
    while i < len(lines) and lines[i].startswith(">"):
        block.append(re.sub(r"^> ?", "", lines[i]).rstrip())
        i += 1
    return block, i


def _math_block(block, i):
    """A $$ block starting at block[i]: (tex, next index)."""
    line = block[i].strip()
    if line.count("$$") >= 2 and line.endswith("$$") and len(line) > 4:
        return line[2:-2].strip(), i + 1
    buf = [line[2:]]
    i += 1
    while i < len(block):
        cur = block[i]
        if cur.strip().endswith("$$"):
            buf.append(cur.strip()[:-2])
            return "\n".join(buf).strip(), i + 1
        buf.append(cur)
        i += 1
    return "\n".join(buf).strip(), i


def aligned_rows(tex):
    """Rows of every aligned environment of a formula."""
    rows = []
    for body in re.findall(r"\\begin\{aligned\}(.*?)\\end\{aligned\}", tex, re.S):
        rows += [r.strip() for r in re.split(r"\\\\(?:\[[^\]]*\])?", body) if r.strip()]
    return rows


def parse(block):
    """(box, errors). box: title, law, source, units, meaning, items [('p', text) | ('li', text) | ('math', tex) | ('fig', (folder, file))]."""
    box = {"title": "", "law": "", "source": "", "units": "", "meaning": "", "items": []}
    errors = []
    m = START.match("> " + block[0]) if block else None
    box["title"] = m.group(1).strip() if m else ""
    i = 1
    while i < len(block):
        line = block[i].strip()
        if not line:
            i += 1
            continue
        f = FIELD.match(line)
        if f:
            box[f.group(1).lower()] = f.group(2).strip()
            i += 1
        elif line.startswith("$$"):
            tex, i = _math_block(block, i)
            box["items"].append(("math", tex))
        elif FIGURE.match(line):
            g = FIGURE.match(line)
            box["items"].append(("fig", (g.group(1), g.group(2))))
            i += 1
        elif re.match(r"^[-*] ", line):
            box["items"].append(("li", line[2:].strip()))
            i += 1
        else:
            box["items"].append(("p", line))
            i += 1
    name = box["title"] or "(untitled)"
    if not box["title"]:
        errors.append("derivation box without a title")
    for key in ("law", "source", "units", "meaning"):
        if not box[key]:
            errors.append(f"box '{name}': no **{key.capitalize()}:** line")
    if box["source"] and not CITATION.search(re.sub(r"\$[^$]*\$", "", box["source"])):
        errors.append(f"box '{name}': the source has no official citation outside maths "
                      "(Notes.pdf, Eq. X.Y | [Lecture N, Slide M] | Problems.pdf, p. N)")
    maths = [t for k, t in box["items"] if k == "math"]
    if not maths:
        errors.append(f"box '{name}': no $$ development")
    elif not any("\\boxed" in t for t in maths):
        errors.append(f"box '{name}': no \\boxed result")
    for tex in maths:
        for row in aligned_rows(tex):
            if "\\text{(" not in row:
                errors.append(f"box '{name}': aligned row without its reason \\text{{(...)}}: {row[:60]}")
    return box, errors


def render(box, inl, figure=None):
    """HTML of a parsed box. inl(text) renders inline markdown; figure((folder, file)) renders an embedded figure."""
    out = ['<div class="derivation-box">', '  <div class="derivation-head">',
           f'    <span class="derivation-title">{inl(box["title"])}</span>',
           f'    <span class="derivation-law"><strong>Law:</strong> {inl(box["law"])}</span>',
           f'    <span class="derivation-source"><strong>Source:</strong> {inl(box["source"])}</span>',
           "  </div>", '  <div class="derivation-body">']
    items, k = box["items"], 0
    while k < len(items):
        kind, val = items[k]
        if kind == "li":
            out.append("    <ul>")
            while k < len(items) and items[k][0] == "li":
                out.append(f"      <li>{inl(items[k][1])}</li>")
                k += 1
            out.append("    </ul>")
            continue
        if kind == "p":
            out.append(f"    <p>{inl(val)}</p>")
        elif kind == "math":
            cls = "derivation-result" if "\\boxed" in val else "derivation-steps"
            out.append(f'    <div class="{cls}">$${_html.escape(val, quote=False)}$$</div>')
        elif kind == "fig" and figure:
            out.append("    " + figure(val))
        k += 1
    out += ["  </div>", f'  <p class="derivation-units"><strong>Units:</strong> {inl(box["units"])}</p>',
            f'  <p class="derivation-foot"><strong>Meaning:</strong> {inl(box["meaning"])}</p>', "</div>"]
    return "\n".join(out)


def strip_boxes(fragment):
    """The fragment without its <div class="derivation-box"> elements (nested divs included)."""
    out, pos = [], 0
    for m in re.finditer(r'<div class="derivation-box">', fragment):
        if m.start() < pos:
            continue
        out.append(fragment[pos:m.start()])
        depth, j = 1, m.end()
        for t in re.finditer(r"<div\b|</div>", fragment[m.end():]):
            depth += 1 if t.group(0) != "</div>" else -1
            if depth == 0:
                j = m.end() + t.end()
                break
        else:
            j = len(fragment)
        pos = j
    out.append(fragment[pos:])
    return "".join(out)


def gate(fragment):
    """no-inline-calc: messages for every calculation written outside a derivation box."""
    rest = strip_boxes(fragment)
    errors = []
    for tag, body in re.findall(r"<(p|li)\b[^>]*>(.*?)</\1>", rest, re.S):
        text = _html.unescape(re.sub(r"<[^>]+>", "", body))
        if "$$" in text:
            errors.append(f"no-inline-calc: display formula in a <{tag}> outside a derivation box: {text.strip()[:70]}")
            continue
        for span in INLINE.findall(text):
            hit = BANNED.search(span)
            if hit:
                errors.append(f"no-inline-calc: '{hit.group(0)}' in prose outside a derivation box: ${span.strip()[:70]}$")
    loose = re.sub(r"<(p|li)\b[^>]*>.*?</\1>", "", rest, flags=re.S)
    for tex in re.findall(r"\$\$(.+?)\$\$", loose, re.S):
        errors.append(f"no-inline-calc: display formula outside a derivation box: {_html.unescape(tex).strip()[:70]}")
    return errors
