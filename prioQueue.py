__author__ = "maxime"
__file__ = "prioQueue.py"
__date__ = "09/12/19"

from element import*

class PrioQueue():
    def __init__(self, queue):
        self.queue = queue
        assert(self.isPrioQueue(queue))

    def getQueue(self):
        assert not self.isEmpty()
        return self.queue

    def setQueue(self, Q):
        self.queue = Q

    def dequeue(self):
        assert not self.isEmpty()
        l = self.getQueue()
        x = l[0]
        self.setQueue(l[1:])
        return x

    def enqueue(self, elmt: Element):
        v = elmt.getValue()
        p = elmt.getPriority()
        l = self.getQueue()
        if l.isEmpty():
            self.setQueue(elmt)
        else:
            b = False
            for i, x in enumerate(l):
                val = x.getValue()
                prio = x.getPriority()
                if prio > p:
                    l = l[:i] + (prio, val) + l[i:]
                    self.setQueue(l)
                    b = True
                    break
            if not b:
                l.append((p, v))
                self.setQueue(l)

    def isEmpty(self):
        n = len(self.queue)
        if n != 0:
            return False
        return True

    def isPrioQueue(self, queue):
        return queue == queue.spell()
