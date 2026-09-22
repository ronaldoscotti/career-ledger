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
