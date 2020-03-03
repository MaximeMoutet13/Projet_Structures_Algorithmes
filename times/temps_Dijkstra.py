__author__ = "maxime"
__file__ = "temps_Dijkstra.py"
__date__ = "20/02/2020"

from sources.graph_generation import *
from time import process_time

n = [i * 1000 for i in range(1, 11)]
edges_percent = 0.1
t = []
for i, v in enumerate(n):
    print("Etape i:", i)
    G = generate_random_graph(v, edges_percent * v * (v - 1) / 2, directed=False)
    t0 = process_time()
    G.Dijsktra(0)
    t1 = process_time()
    t.append(t1 - t0)


plt.plot(n, t)
plt.xlabel("nb de sommets $n$")
plt.ylabel("temps (s)")
plt.xscale("log")
plt.yscale("log")
plt.grid(True)


# Renommer le fichier !!!
plt.title("Dijkstra, 0.1 * max_edges")
plt.savefig("imTemps_Dijkstra.png")
