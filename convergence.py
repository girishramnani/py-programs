__author__ = 'Girish'

__author__ = 'Girish'

import math

def fractionalcoll(num,n):
    li=[int(num)]
    x=1
    while len(li) <n:
        if (len(li)+1)%3==0 :
            li.append(2*int(x))
            x+=1
        else:
            li.append(1)
    numerator=1
    denominator=li[-1]
    for i in range(len(li)-2,-1,-1):
        numerator+=denominator*li[i]
        numerator,denominator = denominator,numerator
        #y              #x
    return denominator

t = int(input())
ans = fractionalcoll(math.e,t)
p =0
while ans>0:
    temp =ans%10
    ans//=10
    p+=temp
print(p)


