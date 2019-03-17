import copy
import operator

class Vertex:

    def __init__(self, number):
        '''
        param number
        creates a list of inbound vertexes and one of outbound vertexes, as well as iterators for each one
        '''
        self.number = number
        self.edges = []
        self.iterator = Iterator()
        self.colors = []
        self.is_colored = 0

    def __str__(self):
        return str(self.number)

    def get_number(self):
        return self.number

    def delete_edge(self, v):
        if v in self.edges:
            self.edges.remove(v)

    def plus_edge(self, v):
        if v not in self.edges:
            self.edges.append(v)

    def remove_color(self, c):
        self.colors.remove(c)

    def add_color(self, c):
        self.colors.append(c)


class Iterator:
    """
    generic iterator which holds the current position and the maximum position
    """
    def __init__(self):
        self.n = 0
        self.i = 0

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration

class UndirectedGraph:

    def __init__(self):
        '''
        initializer for the directed graph
        the list of vertices is a normal list
        the list of edges is a dictionary with the key a tuple consisting of the vertexes and the value its cost
        '''
        self.__number_of_vertices = 0
        self.__number_of_edges = 0
        self.__list_vertices = []
        self.__list_edges = []

    def read_from_file(self, filename):
        '''
        param filename:
        function which reads a graph from a text file and modifies the internal representation
        '''
        with open(filename, "r") as f:
            lines = f.readlines()
            # the first consists of the numbers of vertices and edges
            line = lines[0]
            line = line.split()
            self.__number_of_vertices = int(line[0])
            self.__number_of_edges = int(line[1])
            lines.pop(0)

            #create the vertices
            for i in range(self.__number_of_vertices):
                v = Vertex(i)
                self.__list_vertices.append(v)
                for j in range(self.__number_of_vertices):
                    v.add_color(j)
                v.remove_color(0)
                v.add_color(self.__number_of_vertices)

            for line in lines:
                line = line.split()
                #get the edges
                v1 = int(line[0])
                v2 = int(line[1])
                #record them for the vertices such that we can iterate through the neighbours
                self.__list_vertices[v1].edges.append(self.__list_vertices[v2])
                self.__list_vertices[v2].edges.append(self.__list_vertices[v1])
                tpl = (v1,v2)
                #add the edge to the list
                self.__list_edges.append(tpl)

            #set the maximum length for iterators
            for i in self.__list_vertices:
                i.iterator.n = len(i.edges)

        f.close()


    def eliminate_edge(self, v1, v2):
        if (v1,v2) in self.__list_edges:
            self.__list_edges.remove((v1,v2))

    def eliminate_vertex(self, v):

        t = Vertex(-1)
        ok = False
        for i in self.__list_vertices:
            if i.get_number() == v:
                t = i
                ok = True
                break

        if ok == False:
            return False

        for i in self.__list_vertices:
            self.eliminate_edge(v, i.get_number())
            self.eliminate_edge(i.get_number(), v)

        for i in self.__list_vertices:
            i.delete_edge(t)

        self.__list_vertices.remove(t)

        self.__number_of_vertices -= 1

        return t

    def add_edge(self, v1, v2):
        self.__list_edges.append((v1,v2))

    def add_vertex(self, v):

        for i in v.edges:
            self.add_edge(i.get_number(), v.get_number())

        for i in self.__list_vertices:
            if i in v.edges:
                i.plus_edge(v)

        self.__number_of_vertices += 1

        self.__list_vertices.append(v)

    def get_vertex(self, v):
        return self.__list_vertices[v]

    def print_vertices(self):
        for i in self.__list_vertices:
            print(i.number, "edges:")
            for j in i.edges:
                print(j.number)
            print(i.colors)
            print("\n")

    def print_edges(self):
        print(self.__list_edges)

    def get_nr_of_vertices(self):
        return self.__number_of_vertices

    def get_nr_of_edges(self):
        return self.__number_of_edges

    def verify_edge(self, v1, v2):
        return (v1,v2) in self.__list_edges

    def get_degree(self, v):
        return len(self.__list_vertices[v].edges)

    def get_vertices(self):
        return self.__list_vertices

    def get_edges(self):
        return self.__list_edges

G = UndirectedGraph()
G.read_from_file("UndirectedGraph3.txt")

def GCP(g, k, ub):

    #print(k, ub, g.get_nr_of_vertices())

    if g.get_nr_of_vertices() == 0:
        return k

    vertices = g.get_vertices()

    #for i in vertices:
    #   print(i, ",", i.colors)

    for i in vertices:
        ok = 1
        for j in i.colors:
            if j < ub:
                ok = 0
        if ok == 1:
            return ub

    # order_of_vertices = []
    # for i in vertices:
    #     nc = 0
    #     nv = 0
    #     for j in i.colors:
    #         if j < ub:
    #             nc += 1
    #
    #     for j in i.edges:
    #         if j.is_colored == 0:
    #             nv += 1
    #
    #     order_of_vertices.append([i, nc, nv])
    #
    # order_of_vertices.sort(key = lambda x: (x[1], -x[2]))
    #
    # v = order_of_vertices[0][0]

    v = vertices[0]

    colors = []

    for i in v.colors:
        if i < ub:
            colors.append(i)

    #v.is_colored = 1

    for c in colors:
        for j in v.edges:
            if c in j.colors:
                j.colors.remove(c)
        v = g.eliminate_vertex(v.get_number())
        ub = min(ub,GCP(g, max(k,c), ub))
        g.add_vertex(v)
        for j in v.edges:
            if c not in j.colors:
                j.colors.append(c)
        # for j in vertices:
        #     if j != v:
        #         j.is_colored = 0

    return ub

p = GCP(G, 0, G.get_nr_of_vertices()+1)
print(p)




