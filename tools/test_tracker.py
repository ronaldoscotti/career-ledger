import json
import tempfile
import unittest
from pathlib import Path

from tracker import STATUSES, REQUIRE_SENT_ON, validate_card, ValidationError


def card(**over):
    base = dict(id="acme", company="Acme", site="acme.com", role="Staff Engineer",
                status="ready", level="good", triaged_on="2026-09-22",
                sent_on="", moved_on="2026-09-22", comp="", resume="resume",
                fit="Read on 22/09. Strong on the product side.",
                situation="Triaged, material not written.", next="Write the resume.",
                files={})
    base.update(over)
    return base


class TestValidation(unittest.TestCase):
    def test_accepts_a_well_formed_ready_card(self):
        validate_card(card())

    def test_rejects_unknown_status(self):
        with self.assertRaises(ValidationError):
            validate_card(card(status="maybe"))

    def test_rejects_sent_without_date(self):
        with self.assertRaises(ValidationError):
            validate_card(card(status="sent", sent_on=""))

    def test_accepts_sent_with_date(self):
        validate_card(card(status="sent", sent_on="2026-09-23"))

    def test_rejects_missing_field(self):
        broken = card()
        del broken["fit"]
        with self.assertRaises(ValidationError):
            validate_card(broken)

    def test_rejects_non_iso_date(self):
        with self.assertRaises(ValidationError):
            validate_card(card(triaged_on="22/09/2026"))

    def test_every_status_except_ready_requires_sent_on(self):
        self.assertEqual(REQUIRE_SENT_ON, set(STATUSES) - {"ready"})
