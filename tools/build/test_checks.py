import os
import tempfile
import unittest

from checks import ats_failures, count_em_dashes, count_pages_from_pdf, keyword_coverage


class TestChecks(unittest.TestCase):
    def test_counts_em_dashes(self):
        self.assertEqual(count_em_dashes("a — b — c"), 2)

    def test_hyphen_is_not_an_em_dash(self):
        self.assertEqual(count_em_dashes("well-known trade-off"), 0)

    def test_keyword_coverage_is_a_ratio(self):
        posting = "We need TypeScript, Postgres and Kubernetes experience."
        resume = "Built TypeScript services on Postgres."
        self.assertAlmostEqual(keyword_coverage(resume, posting), 2 / 3, places=2)

    def test_keyword_coverage_ignores_stopwords(self):
        self.assertEqual(keyword_coverage("we need and the", "we need and the"), 1.0)

    def test_ats_flags_layout_tables(self):
        self.assertIn("table", ats_failures("<body><table><tr><td>x</td></tr></table></body>"))

    def test_ats_flags_images(self):
        self.assertIn("image", ats_failures("<body><img src='x.png'></body>"))

    def test_ats_flags_letter_spacing(self):
        self.assertIn("letter-spacing", ats_failures("<h2 style='letter-spacing:2px'>X</h2>"))

    def test_ats_passes_a_clean_document(self):
        self.assertEqual(ats_failures("<body><h2>Experience</h2><ul><li>Did a thing</li></ul></body>"), [])

class TestPageCount(unittest.TestCase):
    """The one function on the critical path that a fixture run used to cover alone.

    Two pages is a hard gate on a resume, so a silently wrong count is expensive.
    """

    def _pdf(self, body: bytes) -> str:
        handle = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
        handle.write(b"%PDF-1.4\n" + body + b"\n%%EOF\n")
        handle.close()
        self.addCleanup(os.unlink, handle.name)
        return handle.name

    def test_reads_count_after_type(self):
        path = self._pdf(b"2 0 obj << /Type /Pages /Kids [3 0 R] /Count 3 >> endobj")
        self.assertEqual(count_pages_from_pdf(path), 3)

    def test_reads_count_before_type(self):
        path = self._pdf(b"2 0 obj << /Count 5 /Kids [3 0 R] /Type /Pages >> endobj")
        self.assertEqual(count_pages_from_pdf(path), 5)

    def test_prefers_the_page_tree_over_the_outline(self):
        path = self._pdf(b"1 0 obj << /Type /Outlines /Count 9 >> endobj\n"
                         b"2 0 obj << /Type /Pages /Count 2 >> endobj")
        self.assertEqual(count_pages_from_pdf(path), 2)

    def test_returns_zero_when_absent(self):
        self.assertEqual(count_pages_from_pdf(self._pdf(b"nothing here")), 0)

