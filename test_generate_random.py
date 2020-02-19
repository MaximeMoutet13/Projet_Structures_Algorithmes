from graph_generation import *


def test(G, nb_nodes, nb_edges, directed):
    assert (len(G) == nb_nodes)
    nb = 0
    for x in G:
        nb += len(G[x])
    if not directed:
        nb /= 2
    assert (nb == nb_edges)


G1 = generate_random_graph(5, 4)
test(G1, 5, 4, False)
G2 = generate_random_graph(200, 19900, False)
test(G2, 200, 19900, False)
G3 = generate_random_graph(30, 50, True)
test(G3, 30, 50, True)
