from math import floor
import rsa
from rsa import key
from rsa.key import PublicKey
import random

Lock = ()
Key = ()

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def generate_keys():
    global Lock, Key   

    #MAKE OUR 2 STARTING PRIME NUMBERS
    pn1 = 2
    pn2 = 7

    #MULTIPLY 2 PRIME NUMBERS
    pnp = pn1*pn2

    #Figure out how many numbers under pnp that are factors of pn1 and pn2
    pupnp = (pn1-1)*(pn2-1)

    #FIND OUR LOCK
    #sub step one: make list of all numbers between 1 and pupnp:
    numbers_below = []
    for i in range(pupnp - 1):
        numbers_below.append(i+1)

    #sub step two: find numbers in numbers_below that are coprime to pnp and pupnp
    coprime_numbers = [] #list of numebrs that meet criteria
    for idx, num in enumerate(numbers_below):
        if is_coprime(num, pnp): #check to see if its coprime with pnp
            if is_coprime(num, pupnp): #check to see if its coprime with pupnp
                coprime_numbers.append(num) #if its coprime with both add it to the list


    #sub step three: pick a lock from the list coprime_numbers (NOTE: CANT BE ONE!)
    coprime_numbers.pop(0)#remove the one from the list as there will allways be a 1
    Lock = (random.choice(coprime_numbers), pnp)
    

    #FIND OUR KEY
    #our key will be D in the formula D*Lock(mod(pupnp)) = 1
    
    #substep one: make a list of x amount numbers that have are a factor of lock from a start point
    factors_of_lock = []
    startPoint = Lock[0]*random.randint(1,100) #CHANGE THIS TO BIGGER NUMBERS MABEY EVEN RANDOM(check to see if random ones are ok)

    for i in range(500):
        factors_of_lock.append(i + startPoint)

    #substep two: pick any number in the list factors_of_lock that have the pupnpth index
    index_pick = pupnp*random.randint(0,floor(len(factors_of_lock)/pupnp))
    Key = (factors_of_lock[index_pick], pnp)
    



    # with open("G:\My Drive\Programing\Personal scripts\DataBase\RSA_encryption\pubKey.pem", "wb") as f:
    #     f.write(pubKey.save_pkcs1('PEM'))
    # with open("G:\My Drive\Programing\Personal scripts\DataBase\RSA_encryption\privKey.pem", "wb") as f:
    #     f.write(privKey.save_pkcs1('PEM'))

def load_Keys():
    with open("G:\My Drive\Programing\Personal scripts\DataBase\RSA_encryption\pubKey.pem", "rb") as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())
    with open("G:\My Drive\Programing\Personal scripts\DataBase\RSA_encryption\privKey.pem", "rb") as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())
    
    return pubKey,privKey

def encrypt(msg, lock):
    encryptMsgList = [ord(msg) - 96 for letter in msg]
    encryptMsg = (encryptMsgList[0]**lock[0])%lock[1]

    return encryptMsg

def decrypt(msg, key):
    try:
        decryptMsg = (msg[0]**key[0])%key[1]

        return decryptMsg
    except:
        return False

def sign_sha1(msg, key):
    return rsa.sign(msg.encode('ascii'), key, "SHA-1")

def verify_sha1(msg, sign, key):
    try:
        return rsa.verify(msg.encode("ascii"), sign, key) == "SHA-1"
    except:
        return False


generate_keys()

print(encrypt("b",Lock))

enm = encrypt("b",Lock)

print(decrypt(enm, Key))

#print(Lock,Key)