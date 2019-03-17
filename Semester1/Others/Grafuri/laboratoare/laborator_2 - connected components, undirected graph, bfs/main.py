from domain import Graph, connectedComponents

graph = Graph("input.txt")
print("The graph is: ")
graph.printGraph()
print("The connected components are: ")
ans = connectedComponents(graph)
