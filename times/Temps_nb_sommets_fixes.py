'missouripolitics'

from sources.graph_generation import *
from time import process_time

n = np.linspace(10,45,36)
print(n)
n /= 100
edges_percent = 0.3
t_Dijkstra = []
t_binary_heap = []
t_networkx = []

# Renommer l'image enregistrée avant de lancer le programme !!

# nous avons décidé de ne pas inclure l'algorithme de Bellman Ford qui semblaient etre très long
# meme pour des "petits" graphes
nb_sommet = 2000

for i,v in enumerate(n):
    print('étape',i)
    G = generate_random_graph(nb_sommet, v * nb_sommet ** 2, directed=False)
    t0 = process_time()
    G.Dijkstra(0)
    t1 = process_time()
    t_Dijkstra.append(t1 - t0)
    print(4)
    t2 = process_time()
    G.Dijkstra_binary_heap(0)
    t3 = process_time()
    t_binary_heap.append(t3 - t2)
    print(5)
    J = G.to_networkx()
    t4 = process_time()
    nx.shortest_path_length(J, 0)
    t5 = process_time()
    t_networkx.append(t5 - t4)
    print(6)

plt.plot(n, t_Dijkstra, label="Dijkstra")
plt.plot(n, t_binary_heap, label="Binary heaps")
plt.plot(n, t_networkx, label="Networkx")
plt.xlabel("alpha ", fontsize=20)
plt.ylabel("Temps(s) pour graph à 2000 sommets", fontsize=20)
plt.grid(True)
plt.legend()
plt.show()


# Renommer le fichier !!!
# plt.title(r"Dijkstra, edges=0.3n^2")
# plt.savefig(nsoqm)