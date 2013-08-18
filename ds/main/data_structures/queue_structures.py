from node_class import Node

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


class QueueWithList(object):
    def __init__(self):
        self.storage = []

    def enqueue(self, d):
        self.storage.append(d)

    def dequeue(self):
        try:
            return self.storage.pop(0)
        except:
            return None


def test():
    q = QueueFromList()
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)

    while True:
        i = q.dequeue()
        if not i: break
        else: print i


if __name__ == '__main__':
    test()
