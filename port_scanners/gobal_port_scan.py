#Imports for good looks
import logging
import pyfiglet
from colorama import init, Fore
from datetime import datetime
import sys
#Imports for port scans
import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "72.83.137.233"
        self.port = 4983
        self.addr = (self.server, self.port)

    def connect(self):
        try:
            self.client.connect(self.addr)
            print("Pass")
            print(self.client.recv(2048).decode())
        except:
            print("Fail")

network = Network()
network.connect()