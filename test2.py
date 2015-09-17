__author__ = 'Girish'

li = range(2,100001)

i=2
anslist = [2]

from time import time

t = time()
while True:
    li = filter(lambda a,t2 = i: a % t2 !=0 , li)
    try:
        i = next(li)
    except:
        break
    anslist.append(i)

ans = time() - t

print(len(anslist))
for i in range(int(input())):
    data = int(input())
    print(anslist[data-1])

