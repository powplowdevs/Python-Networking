import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 444

server.bind((HOST,PORT))

print(f"listening on port {HOST}:{PORT}".format(HOST,PORT))
server.listen(3)

while True:
    client, addr = server.accept()

    print(f"Connection from {addr}".format(addr))

    msg = "hi"
    client.send(msg.encode())

    client.close()