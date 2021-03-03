import socket
import sys

HOST, PORT = "localhost", 4002

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))

    while True:
        data = input(">")
        sock.sendall(bytes(data + "\n", "utf-8"))
