__author__ = "maxime"
__file__ = "graph_mat.py"
__date__ = "04/12/19"

import numpy as np


class GraphMat(object):
    def __init__(self: 'GraphMat', matrix: np.array) -> None:
        self.matrix = matrix
        assert (self.isGraph())

    def getMatrix(self: 'GraphMat') -> np.array:
        return self.matrix

    def setMatrix(self: 'GraphMat', mat: np.array) -> None:
        assert (GraphMat(mat).isGraph())
        self.matrix = mat

    def isGraph(self: 'GraphMat') -> bool:
        M = self.getMatrix()
        cond = True
        n, m = M.shape
        if n != m:
            cond = False
        else:
            for i in range(n):
                for j in range(m):
                    if M[i, j] != M[j, i]:
                        cond = False
        return cond

    def depthSearchConnexe(self, i, marks, l=[]):
        if not marks[i]:
            marks[i] = True
            l.append(i)
            M = self.getMatrix()
            for j in range(M.shape[0]):
                if M[i, j] != 0:
                    self.depthSearchConnexe(j, marks, l)
        return l

    def depthSearchNonConnexe(self):
        marks = [False for i in range(self.getMatrix().shape[0])]
        for i in range(self.getMatrix().shape()[0]):
            if not marks[i]:
                self.depthSearchConnexe(i, marks)

    def estFortConnexe(self):
        M = self.getMatrix()
        s = 0
        l1 = self.depthSearchConnexe(s, [False for i in range(M.shape[0])])
        M = M.T
        l2 = self.depthSearchConnexe(s, [False for i in range(M.shape[0])])
        if len(l1) == len(l2) == M.shape[0]:
            return True
        return False


M = np.array(
    [[0, 1, 1, 0, 1, 1, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 1, 0],
     [1, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0]])

G = GraphMat(M)
print(G.depthSearchConnexe(0, [False, False, False, False, False, False, False, False, False]))
print(G.estFortConnexe())

M = np.array([[]])