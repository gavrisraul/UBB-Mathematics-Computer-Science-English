from domain import Graph
from queue import Queue

def sorting(graph):
    sortedd = []
    count = {}
    q = Queue()
    for x in graph.parse():
        count[x] = graph.inDegree(x)
        if count[x] == 0:
            q.enqueue(x)
    while not q.isEmpty():
        x = q.dequeue()
        sortedd.append(x)
        for y in graph.parseOut(x):
            count[y] = count[y] - 1
            if count[y] == 0:
                q.enqueue(y)
    if len(sortedd) < graph.getNumber():
        sortedd = None
    return sortedd

def highestCost(graph, start, end):
    topological_sort = sorting(graph)
    costs = [0] * graph.getNumber()
    previous = [start]

    i = 0
    while i < len(topological_sort) and topological_sort[i] != start:
        i = i + 1

    while i < len(topological_sort) and topological_sort[i] != end:
        vertex = topological_sort[i]
        for destination in range(graph.getNumber()):
            if graph.isEdge(vertex, destination):
                new_cost = costs[vertex] + graph.getCost(vertex, destination)
                if new_cost > costs[destination]:
                    costs[destination] = new_cost
        i = i + 1

    for i in range(0,len(costs)):
        if costs[i] != 0:
            previous.append(i)

    print(previous)

    if i == len(topological_sort):
        return None
    return costs[end]