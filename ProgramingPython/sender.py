from time import sleep

__author__ = 'Girish'
from socket import *


myAddress = "localhost"
myPort = 50007
sock = socket(AF_INET,SOCK_STREAM)
sock.connect((myAddress,myPort))
while True:
    sock.send(b"hey")
    t = sock.recv(1024)
    sleep(1)
    print(t.decode())
