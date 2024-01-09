from pydoc import cli
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 444
SEPARATOR = "<sep>"

client.connect((HOST,PORT))

def mul(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1

    #ISSUE HERE
    product = str(decimal)[0]
    #print(f"prod: {product} deci: {decimal}")
    #print(f"we are gonna loop {len(str(decimal))-1} times")
    for i in range(len(str(decimal))-1):
        #print(f"{product} times {(int(str(decimal)[i+1]))}")
        product = int(product)*(int(str(decimal)[i+1]))
        
    #ISSUE HERE

    return product

print(f"Connected {HOST}:{PORT}".format(HOST,PORT))

msg = client.recv(1024).decode()
msg = msg.split(SEPARATOR)
rem = msg[1]
msg = msg[0]
res_rem = mul(int(msg))%251


print(f"Msg {msg} Rem {rem}")
print(f"Res_msg_rem {res_rem}")

if res_rem != rem:
    print("An error in the msg has been found")

client.close()

