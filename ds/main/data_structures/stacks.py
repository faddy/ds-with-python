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


def test():
    s=Stack()
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())

if __name__ == '__main__':
    test()
