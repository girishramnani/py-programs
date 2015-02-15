__author__ = 'Girish'

def successor(x,y,X,Y):

    return [(0,y),(x,0),(X,y),(x,Y),(0,y+x) if (x+y)<=Y else ((x+y)-Y,Y),(y+x,0) if (y+x)<=X else (X,(x+y)-X)]


def pour_problem(X,Y,goal,start=(0,0)):

    if goal in start:
        return start

    stack = [[start]]
    explored = set()
    explored.add(start)
    while stack:
        t = stack.pop(0)
        (x,y)=  t[-1]
        for path in successor(x,y,X,Y): #path is a tuple
            if path not in explored:
                explored.add(path)
                path2 = t+[path]
                if goal in path:
                    return path2
                else:
                    stack.append(path2)

print(pour_problem(7,9,8))