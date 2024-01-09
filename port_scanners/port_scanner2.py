import pyfiglet
import sys
import socket
from datetime import datetime
from colorama import init, Fore

# some colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX
  
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
  
# Defining a target
if len(sys.argv) == 2:
     
    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")
 
target = socket.gethostbyname("127.0.0.1")
# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)
  
try:
     
    # will scan ports between 1 to 65,535
    for port in range(134,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.00001)
         
        # returns an error indicator
        result = s.connect_ex((target,port))
        if result ==0:
            print(f"{GREEN}{port:5} is open")
            #print("Port {} is open".format(port))
        #else:
            #print("Port {} is closed".format(port))
        s.close()
         
except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()