#!/usr/bin/env python3
"""Check an Engineering Mechanics theory note before its figures exist (mission tool, deleted when the mission closes).

Builds the page of tools/topic_pages.json (or, before it is registered there, of tools/briefs/em_theory_pages.json) exactly as tools/build_topic_pages.py does (derivation-box syntax, the
no-inline-calc gate, PDF deep links), but replaces every figure that is not drawn yet by a placeholder, so a writer
can check the text while the figure modules are still to be written. Writes nothing.

Usage:
    python3 tools/briefs/check_theory_note.py subjects/engineering-mechanics/teoria/topic-N.html [--katex PATH/katex.js]

Reports: derivation-box and gate errors, figures embedded but not drawn yet, number of boxes, any "Phase" word,
and (with --katex, needs node) every formula of the note that KaTeX cannot render. Exit 0 only when the only
findings are figures not drawn yet.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys

TOOLS = pathlib.Path(__file__).resolve().parent.parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import build_topic_pages as btp  # noqa: E402
import source_links as sl  # noqa: E402

PENDING = pathlib.Path(__file__).resolve().parent / "em_theory_pages.json"  # entries not yet in topic_pages.json

_JS = r"""
const katex = require(process.argv[1]);
const fs = require('fs');
let s = fs.readFileSync(process.argv[2], 'utf8').split('\n').map(l => l.replace(/^> ?/, '')).join('\n');
s = s.replace(/^---[\s\S]*?\n---/, '');
const disp = [...s.matchAll(/\$\$([\s\S]+?)\$\$/g)].map(m => m[1]);
const rest = s.replace(/\$\$[\s\S]+?\$\$/g, ' ');
const inl = [...rest.matchAll(/(?<![\\$])\$(?!\$)(.+?)(?<![\\$])\$(?!\$)/g)].map(m => m[1]);
let bad = 0, n = 0;
for (const [tex, d] of [...disp.map(t => [t, true]), ...inl.map(t => [t, false])]) {
  n++;
  try { katex.renderToString(tex, {displayMode: d, throwOnError: true, strict: false}); }
  catch (e) { bad++; console.log('katex: ' + e.message.slice(0, 220)); }
}
console.log('katex: checked ' + n + ' formulas, ' + bad + ' failed');
process.exit(bad ? 1 : 0);
"""


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("page")
    ap.add_argument("--katex", help="path to katex.js (e.g. the dist/ folder of `npm pack katex@0.16.8`)")
    args = ap.parse_args(argv)
    cfg = json.loads(btp.CONFIG.read_text(encoding="utf-8"))
    pending = json.loads(PENDING.read_text(encoding="utf-8")) if PENDING.exists() else {}
    spec = cfg["pages"].get(args.page) or pending[args.page]
    missing = []
    real_call = btp.FigureSet.__call__

    def call(self, name):
        if self.reg is None or name not in self.reg.web:
            missing.append(name)
            return f'<div class="diagram-card"><p>figure {name} not drawn yet</p></div>'
        return real_call(self, name)

    btp.FigureSet.__call__ = call
    ok = True
    try:
        btp.build_page(args.page, spec, json.loads(sl.CONFIG.read_text(encoding="utf-8")), sl.load_json(sl.ANCHORS, {}))
    except btp.NoteError as err:
        ok = False
        for m in err.messages:
            print(f"error: {m}")
    note = REPO / spec["note"]
    text = note.read_text(encoding="utf-8")
    print(f"boxes: {len(re.findall(r'^> \[!derivation\]', text, re.M))}")
    if re.search(r"\bphase\s+\d|\b(first|second|third|fourth|four|4)[- ]phases?\b", text, re.I):
        ok = False
        print("error: a 'Phase N' / 'four phases' label appears in the note (AGENTS.md forbids them)")
    for name in dict.fromkeys(missing):
        print(f"figure not drawn yet: {name}")
    if args.katex:
        res = subprocess.run(["node", "-e", _JS, args.katex, str(note)], capture_output=True, text=True)
        print(res.stdout.strip() or res.stderr.strip())
        ok = ok and res.returncode == 0
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
