from sources.graph_generation import *
import unittest


class TestGenerateGraph(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def testGenerateRandomDirected(self):
        G = generate_random_graph(30, 50, directed=True)
        vertices = len(G)
        edges = 0
        for x in G:
            edges += len(G[x])
        value0 = vertices == 30
        value1 = edges == 50
        self.assertEqual(value0, True)
        self.assertEqual(value1, True)

    def testGenerateRandomUndirected(self):
        G1 = generate_random_graph(5, 4, directed=False)
        G2 = generate_random_graph(200, 19900, directed=False)
        vertices1 = len(G1)
        edges1 = 0
        for x in G1:
            edges1 += len(G1[x])
        value1_0 = vertices1 == 5
        value1_1 = edges1 / 2 == 4
        self.assertEqual(value1_0, True)
        self.assertEqual(value1_1, True)

        vertices2 = len(G2)
        edges2 = 0
        for x in G2:
            edges2 += len(G2[x])
        value2_0 = vertices2 == 200
        value2_1 = edges2 / 2 == 19900
        self.assertEqual(value2_0, True)
        self.assertEqual(value2_1, True)
