#Imports for good looks
import logging
import s
from colorama import init, Fore
from datetime import datetime
import sys
#Imports for port scans
import socket

#Start colorama and define some colors
init(autoreset=True)
GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN
GRAY = Fore.LIGHTBLACK_EX
  
#create and display banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

#VARS
TARGET = None
LEVEL = logging.DEBUG
open_ports = []

fmt = f"{RED}[%(levelname)s] %(asctime)s - %(message)s"

#setup logging
logging.basicConfig(level=LEVEL, format=fmt)

#Defining a TARGET
TARGET = ((input("[+] Enter a target to scan. Targets may be seperated by a comma -> ")).split(","))

def show_info(index):
    #Show basic info
    print("-" * 50)
    print("Scanning target: " + TARGET[index] + " | " + str(index+1) + "/" + str(len(TARGET)))
    print("Scanning started at: " + str(datetime.now()))
    print("-" * 50)
    scan(index)

def get_banner(sock):
    return sock.recv(1024)

def scan(i):
    index=i
    try: 
        # will scan ports between 1 to 65,535
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.00001)
            # returns an error indicator
            result = s.connect_ex((TARGET[index],port))
            if result ==0:
                try:
                    ban = get_banner(s)
                    print(f"{GREEN}{port:5} is open with {ban} banner")
                    open_ports.append((f"{GREEN}{port:5} is open with {ban} banner"))
                except:
                    print(f"{GREEN}{port:5} is open")
                    open_ports.append((f"{GREEN}{port:5} is open"))
            else:
                #print(f"{RED}{port:5} closed")
                pass
            s.close()
        
        print(f"{CYAN}Done scaning {TARGET[index]}") 
        if index < len(TARGET)-1:
                index+=1
                show_info(index)
        else:
            return

    except KeyboardInterrupt:
            logging.debug("Exiting Program")
            sys.exit()
    except socket.gaierror:
            logging.debug("Hostname Could Not Be Resolved")
            if index < len(TARGET)-1:
                index+=1
                show_info(index)
            else:
                return
    except socket.error:
            logging.debug("Server not responding")
            if index < len(TARGET)-1:
                index+=1
                show_info(index)
            else:
                return

show_info(0)
print(open_ports)
print("-"*50)
print(F"{CYAN}Done scanning all targets")
sys.exit()