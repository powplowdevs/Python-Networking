from socket import *
import socket
BUFFER_SIZE = 1024 * 128
s = socket.socket()#(AF_INET, SOCK_STREAM)
s.connect(('192.168.1.178', 5040))
#s.listen(1)
while True:
    output = s.recv(BUFFER_SIZE).decode()
    # split command output and current directory
    results = output
    # print output
    print(results, "heyy")