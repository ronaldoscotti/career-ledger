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
