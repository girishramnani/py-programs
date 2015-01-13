__author__ = 'Girish'


from itertools import permutations
x= permutations(range(8))


for w in x:
    diag = set([])
    diag2 = set([])
    for w2 in range(8):
        diag.add(w[w2]+w2)
        diag2.add(w[w2]-w2)
    if len(diag)==len(diag2)==8:
        print(w)
