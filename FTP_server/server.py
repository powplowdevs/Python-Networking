import socket
#import client as sock_client

HOST = socket.gethostname()
PORT = 444
ENCODE = "utf-8"

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST,PORT))

    print(f"listening on port {HOST}:{PORT}".format(HOST,PORT))
    server.listen(3)

    #sock_client.main()

    while True:
        client, addr = server.accept()

        print(f"Connection from {addr}".format(addr))

        path = input(":PATH TO FILE:$>")
        
        if path[len(path)-3:] == "txt":
            
            with open(path, 'rb') as f:
                bytes = f.read()
                size = len(bytes)
            f.close()
            
            client.send(f"TXT SIZE {size}".encode())
            ans = client.recv(1024)
            
            if ans.decode() == "SIZE RES":
                with open(path) as file:
                    for line in file:
                        client.send(line.encode(ENCODE))
                client.send("END-OF-FILE".encode(ENCODE))

        elif path[len(path)-3:] == "png":
            with open(path, 'rb') as f:
                bytes = f.read()
                size = len(bytes)

            client.send(f"SIZE {size}".encode())
            ans = client.recv(1024)
            
            if ans.decode() == "SIZE RES":
                client.sendall(bytes)
            client.send("END-OF-FILE".encode())

        client.close()

if __name__ == "__main__":
    main()