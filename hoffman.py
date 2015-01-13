__author__ = 'girish'
from heapq import heappush, heappop,heapify
def createDict(string):
    return dict((sy , string.count(sy)) for sy in set(string) )


def hoffman(symbols):
    """
    takes in a dictionary and returns a dictionary with hoffman code for each letter given/
    the pattern of the hoffman tree is [ num , [symbol , hofmancode'] ] so for a tree
                     2
                  /    \
                b(1)  c(1)
     the tree would look like [2 , ['b' , ['0']] , ['c' , ['1']]]

    :param symbols:
    :return:
    """
    heap = [[int(wt),[sym,[]]] for sym,wt in symbols.items()]
    heapify(heap)
    while len(heap)>1:
        item1 = heappop(heap)
        item2 = heappop(heap)
        for x in item1[1:]:
            x[1].insert(0,'0')
        for x in item2[1:]:
            x[1].insert(0,'1')

        heappush(heap,[item1[0]+item2[0]]+item1[1:]+item2[1:])
    li = heappop(heap)[1:]
    d = dict()
    for k in li:
        d[k[0]]="".join(k[1])
    return d


