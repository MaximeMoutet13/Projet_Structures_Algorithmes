__Author__ = "aillet"
__Filename__ = "test_graph"
__Creationdate__ = "19/02/2020"
import graph.py


graph = DirectedGraph()
graph.add_vertex(1)
graph.add_edge(1,2,1)
graph.add_edge(2,1,1)
graph.add_edge(2,3,1)

print(graph.vertices)
print(len(graph))
print(graph[2])
print(graph)


for vertex in graph:
    print(vertex)


graph.remove_edge(1,2)
print(graph)