import http.server
import os

os.chdir('/home/runner/workspace')

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

http.server.HTTPServer(('0.0.0.0', 5000), Handler).serve_forever()
