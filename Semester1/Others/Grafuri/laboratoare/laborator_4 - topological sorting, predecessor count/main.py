from topological_sorting import *

g = Graph("input.txt")
g.printGraph()
topologically_sorted = sorting(g)
if topologically_sorted == None:
    print("The graph has a cycle and thus is not a DAG.")
else:
    print("The graph is a DAG, and its topological sorting is:", topologically_sorted)
    x = int(input("Give x: "))
    y = int(input("Give y: "))
    if(highestCost(g,x,y) == None):
        print("There is no path between the given vertices!")
    else:
        print("The highest cost path between",x,"and",y,"is: ",highestCost(g, x, y))

