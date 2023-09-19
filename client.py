#!/usr/bin/env python3
import socket

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("www.google.com", 8080))
        s.sendall(b"GET / HTTP/1.0\r\nHost:www.google.com\r\n\r\n")
        s.shutdown(socket.SHUT_WR)
        result = s.recv(4096)
        while(len(result)>0):
            print(result)
            result = s.recv(4096)
        #full_data = b""
        #while True:
        #    data = s.recv(4096)
        #    if not data:
        #        break
        #    full_data += data
        #print(full_data)


if __name__ == "__main__":
    main()
