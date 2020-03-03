__author__ = "maxime"
__file__ = "temps_Dijkstra.py"
__date__ = "20/02/2020"

from graph_generation import *
from time import process_time, perf_counter

n_range = 2 ** np.arange(2, 10)

t = np.empty(n_range.size)
for i, n in enumerate(n_range):
    G = generate_random_graph(n, n * (n - 1) / 2)
    t0 = process_time()
    G.Dijsktra(0)
    t1 = process_time()
    t[i] = t1 - t0


plt.plot(n_range, t)
plt.xlabel("nb de sommets $n$")
plt.ylabel("temps (s)")
plt.xscale("log")
plt.yscale("log")
plt.grid(True)
plt.title("Compute shortest path with Dijkstra")
plt.savefig("test2.png")
