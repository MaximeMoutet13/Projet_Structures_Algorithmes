__author__ = "maxime"
__file__ = "graph_generation.py.py"
__date__ = "19/02/20"

import random
from graph import *


def generate_random_graph(n_nodes, n_edges, directed=False):
    if n_edges < n_nodes - 1:
        raise ValueError
    if n_nodes == 0:
        return dict()
    if directed:
        if n_edges > n_nodes * (n_nodes - 1):
            raise ValueError
    else:
        if n_edges > n_nodes * (n_nodes - 1) / 2:
            raise ValueError

    if directed:
        G = DirectedGraph.empty_graph()
    else:
        G = UndirectedGraph.empty_graph()

    V = []  # visited vertices
    N = [i for i in range(n_nodes)]  # not visited vertices
    e = 0

    s0 = random.choice(N)  # initial vertice
    V.append(s0)
    N.remove(s0)

    while len(N) != 0:
        s1 = random.choice(V)
        s2 = random.choice(N)
        G.add_edge(s1, s2, 1)
        V.append(s2)
        N.remove(s2)
        e += 1

    while e != n_edges:
        s1, s2 = random.choice(V), random.choice(V)
        if (s1 != s2) and (s2 not in G[s1]):
            G.add_edge(s1, s2, 1)
            e += 1

    return G


# def generate_random_community_graph(n_nodes_per_community, p_intra, p_inter):
#     nb_community = len(n_nodes_per_community)
#
#     g = []
#     for c in range(nb_community):
#         for n in range(n_nodes_per_community[c]):


