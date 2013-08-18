from node_class import Node


class StackWithList(object):
    def __init__(self):
        self.storage = []

    def push(self, d):
        self.storage.append(d)

    def pop(self):
        if len(self.storage): return self.storage.pop()
        else: return None

    def peek(self):
        if not len(self.storage): return None
        else: return self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0


class StackWithLinkedList(object):
    def __init__(self):
        self.top = None

    def pop(self):
        if not self.top: return None
        else:
            item = self.top
            self.top = self.top.nxt
            return item.data

    def push(self):
        if not self.top:
            self.top = Node(data)
        else:
            n = Node(data)
            n.nxt = self.top
            self.top = n


def test():
    s = StackWithList()
    s.push(4)
    s.push('asd')

    print s.pop()
    print s.pop()
    print s.pop()

