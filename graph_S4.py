__author__ = "maxime"
__file__ = "graph_S4.py"
__date__ = "14/01/20"

import random


def generate(vertices, edges):
    """
    Generate a connected graph with a defined number of vertices and edges
    :param vertices: number of vertices
    :param edges: number of edges
    :return: a dictionary with vertices in keys and a set with their neighbours in value
    """
    if edges < vertices - 1:
        return ValueError
    if vertices == 0:
        return dict()
    D = dict()
    for i in range(vertices):
        D[i] = set()
    V = []  # visited vertices
    N = [i for i in range(vertices)]  # not visited vertices
    e = 0

    s0 = random.choice(N)  # initial vertice
    V.append(s0)
    N.remove(s0)

    while len(N) != 0:
        s1 = random.choice(V)
        s2 = random.choice(N)
        D[s1].add(s2)
        D[s2].add(s1)
        V.append(s2)
        N.remove(s2)
        e += 1

    while e != edges:
        s1, s2 = random.choice(V), random.choice(V)
        if (s1 != s2) and (s1 not in D[s2]):
            D[s1].add(s2)
            D[s2].add(s1)
            e += 1
    return D


def coloring(G, order):
    """
    Color the graph G following the given order
    :param G: connected graph
    :param order: order of coloration
    :return: a dictionary with vertices in keys and their color as an integer in value and the number of colors used
    """
    V = len(G)
    color = {}
    for i in range(V):
        color[i] = -1

    available = {i for i in range(V)}
    for s in order:
        for s2 in G[s]:
            available.discard(color[s2])
        color[s] = min(available)
        available = {i for i in range(V)}
    k = max(color.values()) + 1
    return color, k


def degree(G):
    """
    :param G: connected graph
    :return: dictionary with vertices in keys and their degree in values
    """
    D = dict()
    for s in range(len(G)):
        D[s] = len(G[s])
    return D


def degeneracy_order(G):
    """
    :param G: connected graph
    :return: degeneracy order in a list
    """

    order = []
    vertice = {i for i in range(len(G))}
    deg = degree(G)
    while len(vertice) != 0:
        min = float('inf')
        s = 0
        for s1 in vertice:
            if deg[s1] < min:
                min = deg[s1]
                s = s1
        order = [s] + order
        for s2 in G[s]:
            deg[s2] -= 1
        vertice.remove(s)
    return order
