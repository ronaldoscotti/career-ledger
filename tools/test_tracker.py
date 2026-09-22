import unittest

from tracker import (STATUSES, REQUIRE_SENT_ON, validate_card, ValidationError,
                     apply_update, demote)


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


class TestFrozenFields(unittest.TestCase):
    def test_rejects_rewriting_fit(self):
        existing = card()
        with self.assertRaises(ValidationError):
            apply_update(existing, {"fit": "actually it was a stretch"})

    def test_rejects_rewriting_level(self):
        with self.assertRaises(ValidationError):
            apply_update(card(), {"level": "stretch"})

    def test_allows_rewriting_situation_and_next(self):
        updated = apply_update(card(), {"situation": "Sent.", "next": "Follow up 01/10."})
        self.assertEqual(updated["situation"], "Sent.")

    def test_move_stamps_moved_on(self):
        updated = apply_update(card(), {"status": "sent", "sent_on": "2026-09-23"},
                               today="2026-09-24")
        self.assertEqual(updated["moved_on"], "2026-09-24")


class TestDemotion(unittest.TestCase):
    def test_demote_moves_card_to_triage_array(self):
        data = {"updated": "", "applications": [card()], "triage": []}
        demote(data, "acme", "posting closed before sending", today="2026-09-24")
        self.assertEqual(data["applications"], [])
        self.assertEqual(data["triage"][0]["company"], "Acme")
        self.assertEqual(data["triage"][0]["reason"], "posting closed before sending")
