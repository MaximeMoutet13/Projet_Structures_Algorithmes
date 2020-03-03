from sources.graph_generation import *
import unittest


class TestDijkstra(unittest.TestCase):
    def setUp(self) -> None:

        self.emptygraph = DirectedGraph.empty_graph()
        self.G1 = DirectedGraph(
            {0: {1: 10, 3: 5}, 1: {3: 2, 2: 1}, 2: {4: 4}, 3: {1: 3, 2: 9, 4: 2}, 4: {0: 7, 2: 6}})
        self.G2 = DirectedGraph(
            {0: {1: 10, 3: 5}, 1: {3: 2}, 2: {}, 3: {1: 3, 4: 2}, 4: {0: 7}})

    def testDijkstra(self):
        G = self.G1
        dist0, pred0 = G.Dijsktra(0)
        l = {0: 0, 1: 8, 2: 9, 3: 5, 4: 7}
        value0 = l == dist0
        self.assertEqual(value0, True)

        dist1, pred1 = G.Dijkstra_binary_heap(0)
        value1 = l == dist1
        self.assertEqual(value1, True)

    def testDijkstraEmpty(self):
        G = self.emptygraph
        try:
            dist, pred = G.Dijsktra(0)
        except:
            self.assertRaises(KeyError)

    def testDijkstraNonConnexe(self):
        G = self.G2
        dist0_0, pred0_0 = G.Dijsktra(0)
        dist0_1, pred0_1 = G.Dijkstra_binary_heap(0)
        l0 = {0: 0, 1: 8, 2: float("inf"), 3: 5, 4: 7}
        value0_0 = l0 == dist0_0
        value0_1 = l0 == dist0_1
        self.assertEqual(value0_0, True)
        self.assertEqual(value0_1, True)

        dist1_0, pred1_0 = G.Dijsktra(2)
        dist1_1, pred1_1 = G.Dijkstra_binary_heap(2)
        l1 = {0: float("inf"), 1: float("inf"), 2: 0, 3: float("inf"), 4: float("inf")}
        value1_0 = l1 == dist1_0
        value1_1 = l1 == dist1_1
        self.assertEqual(value1_0, True)
        self.assertEqual(value1_1, True)

    def testDijkstraFromUtoV(self):
        G = self.G1
        d, p = G.Dijkstra_from_u_to_v(0, 2)
        value = d == 9
        self.assertEqual(value, True)
