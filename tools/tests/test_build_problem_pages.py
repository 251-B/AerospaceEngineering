"""Tests for tools/build_problem_pages.py (Business Management Topic 3 problem pages from vault notes)."""
import pathlib
import re
import sys
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import build_problem_pages as bpp  # noqa: E402
import source_links as sl  # noqa: E402

NOTE = """---
tags: [x]
---

# ✏️ Problem: Demo problem

## 📄 Statement

The company sells $10$ units.

## Phase 1 — Setup

### Step 1. Revenue

$$R = 10 \\times 2$$

> [!warning] Discrepancy with the official solution
> The key differs by 1.

---

**Back to:** [[Business Management MOC]]
"""


class HelperTests(unittest.TestCase):
    def test_sections_split_statement_and_phases(self):
        md = bpp.bt.strip_frontmatter(NOTE)
        secs = bpp.sections(md)
        self.assertEqual([t for t, _ in secs], ["📄 Statement", "Phase 1 — Setup"])
        self.assertIn("sells $10$ units", secs[0][1])

    def test_render_makes_step_titles_math_and_callouts(self):
        out = bpp.render(bpp.sections(bpp.bt.strip_frontmatter(NOTE))[1][1])
        self.assertIn('<h4 class="step-title">Step 1. Revenue</h4>', out)
        self.assertIn('<div class="math-block">$$R = 10 \\times 2$$</div>', out)
        self.assertIn('class="callout callout-warning"', out)
        self.assertNotIn("<hr", out)


class RepositoryTests(unittest.TestCase):
    def test_pages_are_up_to_date_with_their_notes(self):
        self.assertEqual(bpp.main(["--check"]), 0)

    def test_every_card_has_a_statement_and_phase_blocks_and_the_official_key_section(self):
        for rel in bpp.PAGES:
            page = sl.strip_links((bpp.REPO / rel).read_text(encoding="utf-8"))
            cards = re.split(r'<section class="problem-box"', page)[1:]
            self.assertEqual(len(cards), len(bpp.PAGES[rel][1]))
            for c in cards:
                self.assertIn('class="statement-box"', c)
                self.assertIn('class="phase-block"', c)
                self.assertIn("Check against the official key", c)


if __name__ == "__main__":
    unittest.main()
