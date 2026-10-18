#!/usr/bin/env python3
"""Parse one or more Engineering Mechanics bank notes with the real builder and print a summary (no files are written).

Usage:  python scripts/check_bank_note.py P05 [P06 ...]      (bank ids)
"""
import pathlib
import sys
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # warnings may contain Unicode minus signs
REPO = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))
import build_mechanics_bank as b  # noqa: E402


def main(ids):
    rc = 0
    b.emfig.build()
    for i in ids:
        notes = sorted(b.BANK.glob(f"Problem - Bank {i.upper()} - *.md"))
        if len(notes) != 1:
            print(f"{i}: expected one note, found {len(notes)}")
            rc = 1
            continue
        try:
            item = b.parse_note(notes[0])
        except b.bpb.BankError as exc:
            print(f"{i}: INVALID {exc}")
            rc = 1
            continue
        pts = " + ".join(f"({s['label']}) {s['points']:g}" for s in item["subquestions"])
        print(f"{i}: ok  {item['title'][:70]}  | {item['category']} {item['archetype']} {item['level']} unit {item['unit']} | {pts} = {item['points']:g} | figures {item['figures']}")
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
