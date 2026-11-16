import socket

HOST = "127.0.0.1"
PORT = 5060

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall("hello socket".encode("utf-8"))
    reply = client.recv(1024)
    print(f"პასუხი: {reply.decode('utf-8')}")