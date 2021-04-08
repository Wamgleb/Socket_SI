import socket
import sys, time, threading
import os, subprocess
from tabulate import tabulate


print("""
 _______  _______  _______  _        _______ _________   _______ _________
(  ____ \(  ___  )(  ____ \| \    /\(  ____ \\__   __/  (  ____ \\__   __/
| (    \/| (   ) || (    \/|  \  / /| (    \/   ) (     | (    \/   ) (   
| (_____ | |   | || |      |  (_/ / | (__       | |     | (_____    | |   
(_____  )| |   | || |      |   _ (  |  __)      | |     (_____  )   | |   
      ) || |   | || |      |  ( \ \ | (         | |           ) |   | |   
/\____) || (___) || (____/\|  /  \ \| (____/\   | |     /\____) |___) (___
\_______)(_______)(_______/|_/    \/(_______/   )_(_____\_______)\_______/
                                                  (_____)                 \n\n""")

def the_process_function():
    n = 20
    for i in range(n):
        time.sleep(0.4)
        sys.stdout.write('\r'+'                 creating socket...    process '+str(i)+'/'+str(n)+' '+ '{:.2f}'.format(i/n*100)+'%')
        sys.stdout.flush()
    sys.stdout.write('\r'+'socket created               \n')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def animated_loading():
    chars = "/—\|" 
    for char in chars:
        sys.stdout.write('\r'+'loading... '+char)
        time.sleep(.1)
        sys.stdout.flush() 

the_process = threading.Thread(name='process', target=the_process_function)
the_process.start()

while the_process.is_alive():
    animated_loading()

time.sleep(2)
print("\n", "="*50, "\n")
print('Socket created.')
print("Connection with remout host ...\n")

target_host = "www.google.com"
target_port = 80
tab = [(target_host, target_port)]
colums = ["Target host", "Target Port"]

print(tabulate(tab, headers=colums))
print("="*50, "\n")
s.connect((target_host, target_port))
print("Connection OK")
print("="*50, "\n")

request = "GET / HTTP/1.1\r\nHost:{0}\r\n\r\n".format(target_host)
s.send(request.encode())

data = s.recv(4069)
print("\n", "Length", len(data))
print("="*50, "\n")
print("*"*30, "Closing the socket", "*"*30, "\n")

if not os.path.exists("data.txt"):
    try:
        f = open("data.txt", "w+")
        f.write(str(bytes(data)))
        f.close()
    except Exception as ex:
        print("Error:", str(ex))

s.close()

fileName = "data.txt"

def openFile():
    p = subprocess.Popen(["notepad.exe", fileName])
    p.wait()

openFile()



