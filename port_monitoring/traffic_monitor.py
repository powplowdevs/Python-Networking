from socket import *
import socket

s = socket.socket()#(AF_INET, SOCK_STREAM)
s.bind(('0.0.0.0', 5040))
s.listen(1)
while True:
    print(s.accept()[1])
