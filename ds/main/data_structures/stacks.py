
from data_structures.linked_lists import Node


class Stack(object):
    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def push(self, item):
        if item is None: return
        self.data.append(item)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()

    def peek(self):
        if not self.is_empty():
            return self.data[-1]

    def size(self):
        return len(self.data)

    def __repr__(self):
        return ', '.join([str(i) for i in self.data])


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

