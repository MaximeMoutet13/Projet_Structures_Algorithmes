__author__ = "maxime"
__file__ = "test_dijkstra.py"
__date__ = "19/02/2020"

import time
from graph_generation import *

G = generate_random_graph(1000, 3000)
d = time.process_time()
l1 = G.Dijsktra(0)
d2 = time.process_time()
l2 = G.Dijkstra_binary_heap(0)
d3 = time.process_time()
assert (l1 == l2)

G = generate_random_community_graph([3, 3, 3], 0.8, 0)

l1 = G.Dijsktra(0)
l2 = G.Dijkstra_binary_heap(0)
assert (l1 == l2)

# print(d2 - d, d3 - d2)
