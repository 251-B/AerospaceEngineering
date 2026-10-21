#!/usr/bin/env python3
"""Author the Advanced Maths problem-sheet notes (Chapter 3 part 2, Chapter 4 parts 1 and 2).

Every result is computed with SymPy (scripts/am_problems/) and written as Markdown: one vault note per exercise
under vault/04 - Advanced Maths/, the set index notes, and tools/am_problems/figures.json (the phase portraits that
tools/am_problems/build.py draws).  After this first run the notes are the source of truth: edit them by hand and
run python tools/am_problems/build.py.  Existing notes are never overwritten unless --force is given.

    python scripts/author_am_problems.py [--sheet ch3b|ch4a|ch4b ...] [--out DIR] [--force]
"""
import argparse
import importlib
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from am_problems import core  # noqa: E402

SHEETS = {
    "ch3b": ("am_problems.ch3b", ["ex1", "ex2", "ex3", "ex4", "ex5"], "am_problems.ch3b_vp", ["ex6", "ex7", "ex8", "ex9"]),
    "ch4a": ("am_problems.ch4a", ["ex1", "ex2", "ex3", "ex4", "ex5", "ex6", "ex7"], "am_problems.ch4a_b", ["ex8", "ex9", "ex10", "ex11"]),
    "ch4b": ("am_problems.ch4b_b", None, None, None),
}


def collect(sheet):
    mod_name, first, mod2_name, second = SHEETS[sheet]
    mod = importlib.import_module(mod_name)
    notes = []
    if first is None:
        notes = mod.build()
    else:
        notes += [getattr(mod, f)() for f in first]
        if mod2_name:
            mod2 = importlib.import_module(mod2_name)
            notes += [getattr(mod2, f)() for f in second]
    return mod.SHEET, notes


def index_note(sheet, notes, title, blurb):
    lines = ["---", 'materia: "Advanced Maths"', f'tema: "{sheet["tema"]}"', "tags:", "  - problem-set", "  - problemas-resueltos", "---", "",
             f"# {title}", "", f"> {blurb}", "", f"Method and notation: [[{sheet['theory_note']}]]. Hub: [[Advanced Maths MOC]].", ""]
    for n in notes:
        lines.append(f"{n.num}. [[{n.filename[:-3]}|Exercise {n.num}: {n.title}]] - {n.pill}")
    return "\n".join(lines) + "\n"


TITLES = {
    "ch3b": ("Problem Set - Chapter 3 Part 2", "Official sheet probls_ch3-ii_2627.pdf: inhomogeneous constant-coefficient equations, resonance, variation of constants and reduction of order. Nine exercises, all solved step by step."),
    "ch4a": ("Problem Set - Chapter 4 Part 1", "Official sheet probls_ch4-i_2627_v2.pdf: first-order systems, theory of linear systems, elimination, real eigenvalues, decoupling and phase portraits. Eleven exercises, all solved step by step."),
    "ch4b": ("Problem Set - Chapter 4 Part 2", "Official sheet probls_ch4-ii_2627.pdf: complex and repeated eigenvalues, canonical forms, constructing matrices from eigen-data and the nine linear phase portraits. Eight exercises, all solved step by step."),
}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sheet", action="append", choices=sorted(SHEETS), help="sheet(s) to author (default: all that exist)")
    ap.add_argument("--out", help="write the notes here instead of the vault (testing)")
    ap.add_argument("--force", action="store_true", help="overwrite existing notes")
    args = ap.parse_args(argv)
    out = pathlib.Path(args.out) if args.out else core.VAULT
    out.mkdir(parents=True, exist_ok=True)
    wrote = skipped = 0
    for sheet in (args.sheet or sorted(SHEETS)):
        try:
            sh, notes = collect(sheet)
        except ModuleNotFoundError as exc:
            print(f"{sheet}: not available yet ({exc.name})")
            continue
        for n in notes:
            path = out / n.filename
            if path.exists() and not args.force:
                skipped += 1
                print("skip (exists)", n.filename)
                continue
            path.write_text(n.markdown(), encoding="utf-8", newline="\n")
            wrote += 1
        title, blurb = TITLES[sheet]
        ipath = out / f"{title}.md"
        if args.force or not ipath.exists():
            ipath.write_text(index_note(sh, notes, title, blurb), encoding="utf-8", newline="\n")
        print(f"{sheet}: {len(notes)} notes")
    if not args.out:
        core.write_figures()
    else:
        core.FIG_JSON = out / "figures.json"
        core.write_figures()
    print(f"wrote {wrote} notes, skipped {skipped}; {len(core.FIGURES)} figures registered")


if __name__ == "__main__":
    main()
