import argparse
import socket # for connecting
from colorama import init, Fore
from threading import Thread, Lock
from queue import Queue
import time

# some colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

# number of threads, feel free to tune this parameter as you wish
N_THREADS = 200
# thread queue
q = Queue()
print_lock = Lock()

host = "127.0.0.1"
port = 12345       

def port_scan(port):
    """
    Scan a port on the global variable `host`
    """
  
    try:
        s = socket.socket()
        s.connect((host, port))
        #s.send("abc123")
    except:
        #with print_lock:
            print(f"{GRAY}{host:15}:{port:5} is closed")#, end='\r')
    else:
       # with print_lock:
            print(f"{GREEN}{host:15}:{port:5} is open")
    finally:
        s.close()

for i in range(100):
    port_scan(80)
#for i in range(1,69420):
#    port_scan(i)
