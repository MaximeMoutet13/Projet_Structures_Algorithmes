from sources.graph_generation import *
from time import process_time

n = [i * 1000 for i in range(1, 11)]
edges_percent = 0.2
t_Dijkstra = []
t_binary_heap = []
t_networkx = []


for i, v in enumerate(n):
    print("Etape i:", i)
    G = generate_random_graph(v, edges_percent * v * (v - 1) / 2, directed=False)
    t0 = process_time()
    G.Dijsktra(0)
    t1 = process_time()
    t_Dijkstra.append(t1 - t0)

    t2 = process_time()
    G.Dijkstra_binary_heap(0)
    t3 = process_time()
    t_binary_heap.append(t3 - t2)

    J = G.to_networkx()
    t4 = process_time()
    nx.shortest_path_length(J, 0)
    t5 = process_time()
    t_networkx.append(t5 - t4)


plt.plot(n, t_Dijkstra, label="Dijkstra")
plt.plot(n, t_binary_heap, label="Binary heaps")
plt.plot(n, t_networkx, label="Networkx")
plt.xlabel("nb de sommets $n$")
plt.ylabel("temps (s)")
plt.xscale("log")
plt.yscale("log")
plt.grid(True)
plt.legend()


# Renommer le fichier !!!
plt.title("Dijkstra, 0.2 * max_edges")
plt.savefig("imTemps_all_Dijkstra.png")
