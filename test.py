
import math
def proper_fact(num):
    yield 1
    
    for i in range(2,(math.ceil(num/2)+1)):
        if num%i==0:
            yield i


an2=0
for i in range(1,10000):
    ans = sum(proper_fact(i))
    ans2 =sum(proper_fact(ans))
    if ans2==i and ans !=ans2:
        an2+=i
        print(i)

print(an2)
    
    
    



    
