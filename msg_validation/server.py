from math import prod
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 444
SEPARATOR = "<sep>"

def toBinary(binary):
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

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


server.bind((HOST,PORT))

print(f"listening on port {HOST}:{PORT}".format(HOST,PORT))
server.listen(3)

msg = "hi"
msg_binary = ''.join(format(ord(i), '08b') for i in msg)
#0110100001101(00)1 

msg_error = "ho"
msg_binary_error = ''.join(format(ord(i), '08b') for i in msg_error)
#0110100001101(11)1

mul_value = mul(int(msg_binary))
mul_div = mul_value%251
msg_to_send = str(msg_binary_error) + SEPARATOR + str(mul_div)#str(msg_binary) + SEPARATOR + str(mul_div)

print(f"Sending ascii: {msg} binary: {msg_binary} binary error: {msg_binary_error}")
print(f"Mul: {mul_value} Mul_div_rem {mul_div}")
print(f"Msg to send {msg_to_send}")

while True:
    client, addr = server.accept()

    print(f"Connection from {addr}".format(addr))

    client.send(msg_to_send.encode())

    client.close()