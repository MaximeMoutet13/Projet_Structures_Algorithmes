redditGraph = create_graph(
    "/home/aillet/Bureau/Infromatique/Projet_Structures_Algorithmes/soc-redditHyperlinks-title.tsv")


def top10(subreddit):
    nbr = []
    for i in subreddit:
        nbr += [(i, len(redditGraph[i]))]
    nbr.sort(key=lambda x: x[1], reverse=True)
    return nbr[:10]


print(top10(redditGraph))


def isolated(subreddit):
    nbr = []
    isolated = 0
    for i in subreddit:
        nbr += [(i, len(redditGraph[i]))]
    nbr.sort(key=lambda x: x[1])

    while nbr[isolated][1] == 0:
        isolated += 1

    return isolated


print(isolated((redditGraph)))


def activity_Part_Two_Percent(subreddit):
    max = len(subreddit)
    nbr_links = 0
    two_percent = int((max * 2) / 100)
    nbr_links_two_percent = 0
    activityPartTwoPercent = 0
    nbr = []

    for i in subreddit:
        nbr += [(i, len(redditGraph[i]))]
    nbr.sort(key=lambda x: x[1], reverse=True)

    for i in range(max):
        nbr_links += nbr[i][1]

    for i in range(two_percent):
        nbr_links_two_percent += nbr[i][1]

    activityPartTwoPercent = (100 * nbr_links_two_percent) / nbr_links
    return activityPartTwoPercent


print(activity_Part_Two_Percent(redditGraph))
un, deux = redditGraph.Dijkstra_binary_heap('disney')
print(1)
print(redditGraph.DijkstraPath(deux, 'vegan'))
