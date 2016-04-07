__author__ = 'Girish'
import math

n,b,p = [int(x) for x in input().split()]

towels = p*n

current = n
bottles = 0
while current > 1:
    val = int(math.log2(current))
    bottles+=((2**val)*b)+(2**val//2)
    current = (2**val)//2 + (current - 2**val)

print(bottles,towels)

