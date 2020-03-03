from sources.graph_generation import*
from time import process_time

n_range = 2 ** np.arange(2, 10)

t = np.empty(n_range.size)
for i, n in enumerate(n_range):
    G = generate_random_graph(n, n * (n - 1) / 2)
    J = G.to_networkx()
    t0 = process_time()
    nx.shortest_path_length(J, 0)
    t1 = process_time()
    t[i] = t1 - t0

plt.plot(n_range, t)
plt.xlabel("nb de sommets $n$")
plt.ylabel("temps (s)")
plt.xscale("log")
plt.yscale("log")
plt.grid(True)
plt.title("Compute shortest path with networkx")
plt.savefig("test2.png")
