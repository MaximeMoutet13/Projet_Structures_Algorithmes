__author__ = 'lugiez'
__Filename__ = 'fileprio'
__Creationdate__ = '07/12/2019'

from typing import *
from elt import *

#Réalisation de file d'attente à priorité
#en utilisant les listes python
#les éléments sont rangés par priorité décroissante


class PriorityQueue():

    def __init__(self):
        self.queue = []

#getters et setters
    def getQueue(self: 'PriorityQueue') -> List:
        return self.queue

    def setQueue(self: 'PriorityQueue', queue: List) -> None:
        self.queue = queue

#test si la file est vide
    def isEmpty(self: 'PriorityQueue') ->bool:
        return self.getQueue() == []

#enlever la tete de la file si non vide
    def dequeue(self: 'PriorityQueue') -> 'Elt':
        assert (not self.isEmpty())
        queue = self.getQueue()
        self.setQueue(queue[1:])
        return queue[0]

#ajouter en queue de file
    def enqueue(self: 'PriorityQueue', elt: 'Elt') -> None:
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
