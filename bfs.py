

def viable_neighbors(graph,current):
    moves={(1,0):"right",(-1,0):"left",(0,1):"up",(0,-1):"down"}
    viable_moves =dict()
    
    for x,y in moves.keys():
                    
        cordy=current[0]+y
        cordx =current[1]+x
        if -1 < cordy <len(graph) and -1 < cordx < len(graph[0]):    
            if graph[cordy][cordx]:
                viable_moves[(cordx,cordy)]=moves[(x,y)]
    return viable_moves

minemap = [[True, False],
    [True, True]]

current, final =  {'x':0,'y':0}, {'x':1,'y':0}

print(viable_neighbors(minemap,(current['x'],current['y'])))

def bfs(graph,miner,exit_):
    queue = [miner]
    
