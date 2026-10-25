#!/usr/bin/env python3
"""Run Ruang Informatika SMA locally using only Python's standard library."""
from __future__ import annotations
import argparse
import os
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent

class QuietHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt: str, *args) -> None:
        print(f"[{self.log_date_time_string()}] {fmt % args}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Jalankan Ruang Informatika SMA pada localhost.")
    parser.add_argument("--port", type=int, default=8000, help="Port server (default: 8000). Gunakan 0 untuk port otomatis.")
    args = parser.parse_args()
    try:
        server = ThreadingHTTPServer(("127.0.0.1", args.port), QuietHandler)
    except OSError as exc:
        if args.port != 0:
            print(f"Port {args.port} tidak tersedia ({exc}). Coba jalankan: python start_localhost.py --port 8001")
        raise SystemExit(1)
    host, port = server.server_address
    url = f"http://{host}:{port}/"
    print("=" * 64)
    print("RUANG INFORMATIKA SMA")
    print(f"Folder: {ROOT}")
    print(f"Alamat: {url}")
    print("Tekan Ctrl+C untuk menghentikan server.")
    print("=" * 64)
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer dihentikan.")
    finally:
        server.server_close()

if __name__ == "__main__":
    main()
