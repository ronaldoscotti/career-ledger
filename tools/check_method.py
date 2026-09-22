#!/usr/bin/env python3
"""The portability gate: keeps candidate data and agent vocabulary out of method/.

Exists because the system this was extracted from copied the same compensation
figure into seven files, and two of them were a month stale before anyone noticed.
Prose does not validate. This does.
"""
import fnmatch
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


def check_denylist(lines, ctx):
    if not ctx.denylist:
        return []
    pattern = re.compile(r"\b(?:" + "|".join(
        re.escape(w) for w in sorted(ctx.denylist)) + r")\b")
    out = []
    for line in lines:
        # No exemptions at all. A denylisted name in a code fence, in a code span
        # or inside a pt-BR sample is still that name.
        hit = pattern.search(line.raw)
        if hit:
            out.append(Finding(ctx.path, line.no, "denylist", hit.group(0)))
    return out


WORD = re.compile(r"\b[A-Za-z][A-Za-z'’-]*\b")
SENTENCE_END = re.compile(r"[.!?:]['\"”’)]?\s*$")
# Markdown furniture that starts a line and must not count as sentence-initial context.
LEADER = re.compile(r"^\s*(?:[-*+]|\d+\.|>|\|)?\s*")


def check_proper_nouns(lines, ctx):
    out = []
    for line in lines:
        if line.in_fence or line.is_heading or line.in_lang:
            continue
        text = line.prose
        start = LEADER.match(text).end()
        for m in WORD.finditer(text, start):
            word = m.group(0)
            if not word[0].isupper():
                continue
            if word in ctx.allowlist or word == "I":
                continue
            # Hyphens do not count toward acronym length, or the method's own
            # ZERO-A, ZERO-B and ZERO-C would trip the check that guards them.
            bare = word.replace("-", "").replace("’", "").replace("'", "")
            if bare.isupper() and len(bare) <= 5:
                continue
            before = text[start:m.start()]
            if not before.strip() or SENTENCE_END.search(before):
                continue  # sentence-initial: the accepted miss
            out.append(Finding(ctx.path, line.no, "proper-noun", word))
    return out


# Inline, not a file: this list is the method's own vocabulary discipline, not
# something a person adopting the repo is expected to tune.
AGENT_TOOLING = re.compile(
    r"\b(?:Task|Skill|Bash|Read|Write|Edit|Glob|Grep|WebFetch|WebSearch)\s+tool\b"
    r"|\bTodoWrite\b|\bslash command\b|\bsubagent_type\b"
    r"|\.claude/|\bCLAUDE\.md\b",
    re.IGNORECASE,
)


def check_agent_tooling(lines, ctx):
    return _scan(lines, ctx, "agent-tooling", AGENT_TOOLING)


# Portuguese-only diacritics. Acute accents are excluded on purpose: résumé and
# café are English enough to appear in this method, and ã õ ç are not.
PT_DIACRITIC = re.compile(r"[ãõÃÕçÇ]")
# High-frequency Portuguese function words with no English collision.
PT_WORDS = {
    "que", "nao", "não", "para", "com", "uma", "dos", "das", "são", "sao",
    "você", "voce", "pelo", "pela", "isso", "mais", "seu", "sua", "quando",
    "onde", "porque", "depois", "antes", "sempre", "nunca", "aqui", "ali",
    "ele", "ela", "eles", "elas", "nós", "nos", "esta", "está", "esse",
    "essa", "aquele", "cada", "todo", "toda", "muito", "pouco", "entre",
}


def check_language(lines, ctx):
    out = []
    for line in lines:
        if line.in_lang or line.in_fence:
            continue
        if PT_DIACRITIC.search(line.prose):
            out.append(Finding(ctx.path, line.no, "language", line.prose.strip()[:60]))
            continue
        words = {w.lower() for w in WORD.findall(line.prose)}
        hits = words & PT_WORDS
        if len(hits) >= 2:
            out.append(Finding(ctx.path, line.no, "language", " ".join(sorted(hits))))
    return out


# A code span is treated as a path when it carries a slash or ends in a known
# extension. `status` is not a path; `tracker.py` is, and is meant to fail.
PATHISH = re.compile(r"^[\w./-]+(?:/[\w./-]+|\.(?:md|py|json|sh|txt|html|pdf))$")


def check_paths(lines, ctx):
    out = []
    for line in lines:
        if line.in_lang:
            continue
        for span in CODE_SPAN.findall(line.raw):
            candidate = span.strip("`").strip()
            if not PATHISH.match(candidate):
                continue
            if any(fnmatch.fnmatch(candidate, glob) or
                   fnmatch.fnmatch(candidate, glob.replace("/**", "/*"))
                   for glob in ctx.contract_paths):
                continue
            if (ctx.root / candidate).exists():
                continue
            out.append(Finding(ctx.path, line.no, "path", candidate))
    return out


import argparse
import sys
from pathlib import Path

CHECKS = (check_money, check_timezone, check_denylist, check_proper_nouns,
          check_agent_tooling, check_language, check_paths)


class Context:
    def __init__(self, root: Path):
        self.root = root
        self.allowlist = _words(root / "tools" / "allowlist.txt")
        self.denylist = _words(root / "tools" / "denylist.txt")
        self.contract_paths = sorted(_words(root / "tools" / "contract-paths.txt"))
        self.path = ""


def _words(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {line.strip() for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")}


def run(root: Path) -> list[Finding]:
    ctx = Context(root)
    findings = []
    for md in sorted((root / "method").rglob("*.md")):
        ctx.path = str(md.relative_to(root))
        lines = parse_lines(md.read_text(encoding="utf-8"))
        for check in CHECKS:
            findings.extend(check(lines, ctx))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", type=Path)
    args = parser.parse_args()
    findings = run(args.root.resolve())
    for f in sorted(findings, key=lambda f: (f.path, f.line)):
        print(f"{f.path}:{f.line}: {f.check}: {f.excerpt}")
    print(f"\n{len(findings)} finding(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
