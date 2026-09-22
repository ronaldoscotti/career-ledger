import unittest

from scan import build_queries

PROFILE = {
    "target_market": "international",
    "roles": ["staff software engineer", "principal engineer"],
    "stack": ["TypeScript", "Node"],
    "location_terms": ["Remote", "Latam"],
}


class TestQueries(unittest.TestCase):
    def test_includes_every_role(self):
        q = " ".join(build_queries(PROFILE))
        self.assertIn("staff software engineer", q)
        self.assertIn("principal engineer", q)

    def test_international_market_injects_its_own_terms(self):
        # REACH is injected by the function, not carried in the profile. Asserting
        # on a plain location term instead would pass against a function that does
        # no market gating whatsoever.
        q = " ".join(build_queries(PROFILE))
        self.assertIn("Worldwide", q)
        self.assertIn("EOR", q)

    def test_domestic_market_injects_none_of_them(self):
        q = " ".join(build_queries({**PROFILE, "target_market": "domestic"}))
        self.assertNotIn("Worldwide", q)
        self.assertNotIn("EOR", q)

    def test_both_assembles_the_international_set(self):
        # "both" is a spec-valid target_market. Without its own key, indexing
        # REACH raises KeyError on a perfectly legal profile.
        self.assertIn("Worldwide", " ".join(build_queries({**PROFILE, "target_market": "both"})))

    def test_profile_location_terms_survive_every_market(self):
        for market in ("international", "domestic", "both"):
            with self.subTest(market=market):
                q = " ".join(build_queries({**PROFILE, "target_market": market}))
                self.assertIn("Latam", q)

    def test_produces_one_query_per_site_template(self):
        self.assertGreaterEqual(len(build_queries(PROFILE)), 3)
