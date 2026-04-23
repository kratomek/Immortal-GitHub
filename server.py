from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 5500


class ImmortalRequestHandler(SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()


def main() -> None:
    TCPServer.allow_reuse_address = True
    with TCPServer(("", PORT), ImmortalRequestHandler) as httpd:
        print(f"Immortal: http://127.0.0.1:{PORT}/  (Ctrl+C to stop)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    main()
