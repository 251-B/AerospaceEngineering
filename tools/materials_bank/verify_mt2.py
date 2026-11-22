#!/usr/bin/env python3
"""Recompute every number of the Aerospace Materials I Midterm 2 bank.

For each test question with `- calc:` the expression is evaluated again and compared with the number of the right option
(1.2 % tolerance, the rounding of a three-figure option); no wrong option may coincide with it (3 %). Each `- check:`
condition must be true. For each problem, every line of its "## Verification" section
("- <label> | <expression> | <stated value>") is evaluated and compared with the stated value (0.6 % or half a unit of
its last printed digit), and the stated value must be printed in the note.

    python tools/materials_bank/verify_mt2.py                 # the whole bank
    python tools/materials_bank/verify_mt2.py B01 B02 P05     # only these notes (authors use this while writing);
                                                              # it also runs the concept and similarity rules on them

Exit code 1 on any mismatch, on a numeric question without `calc`, or on a problem without Verification lines.
"""
import pathlib
import re
import sys

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import build_materials_bank as bmb  # noqa: E402
import build_problem_bank as bpb  # noqa: E402


def stated_tolerance(text):
    """Half a unit of the last printed digit of `text` ('50.2' -> 0.05, '1.2e-3' -> 5e-5)."""
    mant, _, exp = text.lower().partition("e")
    decimals = len(mant.split(".")[1]) if "." in mant else 0
    return 0.5 * 10 ** (-decimals) * 10 ** int(exp or 0)


def verify_problem(item, path):
    errors = []
    note = path.read_text(encoding="utf-8").split("## Verification")[0]
    if not item["verify"]:
        errors.append(f"{item['id']}: no '## Verification' lines")
    for v in item["verify"]:
        value = float(bmb.evaluate(v["expr"], f"{item['id']} {v['label']}"))
        tol = max(stated_tolerance(v["text"]) * 1.02, 0.006 * abs(value))
        if abs(value - v["stated"]) > tol:
            errors.append(f"{item['id']}: {v['label']} = {value:.6g}, the note states {v['text']}")
        plain = v["text"].lstrip("-")
        mant = plain.lower().split("e")[0]
        if mant not in note.replace("{,}", "").replace("\\,", ""):
            errors.append(f"{item['id']}: stated value {v['text']} ({v['label']}) is not printed in the note")
    return errors


def main(argv):
    only = {a.upper() for a in argv}
    quiz = sorted(bmb.BANK.glob("Quiz - Bank *.md"))
    probs = sorted(bmb.BANK.glob("Problem - Bank *.md"))
    if only:
        pick = lambda p: re.search(r"Bank ([BP]\d{2,3})", p.name).group(1) in only  # noqa: E731
        quiz, probs = [p for p in quiz if pick(p)], [p for p in probs if pick(p)]
        if len(quiz) + len(probs) != len(only):
            print(f"verify_mt2: some of {sorted(only)} do not exist")
            return 1
    bmb.mt2fig.build()
    errors, blocks, items = [], [], []
    for p in quiz:
        try:
            blocks.append(bmb.parse_quiz_note(p))     # raises on a calc or check mismatch
        except bpb.BankError as exc:
            errors.append(str(exc))
    for p in probs:
        try:
            item = bmb.parse_problem_note(p)
            items.append(item)
            errors += verify_problem(item, p)
        except bpb.BankError as exc:
            errors.append(str(exc))
    review = []
    try:
        review = bmb.check_bank(blocks, items, partial=True)
    except bpb.BankError as exc:
        errors.append(str(exc))
    questions = [q for b in blocks for q in b["questions"]]
    n_calc = sum(1 for q in questions if q["calc"])
    n_check = sum(1 for q in questions if q["check"])
    n_ver = sum(len(i["verify"]) for i in items)
    for e in errors:
        print("ERROR", e)
    if only:
        letters = {k: sum(q["answer"] == k for q in questions) for k in "abcd"}
        print(f"  right answers: {letters}; formats: " + ", ".join(
            f"{f} {sum(q['format'] == f for q in questions)}" for f in bmb.FORMATS if any(q["format"] == f for q in questions)))
        for r, a, b in review:
            print(f"  similar {r:.2f}: {a} ~ {b}")
    print(f"verify_mt2: {len(questions)} questions ({n_calc} calc, {n_check} check) and {len(items)} problems "
          f"({n_ver} recomputed results): {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
