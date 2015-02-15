__author__ = 'Girish'

def pour_problem(X,Y,goal,start=(0,0)):
    if goal in start:
        return [start]
    explored = set()

    frontier = [[start]]
    while frontier:
        path = frontier.pop(0)
        (x,y) = path[-1]
        for (state,action) in successor(x,y,X,Y).items():
            if state not in explored:
                explored.add(state)
                path2 = path+[action, state]
                if goal in state:
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail =[]





def successor(x,y,X,Y):
    return {(0,y):"Empty x",(x,0):"empty y",(X,y):"filling x",(x,Y):"filling y",
        (0,y+x) if (x+y)<=Y else ((x+y)-Y,Y):"x->y",(y+x,0) if (y+x)<=X else (X,(x+y)-X):"y->x" }



print(pour_problem(9,4,6))