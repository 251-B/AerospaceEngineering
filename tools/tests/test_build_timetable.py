"""Account calendar data (tools/build_timetable.py): official class plans read from the
vault schedule notes and written to assets/data/timetable.js."""
import pathlib
import re
import shutil
import sys
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))

import build_timetable as bt  # noqa: E402


class TimetableTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = bt.build(REPO)

    def sessions(self, slug):
        return self.data["subjects"][slug]["sessions"]

    def session(self, sid):
        for subj in self.data["subjects"].values():
            for s in subj["sessions"]:
                if s["id"] == sid:
                    return s
        self.fail(f"no session {sid}")

    def test_check_is_clean(self):
        self.assertEqual(bt.main(["--check"]), 0)

    def test_em_session_21(self):
        s = self.session("em-s21")
        self.assertEqual((s["date"], s["start"], s["room"], s["kind"]), ("2026-11-18", "15:30", "7.2.J01", "problems"))
        self.assertIn("Problems 17, 24", s["title"])
        self.assertEqual([l["href"] for l in s["links"]],
                         ["subjects/engineering-mechanics/problemas/topic-8.html#rb-17",
                          "subjects/engineering-mechanics/problemas/topic-7.html#rb-24"])

    def test_mat_groups(self):
        g = self.data["subjects"]["aerospace-materials-1"]["groups"]
        self.assertEqual(sorted(g), ["G45", "G46"])
        self.assertEqual(g["G45"]["slots"], [
            {"dow": 3, "start": "15:30", "end": "17:00", "room": "7.1.J06", "kind": "lecture"},
            {"dow": 5, "start": "15:30", "end": "17:00", "room": "7.1.J03", "kind": "lecture"}])
        self.assertEqual({s["room"] for s in g["G46"]["slots"]}, {"7.2.J02"})
        self.assertTrue(g["G46"]["dated"])

    def test_lab_groups(self):
        self.assertEqual(self.data["subjects"]["engineering-mechanics"]["labGroups"], ["A", "B"])
        self.assertEqual(self.data["subjects"]["aerospace-materials-1"]["labGroups"], [])
        self.assertEqual(self.session("em-lab3a")["lab"], "A")

    def test_ids_unique(self):
        ids = [s["id"] for subj in self.data["subjects"].values() for s in subj["sessions"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_links_exist(self):
        for subj in self.data["subjects"].values():
            for s in subj["sessions"]:
                for link in s["links"]:
                    path, _, anchor = link["href"].partition("#")
                    page = REPO / path
                    self.assertTrue(page.is_file(), link["href"])
                    if anchor:
                        self.assertIn(f'id="{anchor}"', page.read_text(encoding="utf-8"), link["href"])

    def test_no_lab_links(self):
        labs = [s for subj in self.data["subjects"].values() for s in subj["sessions"] if s["kind"] == "lab"]
        self.assertTrue(labs)
        self.assertTrue(all(s["links"] == [] for s in labs))

    def test_dates_inside_term(self):
        term = self.data["term"]
        for subj in self.data["subjects"].values():
            for s in subj["sessions"]:
                if s["date"]:
                    self.assertTrue(term["start"] <= s["date"] <= term["end"], s["id"])

    def test_days_off_from_sources(self):
        self.assertEqual(self.data["term"]["daysOff"], [
            {"date": "2026-10-09", "subjects": None, "why": "Bank holiday"},
            {"date": "2026-10-14", "subjects": ["aerospace-materials-1"], "why": "No lecture"}])
        kinds = {s["kind"] for s in self.sessions("aerospace-materials-1")}
        self.assertNotIn("holiday", kinds)
        self.assertNotIn("no-class", kinds)

    def test_maths_is_log(self):
        am = self.data["subjects"]["advanced-maths"]
        self.assertEqual(am["basis"], "log")
        self.assertEqual(len(am["sessions"]), 26)
        self.assertTrue(all(s["date"] <= "2026-11-24" for s in am["sessions"]))
        self.assertEqual(am["groups"], {})

    def test_generated_file_is_js(self):
        text = (REPO / "assets/data/timetable.js").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("/*"))
        self.assertIn("window.AE_TIMETABLE = ", text)

    def test_lab_row_with_link_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            note = REPO / "vault/03 - Engineering Mechanics/Schedule - Engineering Mechanics 2026-27.md"
            dest = root / "vault/03 - Engineering Mechanics" / note.name
            dest.parent.mkdir(parents=True)
            text = note.read_text(encoding="utf-8")
            text, n = re.subn(r"(\| em-lab1a \|.*?\| Laboratory session 1, lab group A\. \|)\s+\|",
                              r"\1 [Lab](subjects/engineering-mechanics/teoria/topic-1.html) |", text)
            self.assertEqual(n, 1)
            dest.write_text(text, encoding="utf-8")
            shutil.copytree(REPO / "subjects/engineering-mechanics", root / "subjects/engineering-mechanics")
            with self.assertRaises(ValueError):
                bt.build(root)


if __name__ == "__main__":
    unittest.main()
