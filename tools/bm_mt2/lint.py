#!/usr/bin/env python3
"""Validate the Business Management Midterm 2 bank notes without writing anything.

    python tools/bm_mt2/lint.py              # every note; bank rules with quotas off; prints counts and similar pairs
    python tools/bm_mt2/lint.py --full       # also the unit quotas and the spread of the answers (the finished bank)
    python tools/bm_mt2/lint.py F06 M06      # only the notes with these ids (each checked on its own)

The index note is not checked here (build_problem_bank.py does that when the notes are listed).
"""
import argparse
import pathlib
import sys

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import build_problem_bank as bpb  # noqa: E402
from bm_mt2 import bank  # noqa: E402
from figures import bm_mt2 as figmod  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--full", action="store_true")
    args = ap.parse_args(argv)
    figmod.build()
    paths = sorted(bank.BANK.glob("Quiz - Bank *.md")) + sorted(bank.BANK.glob("Problem - Bank M*.md"))
    if args.ids:
        paths = [p for p in paths if p.name.split(" - ")[1].split()[-1] in args.ids]
    blocks, problems, errors = [], [], 0
    for p in paths:
        try:
            if p.name.startswith("Quiz"):
                blocks.append(bank.parse_quiz_note(p))
            else:
                problems.append(bank.parse_problem_note(p))
        except bpb.BankError as exc:
            errors += 1
            print("ERROR", exc)
    try:
        review = bank.check_bank(blocks, problems, partial=not args.full)
    except bpb.BankError as exc:
        print("ERROR (bank)", exc)
        return 1
    tf = [q for b in blocks if b["kind"] == "true_false" for q in b["questions"]]
    mc = [q for b in blocks if b["kind"] == "multiple_choice" for q in b["questions"]]
    for u in bank.UNITS:
        print(f"unit {u}: {sum(q['unit'] == u for q in tf)} T/F, {sum(q['unit'] == u for q in mc)} MC")
    if tf:
        print(f"true statements: {sum(q['answer'] == 'T' for q in tf)} of {len(tf)}")
    if mc:
        print("right letters: " + ", ".join(f"{k} {sum(q['answer'] == k for q in mc)}" for k in "abcd"))
    for a in bank.ARCHETYPES:
        print(f"problems {a}: {sum(p['archetype'] == a for p in problems)}")
    for r, a, b in review:
        print(f"similar {r:.2f}: {a} ~ {b}")
    print("OK" if not errors else f"{errors} note(s) with errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
