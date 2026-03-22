import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")
    def log_message(self, format, *args):
        pass

PORT = int(os.environ.get("PORT", 8080))
threading.Thread(
    target=lambda: HTTPServer(("0.0.0.0", PORT), Handler).serve_forever(),
    daemon=True
).start()

from ub_core import BOT, LOGGER, Config, Convo, CustomDB, Message, bot
