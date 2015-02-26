

t = int(input())

for i in range(t):
    input()
    ladders = [ [int(x) for x in i.split(",")] for i in input().split()]
    lad = dict(ladders)
    input()

    path = [[1]]

    visited = [False] *101
    flag =True
    while path and flag:
        first = path[0]
        if visited[first[-1]]:
            path.pop(0)
        else:
            visited[first[-1]] = True
            for j in range(1,7):
                temp = first[-1]+j
                while temp in lad:
                    temp =lad[temp]
                path.append(first+[temp])

                if temp ==100 :
                    print(len(path[0]))
                    flag=False
                    break
            path.pop(0)


