from graph import *
import unittest


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.emptygraph = DirectedGraph.empty_graph()
        self.graph1 = DirectedGraph(
            {0: {1: 10, 3: 5}, 1: {3: 2, 2: 1}, 2: {4: 4}, 3: {1: 3, 2: 9, 4: 2}, 4: {0: 7, 2: 6}})

    def testGetVertices(self):
        G = self.graph1
        G0 = self.emptygraph
        l = list(G.vertices)
        l0 = list(G0.vertices)
        value = [0, 1, 2, 3, 4] == l
        value0 = [] == l0
        self.assertEqual(value, True)
        self.assertEqual(value0, True)

    def testAddVertex(self):
        G0 = self.emptygraph
        G0.add_vertex(0)
        G0.add_vertex(0)
        l = list(G0.vertices)
        value = l == [0]
        self.assertEqual(value, True)

    def testAddEdge(self):
        G0 = self.emptygraph
        G0.add_edge(1, 3, 5)
        G0.add_edge(1, 3, 7)
        l = G0.edges
        value = l == {1: {3: 7}, 3: {}}
        self.assertEqual(value, True)

    def testRemoveEdge(self):
        G = self.graph1
        G.remove_edge(0, 1)
        l = G.edges
        value = l == {0: {3: 5}, 1: {3: 2, 2: 1}, 2: {4: 4}, 3: {1: 3, 2: 9, 4: 2}, 4: {0: 7, 2: 6}}
        self.assertEqual(value, True)
        G.remove_edge(0, 1)
        self.assertEqual(value, True)

    def testChangeWeight(self):
        G = self.graph1
        G.change_weight(0, 1, 5)
        l = G.edges[0][1]
        value = l == 5
        self.assertEqual(value, True)

        try:
            G.change_weight(0, 1, -1)
        except:
            self.assertRaises(KeyError)


# graph = DirectedGraph.empty_graph()
# graph2 = UndirectedGraph.empty_graph()
#
# graph.add_vertex(1)
# graph.add_edge(1, 2, 1)
# print(graph.edges)
# graph.add_edge(2, 1, 1)
# graph.add_edge(2, 3, 1)
#
# graph2.add_edge(1, 3, 5)
# graph2.add_edge(3, 2, 2)
# graph2.add_edge(3, 4, 1)
#
# print("Graph 1:")
# print(graph.vertices)
# print(len(graph))
# print(graph[1])
# print(graph)
#
# for vertex in graph:
#     print(vertex)
#
# graph.remove_edge(1, 2)
# print(graph)
# graph.change_weight(2, 3, 10)
# print(graph)
#
# print("Graph 2:")
# print(graph2)
#
# G = graph.to_networkx()
# plt.figure()
# nx.draw(G, with_labels=True)
# plt.show()
#
# G2 = graph2.to_networkx()
# plt.figure()
# nx.draw(G2, with_labels=True)
# plt.show()
