#!/usr/bin/env python3
"""Validated writes to applications/applications.json.

Exists because the rule in prose, "update the tracker in the same turn", failed:
on 2026-07-30 four cards read `sent` while their own situation text said the
material had never left the repo. Prose does not validate. This does.
"""
import argparse
import json
import re
import sys
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


def apply_update(existing: dict, changes: dict, today: str | None = None) -> dict:
    for field in FROZEN:
        if field in changes and changes[field] != existing[field]:
            raise ValidationError(
                f"{field} is frozen: it is the judgment of the day the posting was "
                f"read. What changes with time belongs in situation and next")
    updated = {**existing, **changes}
    updated["moved_on"] = today or date.today().isoformat()
    validate_card(updated)
    return updated


def demote(data: dict, card_id: str, reason: str, today: str | None = None) -> None:
    """A posting that never became contact is not an application.

    Without this, the funnel inflates and `withdrew` stops measuring abandoned
    processes, which is the only thing it is good for.
    """
    match = next((c for c in data["applications"] if c["id"] == card_id), None)
    if match is None:
        raise ValidationError(f"no application with id {card_id!r}")
    data["applications"].remove(match)
    data["triage"].append({
        "company": match["company"],
        "role": match["role"],
        "reason": reason,
        "date": today or date.today().isoformat(),
    })


def load() -> dict:
    return json.loads(DATA.read_text(encoding="utf-8"))


def save(data: dict) -> None:
    """Write to a temporary file and rename it over the original.

    An interrupted write must not be able to truncate the funnel.
    """
    data["updated"] = date.today().isoformat()
    tmp = DATA.with_name(DATA.name + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(DATA)


def find(data: dict, card_id: str) -> int:
    match = next((i for i, c in enumerate(data["applications"]) if c["id"] == card_id), None)
    if match is None:
        raise ValidationError(f"no application with id {card_id!r}")
    return match


def supplied(args) -> dict:
    """Only the flags actually given on the command line.

    A merge of the whole namespace would send `None` for every omitted optional,
    and `None != existing['fit']` makes the frozen-field check reject every move.
    """
    return {k: v for k, v in vars(args).items()
            if v is not None and k not in ("command", "id")}


def cmd_new(args) -> int:
    data = load()
    if any(c["id"] == args.id for c in data["applications"]):
        raise ValidationError(f"an application with id {args.id!r} already exists")
    today = date.today().isoformat()
    card = {"id": args.id, "company": args.company, "site": args.site,
            "role": args.role, "status": args.status, "level": args.level,
            "triaged_on": today, "sent_on": "", "moved_on": today,
            "comp": args.comp, "resume": args.resume, "fit": args.fit,
            "situation": args.situation, "next": args.next, "files": {}}
    validate_card(card)
    data["applications"].append(card)
    save(data)
    return 0


def cmd_move(args) -> int:
    data = load()
    i = find(data, args.id)
    data["applications"][i] = apply_update(data["applications"][i], supplied(args))
    save(data)
    return 0


def cmd_file(args) -> int:
    data = load()
    data["applications"][find(data, args.id)]["files"][args.label] = args.path
    save(data)
    return 0


def cmd_no(args) -> int:
    data = load()
    data["triage"].append({"company": args.company, "role": args.role,
                           "reason": args.reason, "date": date.today().isoformat()})
    save(data)
    return 0


def cmd_demote(args) -> int:
    data = load()
    demote(data, args.id, args.reason)
    save(data)
    return 0


def cmd_check(args) -> int:
    """Exit code is the point: it is how anyone finds out whether the funnel lies."""
    failures = 0
    for c in load()["applications"]:
        try:
            validate_card(c)
        except ValidationError as e:
            print(f"{c.get('id', '?')}: {e}", file=sys.stderr)
            failures += 1
    return 1 if failures else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validated writes to the application funnel.")
    sub = parser.add_subparsers(dest="command", required=True)

    new = sub.add_parser("new", help="add a card to the funnel")
    for flag in ("--id", "--company", "--site", "--role", "--level", "--resume",
                 "--fit", "--situation", "--next"):
        new.add_argument(flag, required=True)
    new.add_argument("--comp", default="")
    new.add_argument("--status", default="ready")

    move = sub.add_parser("move", help="change the status of a card")
    move.add_argument("--id", required=True)
    # No `choices`: argparse would exit 2 before validate_card could name the status.
    move.add_argument("--status", required=True)
    for flag in ("--sent-on", "--situation", "--next", "--comp"):
        move.add_argument(flag)
    # Accepted only so they can be refused by apply_update rather than by argparse.
    for flag in ("--fit", "--level"):
        move.add_argument(flag)

    attach = sub.add_parser("file", help="record a file produced for a card")
    attach.add_argument("--id", required=True)
    attach.add_argument("--label", required=True)
    attach.add_argument("--path", required=True)

    no = sub.add_parser("no", help="record a posting that was never pursued")
    for flag in ("--company", "--role", "--reason"):
        no.add_argument(flag, required=True)

    down = sub.add_parser("demote", help="move a card from applications to triage")
    down.add_argument("--id", required=True)
    down.add_argument("--reason", required=True)

    sub.add_parser("check", help="validate every card in the funnel")
    return parser


COMMANDS = {"new": cmd_new, "move": cmd_move, "file": cmd_file,
            "no": cmd_no, "demote": cmd_demote, "check": cmd_check}


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return COMMANDS[args.command](args)
    except ValidationError as e:
        print(e, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
