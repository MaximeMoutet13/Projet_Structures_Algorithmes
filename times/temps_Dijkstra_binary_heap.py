from sources.graph_generation import*
from time import process_time
import matplotlib.pyplot as plt

n = [i * 1000 for i in range(1, 11)]
t_Dijkstra = []
t_Generate = []

for i, node in enumerate(n):
    print("Etape:", i)
    t0 = process_time()
    G = generate_random_graph_2(node, 0.1 * node * (node - 1) / 2, directed=False)
    t_Generate.append(process_time() - t0)
    t1 = process_time()
    G.Dijkstra_binary_heap(0)
    t_Dijkstra.append(process_time() - t1)

plt.figure()
plt.plot(n, t_Dijkstra)
plt.xlabel("nb de sommets $n$")
plt.ylabel("temps (s)")
plt.xscale("log")
plt.yscale("log")
plt.grid(True)
plt.title("Compute shortest path with Dijkstra")
# plt.savefig("temps_Dijkstra_binary_heap.png")


plt.figure()
plt.plot(n, t_Generate)
plt.xlabel("nb de sommets $n$")
plt.ylabel("temps (s)")
plt.xscale("log")
plt.yscale("log")
plt.grid(True)
plt.title("Generate random graph with 0.1 * max_edges with second method")
plt.savefig("imTemps_generate2.png")
