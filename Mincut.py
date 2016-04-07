import random

__author__ = 'girish'
GRAPH = {0: [1, 3],
         1: [3, 2],
         2: [3,1],
         3: [0, 1,2]}


def createMergedEdgeAndClean(ed1, ed2, graph):
    """
    this method creates a list of non redundent edges with a list of the combined edge as a key and also removes the nodes from the graphs
    :type ed2: int
    """
    print("absorbing",ed2,"in",ed1)


    t = graph.pop(ed1)
    while ed2 in t:
        t.remove(ed2)
    t2 = graph.pop(ed2)
    while ed1 in t2:
        t2.remove(ed1)
    t.extend(t2)

    graph[ed1]=t
    for z in graph:
        if ed2 in graph[z]:
            graph[z].remove(ed2)
            graph[z].append(ed1)




    print(graph)



def mincut(graph):
    ans=set()
    t2 = set(graph.keys())

    while len(graph)>2:
        n = random.choice(list(graph.keys()))
        edge = random.choice(graph[n])
        createMergedEdgeAndClean(n,edge,graph)
        ans.add(n)

        ans.add(edge)

    print(ans)
    print(t2-ans)

mincut(GRAPH)