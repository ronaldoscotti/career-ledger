#!/usr/bin/env python3
"""The portability gate: keeps candidate data and agent vocabulary out of method/.

Exists because the system this was extracted from copied the same compensation
figure into seven files, and two of them were a month stale before anyone noticed.
Prose does not validate. This does.
"""
import re
from dataclasses import dataclass

FENCE = re.compile(r"^\s*```")
LANG_OPEN = re.compile(r"<!--\s*lang:[\w-]+\s*-->")
LANG_CLOSE = re.compile(r"<!--\s*/lang\s*-->")
CODE_SPAN = re.compile(r"`[^`]*`")


@dataclass(frozen=True)
class Line:
    no: int
    raw: str
    prose: str
    in_fence: bool
    in_lang: bool
    is_heading: bool


def parse_lines(text: str) -> list[Line]:
    out, in_fence, in_lang = [], False, False
    for no, raw in enumerate(text.splitlines(), start=1):
        opens_fence = bool(FENCE.match(raw))
        opens_lang = bool(LANG_OPEN.search(raw))
        closes_lang = bool(LANG_CLOSE.search(raw))
        if opens_fence:
            in_fence = not in_fence
        if opens_lang:
            in_lang = True
        out.append(Line(
            no=no,
            raw=raw,
            prose=CODE_SPAN.sub(" ", raw),
            in_fence=in_fence or opens_fence,
            in_lang=in_lang,
            is_heading=raw.lstrip().startswith("#"),
        ))
        if closes_lang:
            in_lang = False
    return out


# IGNORECASE is deliberately NOT applied to the whole pattern. It would make
# [$€£R] match a lowercase r, and then "wait for 24 hours", "after 3 weeks"
# and "LAYER 3" all report as money. Only the ISO codes are case-insensitive.
MONEY = re.compile(
    r"(?:[$€£]\s?\d|R\$\s?\d|\b(?i:USD|BRL|EUR|GBP)\s?\d|\b\d[\d.,]*\s?[kK]\b)"
)
TZ_ABBREVIATIONS = {"PST", "PDT", "EST", "EDT", "CST", "CDT", "MST",
                    "MDT", "CET", "CEST", "GMT", "BRT", "IST", "JST"}
TIMEZONE = re.compile(
    r"\b(?:UTC|GMT)\s?[+-]\s?\d{1,2}\b"
    r"|\b[A-Z][a-z]+/[A-Z][A-Za-z_]+\b"
    r"|\b(?:" + "|".join(TZ_ABBREVIATIONS) + r")\b"
)


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    check: str
    excerpt: str


def _scan(lines, ctx, name, pattern):
    out = []
    for line in lines:
        if line.in_lang:
            continue
        hit = pattern.search(line.prose)
        if hit:
            out.append(Finding(ctx.path, line.no, name, hit.group(0)))
    return out


def check_money(lines, ctx):
    return _scan(lines, ctx, "money", MONEY)


def check_timezone(lines, ctx):
    return _scan(lines, ctx, "timezone", TIMEZONE)
