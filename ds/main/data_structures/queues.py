
from data_structures.linked_lists import Node


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        if item is None: return
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class QueueWithLinkedList(object):
    def __init__(self):
        self.front = None
        self.end = None

    def enqueue(self, d):
        if not self.end:
            self.front = self.end = Node(d)
        else:
            self.end.nxt = Node(d)
            self.end = self.end.nxt

    def dequeue(self):
        if not self.front:
            return None
        else:
            item = self.front
            self.front = self.front.nxt
            return item.data


