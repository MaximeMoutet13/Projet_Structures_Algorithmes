__author__ = "maxime"
__file__ = "element.py"
__date__ = "09/12/19"


class Element():
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def getValue(self):
        return self.value

    def getPriority(self):
        return self.priority

    def setValue(self, val):
        self.value = val

    def setPriority(self, prio):
        self.priority = prio
