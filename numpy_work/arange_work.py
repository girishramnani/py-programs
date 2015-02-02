__author__ = 'Girish'
import numpy as np

def vec(n):
    import time
    t = time.time()
    a = np.arange(n**2)
    b= np.arange(n**2)
    c = a+b
    print(c)
    return time.time() -t

def vec2(n):
    import time
    t= time.time()
    a = range(n**2)
    b=range(n**2)
    c=[]
    for i in range(n**2):

        c.append(a[i]+b[i])

    return time.time()-t
print(range(5,7,0.1))
def vec3(n):
    import time
    t= time.time()
    a = range(n**2)
    b=range(n**2)
    c=[a[i]+b[i] for i in range(n**2)]
    return time.time()-t
print(vec(1000))
print(vec2(1000))
print(vec3(1000))
