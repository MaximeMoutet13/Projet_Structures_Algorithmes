from graph import*


graph = DirectedGraph.empty_graph()

graph.add_vertex(1)
graph.add_edge(1, 2, 1)
graph.add_edge(2, 1, 1)
graph.add_edge(2, 3, 1)

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


G = graph.to_networkx()
plt.figure()
nx.draw(G, with_labels=True)
plt.show()
