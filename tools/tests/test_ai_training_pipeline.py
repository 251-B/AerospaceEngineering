"""Offline pure-stdlib unit tests for Sideris training notebooks and books_to_sft.py."""
import ast
import json
import pathlib
import re
import sys
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools/ai_training"))

import books_to_sft as b2s  # noqa: E402

NB_MAIN = REPO / "tools/ai_training/Sideris_Train_Colab_Kaggle.ipynb"
NB_PACK = REPO / "tools/ai_training/kaggle_pack/Sideris_Train_Colab_Kaggle.ipynb"


def _cell_src(cell):
    src = cell.get("source", "")
    return "".join(src) if isinstance(src, list) else str(src)


def _extract_notebook_cpt_filter():
    nb = json.loads(NB_MAIN.read_text(encoding="utf-8"))
    cell4_src = _cell_src(nb["cells"][4])
    tree = ast.parse(cell4_src)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "is_clean_cpt_chunk":
            mod = ast.Module(body=[node], type_ignores=[])
            ns = {}
            exec(compile(mod, "<cell4>", "exec"), ns)
            return ns["is_clean_cpt_chunk"]
    raise AssertionError("is_clean_cpt_chunk not found in Cell 4")


class SiderisNotebookTests(unittest.TestCase):
    def test_both_notebook_copies_exist_and_are_byte_identical(self):
        self.assertTrue(NB_MAIN.is_file(), f"Missing {NB_MAIN}")
        self.assertTrue(NB_PACK.is_file(), f"Missing {NB_PACK}")
        self.assertEqual(NB_MAIN.read_bytes(), NB_PACK.read_bytes())

        nb = json.loads(NB_MAIN.read_text(encoding="utf-8"))
        self.assertEqual(nb.get("nbformat"), 4)
        cells = nb.get("cells", [])
        self.assertEqual(len(cells), 10)
        self.assertEqual(cells[0]["cell_type"], "markdown")
        for idx in range(1, 10):
            self.assertEqual(cells[idx]["cell_type"], "code", f"Cell {idx} must be code")

    def test_every_notebook_code_cell_parses_cleanly(self):
        nb = json.loads(NB_MAIN.read_text(encoding="utf-8"))
        for idx, cell in enumerate(nb["cells"]):
            if cell["cell_type"] == "code":
                src = _cell_src(cell)
                ast.parse(src, filename=f"cell_{idx}.py")

    def test_notebook_configuration_privacy_and_stage_structure(self):
        nb = json.loads(NB_MAIN.read_text(encoding="utf-8"))
        c1 = _cell_src(nb["cells"][1])
        c2 = _cell_src(nb["cells"][2])
        c3 = _cell_src(nb["cells"][3])
        c4 = _cell_src(nb["cells"][4])
        c5 = _cell_src(nb["cells"][5])
        c6 = _cell_src(nb["cells"][6])
        c7 = _cell_src(nb["cells"][7])
        c8 = _cell_src(nb["cells"][8])
        c9 = _cell_src(nb["cells"][9])
        full_nb = "\n".join(_cell_src(c) for c in nb["cells"])

        # Cell 1 switches, recipes, and dataset autodiscovery
        for var in (
            "MODEL_CHOICE",
            'HF_USERNAME           = "SiderisAI"',
            "RUN_CPT",
            "CPT_EPOCHS",
            "CPT_MAX_STEPS",
            "CPT_LR",
            "CPT_SUBJECT_WEIGHTS",
            "CPT_SFT_REPLAY_RATIO",
            "RESUME_FROM_ADAPTER",
            "SESSION_MAX_HOURS",
            "RUN_SFT",
            "SFT_EPOCHS",
            "RUN_DPO",
            "RUN_GRPO",
            "GRPO_MAX_STEPS",
            "RUN_EXPORT",
            "BOOKS_FILE",
            "DATA_DIR",
        ):
            self.assertIn(var, c1)

        # Cell 2 avoids optimum[onnxruntime] downgrade trap
        self.assertNotIn('pip_run("install", "-q", "--upgrade",\n        "optimum', c2)
        self.assertIn("transformers>=5.2.0", c2)

        # Cell 3 supports resume from private HF adapter
        self.assertIn("RESUME_FROM_ADAPTER", c3)
        self.assertIn("snapshot_download", c3)
        self.assertIn("PeftModel.from_pretrained", c3)
        self.assertIn("restore_adapter_in_place", c3)

        # Cell 4 CPT: packing, 4096->2048 OOM fallback, SFT replay, eos, HF push
        self.assertIn('"packing": True', c4)
        self.assertIn("CPT_MAX_SEQ_LEN", c4)
        self.assertIn("CPT_FALLBACK_SEQ_LEN", c4)
        self.assertIn("CPT_SFT_REPLAY_RATIO", c4)
        self.assertIn("eos_token", c4)
        self.assertIn("-cpt", c4)
        c4_code = "\n".join(ln for ln in c4.splitlines() if not ln.strip().startswith("#"))
        self.assertNotIn("eval_holdout", c4_code)
        self.assertNotIn("get_peft_model", c4)

        # Cell 5 SFT reuses existing LoRA without recreating it
        self.assertNotIn("get_peft_model", c5)
        self.assertIn('hasattr(model, "peft_config")', c5)
        self.assertIn("-sft", c5)

        # Cells 6 & 7 DPO / GRPO fault-tolerant error handling & rollback
        for stage_cell in (c6, c7):
            self.assertIn("try:", stage_cell)
            self.assertIn("except Exception", stage_cell)
            self.assertIn("restore_adapter_in_place", stage_cell)
            self.assertIn("push_folder_to_hf", stage_cell)

        # Cell 8 evaluation on eval_holdout + rewards.py + optional base comparison
        self.assertIn("eval_holdout.jsonl", c8)
        self.assertIn("disable_adapter", c8)
        for fn in ("katex_syntax_reward", "no_skip_rigour_reward", "socratic_guard_reward", "sympy_answer_reward"):
            self.assertIn(fn, c8)

        # Cell 9 disk guard & private HF exports
        self.assertIn("disk_usage", c9)
        self.assertIn("private=True", c1)
        for call in re.finditer(r"create_repo\(([^)]+)\)", full_nb):
            self.assertIn("private=True", call.group(1))

        # No leaked tokens or copyrighted textbook strings
        self.assertIsNone(re.search(r"\bhf_[A-Za-z0-9]{15,}\b", full_nb))
        self.assertNotIn("ISBN", full_nb)


class BooksCptAndSftTests(unittest.TestCase):
    def test_cpt_ocr_noise_filter_language_aware(self):
        nb_filter = _extract_notebook_cpt_filter()
        en_prose = (
            "F. M. White. Fluid Mechanics. Mc-Graw Hill. 2015\n\n"
            + " ".join(
                [
                    "The steady incompressible Navier-Stokes momentum equation balances convective acceleration, "
                    "pressure gradients, gravitational body forces, and viscous shear stresses throughout a laminar boundary layer."
                ]
                * 8
            )
        )
        # Realistic Spanish textbook prose has ~40% <=2-char stopwords (de, la, el, en, un, se, al, y, a)
        es_prose = (
            "A. Crespo Martínez. Mecánica de Fluidos. Thompson. 2006\n\n"
            + " ".join(
                [
                    "En el estudio de la mecánica de fluidos se aplica la ecuación de continuidad en un volumen de control "
                    "para analizar el flujo estacionario y la conservación de la masa en un conducto."
                ]
                * 8
            )
        )
        ocr_soup = (
            "G. K. Batchelor\n\n"
            + " ".join(["a = 1 + x / y * z - 2 | 3 = k p q r s t u v 0 1 2 3"] * 12)
        )
        mojibake = "Title\n\n" + ("word " * 130) + ("\ufffd" * 80)
        too_short = "Title\n\nShort engineering sentence with fewer than one hundred twenty words."

        for fn in (nb_filter, b2s.is_clean_cpt_chunk):
            self.assertEqual(fn({"text": en_prose, "lang": "en"}), (True, "ok"))
            self.assertEqual(fn({"text": es_prose, "lang": "es"}), (True, "ok"))
            self.assertFalse(fn({"text": ocr_soup, "lang": "en"})[0])
            self.assertFalse(fn({"text": mojibake, "lang": "en"})[0])
            self.assertEqual(fn({"text": too_short, "lang": "en"}), (False, "too_short"))

    def test_books_to_sft_gates_ocr_safety_dedup_and_copyright(self):
        holdout_prompt = (
            "Consider a steady incompressible laminar boundary layer over a flat plate with free-stream velocity "
            "$U_\\infty = 10\\,\\mathrm{m/s}$ and kinematic viscosity $\\nu$. Derive the Blasius similarity variable."
        )
        holdout_row = {
            "id": "holdout-blasius",
            "messages": [
                {"role": "system", "content": "sys"},
                {"role": "user", "content": holdout_prompt},
                {"role": "assistant", "content": "Similarity transformation gives $\\eta = y\\sqrt{U_\\infty/(\\nu x)}$."},
            ],
        }

        with tempfile.TemporaryDirectory() as tmp:
            tp = pathlib.Path(tmp)
            holdout_p = tp / "eval_holdout.jsonl"
            holdout_p.write_text(json.dumps(holdout_row) + "\n", encoding="utf-8")
            holdout_idx = b2s.load_holdout_index(holdout_p)

            # 1. Valid clean-text worked derivation passes
            clean_deriv = b2s.normalise_book_sft_record(
                {
                    "id": "bk-deriv-1",
                    "task": "worked_derivation",
                    "subject": "fluid-mechanics",
                    "lang": "en",
                    "ocr_source": False,
                    "messages": [
                        {"role": "user", "content": "Derive Poiseuille velocity profile between fixed parallel plates separated by $h$."},
                        {
                            "role": "assistant",
                            "content": (
                                "From the steady axial Navier-Stokes balance we write $\\mu \\frac{d^2 u}{dy^2} = \\frac{dp}{dx}$. "
                                "Integrating once yields $\\frac{du}{dy} = \\frac{1}{\\mu}\\frac{dp}{dx} y + C_1$, and integrating again "
                                "with no-slip conditions $u(\\pm h/2) = 0$ yields $$u(y) = -\\frac{h^2}{8\\mu}\\frac{dp}{dx}\\left(1 - \\frac{4y^2}{h^2}\\right).$$ "
                                "Dimensional check: $[\\mathrm{m^2}]/[\\mathrm{Pa\\cdot s}] \\cdot [\\mathrm{Pa/m}] = [\\mathrm{m/s}]$ in SI units."
                            ),
                        },
                    ],
                }
            )
            self.assertEqual(b2s.validate_book_sft_record(clean_deriv, holdout_idx, set()), (True, "ok"))

            # 2. OCR source strictly forbidden for worked_derivation or formula exercises
            ocr_deriv = dict(clean_deriv, ocr_source=True)
            self.assertEqual(
                b2s.validate_book_sft_record(ocr_deriv, holdout_idx, set()),
                (False, "ocr_worked_derivation_forbidden"),
            )
            ocr_calc_soc = b2s.normalise_book_sft_record(
                {
                    "id": "bk-soc-ocr-risk",
                    "task": "socratic_book",
                    "subject": "fluid-mechanics",
                    "lang": "en",
                    "ocr_source": True,
                    "hidden_solution": "$$\\boxed{42.5}$$",
                    "messages": [
                        {"role": "user", "content": "Calculate the Reynolds number using the given pipe velocity and pipe diameter."},
                        {"role": "assistant", "content": "Before substituting any numbers into the formula, what are the density, velocity, characteristic length, and viscosity in SI units?"},
                    ],
                }
            )
            self.assertEqual(
                b2s.validate_book_sft_record(ocr_calc_soc, holdout_idx, set()),
                (False, "ocr_unverified_formula_exercise"),
            )

            # 3. OCR source ALLOWED for conceptual qa_theory
            ocr_qa = b2s.normalise_book_sft_record(
                {
                    "id": "bk-qa-ocr-ok",
                    "task": "qa_theory",
                    "subject": "fluid-mechanics",
                    "lang": "en",
                    "ocr_source": True,
                    "messages": [
                        {"role": "user", "content": "What physical assumption defines an incompressible fluid flow model?"},
                        {
                            "role": "assistant",
                            "content": (
                                "An incompressible flow model assumes that the density $\\rho$ of a fluid particle remains constant "
                                "following its motion, meaning $D\\rho/Dt = 0$ and the velocity field is divergence-free."
                            ),
                        },
                    ],
                }
            )
            self.assertEqual(b2s.validate_book_sft_record(ocr_qa, holdout_idx, set()), (True, "ok"))

            # 4. Quality gates: skip phrase, Phase label, emoji, unbalanced KaTeX, holdout overlap, verbatim copy
            bad_skip = dict(clean_deriv, messages=[clean_deriv["messages"][0], clean_deriv["messages"][1], {"role": "assistant", "content": clean_deriv["messages"][2]["content"] + " After some algebra it is done."}])
            self.assertEqual(b2s.validate_book_sft_record(bad_skip, holdout_idx, set()), (False, "skip_phrase"))

            bad_phase = dict(clean_deriv, messages=[clean_deriv["messages"][0], clean_deriv["messages"][1], {"role": "assistant", "content": "Phase 1: " + clean_deriv["messages"][2]["content"]}])
            self.assertEqual(b2s.validate_book_sft_record(bad_phase, holdout_idx, set()), (False, "legacy_phase_label"))

            bad_katex = dict(clean_deriv, messages=[clean_deriv["messages"][0], clean_deriv["messages"][1], {"role": "assistant", "content": clean_deriv["messages"][2]["content"] + " $broken"}])
            self.assertEqual(b2s.validate_book_sft_record(bad_katex, holdout_idx, set()), (False, "katex_unbalanced"))

            near_dup_holdout = b2s.normalise_book_sft_record(
                {
                    "id": "bk-leak",
                    "task": "qa_theory",
                    "subject": "fluid-mechanics",
                    "messages": [
                        {"role": "user", "content": holdout_prompt + " Show the exact variable."},
                        {"role": "assistant", "content": "The similarity variable scales transverse distance by the boundary-layer thickness over x."},
                    ],
                }
            )
            self.assertEqual(b2s.validate_book_sft_record(near_dup_holdout, holdout_idx, set()), (False, "holdout_contaminated"))

            src_chunk = "The continuum hypothesis treats matter as continuously distributed throughout space so macroscopic properties such as density pressure and velocity vary smoothly."
            verbatim_rec = b2s.normalise_book_sft_record(
                {
                    "id": "bk-copy",
                    "task": "qa_theory",
                    "subject": "fluid-mechanics",
                    "messages": [
                        {"role": "user", "content": "What is the continuum hypothesis in fluid mechanics?"},
                        {"role": "assistant", "content": src_chunk + " It holds when the Knudsen number is small."},
                    ],
                }
            )
            # 22 words in src_chunk < 25; test with 30-word overlap
            long_src = " ".join(f"word{i}" for i in range(40))
            verbatim_rec["messages"][2]["content"] = "Explanation: " + " ".join(f"word{i}" for i in range(30)) + " in SI units."
            self.assertEqual(
                b2s.validate_book_sft_record(verbatim_rec, holdout_idx, set(), source_chunk_text=long_src),
                (False, "verbatim_copy"),
            )

            # 5. Export CLI skips OCR books on worked_derivation
            books_p = tp / "books_cpt.jsonl"
            rep_p = tp / "books_report.json"
            clean_txt = " ".join(["engineering fluid momentum conservation law viscosity density velocity"] * 22)
            books_p.write_text(
                "\n".join([
                    json.dumps({"text": f"Clean Book\n\n{clean_txt}", "book_id": "clean-book", "subject": "fluid-mechanics", "lang": "en"}),
                    json.dumps({"text": f"OCR Book\n\n{clean_txt}", "book_id": "ocr-book", "subject": "fluid-mechanics", "lang": "en"}),
                ]) + "\n",
                encoding="utf-8",
            )
            rep_p.write_text(json.dumps({"ocr-book": {"ocr_pages": 120}}), encoding="utf-8")
            rc = b2s.main(["export", "--mode", "worked_derivation", "--books-jsonl", str(books_p), "--report", str(rep_p), "--ocr-dir", str(tp / "no_ocr"), "--out-dir", str(tp)])
            self.assertEqual(rc, 0)
            batch = (tp / "book_sft_batches_worked_derivation/batch_001.txt").read_text(encoding="utf-8")
            self.assertIn("clean-book", batch)
            self.assertNotIn("ocr-book", batch)

            # 6. Validate-merge CLI end-to-end (writes verified file & blocks invalid)
            raw_in = tp / "raw_gen.jsonl"
            verified_out = tp / "verified_book_sft.jsonl"
            raw_in.write_text(
                "\n".join([json.dumps(ocr_qa), json.dumps(ocr_deriv)]) + "\n",
                encoding="utf-8",
            )
            rc_vm = b2s.main([
                "validate-merge",
                "--inputs", str(raw_in),
                "--holdout", str(holdout_p),
                "--books-jsonl", str(books_p),
                "--out", str(verified_out),
            ])
            self.assertEqual(rc_vm, 0)
            merged_rows = [json.loads(l) for l in verified_out.read_text(encoding="utf-8").splitlines() if l.strip()]
            self.assertEqual(len(merged_rows), 1)
            self.assertEqual(merged_rows[0]["id"], "bk-qa-ocr-ok")


if __name__ == "__main__":
    unittest.main()
