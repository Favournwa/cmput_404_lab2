#!/usr/bin/env python3
import socket
from threading import Thread

# define address & buffer size
HOST = ""
PORT = 8001
BYTES_TO_READ = 4096


def handle_connection(conn, addr):
    with conn:
        print("Connected by", addr)
        full_data = b""
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            full_data += data
        print(full_data)
        conn.sendall(full_data)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # bind socket to address
        s.bind((HOST, PORT))
        # QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # set to listening mode
        s.listen(2)

        # continuously listen for connections
        while True:
            conn, addr = s.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()


if __name__ == "__main__":
    main()
