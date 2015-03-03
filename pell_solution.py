__author__ = 'Girish'


test = 19

import math
from fractions import Fraction


def pell_coefficient(num):

    sq = int(math.sqrt(num))
    if num ==sq**2:
        return -1
    m0=0
    m1=0
    d0=1
    d1=0
    a0=int(sq)
    a1=0
    li=[]
    li.append(sq)
    while a0!=2*sq:

        m1=(d0*a0)-m0
        d1 = int((num - (m1**2) )/ d0)
        a1 = int((sq+m1)/d1)
        m0=m1
        d0=d1
        a0=a1
        li.append(a1)
    if li[1]!=(li[0]<<1):
        li.pop()
    return li


def recoll(li,i=0):
    if i ==len(li)-1:
        return 1/li[i]
    return 1/(li[i]+recoll(li,i+1))


def fractionalcoll(num):
    sq = int(math.sqrt(num))
    if num ==sq**2:
        return -1
    m0=0
    m1=0
    d0=1
    d1=0
    a0=int(sq)
    a1=0
    li=[]
    li.append(sq)
    while a0!=2*sq:
        m1=(d0*a0)-m0
        d1 = int((num - (m1**2) )/ d0)
        a1 = int((sq+m1)/d1)
        m0=m1
        d0=d1
        a0=a1
        li.append(a1)
    if li[1]!=(li[0]<<1):
        li.pop()
    numerator=1
    denominator=li[-1]
    for i in range(len(li)-2,-1,-1):
        numerator+=denominator*li[i]
        numerator,denominator = denominator,numerator
        #y              #x
    return denominator


print(fractionalcoll(math.pi))
