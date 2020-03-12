__author__ = "maxime"
__file__ = "stats.py"
__date__ = "12/03/2020"

from sources.graph_generation import *
from time import process_time

nb_sommets = [500 * i for i in range(1, 11)]
t = []
percent = 0.2
print(nb_sommets)
print(t)

for i, v in enumerate(nb_sommets):
    print("Etape:", i)
    g = generate_random_graph(v, percent * v ** 2, directed=False)
    tj = []
    for k in range(20):
        s1, s2 = np.floor(random.random() * v), np.floor(random.random() * v)

        t0 = process_time()
        d, c = g.Dijkstra_from_u_to_v(s1, s2)
        t1 = process_time()

        tj.append(t1 - t0)

    t.append(tj)


moyenne = []
medianne = []
maximum = []
minimum = []

for x in t:
    moyenne.append(np.mean(x))
    medianne.append(np.median(x))
    maximum.append(np.amax(x))
    minimum.append(np.amin(x))

plt.plot(nb_sommets, moyenne, label="temps moyen")
plt.plot(nb_sommets, maximum, label="temps maximum")
plt.plot(nb_sommets, minimum, label="temps minimum")
plt.plot(nb_sommets, medianne, label="temps median")

axes = plt.gca()
plt.xlabel("nb de sommets $n$", fontsize=20)
plt.ylabel("Temps (s)", fontsize=20)
axes.set_ylim(0, 2)


plt.grid(True)
plt.legend()


# Renommer le fichier !!!
plt.title(r"Statistiques Dijkstra, $0.2*n^2$")
plt.savefig("stats.png")
