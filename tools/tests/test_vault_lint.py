"""Tests for tools/vault_lint.py (Obsidian vault linter with safe auto-fixes)."""
import pathlib
import sys
import tempfile
import unittest

TOOLS = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import vault_lint as vl  # noqa: E402

FM = "---\ntags:\n  - teoria\nsubject: Fluid Mechanics\ntopic: 1\n---\n"


class VaultCase(unittest.TestCase):
    def repo(self, notes, extra=None):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = pathlib.Path(tmp.name)
        for rel, content in {**notes, **(extra or {})}.items():
            p = root / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            if isinstance(content, bytes):
                p.write_bytes(content)
            else:
                p.write_text(content, encoding="utf-8", newline="")
        return root

    def lint(self, notes, extra=None):
        root = self.repo(notes, extra)
        return vl.lint(root / "vault")

    def of(self, findings, check):
        return [f for f in findings if f.check == check]

    def note(self, body, name="A.md"):
        return {f"vault/01/{name}": FM + body}


class FrontmatterTests(VaultCase):
    def test_note_without_frontmatter_is_an_error(self):
        f = self.lint({"vault/01/A.md": "# Title\n"})
        hits = self.of(f, "no-frontmatter")
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0].severity, "error")

    def test_complete_frontmatter_passes(self):
        self.assertEqual(self.lint(self.note("# T\n")), [])

    def test_missing_tags_is_a_warning(self):
        f = self.lint({"vault/01/A.md": "---\nsubject: X\n---\n# T\n"})
        hits = self.of(f, "frontmatter-keys")
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0].severity, "warn")

    def test_spanish_key_names_are_accepted(self):
        f = self.lint({"vault/01/A.md": "---\ntags: [a]\nmateria: Fluidos\n---\n# T\n"})
        self.assertEqual(self.of(f, "frontmatter-keys"), [])

    def test_obsidian_templates_and_attachments_are_not_linted(self):
        f = self.lint({"vault/.obsidian/app.json": "{}", "vault/Templates/T.md": "# {{title}} [[Nombre]]",
                       "vault/attachments/README.md": "# x"})
        self.assertEqual(f, [])


class BacktickedLinkTests(VaultCase):
    def test_backticked_wikilink_is_flagged(self):
        f = self.lint(self.note("See `[[A]]` now\n"))
        self.assertEqual(len(self.of(f, "backticked-wikilink")), 1)

    def test_backticked_alias_link_is_flagged(self):
        f = self.lint(self.note("See `[[A|alias]]`\n"))
        self.assertEqual(len(self.of(f, "backticked-wikilink")), 1)

    def test_alias_containing_square_brackets_is_still_a_link(self):
        text = "see `[[A|Direction [111] of Fe]]` now\n"
        self.assertEqual(len(self.of(self.lint(self.note(text)), "backticked-wikilink")), 1)
        fixed, counts = vl.fix_text(text)
        self.assertEqual(fixed, "see [[A|Direction [111] of Fe]] now\n")
        self.assertEqual(counts["backticked-wikilink"], 1)

    def test_span_with_two_links_and_prose_between_is_left_alone(self):
        text = "`[[A]] then text [[B]]`\n"
        fixed, _ = vl.fix_text(text)
        self.assertEqual(fixed, text)

    def test_link_inside_fenced_block_is_not_flagged(self):
        f = self.lint(self.note("```\n`[[A]]`\n```\n"))
        self.assertEqual(self.of(f, "backticked-wikilink"), [])

    def test_plain_wikilink_is_fine(self):
        self.assertEqual(self.of(self.lint(self.note("See [[A]]\n")), "backticked-wikilink"), [])

    def test_fix_unwraps_exact_single_link_spans_only(self):
        text = "a `[[A]]` b `[[A|x]]` c `see [[A]] too` d `code`\n"
        fixed, counts = vl.fix_text(text)
        self.assertEqual(fixed, "a [[A]] b [[A|x]] c `see [[A]] too` d `code`\n")
        self.assertEqual(counts["backticked-wikilink"], 2)

    def test_fix_leaves_fenced_code_untouched(self):
        text = "```\n`[[A]]` and \\text{a & b}\n```\n"
        fixed, counts = vl.fix_text(text)
        self.assertEqual(fixed, text)
        self.assertEqual(sum(counts.values()), 0)

    def test_fix_is_idempotent(self):
        text = "x `[[A]]` y $\\text{P&L}$\n"
        once, _ = vl.fix_text(text)
        twice, counts = vl.fix_text(once)
        self.assertEqual(once, twice)
        self.assertEqual(sum(counts.values()), 0)


class AmpersandTests(VaultCase):
    def test_ampersand_in_text_macro_is_flagged(self):
        f = self.lint(self.note(r"$$\text{Cash & Deposits}$$" + "\n"))
        self.assertEqual(len(self.of(f, "text-ampersand")), 1)

    def test_escaped_ampersand_and_array_separator_pass(self):
        body = r"$\text{P\&L}$ $$\begin{array}{cc} a & b \end{array}$$" + "\n"
        self.assertEqual(self.of(self.lint(self.note(body)), "text-ampersand"), [])

    def test_fix_escapes_only_unescaped_ampersands_inside_text(self):
        text = r"$\text{A & B \& C}$ and a & b" + "\n"
        fixed, counts = vl.fix_text(text)
        self.assertEqual(fixed, r"$\text{A \& B \& C}$ and a & b" + "\n")
        self.assertEqual(counts["text-ampersand"], 1)


class WikilinkResolutionTests(VaultCase):
    def lint_links(self, body, extra=None):
        notes = {**self.note(body), **(extra or {})}
        notes.setdefault("vault/01/Target Note.md", FM + "# t\n")
        return self.of(self.lint(notes), "broken-wikilink")

    def test_missing_target_is_an_error(self):
        self.assertEqual(len(self.lint_links("[[Does Not Exist]]\n")), 1)

    def test_resolves_by_stem(self):
        self.assertEqual(self.lint_links("[[Target Note]]\n"), [])

    def test_resolves_by_folder_path_alias_heading_and_block(self):
        body = "[[01/Target Note|alias]] [[Target Note#Heading]] [[Target Note^abc]] ![[Target Note]]\n"
        self.assertEqual(self.lint_links(body), [])

    def test_resolution_is_case_insensitive_like_obsidian(self):
        self.assertEqual(self.lint_links("[[target note]]\n"), [])

    def test_resolves_attachment_file_names(self):
        self.assertEqual(self.lint_links("[[slides.pdf]]\n", {"vault/attachments/slides.pdf": b"%PDF"}), [])

    def test_broken_link_with_bracketed_alias_is_detected(self):
        self.assertEqual(len(self.lint_links("[[Nope|Direction [111] of Fe]]\n")), 1)

    def test_same_note_heading_links_are_fine(self):
        self.assertEqual(self.lint_links("[[#Local heading]]\n"), [])

    def test_fenced_code_links_are_ignored(self):
        self.assertEqual(self.lint_links("```\n[[Nope]]\n```\n"), [])

    def test_backticked_broken_link_is_still_reported(self):
        self.assertEqual(len(self.lint_links("`[[Nope]]`\n")), 1)


class SourcePathTests(VaultCase):
    def test_dangling_source_path_is_an_error(self):
        f = self.lint(self.note("Ref: sources/cuatrimestre-1/x/Notes.pdf, Ch. 2\n"))
        self.assertEqual(len(self.of(f, "dangling-source-path")), 1)

    def test_existing_source_path_with_spaces_passes(self):
        extra = {"sources/cuatrimestre-1/x/Session 2 T1.pdf": b"%PDF"}
        f = self.lint(self.note("From `sources/cuatrimestre-1/x/Session 2 T1.pdf`.\n"), extra)
        self.assertEqual(self.of(f, "dangling-source-path"), [])

    def test_path_in_frontmatter_is_checked(self):
        note = {"vault/01/A.md": '---\ntags: [a]\nsubject: s\nfuente: "sources/old/K1.pdf"\n---\n# T\n'}
        self.assertEqual(len(self.of(self.lint(note), "dangling-source-path")), 1)


class LanguageTests(VaultCase):
    SPANISH = ("La ecuación de conservación de la masa para un volumen de control que se mueve con el fluido "
               "es una de las leyes que se utilizan para el análisis de los flujos en los que el fluido "
               "se considera como un medio continuo con las propiedades que se definen en el tema.\n")
    ENGLISH = ("The conservation of mass for a control volume that moves with the fluid is one of the laws "
               "which are used for the analysis of flows in which the fluid is treated as a continuum "
               "with the properties that are defined in the topic.\n")

    def test_spanish_note_is_warned(self):
        hits = self.of(self.lint(self.note(self.SPANISH)), "spanish-note")
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0].severity, "warn")

    def test_english_note_passes(self):
        self.assertEqual(self.of(self.lint(self.note(self.ENGLISH)), "spanish-note"), [])

    def test_math_and_code_do_not_count_as_prose(self):
        body = "$$ el la los de que para con una $$\n```\nel la los de que para con una\n```\n" + self.ENGLISH
        self.assertEqual(self.of(self.lint(self.note(body)), "spanish-note"), [])


class FixRunnerTests(VaultCase):
    def test_fix_rewrites_files_preserving_crlf_and_accents(self):
        original = (FM.replace("\n", "\r\n") + "Ecuación `[[A]]`\r\n$\\text{a & b}$\r\n")
        root = self.repo({"vault/01/A.md": original})
        summary = vl.fix(root / "vault")
        data = (root / "vault/01/A.md").read_bytes().decode("utf-8")
        self.assertEqual(data, FM.replace("\n", "\r\n") + "Ecuación [[A]]\r\n$\\text{a \\& b}$\r\n")
        self.assertEqual(summary["files_changed"], 1)
        self.assertEqual(summary["backticked-wikilink"], 1)
        self.assertEqual(summary["text-ampersand"], 1)

    def test_crlf_note_with_code_fence_still_fixes_text_after_the_fence(self):
        original = (FM.replace("\n", "\r\n")
                    + "```text\r\ncode `[[Keep]]`\r\n```\r\nafter `[[A]]` and $\\text{a & b}$\r\n")
        root = self.repo({"vault/01/A.md": original})
        vl.fix(root / "vault")
        data = (root / "vault/01/A.md").read_bytes().decode("utf-8")
        self.assertIn("code `[[Keep]]`", data)                       # inside the fence: untouched
        self.assertIn("after [[A]] and $\\text{a \\& b}$", data)     # after the fence: fixed

    def test_fix_does_not_touch_clean_files(self):
        root = self.repo(self.note("clean\n"))
        path = root / "vault/01/A.md"
        before = path.stat().st_mtime_ns
        self.assertEqual(vl.fix(root / "vault")["files_changed"], 0)
        self.assertEqual(path.stat().st_mtime_ns, before)

    def test_fix_skips_non_utf8_files_without_corrupting_them(self):
        raw = FM.encode() + b"caf\xe9 `[[A]]`\n"
        root = self.repo({"vault/01/A.md": raw})
        summary = vl.fix(root / "vault")
        self.assertEqual((root / "vault/01/A.md").read_bytes(), raw)
        self.assertEqual(summary["skipped"], 1)


class RunnerTests(VaultCase):
    def test_exit_one_on_errors_zero_on_warnings_only(self):
        root = self.repo({"vault/01/A.md": "# no frontmatter\n"})
        self.assertEqual(vl.main(["--root", str(root / "vault"), "--quiet"]), 1)
        root2 = self.repo({"vault/01/A.md": "---\nsubject: X\n---\n# T\n"})  # warn only
        self.assertEqual(vl.main(["--root", str(root2 / "vault"), "--quiet"]), 0)

    def test_fix_flag_resolves_fixable_errors(self):
        root = self.repo(self.note("see `[[A]]` $\\text{a & b}$\n"))
        self.assertEqual(vl.main(["--root", str(root / "vault"), "--quiet"]), 1)
        self.assertEqual(vl.main(["--root", str(root / "vault"), "--quiet", "--fix"]), 0)
        self.assertEqual(vl.main(["--root", str(root / "vault"), "--quiet"]), 0)


if __name__ == "__main__":
    unittest.main()
