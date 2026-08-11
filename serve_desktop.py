import http.server
import socketserver
import mimetypes

mimetypes.init()
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('text/html', '.html')

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

PORT = 8200
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    httpd.serve_forever()
