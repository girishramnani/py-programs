__author__ = 'Girish'
import random
def shuffle(iterable):
    for i in range(len(iterable)-1):
        swap(iterable,i,iterable[random.randrange(i,len(iterable)-1)])

def swap(iterable,i,last):
    temp = iterable[i]
    iterable[i]=iterable[last]
    iterable[last] = temp

li=[1,2,3,4,5]
shuffle(li)
print(li)