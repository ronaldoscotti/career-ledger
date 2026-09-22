import unittest
from check_method import parse_lines


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


if __name__ == "__main__":
    unittest.main()
