
from socket import *

__author__ = 'Girish'
port = 50008
host = 'localhost'

def initListenerSocket(port=port):
    sock= socket(AF_INET,SOCK_STREAM)
    sock.bind(('',port))
    sock.listen(5)
    conn,addr  = sock.accept()
    return conn

def redirectOut(port=port, host = host):
    sock = socket(AF_INET,SOCK_STREAM)
    sock.connect((host,port))
    file = sock.makefile('w')
    sys.stdout = file
    return sock
def redirectIn(port = port, host= host):
    sock = socket()
    sock.connect((port,host))
    file = sock.makefile('r')
    sys.stdin = file
    return sock
def redirectBothAsClient(port=port, host = host):
    sock = socket.connect((host,port))
    inFile =sock.makefile()
    outfile = sock.makefile('w')
    return sock

