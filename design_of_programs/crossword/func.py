__author__ = 'Girish'


import time

def timer(f):
    def function(*args):
        t = time.time()
        ans = f(*args)
        an=time.time()-t
        print(an)
        return ans
    return function

