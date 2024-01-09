from logging import NullHandler
from pydoc import cli
import socket

HOST = socket.gethostname()
PORT = 444
ENCODE = "utf-8"
transmissionStaus = False
file = NullHandler

def main():
    global transmissionStaus, file

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((HOST,PORT))

    print(f"Connected {HOST}:{PORT}".format(HOST,PORT))

    msg = client.recv(1024)

    #TXT FILES
    if "TXT" in msg.decode():
        print(f"FILE {msg.decode()}")

        client.send("SIZE RES".encode(ENCODE))
        print(msg.decode().split("SIZE")[1])
        msg = client.recv(int(msg.decode().split("SIZE")[1]))

        if msg.decode() != "END-OF-FILE":
            if not transmissionStaus:
                file = open(input("A new transmission has been sent by the server! What shall we name it? $>"), "w")
                transmissionStaus = True
            if transmissionStaus == True:
                file.write(msg.decode(ENCODE))
        else:
            print("TRASMISSON COMPLTE")
            transmissionStaus = False
            file.close()

        client.close()

    #PNG FILES
    if "SIZE" in msg.decode():
        print(f"FILE {msg.decode()}")

        client.send("SIZE RES".encode(ENCODE))

        msg = client.recv(int(msg.decode().split("SIZE")[1]))
        
        #if msg.decode() != "END-OF-FILE":
        if not transmissionStaus:
            file = open(input("A new transmission has been sent by the server! What shall we name it? $>"), "wb")
            transmissionStaus = True
        if transmissionStaus == True:
            file.write(msg)
        else:
            print("TRASMISSON COMPLTE")
            transmissionStaus = False
            file.close()

    client.close()



if __name__ == "__main__":
    main()