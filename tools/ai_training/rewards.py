#!/usr/bin/env python3
"""Deterministic GRPO reward functions for training Sideris (Unsloth / TRL).

Every reward function takes a list of model completions (strings or chat message lists) and
returns a list of floats, so it plugs directly into TRL's GRPOTrainer(..., reward_funcs=[...]).

Rewards enforced:
  1. katex_syntax_reward     : +0.5 balanced $ / $$, zero \\euro, zero & inside \\text{}
  2. no_skip_rigour_reward   : +0.5 penalises "after some algebra" / "it can be shown"; rewards
                               explicit derivation markers & SI dimensional checks
  3. socratic_guard_reward   : +1.0 when Socratic mode keeps the answer hidden and asks 1 question;
                               -1.0 if it leaks the hidden target expression/value
  4. sympy_answer_reward     : +1.0 when the final boxed/stated expression is symbolically
                               equivalent to the gold answer (requires sympy at training time)
"""
import re

_EURO_RE = re.compile(r"\\euro\b")
_TEXT_AMP_RE = re.compile(r"\\text\{[^}]*&[^}]*\}")
_SKIP_PHRASES = re.compile(
    r"\b(after some algebra|it can be shown|left as an exercise|trivially|obviously|easily seen|"
    r"tras algo de algebra|es trivial|obviamente|se deja como ejercicio)\b",
    re.I,
)
_DIM_CHECK_RE = re.compile(
    r"(dimensional check|comprobaci[oó]n dimensional|an[aá]lisis dimensional|\[[MLT\u0398\s\^0-9\-\.\*\/]+\]|SI units|unidades SI)",
    re.I,
)
_THINK_RE = re.compile(r"<think>([\s\S]*?)</think>", re.S)
_BOXED_RE = re.compile(r"\\boxed\{([^{}]+(?:\{[^{}]*\}[^{}]*)*)\}")


def _extract_text(completion):
    if isinstance(completion, str):
        return completion
    if isinstance(completion, list) and completion:
        last = completion[-1]
        if isinstance(last, dict):
            return str(last.get("content", ""))
    return str(completion or "")


def _strip_think(text):
    return _THINK_RE.sub("", text).strip()


def katex_syntax_reward(completions, **_kwargs):
    scores = []
    for c in completions:
        text = _strip_think(_extract_text(c))
        if not text:
            scores.append(-0.5)
            continue
        if _EURO_RE.search(text) or _TEXT_AMP_RE.search(text):
            scores.append(-0.5)
            continue
        stripped = re.sub(r"\\\$", "", text)
        disp_ok = stripped.count("$$") % 2 == 0
        no_disp = re.sub(r"\$\$[\s\S]*?\$\$", "", stripped)
        inline_ok = no_disp.count("$") % 2 == 0
        has_math = ("$" in stripped)
        if disp_ok and inline_ok:
            scores.append(0.5 if has_math else 0.2)
        else:
            scores.append(-0.5)
    return scores


def no_skip_rigour_reward(completions, socratic=None, **_kwargs):
    scores = []
    soc_flags = socratic if isinstance(socratic, list) else [bool(socratic)] * len(completions)
    for c, is_soc in zip(completions, soc_flags):
        text = _strip_think(_extract_text(c))
        if is_soc:
            scores.append(0.0)
            continue
        score = 0.0
        if _SKIP_PHRASES.search(text):
            score -= 0.5
        else:
            score += 0.25
        if _DIM_CHECK_RE.search(text):
            score += 0.25
        scores.append(score)
    return scores


def socratic_guard_reward(completions, socratic=None, forbidden_answers=None, **_kwargs):
    scores = []
    soc_flags = socratic if isinstance(socratic, list) else [bool(socratic)] * len(completions)
    forbids = forbidden_answers if isinstance(forbidden_answers, list) else [forbidden_answers] * len(completions)
    for c, is_soc, forbid in zip(completions, soc_flags, forbids):
        if not is_soc:
            scores.append(0.0)
            continue
        answer = _strip_think(_extract_text(c))
        if forbid and str(forbid).strip() and str(forbid).strip().lower() in answer.lower():
            scores.append(-1.0)
            continue
        q_count = answer.count("?")
        if 1 <= q_count <= 2 and len(answer) <= 650:
            scores.append(1.0)
        elif q_count >= 1:
            scores.append(0.3)
        else:
            scores.append(-0.5)
    return scores


def sympy_answer_reward(completions, expected_answer=None, **_kwargs):
    """Compare final \\boxed{...} expression symbolically with expected_answer via SymPy."""
    try:
        import sympy as sp  # type: ignore
        from sympy.parsing.latex import parse_latex  # type: ignore
    except Exception:
        return [0.0] * len(completions)

    expected = expected_answer if isinstance(expected_answer, list) else [expected_answer] * len(completions)
    scores = []
    for c, gold in zip(completions, expected):
        if not gold:
            scores.append(0.0)
            continue
        answer = _strip_think(_extract_text(c))
        matches = _BOXED_RE.findall(answer)
        if not matches:
            scores.append(0.0)
            continue
        pred_tex = matches[-1].strip()
        try:
            diff = sp.simplify(parse_latex(pred_tex) - parse_latex(str(gold)))
            scores.append(1.0 if diff == 0 else -0.2)
        except Exception:
            scores.append(1.0 if pred_tex.replace(" ", "") == str(gold).replace(" ", "") else 0.0)
    return scores
