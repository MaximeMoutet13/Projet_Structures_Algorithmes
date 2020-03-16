from sources.graph_generation import*
from time import process_time

n = [i * 1000 for i in range(1, 11)]
t = []
percent_edges = 0.1

# Renommer l'image enregistrée avant de lancer le programme !!

for i, v in enumerate(n):
    print("Etape:", i)
    G = generate_random_graph(v, 0.1 * v * (v - 1) / 2, directed=False)
    J = G.to_networkx()
    t0 = process_time()
    nx.shortest_path_length(J, 0)
    t1 = process_time()
    t.append(t1 - t0)

plt.plot(n, t)
plt.xlabel("nb de sommets $n$")
plt.ylabel("temps (s)")
plt.xscale("log")
plt.yscale("log")
plt.grid(True)

# Renommer le fichier !!!
plt.title("Dijkstra networkx, 0.1 * max_edges")
plt.savefig("imTemps_Dijkstra_Networkx.png")
