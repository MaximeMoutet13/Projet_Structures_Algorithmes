from sources.graph_generation import *
from time import process_time

n = [i * 1000 for i in range(1, 11)]
edges_percent = 0.2
t_Dijkstra = []
t_binary_heap = []
t_networkx = []

# nous avons décidé de ne pas inclure l'algorithme de Bellman Ford qui semblaient etre très long
# meme pour des "petits" graphes


for i, v in enumerate(n):
    print("Etape i:", i)
    G = generate_random_graph(v, edges_percent * v ** 2, directed=True)
    t0 = process_time()
    G.Dijkstra(0)
    t1 = process_time()
    t_Dijkstra.append(t1 - t0)

    t2 = process_time()
    G.Dijkstra_binary_heap(0)
    t3 = process_time()
    t_binary_heap.append(t3 - t2)

    J = G.to_networkx()
    t4 = process_time()
    nx.shortest_path_length(J, source=0)
    t5 = process_time()
    t_networkx.append(t5 - t4)


plt.plot(n, t_Dijkstra, label="Dijkstra")
plt.plot(n, t_binary_heap, label="Binary heaps")
plt.plot(n, t_networkx, label="Networkx")
plt.xlabel("nb de sommets $n$", fontsize=20)
plt.ylabel("Temps (s)", fontsize=20)
plt.grid(True)
plt.legend()


# Renommer le fichier !!!
plt.title(r"Dijkstra, edges=0.3n^2")
plt.savefig("temps_all_dijkstra.png")
