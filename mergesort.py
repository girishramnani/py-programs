__author__ = 'girish'

def mergesort(li):
    if len(li)<2:
        return li

    anslist=[]



    x=mergesort(li[:len(li)//2])
    y=mergesort(li[len(li)//2:])
    k=0
    j=0
    pointer=0

    while k<len(x) and j <len(y):
        if x[k]>y[j]:
            anslist.append(y[j])
            j+=1
        elif x[k]<=y[j]:
            anslist.append(x[k])
            k+=1
    anslist.extend(x[k:])
    anslist.extend(y[j:])
    return anslist

print(mergesort([5,4,3,2,1]))
