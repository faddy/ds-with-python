# implementing a stack with minimum

import sys
MAX = sys.maxint


class NodeWithMin(object):
    def __init__(self, d):
        self.data = d
        self.minimum = None


class StackWithMin(object):
    def __init__(self):
        self.storage = []

    def push(self, d):
        n = NodeWithMin(d)
        n.minimum = min(self.min_val(), d)
        self.storage.append(n)

    def pop(self):
        if len(self.storage): return self.storage.pop().data
        else: return None

    def min_val(self):
        if len(self.storage): return self.storage[-1].minimum
        else: return MAX
