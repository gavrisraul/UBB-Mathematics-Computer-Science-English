class Graph:
    def __init__(self, fileName):
        self.In = {}
        self.Out = {}
        self.Vertices = self.readVertices(fileName)
        self.Edges = self.readEdges(fileName)
        for i in range(0, self.Vertices):
            self.In[i] = []
            self.Out[i] = []
        self.readFromFile(fileName)

    @staticmethod
    def readVertices(fileName):
        f = open(fileName, "r")
        lines = f.read().split("\n")
        line = lines[0].split(" ")
        f.close()
        return int(line[0])

    def getVertices(self):
        return self.Vertices

    def getEdges(self):
        return self.Edges

    @staticmethod
    def readEdges(fileName):
        f = open(fileName, "r")
        lines = f.read().split("\n")
        line = lines[0].split(" ")
        f.close()
        return int(line[1])

    def readFromFile(self, fileName):
        f = open(fileName, "r")
        lines = f.readline().strip()
        lines = f.readline().strip()
        while lines != "":
            line = lines.split(" ")
            x = int(line[0])
            y = int(line[1])
            self.addEdge(x, y)
            self.addEdge(y, x)
            lines = f.readline().strip()

    def parse(self):
        return list(self.In.keys())

    def parseIn(self, x):
        if self.isVertex(x):
            return self.In[x]
        return False

    def parseOut(self, x):
        if self.isVertex(x):
            return self.Out[x]
        return False

    def addEdge(self, x, y):
        # x -> y, with the cost c
        if not self.isEdge(x, y):
            self.In[y].append(x)
            self.Out[x].append(y)
            return True
        return False

    def isEdge(self, x, y):
        # looks for edge x->y
        for i in self.Out[x]:
            if i == y:
                return True
        return False

    def isVertex(self, x):
        if x in self.parse():
            return True
        return False

    def printGraph(self):
        for i in self.parse():
            if len(self.In[i]) == len(self.Out[i]) == 0:
                print(i, "is an isolated vertex")
            else:
                print(i, ":", [j for j in self.Out[i]])


def connectedComponents(graph):
    visited = {}
    # we mark all vertices as not having been visited
    for i in range(0, graph.getVertices()):
        visited[i] = False

    for i in range(0, graph.getVertices()):
        if visited[i] == False:  # if the current vertex has not already been visited
            ans = bfs(graph, i)
            print(ans)
            for x in ans:
                visited[x] = True


def bfs(graph, start):
    explored = []  # keep track of all the visited nodes
    queue = [start]  # keep track of nodes to be checked
    visited = [start]
    while queue:  # keep looping until there are no more nodes to be checked
        node = queue.pop(0)
        explored.append(node)
        neighbours = graph.parseOut(node)

        # add neighbours of the node to queue
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
    return explored
