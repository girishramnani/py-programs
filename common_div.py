from functools import reduce

__author__ = 'Girish'
import math
def gcd(a,b):
    while b:
        a%=b
        b^=a
        a ^=b
        b^=a
    return a

def no_div(n):
    sqr = int(math.sqrt(n))
    d = dict()
    i=2
    while n and i<=sqr:
        if n%i==0:
            d[i] = d.get(i,0)+1
            n//=i
        else:
            i+=1
    w=1
    for x,y in d.items():
        w*=(y+1)
    return 2 if w==1 else w


for x in range(int(input())):
    li = [int(x) for x in input().split()]
    print(no_div(gcd(*li)))

