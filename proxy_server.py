import socket  # for socket
from threading import Thread

HOST = "127.0.0.1"  # or the IP address 142.251.33.68
PORT = 8100  # any port number
REQUEST = f'GET / HTTP/1.0\r\nHost: {HOST}\r\n\r\n'
BYTES_T0_READ = 4096


def send_request(host, port, request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(request.encode())
        client_socket.shutdown(socket.SHUT_WR)
        full_data = b""
        while True:
            data = client_socket.recv(BYTES_T0_READ)
            if not data:
                break
            full_data += data
        return full_data


def handle_connection(conn, addr):
    with conn:
        print("Connected by", addr)
        full_data = b""
        while True:
            data = conn.recv(BYTES_T0_READ)
            if not data:
                break
            full_data += data
        print(full_data)
        response = send_request("www.google.com", 8080, REQUEST)
        conn.sendall(response)


def main():
    # there is no need to call s.close() when using with statement.
    # The with statement itself ensures proper acquisition and release of resources.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2)
        while True:
            conn, addr = server_socket.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()


if __name__ == "__main__":
    main()
