__author__ = 'Girish'
from socket import *
myHost =''
myport = 50007
socketobj = socket(AF_INET,SOCK_STREAM)
socketobj.bind((myHost,myport))
socketobj.listen(5)

while True:
    connection , address = socketobj.accept()
    print(address)
    while True:
        ''' The recv blocks until one byte of data is received '''
        data = connection.recv(1024)

        if data =='':
            break
        connection.send(b'Ech=> '+data)
    connection.close()







