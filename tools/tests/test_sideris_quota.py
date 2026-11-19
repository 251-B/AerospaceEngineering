"""Daily Sideris allowance per student in the Cloudflare worker (needs Node.js, skipped without it)."""
import pathlib
import shutil
import subprocess
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parents[2]
NODE = shutil.which("node")


@unittest.skipUnless(NODE, "Node.js not available")
class SiderisQuotaTests(unittest.TestCase):
    def test_student_ip_and_portal_limits(self):
        with tempfile.TemporaryDirectory() as tmp:
            # .mjs copies so Node loads the worker as an ES module on any version
            shutil.copy(REPO / "tools/cloudflare/sideris-worker.js", pathlib.Path(tmp) / "worker.mjs")
            shutil.copy(REPO / "tools/tests/sideris_quota_check.mjs", pathlib.Path(tmp) / "check.mjs")
            proc = subprocess.run([NODE, "check.mjs"], cwd=tmp, capture_output=True, text=True, timeout=60)
        self.assertEqual(proc.returncode, 0, proc.stderr[-800:])
        for line in ("student limit ok", "ip cap + refund ok", "portal cap ok", "fallback id ok", "day reset + fail-open ok"):
            self.assertIn(line, proc.stdout)


if __name__ == "__main__":
    unittest.main()
