"""Checks a generated resume must pass before it is worth sending.

The three ATS rules are the ones decidable against the generated HTML alone.
The wider checklist lives in method/funnel/_refs/ats.md and arrives in phase 3.
"""
import re

TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9+#./-]*")
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "from",
    "have", "in", "is", "it", "need", "needs", "of", "on", "or", "our", "the",
    "this", "to", "we", "will", "with", "you", "your",
}


def count_em_dashes(text: str) -> int:
    """Counts em dashes only; hyphens and en dashes are not flagged."""
    return text.count("—")


def ats_failures(html: str) -> list[str]:
    """Names the ATS rules the HTML breaks, in a stable order."""
    failures = []
    if re.search(r"<table\b", html, re.I):
        failures.append("table")
    if re.search(r"<img\b", html, re.I):
        failures.append("image")
    if re.search(r"letter-spacing", html, re.I):
        failures.append("letter-spacing")
    return failures


def _keywords(posting: str) -> list[str]:
    seen = {}
    for raw in TOKEN.findall(posting):
        token = raw.strip("./-")
        if not token or token.lower() in STOPWORDS:
            continue
        technical = any(c.isdigit() or c in "+#/." for c in token[1:])
        if token[0].isupper() or technical:
            seen.setdefault(token.lower(), token)
    return list(seen)


def keyword_coverage(resume: str, posting: str) -> float:
    """Fraction of the posting's keywords present in the resume, case-insensitive.

    An empty keyword set scores 1.0: a posting with nothing to match cannot be missed.
    """
    keywords = _keywords(posting)
    if not keywords:
        return 1.0
    present = {t.strip("./-").lower() for t in TOKEN.findall(resume)}
    return sum(1 for k in keywords if k in present) / len(keywords)


def count_pages_from_pdf(path) -> int:
    """Reads /Count off the PDF page tree with a regex rather than a dependency."""
    data = open(path, "rb").read()
    counts = [int(m) for m in re.findall(rb"/Type\s*/Pages\b[^>]*?/Count\s+(\d+)", data)]
    if not counts:
        counts = [int(m) for m in re.findall(rb"/Count\s+(\d+)", data)]
    return max(counts) if counts else 0
