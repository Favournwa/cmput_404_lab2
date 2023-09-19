# Import socket module
import socket

HOST = "127.0.0.1"  # IPv4 reserves all addresses in the range 127.0.0.0 up to 127.255.255.255 for use in loopback testing
PORT = 8100  # any port number
BYTES_TO_READ = 4096
REQUEST = f'GET / HTTP/1.0\r\nHost: {HOST}\r\n\r\n'


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(REQUEST.encode())
        s.shutdown(socket.SHUT_WR)
        full_data = b""
        while True:
            data = s.recv(BYTES_TO_READ)
            if not data:
                break
            full_data += data
        print(full_data)


if __name__ == "__main__":
    main()
