#!/usr/bin/env python3
"""Recompute every number of the Aerospace Materials I Midterm 3 bank (Blocks B63-B112, Problems P21-P36).

    python tools/materials_bank/verify_mt3.py                 # all Midterm 3 notes
    python tools/materials_bank/verify_mt3.py B63 P21         # only these notes
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_mt2  # noqa: E402
import build_materials_bank as bmb  # noqa: E402
import build_problem_bank as bpb  # noqa: E402


def _is_mt3(path):
    m = re.search(r"Bank ([BP])(\d{2,3})", path.name)
    if not m:
        return False
    num = int(m.group(2))
    return (m.group(1) == "B" and num >= 63) or (m.group(1) == "P" and num >= 21)


def main(argv):
    only = {a.upper() for a in argv}
    quiz = sorted(p for p in bmb.BANK.glob("Quiz - Bank *.md") if _is_mt3(p))
    probs = sorted(p for p in bmb.BANK.glob("Problem - Bank *.md") if _is_mt3(p))
    if only:
        pick = lambda p: re.search(r"Bank ([BP]\d{2,3})", p.name).group(1) in only  # noqa: E731
        quiz, probs = [p for p in quiz if pick(p)], [p for p in probs if pick(p)]
        if len(quiz) + len(probs) != len(only):
            print(f"verify_mt3: some of {sorted(only)} do not exist in MT3")
            return 1
    bmb.mt2fig.build()
    errors, blocks, items = [], [], []
    for p in quiz:
        try:
            blocks.append(bmb.parse_quiz_note(p))
        except bpb.BankError as exc:
            errors.append(str(exc))
    for p in probs:
        try:
            item = bmb.parse_problem_note(p)
            items.append(item)
            errors += verify_mt2.verify_problem(item, p)
        except bpb.BankError as exc:
            errors.append(str(exc))
    try:
        review = bmb.check_bank(blocks, items, partial=True)
    except bpb.BankError as exc:
        errors.append(str(exc))
        review = []
    questions = [q for b in blocks for q in b["questions"]]
    n_calc = sum(1 for q in questions if q["calc"])
    n_check = sum(1 for q in questions if q["check"])
    n_ver = sum(len(i["verify"]) for i in items)
    for e in errors:
        print("ERROR", e)
    if only and questions:
        letters = {k: sum(q["answer"] == k for q in questions) for k in "abcd"}
        print(f"  right answers: {letters}; formats: " + ", ".join(
            f"{f} {sum(q['format'] == f for q in questions)}" for f in bmb.FORMATS if any(q["format"] == f for q in questions)))
        for r, a, b in review:
            print(f"  similar {r:.2f}: {a} ~ {b}")
    print(f"verify_mt3: {len(questions)} questions ({n_calc} calc, {n_check} check) and {len(items)} problems "
          f"({n_ver} recomputed results): {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
