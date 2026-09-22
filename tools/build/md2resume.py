#!/usr/bin/env python3
"""Turns a resume markdown file into one ATS-safe HTML file next to it.

One column, real text, standard bullets, no tables and no images: a parser reads
this before a person does. The style block is inlined here so an output file is
never hand-edited.
"""
import html
import re
import sys
from pathlib import Path

STYLE = """
@page { size: Letter; margin: 0.5in 0.6in; }
body { font-family: Georgia, "Times New Roman", serif; font-size: 10.5pt;
       line-height: 1.34; color: #000; margin: 0; max-width: 7.3in; }
h1 { font-size: 16pt; margin: 0 0 2pt; font-weight: bold; }
h2 { font-size: 11pt; margin: 12pt 0 4pt; font-weight: bold;
     border-bottom: 1px solid #000; padding-bottom: 1pt; }
h3 { font-size: 10.5pt; margin: 8pt 0 2pt; font-weight: bold; }
p { margin: 0 0 5pt; }
ul { margin: 2pt 0 6pt; padding-left: 16pt; }
li { margin: 0 0 2pt; }
hr { border: 0; border-top: 1px solid #000; margin: 8pt 0; }
a { color: #000; text-decoration: none; }
"""

INLINE = [
    (re.compile(r"\[([^\]]+)\]\(([^)]+)\)"), r'<a href="\2">\1</a>'),
    (re.compile(r"\*\*(.+?)\*\*"), r"<strong>\1</strong>"),
    (re.compile(r"(?<![\w*])\*([^*]+)\*(?![\w*])"), r"<em>\1</em>"),
    (re.compile(r"`([^`]+)`"), r"\1"),
]


def _inline(text: str) -> str:
    out = html.escape(text, quote=False)
    for pattern, repl in INLINE:
        out = pattern.sub(repl, out)
    return out


# A comment is a note to the writer. Rendering one ships "cut the mentoring
# bullet" inside the document sent to the company, which is worse than useless.
COMMENT = re.compile(r"<!--.*?-->", re.S)


def render(markdown: str) -> str:
    """Renders the supported markdown subset to the body of the resume."""
    body, bullets, paragraph = [], [], []

    def flush():
        if bullets:
            body.append("<ul>" + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>")
            bullets.clear()
        if paragraph:
            body.append(f"<p>{' '.join(paragraph)}</p>")
            paragraph.clear()

    markdown = COMMENT.sub("", markdown)
    for line in markdown.splitlines():
        stripped = line.strip()
        heading = re.match(r"(#{1,3})\s+(.*)", stripped)
        bullet = re.match(r"[-*+]\s+(.*)", stripped)
        if not stripped:
            flush()
        elif heading:
            flush()
            level = len(heading.group(1))
            body.append(f"<h{level}>{_inline(heading.group(2))}</h{level}>")
        elif re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped):
            flush()
            body.append("<hr>")
        elif bullet:
            if paragraph:
                body.append(f"<p>{' '.join(paragraph)}</p>")
                paragraph.clear()
            bullets.append(_inline(bullet.group(1)))
        else:
            if bullets:
                flush()
            paragraph.append(_inline(stripped))
    flush()
    return "\n".join(body)


def convert(md_path: Path) -> Path:
    out = md_path.with_suffix(".html")
    title = html.escape(md_path.stem, quote=False)
    out.write_text(
        f"<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        f"<title>{title}</title>\n<style>{STYLE}</style>\n</head>\n<body>\n"
        f"{render(md_path.read_text())}\n</body>\n</html>\n",
        encoding="utf-8",
    )
    return out


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: md2resume.py <resume.md>")
    print(convert(Path(sys.argv[1])))
