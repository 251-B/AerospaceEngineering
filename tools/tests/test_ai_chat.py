"""Sideris in-page AI tutor (assets/js/ai-chat.js, ai-engine.js, ai-rag.js, assets/data/ai-models.js)
and its vault RAG index (tools/build_ai_index.py) + training utilities (tools/ai_training/)."""
import html
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import unittest

from test_focus_lab import BROWSER

REPO = pathlib.Path(__file__).resolve().parents[2]
HARNESS = pathlib.Path(__file__).resolve().parent / "ai_chat_harness.html"
MODELS_JS = REPO / "assets/data/ai-models.js"
RAG_JS = REPO / "assets/js/ai-rag.js"
ENGINE_JS = REPO / "assets/js/ai-engine.js"
CHAT_JS = REPO / "assets/js/ai-chat.js"
CHAT_CSS = REPO / "assets/css/ai-chat.css"
INDEX_DIR = REPO / "assets/data/ai-index"

sys.path.insert(0, str(REPO / "tools/ai_training"))
import rewards  # noqa: E402


def load_models():
    source = MODELS_JS.read_text(encoding="utf-8")
    m = re.search(r"window\.AE_SIDERIS_MODELS\s*=\s*(\[.*\])\s*;", source, re.S)
    if not m:
        raise AssertionError("assets/data/ai-models.js must define window.AE_SIDERIS_MODELS = [ ... ];")
    return json.loads(m.group(1))


class SiderisStaticTests(unittest.TestCase):
    """Checks that need no browser."""

    def test_models_catalogue_has_the_four_sideris_models(self):
        models = load_models()
        self.assertEqual(
            [m["name"] for m in models],
            ["Sideris Lux", "Sideris Aether", "Sideris Orion", "Sideris Titan"],
        )
        defaults = [m["id"] for m in models if m.get("default")]
        self.assertEqual(defaults, ["sideris-aether"])
        for m in models:
            self.assertEqual(m["backend"], "cloud")
            self.assertIn(m["offlineBackend"], {"webgpu", "ollama"})
            self.assertTrue(m["repo"].strip())

    def test_cloud_worker_and_config_contain_no_secrets(self):
        cfg = (REPO / "assets/data/sideris-config.js").read_text(encoding="utf-8")
        worker = (REPO / "tools/cloudflare/sideris-worker.js").read_text(encoding="utf-8")
        self.assertIn("window.AE_SIDERIS_CONFIG", cfg)
        # Workers AI only: no external provider in the worker, the engine or the settings
        engine = (REPO / "assets/js/ai-engine.js").read_text(encoding="utf-8")
        chat = (REPO / "assets/js/ai-chat.js").read_text(encoding="utf-8")
        for text in (worker, engine, chat):
            self.assertIsNone(re.search(r"(?i)GEMINI_API_KEY|GROQ_API_KEY|OPENROUTER_API_KEY|byok|api\.groq\.com|openrouter\.ai|generativelanguage", text))
        for text in (cfg, worker):
            self.assertIsNone(re.search(r"AIza[0-9A-Za-z_-]{20,}|gsk_[0-9A-Za-z]{20,}|sk-or-v1-[0-9a-f]{20,}", text))

    def test_theme_js_loads_sideris_in_order_before_solution_close(self):
        theme = (REPO / "assets/js/theme.js").read_text(encoding="utf-8")
        m = re.search(r"\[('focus-lab\.js'[^\]]*)\]\.forEach", theme)
        self.assertIsNotNone(m)
        names = re.findall(r"'([^']+)'", m.group(1))
        seq = ["../data/sideris-config.js", "../data/ai-models.js", "ai-rag.js", "ai-engine.js", "ai-chat.js", "solution-close.js"]
        for item in seq:
            self.assertIn(item, names)
        positions = [names.index(item) for item in seq]
        self.assertEqual(positions, sorted(positions))
        self.assertEqual(names[-1], "solution-close.js")

    def test_storage_keys_never_contain_theme(self):
        js = CHAT_JS.read_text(encoding="utf-8")
        self.assertIn("var KEY = 'ae_sideris';", js)
        self.assertIn("var CHATS_KEY = 'ae_sideris_chats';", js)
        keys = set(re.findall(r"localStorage\.(?:get|set)Item\(([^,)]+)", js))
        self.assertEqual(keys, {"KEY", "CHATS_KEY", "LANG_KEY"})

    def test_no_dynamic_inner_html_in_chat(self):
        js = CHAT_JS.read_text(encoding="utf-8")
        for m in re.finditer(r"innerHTML\s*=\s*([^;]+);", js):
            self.assertEqual(m.group(1).strip(), "inner", m.group(0))
        self.assertNotIn("insertAdjacentHTML", js)

    def test_no_emoji_in_sideris_assets(self):
        emoji = re.compile("[☀-➿\U0001f000-\U0001faff⬀-⯿]")
        for path in (MODELS_JS, RAG_JS, ENGINE_JS, CHAT_JS, CHAT_CSS):
            self.assertIsNone(emoji.search(path.read_text(encoding="utf-8")), path.name)

    def test_skipped_in_print_mode_and_print_css_untouched(self):
        for path in (RAG_JS, ENGINE_JS, CHAT_JS):
            self.assertIn("has('print')", path.read_text(encoding="utf-8"), path.name)
        css = CHAT_CSS.read_text(encoding="utf-8")
        self.assertRegex(css, r"@media print\s*\{\s*\.sd-launcher, \.sd-drawer, \.sd-backdrop \{ display: none !important; \}")
        self.assertIn('html[data-theme="print"] .sd-launcher', css)
        print_css = (REPO / "assets/css/print.css").read_text(encoding="utf-8")
        self.assertNotIn("sideris", print_css.lower())
        self.assertNotIn(".sd-", print_css)

    def test_text_colours_come_strictly_from_reading_palette(self):
        css = CHAT_CSS.read_text(encoding="utf-8")
        colours = set(re.findall(r"(?<![-\w])color:\s*([^;]+);", css))
        self.assertTrue(colours)
        self.assertTrue(colours <= {"var(--sd-text)", "var(--sd-muted)", "var(--sd-surface)"}, colours)

    def test_no_page_carries_its_own_sideris_tag(self):
        for page in list((REPO / "subjects").glob("*/*/*.html")) + [REPO / "index.html"]:
            text = page.read_text(encoding="utf-8")
            self.assertNotIn("ai-chat.js", text, page)
            self.assertNotIn("ai-models.js", text, page)

    def test_rag_index_is_fresh_and_contains_no_lab_material(self):
        proc = subprocess.run(
            [sys.executable, str(REPO / "tools/build_ai_index.py"), "--check"],
            capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)
        manifest = json.loads((INDEX_DIR / "manifest.json").read_text(encoding="utf-8"))
        self.assertGreater(manifest["total"], 1000)
        self.assertEqual(len(manifest["subjects"]), 5)
        for slug, info in manifest["subjects"].items():
            shard = json.loads((INDEX_DIR / info["file"]).read_text(encoding="utf-8"))
            self.assertEqual(shard["count"], info["chunks"])
            for c in shard["chunks"]:
                self.assertNotRegex(c["t"].lower(), r"laborator|\blabs?\b", slug)

    def test_grpo_rewards_catch_leaks_skips_and_bad_katex(self):
        self.assertEqual(rewards.katex_syntax_reward(["$u = U y / h$"]), [0.5])
        self.assertEqual(rewards.katex_syntax_reward(["$u = U y / h"]), [-0.5])
        self.assertEqual(rewards.katex_syntax_reward([r"\text{price } 5 \euro"]), [-0.5])
        self.assertEqual(
            rewards.no_skip_rigour_reward(["By the chain rule we obtain v = 2 m/s. Dimensional check: [L T^-1]."]),
            [0.5],
        )
        self.assertLess(rewards.no_skip_rigour_reward(["After some algebra we get 2."])[0], 0.0)
        self.assertEqual(
            rewards.socratic_guard_reward(
                ["Which conservation law applies to this control volume?"],
                socratic=[True],
                forbidden_answers=["42.5 Pa"],
            ),
            [1.0],
        )
        self.assertEqual(
            rewards.socratic_guard_reward(
                ["The final pressure is 42.5 Pa. Does that make sense?"],
                socratic=[True],
                forbidden_answers=["42.5 Pa"],
            ),
            [-1.0],
        )

    def test_dataset_sanitiser_removes_legacy_phase_labels_and_emojis(self):
        import build_dataset  # noqa: E402
        dirty = "## 📊 1. Phase 1: Hypotheses and Data\n✅ Check result: $p = \\rho g h$."
        cleaned = build_dataset.sanitise_text(dirty)
        self.assertNotIn("Phase 1", cleaned)
        self.assertNotIn("📊", cleaned)
        self.assertNotIn("✅", cleaned)
        self.assertIn("$p = \\rho g h$", cleaned)
        self.assertTrue(build_dataset.katex_balanced(cleaned))
        self.assertTrue((REPO / "tools/ai_training/Sideris_Train_Colab_Kaggle.ipynb").is_file())


@unittest.skipUnless(BROWSER, "no Chromium-based browser available for headless tests")
class SiderisBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as profile:
            proc = subprocess.run(
                [BROWSER, "--headless=new", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                 f"--user-data-dir={profile}", "--virtual-time-budget=25000", "--dump-dom", HARNESS.as_uri()],
                capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120,
            )
        m = re.search(r'<pre id="results">(.*?)</pre>', proc.stdout, re.S)
        if not m or m.group(1).strip() == "PENDING":
            raise AssertionError(f"harness produced no results; stderr={proc.stderr[-300:]!r}")
        cls.results = json.loads(html.unescape(m.group(1)))

    def test_harness_ran_every_scenario(self):
        self.assertEqual(len(self.results), 31)

    def test_prebuilt_index_tokenizer_matches_the_browser(self):
        sys.path.insert(0, str(REPO / "tools"))
        import build_ai_index
        sample = [r for r in self.results if r["name"] == "tokenizer-sample"][0]
        text = "Explícame el \\nabla \\cdot u = 0 con r_1, EBITDA y la Ecuación de Navier-Stokes (2024) of the fluid"
        self.assertEqual(build_ai_index.tokenize(text), json.loads(sample["detail"]))

    def test_every_scenario_passes(self):
        failures = [f"{r['name']}: {r['detail']}" for r in self.results if not r["pass"]]
        self.assertEqual(failures, [], "\n" + "\n".join(failures))
