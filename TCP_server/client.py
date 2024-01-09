from pydoc import cli
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 444

client.connect((HOST,PORT))

print(f"Connected {HOST}:{PORT}".format(HOST,PORT))

msg = client.recv(1024)

print(msg.decode())

client.close()

