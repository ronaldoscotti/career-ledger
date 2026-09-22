#!/usr/bin/env bash
# Usage: build.sh <application-dir> <markdown-basename> <output.pdf> [--posting <file>]
set -euo pipefail

CHROME="${CHROME:-}"
if [ -z "$CHROME" ]; then
  for candidate in \
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    "$(command -v google-chrome || true)" \
    "$(command -v chromium || true)"; do
    [ -x "$candidate" ] && CHROME="$candidate" && break
  done
fi
[ -x "$CHROME" ] || { echo "no Chrome found; set CHROME=/path/to/binary" >&2; exit 1; }

[ $# -ge 3 ] || { echo "usage: build.sh <dir> <basename> <out.pdf> [--posting <file>]" >&2; exit 2; }
dir="$1"; base="${2%.md}"; out="$3"; shift 3
posting=""
[ "${1:-}" = "--posting" ] && posting="$2"

here="$(cd "$(dirname "$0")" && pwd)"
dir="$(cd "$dir" && pwd)"
md="$dir/$base.md"
[ -f "$md" ] || { echo "no such markdown: $md" >&2; exit 1; }
case "$out" in /*) ;; *) out="$dir/$out" ;; esac

html="$(python3 "$here/md2resume.py" "$md")"
"$CHROME" --headless=new --print-to-pdf="$out" "$html" >/dev/null 2>&1

python3 - "$here" "$md" "$html" "$out" "$posting" <<'PYEOF'
import sys
from pathlib import Path

sys.path.insert(0, sys.argv[1])
from checks import ats_failures, count_em_dashes, count_pages_from_pdf, keyword_coverage

md, html, pdf, posting = (Path(p) if p else None for p in sys.argv[2:6])
text = md.read_text()
failures = ats_failures(html.read_text())
keywords = f"{round(keyword_coverage(text, posting.read_text()) * 100)}%" if posting else "n/a"
print(f"pages {count_pages_from_pdf(pdf)} · em-dashes {count_em_dashes(text)} · "
      f"ats {'ok' if not failures else ','.join(failures)} · keywords {keywords}")
PYEOF
