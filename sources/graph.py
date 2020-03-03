import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import heapq


class DirectedGraph:
    def __init__(self, edges):
        self.edges = edges

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, d):
        if isinstance(d, dict):
            for v in d.values():
                for w in v.values():
                    if w <= 0:
                        raise ValueError
            self.__edges = d

    @property
    def vertices(self):
        return self.edges.keys()

    @classmethod
    def empty_graph(cls):
        return cls({})

    def add_vertex(self, v):
        self.edges[v] = {}

    def remove_vertex(self, v):
        for s in self:
            try:
                del s[v]
            except KeyError:
                pass
        del self.edges[v]

    def add_edge(self, v1, v2, weight):
        if v1 not in self.edges:
            self.add_vertex(v1)
        if v2 not in self.edges:
            self.add_vertex(v2)
        self.edges[v1][v2] = weight

    def remove_edge(self, v1, v2):
        try:
            del self.edges[v1][v2]
        except KeyError:
            pass

    def change_weight(self, v1, v2, w):
        self.edges[v1][v2] = w

    def reset(self):
        self.edges = {}

    def graph_induit(self, G, vertices):
        G2 = DirectedGraph.empty_graph()
        e = dict()
        for i, x in enumerate(vertices):
            e[x] = G.edges[x]
        G2.edges = e
        return G2

    def __len__(self):
        return len(self.edges)

    def __getitem__(self, key):
        return self.edges[key]

    def __iter__(self):
        return iter(self.edges.keys())

    def __str__(self):
        l = ""
        for x in self.edges:
            for y in self.edges[x]:
                l += (str(x) + "->" + str(y) + " // W=" + str(self.edges[x][y]) + "\n")
        if len(l) == 0:
            l = "empty graph"
        return l

    def to_networkx(self):
        d = self.edges
        return nx.Graph(d, create_using=nx.DiGraph)

    def Dijsktra(self, u):
        F = set(self.edges)
        dist = dict()
        pred = dict()
        for i in self:
            dist[i] = float('inf')
            pred[i] = None
        dist[u] = 0
        while len(F) != 0:
            min = float("inf")
            s = 0
            for x in F:
                if dist[x] <= min:
                    min = dist[x]
                    s = x
            u = s
            F.remove(u)
            S = set(self.edges[u])
            for x in S.intersection(F):
                if dist[u] + self.edges[u][x] < dist[x]:
                    dist[x] = dist[u] + self.edges[u][x]
                    pred[x] = u
        return dist, pred

    @staticmethod
    def DijkstraPath(pred, t):
        path = []
        u = t
        while pred[u] != None:
            path = [u] + path
            u = pred[u]
        return path

    def Dijkstra_binary_heap(self, u):
        F = set(self.vertices)
        queue = []
        dist = dict()
        pred = dict()
        for i in self:
            dist[i] = float('inf')
            pred[i] = None
        dist[u] = 0
        for x in range(len(self.edges)):
            if x != u:
                heapq.heappush(queue, (float("inf"), x))
        heapq.heappush(queue, (0, u))
        while len(F) != 0:
            d, u = heapq.heappop(queue)
            F.discard(u)
            S = set(self.edges[u])
            for x in S.intersection(F):
                if d + self.edges[u][x] < dist[x]:
                    dist[x] = dist[u] + self.edges[u][x]
                    heapq.heappush(queue, (dist[x], x))
                    pred[x] = u
        return dist, pred

    def Dijkstra_from_u_to_v(self, u, v):
        F = set(self.edges)
        queue = []
        dist = [float("inf") for j in range(len(self.edges))]
        pred = [None for j in range(len(self.edges))]
        dist[u] = 0
        for x in range(len(self.edges)):
            if x != u:
                heapq.heappush(queue, (float("inf"), x))
        heapq.heappush(queue, (0, u))
        while u != v:
            d, u = heapq.heappop(queue)
            F.discard(u)
            S = set(self.edges[u])
            for x in S.intersection(F):
                if d + self.edges[u][x] < dist[x]:
                    dist[x] = dist[u] + self.edges[u][x]
                    heapq.heappush(queue, (dist[x], x))
                    pred[x] = u
        return dist[v], pred


class UndirectedGraph(DirectedGraph):
    def __int__(self, edge):
        super().__init__(edge)

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self.vertices:
            self.add_vertex(vertex2)

        self.edges[vertex1][vertex2] = weight
        self.edges[vertex2][vertex1] = weight

    def remove_edge(self, vertex1, vertex2):
        try:
            del self.edges[vertex1][vertex2]
            del self.edges[vertex1][vertex2]
        except KeyError:
            pass

    def change_weight(self, v1, v2, w):
        self.edges[v1][v2] = w
        self.edges[v2][v1] = w

    def __str__(self):
        l = "V = "
        V = list(self.vertices)
        l += str(V)
        l += "     E = "
        E = []
        for x in self.edges:
            for y in self.edges[x]:
                E += [[x, y, self.edges[x][y]]]
        l += str(E)
        return l
