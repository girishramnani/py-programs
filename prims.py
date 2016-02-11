__author__ = 'Girish'


x,y = [int(a) for a in input().split()]
grid = [[0 for _ in range(x+1)] for _ in range(x+1) ]




def find_min(grid,l,done):

    min = float("inf")
    min_point = 0
    for i in l:
        for j in range(1,len(grid)):
            if grid[i][j] != 0 and (i,j) not in done and grid[i][j] < min and j not in l:
                min_point= (i,j)
                min = grid[i][j]

    return min_point

def work(grid,x):
    su=0
    done = set([])
    l=set([x])
    spanning_tree = []
    while len(spanning_tree) != len(grid)-2:
            min_point = find_min(grid,l,done)
            su+=grid[min_point[0]][min_point[1]]
            spanning_tree.append(min_point)
            done.add((min_point[1],min_point[0]))
            done.add(min_point)
            l.add(min_point[1])
    return su







for j in range(y):
    x,y,w = [int(a) for a in input().split()]
    grid[x][y] = w
    grid[y][x] = w

print(work(grid,int(input())))

