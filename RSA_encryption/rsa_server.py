import rsa
from rsa import key
from rsa.key import PublicKey

def generate_keys():
    (pubKey, privKey) = rsa.newkeys(1024)
    with open("G:\My Drive\Programing\Personal scripts\DataBase\RSA_encryption\pubKey.pem", "wb") as f:
        f.write(pubKey.save_pkcs1('PEM'))
    with open("G:\My Drive\Programing\Personal scripts\DataBase\RSA_encryption\privKey.pem", "wb") as f:
        f.write(privKey.save_pkcs1('PEM'))

def load_Keys():
    with open("G:\My Drive\Programing\Personal scripts\DataBase\RSA_encryption\pubKey.pem", "rb") as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())
    with open("G:\My Drive\Programing\Personal scripts\DataBase\RSA_encryption\privKey.pem", "rb") as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())
    
    return pubKey,privKey

def encrypt(msg, key):
    return rsa.encrypt(msg.encode('ascii'), key)

def deecrypt(msg, key):
    try:
        return rsa.decrypt(msg, key).decode('ascii')
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