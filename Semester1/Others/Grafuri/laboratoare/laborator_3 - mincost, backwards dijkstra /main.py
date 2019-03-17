from domain import Graph
from dijkstra import *

graph = Graph("input.txt")
print("The graph is: ")
graph.printGraph()
x = int(input("Give vertex 1:"))
y = int(input("Give vertex 2: "))
if dijkstra(graph, x, y, graph.getCosts()) == None:
    print("There is no path between the two.")
else:
    print(dijkstra(graph, x, y, graph.getCosts()))