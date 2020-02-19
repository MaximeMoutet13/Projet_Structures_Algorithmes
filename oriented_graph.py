__author__ = "maxime"
__file__ = "oriented_graph.py"
__date__ = "04/12/19"


class GraphO(object):
    def __init__(self: 'GraphO', vertices: list, successors: list) -> None:
        self.vertices = vertices
        self.successors = successors
        try:
            self.isGraph()
        except False:
            raise ValueError

    def getVertices(self: 'GraphO') -> list:
        return self.vertices

    def getSuccessors(self: 'GraphO') -> list:
        return self.successors

    def setVertices(self: 'GraphO', liste: list) -> None:
        assert (GraphO(liste, self.getSuccessors()).isGraph())
        self.vertices = liste

    def setSuccessors(self: 'GraphO', liste: list) -> None:
        assert (GraphO(liste, self.getVertices()).isGraph())
        self.successors = liste

    def isGraph(self: 'GraphO') -> bool:
        S = self.getVertices()
        A = self.getSuccessors()
        cond = True

        if len(A) != len(S):
            cond = False

        else:
            for sommet in range(len(S)):
                for j in A[sommet]:
                    if j in S:
                        if sommet not in A[j]:
                            cond = False
                    else:
                        cond = False

        return cond

    def parcoursProfondeur(self):
        S = self.getVertices()
        A = self.getSuccessors()
        Marque = [False for i in range(len(S))]
        pile = []
        pile.append(S[0])
        while len(pile) != 0:
            elmt = pile[0]
            i = S.index(elmt)
            pile = pile[1:]
            if not Marque[i]:
                Marque[i] = True
                pile = A[i] + pile

    def parcoursProfondeurRec(self):
        S = self.getVertices()
        A = self.getSuccessors()
        M = [False for s in range(len(S))]
        s0 = S[0]
        M[s0] = True
        for s in A[s0]:
            if not M[s]:
                vertices = s
                successors = A[s]
                GraphO(vertices, successors).parcoursProfondeurRec()

    def parcoursLargeur(self):
        S = self.getVertices()
        A = self.getSuccessors()
        Marque = [False for i in range(len(S))]
        file = []
        file.append(S[0])
        while len(file) != 0:
            elmt = file[0]
            i = S.index(elmt)
            file = file[1:]
            if not Marque[i]:
                Marque[i] = True
                file = file + A[i]

    def degres(self):
        S = self.getVertices()
        A = self.getSuccessors()
        D = [0 for i in range(len(S))]
        for i, s in enumerate(S):
            for j, s2 in enumerate(A[i]):
                D[j] += 1
