__author__ = "maxime"
__file__ = "tutoratS4.py"
__date__ = "13/02/20"


import numpy as np


def estForteConnexe(G):
    V = G.vertices
    s = 0
    m = ParcoursProfondeur(G, s, [False for i in range(len(V))])
    M = G.matrice
    T = M.T
    G.matrice = T
    m2 = ParcoursProfondeur(G, s, [False for i in range(len(V))])
