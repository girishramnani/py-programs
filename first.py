__author__ = 'girish'
import threading




class athread(threading.Thread):
    def __init__(self, num , val):
        threading.Thread.__init__(self)
        self.threadnum = num
        self.loop = val
    def run(self):
        print("Starting run:",self.threadnum)
        myfunc(self.threadnum,self.loop)

def myfunc(threadnum, loop):
    count =0
    for i in range(loop):
        print(threadnum ,":",i)

t1= athread(23,34)
t2= athread(345,677)
t1.start()
t2.start()
t1.join()
t2.join()


