from graph_generation import*
from time import process_time
import matplotlib.pyplot as plt
import sys
n_range = np.arange(1000, 6000, 1000)

t = np.empty(n_range.size)
for i, n in enumerate(n_range):
    print("Etape:", i)
    t12 = process_time()
    G = generate_random_graph(n, 0.1 * n * (n - 1) / 2)
    print("Temps generation:", process_time() - t12)
    t0 = process_time()
    G.Dijkstra_binary_heap(0)
    t1 = process_time()
    t[i] = t1 - t0
    print("Temps Dijkstra:", t[i])


plt.plot(n_range, t)
plt.xlabel("nb de sommets $n$")
plt.ylabel("temps (s)")
plt.xscale("log")
plt.yscale("log")
plt.grid(True)
plt.title("Compute shortest path with Dijkstra")
plt.savefig("temps_Dijkstra_binary_heap.png")
