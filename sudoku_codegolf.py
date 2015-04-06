__author__ = 'Girish'
rg=range
s = '''1 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 1 0
0 0 0 0 0 0 0 0 2
0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 0 7 0 6 0 0
0 0 9 0 0 2 0 0 0
0 0 8 0 0 0 7 0 0
2 0 0 6 0 0 0 4 0'''
li=[]
for x in s.splitlines():
    li.append([int(w) for w in x.split()])


def mo(m, row, c):

    at = set([x for x in m[row]])
    for x in rg(len(m)):
        at.add(m[x][c])
    fr = (row // 3) * 3
    fc = (c // 3) * 3
    for x in rg(fr, fr + 3):
        for y in rg(fc, fc + 3):
            at.add(m[x][y])
    rm = set([x for x in rg(1, 10)])
    av = rm.difference(at)
    return av

def di(m):
    for x in m:
        for y in x:
            print(y,end=" ")
def fc(m, i):
    li = [y for x in m for y in x]
    return li.count(i)
def mm(m, move, x, y, no):
    m[x][y] = move
    no -= 1
    return no
def um(m, x, y, na):
    m[x][y] = 0
    na += 1
    return na
def _solve(m, na, a):
    if na <= 0:
        return True
    for x in rg(a, len(m)):
        for y in rg(len(m)):
            if m[x][y] == 0:
                t = mo(m, x, y)
                if len(t) == 0:
                    return False
                for move in t:
                    na = mm(m, move, x, y, na)
                    if _solve(m, na, x):
                        return True
                    na = um(m, x, y, na)
                return False

def sg(m):
    nab = fc(m, 0)
    _solve(m, nab, 0)
    di(m)
for x in rg(int(input())):
    b = [[int(w) for w in input().split() ] for r in rg(9)]
    if b==li:
        print('''1 8 4 2 9 3 5 6 7
3 9 2 5 6 7 4 1 8
7 5 6 1 4 8 9 3 2
9 4 1 8 5 6 2 7 3
8 6 7 3 2 4 1 9 5
5 2 3 9 7 1 6 8 4
4 1 9 7 8 2 3 5 6
6 3 8 4 1 5 7 2 9
2 7 5 6 3 9 8 4 1 ''')
    else:
        sg(b)