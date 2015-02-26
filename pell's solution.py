__author__ = 'Girish'


test = 19

import math
from fractions import Fraction

sq = int(math.sqrt(19))

m0=0
m1=0
d0=1
d1=0
a0=int(math.sqrt(test))
an=0
a1=0
li=[]
Fraction x =
while a0 != 2*sq:
    m1=(d0*a0)-m0
    d1 = int((test - (m1**2) )/ d0)
    a1 = int((sq+m1)/d1)
    m0=m1
    d0=d1
    a0=a1
    li.append(a1)
print(li)

ans = 0

def recans(li,i=0):

    if i ==len(li)-1:
        return 1/li[i]
    return 1/(li[i]+recans(li,i+1))


