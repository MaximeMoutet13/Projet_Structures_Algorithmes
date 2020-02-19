__author__ = "maxime"
__file__ = "test_dijkstra.py"
__date__ = "19/02/2020"


from graph_generation import*

G = generate_random_graph(20, 40)
l1 = G.Dijsktra(0)
print(l1)
l2 = G.Dijkstra_binary_heap(0)
print(l2)
assert(l1 == l2)
