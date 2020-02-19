__author__ = "maxime"
__file__ = "graph.py"
__date__ = "29/11/19"


class Graph(object):
    def __init__(self: 'Graph', vertices: list, successors: list) -> None:
        self.vertices = vertices
        self.successors = successors
        assert(self.isGraph())

    def getVertices(self: 'Graph') -> list:
        return self.vertices

    def getSuccessors(self: 'Graph') -> list:
        return self.successors

    def setVertices(self: 'Graph', liste: list) -> None:
        assert (Graph(liste, self.getSuccessors()).isGraph())
        self.vertices = liste

    def setSuccessors(self: 'Graph', liste: list) -> None:
        assert (Graph(self.getVertices(), liste).isGraph())
        self.successors = liste

    def isGraph(self: 'Graph') -> bool:
        S = self.getVertices()
        A = self.getSuccessors()
        cond = True

        if len(A) != len(S):
            cond = False

        else:
            for s in range(len(S)):
                for j in range(len(S)):
                    if (s in A[j]) != (j in A[s]):
                        cond = False
        return cond

    def searchConnexe(self):
        elmt = []
        S = self.getVertices()
        A = self.getSuccessors()
        Marque = [False for i in range(len(S))]
        pile = [i for i in range(len(S))]
        while len(pile) != 0:
            if not Marque[pile[0]]:
                elmt += S[pile[0]]
                Marque[pile[0]] = True
                pile = A[pile[0]] + pile[1:]
            else:
                pile = pile[1:]
        print(elmt)

    def depthSearchConnexe(self, i, marks):
        if not marks[i]:
            marks[i] = True
            print(self.getVertices()[i])
            for j in self.getSuccessors()[i]:
                self.depthSearchConnexe(j, marks)

    def depthSearchNonConnexe(self):
        marks = [False for i in range(len(self.getVertices()))]
        for i in range(len(self.getVertices())):
            if not marks[i]:
                self.depthSearchConnexe(i, marks)

    def degres(self):
        S = self.getVertices()
        A = self.getSuccessors()
        D = [0 for i in range(len(S))]
        for i, s in enumerate(S):
            for j, s2 in enumerate(A[i]):
                D[j] += 1

    def estForteConnexe(self):

# marks = [False for i in range(9)]
# G = Graph(['1', '2', '3', '4', '5', '6', '7', '8', '9'], [[1, 2, 4, 5], [0, 2, 3, 7], [0, 1, 5, 6], [1, 7, 8], [0, 7], [0, 2, 6], [2, 5], [1, 3, 4], [3]])
# print(G.isGraph())
# G.searchConnexe()

# H = Graph(['1', '2', '3', '4', '5', '6', '7', '8', '9'], [[2, 4, 5], [2], [0, 1, 5, 6], [7, 8], [0], [0, 2, 6], [2, 5], [3], [3]])
# H.depthSearchNonConnexe()