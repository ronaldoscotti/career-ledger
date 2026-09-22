#!/usr/bin/env python3
"""Validated writes to applications/applications.json.

Exists because the rule in prose, "update the tracker in the same turn", failed:
on 2026-07-30 four cards read `sent` while their own situation text said the
material had never left the repo. Prose does not validate. This does.
"""
import json
import re
from datetime import date
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "applications" / "applications.json"

STATUSES = ["ready", "sent", "process", "offer", "limbo",
            "paused", "rejected", "failed", "withdrew"]
# Every status but `ready` asserts something left the repo, so every one of them
# needs a date. A required date is an assertion that cannot be made vaguely.
REQUIRE_SENT_ON = set(STATUSES) - {"ready"}
LEVELS = ["strong", "good", "stretch"]
FIELDS = ["id", "company", "site", "role", "status", "level", "triaged_on",
          "sent_on", "moved_on", "comp", "resume", "fit", "situation",
          "next", "files"]
FROZEN = ["fit", "level"]
ISO = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class ValidationError(Exception):
    pass


def validate_card(c: dict) -> None:
    missing = [f for f in FIELDS if f not in c]
    if missing:
        raise ValidationError(f"missing field(s): {', '.join(missing)}")
    if c["status"] not in STATUSES:
        raise ValidationError(f"unknown status {c['status']!r}")
    if c["level"] not in LEVELS:
        raise ValidationError(f"unknown level {c['level']!r}")
    for field in ("triaged_on", "moved_on"):
        if not ISO.match(c[field]):
            raise ValidationError(f"{field} must be ISO yyyy-mm-dd, got {c[field]!r}")
    if c["status"] in REQUIRE_SENT_ON and not ISO.match(c["sent_on"]):
        raise ValidationError(
            f"status {c['status']!r} asserts the application left the repo "
            f"and requires sent_on")
    if not c["fit"].strip():
        raise ValidationError("fit is the judgment of the day and cannot be empty")
