class Graph:
    def __init__(self, fileName):
        self.In = {}
        self.Out = {}
        self.Cost = {}
        self.Vertices = self.readVertices(fileName)
        for i in range(0, self.Vertices):
            self.In[i] = []
            self.Out[i] = []
        self.readFromFile(fileName)

    @staticmethod
    def readVertices(fileName):
        f = open(fileName, "r")
        lines = f.read().split("\n")
        return int(lines[0][0])

    def readFromFile(self, fileName):
        f = open(fileName, "r")
        lines = f.readline().strip()
        lines = f.readline().strip()
        while lines != "":
            line = lines.split(" ")
            x = int(line[0])
            y = int(line[1])
            c = int(line[2])
            self.addEdge(x, y, c)
            lines = f.readline().strip()

    def getNumber(self):
        return len(self.In.keys())

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

    def addEdge(self, x, y, c):
        # x -> y, with the cost c
        if not self.isEdge(x, y):
            self.In[y].append(x)
            self.Out[x].append(y)
            self.Cost[(x, y)] = c
            return True
        return False

    def isEdge(self, x, y):
        # looks for edge x->y
        for i in self.Out[x]:
            if i == y:
                return True
        return False

    def removeEdge(self, x, y):
        if self.isEdge(x, y):
            self.In[y].remove(x)
            self.Out[x].remove(y)
            del self.Cost[(x, y)]
            return True
        return False

    def addVertex(self, x):
        if not self.isVertex(x):
            self.In[x] = []
            self.Out[x] = []
            return True
        return False

    def isVertex(self, x):
        if x in self.parse():
            return True
        return False

    def removeVertex(self, x):
        if self.isVertex(x):
            for i in self.parseIn(x):
                self.removeEdge(i, x)
            for i in self.parseOut(x):
                self.removeEdge(x, i)
            del self.In[x]
            del self.Out[x]
            return True
        return False

    def getCost(self, x, y):
        if self.isEdge(x, y):
            return self.Cost[(x, y)]
        return False

    def setCost(self, x, y, new_cost):
        if self.isEdge(x, y):
            self.Cost[(x, y)] = new_cost
            return True
        return False

    def printGraph(self):
        for i in self.parse():
            if len(self.In[i]) == len(self.Out[i]) == 0:
                print(i, "is an isolated vertex")
            else:
                for j in self.Out[i]:
                    print(i, "->", j, "having the cost:", self.Cost[(i, j)])
