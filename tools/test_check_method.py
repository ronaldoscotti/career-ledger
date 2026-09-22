import unittest
from check_method import parse_lines, Finding, check_money, check_timezone


class Ctx:
    allowlist: set = set()
    denylist: set = set()
    contract_paths: list = []
    root = None
    path: str = "<test>"


class TestParseLines(unittest.TestCase):
    def test_marks_fenced_blocks(self):
        lines = parse_lines("before\n```\ninside\n```\nafter\n")
        self.assertEqual([l.in_fence for l in lines], [False, True, True, True, False])

    def test_marks_language_sections(self):
        text = "en\n<!-- lang:pt-BR -->\nnao\n<!-- /lang -->\nen again\n"
        lines = parse_lines(text)
        self.assertEqual([l.in_lang for l in lines], [False, True, True, True, False])

    def test_marks_headings(self):
        lines = parse_lines("# Title\ntext\n## Sub\n")
        self.assertEqual([l.is_heading for l in lines], [True, False, True])

    def test_strips_code_spans(self):
        lines = parse_lines("see `tools/tracker.py` now\n")
        # Three spaces: the one before the span, the substitution, the one after.
        # Substituting with "" instead would glue `a`x`b` into `ab` and destroy
        # the word boundaries the proper-noun and language checks rely on.
        self.assertEqual(lines[0].prose, "see   now")

    def test_keeps_line_numbers_one_based(self):
        lines = parse_lines("a\nb\n")
        self.assertEqual([l.no for l in lines], [1, 2])


class TestMoney(unittest.TestCase):
    def test_flags_currency_symbol(self):
        found = check_money(parse_lines("the floor is US$120k\n"), Ctx())
        self.assertEqual(len(found), 1)

    def test_flags_bare_thousands(self):
        self.assertEqual(len(check_money(parse_lines("asking 160k\n"), Ctx())), 1)

    def test_flags_iso_code(self):
        self.assertEqual(len(check_money(parse_lines("BRL 20000 monthly\n"), Ctx())), 1)

    def test_allows_plain_numbers(self):
        self.assertEqual(check_money(parse_lines("keep it to 2 pages\n"), Ctx()), [])

    def test_allows_ordinary_english_with_numbers(self):
        # Every one of these matched while the pattern carried a blanket IGNORECASE.
        for ok in ["wait for 24 hours", "after 3 weeks", "under 5 minutes",
                   "over 100 applications", "LAYER 3 is state"]:
            with self.subTest(ok=ok):
                self.assertEqual(check_money(parse_lines(ok + "\n"), Ctx()), [])

    def test_allows_inside_language_section(self):
        text = "<!-- lang:pt-BR -->\nUS$120k\n<!-- /lang -->\n"
        self.assertEqual(check_money(parse_lines(text), Ctx()), [])


class TestTimezone(unittest.TestCase):
    def test_flags_utc_offset(self):
        self.assertEqual(len(check_timezone(parse_lines("works UTC-3\n"), Ctx())), 1)

    def test_flags_iana_zone(self):
        self.assertEqual(len(check_timezone(parse_lines("America/Sao_Paulo\n"), Ctx())), 1)

    def test_flags_abbreviation(self):
        self.assertEqual(len(check_timezone(parse_lines("overlap with PST\n"), Ctx())), 1)

    def test_does_not_flag_country_names(self):
        # Country and city names belong to the proper-noun check, not this one.
        self.assertEqual(check_timezone(parse_lines("hiring in Brazil\n"), Ctx()), [])


if __name__ == "__main__":
    unittest.main()
