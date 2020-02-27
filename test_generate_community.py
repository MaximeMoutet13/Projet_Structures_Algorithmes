from graph_generation import *


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


def set_colors(n_nodes_per_community):
    D = dict()
    for i, x in enumerate(n_nodes_per_community):
        for j in range(x):
            D[int(j + np.sum(n_nodes_per_community[:i]))] = i

    return D


nodes_per_community = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
J = generate_random_community_graph(nodes_per_community, 0.9, 0.05)
G = J.to_networkx()
Gcolors = set_colors(nodes_per_community)
some_colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'grey', 'lightblue', 'lightgreen', 'white', 'pink',
               'darkblue', 'darkgreen']
draw_coloring(G, Gcolors, some_colors)
