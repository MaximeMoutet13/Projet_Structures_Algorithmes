# Graphs represented with adjacency lists__author__ = 'lugiez'
__Filename__ = 'graph'
__Creationdate__ = '29/08/18'


# Implementation of graph with adjacency lists

class Graph():

    # vertices is the list of vertices
    # len(vertices) = n is the number of vertices of the graph
    # and vertices [i] = i for i= 0, ... n - 1
    # successors[i] is the list of the  successors of vertex i

    def __init__(self, vertices, successors):
        self.vertices = vertices
        self.successors = successors

    def getVertices(self):
        return self.vertices

    def getSuccessors(self):
        return self.successors

    def setVertices(self, vertices):
        self.vertices = vertices

    def setSuccessors(self, edges):
        self.successors = edges

    def depthFirstSearch1(self, vertex, marks):
        if not marks[vertex]:
            marks[vertex] = True
            print(vertex)
            sucessors = self.getSuccessors()(vertex)
            for v in sucessors:
                self.depthFirstSearch1(v, marks)

    def depthFirstSearch2(self, vertex, marks):
        result = []
        marks[vertex] = True
        result.append(vertex)
        successors = self.getSuccessors()[vertex]
        for v in successors:
            if not marks[v]:
                result += self.depthFirstSearch2(v, marks)
        return result

    def search(self):
        marks = [False for v in self.vertices]
        vertices = self.getVertices()
        result = []
        for v in vertices:
            if not marks[v]:
                result += self.depthFirstSearch2(v, marks)
        return result
