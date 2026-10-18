#!/usr/bin/env python3
"""Run the SymPy checks of every Engineering Mechanics Midterm 1 bank item (scripts/mechanics/pNN.py, cNN.py).

Usage:  python scripts/verify_mechanics_problems.py [P05 ...]   (no argument: every module)
Exit code 1 if any check fails.
"""
import importlib
import sys
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # warnings may contain Unicode minus signs
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from mechanics._kit import Checker  # noqa: E402


def main(argv):
    names = [a.lower() for a in argv] or sorted(p.stem for p in (HERE / "mechanics").glob("[pc][0-9][0-9].py"))
    failed = 0
    for name in names:
        chk = Checker(name.upper())
        importlib.import_module(f"mechanics.{name}").verify(chk)
        bad = [r for r in chk.rows if not r[1]]
        print(f"{name.upper()}: {len(chk.rows) - len(bad)}/{len(chk.rows)} checks passed")
        for row in chk.rows:
            print(f"   {'ok ' if row[1] else 'FAIL'} {row[0]} {row[2]}")
        failed += len(bad)
    print("ALL PASSED" if not failed else f"{failed} CHECK(S) FAILED")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
