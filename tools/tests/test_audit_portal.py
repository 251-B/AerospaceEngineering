"""Tests for tools/audit_portal.py (static quality gate for index.html + subjects/)."""
import pathlib
import sys
import tempfile
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import audit_portal as ap  # noqa: E402

GOOD_PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>T</title>
<link rel="stylesheet" href="{css}">
<script>try {{ localStorage.getItem('ae_theme'); }} catch (e) {{}}</script></head>
<body><a href="{back}">Back</a><p>Energy $E=mc^2$ and
$$ \\int_0^1 x\\,dx = \\tfrac12 $$</p></body></html>
"""


def good_page(depth=3):
    back = "../" * depth + "index.html"
    css = "../" * depth + "assets/css/celestial-sky.css"
    return GOOD_PAGE.format(back=back, css=css)


class AuditCase(unittest.TestCase):
    def repo(self, files):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = pathlib.Path(tmp.name)
        base = {"index.html": "<html><body>hub</body></html>", "assets/css/celestial-sky.css": "/* css */"}
        base.update(files)
        for rel, content in base.items():
            p = root / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")
        return root

    def run_checks(self, files):
        root = self.repo(files)
        return ap.audit(root)

    def of(self, findings, check):
        return [f for f in findings if f.check == check]


class CleanPageTests(AuditCase):
    def test_well_formed_page_has_no_findings(self):
        f = self.run_checks({"subjects/fluid-mechanics/teoria/topic-1.html": good_page()})
        self.assertEqual(f, [])


class LinkTests(AuditCase):
    def test_missing_local_link_is_an_error(self):
        page = good_page() + '<a href="gone.html">x</a>'
        f = self.run_checks({"subjects/fluid-mechanics/teoria/topic-1.html": page})
        hits = self.of(f, "broken-link")
        self.assertEqual(len(hits), 1)
        self.assertIn("gone.html", hits[0].message)
        self.assertEqual(hits[0].severity, "error")

    def test_external_anchor_mailto_and_data_links_are_ignored(self):
        extra = ('<a href="https://x.org/a">e</a><a href="#top">a</a>'
                 '<a href="mailto:a@b.c">m</a><img src="data:image/png;base64,AA">')
        f = self.run_checks({"subjects/a/teoria/t.html": good_page() + extra})
        self.assertEqual(self.of(f, "broken-link"), [])

    def test_query_and_fragment_are_stripped_before_checking(self):
        page = good_page() + '<a href="other.html?x=1#sec">o</a>'
        f = self.run_checks({"subjects/a/teoria/t.html": page, "subjects/a/teoria/other.html": good_page()})
        self.assertEqual(self.of(f, "broken-link"), [])

    def test_percent_encoded_names_are_decoded(self):
        page = good_page() + '<a href="My%20File.pdf">p</a>'
        f = self.run_checks({"subjects/a/teoria/t.html": page, "subjects/a/teoria/My File.pdf": "x"})
        self.assertEqual(self.of(f, "broken-link"), [])

    def test_case_mismatch_is_flagged_because_pages_is_case_sensitive(self):
        page = good_page() + '<a href="page.html">p</a>'
        f = self.run_checks({"subjects/a/teoria/t.html": page, "subjects/a/teoria/Page.html": good_page()})
        self.assertEqual(len(self.of(f, "broken-link")), 1)

    def test_directory_link_resolves_to_its_index(self):
        page = good_page() + '<a href="sub/">s</a>'
        f = self.run_checks({"subjects/a/teoria/t.html": page, "subjects/a/teoria/sub/index.html": good_page(4)})
        self.assertEqual(self.of(f, "broken-link"), [])

    def test_links_inside_html_comments_are_ignored(self):
        page = good_page() + '<!-- <a href="nope.html">x</a> -->'
        f = self.run_checks({"subjects/a/teoria/t.html": page})
        self.assertEqual(self.of(f, "broken-link"), [])

    def test_missing_asset_src_is_an_error(self):
        page = good_page() + '<script src="../../../assets/js/missing.js"></script>'
        f = self.run_checks({"subjects/a/teoria/t.html": page})
        self.assertEqual(len(self.of(f, "broken-link")), 1)


class BacklinkTests(AuditCase):
    def test_page_without_link_to_hub_is_flagged(self):
        page = "<html><body><p>no link</p></body></html>"
        f = self.run_checks({"subjects/a/teoria/t.html": page})
        self.assertEqual(len(self.of(f, "missing-backlink")), 1)

    def test_wrong_depth_backlink_is_flagged(self):
        page = good_page(depth=2)  # resolves to subjects/index.html, not the hub
        f = self.run_checks({"subjects/a/teoria/t.html": page})
        self.assertEqual(len(self.of(f, "missing-backlink")), 1)

    def test_correct_depth_backlink_passes(self):
        f = self.run_checks({"subjects/a/teoria/t.html": good_page(3)})
        self.assertEqual(self.of(f, "missing-backlink"), [])


class KatexTests(AuditCase):
    def page(self, body):
        return good_page().replace("</body>", body + "</body>")

    def test_odd_display_delimiters_flagged(self):
        f = self.run_checks({"subjects/a/teoria/t.html": self.page("<p>$$ x = 1 </p>")})
        self.assertEqual(len(self.of(f, "katex-parity")), 1)

    def test_odd_inline_delimiters_flagged(self):
        f = self.run_checks({"subjects/a/teoria/t.html": self.page("<p>cost $5 and $x$</p>")})
        self.assertEqual(len(self.of(f, "katex-parity")), 1)

    def test_escaped_dollar_is_not_counted(self):
        f = self.run_checks({"subjects/a/teoria/t.html": self.page(r"<p>cost \$5 and $x$</p>")})
        self.assertEqual(self.of(f, "katex-parity"), [])

    def test_dollars_in_scripts_and_styles_are_ignored(self):
        body = "<script>var s = '$';</script><style>.a::after{content:'$'}</style>"
        f = self.run_checks({"subjects/a/teoria/t.html": self.page(body)})
        self.assertEqual(self.of(f, "katex-parity"), [])

    def test_ampersand_inside_text_macro_flagged(self):
        f = self.run_checks({"subjects/a/teoria/t.html": self.page(r"<p>$\text{Cash & Deposits}$</p>")})
        self.assertEqual(len(self.of(f, "katex-text-ampersand")), 1)

    def test_escaped_ampersand_and_array_separator_pass(self):
        body = r"<p>$\text{P\&L}$ $$\begin{array}{cc} a & b \end{array}$$</p>"
        f = self.run_checks({"subjects/a/teoria/t.html": self.page(body)})
        self.assertEqual(self.of(f, "katex-text-ampersand"), [])


class DebrisTests(AuditCase):
    def page(self, body):
        return good_page().replace("</body>", body + "</body>")

    def check(self, body, check="debris"):
        return self.of(self.run_checks({"subjects/a/teoria/t.html": self.page(body)}), check)

    def test_wait_scratch_work_flagged(self):
        self.assertEqual(len(self.check("<p>Wait, according to the diagram...</p>")), 1)

    def test_replacement_character_flagged(self):
        self.assertEqual(len(self.check("<p>Newton�s law</p>")), 1)

    def test_question_mark_header_flagged(self):
        self.assertEqual(len(self.check("<h3>?? Full Analytical Solution</h3>")), 1)

    def test_raw_markdown_bold_flagged(self):
        self.assertEqual(len(self.check("<li>**Rod Tension:** acts inward</li>")), 1)

    def test_raw_markdown_bullet_flagged(self):
        self.assertEqual(len(self.check("<p>\n* first item\n</p>")), 1)

    def test_spanish_label_flagged(self):
        self.assertEqual(len(self.check("<h4>Enunciado</h4>", "spanish-label")), 1)

    def test_debris_words_in_script_or_comment_are_ignored(self):
        body = "<script>// Wait for DOM\n</script><!-- Wait here -->"
        self.assertEqual(self.check(body), [])


class FalseClaimTests(AuditCase):
    def check(self, text):
        page = good_page().replace("</body>", f"<footer>{text}</footer></body>")
        return self.of(self.run_checks({"subjects/a/teoria/t.html": page}), "false-claim")

    def test_fully_verified_banner_flagged(self):
        self.assertEqual(len(self.check("Faculty solutions fully verified")), 1)

    def test_zero_hallucinations_flagged_case_insensitive(self):
        self.assertEqual(len(self.check("Zero Hallucinations Guarantee")), 1)

    def test_ordinary_use_of_verified_is_allowed(self):
        self.assertEqual(self.check("We verified the result by substitution."), [])


class LabTests(AuditCase):
    def test_link_to_laboratory_pages_flagged(self):
        page = good_page() + '<a href="../laboratorio/index.html">Lab</a>'
        f = self.run_checks({"subjects/a/teoria/t.html": page, "subjects/a/laboratorio/index.html": good_page()})
        self.assertGreaterEqual(len(self.of(f, "lab-reference")), 1)

    def test_existing_laboratory_page_file_flagged(self):
        f = self.run_checks({"subjects/a/laboratorio/lab-1.html": good_page()})
        hits = self.of(f, "lab-reference")
        self.assertEqual(len(hits), 1)
        self.assertIn("laboratorio", hits[0].file)

    def test_laboratory_frame_in_prose_is_fine(self):
        page = good_page().replace("</body>", "<p>fixed in the laboratory frame</p></body>")
        f = self.run_checks({"subjects/a/teoria/t.html": page})
        self.assertEqual(self.of(f, "lab-reference"), [])


class ThemeKeyTests(AuditCase):
    def check(self, script):
        page = good_page().replace("</body>", f"<script>{script}</script></body>")
        return self.of(self.run_checks({"subjects/a/teoria/t.html": page}), "theme-key")

    def test_legacy_theme_key_flagged(self):
        self.assertEqual(len(self.check("localStorage.setItem('theme', t);")), 1)
        self.assertEqual(len(self.check('localStorage.getItem("aero-portal-theme")')), 1)

    def test_ae_theme_and_other_keys_pass(self):
        self.assertEqual(self.check("localStorage.getItem('ae_theme'); localStorage.getItem('ae_lang');"), [])


INDEX_TMPL = """<html><body>
<article class="subject-card" data-subject="fluid-mechanics">
<a class="area-link" href="subjects/fluid-mechanics/teoria/index.html"><span class="area-badge available">{theory}</span></a>
<a class="area-link" href="subjects/fluid-mechanics/problemas/index.html"><span class="area-badge available">{problems}</span></a>
</article></body></html>"""

PROBLEM_PAGE = good_page().replace(
    "</body>", '<div class="problem-card problem">a</div><div class="problem-card">b</div></body>')


class BadgeTests(AuditCase):
    def files(self, theory, problems):
        return {
            "index.html": INDEX_TMPL.format(theory=theory, problems=problems),
            "subjects/fluid-mechanics/teoria/index.html": good_page(),
            "subjects/fluid-mechanics/teoria/topic-1.html": good_page(),
            "subjects/fluid-mechanics/teoria/topic-2.html": good_page(),
            "subjects/fluid-mechanics/teoria/topic-2-1-sub.html": good_page(),
            "subjects/fluid-mechanics/problemas/index.html": good_page(),
            "subjects/fluid-mechanics/problemas/topic-2.html": PROBLEM_PAGE,
        }

    def test_matching_badges_pass(self):
        f = self.run_checks(self.files("2 topics", "1 topic (2 prob.)"))
        self.assertEqual(self.of(f, "badge-drift"), [])

    def test_wrong_problem_count_flagged(self):
        f = self.run_checks(self.files("2 topics", "1 topic (5 prob.)"))
        hits = self.of(f, "badge-drift")
        self.assertEqual(len(hits), 1)
        self.assertIn("5", hits[0].message)
        self.assertIn("2", hits[0].message)

    def test_wrong_topic_count_flagged(self):
        f = self.run_checks(self.files("3 topics", "1 topic (2 prob.)"))
        self.assertEqual(len(self.of(f, "badge-drift")), 1)

    def test_subtopic_pages_count_once_per_topic_number(self):
        # topic-2.html and topic-2-1-sub.html are the same topic 2 -> 2 distinct topics (1, 2)
        f = self.run_checks(self.files("2 topics", "2 problems"))
        self.assertEqual(self.of(f, "badge-drift"), [])

    def test_problem_box_markup_used_by_business_pages_is_counted(self):
        files = self.files("2 topics", "1 topic (3 prob.)")
        files["subjects/fluid-mechanics/problemas/topic-2.html"] = good_page().replace(
            "</body>", '<div class="problem-box"><h3 class="problem-title">a</h3></div>' * 3 + "</body>")
        f = self.run_checks(files)
        self.assertEqual(self.of(f, "badge-drift"), [])

    def test_of_total_units_badge_checks_the_built_count(self):
        ok = self.run_checks(self.files("2 of 7 units", "2 problems"))
        self.assertEqual(self.of(ok, "badge-drift"), [])
        bad = self.run_checks(self.files("3 of 7 units", "2 problems"))
        self.assertEqual(len(self.of(bad, "badge-drift")), 1)

    def test_text_badges_without_numbers_are_ignored(self):
        f = self.run_checks(self.files("Coming Soon", "Coming Soon"))
        self.assertEqual(self.of(f, "badge-drift"), [])


class RunnerTests(AuditCase):
    def test_summary_counts_errors(self):
        root = self.repo({"subjects/a/teoria/t.html": "<p>Wait, no</p>"})
        findings = ap.audit(root)
        self.assertTrue(any(f.severity == "error" for f in findings))
        self.assertEqual(ap.main(["--root", str(root), "--quiet"]), 1)

    def test_exit_zero_when_clean(self):
        root = self.repo({"subjects/a/teoria/t.html": good_page()})
        self.assertEqual(ap.main(["--root", str(root), "--quiet"]), 0)

    def test_skip_option_removes_a_check(self):
        root = self.repo({"subjects/a/teoria/t.html": "<p>Wait, no</p>"})
        self.assertEqual(ap.main(["--root", str(root), "--quiet", "--skip", "debris,missing-backlink"]), 0)


if __name__ == "__main__":
    unittest.main()
