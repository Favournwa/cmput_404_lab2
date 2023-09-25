#!/usr/bin/env python3
import socket


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("www.google.com", 80))
        s.sendall(b"GET / HTTP/1.0\r\nHost:www.google.com\r\n\r\n")
        s.shutdown(socket.SHUT_WR)
        response = b""
        while True:
            chunk = s.recv(4096)
            if len(chunk) == 0:
                break
            response = response + chunk
        print(response)


if __name__ == "__main__":
    main()
