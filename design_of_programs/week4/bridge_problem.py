__author__ = 'Girish'

import itertools
def time_taken(f,s,t,ff):
    time =0
    t1= max(f,s)
    time+=t1
    t2= min(f,s)
    time+=t2
    time+=max(t,t2)
    t3= min(t,t2)
    time+=t3
    t4 = max(ff,t3)
    time+=t4
    return time

def bridge_problem(li):
    total = itertools.permutations(li)
    times = []
    for (f,s,t,ff) in total:
        times.append(time_taken(f,s,t,ff))
    return min(times)


print(bridge_problem([1,2,5,10]))
