__author__ = 'girish'

import threading,os,time

def child(pipin):
    zz=4
    while True:
        zz+=1
        time.sleep(0.5)
        os.write(pipin,str(zz).encode())
        zz=zz%10
def parent(pipeout):
    while True:
        read = os.read(pipeout,32)
        print("got {} from the child".format(read))

pipin ,pipeout = os.pipe()
threading.Thread(target=child,args=(pipeout,)).start()
parent(pipin)