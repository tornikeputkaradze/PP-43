import socket

HOST = "127.0.0.1"
PORT = 5060

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("სერვერი ელოდება კლიენტს...")

    conn, addr = server.accept()
    with conn:
        data = conn.recv(1024)
        text = data.decode("utf-8")
        print(f"მივიღეთ: {text}")
        conn.sendall(text.upper().encode("utf-8"))

print("სერვერი დასრულდა")