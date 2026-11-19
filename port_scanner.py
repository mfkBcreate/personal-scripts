#!/usr/bin/env python3
"""Simple TCP port scanner. Only scan machines you own or have permission to test."""

import socket
import sys

def scan_port(host, port, timeout=0.5):
    """Return True if the port accepts a TCP connection."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 port_scanner.py <host> <start_port> <end_port>")
        sys.exit(1)

    host = sys.argv[1]
    start, end = int(sys.argv[2]), int(sys.argv[3])

    print(f"Scanning {host} ports {start}-{end}...")
    open_ports = []
    for port in range(start, end + 1):
        if scan_port(host, port):
            print(f"  Port {port} is open")
            open_ports.append(port)

    print(f"Done. {len(open_ports)} open port(s) found.")

if __name__ == "__main__":
    main()
