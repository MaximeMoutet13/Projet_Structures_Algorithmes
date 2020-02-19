__author__ = "maxime"
__file__ = "draws.py"
__date__ = "21/01/20"

import networkx as nx
from graph_S4 import *
import matplotlib.pyplot as plt

M = generate(30, 29)
G = nx.from_dict_of_lists(M)
plt.figure()
nx.draw(G, with_labels=True)
plt.show()

l = degeneracy_order(G)
color, k = coloring(G, l)


def draw_coloring(G, coloring, colors):
    """
    Draw the graph G and colors the vertices
    :param G: a connected graph
    :param coloring: a dictionary with vertices in keys and a number (which represents a color) in value
    :param colors: a list of colors (str)
    :return: return the figure with the colored graph
    """
    fig = plt.figure()
    n_colors = len(colors)

    pos = nx.spring_layout(G)
    for i in range(n_colors):
        nx.draw_networkx_nodes(G, pos, [x for x in G.nodes() if coloring[x] == i], node_color=colors[i])
        nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

    plt.axis('off')
    plt.show()
    return fig


some_colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'grey']
draw_coloring(G, color, some_colors)
