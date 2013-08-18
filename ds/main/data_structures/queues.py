
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



