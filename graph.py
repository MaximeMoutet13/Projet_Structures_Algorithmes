class DirectedGraph:
    def __init__(self, edges):
        self.edges = edges
        self.vertices = [i for i in range(len(edges))]

    # @property
    # def vertices(self):
    #     return
    @classmethod
    def empty_graph(cls):
        return cls({})

    def add_vertex(self, v):
        self.edges[v] = {}

    def remove_vertex(self, v):
        del self.edges[v]
        for x in self.edges.values:
            if v in x:
                del x[v]

    def add_edge(self, v1, v2, weight):
        if v1 not in self.edges:
            self.add_vertex(v1)
        if v2 not in self.edges:
            self.add_vertex(v2)
        self.edges[v1][v2] = weight

    def remove_edge(self, v1, v2):
        del self.edges[v1][v2]

    def change_weight(self, v1, v2, w):
        self.edges[v1][v2] = w

    def reset_graph(self):
        self.edges = {}

    def graph_induit(self, vertices):
        G = DirectedGraph.empty_graph()
        e = dict()
        for i, x in enumerate(vertices):
            e[x] = self.edges[x]
        return G

    def __len__(self):
        return len(self.edges)

    def __getitem__(self, key):
        return self.edges[key]

    def __iter__(self):
        return iter(self.edges.items())

    def __str__(self):
        l = ""
        for x in self.edges:
            for y in self.edges[x]:
                l += (str(x) + "->" + str(y) + " // W=" + str(self.edges[x][y]) + "\n")
        return l
