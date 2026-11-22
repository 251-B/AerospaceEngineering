"""partner-setup/install.py on a simulated fresh computer (temporary home, no CLI calls)."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
INSTALL = REPO / "partner-setup" / "install.py"
MANIFEST = json.loads((REPO / "partner-setup" / "manifest.json").read_text(encoding="utf-8"))


def run(*args, home):
    return subprocess.run([sys.executable, str(INSTALL), *args, "--skip-cli", "--home", str(home)],
                          capture_output=True, text=True, encoding="utf-8")


class PartnerSetupTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.home = Path(self.tmp.name)
        # What the Claude CLI steps would have produced: plugin caches and upstream skills.
        for name, spec in MANIFEST["gemini"]["built_plugins"].items():
            base = self.home / spec["from"]
            root = base if spec["from"].endswith("skills") else base / "1.0.0" / "skills"
            for skill in spec["skills"]:
                (root / skill).mkdir(parents=True, exist_ok=True)
                (root / skill / "SKILL.md").write_text(f"---\nname: {skill}\n---\n", encoding="utf-8")
        own = self.home / ".claude" / "CLAUDE.md"
        own.write_text("# My own rules\n- keep me\n", encoding="utf-8")
        cli = self.home / ".gemini" / "antigravity-cli" / "settings.json"
        cli.parent.mkdir(parents=True)
        cli.write_text(json.dumps({"permissions": {"allow": ["read_file(/Users/someone/GitHub)", "mcp(other/*)"]}}), encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_apply_then_check_passes_and_is_idempotent(self):
        plan = run("plan", home=self.home)
        self.assertEqual(plan.returncode, 0, plan.stderr)
        self.assertFalse((self.home / ".claude" / "hooks").exists(), "plan must not write")
        for _ in range(2):
            p = run("apply", home=self.home)
            self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        chk = run("check", home=self.home)
        self.assertEqual(chk.returncode, 0, chk.stdout + chk.stderr)
        claude_md = (self.home / ".claude" / "CLAUDE.md").read_text(encoding="utf-8")
        self.assertIn("- keep me", claude_md)
        self.assertEqual(claude_md.count("AE-PARTNER-SETUP:START"), 1)
        settings = json.loads((self.home / ".claude" / "settings.json").read_text(encoding="utf-8"))
        self.assertEqual(len(settings["hooks"]["UserPromptSubmit"]), 1)
        cli = json.loads((self.home / ".gemini" / "antigravity-cli" / "settings.json").read_text(encoding="utf-8"))
        allow = cli["permissions"]["allow"]
        self.assertIn("mcp(other/*)", allow, "the partner's own rules are kept")
        if sys.platform == "win32":
            self.assertNotIn("read_file(/Users/someone/GitHub)", allow, "drive-less paths break agy's sandbox")
            self.assertTrue(all(":" in x for x in allow if x.startswith(("read_file", "write_file"))))

    def test_check_fails_on_empty_home(self):
        self.assertEqual(run("check", home=self.home).returncode, 1)


if __name__ == "__main__":
    unittest.main()
