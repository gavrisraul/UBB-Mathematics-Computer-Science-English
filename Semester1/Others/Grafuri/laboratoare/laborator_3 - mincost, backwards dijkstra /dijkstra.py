import heapq

def getPath(prev, final):
    """
        In:
            - prev = the dictionary of parent nodes for each node of a graph
            - final = the final node of a path

        Description:
            - returns a list of vertices representign the shortest path from final to start

        Output:
            - a list of nodes
    """
    path = []
    if final not in prev:
        return None # the path could not be found
    while final != None:
        path.append(final)
        final = prev[final]
    return path

def dijkstra(graph, start, final, costs):
    """
        In:
            - graph = the graph on which we find the shortest path
            - start = the starting node of the path
            - final = the end point of the path
            - costs = the cost dictionary, having as keys pairs of vertices representing edges x->y

        Out:
            - a tuple containing:
                - path = a list of vertices representing the mincost path
                - pCost = the cost of the path
            - None if there is no path between the given vertices
    """
    dist = {}
    prev = {}
    prev[final] = None
    q = []
    dist[final] = 0
    heapq.heappush(q, (dist[final], final))
    while len(q) > 0:
        dummy, x = heapq.heappop(q)
        if(dummy == dist[x]):
            for y in graph.parseIn(x):
                if y not in prev or dist[y] > dist[x] + costs[(y, x)]:
                    prev[y] = x
                    dist[y] = dist[x] + costs[(y, x)]
                    heapq.heappush(q, (dist[y], y))
    if getPath(prev, start) is None:
        return None
    return (getPath(prev, start), dist[start])
