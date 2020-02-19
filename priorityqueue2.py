__author__ = 'lugiez'
__Filename__ = 'priorityQueue2'
__Creationdate__ = '13/12/2019'

from elt import *

#file d'attente à priorité
#avec utilisation d'un attribut pour le nb d'éléments
#cet attribut est utile pour les files d'attente à priorité
#de capacité bornée pour lesquelles l'attribut queue a une
#longueur fixe qui est la dimension maximale de la file

class PriorityQueue2():

    def __init__(self):
        self.nbelt = 0
        self.queue = []

    #getters et setters
    def getQueue(self):
        return self.queue

    def setQueue(self, queue):
        self.queue = queue

    def getNbElt(self):
        return self.nbelt

    def setNbElt(self, value):
        assert(value >= 0)
        self.nbelt = value

    #tester vide
    def isEmpty(self):
        return self.nbelt == 0

    #enlever de la file
    def dequeue(self):
        assert(not self.isEmpty())
        self.nbelt += -1
        value = self.queue[0]
        self.queue = self.queue[1:]
        return value

    #ajouter un élément dans la file
    def enqueue(self, elt):
        if self.isEmpty():
            self.setQueue([elt])
        else:
            index = 0
            queue = self.getQueue()
            for qelt in queue:
                if qelt.getPriority() >= elt.getPriority():
                    index += 1
                else:
                    break
            self.setQueue( queue[:index] + [elt] + queue[index:])
        self.nbelt += 1
