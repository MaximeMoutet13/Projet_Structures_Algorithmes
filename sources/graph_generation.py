import random
from sources.graph import *


def generate_random_graph(n_nodes, n_edges, directed=False):
    """
        Generate a random connected graph
    """
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


def generate_random_graph_2(n_nodes, n_edges, directed=False):
    """
        Generate a random connected graph using an other method, but this one is too long to be used
    """
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

    e = 0
    G.add_vertex(0)
    for i in range(1, n_nodes):
        G.add_vertex(i)
        k = np.floor((random.random() * (i - 1)))
        G.add_edge(i, k, 1)
        e += 1

    S = set(G.vertices)
    while e != n_edges:
        k1 = np.floor(random.random() * (n_nodes - 1))
        S2 = set(G[k1])
        S2.add(k1)
        Dir = S.difference(S2)
        if len(Dir) == 0:
            break
        k2 = random.sample(Dir, 1)[0]
        G.add_edge(k1, k2, 1)
        e += 1
    return G


def generate_random_community_graph(n_nodes_per_community, p_intra, p_inter):
    """
        Generate a random community graph
    """
    nb_nodes = int(np.sum(n_nodes_per_community))
    g = []
    for i, x in enumerate(n_nodes_per_community):
        G = DirectedGraph.empty_graph()
        for j in range(x):
            G.add_vertex(int(j + np.sum(n_nodes_per_community[:i])))
        g.append(G)

    J = UndirectedGraph.empty_graph()

    for i in range(nb_nodes):
        J.add_vertex(i)

    Visited = set()
    for G in g:
        for s in G:
            for s2 in range(nb_nodes):
                if s2 != s and s2 not in Visited:
                    k = random.random()
                    if s2 in G.edges:
                        if k < p_intra:
                            J.add_edge(s, s2, 1)
                    else:
                        if k < p_inter:
                            J.add_edge(s, s2, 1)
            Visited.add(s)
    return J
