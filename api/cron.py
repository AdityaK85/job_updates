import os
import sys
import subprocess
from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
     

        result = subprocess.run(
            [sys.executable, "index.py"],
            capture_output=True,
            text=True,
            timeout=50,
        )

        print(result.stdout)
        print(result.stderr)

        self.send_response(200 if result.returncode == 0 else 500)
        self.end_headers()
        self.wfile.write(
            b"Success" if result.returncode == 0 else b"Failed"
        )