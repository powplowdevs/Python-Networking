from socket import *
import socket
import sys

SERVER_HOST = "192.168.1.178"
SERVER_PORT = 5040
BUFFER_SIZE = 1024 * 128

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))


#MAIN LOOP
while True:
    # get the command from prompt
    command = input("$> ")
    if not command.strip():
        # empty command
        print("emty com")
        continue
    # send the command to the client
    s.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    output = s.recv(BUFFER_SIZE).decode()
    # split command output and current directory
    results = output
    # print output
    print(results)

