#!/usr/bin/env python3
"""Assembles boolean search strings from the profile and prints them.

It opens nothing. The boards worth searching block agents, so the method hands
the queries to the person instead of pretending to run them.
"""
import re
import sys
from pathlib import Path

PROFILE_PATH = Path(__file__).resolve().parent.parent / "profile" / "PROFILE.md"

SITES = ["site:lever.co", "site:greenhouse.io", "site:ashbyhq.com", ""]

INTERNATIONAL = ["Remote", "Worldwide", "EOR", "contractor"]
REACH = {
    "international": INTERNATIONAL,
    "domestic": [],
    # A superset of queries costs nothing but a longer list to read, and the
    # spec makes all three values valid, so this key is not optional.
    "both": INTERNATIONAL,
}


def _group(terms) -> str:
    return "(" + " OR ".join(f'"{t}"' for t in terms) + ")"


def build_queries(profile: dict) -> list[str]:
    """One boolean query per site template, crossing roles, stack and reach."""
    reach = REACH[profile["target_market"]]
    locations = list(dict.fromkeys(list(profile.get("location_terms", [])) + reach))
    groups = [_group(profile[k]) for k in ("roles", "stack") if profile.get(k)]
    if locations:
        groups.append(_group(locations))
    body = " ".join(groups)
    return [f"{site} {body}".strip() for site in SITES]


def read_profile(path: Path = PROFILE_PATH) -> dict:
    """Reads the front matter of profile/PROFILE.md into the dict build_queries takes."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---", text, re.S)
    if not match:
        raise SystemExit(f"{path} has no front matter")
    profile, key = {}, None
    for line in match.group(1).splitlines():
        item = re.match(r"\s*-\s+(.*)", line)
        pair = re.match(r"([\w-]+):\s*(.*)", line)
        if item and key:
            profile[key].append(item.group(1).strip().strip("\"'"))
        elif pair:
            key, value = pair.group(1), pair.group(2).strip()
            if value.startswith("["):
                profile[key] = [v.strip().strip("\"'") for v in value[1:-1].split(",") if v.strip()]
            elif value:
                profile[key] = value.strip("\"'")
            else:
                profile[key] = []
    return profile


if __name__ == "__main__":
    if not PROFILE_PATH.exists():
        sys.exit(f"no profile yet: {PROFILE_PATH}")
    for query in build_queries(read_profile()):
        print(query)
