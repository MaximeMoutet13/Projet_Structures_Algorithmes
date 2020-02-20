from graph import *

graph = DirectedGraph.empty_graph()
graph2 = UndirectedGraph.empty_graph()

graph.add_vertex(1)
graph.add_edge(1, 2, 1)
graph.add_edge(2, 1, 1)
graph.add_edge(2, 3, 1)

graph2.add_edge(1, 3, 5)
graph2.add_edge(3, 2, 2)
graph2.add_edge(3, 4, 1)

print("Graph 1:")
print(graph.vertices)
print(len(graph))
print(graph[2])
print(graph)

for vertex in graph:
    print(vertex)

graph.remove_edge(1, 2)
print(graph)
graph.change_weight(2, 3, 10)
print(graph)

print("Graph 2:")
print(graph2)

G = graph.to_networkx()
plt.figure()
nx.draw(G, with_labels=True)
plt.show()

G2 = graph2.to_networkx()
plt.figure()
nx.draw(G2, with_labels=True)
plt.show()
