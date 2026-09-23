#!/usr/bin/env python3
"""Serve the funnel page and let it write applications.json back.

    python3 tools/serve.py

ponytail: stdlib http.server, no framework and no database. The JSON stays the
source of truth and stays diffable in git. If the funnel ever passes a few
hundred cards or needs concurrent access, that is when SQLite earns its place.
"""
import http.server
import json
import socketserver
import threading
import webbrowser
from pathlib import Path

import tracker

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "applications" / "applications.json"
PORT = 8777

# The page lives in tools/ and the data in applications/. The server root is the
# repository, so the paths in `files` open as links, and these two aliases put
# the page and the funnel at the top level where the page expects them.
ALIASES = {
    "/": "tools/funnel.html",
    "/funnel.html": "tools/funnel.html",
    "/applications.json": "applications/applications.json",
}


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(ROOT), **kw)

    def translate_path(self, path):
        alias = ALIASES.get(path.split("?", 1)[0])
        return str(ROOT / alias) if alias else super().translate_path(path)

    def do_PUT(self):
        if self.path != "/applications.json":
            return self.send_error(404)
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        try:
            data = self.parsed(body)
        except (ValueError, tracker.ValidationError) as e:
            return self.send_error(400, f"rejected: {e}")
        tmp = DATA.with_name(DATA.name + ".tmp")
        tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                       encoding="utf-8")
        tmp.replace(DATA)  # atomic: an interrupted write never truncates the funnel
        self.send_response(204)
        self.end_headers()

    @staticmethod
    def parsed(body: bytes) -> dict:
        """The same gate as the tracker, so the page cannot write a card it would reject."""
        data = json.loads(body)
        for key in ("applications", "triage"):
            if not isinstance(data.get(key), list):
                raise ValueError(f"{key} must be a list")
        for card in data["applications"]:
            tracker.validate_card(card)
        return data

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, *a):
        pass


class Server(socketserver.TCPServer):
    allow_reuse_address = True  # must be a class attribute: it is read before the bind


if __name__ == "__main__":
    url = f"http://localhost:{PORT}/funnel.html"
    try:
        server = Server(("127.0.0.1", PORT), Handler)
    except OSError:
        raise SystemExit(
            f"Port {PORT} is taken. Is a serve.py already running? Open {url}\n"
            f"Or kill the old one: lsof -ti tcp:{PORT} | xargs kill"
        )
    print(f"Funnel at {url}   (ctrl+c to stop)")
    threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    with server as s:
        try:
            s.serve_forever()
        except KeyboardInterrupt:
            print("\nbye")
