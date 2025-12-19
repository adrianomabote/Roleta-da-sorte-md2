import http.server, os
os.chdir('/home/runner/workspace')
http.server.HTTPServer(('0.0.0.0', 5000), http.server.SimpleHTTPRequestHandler).serve_forever()
