__author__ = 'girish'

Graph = {'A': ['B', 'C'],
         'B': ['A']}

from collections import deque

def BFS(graph, start, end):
    q=deque()
    temp_path = [start]

    q.appendleft(temp_path)
    no = 0
    while q:
        tmp_path = q.popleft()
        last_node = tmp_path[len(tmp_path) - 1]

        if last_node == end:
            no += 1
        for link_node in graph[last_node]:
            if link_node not in tmp_path:
                # new_path = []
                new_path = tmp_path + [link_node]
                q.appendleft(new_path)
    return no

t = int(input())
v = int(input())



def GenerateGraph(inputtaken, v):
    li = dict()
    for k in range(v):
        if inputtaken[k][v - 1] == '.':
            li[(k * v) + (v - 1)] = []

        for w in range(v):
            if inputtaken[k][w] == '.':
                li[(k * v) + w] = []
                if k + 1 < v:
                    if inputtaken[k + 1][w] == '.':
                        li[(k * v) + w].append(((k + 1) * v) + w)
                if w + 1 < v:
                    if inputtaken[k][w + 1] == '.':
                        li[(k * v) + w].append((k * v) + w + 1)

    return li







