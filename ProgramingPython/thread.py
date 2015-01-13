__author__ = 'girish'

import threading as th
def fact(i):
    def t(i):
        if i==1:
            return i
        else:
            return i*t(i-1)
    print(t(i))
''' direct invocation of thread using lambda'''
th.Thread(target=lambda :fact(3)).start()
import time

class Th(th.Thread):
    def __init__(self,j):
        self.j = j
        super().__init__()
    def run(self):
        for i in range(1,self.j):
            fact(i)
            time.sleep(1)


# w = Th(5)
# w.start()
# w2 = Th(6)
# w2.start()
count=0
def add():
    global count
    count+=1
    time.sleep(0.5)
    count+=1
li = []
for i in range(100):
    th2 = th.Thread(target=lambda : add())
    th2.start()
    li.append(th2)

print("girihs")
import sys
try:
    sys.exit(1)
except SystemExit:
    print("exiting system")
    raise SystemExit
print("ullu")

